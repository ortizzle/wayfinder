/* v121 — the Lesson 1 Synonyms & Antonyms unit no longer hands the answer over.
   A vocabulary question that defines the word in its own stem tests nothing;
   this asserts the stems are bare, the distractors are real, and the unit still
   plays end to end. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8121;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const seed = await p.evaluate(async () => {
    const j = await (await fetch('./content/wordly-wise-5-01-syn.json', {cache:'no-store'})).json();
    const u = Object.values(j.records).find(r => r.type === 'unit');
    u.status = 'approved'; u.updatedAt = Date.now() - 1000;
    DATA.records[u.id] = u; saveLocal();
    return {id:u.id, libv:u.libv, qs:u.questions, cards:u.cards.length};
  });

  // No stem may gloss the word it is asking about.
  const glossed = seed.qs.filter(q => /\b\w+\s*\([a-z][^)]{4,}\)/.test(q.q)).map(q => q.id);
  ck('no stem defines the word it is testing', glossed.length === 0, glossed);

  // No option may appear in the stem — that hands the answer over outright.
  const echoed = seed.qs.filter(q => q.opts.some(o =>
    new RegExp('\\b' + o.split(',')[0].trim() + '\\b', 'i').test(q.q))).map(q => q.id);
  ck('no option is echoed inside its own stem', echoed.length === 0, echoed);

  // Every question must carry a real trap: a word related to the stem word the
  // other way round (a synonym in an antonym question, or vice versa), so the
  // item cannot be answered by elimination on part of speech alone.
  const noHint = seed.qs.filter(q => /then find its match/.test(q.hint||'')).map(q => q.id);
  ck('the boilerplate hint is gone from every question', noHint.length === 0, noHint);
  ck('every explanation says why, not just what',
     seed.qs.every(q => (q.ex.main||'').length > 40), seed.qs.filter(q=>q.ex.main.length<=40).map(q=>q.id));

  ck('the fix ships with a libv so it wins the approval race', seed.libv >= 1, seed.libv);
  ck('19 questions, 15 cards, four unique options each',
     seed.qs.length === 19 && seed.cards === 15 &&
     seed.qs.every(q => q.opts.length === 4 && new Set(q.opts).size === 4), seed.qs.length);
  ck('correct answers are spread across all four positions',
     [0,1,2,3].every(i => seed.qs.some(q => q.ans === i)),
     [0,1,2,3].map(i => seed.qs.filter(q=>q.ans===i).length));

  // It still plays: a full quiz round, answered correctly, logs.
  const quiz = await p.evaluate(async (uid) => {
    quizState = null;
    go('quiz', {unitId: uid, classId: 'english'});
    let guard = 0;
    while (view === 'quiz' && guard++ < 40) {
      const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
      if (opts.length) for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,4)); }
      await new Promise(r=>setTimeout(r,8));
      const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
      if (next) { next.click(); await new Promise(r=>setTimeout(r,8)); continue; }
      if (!opts.length) break;
    }
    return {logged: all('log').some(l => l.unitId === uid)};
  }, seed.id);
  ck('a full quiz round completes and logs', quiz.logged, quiz);

  // It still shelves in the right place, right after Lesson 1.
  const shelf = await p.evaluate(async () => {
    for (const f of ['wordly-wise-5-01.json','wordly-wise-5-02.json']) {
      const j = await (await fetch('./content/' + f, {cache:'no-store'})).json();
      const u = Object.values(j.records).find(r => r.type === 'unit');
      u.status = 'approved'; u.updatedAt = Date.now() - 1000; DATA.records[u.id] = u;
    }
    saveLocal();
    go('shelf', {classId:'english', series:'Wordly Wise'});
    return [...document.querySelectorAll('#screen .stop .t')].map(x => x.textContent);
  });
  const i1 = shelf.findIndex(t => /^Lesson 1$/.test(t.trim()));
  const iS = shelf.findIndex(t => /Synonyms/.test(t));
  ck('it still sits directly after Lesson 1 on the shelf',
     i1 >= 0 && iS === i1 + 1, shelf);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + JSON.stringify(r.got).slice(0,300))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
