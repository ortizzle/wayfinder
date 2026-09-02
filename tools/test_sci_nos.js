/* v122 — River's Nature of Science unit test material.

   Two units: the teacher's practice test transcribed VERBATIM as a guide unit
   (paper entry, fixed option order, letter-for-letter with the printout), and
   a parallel study test on the same skills with a fresh experiment.

   The assertion that matters most is the option ORDER on the guide: if the
   app's C is not the paper's C, the whole "I did it on paper" mode is a lie. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8122;
const PAPER_KEY = 'CBACDBCBCABCBCBCDAD';   // the teacher's circled answers, Q1..Q19

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
    for (const f of ['science-quiz-1.json','science-measurement.json',
                     'science-variables.json','science-scales.json']) await load(f);
    const g = await load('science-nos-practice.json');
    const t = await load('science-nos-test.json');
    saveLocal();
    return {
      guide: {id:g.id, guide:!!g.guide, prep:!!g.prep, order:g.order, cards:g.cards.length,
              key: g.questions.map(q => 'ABCD'[q.ans]).join(''),
              optCounts: g.questions.map(q => q.opts.length),
              variants: g.questions.filter(q => q.variant).length, n: g.questions.length},
      test: {id:t.id, prep:!!t.prep, order:t.order, round:t.round, n:t.questions.length,
             graphs: t.questions.filter(q => q.graph).length,
             ansSpread: [0,1,2,3].map(i => t.questions.filter(q => q.ans === i).length)}
    };
  });

  // ---- the replica is faithful to the paper --------------------------------
  ck('the guide unit carries the teacher\'s key, letter for letter',
     seed.guide.key === PAPER_KEY, {got: seed.guide.key, want: PAPER_KEY});
  ck('19 questions, every one with a rescue variant',
     seed.guide.n === 19 && seed.guide.variants === 19, seed.guide);
  ck('the True/False item keeps two options, the rest have four',
     seed.guide.optCounts.filter(n => n === 2).length === 1 &&
     seed.guide.optCounts.filter(n => n === 4).length === 18, seed.guide.optCounts);
  ck('it is flagged guide + prep and shelves after Reading Scales',
     seed.guide.guide && seed.guide.prep && seed.guide.order === 4, seed.guide);

  // Option order must NOT shuffle on a guide unit — she is entering letters.
  const fixed = await p.evaluate((uid) => {
    const u = DATA.records[uid];
    quizState = null;
    go('quiz', {unitId: uid, classId: 'science', guideMode: 'work'});
    const shown = [...document.querySelectorAll('#screen .opt')].map(x => x.textContent.trim());
    const q0 = u.questions.find(q => shown.some(s => s.includes(q.opts[0].slice(0, 24))));
    return {shown: shown.slice(0, 4), authored: q0 ? q0.opts.slice(0, 4) : null};
  }, seed.guide.id);
  ck('options render in the authored order, never shuffled',
     fixed.authored && fixed.shown.every((s, i) => s.includes(fixed.authored[i].slice(0, 24))),
     fixed);

  // ---- the paper-entry door ------------------------------------------------
  const grid = await p.evaluate((uid) => {
    go('guideentry', {unitId: uid, classId: 'science'});
    const rows = [...document.querySelectorAll('#screen .grow')];
    return {rows: rows.length, letters: rows.map(r => [...r.querySelectorAll('.gopt button')]
      .map(b => b.textContent).join(''))};
  }, seed.guide.id);
  ck('the entry grid renders one row per question, A/B on the True/False row',
     grid.rows === 19 && grid.letters[10] === 'AB' &&
     grid.letters.filter(l => l === 'ABCD').length === 18, grid);

  // A realistic mixed pass: she gets 14 right and misses 5.
  const graded = await p.evaluate((uid) => {
    const u = DATA.records[uid];
    const wrong = new Set([3, 7, 8, 12, 18]);           // indexes she misses
    const answers = {};
    u.questions.forEach((q, i) => {
      answers[q.id] = wrong.has(i) ? (q.ans + 1) % q.opts.length : q.ans;
    });
    const g = guidePass(u.id); put({...g, answers});
    gradeGuide(u);
    const logs = all('log').filter(l => l.unitId === uid);
    return {
      score: logs.length ? logs[0].correct + '/' + logs[0].total : null,
      paper: logs.length ? !!logs[0].paper : false,
      misses: all('miss').filter(m => m.unitId === uid).length,
      qstats: all('qstat').length,
      view, walkText: (document.getElementById('screen')||{}).textContent || ''
    };
  }, seed.guide.id);
  ck('marking the paper scores 14 of 19 and logs it as paper work',
     graded.score === '14/19' && graded.paper, graded);
  ck('the five misses land on the review ladder', graded.misses === 5, graded);
  ck('it hands off to the walkthrough', graded.view === 'guidewalk', graded.view);

  // The rescue round asks the VARIANTS of what she missed, and only those.
  const rescue = await p.evaluate((uid) => {
    const r = buildRescueUnit(uid);
    if (!r) return {built: false};
    const orig = DATA.records[uid];
    return {built: true, n: r.questions.length,
            allRescue: r.questions.every(q => q._rescue),
            noneVerbatim: r.questions.every(q =>
              !orig.questions.some(o => o.q.trim() === q.q.trim()))};
  }, seed.guide.id);
  ck('the rescue round asks a fresh variant for each of the 5 misses',
     rescue.built && rescue.n === 5 && rescue.allRescue && rescue.noneVerbatim, rescue);

  // ---- the study test ------------------------------------------------------
  ck('the study test is prep-flagged, 20 questions in one sitting, after the guide',
     seed.test.prep && seed.test.n === 20 && seed.test.round === 20 && seed.test.order === 5,
     seed.test);
  ck('two questions carry a graph the app draws itself', seed.test.graphs === 2, seed.test);
  ck('its answers are spread across all four positions',
     seed.test.ansSpread.every(n => n > 0), seed.test.ansSpread);

  const play = await p.evaluate(async (uid) => {
    quizState = null;
    go('quiz', {unitId: uid, classId: 'science'});
    const svg = !!document.querySelector('#screen svg');
    let guard = 0, sawGraph = svg;
    while (view === 'quiz' && guard++ < 60) {
      if (document.querySelector('#screen svg')) sawGraph = true;
      const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
      if (opts.length) for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,3)); }
      await new Promise(r=>setTimeout(r,6));
      const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
      if (next) { next.click(); await new Promise(r=>setTimeout(r,6)); continue; }
      if (!opts.length) break;
    }
    return {logged: all('log').some(l => l.unitId === uid), sawGraph};
  }, seed.test.id);
  ck('a full 20-question round plays and logs', play.logged, play);
  ck('a graph actually renders inside the round', play.sawGraph, play);

  // ---- both wear the gold test-prep treatment on the Science shelf ---------
  const shelf = await p.evaluate(() => {
    go('shelf', {classId:'science', series:'Science'});
    const stops = [...document.querySelectorAll('#screen .stop')];
    return {titles: stops.map(s => (s.querySelector('.t')||{}).textContent || ''),
            gold: stops.filter(s => s.className.includes('prep')).length};
  });
  const iScales = shelf.titles.findIndex(t => /Reading Scales/.test(t));
  const iGuide  = shelf.titles.findIndex(t => /Practice Test/.test(t));
  const iTest   = shelf.titles.findIndex(t => /Study Test/.test(t));
  ck('both shelve after Reading Scales, guide then study test',
     iScales >= 0 && iGuide === iScales + 1 && iTest === iGuide + 1, shelf.titles);
  ck('three prep stops now wear the gold ring', shelf.gold === 3, shelf.gold);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + JSON.stringify(r.got).slice(0,320))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
