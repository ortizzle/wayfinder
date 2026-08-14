// Wayfinder v57 math-shelf test: library ingest, shelving, one-sitting rounds.
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8123;

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('PAGEERROR: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push('CONSOLE: ' + m.text()); });

  await page.goto(`http://localhost:${PORT}/index.html`, { waitUntil: 'networkidle' });

  const out = await page.evaluate(async () => {
    const r = {};
    // 1. Ingest the content library (no button — call the fetch loop's core directly).
    await fetchLibrary({ textContent: '', disabled: false });
    const units = Object.values(DATA.records).filter(x => x.type === 'unit' && !x.deleted);
    const math = units.filter(u => u.classId === 'math');
    r.mathUnits = math.map(u => `${u.id}|${u.title}|q${u.questions.length}|round${u.round || 'def'}|${u.status || 'live'}`).sort();

    // 2. Approve all math drafts (simulating the grown-up pass).
    math.forEach(u => { if (u.status === 'draft') { u.status = 'approved'; u.updatedAt = Date.now(); } });

    // 3. Shelves for math: expect Topic 1 (6 units incl. review) and Topic 2 (8).
    const sh = shelvesFor('math');
    r.shelves = sh.shelves.map(s => s.name + ': ' + s.units.map(u => u.title.split(' · ')[1]).join(' / '));
    r.loose = sh.loose.map(u => u.title);

    // 4. Round sizes: lesson serves all 10; review serves 12 of 24; a non-round unit uses default.
    const m21 = unitFor ? unitFor('unit-m21') : DATA.records['unit-m21'];
    const m2r = DATA.records['unit-m2r'];
    const m11 = DATA.records['unit-m11'];
    r.roundM21 = pickRound(m21).length;          // expect 10
    r.roundM2r = pickRound(m2r).length;          // expect 12
    r.roundM11 = pickRound(m11).length;          // expect 13 (retitled, round = all)
    const ww = units.find(u => /Wordly/.test(u.title || ''));
    r.roundDefault = ww ? pickRound(ww).length : 'n/a';  // expect 5 (QUIZ_ROUND)

    // 5. Pill wording check (mirrors the unitCard template).
    const pill = u => `${u.questions.length} questions · ${(u.round || QUIZ_ROUND) >= u.questions.length ? 'one sitting' : 'rounds of ' + Math.min(u.round || QUIZ_ROUND, u.questions.length)}`;
    r.pillM21 = pill(m21);
    r.pillM2r = pill(m2r);
    r.pillM11 = pill(m11);

    // 6. Retitle kept the id: qstat progress attaches to unit-m11.
    r.m11Title = m11.title;
    r.m11Round = m11.round;
    return r;
  });

  console.log(JSON.stringify(out, null, 1));
  console.log('errors:', errors.length ? errors : 'none');
  await browser.close();
  process.exit(errors.length ? 1 : 0);
})();
