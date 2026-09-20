/* SUGGESTED_ASSESS, end to end — the one-tap adds from a newsletter or a
   teacher update reach the parent view, accept into real assess records, and
   drop out of the suggestion card once taken.

   This exists because tools/test_newsletter.js has been stale since the brief
   rework removed the .runway class it queries: it crashes before its first
   assertion, so this path had no working coverage at all.

   NOTHING here names a date or a title. It was written for the 9/9 math
   update's two dates and pinned the 9/18 quiz by name; that assertion expired
   on 9/19 and took four others down with it, which is the SECOND time this
   file has rotted by the calendar (the first pinned the 9/10 test and broke
   overnight on 9/11). So the whole flow now runs against whichever suggestion
   is still ahead TODAY — pin the rule, never the almanac. */
const { chromium } = require('playwright');
const port = process.argv[2] || 8302;
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage();
  const errs = []; pg.on('pageerror', e => errs.push(e.message));
  await pg.goto(`http://localhost:${port}/index.html`, {waitUntil:'networkidle'});

  const live = await pg.evaluate(() => {
    const today = AZ.today();
    const ahead = SUGGESTED_ASSESS.filter(s => s.date >= today);
    const p = ahead[0] || null;
    return {
      today,
      shown: ahead.map(s => s.title + ' · ' + s.date),
      pick: p && {id:p.id, title:p.title, date:p.date, classId:p.classId, kind:p.kind},
      dupIds: SUGGESTED_ASSESS.length !== new Set(SUGGESTED_ASSESS.map(s=>s.id)).size,
      badClass: SUGGESTED_ASSESS.filter(s => !CLASS_BY_ID[s.classId]).map(s=>s.classId)
    };
  });

  // open the parent view for real and find the rows
  const parent = await pg.evaluate((pick) => {
    go('parent');
    const txt = document.getElementById('screen').textContent;
    return {
      /* Every suggestion still ahead is actually offered — the count is
         whatever the calendar happens to hold, which is the point. */
      allOffered: SUGGESTED_ASSESS.filter(s => s.date >= AZ.today())
                    .every(s => txt.includes(s.title)),
      offered: !!(pick && txt.includes(pick.title)),
      /* And the mirror rule: SUGGESTED_ASSESS filters on sg.date >= today, so
         anything already past must not be offered. */
      past: SUGGESTED_ASSESS.filter(s => s.date < AZ.today())
              .some(s => txt.includes(s.title))
    };
  }, live.pick);

  // accept it through the real button in the newsletter card
  const accepted = live.pick && await pg.evaluate((pick) => {
    const row = [...document.querySelectorAll('.row')]
      .find(r => r.textContent.includes(pick.title));
    const btn = row && [...row.querySelectorAll('button')]
      .find(b => b.textContent.trim() === 'Add');
    if (!btn) return {err:'no Add button found on the row'};
    btn.click();
    const r = DATA.records['assess_' + pick.id];
    return r ? {date:r.date, classId:r.classId, kind:r.kind, score:r.score, title:r.title} : {err:'no record written'};
  }, live.pick);

  // once accepted it must leave the suggestion list rather than sit there twice
  const gone = live.pick && await pg.evaluate((pick) => {
    const txt = document.getElementById('screen').textContent;
    const card = [...document.querySelectorAll('.card')]
      .find(c => /From the newsletter/.test(c.textContent));
    return { stillSuggested: !!(card && card.textContent.includes(pick.title)),
             nowListed: txt.includes(pick.title) };
  }, live.pick);

  // and it should now drive the runway / study plan like a real test
  const plan = live.pick && await pg.evaluate((pick) => {
    const p = studyPlan(AZ.today());
    const m = p.find(x => x.classId === pick.classId);
    return m ? m.why || (m.reasons||[]).join('; ') : 'no entry for ' + pick.classId;
  }, live.pick);

  const out = []; const T=(n,c)=>out.push((c?'ok   ':'FAIL ')+n);
  T('at least one suggestion is still ahead to exercise', !!live.pick);
  T('every still-ahead suggestion is offered in the parent view', parent.allOffered);
  T('no duplicate suggestion ids', !live.dupIds);
  T('every suggestion points at a real subject', live.badClass.length === 0);
  T('the one under test renders in the parent view', parent.offered);
  T('a suggestion whose date has passed is no longer offered', !parent.past);
  T('accepting writes a real assess record, unscored', accepted && !accepted.err
      && accepted.date===live.pick.date && accepted.classId===live.pick.classId
      && accepted.kind===live.pick.kind && accepted.score==null);
  T('an accepted one leaves the suggestion card but stays on the screen',
      gone && !gone.stillSuggested && gone.nowListed);
  T('an accepted test drives the study plan', /quiz|test|day/i.test(plan||''));
  console.log(out.join('\n'));
  console.log('shown from ' + live.today + ':\n  ' + live.shown.join('\n  '));
  console.log('under test: ' + (live.pick ? live.pick.title + ' · ' + live.pick.date : 'none'));
  console.log('plan reason: ' + plan);
  if(accepted && accepted.err) console.log('accept error: ' + accepted.err);
  const bad = out.some(l=>l.startsWith('FAIL'));
  console.log(bad ? 'SOME FAILED' : 'ALL PASS', '| page errors:', errs.length?errs:'none');
  await b.close();
  if(bad || errs.length) process.exit(1);
})();
