/* Chemistry · 4 Molecules and Compounds (Wayfinder only).
   Built from her completed Molecules and Compounds lesson check, read for the
   QUESTIONS it asks rather than to mark it (the standing rule, Chris
   2026-09-27). The paper asks one skill twelve times: which TWO of atom /
   element / molecule / compound fit a substance.

   What this guards beyond the ordinary shelving/round checks:
     - it is the last Unit 1.2 part on the one Unit 1 shelf (v195; it began as
       Chemistry part 4);
     - the four definitions and the two-word pairing rule are taught, asserted
       by their TEACHING rather than by question id;
     - every pair a question claims agrees with the rule recomputed here from
       the formula itself (capitals = kinds, subscripts = atoms);
     - the ionic nuance is named for a grown-up and no graded question's
       answer depends on it;
     - nothing about how she did on the paper is recorded anywhere. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8413;
const UID = 'unit-sci-molcomp';
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  // Seed the WHOLE science subject, so the shelf claim is about coexistence.
  const seed = await p.evaluate(async (UID) => {
    const files = ['science-quiz-1','science-measurement','science-variables','science-scales',
                   'science-nos-practice','science-nos-test','science-phases-matter',
                   'science-phase-changes','science-density-buoyancy','science-molecules-compounds'];
    for (const f of files) {
      const j = await (await fetch('./content/'+f+'.json',{cache:'no-store'})).json();
      const u = Object.values(j.records).find(x=>x.type==='unit');
      u.status='approved'; u.updatedAt=Date.now()-1000; DATA.records[u.id]=u;
    }
    saveLocal();
    const u = DATA.records[UID];
    return {classId:u.classId, title:u.title, libv:u.libv, order:u.order, prep:u.prep,
            status: null, cards:u.cards, qs:u.questions, sorts:u.sorts,
            note:(u.parentNote||{}).text || '', blob: JSON.stringify(u)};
  }, UID);
  const shipped = require('../content/science-molecules-compounds.json').records[UID];

  ck('it loads under the real science classId', seed.classId === 'science', seed.classId);
  ck('it ships as a draft with a libv and an explicit order',
     shipped.status === 'draft' && seed.libv >= 1 && seed.order === 9, [shipped.status, seed.libv, seed.order]);
  ck('updatedAt is stamped in the past', shipped.updatedAt < Date.now() - 3600e3, shipped.updatedAt);
  ck('it is titled as Unit 1.2', /^Unit 1 · 1\.2 Molecules and Compounds$/.test(seed.title), seed.title);
  ck('it is not flagged prep — it is the lesson, not test prep', !seed.prep, seed.prep);
  ck('at least 14 cards and 16 questions, every MC with four unique options',
     seed.cards.length >= 14 && seed.qs.length >= 16 &&
     seed.qs.filter(q => (q.kind||'mc') === 'mc').every(q => q.opts.length === 4 && new Set(q.opts).size === 4),
     [seed.cards.length, seed.qs.length]);
  ck('all three levels are used, and every question has 3-6 steps',
     [1,2,3].every(l => seed.qs.some(q => q.lv === l)) &&
     seed.qs.every(q => q.steps.length >= 3 && q.steps.length <= 6), 'ok');
  ck('correct answers are spread across all four positions',
     [0,1,2,3].every(i => seed.qs.some(q => (q.kind||'mc')==='mc' && q.ans === i)),
     [0,1,2,3].map(i => seed.qs.filter(q=>q.ans===i).length));

  const stems = seed.qs.map(q => q.q + ' ' + q.steps.join(' ')).join(' ');
  ck('no question references the worksheet it was built from',
     !/\b(worksheet|practice sheet|the sheet|lesson check|question \d)\b/i.test(stems), 'ok');
  ck('no stem opens on a neighbour\'s scenario',
     !seed.qs.some(q => /^(the|that) same\b/i.test(q.q.trim())) && !/\bthat same\b/i.test(stems), 'ok');
  ck('no question refers to an option by position',
     !/\b(first|second|third|last) (two |three )?options?\b|all of the above/i.test(
        seed.qs.map(q=>q.q+' '+q.steps.join(' ')+' '+q.ex.main).join(' ')), 'ok');

  const shelf = await p.evaluate(() => {
    const s = shelvesFor('science');
    const u1 = s.shelves.find(x=>x.name==='Unit 1') || {lessons:[]};
    return {names: s.shelves.map(x=>x.name), loose: s.loose.length, ids: u1.lessons.map(u=>u.id),
            labels: u1.lessons.map(u=>lessonLabel(u))};
  });
  ck('Unit 1 runs the six 1.1 parts, then 1.2: Phases → Phase Changes → Density → Molecules, nothing loose',
     shelf.names.join() === 'Unit 1' && shelf.loose === 0 && shelf.ids.length === 10 &&
     shelf.labels.slice(0,6).every(l => /^1\.1 /.test(l)) &&
     shelf.ids.slice(6).join() === 'unit-sci-phases,unit-sci-phasechg,unit-sci-dens,unit-sci-molcomp', shelf);

  // The four words and the pairing rule, by their teaching.
  const card = t => seed.cards.find(c => new RegExp(t,'i').test(c.term)) || {};
  const lead = c => ((c.def||'').match(/^\*\*(.*?)\*\*/)||[])[1] || '';
  ck('an atom is taught as one particle, the smallest piece of an element',
     /smallest piece of an element/i.test(lead(card('^atom$'))) && /one single particle/i.test(card('^atom$').def), lead(card('^atom$')));
  ck('an element is taught as ONE kind of atom, single or joined',
     /only ONE kind of atom/.test(lead(card('^element$'))) && /Na/.test(card('^element$').def) &&
     /H₂/.test(card('^element$').def), lead(card('^element$')));
  ck('a molecule is taught as two or more atoms joined, same kind or different',
     /two or more atoms joined/i.test(lead(card('^molecule$'))) && /SAME/.test(card('^molecule$').def) &&
     /DIFFERENT/.test(card('^molecule$').def), lead(card('^molecule$')));
  ck('a compound is taught as two or more DIFFERENT elements joined',
     /two or more DIFFERENT elements joined/i.test(lead(card('^compound$'))), lead(card('^compound$')));
  const rule = lead(card('two words'));
  ck('the pairing rule names all three pairs',
     /atom and element/i.test(rule) && /element and molecule/i.test(rule) && /molecule and compound/i.test(rule), rule);
  ck('formula reading: capitals count elements, small numbers count atoms, both flagged added',
     /capital letter.*new element/i.test(card('capital').def) && card('capital').from === 'added' &&
     /how many atoms/i.test(card('small numbers').def) && card('small numbers').from === 'added',
     [card('capital').from, card('small numbers').from]);
  ck('every compound is a molecule, not the reverse, is taught',
     /Every compound is a molecule, but not every molecule is a compound/.test(seed.blob), 'ok');

  /* Recompute every claimed pair from the formula itself. */
  const SUB = {'₀':0,'₁':1,'₂':2,'₃':3,'₄':4,'₅':5,'₆':6,'₇':7,'₈':8,'₉':9};
  const parse = f => { const o = {}; f = f.replace(/[₀-₉]/g, c => SUB[c]);
    for (const m of f.matchAll(/([A-Z][a-z]?)(\d*)/g)) o[m[1]] = (o[m[1]]||0) + (m[2] ? +m[2] : 1); return o; };
  const pair = f => { const o = parse(f), k = Object.keys(o).length, a = Object.values(o).reduce((x,y)=>x+y,0);
    return k > 1 ? 'Molecule and compound' : a === 1 ? 'Atom and element' : 'Element and molecule'; };
  const pq = seed.qs.filter(q => /Which two words describe it\?/.test(q.q));
  const bad = pq.filter(q => { const f = (q.q.match(/is written ([A-Za-z₀-₉]+)/)||[])[1];
                               return !f || q.opts[q.ans] !== pair(f); }).map(q => q.id);
  ck('at least 6 pair questions, every answer agreeing with the recomputed rule',
     pq.length >= 6 && !bad.length, {n: pq.length, bad});
  ck('all three real pairs are an answer somewhere',
     ['Atom and element','Element and molecule','Molecule and compound'].every(x => pq.some(q => q.opts[q.ans] === x)), 'ok');
  ck('the many-atoms trap (O₃ or S₈) is asked: more atoms is not more kinds',
     pq.some(q => /O₃/.test(q.q) && q.opts[q.ans] === 'Element and molecule') &&
     seed.qs.some(q => q.opts[q.ans] === 'S₈'), 'ok');
  ck('the Co / CO capital-letter trap is asked',
     seed.qs.some(q => /Co is cobalt and CO/.test(q.q) && /^CO,/.test(q.opts[q.ans])), 'ok');

  /* The ionic nuance: named for a grown-up, never load-bearing in a question. */
  ck('the parent note names the ionic nuance', /ionic/i.test(seed.note) && /NaCl/.test(seed.note), seed.note.slice(0,60));
  const ionic = /NaCl|NaOH|K₂S|CaSO₄|ionic/;
  ck('no graded question depends on the ionic distinction',
     !seed.qs.some(q => ionic.test(q.q + ' ' + q.opts.join(' '))), seed.qs.filter(q=>ionic.test(q.q+q.opts.join(' '))).map(q=>q.id));

  /* Questions, not scoring. */
  const MARK = /\b(\d+\s*(out of|\/)\s*\d+|A\+|aced|she got|full marks|scored|points? (lost|earned))\b/i;
  ck('nothing about how she did on the sheet is recorded anywhere',
     !MARK.test(seed.blob), (seed.blob.match(new RegExp(MARK.source,'ig'))||[]).slice(0,5));
  ck('the note says the sheet was read for its questions, not to mark it',
     /read for the QUESTIONS it asks/.test(seed.note) && /nothing here is a correction/.test(seed.note), 'ok');

  // A ranking question stored in order.
  const ord = seed.qs.find(q => q.kind === 'order');
  const cnt = s => Object.values(parse(s.split(' ')[0])).reduce((x,y)=>x+y,0);
  ck('the fewest-to-most-atoms ranking is stored in ascending order',
     ord && ord.ans === 0 && ord.opts.map(cnt).every((n,i,a) => !i || n > a[i-1]), ord && ord.opts.map(cnt));

  // The sort set.
  const set = seed.sorts && seed.sorts[0];
  ck('one sort set, 12 items, both buckets used, a why on every item',
     seed.sorts.length === 1 && set.items.length === 12 && set.items.filter(i=>i.k==='a').length >= 4 &&
     set.items.filter(i=>i.k==='b').length >= 4 && set.items.every(i => i.why && i.why.length > 10), set && set.items.length);
  ck('no sort item names its own bucket (or any of the four words)',
     set.items.every(i => !/element|compound|molecule|atom\b/i.test(i.t)),
     set.items.filter(i=>/element|compound|molecule|atom\b/i.test(i.t)).map(i=>i.t));
  ck('every sort item is in the bucket its formula says',
     set.items.every(i => (Object.keys(parse(i.t.split(' ')[0])).length > 1) === (i.k === 'b')), 'ok');

  const sorted = await p.evaluate(({UID, sid}) => {
    sortState = null; go('sort', {unitId:UID, classId:'science', sortId:sid});
    const s = DATA.records[UID].sorts.find(x=>x.id===sid);
    const dealt = sortState.queue.length; let guard = 0;
    while (sortState.queue.length && guard++ < 40) {
      if (sortState.verdict) { [...document.querySelectorAll('#screen .btn')].find(b=>/Got it/.test(b.textContent)).click(); continue; }
      const it = s.items[sortState.queue[0]];
      const btns = [...document.querySelectorAll('#screen .sortbtns .btn')];
      (it.k === 'a' ? btns[0] : btns[1]).click();
    }
    const log = all('log').find(l => l.mode === 'sort' && l.unitId === UID);
    return {dealt, left: sortState.queue.length, correct: log && log.correct, xp: log && log.xp};
  }, {UID, sid: set.id});
  ck('a clean pass through the sort set clears it and logs 12 × 3 XP',
     sorted.dealt === 12 && sorted.left === 0 && sorted.correct === 12 && sorted.xp === 36, sorted);

  const quiz = await p.evaluate(async (UID) => {
    quizState = null; go('quiz', {unitId:UID, classId:'science'});
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
    const l = all('log').find(x => x.unitId === UID && x.mode === 'quiz');
    return {logged: !!l, total: l && l.total};
  }, UID);
  ck('a full quiz round completes and logs', quiz.logged && quiz.total >= 5, quiz);

  const deck = await p.evaluate(async (UID) => {
    go('cards', {unitId:UID, classId:'science'});
    const total = cardState.order.length; let seen = 0;
    while (cardState && cardState.unitId === UID && seen < 40) {
      const knew = [...document.querySelectorAll('button')].find(b => /Knew it/.test(b.textContent));
      if (!knew) break; seen++; knew.click(); await new Promise(r=>setTimeout(r,5));
    }
    return {seen, total};
  }, UID);
  ck('the whole deck walks to the end, every card seen once', deck.total >= 14 && deck.seen === deck.total, deck);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + JSON.stringify(r.got).slice(0,300))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
