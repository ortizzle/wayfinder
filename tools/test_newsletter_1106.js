/* The 4th Grade Newsletter of the week of 11/6 and the Cub Hub of 11/6, as
   the app carries them. Pins the facts by id and by the clock (pointed at
   Monday 11/9), so it cannot rot:
   - four quizzes, each dated, each saying what it covers where the issue does
   - the Meteorologist presentations are a Science event that reaches Coming up
   - the Read-a-thon runs 11/16–11/24, FastBridge is a benchmark, Spirit Week
     is a dress event with a note, the Spelling Bee is on 12/3
   - nothing the issue leaves out on purpose (Pizza Friday, NEHS) crept in */
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
    const ev = n => CAL.events.find(e => e.name === n);
    const pick = s => s && {t: s.title, d: s.date, c: s.classId, k: s.kind};
    AZ.today = () => '2026-11-09';
    AZ.nowMinutes = () => 6 * 60;
    go('today');
    const txt = document.getElementById('screen').textContent;
    return {
      az: pick(by('sg-hist-2026-11-10')), lc: pick(by('sg-eng-2026-11-12')),
      u4: pick(by('sg-math-2026-11-13')), op: pick(by('sg-wri-2026-11-13')),
      met: ev('Meteorologist for a Day presentations'), rat: ev('Read-a-thon'),
      fb: ev('Winter FastBridge Testing'), sw: ev('Spirit Week'), bee: ev('School Spelling Bee'),
      shine: CAL.events.filter(e => /SHINE/.test(e.name)).map(e => e.start),
      dupIds: SUGGESTED_ASSESS.length !== new Set(SUGGESTED_ASSESS.map(s => s.id)).size,
      leftOut: CAL.events.some(e => /pizza|NEHS/i.test(e.name)),
      comingMet: /Meteorologist for a Day/.test(txt)
    };
  });
  ok(r.az && r.az.d === '2026-11-10' && r.az.c === 'history' && r.az.k === 'quiz', 'AZ Quiz, History, 11/10');
  ok(r.lc && r.lc.d === '2026-11-12' && r.lc.c === 'english' && /12–16/.test(r.lc.t), 'Lemonade Crime quiz on chapters 12–16, 11/12');
  ok(r.u4 && r.u4.d === '2026-11-13' && r.u4.c === 'math' && /Unit 4/.test(r.u4.t) && /decimals/.test(r.u4.t), 'Unit 4 decimals quiz, 11/13');
  ok(r.op && r.op.d === '2026-11-13' && r.op.c === 'writing' && /preposition/i.test(r.op.t), 'Object of the preposition quiz, 11/13');
  ok(!r.dupIds, 'no duplicate suggestion ids');
  ok(r.met && r.met.start === '2026-11-12' && r.met.end === '2026-11-13' && r.met.classId === 'science', 'Meteorologist presentations are a Science event, 11/12–11/13');
  ok(r.comingMet, 'the presentations reach Coming up from Monday 11/9');
  ok(r.rat && r.rat.start === '2026-11-16' && r.rat.end === '2026-11-24', 'Read-a-thon 11/16–11/24');
  ok(r.fb && r.fb.kind === 'benchmark' && r.fb.start === '2026-12-01' && r.fb.end === '2026-12-11', 'Winter FastBridge is a benchmark, 12/1–12/11');
  ok(r.sw && r.sw.kind === 'dress' && r.sw.note && r.sw.start === '2026-12-14', 'Spirit Week is a dress event with a note');
  ok(r.bee && r.bee.start === '2026-12-03', 'School Spelling Bee on 12/3');
  ok(r.shine.includes('2026-11-18') && r.shine.includes('2026-12-16'), 'both SHINE lunches');
  ok(!r.leftOut, 'Pizza Friday and NEHS stay out');
  ok(errs.length === 0, 'no page errors ' + JSON.stringify(errs));
  await b.close();
  console.log(fails ? `${fails} FAILED` : 'ALL PASS');
  process.exit(fails ? 1 : 0);
})();
