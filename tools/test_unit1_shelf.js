/* The math shelf is ONE book called Unit 1, holding all three topics —
   Chris, 2026-09-11: "update River's Math to be Unit 1 include the 3 topics."

   Each lesson keeps its real printed topic number in its TITLE and the shelf
   comes from an explicit `series` field, which seriesOf() honours ahead of the
   title convention. That is what keeps the sort running topic by topic with
   each Topic Review directly after its own topic's lessons — flattening the
   topic out of the titles would have bunched all three reviews at the end.
   Pins the ids too: this was a re-shelve, never a re-mint. */
const { chromium } = require('playwright');
const port = process.argv[2] || 8302;
const fs = require('fs'), glob = require('path');
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage();
  const errs = []; pg.on('pageerror', e => errs.push(e.message));
  await pg.goto(`http://localhost:${port}/index.html`, {waitUntil:'networkidle'});

  // load every math file the way the app does, then approve so the shelf is live
  const files = fs.readdirSync('content').filter(f=>f.startsWith('math')).map(f=>'content/'+f);
  const data = files.map(f => JSON.parse(fs.readFileSync(f,'utf8')));

  const res = await pg.evaluate(datas => {
    datas.forEach(d => {
      const recs = d.records; const rl = Array.isArray(recs) ? recs : Object.values(recs);
      rl.forEach(r => { if(r && r.type==='unit'){ r.status='approved'; DATA.records[r.id]=r; } });
    });
    saveLocal();
    const sh = shelvesFor('math');
    return {
      shelfNames: sh.shelves.map(s=>s.name),
      loose: sh.loose.map(u=>u.title),
      parts: sh.shelves[0] ? sh.shelves[0].lessons.map(u=>lessonLabel(u)) : [],
      titles: sh.shelves[0] ? sh.shelves[0].lessons.map(u=>u.title) : [],
      ids: sh.shelves[0] ? sh.shelves[0].lessons.map(u=>u.id) : []
    };
  }, data);

  const out=[]; const T=(n,c)=>out.push((c?'ok   ':'FAIL ')+n);
  T('math has exactly one shelf, named Unit 1',
    res.shelfNames.length===1 && res.shelfNames[0]==='Unit 1');
  T('nothing left loose outside it', res.loose.length===0);
  T('all 24 parts are on it', res.parts.length===24);
  T('every part label is distinct', new Set(res.parts).size===res.parts.length);
  // topic order: each topic's lessons, then that topic's review, in topic order
  const want = ['1-1','1-2','1-3','1-4','1-5','Topic 1 Review',
                '2-1','2-2','2-3','2-4','2-5','2-6','2-7','Topic 2 Review',
                '3-1','3-2','3-3','3-4','3-5','3-6','3-7',
                'Decimals Extra Practice','Decimals on the Number Line','Topic 3 Review'];
  const got = res.parts.map(p => /^\d-\d/.test(p) ? p.slice(0,3) : p);
  T('lessons run topic 1 → 2 → 3, each review after its own topic',
    JSON.stringify(got)===JSON.stringify(want));
  T('every id is preserved (no re-mint)',
    res.ids.length===24 && res.ids.every(i=>/^unit-m/.test(i)));
  T('the lesson titles still carry their real topic number',
    res.titles.filter(t=>/^Topic [123] · /.test(t)).length===24);

  console.log(out.join('\n'));
  console.log('\nUnit 1 (' + res.parts.length + ' parts):');
  res.parts.forEach((p,i)=>console.log('  '+String(i+1).padStart(2)+'. '+p));
  console.log(out.some(l=>l.startsWith('FAIL'))?'SOME FAILED':'ALL PASS','| page errors:', errs.length?errs:'none');
  await b.close();
})();
