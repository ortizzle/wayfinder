/* v164 — Unit 2 (Add and Subtract Decimals) shelves as its own book of six
   LESSONS, one per school day, and Unit 1 is untouched beside it.

   The thing this pins hardest: Unit 1 already holds a `Topic 2 · 2-1…2-7` run
   from the GRADE-4 book (whole numbers) and Unit 2 is the GRADE-5 book, whose
   Topic 2 is decimals. Both shelves render on the Math subject screen at once,
   so the lesson-numbered titles are what stop two visible "2-1"s pointing at
   different content. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8302;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const seed = await p.evaluate(async () => {
    const files = [1,2,3,4,5,6].map(n => `./content/math-u2-l${n}.json`)
      .concat(['math-lesson-1-1','math-t2-21','math-t2-23','math-t3-review']
              .map(f => `./content/${f}.json`));
    const ids = [];
    for (const f of files) {
      const j = await (await fetch(f, {cache:'no-store'})).json();
      const u = Object.values(j.records).find(r => r.type === 'unit');
      u.status = 'approved'; u.updatedAt = Date.now() - 6e5;
      DATA.records[u.id] = u; ids.push(u.id);
    }
    saveLocal();
    return ids;
  });
  ck('all six lessons plus four Unit 1 parts seed', seed.length === 10, seed);

  const shelves = await p.evaluate(() => {
    const r = shelvesFor('math');
    return {loose: r.loose.map(u=>u.title),
            books: r.shelves.map(s => ({name: s.name, parts: s.lessons.map(u=>u.title)}))};
  });
  const u2 = shelves.books.find(s => s.name === 'Unit 2');
  const u1 = shelves.books.find(s => s.name === 'Unit 1');
  ck('Unit 2 is its own shelf, beside Unit 1', !!u2 && !!u1, shelves.books.map(s=>s.name));
  ck('nothing is left loose on the subject screen', shelves.loose.length === 0, shelves.loose);
  ck('Unit 2 holds exactly the six lessons', u2 && u2.parts.length === 6, u2 && u2.parts);

  // The order is the order she meets them — lesson 1 through lesson 6.
  const want = ['Mental Math with Decimals','Estimate Sums and Differences',
    'Adding and Subtracting with Models','Add Decimals','Subtract Decimals',
    'Model with Math: Bar Diagrams'];
  ck('the six sort in teaching order, Lesson 1 to Lesson 6',
     u2 && u2.parts.every((t,i) => t === `Unit 2 · Lesson ${i+1}: ${want[i]}`), u2 && u2.parts);

  // Unit 1 keeps its grade-4 Topic 2 run, untouched, on its own shelf.
  ck('Unit 1 still carries its own Topic 2 whole-number lessons',
     u1 && u1.parts.some(t => /Topic 2 · 2-1 Mental Math: Add and Subtract/.test(t)) &&
           u1.parts.some(t => /Topic 2 · 2-3 Add Whole Numbers/.test(t)), u1 && u1.parts);
  // ...and no Unit 2 part borrows a "2-N" label that would read as a duplicate.
  ck('no Unit 2 title reuses a Topic-style 2-N label',
     u2 && u2.parts.every(t => !/·\s*2-\d/.test(t)), u2 && u2.parts);

  const meta = await p.evaluate(() => [1,2,3,4,5,6].map(n => {
    const u = DATA.records['unit-m2u'+n];
    return {id:u.id, cls:u.classId, round:u.round, libv:u.libv, series:u.series,
            cards:u.cards.length, qs:u.questions.length,
            lvs:[1,2,3].map(l=>u.questions.filter(q=>q.lv===l).length),
            slots:[0,1,2,3].map(i=>u.questions.filter(q=>q.ans===i).length)};
  }));
  ck('every lesson is classId math (the orphan trap)', meta.every(m=>m.cls==='math'), meta.map(m=>m.cls));
  ck('every lesson is one sitting of 10 questions',
     meta.every(m=>m.round===10 && m.qs===10 && m.cards===5), meta.map(m=>[m.round,m.qs,m.cards]));
  ck('every lesson carries series and libv', meta.every(m=>m.series==='Unit 2' && m.libv>=1), meta.map(m=>[m.series,m.libv]));
  ck('every lesson spans all three levels', meta.every(m=>m.lvs.every(c=>c>0)), meta.map(m=>m.lvs));
  ck('answers are spread across all four slots in every lesson',
     meta.every(m=>m.slots.every(c=>c>0)), meta.map(m=>m.slots));

  // Exactly one correct answer per question — the bug the first build shipped,
  // lifting the textbook's "circle ALL" item into single-answer MC.
  const dupes = await p.evaluate(() => {
    const bad = [];
    for (const n of [1,2,3,4,5,6]) for (const q of DATA.records['unit-m2u'+n].questions)
      if (new Set(q.opts).size !== q.opts.length) bad.push('unit-m2u'+n+'/'+q.id);
    return bad;
  });
  ck('no question carries a duplicated option', dupes.length === 0, dupes);

  // A real round plays, on the lesson she would open first.
  const round = await p.evaluate(async () => {
    quizState = null;
    go('quiz', {unitId: 'unit-m2u1', classId: 'math'});
    // Capture the round size BEFORE playing it: finishQuiz clears quizState,
    // so reading it after the loop reports 0 for a round that ran perfectly.
    const dealt = (quizState && quizState.order || []).length;
    let guard = 0;
    while (view === 'quiz' && guard++ < 60) {
      const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
      if (opts.length) { opts[0].click(); await new Promise(r=>setTimeout(r,6)); }
      const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
      if (next) { next.click(); await new Promise(r=>setTimeout(r,6)); continue; }
      if (!opts.length) break;
    }
    const lg = all('log').filter(l => l.unitId === 'unit-m2u1').pop();
    return {dealt, logged: !!lg, total: lg && lg.total};
  });
  ck('a full round on Lesson 1 serves all ten and logs',
     round.dealt === 10 && round.logged && round.total === 10, round);

  // The deck opens and steps.
  const deck = await p.evaluate(async () => {
    cardState = {}; go('cards', {unitId:'unit-m2u5', classId:'math'});
    await new Promise(r=>setTimeout(r,30));
    return document.querySelector('#screen .face') ? 'rendered' : 'missing';
  });
  ck('a flashcard deck renders', deck === 'rendered', deck);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + JSON.stringify(r.got).slice(0,320))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,5) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
