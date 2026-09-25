/* v175 — History Unit 5, a three-part shelf (Wayfinder only).

   Built from her class's OPTIONAL Unit 5 Test Study Guide, an image-only scan
   read page by page with pypdfium2. The guide is BLANK, so unlike the two
   science sheets there is nothing of hers to repair — what has to hold is
   COVERAGE of all thirty-three of its items, and the scoping that keeps part
   two from being re-taught.

   The three things this guards that no ordinary round check would:
     - the Unit 5 SHELF, with the lat/long unit retitled onto it keeping its
       id, and the History shelf left exactly as it was;
     - that parts 1 and 3 do NOT re-teach latitude and longitude, which part 2
       already covers (the v142/v189 scoping discipline);
     - that every section of the guide is taught, asserted by its TEACHING
       rather than by question id, which would not survive a renumber. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8403;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  /* Seed every history unit, so "its own shelf" is a claim about coexistence
     with the existing History shelf rather than about an empty subject. */
  const seed = await p.evaluate(async () => {
    const files = ['history-5ws','history-u2-u3-review','az-latlong',
                   'history-u5-p1','history-u5-p3'];
    for (const f of files) {
      const j = await (await fetch('./content/'+f+'.json',{cache:'no-store'})).json();
      const u = Object.values(j.records).find(x=>x.type==='unit');
      u.status='approved'; u.updatedAt=Date.now()-1000; DATA.records[u.id]=u;
    }
    saveLocal();
    const pick = id => { const u = DATA.records[id];
      return {id:u.id, classId:u.classId, title:u.title, libv:u.libv, order:u.order,
              prep:u.prep, cards:u.cards, qs:u.questions, sorts:u.sorts,
              note:(u.parentNote||{}).text||'', blob: JSON.stringify(u)}; };
    return {p1: pick('unit-hist-u5-p1'), p2: pick('unit-az-latlong'), p3: pick('unit-hist-u5-p3')};
  });
  const P = [seed.p1, seed.p2, seed.p3];

  // The v136 orphan trap.
  ck('all three parts load under the real history classId',
     P.every(u => u.classId === 'history'), P.map(u=>u.classId));
  ck('all three carry a libv and set no order bucket',
     P.every(u => u.libv >= 1 && u.order == null), P.map(u=>[u.libv,u.order]));
  /* The numbered form, and it is genuinely load-bearing here: measured, a
     plain "History · Unit 5 Review" sorts AHEAD of the existing
     "History · Units 2–3 Review" on the History shelf, because a space beats
     an 's'. The separate numbered shelf is what avoids that. */
  ck('all three carry the numbered Unit 5 form',
     /^Unit 5 · 1 Features, Maps and Directions$/.test(seed.p1.title) &&
     /^Unit 5 · 2 Latitude and Longitude$/.test(seed.p2.title) &&
     /^Unit 5 · 3 Time Zones, Elevation and the Globe$/.test(seed.p3.title),
     P.map(u=>u.title));
  /* Retitled, never re-minted — the standing rule. Its id is what her qstats
     and any Growth Zone misses are attached to. */
  ck('the lat/long unit kept its original id through the retitle',
     seed.p2.id === 'unit-az-latlong', seed.p2.id);
  ck('the lat/long unit bumped libv for the retitle', seed.p2.libv >= 5, seed.p2.libv);
  /* v139: prep says what a unit IS. These are the lessons behind a study
     guide, and the guide itself is the test-prep object. */
  ck('none of the three is flagged prep', P.every(u => !u.prep), P.map(u=>u.prep));

  ck('parts 1 and 3 carry real decks and banks, every MC with four unique options',
     seed.p1.cards.length >= 16 && seed.p1.qs.length >= 18 &&
     seed.p3.cards.length >= 14 && seed.p3.qs.length >= 17 &&
     [seed.p1, seed.p3].every(u => u.qs.filter(q=>(q.kind||'mc')==='mc')
        .every(q => q.opts.length === 4 && new Set(q.opts).size === 4)),
     [[seed.p1.cards.length, seed.p1.qs.length],[seed.p3.cards.length, seed.p3.qs.length]]);
  ck('answers are spread across all four positions in both new parts',
     [seed.p1, seed.p3].every(u =>
       [0,1,2,3].every(i => u.qs.some(q => (q.kind||'mc')==='mc' && q.ans === i))),
     [seed.p1, seed.p3].map(u => [0,1,2,3].map(i=>u.qs.filter(q=>q.ans===i).length)));

  // Standalone, both halves.
  const stems = [seed.p1, seed.p3].map(u =>
    u.qs.map(q => q.q + ' ' + q.steps.join(' ')).join(' ')).join(' ');
  ck('no question references the study guide it was built from',
     !/\b(the )?(study guide|worksheet|the sheet|question \d)\b/i.test(stems), 'ok');
  /* Anchored to the STEM, deliberately. The documented failure is a stem that
     OPENS on a neighbour's scenario — "The same student…", "That same stone…".
     A loose sweep for "that same" flags a step reading "a different map could
     use that same brown", which restates nothing: the v185 lesson, verbatim. */
  ck('no stem opens on a neighbour\'s scenario',
     ![seed.p1, seed.p3].some(u => u.qs.some(q => /^(the|that) same\b/i.test(q.q.trim()))),
     [seed.p1, seed.p3].flatMap(u => u.qs.filter(q=>/^(the|that) same\b/i.test(q.q.trim())).map(q=>q.id)));
  ck('no question refers to an option by position',
     !/\b(first|second|third|last) (two |three )?options?\b|all of the above/i.test(
        [seed.p1, seed.p3].map(u => u.qs.map(q=>q.q+' '+q.steps.join(' ')+' '+q.ex.main).join(' ')).join(' ')),
     'ok');

  /* The guide's own examples are her homework. Answering from memory of the
     page teaches nothing, so none of them may be a graded item. */
  const ownExamples = [/old faithful/i, /lake michigan/i, /\bchandler\b/i,
                       /canadian province/i, /favou?rite (fast )?food/i,
                       /\bshanghai\b/i, /albrecht/i, /pony express/i, /\bottawa\b/i];
  const gradedBlob = [seed.p1, seed.p3].map(u =>
    u.qs.map(q => q.q + ' ' + q.opts.join(' ')).join(' ')).join(' ');
  ck('none of the guide\'s own examples is used as a graded question',
     !ownExamples.some(re => re.test(gradedBlob)),
     ownExamples.filter(re => re.test(gradedBlob)).map(String));

  /* The scoping claim. Part 2 owns latitude and longitude; parts 1 and 3 must
     not re-ask it, or the shelf teaches the same thing twice and the round
     she gets is half repeats. */
  const latlong = /\b(latitude|longitude|equator|prime meridian)\b/i;
  ck('parts 1 and 3 ask no question whose ANSWER is a latitude/longitude fact',
     ![seed.p1, seed.p3].some(u => u.qs.some(q =>
        latlong.test(q.q) || latlong.test(String(q.opts[q.ans])))),
     [seed.p1, seed.p3].flatMap(u => u.qs.filter(q =>
        latlong.test(q.q) || latlong.test(String(q.opts[q.ans]))).map(q=>q.id)));

  // The shelf itself.
  const shelf = await p.evaluate(() => {
    const s = shelvesFor('history');
    return {names: s.shelves.map(x=>x.name), loose: s.loose.length,
            u5: (s.shelves.find(x=>x.name==='Unit 5')||{units:[]}).units.map(u=>u.id),
            hist: (s.shelves.find(x=>x.name==='History')||{units:[]}).units.map(u=>u.id)};
  });
  ck('Unit 5 is its own shelf, parts 1 → 2 → 3, nothing loose',
     shelf.u5.join() === 'unit-hist-u5-p1,unit-az-latlong,unit-hist-u5-p3' && shelf.loose === 0,
     shelf);
  ck('the existing History shelf still holds its two parts, untouched',
     shelf.hist.join() === 'unit-hist-5ws,unit-hist-u2u3', shelf.hist);
  /* The measured reason the shelf is separate: a plain "Unit 5 Review" title
     on the History shelf lands AHEAD of "Units 2–3 Review". */
  const invert = await p.evaluate(() => {
    DATA.records.tmpX = {id:'tmpX', type:'unit', classId:'history', status:'approved',
      title:'History · Unit 5 Review: Maps and Geography', cards:[], questions:[],
      updatedAt: Date.now()};
    const got = (shelvesFor('history').shelves.find(x=>x.name==='History')||{units:[]})
      .units.map(u=>u.id);
    delete DATA.records.tmpX;
    return got;
  });
  ck('a plain Unit 5 title really would invert with Units 2–3 (why the shelf is separate)',
     invert.indexOf('tmpX') < invert.indexOf('unit-hist-u2u3'), invert);

  // Every section of the guide, by its teaching.
  const t1 = seed.p1.blob.replace(/\\n/g,'\n'), t3 = seed.p3.blob.replace(/\\n/g,'\n');
  const has = (label, blob, re) => ck(label, new RegExp(re,'i').test(blob), label);
  has('§1 human features are defined as created by human beings', t1, 'created by human beings');
  has('§1 natural features are defined as not created by human beings', t1, 'did NOT make|not created by human');
  /* The single likeliest item on the page to be marked wrong: the prime
     meridian sits in a list with a geyser, a lake and a city and IS human. */
  has('§1 an agreed line is taught as a HUMAN feature, not a natural one', t1,
      'human features, even though you cannot touch them|people agreed where to draw');
  ck('§2 all four map types are named with what each shows',
     ['physical map','political map','climate map','cultural map']
       .every(n => new RegExp(n,'i').test(t1)) &&
     /permanent weather conditions/i.test(t1) && /behaviors of a country/i.test(t1),
     'see the four map cards');
  has('§3 the compass rose is taught as what tells you which way is north', t1, 'which way is north');
  has('§3 the intermediate directions are named', t1, 'northeast, northwest, southeast and southwest');
  has('§4 a grid map is taught as letters down the side, numbers across the top', t1,
      'Letters run down the side, numbers run across the top');
  has('§6 six US time zones, four between the coasts', t3, 'four of them lie between the East and West');
  has('§6 east-forward / west-back is taught as the one rule', t3,
      'Travel EAST and you set the clock forward');
  has('§6 crossing midnight changing the DAY is taught', t3, 'the day changes with it');
  has('§6 the international date line is taught with both directions', t3,
      'heading WEST and you jump forward a day');
  has('§7 elevation is height above sea level', t3, 'How high the land is above sea level');
  has('§7 peak and valley are both defined', t3, 'highest point, of a mountain');
  ck('§8 oceans ~70% and continents ~30% are both taught',
     /seven tenths of the surface is ocean/i.test(t3) &&
     /three tenths of the surface is land/i.test(t3), 'see the two globe cards');
  ck('§8 seven continents and five oceans are both listed',
     /Africa, Antarctica, Asia, Australia, Europe/i.test(t3) &&
     /Pacific, Atlantic, Indian, Arctic and Antarctic/i.test(t3), 'see the globe cards');
  /* Her class map names it the Antarctic Ocean; a lot of books say Southern.
     Both reach her, so the card says so rather than letting her guess. */
  has('§8 her class\'s name for the Southern Ocean is the one taught first', t3,
      'Antarctic Ocean is also called the Southern Ocean');
  /* Real, relevant to a child who lives here, and deliberately NOT allowed to
     cast doubt on a test answer. */
  has('Arizona\'s no-daylight-saving quirk is an aside that still names the test answer', t3,
      'Arizona is in the Mountain zone, and that is the answer to use');

  /* The gap her guide exposed in the unit that already existed: items 20 and
     21 grade on the WORDS parallels and meridians, and "parallel" appeared
     nowhere in that record before this. */
  ck('part 2 gained the words "parallels" and "meridians" it was graded on',
     /parallels are the lines of latitude/i.test(seed.p2.blob.replace(/\\n/g,'\n')) &&
     seed.p2.qs.some(q => /other name for the lines of latitude/i.test(q.q)),
     'see the Parallels and meridians card');

  // The sort set on part 1.
  const set = seed.p1.sorts && seed.p1.sorts[0];
  ck('part 1 ships one sort set, 12 items, both buckets, a why on each',
     seed.p1.sorts.length === 1 && set.items.length === 12 &&
     set.items.some(i=>i.k==='a') && set.items.some(i=>i.k==='b') &&
     set.items.every(i=>i.why && i.why.length > 10), set && set.items.length);
  ck('no sort item names its own bucket',
     set.items.every(i => !/\b(natural|made by people|human)\b/i.test(i.t)),
     set.items.filter(i=>/\b(natural|made by people|human)\b/i.test(i.t)).map(i=>i.t));
  /* The trap the guide is most likely to catch her on has to actually be in
     the pile, or the sort is only drilling the easy half. */
  ck('the sort includes an agreed line, which is the trap',
     set.items.filter(i => i.k === 'b' && /equator|where one state stops/i.test(i.t)).length === 2,
     set.items.filter(i=>i.k==='b').map(i=>i.t.slice(0,30)));

  const sorted = await p.evaluate((sid) => {
    sortState = null; go('sort', {unitId:'unit-hist-u5-p1', classId:'history', sortId:sid});
    const u = DATA.records['unit-hist-u5-p1'], s = u.sorts.find(x=>x.id===sid);
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
  ck('a clean pass through the sort clears it and logs 12 × 3 XP',
     sorted.dealt === 12 && sorted.left === 0 && sorted.correct === 12 && sorted.xp === 36, sorted);

  // The time-zone ranking, in the right order.
  const ord = seed.p3.qs.find(q => q.kind === 'order');
  ck('the zones ship as a kind:order question, Pacific → Eastern',
     ord && ord.opts.length === 4 && ord.ans === 0 &&
     /Pacific/.test(ord.opts[0]) && /Mountain/.test(ord.opts[1]) &&
     /Central/.test(ord.opts[2]) && /Eastern/.test(ord.opts[3]), ord && ord.opts);

  // Both new parts play a full round, and both decks walk to the end.
  for (const id of ['unit-hist-u5-p1','unit-hist-u5-p3']) {
    const quiz = await p.evaluate(async (uid) => {
      quizState = null;
      go('quiz', {unitId:uid, classId:'history'});
      let guard = 0;
      while (view === 'quiz' && guard++ < 80) {
        const chips = [...document.querySelectorAll('#screen .ordchip:not([disabled])')];
        if (chips.length) { chips[0].click(); await new Promise(r=>setTimeout(r,4)); continue; }
        const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
        if (opts.length) for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,4)); }
        await new Promise(r=>setTimeout(r,8));
        const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
        if (next) { next.click(); await new Promise(r=>setTimeout(r,8)); continue; }
        if (!opts.length) break;
      }
      const l = all('log').find(x => x.unitId === uid && x.mode === 'quiz');
      return {logged: !!l, total: l && l.total};
    }, id);
    ck('a full quiz round completes and logs on ' + id, quiz.logged && quiz.total >= 5, quiz);

    const deck = await p.evaluate(async (uid) => {
      /* Do NOT null cardState first — SCREENS.cards reads cardState.start on
         the way in. `go` builds it. */
      go('cards', {unitId:uid, classId:'history'});
      const total = cardState.order.length;
      let seen = 0;
      while (cardState && cardState.unitId === uid && seen < 40) {
        const knew = [...document.querySelectorAll('button')].find(b => /Knew it/.test(b.textContent));
        if (!knew) break;
        seen++; knew.click(); await new Promise(r=>setTimeout(r,5));
      }
      return {seen, total};
    }, id);
    ck('the whole deck walks to the end on ' + id,
       deck.total >= 14 && deck.seen === deck.total, deck);
  }

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + JSON.stringify(r.got).slice(0,300))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
