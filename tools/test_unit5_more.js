/* Unit 5 · Lessons 4, 5 and 7 (partial quotients, recording division with a
   two-digit divisor, choosing a strategy) join the Unit 5 shelf after
   Lessons 1–3. There is no 5-6 page in Drive, so there is no Lesson 6.

   Pins the shelf order, the flags, every quotient re-derived HERE from its own
   stem (not trusted from the builder), every wrong option on a worked division
   failing the real-answer test (quotient × divisor + remainder = dividend, with
   a remainder smaller than the divisor), none of the practice pages' own
   divisions reused, the standalone rules, a full round on each new lesson, and
   each deck. Counts are minimums, never exact. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8413;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});
  const NEW = [4,5,7];

  const seed = await p.evaluate(async () => {
    const files = ['math-longdiv-1','math-u5-l1','math-u5-l2','math-u5-l3','math-u5-l4','math-u5-l5','math-u5-l7','math-u3-l1'];
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
  ck('Before You Start, six Unit 5 lessons and a Unit 3 lesson seed', seed.length === 8, seed);

  const shelves = await p.evaluate(() => {
    const r = shelvesFor('math');
    return {loose: r.loose.map(u=>u.title),
            books: r.shelves.map(s => ({name: s.name, parts: s.lessons.map(u=>u.title)}))};
  });
  const u5 = shelves.books.find(s => s.name === 'Unit 5');
  ck('Unit 5 is its own shelf, beside Unit 3, nothing loose',
     !!u5 && shelves.books.some(s => s.name === 'Unit 3') && shelves.loose.length === 0, shelves);
  ck('the shelf reads Before You Start, then Lesson 1, 2, 3, 4, 5, 7',
     u5 && u5.parts.length === 7 && u5.parts[0].startsWith('Unit 5 · Before You Start') &&
     [1,2,3,4,5,7].every((n,i) => u5.parts[i+1].startsWith(`Unit 5 · Lesson ${n}: `)), u5 && u5.parts);
  ck('no Lesson 6, and no title reuses the book\'s 5-N label',
     u5 && !u5.parts.some(t => /Lesson 6\b/.test(t)) && u5.parts.every(t => !/·\s*5-\d/.test(t)), u5 && u5.parts);

  const meta = await p.evaluate((N) => N.map(n => {
    const u = DATA.records['unit-m5u'+n];
    return {n, cls:u.classId, round:u.round, libv:u.libv, series:u.series, prep:!!u.prep, order:u.order,
            quarter:u.quarter, status:'(seeded)', cards:u.cards.length, qs:u.questions.length, src:u.srcName,
            lvs:[1,2,3].map(l=>u.questions.filter(q=>q.lv===l).length),
            slots:[0,1,2,3].map(i=>u.questions.filter(q=>q.ans===i).length),
            bad:u.questions.filter(q=>q.opts.length!==4 || new Set(q.opts).size!==4 || !(q.ans>=0&&q.ans<4)).map(q=>q.id),
            steps:u.questions.filter(q=>!(q.steps && q.steps.length>=3 && q.steps.length<=6) || !q.hint || !(q.ex&&q.ex.main&&q.ex.tip)).map(q=>q.id),
            bold:u.cards.every(c=>c.def.startsWith('**'))};
  }), NEW);
  ck('classId math, series Unit 5, libv, round 10, quarter 2, no prep, no order',
     meta.every(m=>m.cls==='math' && m.series==='Unit 5' && m.libv>=1 && m.round===10 && m.quarter===2 && !m.prep && m.order===undefined), meta);
  ck('8+ cards and 14+ questions each, all three levels', meta.every(m=>m.cards>=8 && m.qs>=14 && m.lvs.every(c=>c>0)), meta.map(m=>[m.cards,m.qs,m.lvs]));
  ck('answers in all four slots, four unique options, bold-first cards, steps/hint/ex on every question',
     meta.every(m=>m.slots.every(c=>c>0) && !m.bad.length && !m.steps.length && m.bold), meta.map(m=>[m.slots,m.bad,m.steps]));
  ck('srcName names the book lesson 5-4 / 5-5 / 5-7', meta.every(m=>m.src.includes('Lesson 5-'+m.n)), meta.map(m=>m.src));
  const files = await p.evaluate(async () => {
    const r = [];
    for (const n of [4,5,7]) {
      const j = await (await fetch(`./content/math-u5-l${n}.json`, {cache:'no-store'})).json();
      const u = j.records['unit-m5u'+n];
      r.push({n, status:u.status, past: u.updatedAt < Date.now() - 3600e3});
    }
    return r;
  });
  ck('shipped files are drafts stamped in the past', files.every(f=>f.status==='draft' && f.past), files);

  const t = await p.evaluate((N) => {
    const U = n => DATA.records['unit-m5u'+n];
    const num = s => Number(String(s).replace(/,/g, ''));
    const parse = s => { const m = String(s).match(/^([\d,]+)(?: R(\d+))?$/); return m && {q: num(m[1]), r: m[2] ? +m[2] : 0}; };
    const real = (a, d, x) => x && x.q * d + x.r === a && x.r >= 0 && x.r < d;
    const ansOf = q => q && q.opts[q.ans];
    const find = (n, re) => U(n).questions.find(q => re.test(q.q));
    const qn = (a, d) => ({q: Math.floor(a/d), r: a % d});

    // Every "What is a ÷ b?" — answer re-derived, every wrong option fails the real-answer test.
    const div = N.flatMap(n => U(n).questions.filter(q => /^What is [\d,]+ ÷ [\d,]+\?$/.test(q.q)).map(q => {
      const [, a, d] = q.q.match(/^What is ([\d,]+) ÷ ([\d,]+)\?$/); const A = num(a), D = num(d);
      const want = qn(A, D), got = parse(ansOf(q));
      return {n, q:q.q, right: got && got.q === want.q && got.r === want.r,
              wrongFail: q.opts.every((o,i) => i === q.ans || !real(A, D, parse(o)))};
    }));

    // "Which division has a quotient of …?" — exactly one option hits, and it is the answer.
    const which = N.flatMap(n => U(n).questions.filter(q => /^Which division has a quotient of /.test(q.q)).map(q => {
      const t = parse(q.q.match(/quotient of ([\d,]+(?: R\d+)?)\?/)[1]);
      const hits = q.opts.map((o,i) => { const [a, d] = o.split(' ÷ ').map(num); const v = qn(a, d); return v.q === t.q && v.r === t.r ? i : -1; }).filter(i => i >= 0);
      return {n, q:q.q, ok: hits.length === 1 && hits[0] === q.ans};
    }));

    // Critiques: the fixed answer named in the option is the real quotient of the stem's division.
    const crit = N.flatMap(n => U(n).questions.filter(q => /found|wrote/.test(q.q) && /What should he fix\?$/.test(q.q)).map(q => {
      const [, a, d] = q.q.match(/([\d,]+) ÷ ([\d,]+)/); const A = num(a), D = num(d);
      const fix = parse(ansOf(q).match(/: ([\d,]+ R\d+)$/)[1]);
      const claimed = parse(q.q.match(/(?:= |wrote )([\d,]+ R\d+)\./)[1]);
      return {n, q:q.q, ok: real(A, D, fix) && claimed.q*D + claimed.r === A && claimed.r >= D};
    }));

    // Word problems and set-ups, each re-derived from its own numbers.
    const W = [
      [4, /672 books/, String(672/24)],
      [4, /504 pages in 12 minutes/, String(504/12/2)],
      [4, /713 ÷ 23 = 13/, String(Math.round(700/20))],
      [4, /638 ÷ 22/, String(638/22)],
      [4, /486 ÷ 18/, '20 groups'],
      [4, /525 ÷ 15/, String(30+5)],
      [4, /527 ÷ 24/, String(Math.floor(527/24/10)*10)],
      [5, /214 students/, String(Math.ceil(214/36))],
      [5, /500 tulip bulbs/, String(Math.floor(500/45))],
      [5, /330 apples/, String(330 % 14)],
      [5, /900 stickers/, String(Math.floor(900/38))],
      [5, /437 ÷ 21/, `21 × ${Math.floor(437/21)} + ${437%21} = 437`],
      [5, /517 ÷ 64/, Math.floor(517/64) < 10 ? 'One digit' : 'Two digits'],
      [5, /739 ÷ 31/, Math.floor(739/31) >= 10 && Math.floor(739/31) < 100 ? 'The tens place' : 'other'],
      [7, /9,216 seats/, String(9216/48)],
      [7, /2,880 eggs/, '$' + String(2880/12*3)],
      [7, /4,560 ÷ 19/, (4600/20) + ', so the answer should be in the hundreds'],
      [7, /6,422 people/, String(6422/26)],
      [7, /1,000 pencils/, String(Math.ceil(1000/24))],
      [7, /4,176 ÷ 36/, String(Math.floor(4176/36)).length === 3 ? 'Three digits' : 'other'],
      [7, /5,600 ÷ 80/, String(5600/80)],
      [7, /2,890 ÷ 17/, (Math.floor(2890/17/100)*100) + ' and ' + (Math.floor(2890/17/100)*100+100)],
    ].map(([n, re, want]) => { const q = find(n, re); return {n, re:String(re), want, got: ansOf(q), ok: !!q && String(ansOf(q)).includes(want)}; });

    // The practice pages' own divisions, listed independently of the builder.
    const BOOK = ['375 ÷ 15','233 ÷ 11','210 ÷ 15','286 ÷ 13','575 ÷ 25','960 ÷ 32','247 ÷ 19','631 ÷ 14','132 ÷ 11',
      '845 ÷ 21','304 ÷ 16','480 ÷ 32','715 ÷ 23','660 ÷ 30','731 ÷ 43','610 ÷ 16','969 ÷ 19','272 ÷ 8','325 ÷ 13',
      '1,400 ÷ 4','704 ÷ 32','420 ÷ 12','1,078 ÷ 49','875 ÷ 25','1,890 ÷ 30','7,700 ÷ 22','1,430 ÷ 65','14,000 ÷ 40','4,500 ÷ 50',
      '258 ÷ 12','200 ÷ 12','196 ÷ 14','766 ÷ 80','304 ÷ 19','593 ÷ 61','360 ÷ 11','544 ÷ 17','250 ÷ 50','867 ÷ 68',
      '966 ÷ 23','492 ÷ 79','375 ÷ 40','980 ÷ 60','660 ÷ 48','3,200 ÷ 10','975 ÷ 15','335 ÷ 40','365 ÷ 40','409 ÷ 40','415 ÷ 40',
      '3,720 ÷ 15','4,618 ÷ 32','452 ÷ 21','378 ÷ 54','664 ÷ 83','761 ÷ 5','510 ÷ 30','7,704 ÷ 24','7,830 ÷ 33',
      '3,136 ÷ 64','6,253 ÷ 71','3,300 ÷ 12','9,690 ÷ 34','4,600 ÷ 10','966 ÷ 21','2,385 ÷ 53','946 ÷ 43','2,116 ÷ 46'];
    const said = N.flatMap(n => U(n).questions.map(q => q.q + ' | ' + q.opts.join(' | '))).join(' || ');
    const reused = BOOK.filter(s => new RegExp('(^|[^\\d,])' + s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '(?![\\d,])').test(said));
    const lean = N.flatMap(n => U(n).questions.filter(q =>
      /^\s*(the|that|this|for the|using the|in the|with the) same\b/i.test(q.q) || /\bfrom before\b|\bthe previous\b|\bworksheet\b|\bpractice (page|sheet)\b/i.test(q.q) ||
      /\b(all|none|both) of the above\b|\b(first|second|third|fourth|last) (option|choice|answer)\b/i.test(q.q + ' ' + q.opts.join(' '))).map(q => n+'/'+q.id));
    const blob = N.map(n => JSON.stringify(U(n))).join(' ');
    return {div, divN: div.length, which, crit, W, reused, lean,
      exclaim: N.some(n => U(n).questions.some(q => /!/.test(q.q + q.ex.main + q.ex.tip)) || U(n).cards.some(c => /!/.test(c.def))),
      british: /\b(colour|metre|centre|favour|grey|neighbour)\b/i.test(blob),
      marks: /\b(she got|she scored|\d+ out of \d+|she was marked|marked (right|wrong) on)\b/i.test(blob),
      slips: {
        rem: N.flatMap(n => U(n).questions).filter(q => /^What is/.test(q.q) && / R\d+$/.test(ansOf(q))).every(q => {
          const a = parse(ansOf(q)); return q.opts.some(o => { const x = parse(o); return x && x.q === a.q && x.r === 0; }) ||
                                             q.opts.some(o => { const x = parse(o); return x && x.q === a.q - 1; }); }),
      }};
  }, NEW);
  ck('every "What is a ÷ b?" re-derived here and right', t.divN >= 12 && t.div.every(x=>x.right), t.div.filter(x=>!x.right));
  ck('every wrong option there fails quotient × divisor + remainder = dividend (or keeps a remainder too big)',
     t.div.every(x=>x.wrongFail), t.div.filter(x=>!x.wrongFail));
  ck('every remainder question offers the remainder-left-off or one-group-short slip', t.slips.rem, t.slips);
  ck('"which division has a quotient of …" has exactly one true option, and it is the answer', t.which.length >= 3 && t.which.every(x=>x.ok), t.which);
  ck('critiques: the stated answer leaves a remainder too big, and the fix is the real quotient', t.crit.length >= 3 && t.crit.every(x=>x.ok), t.crit);
  ck('word problems and set-ups re-derived', t.W.every(w=>w.ok), t.W.filter(w=>!w.ok));
  ck('none of the 5-4, 5-5 or 5-7 practice pages\' own divisions is reused', t.reused.length === 0, t.reused);
  ck('no stem leans on a sibling or a worksheet, no positional options', t.lean.length === 0, t.lean);
  ck('no exclamation marks, American spelling, no mark or score anywhere', !t.exclaim && !t.british && !t.marks, t);

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
  }, NEW);
  ck('a full ten-question round plays and logs on all three new lessons',
     rounds.every(r => r.dealt >= 10 && r.logged && r.total === r.dealt), rounds);

  const deck = await p.evaluate(async (N) => {
    const r = [];
    for (const n of N) {
      cardState = {}; go('cards', {unitId:'unit-m5u'+n, classId:'math'});
      await new Promise(res=>setTimeout(res,30));
      r.push(!!document.querySelector('#screen .face'));
    }
    return r;
  }, NEW);
  ck('every flashcard deck renders', deck.every(Boolean), deck);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + String(JSON.stringify(r.got)).slice(0,500))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,5) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
