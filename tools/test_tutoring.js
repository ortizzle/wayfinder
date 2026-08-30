/* Tutoring today (v118) — a standing weekly appointment read once from her
   calendar, rendered on Today keyed on the REAL weekday, not shownDate — it
   runs school day or not (a Labor Day Monday still shows it). */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8118;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'domcontentloaded'});
  await p.addScriptTag({path:__dirname+'/seed.js'}); await p.waitForTimeout(300);

  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const r = await p.evaluate(() => {
    const readCard = () => {
      const cards = [...document.querySelectorAll('#screen .card.quiet')];
      const c = cards.find(x => (x.querySelector('.eyebrow')||{}).textContent === 'Tutoring today');
      return c ? c.querySelector('.row .k').textContent + '|' + c.querySelector('.row small').textContent : null;
    };
    const out = {};

    // Monday 2026-08-17 — a real school day, a tutoring day.
    AZ.today = () => '2026-08-17';
    go('today'); out.mon = readCard();

    // Tuesday 2026-08-18 — the other weekly slot.
    AZ.today = () => '2026-08-18';
    go('today'); out.tue = readCard();

    // Labor Day, Monday 2026-09-07 — NOT a school day (the schedule folds to
    // showing Tuesday's line-up), but tutoring is her own appointment and
    // must still show, keyed on the real day, not the shown one.
    AZ.today = () => '2026-09-07';
    go('today'); out.laborDay = readCard();

    // Wednesday 2026-08-19 — not a tutoring day, no card.
    AZ.today = () => '2026-08-19';
    go('today'); out.wed = readCard();

    return out;
  });

  ck('Monday shows tutoring, 3:00–5:00 pm',
     r.mon && /🧑/.test(r.mon) && r.mon.includes('3:00–5:00 pm'), r.mon);
  ck('Tuesday shows tutoring, 3:00–5:00 pm',
     r.tue && r.tue.includes('3:00–5:00 pm'), r.tue);
  ck('Labor Day (a Monday, no school) still shows tutoring',
     r.laborDay && r.laborDay.includes('3:00–5:00 pm'), r.laborDay);
  ck('Wednesday (no tutoring) renders no tutoring card', r.wed === null, r.wed);

  out.forEach(x => console.log((x.ok ? ' ok ' : 'FAIL ') + x.n + (x.ok ? '' : ' -> ' + JSON.stringify(x.got))));
  console.log(out.every(x=>x.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(x=>x.ok) || errs.length) process.exit(1);
})();
