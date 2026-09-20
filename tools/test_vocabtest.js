/* v169 — the Wordly Wise units rebuilt to River's real test format.

   Pins the SHAPES, never question ids: a renumber must not break this, and
   the whole point of the change is which shapes exist, not where they sit.

   The five sections of her Unit 2 Vocabulary Test:
     1 context clues off a passage   2 synonyms/antonyms
     3 sentence completion            4 parts of speech (three options)
     5 word association                                                     */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8501;

const REBUILT = ['unit-ww503', 'unit-ww504', 'unit-ww505'];
const FILES = ['wordly-wise-5-02', 'wordly-wise-5-03',
               'wordly-wise-5-04', 'wordly-wise-5-05'];

// The five shapes, recognised from the question itself.
const SHAPE = {
  ctx:   q => !!q.passage,
  syn:   q => /^Which word means the (SAME as|OPPOSITE of)/.test(q.q),
  fit:   q => /\.\.\.$/.test(q.q.split('\n')[0]) && !q.passage,
  pos:   q => /What part of speech is/.test(q.q),
  assoc: q => /Which word connects to all three\?/.test(q.q),
};

(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const seed = await p.evaluate(async (files) => {
    const got = {};
    for (const f of files) {
      const j = await (await fetch('./content/'+f+'.json',{cache:'no-store'})).json();
      const u = Object.values(j.records).find(x => x.type === 'unit');
      u.status = 'approved'; u.updatedAt = Date.now()-1000; DATA.records[u.id] = u;
      got[u.id] = {id:u.id, title:u.title, libv:u.libv, classId:u.classId,
                   cards:u.cards.length, qs:u.questions, blob:JSON.stringify(u)};
    }
    saveLocal();
    return got;
  }, FILES);

  // --- every rebuilt lesson carries all five shapes, four of each ---------
  for (const id of REBUILT) {
    const qs = seed[id].qs;
    const counts = {};
    for (const k of Object.keys(SHAPE)) counts[k] = qs.filter(q => SHAPE[k](eval('0,q'))).length;
    ck(id + ': all five test shapes present, four of each',
       Object.keys(SHAPE).every(k => counts[k] === 4), counts);
    ck(id + ': classId english and a bumped libv',
       seed[id].classId === 'english' && seed[id].libv >= 2,
       [seed[id].classId, seed[id].libv]);
    // The reason this work happened at all.
    const recall = qs.filter(q => /^What (does|is) \w+ ?\w* ?mean\?$|^What is an? /.test(q.q));
    ck(id + ': no bare "What does X mean?" questions left',
       recall.length === 0, recall.map(q => q.q));
  }

  // --- parts of speech: three options, and the set really is the parts ----
  const allPos = REBUILT.concat(['unit-ww502'])
    .flatMap(id => seed[id].qs.filter(SHAPE.pos));
  ck('every parts-of-speech question offers exactly noun/adjective/verb',
     allPos.length >= 15 && allPos.every(q =>
       q.opts.length === 3 &&
       JSON.stringify([...q.opts].sort()) === JSON.stringify(['adjective','noun','verb'])),
     allPos.length);
  ck('their answers are spread across the parts, not all one',
     new Set(allPos.map(q => q.opts[q.ans])).size === 3,
     allPos.map(q => q.opts[q.ans]).reduce((a,x)=>(a[x]=(a[x]||0)+1,a),{}));

  // --- passages stay inside the cap that keeps options above the fold -----
  const allCtx = REBUILT.flatMap(id => seed[id].qs.filter(SHAPE.ctx));
  ck('every passage is within the 45-word cap',
     allCtx.every(q => q.passage.split(/\s+/).length <= 45),
     allCtx.map(q => q.passage.split(/\s+/).length));
  /* The paper's Section 1 always asks how a term is used IN the passage, so
     a stem naming a word the passage never uses is a different, easier
     question. Matched on content words rather than on quotation marks: the
     stem does not always quote the term, and a five-letter prefix lets
     "obscure" in the stem find "obscured" in the passage. The strong version
     of this rule is asserted at build time inside ctx(). */
  const SCAFFOLD = new Set(('what does do this that tell you the word used here '
    + 'passage context clues about suggest best mean means term is a an in of how '
    + 'its say to and for').split(' '));
  const grounded = q => {
    const psg = q.passage.toLowerCase();
    return q.q.toLowerCase().replace(/[^a-z\s]/g, ' ').split(/\s+/)
            .filter(w => w.length >= 4 && !SCAFFOLD.has(w))
            .some(w => psg.includes(w.slice(0, 5)));
  };
  ck('every context question asks about a word its own passage contains',
     allCtx.every(grounded),
     allCtx.filter(q => !grounded(q)).map(q => q.q.slice(0, 60)));

  // --- Lesson 2 was APPENDED to, never renumbered -------------------------
  const l2 = seed['unit-ww502'].qs;
  ck('Lesson 2 keeps its original fifteen ids and adds six',
     l2.length === 21 && l2.slice(0,15).every((q,i) => q.id === 'q'+i) &&
     l2.slice(15).every((q,i) => q.id === 'q'+(15+i)), l2.map(q=>q.id).join(','));
  ck('the additions target cultivate and the parts of speech she missed',
     /merge/.test(seed['unit-ww502'].blob) &&
     l2.slice(15).filter(SHAPE.pos).length === 3 &&
     l2.slice(15).some(q => /export/i.test(q.q)) &&
     l2.slice(15).some(q => /craving/i.test(q.q)),
     l2.slice(15).map(q => q.q.split('\n')[0].slice(0,42)));

  // --- it renders: three options, above the fold, and credits -------------
  const live = await p.evaluate(async () => {
    const u = DATA.records['unit-ww504'];
    const posQ = u.questions.find(q => /What part of speech is/.test(q.q));
    const ctxQ = u.questions.find(q => q.passage);
    // Report a missing shape rather than throwing on indexOf(undefined) —
    // run against the pre-v169 bank this block used to die with a stack
    // trace instead of naming what was absent.
    if (!posQ || !ctxQ) return {missing: {pos: !posQ, ctx: !ctxQ}};
    const r = {};
    for (const [key, target] of [['pos', posQ], ['ctx', ctxQ]]) {
      quizState = null;
      go('quiz', {unitId:'unit-ww504', classId:'english'});
      // force the round onto the question we want to look at
      quizState.order = [u.questions.indexOf(target)];
      quizState.i = 0; quizState.optFor = null; render();
      await new Promise(s => setTimeout(s, 60));
      const opts = [...document.querySelectorAll('#screen .opt')];
      r[key] = {
        n: opts.length,
        letters: opts.map(o => o.querySelector('.ltr').textContent),
        minTap: Math.min(...opts.map(o => Math.round(o.getBoundingClientRect().height))),
        firstOptionTop: Math.round(opts[0].getBoundingClientRect().top),
      };
      if (key === 'pos') {
        const right = opts[[...opts].findIndex(o =>
          o.querySelector('span:not(.ltr)').textContent === target.opts[target.ans])];
        right.click(); await new Promise(s => setTimeout(s, 60));
        r.pos.marked = document.querySelectorAll('#screen .opt.right').length;
        r.pos.qstat = !!DATA.records['qstat_unit-ww504_' + target.id];
      }
    }
    return r;
  });
  ck('the lesson has both shapes to render at all', !live.missing, live.missing);
  ck('a parts-of-speech question renders A/B/C at 44px+ and credits',
     !live.missing && live.pos.n === 3 && live.pos.letters.join('') === 'ABC' &&
     live.pos.minTap >= 44 && live.pos.marked === 1 && live.pos.qstat, live.pos);
  ck('a context question keeps its first option on screen (the 844px fold)',
     !live.missing && live.ctx.firstOptionTop < 844, live.ctx);

  // --- a full round still plays on each rebuilt lesson --------------------
  for (const id of REBUILT) {
    const play = await p.evaluate(async (uid) => {
      quizState = null; go('quiz', {unitId: uid, classId: 'english'});
      let guard = 0;
      while (view === 'quiz' && guard++ < 90) {
        /* A kind:'spell' question renders a bare unclassed <input> and a
           "Check my spelling" button that refuses an empty box — so the
           round stalls forever unless the box is filled first. Lesson 3
           still carries five of them. */
        const sp = document.querySelector('#screen input[type=text]');
        if (sp && !(quizState && quizState.spellVal)) {
          sp.value = 'zzz'; sp.dispatchEvent(new Event('input', {bubbles:true}));
        }
        const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
        if (opts.length) for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,4)); }
        await new Promise(r=>setTimeout(r,8));
        const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
        if (next) { next.click(); await new Promise(r=>setTimeout(r,8)); continue; }
        if (!opts.length) break;
      }
      const l = all('log').find(x => x.unitId === uid && x.mode === 'quiz');
      return {logged: !!l, total: l && l.total};
    }, id);
    ck(id + ': a full round plays and logs', play.logged && play.total > 0, play);
  }

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + JSON.stringify(r.got).slice(0,320))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,6) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
