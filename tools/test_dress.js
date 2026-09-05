/* Cub Hub 9/4: the dated list lands on the calendar, with a `dress` kind for
   the days she dresses differently — Picture Day and Spirit Week — that pins
   on Today with its own label and never renders quiet. Plus the Plot Diagram
   unit built from the quiz study guide. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8202;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const ev = await p.evaluate(() => {
    const on = d => eventsOn(d).map(e => ({name:e.name, kind:e.kind}));
    return {pic: on('2026-09-16'), spirit: on('2026-09-23'), clubs: on('2026-09-14'), pledge: on('2026-10-01'),
            dressCount: CAL.events.filter(e => e.kind==='dress').length};
  });
  ck('Picture Day and Spirit Week are dress days; the rest of the list is in as notes',
     ev.pic.some(e=>/Picture Day/.test(e.name) && e.kind==='dress') && ev.spirit.some(e=>/Spirit Week/.test(e.name) && e.kind==='dress')
     && ev.clubs.some(e=>/clubs begin/i.test(e.name)) && ev.pledge.some(e=>/Pledge/.test(e.name)) && ev.dressCount===2, ev);

  // Render Today AS 9/16 by pointing the clock there.
  const pinned = await p.evaluate(() => {
    const real = AZ.today; AZ.today = () => '2026-09-16';
    try {
      go('today');
      const rows = [...document.querySelectorAll('#screen .evt')].map(r => ({txt: r.textContent, quiet: r.classList.contains('quiet'), tm: (r.querySelector('.tm')||{}).textContent}));
      const dress = rows.find(r => /Picture Day/.test(r.txt));
      return {found: !!dress, tm: dress && dress.tm, quiet: dress && dress.quiet, note: dress && /look sharp/.test(dress.txt)};
    } finally { AZ.today = real; }
  });
  ck('on Picture Day the pinned row says Dress, carries the note, and is not quiet',
     pinned.found && pinned.tm==='Dress' && pinned.quiet===false && pinned.note, pinned);

  const week = await p.evaluate(() => {
    const real = AZ.today; AZ.today = () => '2026-09-23';
    try {
      go('today');
      const rows = [...document.querySelectorAll('#screen .evt')].map(r => r.textContent);
      const sw = rows.find(t => /Spirit Week/.test(t));
      return {found: !!sw, day: sw && /Day 3 of 5/.test(sw)};
    } finally { AZ.today = real; }
  });
  ck('mid Spirit Week the pinned row says Day 3 of 5', week.found && week.day, week);

  const coming = await p.evaluate(() => {
    const real = AZ.today; AZ.today = () => '2026-09-10';
    try {
      go('today');
      const txt = document.getElementById('screen').textContent;
      return {pic: /Fall Picture Day/.test(txt), clubs: /Fall clubs begin/.test(txt)};
    } finally { AZ.today = real; }
  });
  ck('Coming up lists Picture Day and the clubs start from a week out', coming.pic && coming.clubs, coming);

  // The Plot Diagram unit: loose under English, plays, carries the sort door.
  const plot = await p.evaluate(async () => {
    const j = await (await fetch('./content/english-plot-diagram.json',{cache:'no-store'})).json();
    const u = Object.values(j.records).find(r=>r.type==='unit'); u.status='approved'; u.updatedAt=Date.now()-1000; DATA.records[u.id]=u; saveLocal();
    go('unit',{classId:'english'});
    const txt = document.getElementById('screen').textContent;
    const loose = /Plot Diagram: Pixar Shorts/.test(txt) && !seriesOf(u);
    const door = /Sort — Before the climax/.test(txt);
    quizState = null; go('quiz',{unitId:u.id, classId:'english'});
    let guard = 0;
    while (view==='quiz' && guard++ < 40) {
      const opts=[...document.querySelectorAll('#screen .opt:not([disabled])')];
      if (opts.length) for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,3)); }
      await new Promise(r=>setTimeout(r,6));
      const n=document.querySelector('#screen .btn-primary, #screen .explain.go-on'); if(n){ n.click(); await new Promise(r=>setTimeout(r,6)); continue; }
      if(!opts.length) break;
    }
    return {loose, door, cards: u.cards.length, qs: u.questions.length, order: u.questions.filter(q=>q.kind==='order').length,
            logged: all('log').some(l=>l.unitId===u.id)};
  });
  ck('Plot Diagram shelves loose under English with its sort door, 10 cards, 20 questions incl. 2 put-in-order, and plays',
     plot.loose && plot.door && plot.cards===10 && plot.qs===20 && plot.order===2 && plot.logged, plot);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + JSON.stringify(r.got).slice(0,320))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
