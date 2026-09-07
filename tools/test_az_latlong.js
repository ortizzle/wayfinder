/* Latitude/longitude practice map (v144): built from the real US map used
   in class (Arizona Geographic Alliance "US Bingo" sheet, in her Drive
   folder) rather than an invented Arizona-only outline. Chris also asked
   that flashcards not quiz exact coordinates for a place — every card and
   question that asked "what is City X's coordinate" or "which city is at
   this coordinate" is gone; what's left is comparison (furthest N/S/E/W,
   ranking) and estimation (reading between gridlines), all answerable only
   from the map shown. renderGraph() gained optional g.xabs/g.yabs +
   g.xsuf/g.ysuf so a signed-degree map can still show "112°W" on its axis
   instead of "-112". */
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
  ck('unit-az-latlong seeds: 9 cards, 18 questions, classId history',
     seed.cards===9 && seed.questions===18 && seed.classId==='history', seed);
  ck('11 of the questions carry their own map graph, and 2 are put-in-order',
     seed.graphed===11 && seed.order===2, seed);

  // Content safety: no card states a city's exact coordinate as a fact to
  // memorize (the thing Chris asked to remove), and no question's whole
  // point is "what is/which city is at this exact coordinate" — every
  // surviving question is comparison, ranking, or grid-arithmetic instead.
  const safety = await p.evaluate(() => {
    const u = DATA.records['unit-az-latlong'];
    const cityCoordCard = u.cards.find(c => /roughly\s*\d+°[NS],\s*\d+°[EW]/i.test(c.def||''));
    const lookupQ = u.questions.filter(q =>
      /what (is|are) .*coordinate/i.test(q.q||'') || /which city is (at|closest to) \d/i.test(q.q||''));
    return { cityCoordCard: cityCoordCard ? cityCoordCard.id : null, lookupQIds: lookupQ.map(q=>q.id) };
  });
  ck('no card states a specific city\'s exact coordinate as a fact to memorize',
     !safety.cityCoordCard, safety);
  ck('no question asks to state or match a specific city\'s exact coordinate',
     safety.lookupQIds.length===0, safety);

  // renderGraph itself: the axis suffix/abs formatting is correct, and the
  // marked cities render as real SVG elements (no outline is drawn — the
  // continental US coastline was deliberately not attempted).
  const rendered = await p.evaluate(() => {
    const u = DATA.records['unit-az-latlong'];
    const g = u.cards.find(c=>c.graph).graph;
    const svg = renderGraph(g);
    const texts = [...svg.querySelectorAll('text')].map(t=>t.textContent);
    return {
      hasW: texts.some(t=>/°W$/.test(t)), hasN: texts.some(t=>/°N$/.test(t)),
      noNegative: !texts.some(t=>t.includes('-')),
      dots: svg.querySelectorAll('circle').length,
      cityLabel: texts.includes('Seattle')
    };
  });
  ck('axis ticks read like "112°W"/"33°N", never a bare negative number',
     rendered.hasW && rendered.hasN && rendered.noNegative, rendered);
  ck('every marked city on the overview card renders as a dot with its name',
     rendered.dots===8 && rendered.cityLabel, rendered);

  // Atlas treatment (Chris, 2026-09: "make the map have its own white
  // background so it looks like it was ripped out of an Atlas"). Every
  // graph in this unit carries atlas:true; graphNode() should turn that
  // into the .graph-wrap.atlas class every one of them renders through.
  const atlas = await p.evaluate(() => {
    const u = DATA.records['unit-az-latlong'];
    const allAtlas = u.cards.filter(c=>c.graph).every(c=>c.graph.atlas===true)
      && u.questions.filter(q=>q.graph).every(q=>q.graph.atlas===true)
      && u.mapRef.atlas===true;
    const wrap = graphNode(u.mapRef);
    return { allAtlas, hasClass: wrap.classList.contains('atlas') };
  });
  ck('every graph in the unit (cards, questions, mapRef) is flagged atlas:true, and graphNode renders the class',
     atlas.allAtlas && atlas.hasClass, atlas);

  // No two text elements overlap on ANY graph in the unit — city labels
  // (real bug: San Francisco's label ran into Denver's on the overview
  // card, and a deliberately-close comparison pair, Chicago/Detroit, had
  // labels that physically overlapped into unreadable text) AND axis tick
  // labels (real bug: 12 longitude ticks in a 300-unit viewBox measured
  // ~29px wide, ~21px apart — genuinely overlapping — fixed with g.lx
  // labeling only every other gridline while every gridline still draws).
  const overlaps = await p.evaluate(() => {
    const u = DATA.records['unit-az-latlong'];
    const bad = [];
    const check = (graph, tag) => {
      const svg = renderGraph(graph);
      const holder = document.createElement('div'); holder.style.cssText='position:fixed;left:-9999px';
      holder.appendChild(svg); document.body.appendChild(holder);
      const boxes = [...svg.querySelectorAll('text')].map(t => ({ label: t.textContent, box: t.getBBox() }));
      for(let i=0;i<boxes.length;i++) for(let j=i+1;j<boxes.length;j++){
        const A=boxes[i].box, B=boxes[j].box;
        const ox = Math.max(0, Math.min(A.x+A.width,B.x+B.width) - Math.max(A.x,B.x));
        const oy = Math.max(0, Math.min(A.y+A.height,B.y+B.height) - Math.max(A.y,B.y));
        if(ox>2 && oy>2) bad.push(`${tag}: ${boxes[i].label} × ${boxes[j].label}`);
      }
      holder.remove();
    };
    u.cards.forEach(c => { if(c.graph) check(c.graph, 'card:'+c.id); });
    u.questions.forEach(q => { if(q.graph) check(q.graph, 'q:'+q.id); });
    if(u.mapRef) check(u.mapRef, 'mapRef');
    return bad;
  });
  ck('no two text elements (city labels or axis ticks) overlap on any graph in the unit, including the mapRef tool', overlaps.length===0, overlaps);

  // The reference-map tool (Chris: "can we make the actual map, a tool to
  // reference when questions are asked?"). A unit carrying `mapRef` gets a
  // door on its own card AND a "Map" button inside the quiz tool row, both
  // opening the same graph via openMapRef/showModal.
  const mapDoor = await p.evaluate(() => {
    const u = DATA.records['unit-az-latlong'];
    return { hasMapRef: !!u.mapRef, points: (u.mapRef.pts||[]).length };
  });
  ck('the unit carries a mapRef with every city the unit asks about (11)',
     mapDoor.hasMapRef && mapDoor.points===11, mapDoor);

  const cardDoor = await p.evaluate(() => {
    go('unit', {classId:'history'});
    // The title's " · " shelves this as a one-lesson book (seriesOf()), so
    // the unit's own card is one tap inside the shelf spine, not directly
    // on the subject screen — same as any other shelved lesson.
    const spine = [...document.querySelectorAll('#screen button')].find(b => /Latitude and Longitude/.test(b.textContent));
    if(spine) spine.click();
    const btn = [...document.querySelectorAll('#screen button')].find(b => /🗺️.*Map/.test(b.textContent));
    return { found: !!btn };
  });
  ck('the shelved unit\'s own card offers a "Map" door', cardDoor.found, cardDoor);

  const toolBtn = await p.evaluate(async () => {
    quizState = null;
    go('quiz', {unitId:'unit-az-latlong', classId:'history'});
    const before = document.querySelectorAll('.modal-overlay').length;
    const btn = [...document.querySelectorAll('#screen .tool')].find(b => /Map/.test(b.textContent));
    if(!btn) return { found:false };
    btn.click();
    await new Promise(r=>setTimeout(r,20));
    const modal = document.querySelector('.modal-overlay');
    const hasGraph = !!(modal && modal.querySelector('svg'));
    if(modal) modal.remove();
    return { found:true, opened: !before && !!modal, hasGraph };
  });
  ck('the quiz tool row offers a "Map" button that opens the reference graph',
     toolBtn.found && toolBtn.opened && toolBtn.hasGraph, toolBtn);

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
  ck('the 9-card deck steps through cleanly and the map card renders', cards.seen>=7 && cards.sawGraph, cards);

  out.forEach(r => console.log((r.ok ? '  ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' → ' + JSON.stringify(r.got).slice(0,300))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
