/* The Lemonade Crime, all four parts (v120) — the shelf reads in chapter
   order, each part plays as a book unit, and the quoted definitions render. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8119;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});

  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const seed = await p.evaluate(async () => {
    for (const f of ['lemonade-crime-1','lemonade-crime-2','lemonade-crime-3','lemonade-crime-4']) {
      const j = await (await fetch(`./content/${f}.json`, {cache:'no-store'})).json();
      const u = Object.values(j.records)[0];
      u.status = 'approved'; u.updatedAt = Date.now() - 1000;
      DATA.records[u.id] = u;
    }
    saveLocal();
    const u = DATA.records['unit-lc2'];
    return {seeded: !!u, cards: u.cards.length, questions: u.questions.length,
            book: !!u.book, classId: u.classId,
            passages: u.questions.filter(q => q.passage).length,
            order: u.questions.filter(q => q.kind === 'order').length};
  });
  ck('unit-lc2 seeds: 26 cards, 15 questions, book:true, classId english',
     seed.cards === 26 && seed.questions === 15 && seed.book && seed.classId === 'english', seed);
  ck('it carries 4 quoted definitions and 1 put-in-order question',
     seed.passages === 4 && seed.order === 1, seed);

  // Shelf order: Ch. 1–5 must come before Ch. 6–9.
  const shelf = await p.evaluate(() => {
    go('shelf', {classId:'english', series:'The Lemonade Crime', open:'unit-lc2'});
    const titles = [...document.querySelectorAll('#screen .stop .t')].map(x => x.textContent);
    const oc = document.getElementById('shelfopen');
    return {titles, opened: oc ? oc.textContent.slice(0, 120) : null,
            clock: oc ? /Beat the clock/.test(oc.textContent) : null};
  });
  ck('all four parts are on one shelf, in reading order',
     shelf.titles.length === 4 && /1–5/.test(shelf.titles[0]) && /6–9/.test(shelf.titles[1])
     && /10–13/.test(shelf.titles[2]) && /14–16/.test(shelf.titles[3]), shelf.titles);
  ck('the opened card is Ch. 6–9', /6–9/.test(shelf.opened||''), shelf.opened);
  ck('no Beat the clock on a book unit', shelf.clock === false, shelf.clock);

  // A full quiz round, including the order question.
  const quiz = await p.evaluate(async () => {
    quizState = null;
    go('quiz', {unitId:'unit-lc2', classId:'english'});
    let guard = 0;
    while (view === 'quiz' && guard++ < 30) {
      const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
      if (opts.length) for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,4)); }
      await new Promise(r => setTimeout(r, 8));
      const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
      if (next) { next.click(); await new Promise(r=>setTimeout(r,8)); continue; }
      if (!opts.length) break;
    }
    return all('log').some(l => l.unitId === 'unit-lc2');
  });
  ck('a full quiz round completes and logs', quiz, quiz);

  // The passage plate actually renders on a question that carries one.
  /* Rounds serve 5 of the 15 questions, least-practised first, so one round
     need not contain a passage question. Walk whole rounds until one does. */
  const passage = await p.evaluate(async () => {
    for (let round = 0; round < 6; round++) {
      quizState = null;
      go('quiz', {unitId:'unit-lc2', classId:'english'});
      let guard = 0;
      while (view === 'quiz' && guard++ < 30) {
        const el = document.querySelector('#screen .passage');
        if (el) return {found: true, round, text: el.textContent.slice(0, 70)};
        const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
        if (opts.length) for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,4)); }
        await new Promise(r=>setTimeout(r,8));
        const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
        if (next) { next.click(); await new Promise(r=>setTimeout(r,8)); continue; }
        if (!opts.length) break;
      }
    }
    return {found: false};
  });
  ck('a quoted definition renders as a passage plate in the quiz', passage.found, passage);

  // Flashcards run clean.
  const cards = await p.evaluate(async () => {
    go('cards', {unitId:'unit-lc2', classId:'english'});
    let seen = 0, guard = 0;
    while (view === 'cards' && guard++ < 60) {
      const nx = document.querySelector('#screen .btn-primary');
      if (!nx) break;
      nx.click(); seen++;
      await new Promise(r => setTimeout(r, 6));
    }
    return seen;
  });
  ck('the 26-card deck steps through cleanly', cards >= 20, cards);

  /* Units 3 and 4 (the trial and the ending) play end to end too, and only
     the last one carries capstone:true — the book has a real finish. */
  const rest = await p.evaluate(async () => {
    const run = async id => {
      quizState = null;
      go('quiz', {unitId:id, classId:'english'});
      let guard = 0;
      while (view === 'quiz' && guard++ < 30) {
        const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
        if (opts.length) for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,4)); }
        await new Promise(r=>setTimeout(r,8));
        const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
        if (next) { next.click(); await new Promise(r=>setTimeout(r,8)); continue; }
        if (!opts.length) break;
      }
      return all('log').some(l => l.unitId === id);
    };
    return {
      lc3: await run('unit-lc3'), lc4: await run('unit-lc4'),
      caps: ['unit-lc1','unit-lc2','unit-lc3','unit-lc4'].filter(i => DATA.records[i].capstone),
      lc4Cards: DATA.records['unit-lc4'].cards.length,
      lc3Cards: DATA.records['unit-lc3'].cards.length
    };
  });
  ck('a full round on Ch. 10–13 completes and logs', rest.lc3, rest);
  ck('a full round on Ch. 14–16 completes and logs', rest.lc4, rest);
  ck('only the final part is the capstone',
     rest.caps.length === 1 && rest.caps[0] === 'unit-lc4', rest.caps);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + JSON.stringify(r.got).slice(0,300))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
