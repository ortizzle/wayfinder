/* River's two new prep units (Decimals Extra Practice on the Topic 3 shelf,
   Reading Scales Practice on the Science shelf) + the gold prep treatment. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8117;
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});

  const out = [];
  const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const seed = await p.evaluate(async () => {
    const files = ['math-t3-31','math-t3-32','math-t3-33','math-t3-34','math-t3-35','math-t3-36','math-t3-37','math-t3-review','math-t3-extra',
      'science-quiz-1','science-measurement','science-variables','science-scales'];
    for (const f of files) {
      const res = await fetch(`./content/${f}.json`, {cache:'no-store'});
      const j = await res.json();
      const u = Object.values(j.records)[0];
      u.status = 'approved'; u.updatedAt = Date.now() - 1000;
      DATA.records[u.id] = u;
    }
    saveLocal();
    return {mx: !!DATA.records['unit-m3x'], sc: !!DATA.records['unit-sci-scales']};
  });
  ck('both units seeded', seed.mx && seed.sc, seed);

  // Topic 3 shelf: extra practice lands between 3-7 and Topic Review, gold-ringed.
  const t3 = await p.evaluate(() => {
    go('shelf', {classId:'math', series:'Topic 3', open:'unit-m3x'});
    const titles = [...document.querySelectorAll('#screen .stop .t')].map(x=>x.textContent);
    const prep = [...document.querySelectorAll('#screen .stop.prep .t')].map(x=>x.textContent);
    const oc = document.getElementById('shelfopen');
    return {
      titles,
      extraIdx: titles.findIndex(t=>/Extra Practice/.test(t)),
      reviewIdx: titles.findIndex(t=>/Topic Review/.test(t)),
      l37Idx: titles.findIndex(t=>/3-7/.test(t)),
      prep,
      band: oc && oc.querySelector('.prepband') ? oc.querySelector('.prepband').textContent : null
    };
  });
  ck('extra practice sorts after 3-7 and before Topic Review',
     t3.l37Idx < t3.extraIdx && t3.extraIdx < t3.reviewIdx, t3);
  ck('it is the only gold prep stop on the Topic 3 map', t3.prep.length===1 && /Extra Practice/.test(t3.prep[0]), t3.prep);
  ck('its opened card wears the Test prep band', /Test prep/i.test(t3.band||''), t3.band);

  // Science shelf: scales practice sits last (order:3) and gold-ringed.
  const sci = await p.evaluate(() => {
    go('shelf', {classId:'science', series:'Science', open:'unit-sci-scales'});
    const titles = [...document.querySelectorAll('#screen .stop .t')].map(x=>x.textContent);
    const prep = [...document.querySelectorAll('#screen .stop.prep .t')].map(x=>x.textContent);
    return {titles, last: titles[titles.length-1], prep};
  });
  ck('scales practice sits last on the Science shelf', /Reading Scales/.test(sci.last||''), sci);
  ck('and is a gold prep stop', sci.prep.length===1 && /Reading Scales/.test(sci.prep[0]), sci.prep);

  // Full quiz rounds on both.
  const quiz = await p.evaluate(async () => {
    const run = async (id, cid) => {
      quizState = null;
      go('quiz', {unitId:id, classId:cid});
      let guard = 0;
      while (view === 'quiz' && guard++ < 25) {
        const opts = [...document.querySelectorAll('#screen .opt:not([disabled])')];
        if (opts.length) for (const o of opts) { o.click(); await new Promise(r=>setTimeout(r,4)); }
        await new Promise(r => setTimeout(r, 8));
        const next = document.querySelector('#screen .btn-primary, #screen .explain.go-on');
        if (next) { next.click(); await new Promise(r=>setTimeout(r,8)); continue; }
        if (!opts.length) break;
      }
      return all('log').some(l => l.unitId === id);
    };
    return { mx: await run('unit-m3x','math'), sc: await run('unit-sci-scales','science') };
  });
  ck('a full round on the decimals unit completes and logs', quiz.mx, quiz);
  ck('a full round on the scales unit completes and logs', quiz.sc, quiz);

  out.forEach(r => console.log((r.ok ? ' ok ' : 'FAIL ') + r.n + (r.ok ? '' : ' -> ' + JSON.stringify(r.got).slice(0,300))));
  console.log(out.every(r=>r.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(r=>r.ok) || errs.length) process.exit(1);
})();
