/* Arizona latitude/longitude practice map (v143): further practice for
   Unit 5, built on renderGraph()'s existing pts-series + marked-points
   mechanism — a simplified Arizona outline plus real cities, rounded to
   the nearest degree. renderGraph() gained optional g.xabs/g.yabs +
   g.xsuf/g.ysuf so a signed-degree map can still show "112°W" on its
   axis instead of "-112". */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8302;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const seed = await p.evaluate(async () => {
    const j = await (await fetch('./content/az-latlong.json', {cache:'no-store'})).json();
    const u = Object.values(j.records)[0];
    u.status = 'approved'; u.updatedAt = Date.now() - 1000;
    DATA.records[u.id] = u;
    saveLocal();
    return { cards: u.cards.length, questions: u.questions.length, classId: u.classId,
              graphed: u.questions.filter(q=>q.graph).length,
              order: u.questions.filter(q=>q.kind==='order').length };
  });
  ck('unit-az-latlong seeds: 11 cards, 17 questions, classId history',
     seed.cards===11 && seed.questions===17 && seed.classId==='history', seed);
  ck('10 of the questions carry their own map graph, and 2 are put-in-order',
     seed.graphed===10 && seed.order===2, seed);

  // renderGraph itself: the axis suffix/abs formatting is correct, and the
  // outline + marked cities all render as real SVG elements.
  const rendered = await p.evaluate(() => {
    const u = DATA.records['unit-az-latlong'];
    const g = u.cards.find(c=>c.graph).graph;
    const svg = renderGraph(g);
    const texts = [...svg.querySelectorAll('text')].map(t=>t.textContent);
    return {
      hasW: texts.some(t=>/°W$/.test(t)), hasN: texts.some(t=>/°N$/.test(t)),
      noNegative: !texts.some(t=>t.includes('-')),
      dots: svg.querySelectorAll('circle').length,
      outlinePoints: svg.querySelectorAll('polyline').length,
      cityLabel: texts.includes('Phoenix')
    };
  });
  ck('axis ticks read like "112°W"/"33°N", never a bare negative number',
     rendered.hasW && rendered.hasN && rendered.noNegative, rendered);
  ck('the outline draws as a polyline and every city is a marked dot with its name',
     rendered.outlinePoints>=1 && rendered.dots===4 && rendered.cityLabel, rendered);

  // A full quiz round completes, including the map questions and the two
  // order questions, with no console errors from the new graph fields.
  const quiz = await p.evaluate(async () => {
    quizState = null;
    go('quiz', {unitId:'unit-az-latlong', classId:'history'});
    let guard = 0, sawGraph = false;
    while (view === 'quiz' && guard++ < 30) {
      if (document.querySelector('#screen svg')) sawGraph = true;
      const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
      if (opts.length) for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,4)); }
      await new Promise(r => setTimeout(r, 8));
      const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
      if (next) { next.click(); await new Promise(r=>setTimeout(r,8)); continue; }
      if (!opts.length) break;
    }
    return { logged: all('log').some(l => l.unitId === 'unit-az-latlong'), sawGraph };
  });
  ck('a full quiz round completes and logs', quiz.logged, quiz);
  ck('at least one map renders live inside the quiz', quiz.sawGraph, quiz);

  // Walk rounds until an order-kind question is served, to confirm it plays.
  const orderPlay = await p.evaluate(async () => {
    for (let round = 0; round < 8; round++) {
      quizState = null;
      go('quiz', {unitId:'unit-az-latlong', classId:'history'});
      let guard = 0;
      while (view === 'quiz' && guard++ < 30) {
        const u = unitFor('unit-az-latlong');
        const q = u.questions[quizState.order[quizState.i]];
        if (q && q.kind === 'order') {
          const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
          for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,4)); }
          const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
          const hadSvg = !!document.querySelector('#screen svg');
          if (next) next.click();
          return { found: true, hadSvg };
        }
        const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
        if (opts.length) for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,4)); }
        await new Promise(r=>setTimeout(r,8));
        const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
        if (next) { next.click(); await new Promise(r=>setTimeout(r,8)); continue; }
        if (!opts.length) break;
      }
    }
    return { found: false };
  });
  ck('an order question plays with its map visible', orderPlay.found && orderPlay.hadSvg, orderPlay);

  // Flashcards run clean, including the one card that carries a graph.
  // "Flip it" and "Knew it" are both .btn-primary, toggled by display:none
  // rather than removed — a visibility check (offsetParent) is required to
  // find the one actually on screen.
  const cards = await p.evaluate(async () => {
    go('cards', {unitId:'unit-az-latlong', classId:'history'});
    let seen = 0, guard = 0, sawGraph = false;
    while (view === 'cards' && guard++ < 40) {
      if (document.querySelector('#screen svg')) sawGraph = true;
      const nx = [...document.querySelectorAll('#screen .btn-primary')].find(b => b.offsetParent);
      if (!nx) break;
      nx.click(); seen++;
      await new Promise(r => setTimeout(r, 6));
    }
    return { seen, sawGraph };
  });
  ck('the 11-card deck steps through cleanly and the map card renders', cards.seen>=9 && cards.sawGraph, cards);

  out.forEach(r => console.log((r.ok ? '  ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' → ' + JSON.stringify(r.got).slice(0,300))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
