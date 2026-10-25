/* The 4th Grade Newsletter of 10/25, as the app carries it.

   Pins the facts by id and by the clock rather than by today's date, so it
   cannot rot: the clock is pointed at Monday 10/26 before anything renders.
   - the Unit 5 quiz keeps its id (an accepted copy must not duplicate) and no
     longer says "estimated"
   - Regions 3 on 10/27, and the two English quizzes "week of 10/26, date to
     confirm"
   - the weather journal and the owl pellet dissection are Science events,
     and both reach Coming up
   - the journal's note never prints the newsletter's impossible due date */
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
    const math = by('sg-math-2026-10-28'), reg = by('sg-hist-2026-10-27');
    const lc = by('sg-eng-2026-10-26-lc'), ww = by('sg-eng-2026-10-26-ww');
    const ev = n => CAL.events.find(e => e.name === n);
    const wj = ev('Weather journals handed out'), owl = ev('Owl pellet dissection in Science');
    AZ.today = () => '2026-10-26';
    AZ.nowMinutes = () => 6 * 60;
    go('today');
    const txt = document.getElementById('screen').textContent;
    return {
      math: math && {t: math.title, d: math.date, k: math.kind},
      reg: reg && {d: reg.date, c: reg.classId, k: reg.kind},
      lc: lc && {t: lc.title, d: lc.date}, ww: ww && {t: ww.title, d: ww.date},
      wj: wj && {d: wj.start, c: wj.classId, n: wj.note || ''},
      owl: owl && {d: owl.start, c: owl.classId},
      dupIds: SUGGESTED_ASSESS.length !== new Set(SUGGESTED_ASSESS.map(s => s.id)).size,
      comingWJ: /Weather journals handed out/.test(txt),
      comingOwl: /Owl pellet dissection/.test(txt)
    };
  });
  ok(r.math && r.math.d === '2026-10-28' && r.math.k === 'quiz', 'Unit 5 quiz kept its id and date');
  ok(r.math && !/estimated/i.test(r.math.t) && /5-1 to 5-4/.test(r.math.t) && /long division/.test(r.math.t),
     'Unit 5 quiz no longer says estimated and names what it covers');
  ok(r.reg && r.reg.d === '2026-10-27' && r.reg.c === 'history' && r.reg.k === 'quiz', 'Regions 3 quiz on 10/27');
  ok(r.lc && r.lc.d === '2026-10-26' && /6–10/.test(r.lc.t) && /date to confirm/.test(r.lc.t), 'Rising Action quiz, date to confirm');
  ok(r.ww && r.ww.d === '2026-10-26' && /Unit 4/.test(r.ww.t) && /date to confirm/.test(r.ww.t), 'Unit 4 vocab quiz, date to confirm');
  ok(!r.dupIds, 'no duplicate suggestion ids');
  ok(r.wj && r.wj.d === '2026-10-28' && r.wj.c === 'science', 'weather journal is a Science event on 10/28');
  ok(r.wj && !/10\/6/.test(r.wj.n) && /due date/i.test(r.wj.n), 'journal note asks about the due date and never prints 10/6');
  ok(r.owl && r.owl.d === '2026-10-30' && r.owl.c === 'science', 'owl pellet dissection is a Science event on 10/30');
  ok(r.comingWJ && r.comingOwl, 'both reach Coming up from Monday 10/26');
  ok(errs.length === 0, 'no page errors ' + JSON.stringify(errs));
  await b.close();
  console.log(fails ? `${fails} FAILED` : 'ALL PASS');
  process.exit(fails ? 1 : 0);
})();
