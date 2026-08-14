const { chromium } = require('playwright');
const PORT = process.argv[2] || 8099;
(async()=>{
  const b=await chromium.launch({executablePath:process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p=await b.newPage({viewport:{width:390,height:844}});
  const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto(`http://localhost:${PORT}/index.html`,{waitUntil:'networkidle'});
  console.log(JSON.stringify(await p.evaluate(async ()=>{
    const lib = (typeof CONTENT_LIBRARY!=='undefined') ? CONTENT_LIBRARY : [];
    for(const f of lib){
      const nm = typeof f==='string'?f:(f.file||f.name||f.id);
      try{
        const d=await (await fetch('./'+nm)).json();
        const rs=Array.isArray(d.records)?d.records:Object.values(d.records);
        rs.forEach(x=>{ DATA.records[x.id]=x; if(x.type==='unit') x.status='approved'; });
      }catch(e){}
    }
    const out={};
    Object.values(DATA.records).filter(u=>u.type==='unit'&&!u.deleted)
      .forEach(u=>{ out[u.classId]=1; });
    const res={};
    Object.keys(out).forEach(cid=>{
      shelvesFor(cid).shelves.forEach(s=>{ res[s.name]=s.units.map(u=>lessonLabel(u)); });
    });
    return res;
  }),null,1));
  console.log('errors:',errs.length?errs:'none');
  await b.close();
})();
