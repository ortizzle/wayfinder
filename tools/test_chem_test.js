/* v190 — River's Chemistry unit test material.

   Two units, the v122 pattern: the teacher's practice test transcribed
   VERBATIM as a guide unit (paper entry, fixed option order, letter-for-letter
   with the printout), and a parallel study test on the same ideas with fresh
   examples. The assertion that matters most is the option ORDER on the guide:
   if the app's C is not the paper's C, the "I did it on paper" mode is a lie. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8413;
const PAPER_KEY = 'ABACABABADBABCCBBDDAA';   // the teacher's circled answers, Q1..Q21

(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const seed = await p.evaluate(async () => {
    const load = async f => {
      const j = await (await fetch('./content/' + f, {cache:'no-store'})).json();
      const u = Object.values(j.records).find(r => r.type === 'unit');
      u.status = 'approved'; u.updatedAt = Date.now() - 1000;
      DATA.records[u.id] = u; return u;
    };
    for (const f of ['science-phases-matter.json','science-phase-changes.json',
                     'science-density-buoyancy.json','science-molecules-compounds.json',
                     'science-quiz-1.json']) await load(f);
    const g = await load('science-chem-practice.json');
    const t = await load('science-chem-test.json');
    saveLocal();
    const blob = u => JSON.stringify(u);
    const sees = u => u.questions.map(q => q.q + ' ' + q.opts.join(' ')).join(' ');
    return {
      inLib: CONTENT_LIBRARY.includes('content/science-chem-practice.json') &&
             CONTENT_LIBRARY.includes('content/science-chem-test.json'),
      guide: {id:g.id, cls:g.classId, guide:!!g.guide, prep:!!g.prep, order:g.order, libv:g.libv,
              key: g.questions.map(q => 'ABCD'[q.ans]).join(''),
              optCounts: g.questions.map(q => q.opts.length),
              variants: g.questions.filter(q => q.variant && q.variant.opts.length === 4).length,
              n: g.questions.length,
              picture: g.questions.filter(q => /The picture (shows|labels)/.test(q.q)).length,
              notes: ['energy or feelings','know water examples','know freezing too','pick out pieces',
                      'filled minus empty','periodic table','2 or more']
                     .filter(s => !blob(g).toLowerCase().includes(s.toLowerCase()))},
      test: {id:t.id, cls:t.classId, prep:!!t.prep, guide:!!t.guide, order:t.order, round:t.round, n:t.questions.length,
             ansSpread: [0,1,2,3].map(i => t.questions.filter(q => q.ans === i).length),
             reused: ['grape','potash','potassium oxide','compost','hail','lemonade powder','He ']
                     .filter(s => sees(t).includes(s)),
             backref: t.questions.filter(q => /^(that|this|the same)\b/i.test(q.q)).length,
             topics: {solution: /solution/i.test(sees(t)), solvent: /SOLVENT/.test(sees(t)),
                      solute: /SOLUTE/.test(sees(t)), table: /periodic table/i.test(sees(t)),
                      density: t.questions.some(q => /48 g/.test(q.q) && /^2 g\/cm³, and it sinks$/.test(q.opts[q.ans]))}}
    };
  });

  ck('both files are in CONTENT_LIBRARY with the science classId',
     seed.inLib && seed.guide.cls === 'science' && seed.test.cls === 'science', seed);
  ck('the guide unit carries the teacher\'s key, letter for letter',
     seed.guide.key === PAPER_KEY, {got: seed.guide.key, want: PAPER_KEY});
  ck('21 questions, every one with a four-option rescue variant',
     seed.guide.n === 21 && seed.guide.variants === 21, seed.guide);
  ck('the five two-choice items keep two options, the rest have four',
     seed.guide.optCounts.filter(n => n === 2).length === 5 &&
     seed.guide.optCounts.filter(n => n === 4).length === 16, seed.guide.optCounts);
  ck('the two picture questions say what the picture shows', seed.guide.picture === 2, seed.guide.picture);
  ck('the teacher\'s margin notes are carried', seed.guide.notes.length === 0, seed.guide.notes);
  ck('guide + prep, order 1, libv', seed.guide.guide && seed.guide.prep && seed.guide.order === 1 && seed.guide.libv >= 1, seed.guide);

  // Option order must NOT shuffle on a guide unit.
  const fixed = await p.evaluate((uid) => {
    const u = DATA.records[uid];
    quizState = null;
    go('quiz', {unitId: uid, classId: 'science', guideMode: 'work'});
    const shown = [...document.querySelectorAll('#screen .opt')].map(x => x.textContent.trim());
    const q0 = u.questions.find(q => q.opts.length === shown.length &&
      q.opts.every(o => shown.some(s => s.includes(o.slice(0, 20)))));
    return {shown, authored: q0 ? q0.opts : null};
  }, seed.guide.id);
  ck('options render in the authored order, never shuffled',
     fixed.authored && fixed.shown.every((s, i) => s.includes(fixed.authored[i].slice(0, 20))), fixed);

  const grid = await p.evaluate((uid) => {
    go('guideentry', {unitId: uid, classId: 'science'});
    const rows = [...document.querySelectorAll('#screen .grow')];
    return {rows: rows.length, letters: rows.map(r => [...r.querySelectorAll('.gopt button')]
      .map(b => b.textContent).join(''))};
  }, seed.guide.id);
  ck('the entry grid renders 21 rows, A/B on the two-choice rows',
     grid.rows === 21 && grid.letters.filter(l => l === 'AB').length === 5 &&
     grid.letters.filter(l => l === 'ABCD').length === 16, grid.letters);

  const graded = await p.evaluate((uid) => {
    const u = DATA.records[uid];
    const wrong = new Set([6, 10, 14, 15]);
    const answers = {};
    u.questions.forEach((q, i) => { answers[q.id] = wrong.has(i) ? (q.ans + 1) % q.opts.length : q.ans; });
    const g = guidePass(u.id); put({...g, answers});
    gradeGuide(u);
    const logs = all('log').filter(l => l.unitId === uid);
    const r = buildRescueUnit(uid);
    return { score: logs.length ? logs[0].correct + '/' + logs[0].total : null, paper: logs.length ? !!logs[0].paper : false,
             misses: all('miss').filter(m => m.unitId === uid).length, view,
             rescue: r ? {n: r.questions.length, allRescue: r.questions.every(q => q._rescue),
                          four: r.questions.every(q => q.opts.length === 4)} : null };
  }, seed.guide.id);
  ck('a 17-of-21 paper pass grades, logs as paper work and walks through',
     graded.score === '17/21' && graded.paper && graded.view === 'guidewalk', graded);
  ck('the four misses land on the ladder and the rescue round asks four variants',
     graded.misses === 4 && graded.rescue && graded.rescue.n === 4 && graded.rescue.allRescue && graded.rescue.four, graded);

  ck('the study test: prep, not a guide, 20 questions in one sitting, order 2',
     seed.test.prep && !seed.test.guide && seed.test.n === 20 && seed.test.round === 20 && seed.test.order === 2, seed.test);
  ck('its answers are spread across all four positions', seed.test.ansSpread.every(n => n > 0), seed.test.ansSpread);
  ck('none of the paper\'s own examples is reused in a study-test question', seed.test.reused.length === 0, seed.test.reused);
  ck('no study-test stem leans on a neighbour', seed.test.backref === 0, seed.test.backref);
  ck('mixtures, solutions, solvent, solute, the periodic table and a worked density are all asked',
     Object.values(seed.test.topics).every(Boolean), seed.test.topics);

  const play = await p.evaluate(async (uid) => {
    quizState = null; go('quiz', {unitId: uid, classId: 'science'});
    let guard = 0;
    while (view === 'quiz' && guard++ < 60) {
      const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
      if (opts.length) for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,3)); }
      await new Promise(r=>setTimeout(r,6));
      const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
      if (next) { next.click(); await new Promise(r=>setTimeout(r,6)); continue; }
      if (!opts.length) break;
    }
    document.querySelectorAll('.modal-bg, .modal').forEach(m => m.remove());
    const log = all('log').find(l => l.unitId === uid);
    return {logged: !!log, total: log && log.total};
  }, seed.test.id);
  ck('a full 20-question round plays and logs', play.logged && play.total === 20, play);

  const shelf = await p.evaluate(() => {
    go('shelf', {classId:'science', series:'Unit 2'});
    const stops = [...document.querySelectorAll('#screen .stop')];
    const sh = shelvesFor('science');
    return {titles: stops.map(s => (s.querySelector('.t')||{}).textContent || ''),
            gold: stops.filter(s => s.className.includes('prep')).length,
            names: sh.shelves.map(s => s.name),
            u1: (sh.shelves.find(s => s.name === 'Unit 1') || {lessons:[]}).lessons.map(u => u.id),
            loose: sh.loose.map(u => u.id)};
  });
  /* v195: the Chemistry test material lives in River's "Unit 2 - Chemistry"
     Drive folder, so it is its own Unit 2 shelf; the phases parts it tests are
     Unit 1.2 and stay on the Unit 1 shelf. */
  ck('Unit 2 is its own shelf: practice test, then study test; Unit 1 keeps the phases parts',
     shelf.titles.length === 2 && /Practice Unit Test/.test(shelf.titles[0]) && /Study Test/.test(shelf.titles[1]) &&
     shelf.names.slice().sort().join() === 'Unit 1,Unit 2' && !shelf.u1.some(id => /chem/.test(id)) &&
     shelf.u1.includes('unit-sci-molcomp') && shelf.loose.length === 0, shelf);
  ck('both wear the gold prep ring', shelf.gold === 2, shelf.gold);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + JSON.stringify(r.got).slice(0,320))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
