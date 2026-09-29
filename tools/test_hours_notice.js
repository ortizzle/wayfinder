/* Student hours need 24 hours' notice (v177).

   The 4th Grade Newsletter says it on 9/18 and again on 9/25, so it is a
   standing rule and not a one-off: "A 24 hours notice is needed for students
   to attend student hours." Three places in the app OFFER a window, and all
   three have to carry it — the runway most of all, because "the last one
   before it" is a promise the door cannot keep if she has to ask first.

   Two rules are pinned here, and the second is the one worth guarding:

     1. every surface that names a window also names the notice, and
     2. the notice never FILTERS a window away.

   The app cannot know whether she already asked her teacher, so hiding a real
   window from someone who did would be worse than printing the rule twice.

   Nothing here hardcodes a date. The Extra-help card only renders on a school
   day whose weekday carries a window, so the test WALKS FORWARD to the first
   such day and points the clock at it — pin the rule, never the almanac, which
   this file's neighbours have each had to learn separately. */
const { chromium } = require('playwright');
const port = process.argv[2] || 8403;

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto(`http://localhost:${port}/index.html`, {waitUntil:'networkidle'});

  const out = [];
  const ck = (n, c, d) => { out.push((c ? 'ok   ' : 'FAIL ') + n);
    if (!c && d !== undefined) out.push('       ' + JSON.stringify(d).slice(0, 300)); };

  /* ---- the rule itself ---- */
  const konst = await p.evaluate(() => ({
    txt: typeof HOURS_NOTICE === 'string' ? HOURS_NOTICE : null,
    hours: typeof STUDENT_HOURS !== 'undefined' && STUDENT_HOURS.length
  }));
  ck('the notice names 24 hours and says to ask a day ahead',
     !!konst.txt && /24 hours/.test(konst.txt) && /day ahead/i.test(konst.txt), konst);
  ck('student hours still exist to be offered', konst.hours, konst);

  /* ---- 1. Today's "Extra help today" card ---- */
  const card = await p.evaluate(() => {
    const realT = AZ.today, realN = AZ.nowMinutes;
    const from = AZ.today();
    let day = null, ids = null;
    for (let i = 0; i < 21; i++) {
      const ds = AZ.shift(from, i), wd = AZ.weekday(ds);
      const h = STUDENT_HOURS.find(x => x.d === wd);
      const closed = (CAL.closed || []).some(([a, z]) => ds >= a && ds <= z);
      if (h && !closed && wd >= 1 && wd <= 5 && ds >= CAL.firstDay && ds <= CAL.lastDay
          && ds >= HOURS_START) { day = ds; ids = h.ids; break; }
    }
    if (!day) return {err: 'no student-hours school day inside three weeks'};
    AZ.today = () => day;
    AZ.nowMinutes = () => 6 * 60;      // early, so no slot is trimmed as passed
    try {
      go('today');
      const c = [...document.querySelectorAll('#screen .card')]
        .find(x => /Extra help today/.test(x.textContent));
      const hint = c && c.querySelector('.hintline');
      return {day, ids, rendered: !!c,
              window: !!(c && /Student hours/.test(c.textContent)),
              notice: !!(hint && hint.textContent.includes(HOURS_NOTICE)),
              help: !!(hint && /help, not trouble/.test(hint.textContent))};
    } finally { AZ.today = realT; AZ.nowMinutes = realN; }
  });
  ck("Today's Extra help card renders on a student-hours school day", card.rendered, card);
  ck('it still names the window — the notice is stated, never used to filter',
     card.window, card);
  ck('it carries the 24-hour notice', card.notice, card);
  ck('and the encouraging line it already had is still there, not replaced',
     card.help, card);

  /* ---- 2. the subject screen's hintline ---- */
  const subj = await p.evaluate((ids) => {
    const cid = (ids || ['math'])[0];
    go('unit', {classId: cid});
    const hint = [...document.querySelectorAll('#screen .hintline')]
      .find(h => /Student hours/.test(h.textContent));
    return {cid, found: !!hint,
            window: !!(hint && /\d{1,2}:\d{2}/.test(hint.textContent)),
            notice: !!(hint && hint.textContent.includes(HOURS_NOTICE))};
  }, card.ids);
  ck("the subject screen's student-hours hintline renders", subj.found, subj);
  ck('it still prints real times', subj.window, subj);
  ck('it carries the 24-hour notice', subj.notice, subj);

  /* ---- 3. the runway, which is the one that says "the last one before it" ----
     Seeded with an unscored test far enough out that a window genuinely falls
     between today and it, so the hours row has something to report. */
  const rw = await p.evaluate(() => {
    const cid = 'math';
    /* The offset is DERIVED, not chosen: the runway deliberately yields when
       its test falls inside the week the brief already covers, so an offset
       that works on a Monday can hide the whole card on a Friday. Walk out
       from a week ahead to the first day the brief does not cover, staying
       inside runway()'s own 14-day horizon. */
    const today = AZ.today();
    const wk = weekBrief(today);
    let date = null;
    for (let i = 8; i <= 14; i++) {
      const ds = AZ.shift(today, i);
      if (!(wk && wk.covers && wk.covers(ds))) { date = ds; break; }
    }
    if (!date) return {err: 'no uncovered date inside the runway horizon'};
    put({id: 'assess_hoursnotice', type: 'assess', classId: cid, kind: 'test',
         title: 'Seeded — hours notice', date, score: null});
    const r = runway(today);
    go('today');
    const line = document.querySelector('#screen .rhours');
    return {date, picked: r && r.cls && r.cls.id, hasHours: !!(r && r.hours),
            rendered: !!line,
            window: !!(line && /\d{1,2}:\d{2}/.test(line.textContent)),
            last: !!(line && /(the last one before it|the last chance)/.test(line.textContent)),
            notice: !!(line && line.textContent.includes(HOURS_NOTICE)),
            txt: line && line.textContent};
  });
  ck('the runway picks up the seeded test and finds a window before it',
     rw.picked === 'math' && rw.hasHours, rw);
  ck('the runway prints its student-hours row', rw.rendered, rw);
  ck('it still names real times — not filtered away by the notice', rw.window, rw);
  ck('it still says this is the last window before the test', rw.last, rw);
  ck('and it carries the 24-hour notice, which is what makes "the last one" honest',
     rw.notice, rw);

  /* ---- the six dates the same newsletter announced ----
     Titles and dates are deliberately NOT named: this asserts the shape every
     row must have, so next week's additions are guarded too. */
  const sug = await p.evaluate(async () => {
    const today = AZ.today();
    /* Read the SHIPPED library, not DATA.records: a clean test install has no
       units at all, so checking the store would report every subject as
       empty and the note would say nothing true. */
    const shipped = new Set();
    for (const path of CONTENT_LIBRARY) {
      try { const j = await (await fetch(path, {cache:'no-store'})).json();
            Object.values(j.records || {}).forEach(r => { if (r && r.type === 'unit') shipped.add(r.classId); }); }
      catch (e) {}
    }
    const ahead = SUGGESTED_ASSESS.filter(s => s.date >= today);
    return {
      ahead: ahead.length,
      badClass: SUGGESTED_ASSESS.filter(s => !CLASS_BY_ID[s.classId]).map(s => s.classId),
      dupIds: SUGGESTED_ASSESS.length !== new Set(SUGGESTED_ASSESS.map(s => s.id)).size,
      badKind: SUGGESTED_ASSESS.filter(s => s.kind !== 'quiz' && s.kind !== 'test').map(s => s.id),
      badDate: SUGGESTED_ASSESS.filter(s => !/^\d{4}-\d{2}-\d{2}$/.test(s.date)).map(s => s.id),
      /* Every subject she is actually assessed in should be reachable — a row
         pointing at a subject with no study material is a real gap, and the
         one that turned up building this (Writing has no unit at all) is
         reported rather than asserted away. */
      noContent: [...new Set(ahead.map(s => s.classId))]
        .filter(cid => !shipped.has(cid))
    };
  });
  ck('every suggestion points at a real subject', sug.badClass.length === 0, sug.badClass);
  ck('no duplicate suggestion ids', !sug.dupIds, sug);
  ck('every suggestion is a quiz or a test', sug.badKind.length === 0, sug.badKind);
  ck('every suggestion carries an ISO date', sug.badDate.length === 0, sug.badDate);
  ck('there is something still ahead to plan around', sug.ahead > 0, sug);

  console.log(out.join('\n'));
  console.log('hours day used: ' + card.day + ' · subjects ' + JSON.stringify(card.ids));
  console.log('runway line: ' + (rw.txt || '(none)'));
  console.log('suggestions still ahead: ' + sug.ahead);
  if (sug.noContent.length)
    console.log('NOTE — upcoming assessments in subjects with no unit yet: '
                + sug.noContent.join(', '));
  const bad = out.some(l => l.startsWith('FAIL'));
  console.log(bad ? 'SOME FAILED' : 'ALL PASS', '| page errors:', errs.length ? errs : 'none');
  await b.close();
  if (bad || errs.length) process.exit(1);
})();
