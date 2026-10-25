/* Unit 5 · Lessons 1–3 (dividing by two-digit divisors) join the Unit 5 shelf
   behind "Before You Start: Long Division with One-Digit Divisors" (v186).

   Pins the shelf order, the flags, every quotient re-derived HERE (not trusted
   from the builder), the named slips offered as real wrong options, none of
   the practice pages' own divisions reused, the standalone rules, and a full
   round on each lesson. Counts are minimums, never exact. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8413;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});
  const N = [1,2,3];

  const seed = await p.evaluate(async (N) => {
    const files = ['math-longdiv-1'].concat(N.map(n => `math-u5-l${n}`)).concat(['math-u3-l1','math-u3-l2']);
    const ids = [];
    for (const f of files) {
      const j = await (await fetch(`./content/${f}.json`, {cache:'no-store'})).json();
      const u = Object.values(j.records).find(r => r.type === 'unit');
      u.status = 'approved'; u.updatedAt = Date.now() - 6e5;
      DATA.records[u.id] = u; ids.push(u.id);
    }
    saveLocal();
    return ids;
  }, N);
  ck('Before You Start, three Unit 5 lessons and two Unit 3 lessons seed', seed.length === 6, seed);

  const shelves = await p.evaluate(() => {
    const r = shelvesFor('math');
    return {loose: r.loose.map(u=>u.title),
            books: r.shelves.map(s => ({name: s.name, parts: s.lessons.map(u=>u.title)}))};
  });
  const u5 = shelves.books.find(s => s.name === 'Unit 5');
  ck('Unit 5 is its own shelf, beside Unit 3, nothing loose',
     !!u5 && shelves.books.some(s => s.name === 'Unit 3') && shelves.loose.length === 0, shelves);
  ck('the shelf reads Before You Start, then Lesson 1, 2, 3',
     u5 && u5.parts.length === 4 && u5.parts[0].startsWith('Unit 5 · Before You Start') &&
     [1,2,3].every(i => u5.parts[i].startsWith(`Unit 5 · Lesson ${i}: `)), u5 && u5.parts);
  ck('no title reuses the book\'s 5-N label', u5 && u5.parts.every(t => !/·\s*5-\d/.test(t)), u5 && u5.parts);

  const meta = await p.evaluate((N) => N.map(n => {
    const u = DATA.records['unit-m5u'+n];
    return {cls:u.classId, round:u.round, libv:u.libv, series:u.series, prep:!!u.prep, order:u.order,
            cards:u.cards.length, qs:u.questions.length, src:u.srcName,
            lvs:[1,2,3].map(l=>u.questions.filter(q=>q.lv===l).length),
            slots:[0,1,2,3].map(i=>u.questions.filter(q=>q.ans===i).length),
            bad:u.questions.filter(q=>q.opts.length!==4 || new Set(q.opts).size!==4 || !(q.ans>=0&&q.ans<4)).map(q=>q.id),
            bold:u.cards.every(c=>c.def.startsWith('**'))};
  }), N);
  ck('classId math, series Unit 5, libv, round 10, no prep, no order',
     meta.every(m=>m.cls==='math' && m.series==='Unit 5' && m.libv>=1 && m.round===10 && !m.prep && m.order===undefined), meta);
  ck('8+ cards and 12+ questions each, all three levels', meta.every(m=>m.cards>=8 && m.qs>=12 && m.lvs.every(c=>c>0)), meta.map(m=>[m.cards,m.qs,m.lvs]));
  ck('answers in all four slots, four unique options each, bold-first cards',
     meta.every(m=>m.slots.every(c=>c>0) && !m.bad.length && m.bold), meta.map(m=>[m.slots,m.bad]));
  ck('srcName names the book lesson 5-1 / 5-2 / 5-3', meta.every((m,i)=>m.src.includes('Lesson 5-'+(i+1))), meta.map(m=>m.src));

  const t = await p.evaluate((N) => {
    const U = n => DATA.records['unit-m5u'+n];
    const num = s => Number(String(s).replace(/[^\d.]/g, ''));
    const find = (n, re) => U(n).questions.find(q => re.test(q.q));
    const ansOf = q => q && q.opts[q.ans];
    const has = (q, v) => q && q.opts.some(o => num(o) === v);
    // Every "What is a ÷ b?" in lessons 1 and 3 is an exact division: re-derive it.
    const exact = [1,3].flatMap(n => U(n).questions.filter(q => /^What is [\d,]+ ÷ [\d,]+\?$/.test(q.q)).map(q => {
      const [, a, d] = q.q.match(/^What is ([\d,]+) ÷ ([\d,]+)\?$/); const A = num(a), D = num(d);
      return {q:q.q, right: A % D === 0 && num(ansOf(q)) === A / D,
              wrongFail: q.opts.every((o,i) => i === q.ans || num(o) * D !== A)};
    }));
    // Lesson 3's area questions: the side-by-side and tens-only slips, computed here.
    const area = U(3).questions.filter(q => /^What is [\d,]+ ÷ [\d,]+\?$/.test(q.q)).map(q => {
      const [, a, d] = q.q.match(/^What is ([\d,]+) ÷ ([\d,]+)\?$/); const Q = num(a) / num(d);
      const tens = Math.floor(Q/10)*10, ones = Q % 10;
      return has(q, Number(String(tens) + String(ones))) && has(q, tens);
    });
    // Lesson 2 estimates: the answer must sit within 20% of the true quotient, and the
    // wrong-way-rounding slip must be on offer.
    const est = [[413,58,7,8],[1630,41,40,null],[3467,72,50,40]].map(([a,d,e,wrong]) => {
      const q = find(2, new RegExp(`estimate ${a.toLocaleString('en-US')} ÷ ${d}\\.`));
      return {a, ok: q && num(ansOf(q)) === e && Math.abs(a/d - e) <= 0.2*e && (wrong === null || has(q, wrong)) && has(q, e*10)};
    });
    // Word problems, re-derived.
    const word = [
      [1, /5,400 stickers/, 5400/60], [1, /35,000 tickets/, 35000/70],
      [3, /432 square feet/, 432/18], [3, /351 singers/, 351/13], [3, /630 miles/, 630/45]]
      .map(([n, re, v]) => ({re:String(re), ok: num(ansOf(find(n, re))) === v}));
    const q4000 = find(1, /^What is 4,000 ÷ 80\?$/);
    const pepper = find(1, /pepper/);
    const noah = find(3, /Noah/);
    const ava = find(2, /Ava estimates/);
    // The practice pages' own divisions, listed independently of the builder.
    const BOOK = ['18,000 ÷ 90','10,000 ÷ 50','210 ÷ 30','12,000','480 ÷ 60','15,000 ÷ 30','8,100 ÷ 90','2,800 ÷ 70',
      '30,000 ÷ 50','1,800 ÷ 60','560 ÷ 70','360 ÷ 60','6,000 ÷ 50','24,000 ÷ 60','2,000 ÷ 20','6,300 ÷ 90',
      '21,000','2,500 ÷ 50','72,000','56,000','45,000 ÷ 90','42,000 ÷ 70','64,000','32,000','27,000','2,400 ÷ 80',
      '4,200','159 ÷ 75','230','425','287 ÷ 42','320 ÷ 11','208 ÷ 72','554 ÷ 62','815 ÷ 23','2,491','412 ÷ 84',
      '288 ÷ 37','2,964','228 ÷ 19','1,784','7,260','2,280','485 ÷ 92','540 ÷ 61','1,710','2,740','4,322',
      '5,700','7,810','6,395','817','3,128','225 ÷ 12','617','360 ÷ 20','408 ÷ 12','154 ÷ 11','156 ÷ 12',
      '682 ÷ 22','143 ÷ 11','182 ÷ 13','342 ÷ 38','720 ÷ 16','608 ÷ 19','752 ÷ 47','375 ÷ 25','576 ÷ 24',
      '210 ÷ 15','714','391 ÷ 23','512 ÷ 16','286 ÷ 22'];
    const stems = N.flatMap(n => U(n).questions.map(q => q.q)).join(' | ');
    const reused = BOOK.filter(s => stems.includes(s));
    const lean = N.flatMap(n => U(n).questions.filter(q =>
      /^(the|that|this) same\b/i.test(q.q.trim()) || /\bfrom before\b|\bthe previous\b/i.test(q.q) ||
      /\b(all|none|both) of the above\b|\b(first|second|third|last) (option|choice)\b/i.test(q.opts.join(' '))).map(q => n+'/'+q.id));
    const blob = N.map(n => JSON.stringify(U(n))).join(' ');
    return {
      exact, exactN: exact.length, area, est, word,
      borrowed: q4000 && ansOf(q4000) === '50' && has(q4000, 500),
      units: pepper && /2,000 ÷ 40 = 50/.test(ansOf(pepper)) && pepper.opts.some(o => /2 ÷ 40/.test(o)),
      sideBySide: noah && /side by side/.test(ansOf(noah)) && /28/.test(ansOf(noah)),
      direction: ava && /^More/.test(ansOf(ava)),
      reused, lean,
      british: /\b(colour|metre|centre|favour|grey|neighbour)\b/i.test(blob),
      marks: /\b(she got|she scored|\d+ out of \d+|marked (right|wrong))\b/i.test(blob),
    };
  }, N);
  ck('every exact "What is a ÷ b?" re-derived here and right', t.exactN >= 6 && t.exact.every(x=>x.right), t.exact.filter(x=>!x.right));
  ck('every wrong option there fails the multiplication check', t.exact.every(x=>x.wrongFail), t.exact.filter(x=>!x.wrongFail));
  ck('L1: the borrowed zero (4,000 ÷ 80 = 50) offers the counted-twice slip, 500', t.borrowed);
  ck('L1: kilograms changed to grams before dividing, and the unconverted slip offered', t.units);
  ck('L2: estimates land near the real quotient, with the wrong-way rounding and extra-zero slips', t.est.every(e=>e.ok), t.est);
  ck('L2: making the dividend smaller and divisor bigger means the real answer is more', t.direction);
  ck('L3: every area-model division offers the side-by-side and tens-only slips', t.area.length >= 2 && t.area.every(Boolean), t.area);
  ck('L3: the side-by-side mistake is taught (20 and 8 make 28)', t.sideBySide);
  ck('word problems re-derived', t.word.every(w=>w.ok), t.word);
  ck('none of the practice pages\' own divisions is reused', t.reused.length === 0, t.reused);
  ck('no stem leans on a sibling, no positional options', t.lean.length === 0, t.lean);
  ck('American spelling, and no mark or score anywhere (v198)', !t.british && !t.marks, t);

  const rounds = await p.evaluate(async (N) => {
    const res = [];
    for (const n of N) {
      quizState = null;
      go('quiz', {unitId: 'unit-m5u'+n, classId: 'math'});
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
      const lg = all('log').filter(l => l.unitId === 'unit-m5u'+n).pop();
      res.push({n, dealt, logged: !!lg, total: lg && lg.total});
    }
    return res;
  }, N);
  ck('a full ten-question round plays and logs on all three lessons',
     rounds.every(r => r.dealt >= 10 && r.logged && r.total === r.dealt), rounds);

  const deck = await p.evaluate(async (N) => {
    const r = [];
    for (const n of N) {
      cardState = {}; go('cards', {unitId:'unit-m5u'+n, classId:'math'});
      await new Promise(res=>setTimeout(res,30));
      r.push(!!document.querySelector('#screen .face'));
    }
    return r;
  }, N);
  ck('every flashcard deck renders', deck.every(Boolean), deck);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + String(JSON.stringify(r.got)).slice(0,400))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,5) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
