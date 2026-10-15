/* Unit 5 · Before You Start: Long Division with One-Digit Divisors (v186).
   Pins the arithmetic (every computed answer re-derived here, every wrong
   option failing the multiplication check), the teacher's own asks (checking
   with multiplication, finding the mistake), the remainder rules, the shelf,
   and a full round and deck. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8413;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const r = await p.evaluate(async () => {
    const j = await (await fetch('./content/math-longdiv-1.json', {cache:'no-store'})).json();
    const u = Object.values(j.records)[0]; u.status = 'approved'; DATA.records[u.id] = u;
    for (const f of ['content/math-u3-l1.json', 'content/math-facts-1.json']) {
      const k = await (await fetch('./' + f)).json(); const x = Object.values(k.records)[0]; x.status = 'approved'; DATA.records[x.id] = x; }
    saveLocal();
    const sh = shelvesFor('math');
    const u5 = sh.shelves.find(s => s.name === 'Unit 5');
    const num = s => Number(String(s).replace(/,/g, ''));
    const parse = s => { const m = String(s).match(/^([\d,]+)(?: R(\d+))?$/); return m ? [num(m[1]), m[2] ? +m[2] : 0] : null; };
    const comp = u.questions.filter(q => /^What is [\d,]+ ÷ \d\?$/.test(q.q)).map(q => {
      const [, a, d] = q.q.match(/^What is ([\d,]+) ÷ (\d)\?$/); const A = num(a), Dv = +d;
      const ans = parse(q.opts[q.ans]);
      const right = ans && ans[0] === Math.floor(A / Dv) && ans[1] === A % Dv;
      const wrongOk = q.opts.every((o, i) => i === q.ans || (() => { const w = parse(o); return !w || w[0]*Dv + w[1] !== A || w[1] >= Dv; })());
      return {q:q.q, right, wrongOk};
    });
    const blob = JSON.stringify(u);
    const ord = u.questions.find(q => q.kind === 'order');
    const txt = q => q.q + ' ' + q.opts[q.ans];
    return {
      inLib: CONTENT_LIBRARY.includes('content/math-longdiv-1.json'),
      classId: u.classId, series: u.series, libv: u.libv, n: u.questions.length, cards: u.cards.length,
      u5: u5 && u5.lessons.map(x => x.id), names: sh.shelves.map(s => s.name), loose: sh.loose.map(x => x.id),
      comp, compN: comp.length,
      slots: new Set(u.questions.filter(q => q.kind !== 'order').map(q => q.ans)).size,
      lv: [1,2,3].map(l => u.questions.filter(q => q.lv === l).length),
      emailNums: /\b123 ÷ 3\b|1,?723/.test(blob),
      zero: u.questions.some(q => /824 ÷ 4|3,612 ÷ 6/.test(q.q) && q.opts.includes('26') || q.opts.includes('62')),
      check: u.questions.some(q => /checks it/.test(q.q) && /96 × 6 \+ 3 = 579/.test(q.opts[q.ans])),
      mistakes: u.questions.filter(q => /mistake|wrong/i.test(q.q)).length,
      bigRem: u.questions.some(q => /bigger than the divisor/.test(q.opts[q.ans])),
      roundUp: u.questions.some(q => /cars/.test(q.q) && q.opts[q.ans] === '7'),
      dropRem: u.questions.some(q => /bows/.test(q.q) && q.opts[q.ans] === '6'),
      remAns: u.questions.some(q => /teacher get/.test(q.q) && q.opts[q.ans] === '1'),
      ord: ord && ord.opts.join('>') === 'Divide>Multiply>Subtract>Bring down' && ord.ans === 0,
      backref: u.questions.filter(q => /^(the|that|this) same\b/i.test(q.q)).length,
      posref: u.questions.filter(q => /\b(all|none) of the above\b/i.test(q.opts.join(' '))).length,
      bold: u.cards.every(c => c.def.startsWith('**')),
    };
  });
  ck('in CONTENT_LIBRARY, math classId, series Unit 5, libv', r.inLib && r.classId === 'math' && r.series === 'Unit 5' && r.libv >= 1, r);
  ck('a Unit 5 shelf holding the review, beside the other maths shelves, nothing loose',
     JSON.stringify(r.u5) === '["unit-m5-ld1"]' && r.names.includes('Unit 3') && r.names.includes('Math Facts') && r.loose.length === 0, r);
  ck('every "What is a ÷ b?" answer is re-derived here and right', r.compN >= 8 && r.comp.every(c => c.right), r.comp.filter(c=>!c.right));
  ck('every wrong option there fails the multiplication check (or keeps a remainder too big)', r.comp.every(c => c.wrongOk), r.comp.filter(c=>!c.wrongOk));
  ck('18+ questions across all three levels, answers in all four slots', r.n >= 18 && r.lv.every(x => x > 0) && r.slots === 4, r);
  ck('none of the email’s own examples is reused', !r.emailNums, r.emailNums);
  ck('a skipped zero is offered as a real wrong answer', r.zero, r.zero);
  ck('checking with multiplication is asked', r.check, r.check);
  ck('the teacher’s own tip: at least two find-the-mistake questions', r.mistakes >= 2, r.mistakes);
  ck('a remainder bigger than the divisor is named as the giveaway', r.bigRem, r.bigRem);
  ck('remainders in stories: round up, drop it, and the remainder as the answer', r.roundUp && r.dropRem && r.remAns, r);
  ck('the four steps stored in order', r.ord, r.ord);
  ck('no back-references, no positional references, bold-first cards', !r.backref && !r.posref && r.bold, r);

  const play = await p.evaluate(async () => {
    quizState = null; go('quiz', {unitId:'unit-m5-ld1', classId:'math'});
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
    const log = all('log').find(l => l.unitId === 'unit-m5-ld1');
    go('cards', {unitId:'unit-m5-ld1', classId:'math'});
    let seen = 0, g2 = 0;
    while (view === 'cards' && g2++ < 30) { const nx = document.querySelector('#screen .btn-primary'); if (!nx) break; nx.click(); seen++; await new Promise(r=>setTimeout(r,6)); }
    return { logged: !!log, total: log && log.total, seen };
  });
  ck('a full round of 10 plays and logs, and the deck walks', play.logged && play.total === 10 && play.seen >= 9, play);

  out.forEach(r => console.log((r.ok ? '  ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' → ' + JSON.stringify(r.got).slice(0,300))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
