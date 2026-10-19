/* Unit 3 · Test Review: Check Your Work, and the pop quiz's 0-9 range (v189).
   Pins the review's arithmetic (every product re-derived here, every named
   slip really producing the wrong number it names), its place at the end of the
   Unit 3 shelf with the prep band, a full round, and the pop quiz dealing no
   factor above 9 while a set sprint still reaches x12. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8413;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const r = await p.evaluate(async () => {
    const files = ['content/math-u3-review.json', 'content/math-u3-l1.json', 'content/math-u3-l9.json',
      'content/math-facts-1.json', 'content/math-facts-2.json', 'content/math-facts-3.json',
      'content/math-facts-4.json', 'content/math-facts-review.json'];
    for (const f of files) {
      const k = await (await fetch('./' + f, {cache:'no-store'})).json();
      for (const x of Object.values(k.records)) { x.status = 'approved'; DATA.records[x.id] = x; } }
    saveLocal();
    const u = DATA.records['unit-m3-review'];
    const sh = shelvesFor('math'); const u3 = sh.shelves.find(s => s.name === 'Unit 3');
    const num = s => Number(String(s).replace(/,/g, ''));
    /* the four slips, re-implemented here independently of the builder */
    const dig = n => String(n).split('').map(Number);
    const noCarry = (a, m) => Number(dig(a).map((d, i, D) => i === 0 ? String(d*m) : String(d*m % 10)).join(''));
    const side = (a, m) => Number(dig(a).map(d => String(d*m)).join(''));
    const noPlace = (a, b) => a * (b % 10) + a * Math.floor(b / 10);
    const skipZero = (a, m) => Number(String(a).replace(/0/g, '')) * m;
    const SLIP = {carry: noCarry, side, place: noPlace, zero: skipZero};
    const which = o => /carry/.test(o) ? 'carry' : /side by side/.test(o) ? 'side' : /second row/.test(o) ? 'place' : /zero inside/.test(o) ? 'zero' : null;
    const mist = u.questions.filter(q => /worked out [\d,]+ × \d+ and wrote/.test(q.q)).map(q => {
      const [, a, m, w] = q.q.match(/worked out ([\d,]+) × (\d+) and wrote ([\d,]+)/);
      const s = which(q.opts[q.ans]);
      return {q: q.q, s, ok: !!s && SLIP[s](num(a), +m) === num(w) && num(w) !== num(a)*+m,
              onlyOne: q.opts.filter((o, i) => i !== q.ans && which(o) && SLIP[which(o)](num(a), +m) === num(w)).length === 0};
    });
    const prod = u.questions.filter(q => /^(What is|Which answer is correct for) [\d,]+ × [\d,]+\??/.test(q.q)).map(q => {
      const [, a, m] = q.q.match(/([\d,]+) × ([\d,]+)/);
      const P = num(a) * num(m);
      return {q: q.q, ok: num(q.opts[q.ans]) === P, wrong: q.opts.every((o, i) => i === q.ans || num(o) !== P)};
    });
    const blob = JSON.stringify(u);
    const lessons = u3 && u3.lessons.map(x => x.id);
    return {
      inLib: CONTENT_LIBRARY.includes('content/math-u3-review.json'),
      classId: u.classId, series: u.series, prep: u.prep, libv: u.libv, status: u.status === 'approved',
      lessonsLast: lessons && lessons[lessons.length - 1] === 'unit-m3-review', lessons,
      loose: sh.loose.map(x => x.id),
      mist, mistN: mist.length, prod, prodN: prod.length,
      slots: new Set(u.questions.map(q => q.ans)).size, n: u.questions.length,
      lv: [1,2,3].map(l => u.questions.filter(q => q.lv === l).length),
      undo: u.questions.some(q => /2,008/.test(q.q) && /^Undo it/.test(q.opts[q.ans])),
      onesDigit: u.questions.some(q => /ones digit of 46 × 23/.test(q.q) && q.opts[q.ans] === '8'),
      zeros: u.questions.some(q => /60 × 4,000/.test(q.q) && /240,000/.test(q.opts[q.ans])),
      teacherName: /\b(Mrs|Mr|Ms|Miss)\.? [A-Z]/.test(blob),
      backref: u.questions.filter(q => /^(the|that|this) same\b/i.test(q.q)).length,
      posref: u.questions.filter(q => /\b(all|none) of the above\b/i.test(q.opts.join(' '))).length,
      future: u.updatedAt > Date.now(),
    };
  });
  ck('in CONTENT_LIBRARY, math classId, series Unit 3, prep, libv', r.inLib && r.classId === 'math' && r.series === 'Unit 3' && r.prep === true && r.libv >= 1, r);
  ck('the review sits last on the Unit 3 shelf, nothing loose', r.lessonsLast && r.loose.length === 0, r);
  ck('8 find-the-mistake items, each slip really producing the wrong number', r.mistN === 8 && r.mist.every(m => m.ok), r.mist.filter(m => !m.ok));
  ck('no OTHER slip on the list also explains the wrong number', r.mist.every(m => m.onlyOne), r.mist.filter(m => !m.onlyOne));
  ck('every product question is right and no wrong option equals the product', r.prodN >= 5 && r.prod.every(x => x.ok && x.wrong), r.prod.filter(x => !x.ok || !x.wrong));
  ck('the checks: undo catches what estimate and ones digit miss; ones digit; zeros', r.undo && r.onesDigit && r.zeros, r);
  ck('20 questions, all three levels, all four answer slots', r.n === 20 && r.lv.every(x => x > 0) && r.slots === 4, r);
  ck('no teacher name, no back- or positional references, not future-stamped', !r.teacherName && !r.backref && !r.posref && !r.future, r);

  const band = await p.evaluate(async () => {
    go('unit', {classId:'math'}); await new Promise(r => setTimeout(r, 30));
    go('shelf', {classId:'math', series:'Unit 3', open:'unit-m3-review'}); await new Promise(r => setTimeout(r, 30));
    return {prep: !!document.querySelector('#screen .prepband'), stopPrep: !!document.querySelector('#screen .stop.prep')};
  });
  ck('the review wears the gold test-prep treatment on the shelf', band.stopPrep, band);

  const play = await p.evaluate(async () => {
    quizState = null; go('quiz', {unitId:'unit-m3-review', classId:'math'});
    let guard = 0;
    while (view === 'quiz' && guard++ < 40) {
      const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
      if (opts.length) for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,4)); }
      await new Promise(r => setTimeout(r, 8));
      const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
      if (next) { next.click(); await new Promise(r=>setTimeout(r,8)); continue; }
      if (!opts.length) break;
    }
    document.querySelectorAll('.modal-bg, .modal').forEach(m => m.remove());
    const log = all('log').find(l => l.unitId === 'unit-m3-review');
    return { logged: !!log, total: log && log.total };
  });
  ck('a full round of 10 plays and logs', play.logged && play.total === 10, play);

  const pop = await p.evaluate(() => {
    const u = DATA.records['unit-mf-1']; let maxAll = 0, n = 0, pool = new Set();
    for (let i = 0; i < 6; i++) { sprintDeal('all', u, 'math'); n = sprintState.items.length;
      sprintState.items.forEach(it => { maxAll = Math.max(maxAll, it.a, it.b); pool.add([it.a, it.b].sort((x,y)=>x-y).join('x')); }); }
    const u4 = DATA.records['unit-mf-4']; let max4 = 0;
    for (let i = 0; i < 4; i++) { sprintDeal('set', u4, 'math'); sprintState.items.forEach(it => { max4 = Math.max(max4, it.a, it.b); }); }
    sprintState = null;
    return {maxAll, n, distinct: pool.size, max4, cap: POP_QUIZ_MAX};
  });
  ck('the pop quiz deals 50 facts and none has a factor above 9', pop.n === 50 && pop.maxAll <= 9 && pop.cap === 9 && pop.distinct >= 30, pop);
  ck('a set sprint on Set 4 still reaches the x11/x12 facts', pop.max4 >= 11, pop);

  out.forEach(r => console.log((r.ok ? '  ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' → ' + JSON.stringify(r.got).slice(0,400))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
