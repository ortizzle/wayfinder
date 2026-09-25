/* v175 — Chemistry · 3 Density and Buoyancy (Wayfinder only).
   Built from River's completed 20/20 Density/Buoyancy lesson check.

   What this guards beyond the ordinary shelving/round checks:
     - it is part THREE of the Chemistry shelf, behind Phases of Matter and
       Phase Changes, and it carries the numbered form the whole shelf uses;
     - the two things the paper LEANS ON but never states — the formula and
       water's 1 g/cm³ — are both present and both flagged as ours, not her
       class's, since inventing provenance would borrow the school's authority;
     - every one of the sheet's own twenty ideas is taught, asserted by its
       TEACHING rather than by question id, which would not survive a renumber.
   She made no mistakes on this paper, so unlike v161 and v165 there is no
   correction to pin — what has to hold is coverage. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8403;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  /* Seed the WHOLE science subject, both shelves, so "its own place on the
     Chemistry shelf" is a claim about coexistence and not about an empty
     subject screen. */
  const seed = await p.evaluate(async () => {
    const files = ['science-quiz-1','science-measurement','science-variables','science-scales',
                   'science-nos-practice','science-nos-test',
                   'science-phases-matter','science-phase-changes','science-density-buoyancy'];
    for (const f of files) {
      const j = await (await fetch('./content/'+f+'.json',{cache:'no-store'})).json();
      const u = Object.values(j.records).find(x=>x.type==='unit');
      u.status='approved'; u.updatedAt=Date.now()-1000; DATA.records[u.id]=u;
    }
    saveLocal();
    const u = DATA.records['unit-sci-dens'];
    return {classId:u.classId, title:u.title, libv:u.libv, order:u.order, prep:u.prep,
            cards:u.cards, qs:u.questions, sorts:u.sorts,
            note:(u.parentNote||{}).text || '', blob: JSON.stringify(u)};
  });

  // The v136 orphan trap: a classId CLASS_BY_ID does not know shelves nowhere
  // and raises no error anywhere.
  ck('it loads under the real science classId', seed.classId === 'science', seed.classId);
  ck('it carries a libv and sets no order bucket',
     seed.libv >= 1 && seed.order == null, [seed.libv, seed.order]);
  /* Measured, not assumed: an UNNUMBERED "Chemistry · Density and Buoyancy"
     still sorts last today, because numeric-aware collation puts digits ahead
     of letters and parts 1 and 2 are numbered. So the 3 is not fixing a live
     inversion the way v162's numbers were — it is the v180 rule, that mixing
     the two forms inside one shelf IS the bug, and it becomes load-bearing the
     moment a part 4 arrives whose title would sort ahead of "Density". */
  ck('it carries the NUMBERED form, so the shelf sorts structurally',
     /^Chemistry · 3 Density and Buoyancy$/.test(seed.title), seed.title);
  /* v139: prep says what a unit IS. This is the lesson itself. */
  ck('it is not flagged prep — it is the lesson, not test prep', !seed.prep, seed.prep);
  ck('at least 16 cards and 17 questions, every MC with four unique options',
     seed.cards.length >= 16 && seed.qs.length >= 17 &&
     seed.qs.filter(q => (q.kind||'mc') === 'mc')
            .every(q => q.opts.length === 4 && new Set(q.opts).size === 4),
     [seed.cards.length, seed.qs.length]);
  ck('correct answers are spread across all four positions',
     [0,1,2,3].every(i => seed.qs.some(q => (q.kind||'mc')==='mc' && q.ans === i)),
     [0,1,2,3].map(i => seed.qs.filter(q=>q.ans===i).length));

  // The standalone rule, both halves.
  const stems = seed.qs.map(q => q.q + ' ' + q.steps.join(' ')).join(' ');
  ck('no question references the worksheet it was built from',
     !/\b(the )?(worksheet|practice sheet|the sheet|question \d)\b/i.test(stems), 'ok');
  ck('no stem opens on a neighbour\'s scenario',
     !seed.qs.some(q => /^(the|that) same\b/i.test(q.q.trim())) && !/\bthat same\b/i.test(stems),
     seed.qs.filter(q=>/^(the|that) same\b/i.test(q.q.trim())).map(q=>q.id));
  ck('no question refers to an option by position',
     !/\b(first|second|third|last) (two |three )?options?\b|all of the above/i.test(
        seed.qs.map(q=>q.q+' '+q.steps.join(' ')+' '+q.ex.main).join(' ')), 'ok');

  /* The shelf: three parts in teaching order, the Nature of Science run
     untouched beside it, nothing loose. */
  const shelf = await p.evaluate(() => {
    const s = shelvesFor('science');
    return {names: s.shelves.map(x=>x.name), loose: s.loose.length,
            chem: (s.shelves.find(x=>x.name==='Chemistry')||{units:[]}).units.map(u=>u.id),
            sci: (s.shelves.find(x=>x.name==='Science')||{units:[]}).units.map(u=>lessonLabel(u))};
  });
  ck('Chemistry runs Phases → Phase Changes → Density, nothing loose',
     shelf.chem.join() === 'unit-sci-phases,unit-sci-phasechg,unit-sci-dens' && shelf.loose === 0,
     shelf);
  ck('the Nature of Science shelf still runs Quiz 1 → Study Test, unchanged',
     shelf.sci.length === 6 && /^Quiz 1: /.test(shelf.sci[0]) && /Study Test$/.test(shelf.sci[5]),
     shelf.sci);

  /* The two additions, by their teaching AND by their provenance. Flagging
     these 'source' would put the school's name on something its paper never
     said, which is the one failure the provenance scheme exists to prevent. */
  const card = t => seed.cards.find(c => new RegExp(t,'i').test(c.term)) || {};
  const formula = card('^the formula$'), water = card('density of water');
  ck('the formula is taught, with an eq, and flagged as ours not the class\'s',
     /mass ÷ volume/i.test(formula.def||'') && /mass \/ volume/.test(formula.eq||'') &&
     formula.from === 'added', [formula.def && formula.def.slice(0,40), formula.eq, formula.from]);
  ck('water\'s 1 g/cm³ is taught, and flagged as ours too',
     /1 g\/cm³/.test(water.def||'') && /floats/.test(water.def||'') && /sinks/.test(water.def||'') &&
     water.from === 'added', [water.def && water.def.slice(0,40), water.from]);
  ck('the parent note names both of them as leaned-on-but-unstated',
     /never (giv|say)/i.test(seed.note) && /1 g\/cm³/.test(seed.note) &&
     /20 out of 20/.test(seed.note), seed.note.slice(0,80));

  /* Every idea her twenty questions actually test, asserted by teaching.
     A question id would not survive a renumber; the teaching has to. */
  const teach = seed.blob;
  const has = (label, re) => ck(label, new RegExp(re,'i').test(teach.replace(/\\n/g,'\n')), label);
  has('density is taught as comparing mass AND volume', 'mass and how much space|mass ÷ volume');
  has('particle packing is taught as how you read density off a picture', 'packed into');
  has('same-size-different-density is taught with mass as the only difference',
      'only the mass can be different');
  has('the phase order is taught as solid, liquid, gas', 'solid, then liquid, then gas');
  has('subtracting the container to find a mass is taught', 'empty (dish|container)');
  has('the prism volume formula is taught', 'length × width × height');
  has('buoyancy is named as the upward push', 'upward');
  has('heating a liquid is taught as making it less dense and rising', 'less dense.*rises|rises');
  has('cooling a liquid is taught as making it denser and sinking', 'denser.*sinks|sinks back');
  has('convection is named as the movement of warm and cool fluid', 'convection');
  /* The steel-ship idea is the one place the sheet's own float/sink rule could
     look violated, so it has to be taught with the whole-object averaging. */
  has('the steel ship is explained by averaging the WHOLE object', 'entire object|whole ship');
  /* v161's own unit taught the typical order; this one has to name the
     exception without contradicting it, since her Q5 said "typical". */
  has('water is named as the exception to the phase order, because ice floats',
      'LESS dense than liquid water');

  // A genuine ranking question, in the right order, and a real physical loop.
  const ord = seed.qs.find(q => q.kind === 'order');
  ck('the convection loop ships as a kind:order question, heat → rise → cool → sink',
     ord && ord.opts.length === 4 && ord.ans === 0 &&
     /heated/i.test(ord.opts[0]) && /rises/i.test(ord.opts[1]) &&
     /cools/i.test(ord.opts[2]) && /sinks/i.test(ord.opts[3]), ord && ord.opts);

  // The sort set.
  const set = seed.sorts && seed.sorts[0];
  ck('one sort set, 12 items, both buckets used, a why on every item',
     seed.sorts.length === 1 && set.items.length === 12 &&
     set.items.some(i=>i.k==='a') && set.items.some(i=>i.k==='b') &&
     set.items.every(i=>i.why && i.why.length > 10), set && set.items.length);
  /* The checker's own-bucket rule, restated here on the words that actually
     matter: an item that says "floats" or "sinks" answers itself. */
  ck('no sort item gives away its own bucket',
     set.items.every(i => !/\b(float|sink|comes up|goes down)/i.test(i.t)),
     set.items.filter(i=>/\b(float|sink|comes up|goes down)/i.test(i.t)).map(i=>i.t));
  ck('the set deliberately includes a heavy floater and a light sinker',
     set.items.some(i=>i.k==='a' && /kg|200|trunk/i.test(i.t)) &&
     set.items.some(i=>i.k==='b' && /paperclip|small/i.test(i.t)),
     set.items.map(i=>i.k+':'+i.t.slice(0,28)));

  const sorted = await p.evaluate((sid) => {
    sortState = null; go('sort', {unitId:'unit-sci-dens', classId:'science', sortId:sid});
    const u = DATA.records['unit-sci-dens'], s = u.sorts.find(x=>x.id===sid);
    const dealt = sortState.queue.length;
    let guard = 0;
    while (sortState.queue.length && guard++ < 40) {
      if (sortState.verdict) {
        [...document.querySelectorAll('#screen .btn')].find(b=>/Got it/.test(b.textContent)).click();
        continue;
      }
      const it = s.items[sortState.queue[0]];
      const btns = [...document.querySelectorAll('#screen .sortbtns .btn')];
      (it.k === 'a' ? btns[0] : btns[1]).click();
    }
    const log = all('log').find(l => l.mode === 'sort');
    return {dealt, left: sortState.queue.length, correct: log && log.correct, xp: log && log.xp};
  }, set.id);
  ck('a clean pass through the sort set clears it and logs 12 × 3 XP',
     sorted.dealt === 12 && sorted.left === 0 && sorted.correct === 12 && sorted.xp === 36, sorted);

  // The quiz plays end to end, order question and all.
  const quiz = await p.evaluate(async () => {
    quizState = null;
    go('quiz', {unitId:'unit-sci-dens', classId:'science'});
    let guard = 0, sawOrder = false;
    while (view === 'quiz' && guard++ < 80) {
      const chips = [...document.querySelectorAll('#screen .ordchip:not([disabled])')];
      if (chips.length) { sawOrder = true; chips[0].click(); await new Promise(r=>setTimeout(r,4)); continue; }
      const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
      if (opts.length) for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,4)); }
      await new Promise(r=>setTimeout(r,8));
      const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
      if (next) { next.click(); await new Promise(r=>setTimeout(r,8)); continue; }
      if (!opts.length) break;
    }
    const l = all('log').find(x => x.unitId === 'unit-sci-dens' && x.mode === 'quiz');
    return {logged: !!l, total: l && l.total, sawOrder};
  });
  ck('a full quiz round completes and logs', quiz.logged && quiz.total >= 5, quiz);

  // And the deck walks to the end.
  const deck = await p.evaluate(async () => {
    /* Do NOT null cardState first — SCREENS.cards reads cardState.start on the
       way in and throws on a null. `go` builds it. */
    go('cards', {unitId:'unit-sci-dens', classId:'science'});
    const total = cardState.order.length;
    let seen = 0;
    while (cardState && cardState.unitId === 'unit-sci-dens' && seen < 40) {
      const knew = [...document.querySelectorAll('button')].find(b => /Knew it/.test(b.textContent));
      if (!knew) break;
      seen++; knew.click(); await new Promise(r=>setTimeout(r,5));
    }
    return {seen, total};
  });
  ck('the whole deck walks to the end, every card seen once',
     deck.total >= 16 && deck.seen === deck.total, deck);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + JSON.stringify(r.got).slice(0,300))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
