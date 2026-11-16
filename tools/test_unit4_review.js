/* Unit 4 · Test Review, Part 1: Lessons 1–4, and the 11/13 newsletter's two
   assessments.

   Pins: the review trails the four lessons on the Unit 4 shelf in gold; every
   "What is a × b?" re-derived HERE with exact integer arithmetic; every
   find-the-mistake item re-checked against slips re-implemented HERE (the
   named slip makes the printed number, and no other offered slip does); the
   which-check items; the one-option items; no multiplication any lesson or
   practice page already asks; Part 1 saying it is Part 1; a full round; the
   deck; and the two new suggestions by id. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8413;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const seed = await p.evaluate(async () => {
    const ids = [];
    for (const f of ['math-u4-l1','math-u4-l2','math-u4-l3','math-u4-l4','math-u4-review']) {
      const j = await (await fetch(`./content/${f}.json`, {cache:'no-store'})).json();
      const u = Object.values(j.records).find(r => r.type === 'unit');
      ids.push({id: u.id, status: u.status, past: u.updatedAt < Date.now() - 3600e3});
      u.status = 'approved'; u.updatedAt = Date.now() - 6e5;
      DATA.records[u.id] = u;
    }
    saveLocal();
    return {ids, listed: CONTENT_LIBRARY.includes('content/math-u4-review.json')};
  });
  const rv = seed.ids.find(x => x.id === 'unit-m4-review');
  ck('the review ships as a draft stamped in the past, and is in CONTENT_LIBRARY', rv && rv.status === 'draft' && rv.past && seed.listed, seed);

  const shelf = await p.evaluate(() => {
    const s = shelvesFor('math').shelves.find(s => s.name === 'Unit 4');
    const u = DATA.records['unit-m4-review'];
    go('unit', {classId:'math'});
    return {parts: s && s.lessons.map(u => u.title), series: u.series, prep: u.prep, order: u.order,
            round: u.round, libv: u.libv, quarter: u.quarter, cls: u.classId};
  });
  ck('the review trails Lessons 1–4 on the Unit 4 shelf',
     shelf.parts && shelf.parts.length === 5 && shelf.parts[4] === 'Unit 4 · Test Review, Part 1: Lessons 1–4' &&
     [1,2,3,4].every((n,i) => shelf.parts[i].startsWith(`Unit 4 · Lesson ${n}: `)), shelf.parts);
  ck('series Unit 4, prep, no order, round 10, libv, quarter 2, classId math',
     shelf.series === 'Unit 4' && shelf.prep === true && shelf.order === undefined && shelf.round === 10 &&
     shelf.libv >= 1 && shelf.quarter === 2 && shelf.cls === 'math', shelf);

  const t = await p.evaluate(() => {
    const u = DATA.records['unit-m4-review'];
    const qs = u.questions; const ansOf = q => q.opts[q.ans];
    const SUP = {'¹':1,'²':2,'³':3,'⁴':4};
    // Exact decimals: {i: BigInt, p: places}.
    const dec = s => { s = String(s).replace(/[$,]/g,'').trim(); if (!/^\d+(\.\d+)?$/.test(s)) return null;
      const [a, f=''] = s.split('.'); return {i: BigInt(a+f), p: f.length}; };
    const norm = x => { let {i,p} = x; while (p>0 && i%10n===0n) { i/=10n; p--; } return i+'/'+p; };
    const mul = (a,c) => ({i:a.i*c.i, p:a.p+c.p});
    const div10 = (a,n) => ({i:a.i, p:a.p+n});
    const add = (a,c) => { const P=Math.max(a.p,c.p); return {i:a.i*10n**BigInt(P-a.p)+c.i*10n**BigInt(P-c.p), p:P}; };
    const eq = (a,c) => a && c && norm(a) === norm(c);
    const lt = (a,c) => { const P=Math.max(a.p,c.p); return a.i*10n**BigInt(P-a.p) < c.i*10n**BigInt(P-c.p); };
    const round = x => { const s=10n**BigInt(x.p); return {i:(x.i*2n+s)/(2n*s), p:0}; };
    const isWhole = x => norm(x).endsWith('/0');
    const pow = n => ({i: 10n**BigInt(n), p:0});
    // The slips, re-implemented independently of the builder.
    const SL = {
      'The point moved left, the wrong way': (a,n) => div10(a,n),
      'The point moved one place too few': (a,n) => mul(a,pow(n-1)),
      'The point moved one place too many': (a,n) => mul(a,pow(n+1)),
      'The exponent was used as a factor': (a,n) => mul(a,{i:BigInt(10*n),p:0}),
      'The decimal point was left out': (a,c) => { const [w,x] = isWhole(a)?[a,c]:[c,a]; return {i:w.i*x.i, p:w.p}; },
      'The point went one place too far right': (a,c) => mul(mul(a,c),{i:10n,p:0}),
      'The point went one place too far left': (a,c) => div10(mul(a,c),1),
      'The numbers were added, not multiplied': (a,c) => add(a,c),
      'The zero in the whole number was dropped': (a,c) => { const [w,x] = isWhole(a)?[a,c]:[c,a]; return mul({i:w.i/10n,p:w.p},x); },
      'Each place was multiplied, not regrouped': (a,c) => { const [w,x] = isWhole(a)?[a,c]:[c,a]; const W = Number(w.i);
        const s = x.i.toString().padStart(x.p+1,'0'); const ip = s.slice(0, s.length-x.p), fp = s.slice(s.length-x.p);
        return dec(String(W*Number(ip)) + '.' + [...fp].map(ch => String(W*Number(ch))).join('')); },
    };
    const worked = qs.filter(q => /^What is [\d.,]+ × ([\d.,]+|10[¹²³⁴])\?$/.test(q.q)).map(q => {
      const [, a, c] = q.q.match(/^What is ([\d.,]+) × ([\d.,]+|10[¹²³⁴])\?$/);
      const C = /^10[¹²³⁴]$/.test(c) ? pow(SUP[c[2]]) : dec(c);
      const want = mul(dec(a), C);
      return {q:q.q, right: eq(dec(ansOf(q)), want), others: q.opts.every((o,i) => i===q.ans || !eq(dec(o), want))};
    });
    const mist = qs.filter(q => /What went wrong\?$/.test(q.q)).map(q => {
      const [, a, c, w] = q.q.match(/worked out ([\d.,]+) × ([\d.,]+|10[¹²³⁴]) and wrote ([\d.,]+)\./);
      const pw = /^10/.test(c) && c.length === 3; const A = dec(a), Cv = pw ? SUP[c[2]] : dec(c), W = dec(w);
      const make = o => SL[o] ? SL[o](A, Cv) : null;
      const true_ = pw ? mul(A, pow(Cv)) : mul(A, Cv);
      return {q:q.q, named: eq(make(ansOf(q)), W), notTrue: !eq(W, true_),
              only: q.opts.every((o,i) => i===q.ans || !eq(make(o), W)), known: q.opts.every(o => !!SL[o])};
    });
    const nt = (() => { const q = qs.find(q => q.q === 'Which equation is NOT true?');
      const holds = s => { const m = s.match(/^([\d.,]+) × ([\d.,]+) = ([\d.,]+)$/); return eq(mul(dec(m[1]),dec(m[2])), dec(m[3])); };
      const f = q.opts.map((o,i) => holds(o) ? -1 : i).filter(i => i>=0); return f.length===1 && f[0]===q.ans; })();
    const ov = (() => { const q = qs.find(q => /OVERestimate/.test(q.q));
      const h = q.opts.map((o,i) => { const [a,c] = o.split(' × ').map(dec); return lt(mul(a,c), mul(round(a),round(c))) ? i : -1; }).filter(i => i>=0);
      return h.length===1 && h[0]===q.ans; })();
    const find = re => qs.find(q => re.test(q.q));
    const W = [
      [/7\.92 × 31/, '240'], [/\$0\.85 a yard/, '$11.90'], [/2\.75 km/, '16.5 km'],
      [/2 × 0\.47 = 0\.814/, 'Counting places'], [/0\.58 × 9 = 52\.2/, 'estimate'],
    ].map(([re, want]) => { const q = find(re); return {re:String(re), ok: !!q && ansOf(q).includes(want), got: q && ansOf(q)}; });
    const lean = qs.filter(q => /^\s*(the|that|this) same\b/i.test(q.q) || /\b(worksheet|practice (page|sheet)|from before|the previous)\b/i.test(q.q) ||
      /\b(all|none|both) of the above\b|\b(first|second|third|fourth|last) (option|choice|answer)\b/i.test(q.q+' '+q.opts.join(' '))).map(q => q.id);
    const blob = JSON.stringify(u);
    return {worked, mist, nt, ov, W, lean,
      lv:[1,2,3].map(l => qs.filter(q => q.lv===l).length), slots:[0,1,2,3].map(i => qs.filter(q => q.ans===i).length),
      bad: qs.filter(q => q.opts.length!==4 || new Set(q.opts).size!==4).map(q => q.id),
      part1: /Part 2/.test(u.parentNote.text) && /4-5 to 4-8/.test(u.parentNote.text),
      exclaim: /!/.test(qs.map(q => q.q+q.ex.main+q.ex.tip).join('') + u.cards.map(c => c.def).join('')),
      british: /\b(colour|metre|centre|favour|grey)\b/i.test(blob),
      marks: /\b(she got|she scored|\d+ out of \d+|she was marked)\b/i.test(blob),
      cards: u.cards.length, qn: qs.length};
  });
  ck('10+ cards, 20 questions, all three levels, all four answer slots, four unique options',
     t.cards >= 10 && t.qn >= 20 && t.lv.every(c=>c>0) && t.slots.every(c=>c>0) && !t.bad.length, [t.cards, t.qn, t.lv, t.slots, t.bad]);
  ck('every "What is a × b?" re-derived exactly, wrong options all different numbers',
     t.worked.length >= 6 && t.worked.every(x => x.right && x.others), t.worked);
  ck('7+ find-the-mistake items: the named slip makes the printed number, no other offered slip does, and it is not the true answer',
     t.mist.length >= 7 && t.mist.every(x => x.known && x.named && x.only && x.notTrue), t.mist);
  ck('"which equation is NOT true" has exactly one false option, the answer', t.nt, t.nt);
  ck('the overestimate item has exactly one pair that rounds up', t.ov, t.ov);
  ck('word problems and the two which-check items', t.W.every(w => w.ok), t.W.filter(w => !w.ok));
  ck('no back-reference, no positional option', t.lean.length === 0, t.lean);
  ck('no exclamation marks, American spelling, no mark or score', !t.exclaim && !t.british && !t.marks, t);
  ck('the note says it is Part 1 and that 4-5 to 4-8 are not covered', t.part1, t.part1);

  // No multiplication from a lesson or a practice page.
  const reuse = await p.evaluate(async () => {
    const pairs = s => [...s.matchAll(/([\d.,]+) × (10[¹²³⁴]|[\d.,]+)/g)].map(m => {
      const S = {'¹':10,'²':100,'³':1000,'⁴':10000};
      const b = /^10[¹²³⁴]$/.test(m[2]) ? S[m[2][2]] : Number(m[2].replace(/,/g,'').replace(/\.$/,''));
      return [Number(m[1].replace(/,/g,'').replace(/\.$/,'')), b].sort((x,y)=>x-y).join('×'); });
    const lessons = new Set();
    for (let n=1;n<=4;n++) DATA.records['unit-m4u'+n].questions.forEach(q => [q.q, ...q.opts].forEach(s => pairs(s).forEach(x => lessons.add(x))));
    const PAGE = ['4.58×1000','0.009×10','3.1×1000','42.3×10','0.062×100','1.24×10000','0.086×10','63.7×10','563.7×100','0.365×10000',
      '5.02×100','94.6×1000','0.9463×100','0.678×100','681.7×10000','4.82×1000','0.482×10','48.2×10000','2.15×16','0.87×112',
      '0.33×104','9.02×80','0.54×24','33.05×200','0.79×51','0.12×105','4×45.3','82×99.2','0.93×37','1.67×4','3.2×184','0.37×12',
      '0.904×75','0.36×4','1.27×5','0.8×4','0.7×3','0.5×6','0.6×5','0.55×3','0.45×2','0.27×4','0.13×6','0.78×5','0.32×10',
      '2.03×6','1.35×5','0.12×100','0.15×4','2.5×3','0.9×7','0.35×3','0.15×12','0.33×19','2×9.8','0.67×8','5.3×34','4.6×21',
      '0.6×15','1.1×55','9×34.6','20×64.2','0.22×40','2.3×57','5.8×11','0.4×56','0.003×170','0.3×99','1.61×26','0.914×50',
      '10.76×100','2.54×12','0.07×956','2×18.4','3×75','0.3×75','3×7.5','0.03×75','12×50','0.12×50','0.5×12','1.2×50','0.989×9'];
    const page = new Set(PAGE.map(s => s.split('×').map(Number).sort((x,y)=>x-y).join('×')));
    const mine = DATA.records['unit-m4-review'].questions.flatMap(q => pairs(q.q));
    return {fromLessons: mine.filter(x => lessons.has(x)), fromPage: mine.filter(x => page.has(x)), n: mine.length};
  });
  ck('no multiplication any Unit 4 lesson or practice page already asks', reuse.n >= 15 && !reuse.fromLessons.length && !reuse.fromPage.length, reuse);

  const round = await p.evaluate(async () => {
    quizState = null; go('quiz', {unitId:'unit-m4-review', classId:'math'});
    const dealt = (quizState && quizState.order || []).length; let g = 0;
    while (view === 'quiz' && g++ < 80) {
      const o = [...document.querySelectorAll('#screen .opt:not([disabled])')];
      if (o.length) { o[0].click(); await new Promise(r=>setTimeout(r,4)); }
      const n = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
      if (n) { n.click(); await new Promise(r=>setTimeout(r,4)); continue; }
      if (!o.length) break;
    }
    document.querySelectorAll('.modal-back, .modal-bg, .modal').forEach(m => m.remove());
    const lg = all('log').filter(l => l.unitId === 'unit-m4-review').pop();
    cardState = {}; go('cards', {unitId:'unit-m4-review', classId:'math'});
    await new Promise(r=>setTimeout(r,30));
    return {dealt, logged: !!lg && lg.total === dealt, deck: !!document.querySelector('#screen .face')};
  });
  ck('a full ten-question round plays and logs, and the deck renders', round.dealt >= 10 && round.logged && round.deck, round);

  const sg = await p.evaluate(() => {
    const by = id => SUGGESTED_ASSESS.find(s => s.id === id);
    return {v: by('sg-eng-2026-11-18'), n: by('sg-eng-2026-11-20'),
            dup: SUGGESTED_ASSESS.length !== new Set(SUGGESTED_ASSESS.map(s => s.id)).size};
  });
  ck('Wordly Wise Unit 5 vocabulary quiz, English, 11/18', sg.v && sg.v.date === '2026-11-18' && sg.v.classId === 'english' && sg.v.kind === 'quiz' && /Unit 5/.test(sg.v.title), sg.v);
  ck('Lemonade Crime novel test, English, 11/20', sg.n && sg.n.date === '2026-11-20' && sg.n.classId === 'english' && sg.n.kind === 'test' && /Lemonade Crime/.test(sg.n.title), sg.n);
  ck('no duplicate suggestion ids', !sg.dup, sg.dup);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + String(JSON.stringify(r.got)).slice(0,700))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,5) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
