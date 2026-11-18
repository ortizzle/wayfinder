/* The 4th-grade Science update of 11/18, as the app carries it. Pins the
   facts by id and by the clock (pointed at Monday 11/30), so it cannot rot:
   - the Atmosphere test on Thursday 12/3 and the Hydrosphere test on 12/15,
     both Science tests, with no Hydrosphere quiz invented
   - the study guide coming home Tuesday 12/1, as a Science note carrying the
     update's study advice, and reaching Coming up
   - no teacher's name anywhere in what was added */
const { chromium } = require('playwright');
const port = process.argv[2] || 8302;
let fails = 0;
const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) fails++; };
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage();
  const errs = []; pg.on('pageerror', e => errs.push(e.message));
  await pg.goto(`http://localhost:${port}/index.html`, {waitUntil:'networkidle'});
  const r = await pg.evaluate(() => {
    const by = id => SUGGESTED_ASSESS.find(s => s.id === id);
    const sg = CAL.events.find(e => e.name === 'Atmosphere study guide handed out');
    AZ.today = () => '2026-11-30';
    AZ.nowMinutes = () => 6 * 60;
    go('today');
    const txt = document.getElementById('screen').textContent;
    const wd = d => new Date(d + 'T12:00:00Z').getUTCDay();
    return {
      atm: by('sg-sci-2026-12-03'), hyd: by('sg-sci-2026-12-15'),
      hydQuiz: SUGGESTED_ASSESS.some(s => s.classId === 'science' && s.kind === 'quiz' && /hydro/i.test(s.title)),
      sg, wdAtm: wd('2026-12-03'), wdSg: wd('2026-12-01'),
      coming: /Atmosphere study guide/.test(txt),
      dupIds: SUGGESTED_ASSESS.length !== new Set(SUGGESTED_ASSESS.map(s => s.id)).size,
      priv: JSON.stringify([by('sg-sci-2026-12-03'), by('sg-sci-2026-12-15'), sg])
    };
  });
  ok(r.atm && r.atm.date === '2026-12-03' && r.atm.classId === 'science' && r.atm.kind === 'test' && /Atmosphere/.test(r.atm.title), 'Atmosphere test, Science, 12/3');
  ok(r.wdAtm === 4, '12/3 is a Thursday');
  ok(r.hyd && r.hyd.date === '2026-12-15' && r.hyd.classId === 'science' && r.hyd.kind === 'test' && /Hydrosphere/.test(r.hyd.title), 'Hydrosphere test, Science, 12/15');
  ok(!r.hydQuiz, 'no Hydrosphere quiz (the update says there is none)');
  ok(r.sg && r.sg.start === '2026-12-01' && !r.sg.end && r.sg.classId === 'science' && r.sg.kind === 'note', 'study guide comes home 12/1 as a Science note');
  ok(r.wdSg === 2, '12/1 is a Tuesday');
  ok(r.sg && /12\/3/.test(r.sg.note) && /explain/i.test(r.sg.note) && /notes/i.test(r.sg.note), 'the note names the test date and the update\'s study advice');
  ok(r.coming, 'the study guide reaches Coming up from Monday 11/30');
  ok(!r.dupIds, 'no duplicate suggestion ids');
  ok(!/Mrs\.|Nellis|@/.test(r.priv), 'no teacher name or address in what was added');
  ok(errs.length === 0, 'no page errors ' + JSON.stringify(errs));
  await b.close();
  console.log(fails ? `${fails} FAILED` : 'ALL PASS');
  process.exit(fails ? 1 : 0);
})();
