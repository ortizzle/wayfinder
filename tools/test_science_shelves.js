/* v195 — River's Science shelves follow her Drive folders.
   Chris, 2026-10-26: "unit 1 should all be one unit, under 1 folder." Her
   Science folder is now Unit 1.1 Nature of Science, Unit 1.2 Phases of Matter,
   Unit 2 - Chemistry and Unit 3 - Atmosphere. So every Unit 1.1 and 1.2 part
   is ONE "Unit 1" shelf, 1.1 first, and the Chemistry test material is its own
   "Unit 2" shelf.

   Pins the rule rather than a count that will grow: the two shelves, nothing
   loose, the 1.1 run before the 1.2 run, the authored order inside each, every
   id kept (a retitle, never a re-mint, so her progress stays attached), libv
   past its old value and updatedAt in the past so the move wins the approval
   race. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8413;
const FILES = ['science-quiz-1','science-measurement','science-variables','science-scales',
  'science-nos-practice','science-nos-test','science-phases-matter','science-phase-changes',
  'science-density-buoyancy','science-molecules-compounds','science-chem-practice','science-chem-test'];
const U1 = ['unit-sci-q1','unit-sci-meas','unit-sci-vars','unit-sci-scales','unit-sci-nos-practice',
  'unit-sci-nos-test','unit-sci-phases','unit-sci-phasechg','unit-sci-dens','unit-sci-molcomp'];
const U2 = ['unit-sci-chem-practice','unit-sci-chem-test'];
// libv before the move; each must now be past it.
const OLD_LIBV = {'unit-sci-q1':3,'unit-sci-meas':1,'unit-sci-vars':1,'unit-sci-scales':2,
  'unit-sci-nos-practice':1,'unit-sci-nos-test':1,'unit-sci-phases':3,'unit-sci-phasechg':2,
  'unit-sci-dens':1,'unit-sci-molcomp':1,'unit-sci-chem-practice':1,'unit-sci-chem-test':1};
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; p.on('pageerror', e => errs.push(String(e.message)));
  await p.goto(`http://localhost:${PORT}/index.html`, {waitUntil:'networkidle'});
  const out = []; const ck = (n, ok, got) => out.push({n, ok: !!ok, got});

  const r = await p.evaluate(async (FILES) => {
    const shipped = [];
    for (const f of FILES) {
      const k = await (await fetch('./content/' + f + '.json', {cache:'no-store'})).json();
      for (const x of Object.values(k.records)) {
        shipped.push({id:x.id, status:x.status, libv:x.libv, at:x.updatedAt, title:x.title, cls:x.classId});
        x.status = 'approved'; DATA.records[x.id] = x; } }
    saveLocal();
    const sh = shelvesFor('science');
    const get = n => sh.shelves.find(s => s.name === n) || {lessons:[]};
    go('unit', {classId:'science'});
    const spines = [...document.querySelectorAll('#screen .spine')].map(s => s.textContent);
    go('shelf', {classId:'science', series:'Unit 1'});
    const stops = [...document.querySelectorAll('#screen .stop .t')].map(x => x.textContent);
    return {
      inLib: FILES.every(f => CONTENT_LIBRARY.includes('content/' + f + '.json')),
      shipped, names: sh.shelves.map(s => s.name).sort(), loose: sh.loose.map(u => u.id),
      u1: get('Unit 1').lessons.map(u => u.id), u2: get('Unit 2').lessons.map(u => u.id),
      labels1: get('Unit 1').lessons.map(u => lessonLabel(u)),
      labels2: get('Unit 2').lessons.map(u => lessonLabel(u)),
      spines, stops, now: Date.now(),
    };
  }, FILES);

  ck('all twelve still in CONTENT_LIBRARY, science, shipped as drafts',
     r.inLib && r.shipped.length === 12 && r.shipped.every(s => s.status === 'draft' && s.cls === 'science'), r.shipped);
  ck('exactly two shelves, Unit 1 and Unit 2, nothing loose',
     r.names.join() === 'Unit 1,Unit 2' && r.loose.length === 0, [r.names, r.loose]);
  ck('Unit 1 holds the ten 1.1 and 1.2 parts in teaching order', JSON.stringify(r.u1) === JSON.stringify(U1), r.u1);
  ck('the six 1.1 parts come first, then the four 1.2 parts',
     r.labels1.slice(0,6).every(l => /^1\.1 /.test(l)) && r.labels1.slice(6).every(l => /^1\.2 /.test(l)), r.labels1);
  ck('inside 1.1, the Nature of Science tests trail the lessons; inside 1.2, Phases of Matter leads',
     /^1\.1 Quiz 1: /.test(r.labels1[0]) && /Practice Test$/.test(r.labels1[4]) && /Study Test$/.test(r.labels1[5]) &&
     r.labels1[6] === '1.2 Phases of Matter' && r.labels1[9] === '1.2 Molecules and Compounds', r.labels1);
  ck('Unit 2 holds the Chemistry practice test, then the study test', JSON.stringify(r.u2) === JSON.stringify(U2) &&
     /^Chemistry Practice/.test(r.labels2[0]) && /^Chemistry Study/.test(r.labels2[1]), r.labels2);
  ck('no title still carries the old Science · or Chemistry · shelf name',
     !r.shipped.some(s => /^(Science|Chemistry) · /.test(s.title)), r.shipped.map(s => s.title));
  ck('every libv moved past its old value and every updatedAt is in the past',
     r.shipped.every(s => s.libv > OLD_LIBV[s.id] && s.at < r.now - 3600e3), r.shipped.map(s => [s.id, s.libv]));
  ck('the subject screen shows two spines, and the Unit 1 shelf draws ten stops',
     r.spines.length === 2 && r.stops.length === 10, [r.spines, r.stops.length]);

  out.forEach(x => console.log((x.ok ? '  ok ' : 'FAIL ') + x.n + (x.ok ? '' : ' → ' + JSON.stringify(x.got).slice(0,400))));
  console.log(out.every(x => x.ok) ? 'ALL PASS' : 'FAILURES');
  console.log('page errors:', errs.length ? errs.slice(0,10) : 'none');
  await b.close();
  if (!out.every(x => x.ok) || errs.length) process.exit(1);
})();
