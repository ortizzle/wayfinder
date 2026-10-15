/* Math Facts shelf + Facts sprint (v185). Pins the content (every fact
   computed, 66 distinct facts 2–12 x 2–12, four units in order) and the
   sprint's rules: the teacher's 50-in-3 shape, typed answers credited to
   the fact's real question, a skip is not a miss, the clock reaching a fact
   first is not a miss, nothing timed moves the map, and one log in place. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8413;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});
  const sleep = ms => p.waitForTimeout(ms);

  const seed = await p.evaluate(async () => {
    const files = [1,2,3,4].map(n => 'content/math-facts-' + n + '.json');
    for (const f of files) {
      const j = await (await fetch('./' + f, {cache:'no-store'})).json();
      const u = Object.values(j.records)[0];
      u.status = 'approved'; u.updatedAt = Date.now() - 1000;
      DATA.records[u.id] = u;
    }
    /* A neighbour that is NOT a facts unit, so "no doors on ordinary lessons" is tested. */
    const j2 = await (await fetch('./content/math-u3-l1.json', {cache:'no-store'})).json();
    const o = Object.values(j2.records)[0]; o.status = 'approved'; DATA.records[o.id] = o;
    saveLocal();
    return { inLib: files.every(f => CONTENT_LIBRARY.includes(f)), other: o.id };
  });
  ck('all four Math Facts files are in CONTENT_LIBRARY', seed.inLib, seed);

  const content = await p.evaluate(() => {
    const us = [1,2,3,4].map(n => DATA.records['unit-mf-' + n]);
    const facts = new Set(); let bad = [], qs = 0;
    us.forEach(u => u.questions.forEach(q => {
      if (!Array.isArray(q.fact)) return;
      qs++;
      const [a, b] = q.fact, p = a * b;
      if (q.opts[q.ans] !== String(p)) bad.push(u.id + ':' + q.id + ' answer');
      if (new Set(q.opts).size !== 4) bad.push(u.id + ':' + q.id + ' dup');
      if (q.opts.filter(o => o === String(p)).length !== 1) bad.push(u.id + ':' + q.id + ' twice');
      if (a >= 2 && b >= 2) facts.add(Math.min(a,b) + 'x' + Math.max(a,b));
    }));
    const cardsOk = us.every(u => u.cards.filter(c => /^\d+ × \d+$/.test(c.term)).every(c => {
      const [a, b] = c.term.split(' × ').map(Number); return c.def.startsWith('**' + (a*b) + '**'); }));
    const sh = shelvesFor('math').shelves.find(s => s.name === 'Math Facts');
    return { n: facts.size, bad, qs, cardsOk,
      flags: us.every(u => u.facts && u.classId === 'math' && u.libv >= 1 && u.status === 'approved'),
      order: sh ? sh.units.map(u => u.id) : null,
      slots: us.map(u => new Set(u.questions.map(q => q.ans)).size) };
  });
  ck('66 distinct facts, 2–12 × 2–12, every one in a question', content.n === 66, content.n);
  ck('every fact question answers a × b, with 4 unique options', content.bad.length === 0, content.bad.slice(0,5));
  ck('every fact card leads with its product in bold', content.cardsOk, content.cardsOk);
  ck('facts flag, math classId, libv on all four', content.flags, content);
  ck('one Math Facts shelf, parts 1 → 4 in order',
     JSON.stringify(content.order) === JSON.stringify(['unit-mf-1','unit-mf-2','unit-mf-3','unit-mf-4']), content.order);
  ck('answers rotate across all four slots in every unit', content.slots.every(n => n === 4), content.slots);

  const doors = await p.evaluate((other) => {
    go('shelf', {classId:'math', series:'Math Facts', open:'unit-mf-3'});
    const txt = document.getElementById('screen').textContent;
    const btns = [...document.querySelectorAll('#screen button')].filter(b => /Sprint this set|The pop quiz/.test(b.textContent));
    const h = btns.map(b => b.getBoundingClientRect().height);
    go('shelf', {classId:'math', series:'Unit 3', open:other});
    const t2 = document.getElementById('screen').textContent;
    return { set: /Sprint this set/.test(txt), all: /The pop quiz — 50 facts in 3 minutes/.test(txt),
             h, other: /Sprint this set|The pop quiz/.test(t2) };
  }, seed.other);
  ck('a facts card carries both sprint doors, 44px+', doors.set && doors.all && doors.h.every(h => h >= 44), doors);
  ck('an ordinary lesson carries no sprint door', !doors.other, doors);

  // ---- A set sprint: intro first, nothing running until Go.
  const intro = await p.evaluate(() => {
    sprintState = null; go('sprint', {unitId:'unit-mf-3', classId:'math', scope:'set'});
    const t = document.getElementById('screen').textContent;
    return { says: /25 facts\. 90 seconds\./.test(t), started: !!sprintState.start, tick: !!sprintTick,
             n: sprintState.items.length, allHere: sprintState.items.every(i => i.unitId === 'unit-mf-3'),
             repeats: sprintState.items.some((it, k, a) => k && a[k-1].qid === it.qid) };
  });
  ck('the set sprint says "25 facts. 90 seconds." and waits for Go', intro.says && !intro.started && !intro.tick, intro);
  ck('25 facts dealt, all from this set, never the same fact twice in a row', intro.n === 25 && intro.allHere && !intro.repeats, intro);

  const play = await p.evaluate(async () => {
    [...document.querySelectorAll('#screen button')].find(b => /Go/.test(b.textContent)).click();
    await new Promise(r => setTimeout(r, 30));
    const keyH = [...document.querySelectorAll('.keypad .key')].map(b => b.getBoundingClientRect().height);
    const press = async k => { const lab = k === 'ok' ? /^(✓|Skip)$/ : k === 'del' ? /^⌫$/ : new RegExp('^' + k + '$');
      [...document.querySelectorAll('.keypad .key')].find(b => lab.test(b.textContent.trim())).click();
      await new Promise(r => setTimeout(r, 5)); };
    const st = sprintState;
    // 1) right, typed on the keypad (with a slip deleted first).
    let it = st.items[0];
    await press('9'); await press('del');
    for (const d of String(it.a*it.b)) await press(d);
    await press('ok');
    const qs1 = DATA.records['qstat_' + it.unitId + '_' + it.qid];
    const m1 = DATA.records['miss_' + it.unitId + '_' + it.qid];
    // 2) wrong.
    const it2 = st.items[1];
    for (const d of String(it2.a*it2.b + 1)) await press(d);
    await press('ok');
    const m2 = DATA.records['miss_' + it2.unitId + '_' + it2.qid];
    // 3) skip — skip a fact not already answered in this sprint.
    const it3 = st.items[2];
    const before3 = JSON.stringify(DATA.records['qstat_' + it3.unitId + '_' + it3.qid] || null);
    const skipLabel = [...document.querySelectorAll('.keypad .key')].pop().textContent.trim();
    await press('ok');
    const after3 = JSON.stringify(DATA.records['qstat_' + it3.unitId + '_' + it3.qid] || null);
    const sameAsEarlier = it3.qid === it.qid || it3.qid === it2.qid;
    // 4) keyboard.
    const it4 = st.items[3];
    for (const d of String(it4.a*it4.b)) document.dispatchEvent(new KeyboardEvent('keydown', {key:d}));
    document.dispatchEvent(new KeyboardEvent('keydown', {key:'Enter'}));
    await new Promise(r => setTimeout(r, 10));
    const log = all('log').find(l => l.mode === 'sprint' && l.unitId === 'unit-mf-3');
    return { keyH, right:{plain:qs1 && qs1.plain, att:qs1 && qs1.attempts, cor:qs1 && qs1.correct, miss:!!(m1 && !m1.deleted)},
             wrong:{miss:!!(m2 && !m2.deleted), box:m2 && m2.box, chose:m2 && m2.chose},
             skip:{label:skipLabel, unchanged: before3 === after3 || sameAsEarlier, rec: st.answers[2]},
             kb: st.answers[3] && st.answers[3].right, i: st.i,
             log: log && {correct:log.correct, total:log.total, answered:log.answered, xp:log.xp, scope:log.scope} };
  });
  ck('keypad keys are 44px+', play.keyH.length === 12 && play.keyH.every(h => h >= 44), play.keyH);
  ck('a right typed answer credits the real question, timed (plain 0), no miss',
     play.right.att === 1 && play.right.cor === 1 && play.right.plain === 0 && !play.right.miss, play.right);
  ck('a wrong typed answer lands in the Growth Zone at box 0, with what she typed',
     play.wrong.miss && play.wrong.box === 0 && /^\d+$/.test(String(play.wrong.chose)), play.wrong);
  ck('an empty ✓ reads "Skip", and a skip writes no tally and no miss',
     play.skip.label === 'Skip' && play.skip.unchanged && play.skip.rec.typed === null, play.skip);
  ck('the keyboard types and enters too', play.kb === true && play.i === 4, play);
  ck('one sprint log, written in place as she goes', play.log && play.log.correct === 2 && play.log.answered === 3
     && play.log.total === 25 && play.log.xp === 4 && play.log.scope === 'set', play.log);

  // ---- The clock runs out: unreached facts are not misses.
  const timeup = await p.evaluate(async () => {
    const st = sprintState;
    const missesBefore = all('miss').filter(m => !m.deleted).length;
    st.start = Date.now() - 91000;
    await new Promise(r => setTimeout(r, 400));
    const t = document.getElementById('screen').textContent;
    return { over: st.over, tick: sprintTick, says: /Time/.test(t), unreached: /21 the clock got to first/.test(t),
             misses: all('miss').filter(m => !m.deleted).length - missesBefore,
             wrongList: /Worth another look/.test(t) && /you put/.test(t), xp: /\+4 XP/.test(t) };
  });
  ck('time up ends the sprint and stops the clock', timeup.over && timeup.tick === null && timeup.says, timeup);
  ck('facts the clock got to first are named, and none became a miss', timeup.unreached && timeup.misses === 0, timeup);
  ck('the results list the wrong facts with what she typed, and the XP', timeup.wrongList && timeup.xp, timeup);

  // ---- The pop quiz: 50 in 3 minutes across every facts unit.
  const full = await p.evaluate(() => {
    sprintState = null; go('sprint', {unitId:'unit-mf-1', classId:'math', scope:'all'});
    const t = document.getElementById('screen').textContent;
    const st = sprintState;
    return { says: /50 facts\. 3 minutes\./.test(t), n: st.items.length, secs: st.secs,
             units: new Set(st.items.map(i => i.unitId)).size,
             products: st.items.every(i => { const q = DATA.records[i.unitId].questions.find(x => x.id === i.qid);
               return q && q.opts[q.ans] === String(i.a*i.b); }) };
  });
  ck('the pop quiz is 50 facts, 180 seconds, drawn from every facts unit',
     full.says && full.n === 50 && full.secs === 180 && full.units === 4 && full.products, full);

  // ---- Stop early, leave, and the door remembers.
  const after = await p.evaluate(async () => {
    [...document.querySelectorAll('#screen button')].find(b => /Go/.test(b.textContent)).click();
    await new Promise(r => setTimeout(r, 20));
    const it = sprintState.items[0];
    String(it.a*it.b).split('').forEach(d => sprintKey(d)); sprintKey('ok');
    [...document.querySelectorAll('#screen button')].find(b => /Stop/.test(b.textContent)).click();
    await new Promise(r => setTimeout(r, 20));
    const stopped = sprintState.over && /1 of 50 right/.test(document.getElementById('screen').textContent);
    go('shelf', {classId:'math', series:'Math Facts', open:'unit-mf-1'});
    const t = document.getElementById('screen').textContent;
    const lg = all('log').find(l => l.mode === 'sprint' && l.scope === 'all');
    go('today');
    await new Promise(r => setTimeout(r, 300));
    return { stopped, door: /Last: 1 of 50 · best 1/.test(t), label: lg && modeLabel(lg), tick: sprintTick,
             setLabel: modeLabel(all('log').find(l => l.mode === 'sprint' && l.scope === 'set')) };
  });
  ck('Stop ends early and keeps what she answered', after.stopped, after);
  ck('the pop-quiz door says the last score and the best', after.door, after);
  ck('modeLabel names both sprints for the day view',
     after.label === 'Facts sprint · the pop quiz' && after.setLabel === 'Facts sprint', after);
  ck('no clock left running after leaving', after.tick === null, after.tick);

  const sug = await p.evaluate(() => ['2026-10-20','2026-10-28','2026-11-05'].map(d =>
    SUGGESTED_ASSESS.find(s => s.classId === 'math' && s.date === d)).map(s => s && s.title));
  ck('the update’s three math dates are suggested tests', sug.every(Boolean) && /Unit 3/.test(sug[0]) && /Unit 5/.test(sug[1]) && /Unit 5/.test(sug[2]), sug);

  out.forEach(r => console.log((r.ok ? '  ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' → ' + JSON.stringify(r.got).slice(0,300))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
