/* Every accent × every sky × both themes. River repaints the canvas, so the
   old measurements do not carry — this re-takes all of them. */
const { chromium } = require('playwright');
const PORT = process.argv[2] || 8099;
const parse=c=>{let m=c.match(/color\(srgb\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)(?:\s*\/\s*([\d.]+))?\)/);
 if(m)return[+m[1]*255,+m[2]*255,+m[3]*255,m[4]==null?1:+m[4]];
 m=c.match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/);
 if(m)return[+m[1],+m[2],+m[3],m[4]==null?1:+m[4]]; throw new Error('bad "'+c+'"');};
const over=(f,b)=>f.slice(0,3).map((v,i)=>v*f[3]+b[i]*(1-f[3])).concat([1]);
const lum=c=>{const f=c.slice(0,3).map(v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});
 return .2126*f[0]+.7152*f[1]+.0722*f[2]};
const ratio=(a,b)=>{const[x,y]=[lum(a),lum(b)].sort((m,n)=>n-m);return (x+.05)/(y+.05)};
(async()=>{
  const b=await chromium.launch({executablePath:process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium'});
  const p=await b.newPage({viewport:{width:390,height:844}});
  await p.goto(`http://localhost:${PORT}/index.html`,{waitUntil:'networkidle'});
  await p.addScriptTag({path:__dirname+'/seed.js'}); await p.waitForTimeout(400);
  const accents=await p.evaluate(()=>ACCENTS.map(a=>a.id));
  const skies=await p.evaluate(()=>SKIES.filter(s=>s.id!=='seasonal').map(s=>s.id));
  const rows=[];
  for(const theme of ['light','dark']) for(const sky of skies) for(const acc of accents){
    const g=await p.evaluate(({theme,sky,acc})=>{
      const hex=ACCENTS.find(x=>x.id===acc).c;
      const R=document.documentElement;
      R.style.setProperty('--ac',hex); R.dataset.theme=theme; R.dataset.sky=sky;
      if(getComputedStyle(R).getPropertyValue('--ac').trim()!==hex) throw new Error('accent stuck');
      if(R.dataset.sky!==sky||R.dataset.theme!==theme) throw new Error('state stuck');
      go('day',{date:AZ.today(),dayView:'order',openSes:'ses2'});
      const sc=document.getElementById('screen'), cs=n=>getComputedStyle(n);
      const card=sc.querySelector('.card'), felt=sc.querySelector('.felt');
      const S=[['body text',sc.querySelector('.sesrow .nm'),card],
               ['muted',sc.querySelector('.sesrow .mt'),card],
               ['faint',sc.querySelector('.sesrow .score i'),card],
               ['accent text',sc.querySelector('.eyebrow'),card],
               ['felt hint',felt&&felt.querySelector('.hintline'),felt],
               ['felt value',felt&&felt.querySelector('.v'),felt]].filter(x=>x[1]);
      return { pageBg:cs(document.body).backgroundColor, cardBg:cs(card).backgroundColor,
        feltBg:felt?cs(felt).backgroundColor:null,
        s:S.map(([nm,n,host])=>[nm,cs(n).color,host===felt?'felt':'card']) };
    },{theme,sky,acc});
    const page=parse(g.pageBg), card=over(parse(g.cardBg),page);
    const felt=g.feltBg?over(parse(g.feltBg),card):card;
    g.s.forEach(([nm,col,host])=>{ const bg=host==='felt'?felt:card;
      rows.push({theme,sky,acc,el:nm,r:+ratio(over(parse(col),bg),bg).toFixed(2)}); });
  }
  const bad=rows.filter(r=>r.r<4.5);
  const bySky={}; rows.forEach(r=>{bySky[r.sky]=Math.min(bySky[r.sky]??99,r.r)});
  console.log('samples:',rows.length,'| distinct:',new Set(rows.map(r=>r.r)).size);
  console.log('worst per sky:',JSON.stringify(bySky,null,1));
  console.log('BELOW 4.5:1 →', bad.length?JSON.stringify(bad.slice(0,10),null,1):'none');
  await b.close(); process.exit(bad.length?1:0);
})();
