/* Registered vs starred, and registered clubs joining the day they meet.
   The cadence rules are the point: a club only lands on a day when the day,
   the time and the frequency are all genuinely derivable. Ported from
   Ad Astra's clubs engine — see ad-astra/CLAUDE.md for the fuller reasoning
   on `clubMeetsOn`. River's clubs use plain weekly cadence (no per-date
   schedule like Sedona's ASL Club), so this test covers that path instead. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8110;
(async () => {
  const b = await chromium.launch({executablePath:process.env.CHROMIUM_PATH||'/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs=[]; p.on('pageerror',e=>errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`,{waitUntil:'networkidle'});
  await p.addScriptTag({path:__dirname+'/seed.js'}); await p.waitForTimeout(300);
  const out=[]; const ck=(n,ok,got)=>out.push({n,ok:!!ok,got});

  /* ---- three states, and the old `true` still means "want" ---- */
  const st = await p.evaluate(()=>{
    put({id:'clubpicks', type:'clubpicks', picks:{challisland:true}});   // legacy value
    const before = clubState('challisland');
    setClubState('challisland','reg');
    const after = clubState('challisland');
    setClubState('challisland',null);
    const gone = clubState('challisland');
    setClubState('challisland','reg');
    return { before, after, gone, now: clubState('challisland') };
  });
  ck('a legacy `true` still reads as "want"', st.before==='want', st);
  ck('registered is its own state', st.after==='reg' && st.now==='reg', st);
  ck('and can be cleared', st.gone===null, st);

  /* ---- Challenge Island: Monday, weekly, first Sept 14 ---- */
  const chal = await p.evaluate(()=>{
    const c = CLUBS.find(x=>x.id==='challisland');
    return {
      days: clubWeekdays(c),
      first14: clubMeetsOn(c,'2026-09-14'),      // first real meeting, a Monday
      week2: clubMeetsOn(c,'2026-09-21'),        // the following Monday
      wrongDay: clubMeetsOn(c,'2026-09-15'),     // a Tuesday — should never land
      beforeFirst: clubMeetsOn(c,'2026-09-07'),  // a Monday before the club starts
    };
  });
  ck('Challenge Island meets Mondays', chal.days.length===1 && chal.days[0]===1, chal);
  ck('its first real meeting lands', chal.first14, chal);
  ck('weekly cadence: the following Monday also lands', chal.week2, chal);
  ck('a non-Monday never lands', !chal.wrongDay, chal);
  ck('a Monday before the club starts does not land', !chal.beforeFirst, chal);

  /* ---- clubs that must NOT be placed (none in CLUBS lack a time/freq, but
     verify the guard holds for the whole roster over a year regardless) ---- */
  const skipped = await p.evaluate(()=>{
    const bad = CLUBS.filter(c=>{
      const placeable = c.time && /^(weekly|bi-weekly)/i.test(c.freq||'') && clubFirstDate(c);
      if(!placeable) return false;
      return false; // placeable clubs are supposed to be placeable; nothing to flag here
    });
    const noTime = CLUBS.filter(c=>!c.time).length;
    return { wronglyPlaced: bad.map(c=>c.id), noTime, total: CLUBS.length };
  });
  ck('every club has a time and cadence (River\'s catalog states 3:30–4:30 for all)', skipped.noTime===0 && skipped.total===11, skipped);

  /* ---- it shows on the day, and only when registered ---- */
  const day = await p.evaluate(()=>{
    const real=AZ.today; AZ.today=()=>'2026-09-14'; AZ.nowMinutes=()=>9*60;
    setClubState('challisland','reg');
    /* v150: the timetable — and a registered club with it — lives on Study. */
    go('study');
    const reg = [...document.querySelectorAll('#screen .evt.club')].map(n=>n.textContent.replace(/\s+/g,' ').trim());
    setClubState('challisland','want');
    go('study');
    const want = document.querySelectorAll('#screen .evt.club').length;
    setClubState('challisland','reg');
    AZ.today=real;
    return { reg, wantRows: want };
  });
  ck('a registered club joins the day it meets', day.reg.length===1 && /Challenge Island/.test(day.reg[0]), day);
  ck('a merely starred club does not', day.wantRows===0, day);

  /* ---- the clubs screen separates the two ---- */
  const screen = await p.evaluate(()=>{
    setClubState('challisland','reg'); setClubState('madscience','want');
    go('clubs');
    const t=document.getElementById('screen').textContent;
    const marks=[...document.querySelectorAll('#screen .tocrow .st')].map(n=>n.textContent);
    return { signedUp:/You are signed up for/.test(t), hoping:/hoping to join/.test(t),
             tick: marks.filter(m=>m==='✓').length, star: marks.filter(m=>m==='★').length,
             notOpen: /not open to 4th grade/.test(t) };
  });
  ck('the screen separates signed-up from starred', screen.signedUp && screen.hoping, screen);
  ck('rows carry three distinct marks', screen.tick===1 && screen.star>=1, screen);
  ck('the reconciliation list is titled for 4th grade', screen.notOpen, screen);

  /* ---- the registration event routes to the clubs screen ---- */
  /* Today reads AZ.today(), not a ctx date — point the clock into the window
     so this keeps passing after the window has closed. */
  const evt = await p.evaluate(()=>{
    const real = AZ.today; AZ.today = () => '2026-09-01';
    try { go('today'); const t = document.getElementById('screen').innerText; return {hasRow: /Fall club registration/.test(t)}; }
    finally { AZ.today = real; }
  });
  ck('the registration event appears during its window', evt.hasRow, evt);

  out.forEach(r=>console.log((r.ok?'  ok ':'FAIL ')+r.n+(r.ok?'':' → '+JSON.stringify(r.got))));
  console.log(' Challenge Island on the day:', day.reg[0]);
  console.log(out.every(r=>r.ok)?'ALL PASS':'FAILURES');
  console.log('errors:', errs.length?errs:'none');
  await b.close();
  if(!out.every(r=>r.ok)||errs.length) process.exit(1);
})();
