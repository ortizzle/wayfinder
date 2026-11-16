/* Unit 4 · Lessons 1–4 (multiplying decimals: powers of 10, estimating,
   modelling, the algorithm). Her class teaches Unit 4 AFTER Unit 5, so this
   also pins that the Math screen puts the book she studied most recently
   first, whichever number it carries.

   Pins the shelf, the flags, every product re-derived HERE with exact integer
   arithmetic (not trusted from the builder), every wrong option on a worked
   product being a different number from the real one, the true/false and
   over/under items having exactly one right option, the word problems, none
   of the four practice pages' own multiplications reused, the standalone
   rules, a full round on each lesson, and each deck. Counts are minimums. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8413;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});
  const NEW = [1,2,3,4];

  const seed = await p.evaluate(async () => {
    const files = ['math-u4-l1','math-u4-l2','math-u4-l3','math-u4-l4','math-longdiv-1','math-u5-l1','math-u5-l2','math-u5-l3','math-u5-l4','math-u5-l5','math-u5-l7'];
    const ids = [];
    for (const f of files) {
      const j = await (await fetch(`./content/${f}.json`, {cache:'no-store'})).json();
      const u = Object.values(j.records).find(r => r.type === 'unit');
      u.status = 'approved'; u.updatedAt = Date.now() - 6e5;
      DATA.records[u.id] = u; ids.push(u.id);
    }
    saveLocal();
    return ids;
  });
  ck('four Unit 4 lessons and the Unit 5 shelf seed', seed.length === 11, seed);

  const listed = await p.evaluate(() => [1,2,3,4].every(n => CONTENT_LIBRARY.includes(`content/math-u4-l${n}.json`)));
  ck('all four files are in CONTENT_LIBRARY', listed, listed);

  const shelves = await p.evaluate(() => {
    const r = shelvesFor('math');
    return {loose: r.loose.map(u=>u.title),
            books: r.shelves.map(s => ({name: s.name, parts: s.lessons.map(u=>u.title)}))};
  });
  const u4 = shelves.books.find(s => s.name === 'Unit 4');
  const u5 = shelves.books.find(s => s.name === 'Unit 5');
  ck('Unit 4 is its own shelf beside Unit 5, nothing loose', !!u4 && !!u5 && shelves.loose.length === 0, shelves);
  ck('the shelf reads Lesson 1, 2, 3, 4, with no 4-N label in a title',
     u4 && u4.parts.length === 4 && [1,2,3,4].every((n,i) => u4.parts[i].startsWith(`Unit 4 · Lesson ${n}: `)) &&
     u4.parts.every(t => !/·\s*4-\d/.test(t)), u4 && u4.parts);
  ck('Unit 5 is untouched: still seven parts', u5 && u5.parts.length === 7, u5 && u5.parts);

  // "Comes after Unit 5": the shelf she studied last leads, whatever its number.
  const order = await p.evaluate(() => {
    const names = () => shelvesFor('math').shelves.map(s => s.name).filter(n => /^Unit [45]$/.test(n));
    const lg = (unitId, ago) => put({id: 'log_t4_' + unitId, type:'log', mode:'quiz', classId:'math', unitId,
      date: AZ.today(), correct: 3, total: 5, seconds: 60, xp: 30, at: Date.now() - ago});
    lg('unit-m5u7', 5000);
    const a = names();
    lg('unit-m4u1', 1000);
    const b2 = names();
    ['log_t4_unit-m5u7','log_t4_unit-m4u1'].forEach(id => delete DATA.records[id]);
    return {a, b: b2};
  });
  ck('after Unit 5 work, Unit 5 leads; once she starts Unit 4, Unit 4 leads',
     order.a[0] === 'Unit 5' && order.b[0] === 'Unit 4', order);

  const meta = await p.evaluate((N) => N.map(n => {
    const u = DATA.records['unit-m4u'+n];
    return {n, cls:u.classId, round:u.round, libv:u.libv, series:u.series, prep:!!u.prep, order:u.order,
            quarter:u.quarter, cards:u.cards.length, qs:u.questions.length, src:u.srcName,
            lvs:[1,2,3].map(l=>u.questions.filter(q=>q.lv===l).length),
            slots:[0,1,2,3].map(i=>u.questions.filter(q=>q.ans===i).length),
            bad:u.questions.filter(q=>q.opts.length!==4 || new Set(q.opts).size!==4 || !(q.ans>=0&&q.ans<4)).map(q=>q.id),
            steps:u.questions.filter(q=>!(q.steps && q.steps.length>=3 && q.steps.length<=6) || !q.hint || !(q.ex&&q.ex.main&&q.ex.tip)).map(q=>q.id),
            bold:u.cards.every(c=>c.def.startsWith('**'))};
  }), NEW);
  ck('classId math, series Unit 4, libv, round 10, quarter 2, no prep, no order',
     meta.every(m=>m.cls==='math' && m.series==='Unit 4' && m.libv>=1 && m.round===10 && m.quarter===2 && !m.prep && m.order===undefined), meta);
  ck('8+ cards and 14+ questions each, all three levels', meta.every(m=>m.cards>=8 && m.qs>=14 && m.lvs.every(c=>c>0)), meta.map(m=>[m.cards,m.qs,m.lvs]));
  ck('answers in all four slots, four unique options, bold-first cards, steps/hint/ex on every question',
     meta.every(m=>m.slots.every(c=>c>0) && !m.bad.length && !m.steps.length && m.bold), meta.map(m=>[m.slots,m.bad,m.steps]));
  ck('srcName names the book lesson 4-1 … 4-4', meta.every(m=>m.src.includes('Lesson 4-'+m.n)), meta.map(m=>m.src));

  const files = await p.evaluate(async () => {
    const r = [];
    for (const n of [1,2,3,4]) {
      const j = await (await fetch(`./content/math-u4-l${n}.json`, {cache:'no-store'})).json();
      const u = j.records['unit-m4u'+n];
      r.push({n, status:u.status, past: u.updatedAt < Date.now() - 3600e3});
    }
    return r;
  });
  ck('shipped files are drafts stamped in the past', files.every(f=>f.status==='draft' && f.past), files);

  const t = await p.evaluate((N) => {
    const U = n => DATA.records['unit-m4u'+n];
    const qs = N.flatMap(n => U(n).questions.map(q => Object.assign({n}, q)));
    const ansOf = q => q && q.opts[q.ans];
    const find = (n, re) => U(n).questions.find(q => re.test(q.q));
    // Exact decimals as {i: BigInt, p: places}, so 0.1 × 3 is 0.3 and nothing else.
    const SUPN = {'¹':1,'²':2,'³':3,'⁴':4};
    const dec = s => { s = String(s).replace(/[$,]/g, '').trim();
      const m = s.match(/^10([¹²³⁴])$/); if (m) return {i: 10n ** BigInt(SUPN[m[1]]), p: 0};
      if (!/^\d+(\.\d+)?$/.test(s)) return null;
      const [a, f = ''] = s.split('.'); return {i: BigInt(a + f), p: f.length}; };
    const norm = x => { let {i, p} = x; while (p > 0 && i % 10n === 0n) { i /= 10n; p--; } return i + '/' + p; };
    const mul = (a, c) => ({i: a.i * c.i, p: a.p + c.p});
    const eq = (a, c) => a && c && norm(a) === norm(c);
    const lt = (a, c) => { const P = Math.max(a.p, c.p); return a.i * 10n ** BigInt(P - a.p) < c.i * 10n ** BigInt(P - c.p); };
    const round = x => { const s = 10n ** BigInt(x.p); return {i: (x.i * 2n + s) / (2n * s), p: 0}; };   // half up

    const worked = qs.filter(q => /^What is [\d.,]+ × [\d.,]+(10[¹²³⁴])?\?$/.test(q.q) || /^What is [\d.,]+ × 10[¹²³⁴]\?$/.test(q.q)).map(q => {
      const [, a, c] = q.q.match(/^What is ([\d.,]+) × ([\d.,¹²³⁴]+)\?$/);
      const want = mul(dec(a), dec(c));
      return {n:q.n, q:q.q, right: eq(dec(ansOf(q)), want),
              wrongDiffer: q.opts.every((o,i) => i === q.ans || !eq(dec(o), want))};
    });

    const eqs = s => { const m = s.match(/^([\d.,]+) × ([\d.,]+) = ([\d.,]+)$/); return eq(mul(dec(m[1]), dec(m[2])), dec(m[3])); };
    const tf = qs.filter(q => /^Which equation is (true|NOT true)\?$/.test(q.q)).map(q => {
      const want = !/NOT/.test(q.q);
      const hits = q.opts.map((o,i) => eqs(o) === want ? i : -1).filter(i => i >= 0);
      return {n:q.n, q:q.q, ok: hits.length === 1 && hits[0] === q.ans};
    });
    const ou = qs.filter(q => /gives an (OVER|UNDER)estimate\?$/.test(q.q)).map(q => {
      const over = /OVER/.test(q.q);
      const hits = q.opts.map((o,i) => { const [a, c] = o.split(' × ').map(dec); const est = mul(round(a), round(c)), ex = mul(a, c);
        return (over ? lt(ex, est) : lt(est, ex)) ? i : -1; }).filter(i => i >= 0);
      return {n:q.n, q:q.q, ok: hits.length === 1 && hits[0] === q.ans};
    });
    const less9 = (() => { const q = find(3, /^Which product is less than 9\?$/);
      const hits = q.opts.map((o,i) => { const [a, c] = o.split(' × ').map(dec); return lt(mul(a, c), dec('9')) ? i : -1; }).filter(i => i >= 0);
      return hits.length === 1 && hits[0] === q.ans; })();

    const W = [
      [1, /0\.48 × 10 to what power = 480/, '3'],
      [1, /5\.06 × 10 to what power = 5,060/, '3'],
      [1, /ladybug is 0\.6 cm/, '6 cm'],
      [1, /pollen is 2\.5 cm/, '0.025 cm'],
      [1, /rope is 4\.5 meters/, (45 - 4.5) + ' meters'],
      [1, /3\.8 meters long/, 'same length'],
      [2, /3\.86 × 21/, String(4 * 20)],
      [2, /0\.48 × 205/, String(0.5 * 200)],
      [2, /6\.9 × 42/, String(7 * 40)],
      [2, /19 notebooks cost at \$4\.10/, '$' + (4 * 20)],
      [2, /28 folders at \$1\.85/, '$' + (2 * 30)],
      [2, /12\.4 miles/, String(12 * 2 * 5)],
      [2, /4\.95 × 31 is about 15/, String(5 * 30)],
      [2, /\$4 × 12 = \$48/, 'has enough'],
      [3, /7 by 0\.896/, 'near 7'],
      [3, /4 sections, each 2\.35/, '9.4 meters'],
      [3, /3 gardens of 0\.8 acre/, '21.6 acres'],
      [3, /7 × 0\.6 less than or greater/, 'Less'],
      [3, /25 squares, three times/, '3 × 0.25 = 0.75'],
      [4, /47 × 6 = 282/, '28.2'],
      [4, /\$0\.35 on each muffin/, '$22.40'],
      [4, /6\.8 pounds each/, '23.1 pounds'],
      [4, /3\.5 meters wide/, '3.5 and 31.5'],
      [4, /0\.6 × 48, 6 × 4\.8 and 60 × 0\.48/, '28.8'],
      [4, /only one decimal place/, '2.70'],
    ].map(([n, re, want]) => { const q = find(n, re); return {n, re:String(re), want, got: ansOf(q), ok: !!q && String(ansOf(q)).includes(want)}; });

    // The practice pages' own multiplications, listed independently of the builder.
    const BOOK = ['4.58 × 10³','0.009 × 10','3.1 × 10³','42.3 × 10','0.062 × 10²','1.24 × 10⁴','0.086 × 10','63.7 × 10',
      '563.7 × 10²','0.365 × 10⁴','5.02 × 100','94.6 × 10³','0.9463 × 10²','0.678 × 100','681.7 × 10⁴','0.43','9.5 inches','2.6 miles',
      '4.82 × 1,000','0.482 × 10','48.2 × 10⁴','2.15 × 16','3.95','0.75 mile','0.87 × 112','104 × 0.33','9.02 × 80','0.54 × 24',
      '33.05 × 200','0.79 × 51','0.12 × 105','45.3 × 4','99.2 × 82','37 × 0.93','1.67 × 4','3.2 × 184','12 × 0.37','0.904 × 75',
      '18.8','1.28','23.7','21.8','39.45','27.54','9.91','78.95','18.19','11.6 × 9.5','4.49','12.9 × 0.9','0.62 × 1.5','8.46',
      '4 × 0.36','1.27','0.8 × 4','0.7 × 3','0.5 × 6','0.6 × 5','0.55 × 3','0.45 × 2','4 × 0.27','6 × 0.13','0.78 × 5','10 × 0.32',
      '6 × 2.03','1.35 × 5','100 × 0.12','4 × 0.15','3 × 2.5','0.9 × 7','0.35 × 3','1.25 acres','12.5 acres','0.989',
      '0.15 × 12','0.33 × 19','9.8 × 2','0.67 × 8','34 × 5.3','4.6 × 21','0.6 × 15','55 × 1.1','34.6 × 9','64.2 × 20','40 × 0.22',
      '57 × 2.3','5.8 × 11','56 × 0.4','170 × 0.003','0.3 × 99','26 × 1.61','50 × 0.914','10.76 × 100','2.54 × 12','956','18.4',
      '5.5 meters','75 × 0.3','7.5 × 3','75 × 0.03','50 × 0.12','0.5 × 12','50 × 1.2'];
    const said = qs.map(q => q.q + ' | ' + q.opts.join(' | ')).join(' || ');
    const reused = BOOK.filter(s => new RegExp('(^|[^\\d.,])' + s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '(?![\\d,])').test(said));
    const lean = qs.filter(q =>
      /^\s*(the|that|this|for the|using the|in the|with the) same\b/i.test(q.q) || /\bfrom before\b|\bthe previous\b|\bworksheet\b|\bpractice (page|sheet)\b/i.test(q.q) ||
      /\b(all|none|both) of the above\b|\b(first|second|third|fourth|last) (option|choice|answer)\b/i.test(q.q + ' ' + q.opts.join(' '))).map(q => q.n+'/'+q.id);
    const blob = N.map(n => JSON.stringify(U(n))).join(' ');
    return {worked, tf, ou, less9, W, reused, lean,
      exclaim: qs.some(q => /!/.test(q.q + q.ex.main + q.ex.tip)) || N.some(n => U(n).cards.some(c => /!/.test(c.def))),
      british: /\b(colour|metre|centre|favour|grey|neighbour)\b/i.test(blob),
      marks: /\b(she got|she scored|\d+ out of \d+|she was marked|marked (right|wrong) on)\b/i.test(blob)};
  }, NEW);
  ck('every "What is a × b?" re-derived here exactly and right', t.worked.length >= 15 && t.worked.every(x=>x.right), t.worked.filter(x=>!x.right).concat([{count:t.worked.length}]));
  ck('every wrong option there is a different number from the real product', t.worked.every(x=>x.wrongDiffer), t.worked.filter(x=>!x.wrongDiffer));
  ck('"which equation is true / NOT true" has exactly one matching option, and it is the answer', t.tf.length >= 2 && t.tf.every(x=>x.ok), t.tf);
  ck('over- and underestimate items: exactly one option rounds the asked way', t.ou.length === 2 && t.ou.every(x=>x.ok), t.ou);
  ck('"which product is less than 9" has exactly one true option', t.less9, t.less9);
  ck('word problems and set-ups re-derived', t.W.every(w=>w.ok), t.W.filter(w=>!w.ok));
  ck('none of the four practice pages\' own multiplications is reused', t.reused.length === 0, t.reused);
  ck('no stem leans on a sibling or a worksheet, no positional options', t.lean.length === 0, t.lean);
  ck('no exclamation marks, American spelling, no mark or score anywhere', !t.exclaim && !t.british && !t.marks, t);

  const rounds = await p.evaluate(async (N) => {
    const res = [];
    for (const n of N) {
      quizState = null;
      go('quiz', {unitId: 'unit-m4u'+n, classId: 'math'});
      const dealt = (quizState && quizState.order || []).length;
      let guard = 0;
      while (view === 'quiz' && guard++ < 80) {
        const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
        if (opts.length) { opts[0].click(); await new Promise(r=>setTimeout(r,4)); }
        const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
        if (next) { next.click(); await new Promise(r=>setTimeout(r,4)); continue; }
        if (!opts.length) break;
      }
      document.querySelectorAll('.modal-back, .modal-bg, .modal').forEach(m => m.remove());
      const lg = all('log').filter(l => l.unitId === 'unit-m4u'+n).pop();
      res.push({n, dealt, logged: !!lg, total: lg && lg.total});
    }
    return res;
  }, NEW);
  ck('a full ten-question round plays and logs on all four lessons',
     rounds.every(r => r.dealt >= 10 && r.logged && r.total === r.dealt), rounds);

  const deck = await p.evaluate(async (N) => {
    const r = [];
    for (const n of N) {
      cardState = {}; go('cards', {unitId:'unit-m4u'+n, classId:'math'});
      await new Promise(res=>setTimeout(res,30));
      r.push(!!document.querySelector('#screen .face'));
    }
    return r;
  }, NEW);
  ck('every flashcard deck renders', deck.every(Boolean), deck);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + String(JSON.stringify(r.got)).slice(0,600))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,5) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
