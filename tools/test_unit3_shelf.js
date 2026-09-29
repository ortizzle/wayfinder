/* v178 — Unit 3 (Multiply Multi-Digit Whole Numbers) shelves as its own book of
   nine LESSONS, the same shape as Unit 2, and Units 1 and 2 are untouched.

   Counts are asserted as MINIMUMS, never exact — a lesson must be free to grow
   when her work shows a gap (test_phases.js's exact-18, test_k2.js's 16/17 and
   test_az_latlong.js's 9/18 each broke on an honest addition).  The teaching is
   pinned by what the lessons SAY, not by question id, which would not survive
   a renumber. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8403;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});
  const N = [1,2,3,4,5,6,7,8,9];

  const seed = await p.evaluate(async (N) => {
    const files = N.map(n => `./content/math-u3-l${n}.json`)
      .concat([1,2,3,4,5,6].map(n => `./content/math-u2-l${n}.json`))
      .concat(['math-lesson-1-1','math-t3-31','math-t3-review'].map(f => `./content/${f}.json`));
    const ids = [];
    for (const f of files) {
      const j = await (await fetch(f, {cache:'no-store'})).json();
      const u = Object.values(j.records).find(r => r.type === 'unit');
      u.status = 'approved'; u.updatedAt = Date.now() - 6e5;
      DATA.records[u.id] = u; ids.push(u.id);
    }
    saveLocal();
    return ids;
  }, N);
  ck('nine Unit 3 lessons plus Unit 2 and three Unit 1 parts seed', seed.length === 18, seed);

  const shelves = await p.evaluate(() => {
    const r = shelvesFor('math');
    return {loose: r.loose.map(u=>u.title),
            books: r.shelves.map(s => ({name: s.name, parts: s.lessons.map(u=>u.title)}))};
  });
  const u3 = shelves.books.find(s => s.name === 'Unit 3');
  ck('Unit 3 is its own shelf, beside Units 1 and 2',
     !!u3 && ['Unit 1','Unit 2'].every(n => shelves.books.some(s => s.name === n)), shelves.books.map(s=>s.name));
  ck('nothing is left loose on the subject screen', shelves.loose.length === 0, shelves.loose);
  ck('Unit 3 holds all nine lessons', u3 && u3.parts.length === 9, u3 && u3.parts);
  ck('they sort Lesson 1 to Lesson 9 — numeric-aware, so 9 never lands before 1',
     u3 && u3.parts.every((t,i) => t.startsWith(`Unit 3 · Lesson ${i+1}: `)), u3 && u3.parts);
  ck('no Unit 3 title reuses a Topic-style 3-N label (Unit 1 already has 3-1…3-7)',
     u3 && u3.parts.every(t => !/·\s*3-\d/.test(t)), u3 && u3.parts);
  ck('Unit 2 still holds its six lessons', (shelves.books.find(s=>s.name==='Unit 2')||{parts:[]}).parts.length === 6);

  const meta = await p.evaluate((N) => N.map(n => {
    const u = DATA.records['unit-m3u'+n];
    return {id:u.id, cls:u.classId, round:u.round, libv:u.libv, series:u.series,
            cards:u.cards.length, qs:u.questions.length,
            lvs:[1,2,3].map(l=>u.questions.filter(q=>q.lv===l).length),
            slots:[0,1,2,3].map(i=>u.questions.filter(q=>q.ans===i).length),
            dup:u.questions.filter(q=>new Set(q.opts).size !== q.opts.length).map(q=>q.id),
            prep:!!u.prep};
  }), N);
  ck('every lesson is classId math (the v136 orphan trap)', meta.every(m=>m.cls==='math'), meta.map(m=>m.cls));
  ck('every lesson is one sitting (round covers the questions)',
     meta.every(m=>m.qs >= 10 && m.round >= 10 && m.cards >= 5), meta.map(m=>[m.round,m.qs,m.cards]));
  ck('every lesson carries series and libv', meta.every(m=>m.series==='Unit 3' && m.libv>=1), meta.map(m=>[m.series,m.libv]));
  ck('no lesson is flagged prep — these are the lessons, not test prep (v139)', meta.every(m=>!m.prep));
  ck('every lesson spans all three levels', meta.every(m=>m.lvs.every(c=>c>0)), meta.map(m=>m.lvs));
  ck('answers are spread across all four slots in every lesson (the _balance bug)',
     meta.every(m=>m.slots.every(c=>c>0)), meta.map(m=>m.slots));
  ck('no question carries a duplicated option', meta.every(m=>m.dup.length===0), meta.map(m=>m.dup));

  // Standalone from siblings: a round serves 5–10 shuffled, so no stem may lean
  // on another ("the cargo from before", "the painting"). Anchored to the stem
  // start plus "from before", per the v185 over-blunt-regex lesson.
  const leans = await p.evaluate((N) => {
    const bad = [];
    N.forEach(n => DATA.records['unit-m3u'+n].questions.forEach(q => {
      if (/^(the|that) same\b/i.test(q.q.trim()) || /\bfrom before\b|\bthe previous\b/i.test(q.q)) bad.push(n+'/'+q.id);
      if (/\b(all|none) of the above\b/i.test(q.opts.join(' '))) bad.push(n+'/'+q.id+' positional');
    }));
    return bad;
  }, N);
  ck('no stem leans on a sibling question, no positional options', leans.length === 0, leans);

  // The teaching, by what it says.
  const t = await p.evaluate(() => {
    const u = n => DATA.records['unit-m3u'+n];
    const blob = n => JSON.stringify(u(n));
    const qwith = (n, re) => u(n).questions.find(q => re.test(q.q));
    const q34x26 = qwith(4, /What is 34 × 26\?/);
    const q306 = qwith(6, /What is 306 × 4\?/);
    const q34x5 = qwith(3, /What is 34 × 5\?/);
    const quarterly = qwith(7, /paid quarterly\. How many times/);
    return {
      zerosCounted: /60,000, not 6,000/.test(blob(1)),
      exponentNotFactor: /NOT 10 × 3 = 30/.test(blob(1)),
      mixedRounding: /cannot tell which way/.test(blob(2)),
      underProves: /underestimate/i.test(blob(2)) && /at least/i.test(blob(2)),
      carryAfter: /Multiply first, THEN add/.test(blob(3)),
      sideBySide: q34x5 && q34x5.opts.includes('1,520') && q34x5.opts.includes('150'),
      placeholder: q34x26 && q34x26.opts.includes('272') && q34x26.opts[q34x26.ans] === '884',
      skipZero: q306 && q306.opts.includes('144') && q306.opts[q306.ans] === '1,224',
      carryOnZero: /the carried 2 is added/.test(blob(6)),
      quarterlyIs4: quarterly && quarterly.opts[quarterly.ans] === '4',
      /* JSON.stringify escapes the quotes around "Times as many", so the regex
         must not contain them (the v195 trap). */
      timesAsMany: /times as many\W+ is a multiplication signal/i.test(blob(8)),
      critique2496: /2,496/.test(blob(9)) && /either way/.test(blob(9)),
      srcNames: [1,2,3,4,5,6,7,8,9].every(n => /Lesson 3-\d/.test(u(n).srcName))
    };
  });
  ck('L1: a zero already in the number counts (60 × 1,000 = 60,000)', t.zerosCounted);
  ck('L1: an exponent is not a multiplier (10³ ≠ 30)', t.exponentNotFactor);
  ck('L2: mixed rounding promises nothing', t.mixedRounding);
  ck('L2: only an underestimate proves "at least"', t.underProves);
  ck('L3: multiply first, then add the carry', t.carryAfter);
  ck('L3: 34 × 5 offers the side-by-side (1,520) and dropped-carry (150) slips', t.sideBySide, t.sideBySide);
  ck('L4: 34 × 26 offers the missing-placeholder slip (272)', t.placeholder);
  ck('L6: 306 × 4 offers the skipped-zero slip (144)', t.skipZero);
  ck('L6: a carry still lands on a zero digit', t.carryOnZero);
  ck('L7: quarterly means 4 times a year', t.quarterlyIs4);
  ck('L8: "times as many" is taught as multiplication', t.timesAsMany);
  ck('L9: 48 × 52 = 2,496 shows mixed rounding can mislead', t.critique2496);
  ck('every lesson names its textbook lesson in srcName', t.srcNames);

  // A real round plays on every lesson — the quiz a real sitting would give her.
  const rounds = await p.evaluate(async (N) => {
    const res = [];
    for (const n of N) {
      quizState = null;
      go('quiz', {unitId: 'unit-m3u'+n, classId: 'math'});
      const dealt = (quizState && quizState.order || []).length;
      let guard = 0;
      while (view === 'quiz' && guard++ < 80) {
        const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
        if (opts.length) { opts[0].click(); await new Promise(r=>setTimeout(r,4)); }
        const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
        if (next) { next.click(); await new Promise(r=>setTimeout(r,4)); continue; }
        if (!opts.length) break;
      }
      document.querySelectorAll('.modal-back, .modal').forEach(m => m.remove());
      const lg = all('log').filter(l => l.unitId === 'unit-m3u'+n).pop();
      res.push({n, dealt, logged: !!lg, total: lg && lg.total});
    }
    return res;
  }, N);
  ck('a full ten-question round plays and logs on all nine lessons',
     rounds.every(r => r.dealt >= 10 && r.logged && r.total === r.dealt), rounds);

  const deck = await p.evaluate(async () => {
    cardState = {}; go('cards', {unitId:'unit-m3u4', classId:'math'});
    await new Promise(r=>setTimeout(r,30));
    return document.querySelector('#screen .face') ? 'rendered' : 'missing';
  });
  ck('a flashcard deck renders', deck === 'rendered', deck);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + String(JSON.stringify(r.got)).slice(0,320))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,5) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
