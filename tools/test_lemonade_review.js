/* The Lemonade Crime · Novel Test Review — the whole-book review for the
   11/20 novel test. Built ONLY from the four companion parts, so the test
   guards that: every passage is copied from them, and every proper name in
   the review appears in them. Also pins the shelf (five parts, review last),
   the prep/book flags, fresh stems, the order questions, answer spread, a
   played round with a passage plate, and the deck. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8433;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});

  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});
  const FILES = ['lemonade-crime-1','lemonade-crime-2','lemonade-crime-3','lemonade-crime-4','lemonade-crime-review'];

  const S = await p.evaluate(async (FILES) => {
    const raw = {};
    for (const f of FILES) {
      const j = await (await fetch(`./content/${f}.json`, {cache:'no-store'})).json();
      const u = Object.values(j.records)[0];
      raw[f] = JSON.parse(JSON.stringify(u));
      u.status = 'approved'; u.updatedAt = Date.now() - 1000;
      DATA.records[u.id] = u;
    }
    const plot = Object.values((await (await fetch('./content/english-plot-diagram.json', {cache:'no-store'})).json()).records)[0];
    saveLocal();
    return {raw, plot};
  }, FILES);
  const R = S.raw['lemonade-crime-review'];
  const LC = FILES.slice(0, 4).map(f => S.raw[f]);

  /* ---------------- identity and flags */
  ck('the review seeds with the companions\' classId, quarter 2, libv 1, draft',
     R.id === 'unit-lc-review' && R.classId === LC[0].classId && R.quarter === 2 && R.libv === 1
     && R.status === 'draft' && R.updatedAt < Date.now() - 3600e3,
     {classId: R.classId, quarter: R.quarter, libv: R.libv, status: R.status});
  ck('book:true and prep:true, no capstone and no order',
     R.book === true && R.prep === true && !R.capstone && R.order === undefined, R);
  ck('round about 12; ~20 cards and ~24 questions on all three levels',
     R.round === 12 && R.cards.length >= 18 && R.questions.length >= 22
     && [1,2,3].every(l => R.questions.some(q => q.lv === l)),
     {round: R.round, cards: R.cards.length, qs: R.questions.length});

  /* ---------------- sourcing guards */
  const quotable = [];
  LC.forEach(u => { u.questions.forEach(q => q.passage && quotable.push(q.passage));
                    u.cards.forEach(c => quotable.push(c.def, c.hint || '')); });
  const badPass = R.questions.filter(q => q.passage && !quotable.some(t => t.includes(q.passage))).map(q => q.id);
  ck('every passage is copied exactly from a companion passage or card',
     R.questions.filter(q => q.passage).length >= 4 && badPass.length === 0, badPass);

  const corpus = LC.map(u => JSON.stringify(u)).join(' ') + ' ' + JSON.stringify(S.plot);
  /* Ordinary words that start a sentence. Anything else capitalised must be
     a name, title or term the companions already carry. */
  const ORDINARY = new Set(['Afterwards','Age','Answer','Certain','Claim','Collecting','Either','Endings',
    'Found','Handing','Having','Letting','Many','Map','Novel','Once','Preparation','Preparing','Question',
    'Review','Seeing','Seeming','Short','Spreading','State','These','Under','Whichever','Wise','Your']);
  const caps = [...new Set(JSON.stringify(R).match(/\b[A-Z][a-zA-Z]+\b/g))];
  const invented = caps.filter(t => !ORDINARY.has(t) && !new RegExp('\\b' + t + '\\b').test(corpus));
  ck('every capitalised name in the review appears in the companion parts', invented.length === 0, invented);

  /* ---------------- fresh stems: character-bigram Dice against every companion stem */
  const bi = s => { s = s.toLowerCase().replace(/\s+/g, ' '); const m = new Map();
    for (let i = 0; i < s.length - 1; i++) { const k = s.slice(i, i+2); m.set(k, (m.get(k)||0) + 1); } return m; };
  const dice = (a, b) => { const A = bi(a), B = bi(b); let n = 0, ta = 0, tb = 0;
    A.forEach(v => ta += v); B.forEach(v => tb += v);
    A.forEach((v, k) => n += Math.min(v, B.get(k) || 0)); return 2*n / (ta + tb || 1); };
  const lcStems = LC.flatMap(u => u.questions.map(q => q.q));
  let worst = {s: 0};
  R.questions.forEach(q => lcStems.forEach(s => { const d = dice(q.q, s); if (d > worst.s) worst = {s: +d.toFixed(2), q: q.q, lc: s}; }));
  ck('no review stem duplicates a companion stem (bigram similarity < 0.75)', worst.s < 0.75, worst);

  /* ---------------- question shape */
  const ORDERS = [
    ['$208 vanishes', 'warrant', 'not guilty', 'envelope'],
    ['not symmetrical', 'lock box', 'elbow', 'television'],
  ];
  const ords = R.questions.filter(q => q.kind === 'order');
  ck('two order questions, each stored in the correct sequence with ans 0',
     ords.length >= 2 && ords.every(q => q.ans === 0 && q.opts.length === 4)
     && ORDERS.every(keys => ords.some(q => keys.every((k, i) => q.opts[i].includes(k)))),
     ords.map(q => q.opts));
  const mc = R.questions.filter(q => (q.kind || 'mc') === 'mc');
  ck('mc questions: four unique options, answers in all four slots',
     mc.every(q => q.opts.length === 4 && new Set(q.opts).size === 4)
     && [0,1,2,3].every(i => mc.some(q => q.ans === i)), mc.map(q => q.ans).join(''));
  const STAGES = ['Exposition','Rising action','Climax','Falling action','Conclusion'];
  const stageQs = mc.filter(q => q.opts.every(o => STAGES.includes(o)));
  // The climax reads two ways in this book (the verdict, or the game after it) and her
  // teacher's answer is not in Drive, so it is taught on a card and graded nowhere.
  ck('which-stage questions cover the four unambiguous stages, and none is graded as the climax',
     stageQs.length >= 4 && STAGES.filter(s => s !== 'Climax').every(s => stageQs.some(q => q.opts[q.ans] === s))
       && !mc.some(q => /climax/i.test(q.opts[q.ans]) || /why is the verdict not the climax/i.test(q.q)),
     stageQs.map(q => q.opts[q.ans]));
  const backref = R.questions.filter(q => /^\s*(the same|that same|for (that|the) same|from the same|using the same|in the same|with the same)\b/i.test(q.q)
    || /\b(all|none|both) of the above\b|\b(first|second|third|fourth|last) (option|answer|choice)\b/i.test(JSON.stringify(q))).map(q => q.id);
  ck('no back-references and no positional references', backref.length === 0, backref);
  const selfAns = mc.filter(q => q.q.toLowerCase().includes(q.opts[q.ans].toLowerCase())).map(q => q.id);
  ck('no stem contains its own answer', selfAns.length === 0, selfAns);
  ck('the legal words and themes are taught on cards',
     ['hearsay','circumstantial','perjury','impartial','sixth amendment','amends','revenge','not guilty']
       .every(w => R.cards.some(c => (c.term + ' ' + c.def).toLowerCase().includes(w))), null);
  const sa = R.cards.filter(c => /short answer/i.test(c.term));
  const ponder = R.cards.filter(c => /^ponder/i.test(c.term));
  ck('short-answer cards flagged added, and one ponder card flagged added',
     sa.length >= 1 && sa.every(c => c.from === 'added') && ponder.length === 1 && ponder[0].from === 'added',
     {sa: sa.map(c => c.from), ponder: ponder.map(c => c.from)});
  ck('the parent note names its parts, the ending, and that no class material was in Drive',
     /1–5/.test(R.parentNote.text) && /14–16/.test(R.parentNote.text) && /ending/i.test(R.parentNote.text)
     && /finished the book/i.test(R.parentNote.text) && /No class material/i.test(R.parentNote.text), null);
  /* "Xbox 20/20" is the console's name and 11/20 is the test date, not a mark. */
  const blob = JSON.stringify(R).replace(/20\/20|11\/20/g, '');
  const marks = [/\bRiver\b/, /\bSedona\b/, /\d+\s*(\/|out of)\s*\d+\b/, /\bshe (got|scored)\b/i,
                 /\b(scored|scores?|graded|grades)\b/i, /@/, /https?:/].filter(re => re.test(blob)).map(String);
  ck('privacy and mark sweep: no names of the family, no score, no link', marks.length === 0, marks);
  ck('nothing she sees uses an exclamation mark',
     !/!/.test(JSON.stringify([R.cards, R.questions.map(q => [q.q, q.opts, q.hint, q.steps, q.ex])])), null);

  /* ---------------- the shelf */
  const shelf = await p.evaluate(() => {
    const sh = shelvesFor('english').shelves.find(s => s.name === 'The Lemonade Crime');
    go('shelf', {classId:'english', series:'The Lemonade Crime', open:'unit-lc-review'});
    const stops = [...document.querySelectorAll('#screen .stop')];
    const oc = document.getElementById('shelfopen');
    return {order: sh ? sh.units.map(u => u.id) : null,
            titles: stops.map(x => (x.querySelector('.t')||{}).textContent),
            lastPrep: stops.length ? stops[stops.length-1].classList.contains('prep') : null,
            opened: oc ? oc.textContent.slice(0, 160) : null,
            band: oc ? !!oc.querySelector('.prepband') : null,
            clock: oc ? /Beat the clock/.test(oc.textContent) : null};
  });
  ck('shelvesFor: five parts on one shelf, the review last',
     JSON.stringify(shelf.order) === JSON.stringify(['unit-lc1','unit-lc2','unit-lc3','unit-lc4','unit-lc-review']), shelf.order);
  ck('the map shows five stops, the review last and gold-ringed',
     shelf.titles.length === 5 && /Novel Test Review/.test(shelf.titles[4]) && shelf.lastPrep, shelf);
  ck('the opened review wears the test-prep band', shelf.band && /Novel Test Review/.test(shelf.opened || ''), shelf.opened);
  ck('no Beat the clock on the review', shelf.clock === false, shelf.clock);

  /* ---------------- a full round, then rounds until a passage plate renders */
  const play = await p.evaluate(async () => {
    let plate = null, asked = 0;
    for (let round = 0; round < 6 && !plate; round++) {
      quizState = null;
      go('quiz', {unitId:'unit-lc-review', classId:'english'});
      let guard = 0;
      while (view === 'quiz' && guard++ < 60) {
        const el = document.querySelector('#screen .passage');
        if (el && !plate) plate = el.textContent.slice(0, 70);
        const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
        if (opts.length) { asked++; for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,4)); } }
        await new Promise(r=>setTimeout(r,8));
        const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
        if (next) { next.click(); await new Promise(r=>setTimeout(r,8)); continue; }
        if (!opts.length) break;
      }
    }
    const logs = all('log').filter(l => l.unitId === 'unit-lc-review');
    return {logged: logs.length, firstTotal: logs[0] ? logs[0].total : 0, plate, asked};
  });
  ck('a full twelve-question round completes and logs', play.logged >= 1 && play.firstTotal === 12, play);
  ck('a quoted passage renders as a plate in the quiz', !!play.plate, play.plate);

  /* ---------------- the deck */
  const deck = await p.evaluate(async () => {
    go('cards', {unitId:'unit-lc-review', classId:'english'});
    let seen = 0, guard = 0;
    /* Each card is two taps: Flip it, then Knew it. Only the visible primary
       button counts — the other one is hidden, not removed. */
    while (view === 'cards' && guard++ < 200) {
      const nx = [...document.querySelectorAll('#screen .btn-primary')].find(x => x.offsetParent);
      if (!nx) break;
      if (/Knew it/.test(nx.textContent)) seen++;
      nx.click();
      await new Promise(r => setTimeout(r, 6));
    }
    return {seen, left: view,
            logged: all('log').some(l => l.mode === 'cards' && l.unitId === 'unit-lc-review')};
  });
  ck('the deck walks to the end and logs', deck.seen === R.cards.length && deck.left !== 'cards' && deck.logged, deck);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + JSON.stringify(r.got).slice(0,300))));
  console.log(out.length + ' assertions; ' + (out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES'));
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
