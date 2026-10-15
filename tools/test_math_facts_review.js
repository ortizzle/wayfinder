/* Math Facts · All Facts Review (v187). Chris: the sets practise one table
   at a time, "but the quizzes will likely include all numbers". Pins: every
   fact 0–12 in one pool, each answer a × b, a strategy card per table, the
   unit last on the shelf and wearing the prep band, a quiz round that really
   mixes tables, its sprint drawing from every table — and the pop quiz NOT
   doubling any fact now that two units carry it. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8413;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const seed = await p.evaluate(async () => {
    const files = [1,2,3,4].map(n => 'content/math-facts-' + n + '.json').concat('content/math-facts-review.json');
    for (const f of files) {
      const j = await (await fetch('./' + f, {cache:'no-store'})).json();
      const u = Object.values(j.records)[0];
      u.status = 'approved'; u.updatedAt = Date.now() - 1000;
      DATA.records[u.id] = u;
    }
    saveLocal();
    return { inLib: CONTENT_LIBRARY.includes('content/math-facts-review.json') };
  });
  ck('the review file is in CONTENT_LIBRARY', seed.inLib, seed);

  const c = await p.evaluate(() => {
    const u = DATA.records['unit-mf-all'];
    const facts = new Set(), bad = [], tables = new Set();
    u.questions.forEach(q => {
      const [a, b] = q.fact || [];
      if (q.opts[q.ans] !== String(a * b)) bad.push(q.id + ' answer');
      if (new Set(q.opts).size !== 4) bad.push(q.id + ' dup');
      facts.add(Math.min(a,b) + 'x' + Math.max(a,b)); tables.add(a); tables.add(b);
    });
    const big = [...facts].filter(k => k.split('x').every(n => +n >= 2)).length;
    const strat = u.cards.filter(c => /^Any number × \d+$/.test(c.term)).map(c => +c.term.split('× ')[1]);
    const sh = shelvesFor('math').shelves.find(s => s.name === 'Math Facts');
    return { n: u.questions.length, big, bad, tables: [...tables].sort((a,b)=>a-b),
      zeroOne: [...facts].filter(k => /^(0|1)x/.test(k)).length,
      strat, factCards: u.cards.filter(c => /^\d+ × \d+$/.test(c.term)).length,
      flags: u.facts && u.factsMixed && u.prep && u.classId === 'math' && u.libv >= 1 && u.order === 1,
      round: u.round, slots: new Set(u.questions.map(q => q.ans)).size,
      order: sh ? sh.units.map(x => x.id) : null };
  });
  ck('all 66 facts from 2 × 2 to 12 × 12 are in the review', c.big === 66, c.big);
  ck('the × 0 and × 1 rules are asked too, so every table 0–12 appears', c.zeroOne >= 4 && c.tables.join() === '0,1,2,3,4,5,6,7,8,9,10,11,12', c);
  ck('every answer is a × b with 4 unique options', c.bad.length === 0, c.bad.slice(0,5));
  ck('a strategy card for every table 0–12, and no repeated fact cards', c.strat.join() === '0,1,2,3,4,5,6,7,8,9,10,11,12' && c.factCards === 0, c);
  ck('facts, factsMixed, prep, order 1, libv; a round of 20', c.flags && c.round === 20, c);
  ck('answers rotate across all four slots', c.slots === 4, c.slots);
  ck('it sits LAST on the Math Facts shelf, after Set 4',
     JSON.stringify(c.order) === JSON.stringify(['unit-mf-1','unit-mf-2','unit-mf-3','unit-mf-4','unit-mf-all']), c.order);

  const card = await p.evaluate(() => {
    go('shelf', {classId:'math', series:'Math Facts', open:'unit-mf-all'});
    const s = document.getElementById('screen');
    return { prep: !!s.querySelector('.prepband'), txt: s.textContent,
             doors: [...s.querySelectorAll('button')].filter(b => /Sprint this set|The pop quiz/.test(b.textContent)).length };
  });
  ck('the review wears the gold test-prep band', card.prep, card.prep);
  ck('both sprint doors, the set door saying it mixes every table', card.doors === 2 && /Every table, mixed, in a shorter run/.test(card.txt), card.doors);

  /* A real quiz round must mix tables — the whole point of the section. */
  const round = await p.evaluate(() => {
    const u = DATA.records['unit-mf-all'];
    const t = new Set();
    pickRound(u, false).forEach(i => { const [a,b] = u.questions[i].fact; t.add(Math.max(a,b)); });
    return { n: pickRound(u, false).length, tables: t.size };
  });
  ck('a quiz round is 20 facts spread across many tables', round.n === 20 && round.tables >= 5, round);

  const sprint = await p.evaluate(() => {
    const u = DATA.records['unit-mf-all'];
    sprintDeal('set', u, 'math');
    const big = new Set(sprintState.items.map(it => Math.max(it.a, it.b)));
    /* The pop quiz pool, dealt from the review card: every fact once, owned by its set. */
    const setKeys = new Set();
    [1,2,3,4].forEach(n => DATA.records['unit-mf-' + n].questions.forEach(q => q.fact &&
      setKeys.add(Math.min(...q.fact) + 'x' + Math.max(...q.fact))));
    let dupes = 0, stolen = 0;
    for (let r = 0; r < 4; r++) {
      sprintDeal('all', u, 'math');
      const facts = {};
      sprintState.items.forEach(it => {
        const k = Math.min(it.a,it.b) + 'x' + Math.max(it.a,it.b);
        (facts[k] = facts[k] || new Set()).add(it.unitId);
        if (it.unitId === 'unit-mf-all' && setKeys.has(k)) stolen++;
      });
      dupes += Object.values(facts).filter(s => s.size > 1).length;
    }
    return { setTables: big.size, dupes, stolen };
  });
  ck('its own sprint draws from every table', sprint.setTables >= 6, sprint);
  ck('the pop quiz never takes one fact from two units', sprint.dupes === 0, sprint);
  ck('the pop quiz credits a fact a set owns to that set, never the review', sprint.stolen === 0, sprint);

  /* A typed sprint answer still credits the review's own question when the
     review owns the fact (× 0 and × 1 facts the sets never ask). */
  const credit = await p.evaluate(() => {
    const u = DATA.records['unit-mf-all'];
    go('sprint', {unitId:u.id, classId:'math', scope:'set'});
    sprintState.start = Date.now();
    const it = sprintState.items[0];
    String(it.a * it.b).split('').forEach(k => sprintKey(k)); sprintKey('ok');
    const q = sprintState.answers[0];
    const qs = DATA.records['qstat_' + q.unitId + '_' + q.qid];
    stopSprintTick();
    return { right: q.right, unit: q.unitId, att: qs && qs.attempts, plain: qs && (qs.plain||0) };
  });
  ck('a typed answer in its sprint credits the review question, timed (plain 0)', credit.right && credit.unit === 'unit-mf-all' && credit.att === 1 && credit.plain === 0, credit);

  ck('no page errors', errs.length === 0, errs);
  await b.close();
  const bad = out.filter(o => !o.ok);
  out.forEach(o => console.log((o.ok ? 'PASS ' : 'FAIL ') + o.n + (o.ok ? '' : '  ' + JSON.stringify(o.got))));
  console.log(bad.length ? `${bad.length} FAILED of ${out.length}` : `ALL PASS (${out.length})`);
  process.exit(bad.length ? 1 : 0);
})();
