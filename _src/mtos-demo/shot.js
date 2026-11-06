const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();
const html='<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>'+fs.readFileSync('mtos-demo.html','utf8')+'</body></html>';
fs.writeFileSync('preview.html',html);
const p=await b.newPage({viewport:{width:1440,height:960}});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await p.goto('file://'+process.cwd()+'/preview.html');await p.waitForTimeout(1500);
await p.screenshot({path:'d1.png'});
await p.evaluate(()=>document.getElementById('scroll').scrollTop=700);await p.waitForTimeout(900);await p.screenshot({path:'d2.png'});
await p.evaluate(()=>document.getElementById('scroll').scrollTop=0);
for(const i of [0,2,3,4]){await p.click(`.panel .time-btn[data-i="${i}"]`);await p.waitForTimeout(1200);await p.screenshot({path:`t${i}.png`,clip:{x:300,y:100,width:520,height:560}});}
const m=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:1});await m.goto('file://'+process.cwd()+'/preview.html');await m.waitForTimeout(1200);await m.screenshot({path:'m1.png'});
console.log('errors',JSON.stringify(errs));await b.close();})();
