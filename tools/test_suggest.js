/* SUGGESTED_ASSESS, end to end — the one-tap adds from a newsletter or a
   teacher update reach the parent view, accept into real assess records, and
   drop out of the suggestion card once taken.

   This exists because tools/test_newsletter.js has been stale since the brief
   rework removed the .runway class it queries: it crashes before its first
   assertion, so this path had no working coverage at all. Written for the
   9/9 math update's two dates; the structural checks (no duplicate ids, every
   suggestion pointing at a real subject) guard every future addition too. */
const { chromium } = require('playwright');
const port = process.argv[2] || 8302;
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage();
  const errs = []; pg.on('pageerror', e => errs.push(e.message));
  await pg.goto(`http://localhost:${port}/index.html`, {waitUntil:'networkidle'});

  const live = await pg.evaluate(() => {
    const today = AZ.today();
    return {
      today,
      shown: SUGGESTED_ASSESS.filter(s => s.date >= today).map(s => s.title + ' · ' + s.date),
      dupIds: SUGGESTED_ASSESS.length !== new Set(SUGGESTED_ASSESS.map(s=>s.id)).size,
      badClass: SUGGESTED_ASSESS.filter(s => !CLASS_BY_ID[s.classId]).map(s=>s.classId)
    };
  });

  // open the parent view for real and find the rows
  const parent = await pg.evaluate(() => {
    go('parent');
    const txt = document.getElementById('screen').textContent;
    return {
      q18: txt.includes('Unit 2, lessons 2-1 to 2-3'),
      t24: txt.includes('Math test · Unit 2'),
      /* Date-dependent assertions expire. This one asks the RULE instead:
         SUGGESTED_ASSESS filters on sg.date >= today, so anything already
         past must not be offered. (The first cut of this test pinned the
         9/10 math test as "still listed" and broke overnight on 9/11.) */
      past: SUGGESTED_ASSESS.filter(s => s.date < AZ.today())
              .some(s => txt.includes(s.title))
    };
  });

  // accept the 9/18 quiz through the real button in the newsletter card
  const accepted = await pg.evaluate(() => {
    const row = [...document.querySelectorAll('.row')]
      .find(r => /lessons 2-1 to 2-3/.test(r.textContent));
    const btn = row && [...row.querySelectorAll('button')]
      .find(b => b.textContent.trim() === 'Add');
    if (!btn) return {err:'no Add button found on the row'};
    btn.click();
    const r = DATA.records['assess_sg-math-2026-09-18'];
    return r ? {date:r.date, classId:r.classId, kind:r.kind, score:r.score, title:r.title} : {err:'no record written'};
  });

  // once accepted it must leave the suggestion list rather than sit there twice
  const gone = await pg.evaluate(() => {
    const txt = document.getElementById('screen').textContent;
    const card = [...document.querySelectorAll('.card')]
      .find(c => /From the newsletter/.test(c.textContent));
    return { stillSuggested: !!(card && /lessons 2-1 to 2-3/.test(card.textContent)),
             nowListed: /lessons 2-1 to 2-3/.test(txt) };
  });

  // and it should now drive the runway / study plan like a real test
  const plan = await pg.evaluate(() => {
    const p = studyPlan(AZ.today());
    const m = p.find(x => x.classId === 'math');
    return m ? m.why || (m.reasons||[]).join('; ') : 'no math entry';
  });

  const out = []; const T=(n,c)=>out.push((c?'ok   ':'FAIL ')+n);
  T('both new dates are still ahead and shown', live.shown.some(s=>/2-1 to 2-3/.test(s)) && live.shown.some(s=>/Unit 2 · 2026-09-24/.test(s)));
  T('no duplicate suggestion ids', !live.dupIds);
  T('every suggestion points at a real subject', live.badClass.length === 0);
  T('the 9/18 quiz renders in the parent view', parent.q18);
  T('the 9/24 test renders in the parent view', parent.t24);
  T('a suggestion whose date has passed is no longer offered', !parent.past);
  T('accepting writes a real assess record, unscored', accepted && !accepted.err
      && accepted.date==='2026-09-18' && accepted.classId==='math'
      && accepted.kind==='quiz' && accepted.score==null);
  T('an accepted one leaves the suggestion card but stays on the screen',
      !gone.stillSuggested && gone.nowListed);
  T('an accepted test drives the study plan', /quiz|test|day/i.test(plan));
  console.log(out.join('\n'));
  console.log('shown from ' + live.today + ':\n  ' + live.shown.join('\n  '));
  console.log('math plan reason: ' + plan);
  if(accepted && accepted.err) console.log('accept error: ' + accepted.err);
  console.log(out.some(l=>l.startsWith('FAIL')) ? 'SOME FAILED' : 'ALL PASS', '| page errors:', errs.length?errs:'none');
  await b.close();
})();
