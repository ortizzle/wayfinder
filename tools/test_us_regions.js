/* U.S. Regions, five parts (v192), and the Cub Hub of 10/23.
   The capitals and region lists are re-stated HERE, independently of the
   builder, so a fact that drifts in one place fails against the other. Pins
   the shelf order, all fifty states exactly once, every capital question by
   its answer, the biggest-city traps never being capitals themselves, the
   added/no-class-material provenance, a full round on each part, and the
   November dates. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8413;
const CAP = {
  Maine:'Augusta','New Hampshire':'Concord',Vermont:'Montpelier',Massachusetts:'Boston','Rhode Island':'Providence',
  Connecticut:'Hartford','New York':'Albany','New Jersey':'Trenton',Pennsylvania:'Harrisburg',Delaware:'Dover',Maryland:'Annapolis',
  'West Virginia':'Charleston',Virginia:'Richmond',Kentucky:'Frankfort',Tennessee:'Nashville','North Carolina':'Raleigh',
  'South Carolina':'Columbia',Georgia:'Atlanta',Florida:'Tallahassee',Alabama:'Montgomery',Mississippi:'Jackson',
  Arkansas:'Little Rock',Louisiana:'Baton Rouge',
  Ohio:'Columbus',Indiana:'Indianapolis',Illinois:'Springfield',Michigan:'Lansing',Wisconsin:'Madison',Minnesota:'Saint Paul',
  Iowa:'Des Moines',Missouri:'Jefferson City',Kansas:'Topeka',Nebraska:'Lincoln','South Dakota':'Pierre','North Dakota':'Bismarck',
  Arizona:'Phoenix','New Mexico':'Santa Fe',Texas:'Austin',Oklahoma:'Oklahoma City',
  Colorado:'Denver',Wyoming:'Cheyenne',Montana:'Helena',Idaho:'Boise',Washington:'Olympia',Oregon:'Salem',Utah:'Salt Lake City',
  Nevada:'Carson City',California:'Sacramento',Alaska:'Juneau',Hawaii:'Honolulu'};
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const r = await p.evaluate(async (CAP) => {
    const ids = [1,2,3,4,5].map(i => 'unit-hist-reg-' + i);
    for (let i = 1; i <= 5; i++) {
      const k = await (await fetch('./content/history-regions-' + i + '.json', {cache:'no-store'})).json();
      for (const x of Object.values(k.records)) { x.status = 'approved'; DATA.records[x.id] = x; } }
    for (const f of ['content/history-u5-p1.json', 'content/az-latlong.json']) {
      const k = await (await fetch('./' + f, {cache:'no-store'})).json();
      for (const x of Object.values(k.records)) { x.status = 'approved'; DATA.records[x.id] = x; } }
    saveLocal();
    const U = ids.map(id => DATA.records[id]);
    const sh = shelvesFor('history'); const reg = sh.shelves.find(s => s.name === 'U.S. Regions');
    const states = U.flatMap(u => u.cards.map(c => c.term).filter(t => CAP[t]));
    const capQ = U.flatMap(u => u.questions.filter(q => /^What is the capital of /.test(q.q)).map(q => {
      const st = q.q.replace(/^What is the capital of /, '').replace(/\?$/, '');
      return {st, ok: q.opts[q.ans] === CAP[st], wrongOk: q.opts.every((o, i) => i === q.ans || o !== CAP[st])};
    }));
    const revQ = U.flatMap(u => u.questions.filter(q => /is a state capital\. Which state/.test(q.q)).map(q => {
      const c = q.q.split(' is a state capital')[0];
      return {c, ok: CAP[q.opts[q.ans]] === c, unique: q.opts.filter(o => CAP[o] === c).length === 1};
    }));
    const caps = new Set(Object.values(CAP));
    const traps = U.flatMap(u => u.cards.map(c => (c.def.match(/Not ([^,]+), even though/) || [])[1]).filter(Boolean));
    const quizRegion = U.flatMap((u, i) => u.questions.filter(q => /^Which region is /.test(q.q)).map(q => ({i, a: q.opts[q.ans]})));
    const names = ['Northeast','Southeast','Midwest','Southwest','West'];
    return {
      inLib: ids.every((_, i) => CONTENT_LIBRARY.includes('content/history-regions-' + (i+1) + '.json')),
      order: reg && reg.lessons.map(x => x.id), loose: sh.loose.map(x => x.id),
      meta: U.map(u => ({c: u.classId, prep: u.prep, libv: u.libv, status: u.status, q: u.quarter})),
      states, nStates: states.length, uniq: new Set(states).size,
      capQ, revQ, traps, trapIsCap: traps.filter(t => caps.has(t)),
      allAdded: U.every(u => u.cards.every(c => c.from === 'added') && u.questions.every(q => q.from === 'added') && u.summary.from === 'added'),
      noteSays: U.every(u => /No class material/.test(u.parentNote.text) && /Maryland and Delaware/.test(u.parentNote.text)),
      regionAns: quizRegion.every(x => x.a === names[x.i]),
      dc: U[0].cards.some(c => c.term === 'Washington, D.C.' && /NOT a state/.test(c.def)),
      shape: U.every(u => u.questions.every(q => q.opts.length === 4 && new Set(q.opts).size === 4 && q.ans >= 0 && q.ans < 4)),
      slots: U.map(u => new Set(u.questions.map(q => q.ans)).size),
      backref: U.flatMap(u => u.questions.filter(q => /^(the|that|this) same\b/i.test(q.q))).length,
      future: U.some(u => u.updatedAt > Date.now()),
    };
  }, CAP);
  ck('all five in CONTENT_LIBRARY, history, prep, libv, quarter 2', r.inLib && r.meta.every(m => m.c === 'history' && m.prep === true && m.libv >= 1 && m.q === 2), r.meta);
  ck('one U.S. Regions shelf in teaching order, alongside Unit 5, nothing loose', JSON.stringify(r.order) === JSON.stringify([1,2,3,4,5].map(i => 'unit-hist-reg-' + i)) && r.loose.length === 0, r);
  ck('all fifty states, each exactly once', r.nStates === 50 && r.uniq === 50, r.states);
  ck('every capital question has the right capital, and no wrong option is it', r.capQ.length >= 24 && r.capQ.every(x => x.ok && x.wrongOk), r.capQ.filter(x => !x.ok || !x.wrongOk));
  ck('every capital-to-state question names the right state, once', r.revQ.length === 10 && r.revQ.every(x => x.ok && x.unique), r.revQ);
  ck('biggest-city traps are present and never themselves a capital', r.traps.length >= 25 && r.trapIsCap.length === 0, r.trapIsCap);
  ck('which-region questions answer with their own part\'s region', r.regionAns, r);
  ck('every card and question flagged added; the note says no class material and names Maryland/Delaware', r.allAdded && r.noteSays, r);
  ck('Washington, D.C. taught as the capital, not a state', r.dc, r);
  ck('4 unique options everywhere, answers across 4 slots, no back-references, not future-stamped',
     r.shape && r.slots.every(s => s === 4) && !r.backref && !r.future, r.slots);

  for (let i = 1; i <= 5; i++) {
    const play = await p.evaluate(async (id) => {
      quizState = null; go('quiz', {unitId:id, classId:'history'});
      let guard = 0;
      while (view === 'quiz' && guard++ < 40) {
        const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
        if (opts.length) for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,4)); }
        await new Promise(r => setTimeout(r, 8));
        const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
        if (next) { next.click(); await new Promise(r=>setTimeout(r,8)); continue; }
        if (!opts.length) break;
      }
      document.querySelectorAll('.modal-bg, .modal').forEach(m => m.remove());
      const log = all('log').find(l => l.unitId === id);
      return {logged: !!log, total: log && log.total};
    }, 'unit-hist-reg-' + i);
    ck('part ' + i + ': a full round of 10 plays and logs', play.logged && play.total === 10, play);
  }

  const cal = await p.evaluate(() => {
    const on = d => eventsOn(d).map(e => e.name);
    return {o30: on('2026-10-30'), n18: on('2026-11-18'), n19: on('2026-11-19'), n20: on('2026-11-20'),
            n23: on('2026-11-23'), n24: on('2026-11-24'), n13: on('2026-11-13'),
            vets: CAL.closed.some(c => c[0] === '2026-11-11'), tg: CAL.closed.some(c => c[0] === '2026-11-25' && c[1] === '2026-11-30')};
  });
  ck('Cub Hub dates: SHINE lunch 11/18, field trip 11/19, clubs end 11/20, Pie Drive 11/23–24, no weekly pizza rows',
     cal.n18.includes('SHINE lunch') && cal.n19.includes('4th Grade Field Trip') && cal.n20.includes('Fall clubs end') &&
     cal.n23.includes('Pie Drive') && cal.n24.includes('Pie Drive') && !cal.o30.includes('Pizza Friday'), cal);
  ck('Veteran\'s Day and Thanksgiving Break still closed', cal.vets && cal.tg, cal);

  out.forEach(r => console.log((r.ok ? '  ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' → ' + JSON.stringify(r.got).slice(0,400))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
