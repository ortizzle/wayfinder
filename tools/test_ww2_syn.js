/* v161 — Wordly Wise Lesson 2 Synonyms & Antonyms.
   Built to the v121 rules (a stem states the situation, never the knowledge)
   and to the v102 shelving trap: this is a supplementary unit that answers to
   ONE lesson, so it must sit directly after Lesson 2 — `order` is a
   whole-shelf bucket and would exile it behind every other lesson. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8302;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const seed = await p.evaluate(async () => {
    const j = await (await fetch('./content/wordly-wise-5-02-syn.json', {cache:'no-store'})).json();
    const u = Object.values(j.records).find(r => r.type === 'unit');
    u.status = 'approved'; u.updatedAt = Date.now() - 1000;
    DATA.records[u.id] = u; saveLocal();
    return {id:u.id, libv:u.libv, order:u.order, qs:u.questions,
            cards:u.cards, title:u.title, round:u.round};
  });

  ck('it is the Lesson 2 unit and carries a libv',
     seed.id === 'unit-ww502-syn' && /Lesson 2 Synonyms & Antonyms/.test(seed.title) && seed.libv >= 1,
     [seed.id, seed.title, seed.libv]);
  ck('no order field — the v102 whole-shelf-bucket trap', seed.order == null, seed.order);
  ck('15 cards, 20 questions, four unique options each',
     seed.cards.length === 15 && seed.qs.length === 20 &&
     seed.qs.every(q => q.opts.length === 4 && new Set(q.opts).size === 4),
     [seed.cards.length, seed.qs.length]);

  // v121: a stem may never define the word it is testing.
  const glossed = seed.qs.filter(q => /\b\w+\s*\([a-z][^)]{4,}\)/.test(q.q)).map(q => q.id);
  ck('no stem defines the word it is testing', glossed.length === 0, glossed);

  // Nor may an option appear inside the stem.
  const echoed = seed.qs.filter(q => q.opts.some(o =>
    new RegExp('\\b' + o.split(',')[0].trim() + '\\b', 'i').test(q.q))).map(q => q.id);
  ck('no option is echoed inside its own stem', echoed.length === 0, echoed);

  // Where a word has two senses, context disambiguates — never a definition.
  const ex = seed.qs.filter(q => /\bextract\b/i.test(q.q));
  ck('both extract questions tag the part of speech',
     ex.length === 2 && ex.every(q => /As a NOUN/.test(q.q)), ex.map(q => q.q));

  ck('no boilerplate hint survived',
     seed.qs.every(q => !/then find its match/.test(q.hint||'')),
     seed.qs.filter(q=>/then find its match/.test(q.hint||'')).map(q=>q.id));
  ck('every explanation says why, not just what',
     seed.qs.every(q => (q.ex.main||'').length > 40),
     seed.qs.filter(q=>q.ex.main.length<=40).map(q=>q.id));
  ck('correct answers are spread across all four positions',
     [0,1,2,3].every(i => seed.qs.some(q => q.ans === i)),
     [0,1,2,3].map(i => seed.qs.filter(q=>q.ans===i).length));
  ck('every card carries a spoken-as respelling',
     seed.cards.every(c => (c.sp||'').length > 1),
     seed.cards.filter(c=>!c.sp).map(c=>c.term));

  // It plays: a full round, answered, logs.
  const quiz = await p.evaluate(async (uid) => {
    quizState = null;
    go('quiz', {unitId: uid, classId: 'english'});
    let guard = 0;
    while (view === 'quiz' && guard++ < 60) {
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

  // The v102 trap itself: directly after Lesson 2, not at the back of the book.
  const shelf = await p.evaluate(async () => {
    for (const f of ['wordly-wise-5-01.json','wordly-wise-5-01-syn.json',
                     'wordly-wise-5-02.json','wordly-wise-5-03.json',
                     'wordly-wise-5-04.json','wordly-wise-5-05.json']) {
      const r = await fetch('./content/' + f, {cache:'no-store'});
      if (!r.ok) continue;
      const j = await r.json();
      const u = Object.values(j.records).find(x => x.type === 'unit');
      u.status = 'approved'; u.updatedAt = Date.now() - 1000; DATA.records[u.id] = u;
    }
    saveLocal();
    go('shelf', {classId:'english', series:'Wordly Wise'});
    return [...document.querySelectorAll('#screen .stop .t')].map(x => x.textContent.trim());
  });
  const i2 = shelf.findIndex(t => /^Lesson 2$/.test(t));
  const iS = shelf.findIndex(t => /^Lesson 2 Synonyms/.test(t));
  ck('it sits directly after Lesson 2 on the shelf', i2 >= 0 && iS === i2 + 1, shelf);
  ck('Lesson 1 and its own syn/ant pair are still in order',
     shelf.findIndex(t => /^Lesson 1$/.test(t)) + 1 === shelf.findIndex(t => /^Lesson 1 Synonyms/.test(t)),
     shelf);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + JSON.stringify(r.got).slice(0,300))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
