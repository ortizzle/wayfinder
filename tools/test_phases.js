/* v161 — Chemistry · Phases of Matter (Wayfinder only).
   Built from River's completed 20-point practice sheet. Two things this
   guards beyond the ordinary shelving/round checks:
     - it is its OWN shelf, not a seventh part of the Nature of Science
       sequence (which is an explicit order:0..5 run of Unit 1 material);
     - it actually teaches the four things she got wrong, by their teaching
       and not merely by their presence. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8302;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const seed = await p.evaluate(async () => {
    const files = ['science-quiz-1','science-measurement','science-variables','science-scales',
                   'science-nos-practice','science-nos-test','science-phases-matter'];
    for (const f of files) {
      const j = await (await fetch('./content/'+f+'.json',{cache:'no-store'})).json();
      const u = Object.values(j.records).find(x=>x.type==='unit');
      u.status='approved'; u.updatedAt=Date.now()-1000; DATA.records[u.id]=u;
    }
    saveLocal();
    const u = DATA.records['unit-sci-phases'];
    return {classId:u.classId, title:u.title, libv:u.libv, order:u.order, round:u.round,
            prep:u.prep, cards:u.cards, qs:u.questions, sorts:u.sorts,
            blob: JSON.stringify(u)};
  });

  ck('it loads under the real science classId', seed.classId === 'science', seed.classId);
  ck('titled onto its own Chemistry shelf, with a libv and no order bucket',
     /^Chemistry · Phases of Matter$/.test(seed.title) && seed.libv >= 1 && seed.order == null,
     [seed.title, seed.libv, seed.order]);
  ck('16 cards, 18 questions, every MC with four unique options',
     seed.cards.length === 16 && seed.qs.length === 18 &&
     seed.qs.filter(q => (q.kind||'mc') === 'mc')
            .every(q => q.opts.length === 4 && new Set(q.opts).size === 4),
     [seed.cards.length, seed.qs.length]);
  ck('correct answers are spread across all four positions',
     [0,1,2,3].every(i => seed.qs.some(q => (q.kind||'mc')==='mc' && q.ans === i)),
     [0,1,2,3].map(i => seed.qs.filter(q=>q.ans===i).length));

  // The standalone rule: nothing may point back at the worksheet it came from.
  ck('no question references the worksheet it was built from',
     !/\b(the )?(worksheet|practice sheet|the sheet|question \d)\b/i.test(
        seed.qs.map(q => q.q + ' ' + q.steps.join(' ')).join(' ')), 'ok');

  // A new shelf, and the Nature of Science run left exactly as it was.
  const shelf = await p.evaluate(() => {
    const s = shelvesFor('science');
    return {names: s.shelves.map(x=>x.name), loose: s.loose.length,
            chem: (s.shelves.find(x=>x.name==='Chemistry')||{units:[]}).units.map(u=>u.id),
            sci: (s.shelves.find(x=>x.name==='Science')||{units:[]}).units.map(u=>lessonLabel(u))};
  });
  ck('Chemistry is its own shelf holding this unit, nothing loose',
     shelf.names.includes('Chemistry') && shelf.chem.join() === 'unit-sci-phases' && shelf.loose === 0,
     shelf);
  ck('the Nature of Science shelf still runs Quiz 1 → Study Test, unchanged',
     shelf.sci.length === 6 && /^Quiz 1: /.test(shelf.sci[0]) && /Study Test$/.test(shelf.sci[5]),
     shelf.sci);

  // The four things she actually got wrong, checked by their teaching.
  const teach = seed.blob;
  ck('temperature is taught as particle SPEED, and closeness is named as the mix-up',
     /how FAST the particles/.test(teach) && /not\s*\n?how close together they are/.test(teach.replace(/\\n/g,'\n')) &&
     /squeeze a gas into a tiny can/.test(teach), 'see card "Temperature" / "Fast, not close"');
  ck('a solid is taught as keeping BOTH its shape and its volume',
     /A solid keeps its own shape AND its own volume/.test(teach), 'see card "Solid"');
  ck('moving a solid is taught as "nothing happens"',
     /Nothing happens\. Neither the shape nor the volume changes/.test(teach),
     'see card "Moving a solid to a new container"');
  const gasCard = (seed.cards.find(c => /gas to a new container/i.test(c.term)) || {}).def || '';
  ck('a gas is taught as resizing to its container, with the liquid answer named as the trap',
     /bigger container, bigger volume; smaller container, smaller volume/.test(gasCard) &&
     /"the volume stays the same" is the LIQUID answer/.test(gasCard), gasCard.slice(0,120));

  // A real ranking question, in the right order.
  const ord = seed.qs.find(q => q.kind === 'order');
  ck('the energy ranking ships as a kind:order question, ice → steam',
     ord && ord.opts.length === 4 && ord.ans === 0 &&
     /ice/i.test(ord.opts[0]) && /steam/i.test(ord.opts[3]), ord && ord.opts);

  // The sort set: is it matter?
  const set = seed.sorts && seed.sorts[0];
  ck('one sort set, 12 items, both buckets used, a why on every item',
     seed.sorts.length === 1 && set.items.length === 12 &&
     set.items.some(i=>i.k==='a') && set.items.some(i=>i.k==='b') &&
     set.items.every(i=>i.why && i.why.length > 10), set && set.items.length);
  ck('no sort item names its own bucket',
     set.items.every(i => !/\bmatter\b/i.test(i.t)),
     set.items.filter(i=>/\bmatter\b/i.test(i.t)).map(i=>i.t));

  const sorted = await p.evaluate((sid) => {
    sortState = null; go('sort', {unitId:'unit-sci-phases', classId:'science', sortId:sid});
    const u = DATA.records['unit-sci-phases'], s = u.sorts.find(x=>x.id===sid);
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

  // And the quiz itself plays end to end.
  const quiz = await p.evaluate(async () => {
    quizState = null;
    go('quiz', {unitId:'unit-sci-phases', classId:'science'});
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
    const l = all('log').find(x => x.unitId === 'unit-sci-phases' && x.mode === 'quiz');
    return {logged: !!l, total: l && l.total, sawOrder};
  });
  ck('a full quiz round completes and logs', quiz.logged && quiz.total === 9, quiz);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + JSON.stringify(r.got).slice(0,300))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
