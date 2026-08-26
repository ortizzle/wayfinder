/* Smoke test for content/science-variables.json (Quiz 1 Part 3: Variables):
   loads, shelves alongside the existing Quiz 1 parts, flashcards and a full
   quiz round complete cleanly. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8107;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});

  const out = [];
  const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const seed = await p.evaluate(async () => {
    const ids = [];
    for (const f of ['science-quiz-1','science-measurement','science-variables']) {
      const res = await fetch(`./content/${f}.json`, {cache:'no-store'});
      const j = await res.json();
      const u = Object.values(j.records)[0];
      u.status = 'approved'; u.updatedAt = Date.now() - 1000;
      DATA.records[u.id] = u; ids.push(u.id);
    }
    saveLocal();
    return ids;
  });
  ck('all 3 Science Quiz 1 parts seeded', seed.length === 3, seed);

  const struct = await p.evaluate((ids) => {
    const bad = [];
    ids.forEach(id => {
      const u = DATA.records[id];
      if (!u.cards.length) bad.push(id + ': no cards');
      u.questions.forEach(q => {
        if (q.opts.length !== 4) bad.push(id + '/' + q.id + ': opts != 4');
        if (new Set(q.opts).size !== 4) bad.push(id + '/' + q.id + ': dup opts');
        if (q.ans < 0 || q.ans > 3) bad.push(id + '/' + q.id + ': bad ans');
      });
    });
    return bad;
  }, seed);
  ck('no structural problems', struct.length === 0, struct);

  const shelf = await p.evaluate(() => {
    go('unit', {classId:'science'});
    const spines = [...document.querySelectorAll('#screen .spine')].map(s => s.textContent);
    return spines;
  });
  ck('Science shelves as one spine with all 3 parts', shelf.some(t => /^Science/.test(t)), shelf);

  const cardsWalk = await p.evaluate(async () => {
    go('cards', {unitId:'unit-sci-vars', classId:'science'});
    let steps = 0;
    while (cardState.unitId === 'unit-sci-vars' && steps++ < 30) {
      const knowBtn = [...document.querySelectorAll('button')].find(b => /Knew it/.test(b.textContent));
      if (!knowBtn) break;
      knowBtn.click();
      await new Promise(r => setTimeout(r, 5));
    }
    return steps;
  });
  ck('flashcard deck completes cleanly', cardsWalk < 30, cardsWalk);

  const quiz = await p.evaluate(async () => {
    quizState = null;
    go('quiz', {unitId:'unit-sci-vars', classId:'science'});
    let guard = 0;
    while (view === 'quiz' && guard++ < 20) {
      const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
      if (opts.length) for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,5)); }
      await new Promise(r => setTimeout(r, 10));
      const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
      if (next) { next.click(); await new Promise(r=>setTimeout(r,10)); continue; }
      if (!opts.length) break;
    }
    return {logged: all('log').some(l => l.unitId === 'unit-sci-vars')};
  });
  ck('a full quiz round completes and logs', quiz.logged, quiz);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + JSON.stringify(r.got).slice(0,300))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
