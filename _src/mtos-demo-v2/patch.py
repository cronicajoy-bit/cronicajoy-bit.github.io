import re, os
D = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(D, 'template.html')
s = open(P, encoding='utf-8').read()

def rep(old, new, cnt=1):
    global s
    n = s.count(old)
    assert n == cnt, (n, old[:80])
    s = s.replace(old, new)

def rep_between(start, end, new):
    global s
    a = s.index(start); b = s.index(end, a)
    s = s[:a] + new + s[b:]

# ---------- CSS ----------
CSS = r'''
/* ===== Ver.2 ===== */
.task-card,.fcheck,.ocard{background:#F2F3F5;box-shadow:inset 0 0 0 1.5px #E3E6EA}
.app.bleed .task-card{background:#fff}
.dbar-wrap{padding:2px 22px 4px}
.dbar{display:flex;align-items:center;gap:8px;width:100%;background:#F2F3F5;border-radius:12px;padding:11px 14px;text-align:left;color:#111}
.dbar svg{flex:none;display:block}
.dbar b{font-size:15px;font-weight:700;letter-spacing:-.02em;white-space:nowrap}
.dbar .dv{width:15px;height:15px;border-radius:50%;background:var(--navy);display:grid;place-items:center;flex:none}
.dbar .dl{margin-left:auto;font-size:12px;font-weight:600;color:var(--orange);white-space:nowrap}
.dbar-wrap[hidden]{display:none}
.tab{font-size:12px}
.tab svg{color:var(--navy);width:28px;height:28px}
.nums .r .av{display:block;font-size:12px;font-weight:500;color:rgba(17,17,17,.6);margin-top:3px;letter-spacing:0}
.nums .r .av b{font-size:12px;font-weight:700;color:rgba(17,17,17,.6)}
.rail{height:88px}
.rail .cap{top:66px;display:flex;align-items:center;gap:4px;font-size:12px}
.rail .capb{font-weight:700;color:var(--navy);pointer-events:auto;padding:4px 0;margin-top:-4px}
.rail .capb .cv{width:14px;height:14px;border-radius:50%;background:rgba(255,255,255,.65);display:grid;place-items:center;transition:rotate .2s}
.rail .capb[aria-expanded="true"] .cv{rotate:180deg}
.slots{background:#fff;border-radius:16px;padding:2px 14px;display:flex;flex-direction:column;cursor:default}
.slots[hidden]{display:none}
.slots .sr{display:flex;align-items:center;gap:12px;padding:12px 0}
.slots .sr+.sr{border-top:1px solid #ECEDEF}
.slots .tm{width:44px;flex:none}.slots .tm small{display:block;font-size:12px;color:#6B7280;font-weight:500}.slots .tm b{font-size:16px;font-weight:700}
.slots .if{flex:1;min-width:0}.slots .if b{display:block;font-size:14px;font-weight:600;letter-spacing:-.02em}.slots .if small{display:block;font-size:12px;color:#6B7280;margin-top:2px}
.slots .bd{flex:none;display:flex;align-items:center;gap:4px;font-size:11px;font-weight:700;padding:4px 8px;border-radius:999px;background:#F2F3F5;color:#6B7280}
.slots .bd.on{background:var(--lime);color:#111}.slots .bd.on i{width:6px;height:6px;border-radius:50%;background:var(--orange)}
.trk{display:flex;align-items:center;gap:8px;font-size:12px;font-weight:500;color:#4E5560;margin-top:-2px}
.trk .b{display:flex;align-items:center;gap:5px;background:#fff;border-radius:999px;padding:5px 10px;color:#111;font-weight:700}
.trk .b i{width:6px;height:6px;border-radius:50%;background:var(--orange);animation:blink 1.2s ease-in-out infinite}
@keyframes blink{50%{opacity:.25}}
/* orders v2 */
.irow .t .mm{display:inline-flex;align-items:center;gap:3px;margin-left:8px;color:#6B7280;font-size:12px;font-weight:500}
.irow .t .sp{display:flex;align-items:center}
.memo{margin:-4px 0 12px 68px;background:#F2F3F5;border-radius:10px;padding:8px 10px;font-size:12px}
.memo b{margin-right:6px}.memo .op{display:flex;gap:10px;margin-top:4px;color:#6B7280;font-size:11px}.memo .op u{text-underline-offset:2px}
.memo .op span{display:inline-flex;align-items:center;gap:4px}.memo .op span i{width:12px;height:12px;border-radius:3px;background:var(--navy)}
.olinks{display:flex;gap:14px;font-size:12px;color:#6B7280;font-weight:500}
.stchip.ok{color:var(--orange)}
.day{cursor:pointer}
.onums .r .av{display:block;font-size:12px;color:#6B7280;margin-top:2px}.onums .r .av b{font-size:12px;font-weight:700;color:#6B7280}
/* cart */
.cartv{position:absolute;inset:0;z-index:30;background:#fff;display:flex;flex-direction:column}
.cartv[hidden]{display:none}
.cartv .cs{flex:1;overflow-y:auto;scrollbar-width:none;padding-bottom:160px}.cartv .cs::-webkit-scrollbar{display:none}
.cartv .chd{display:flex;align-items:center;gap:4px;padding:14px 22px 14px 14px}
.cartv .chd h2{margin:0;font-size:20px;font-weight:700;letter-spacing:-.02em}
.cartv .chd .back{width:36px;height:36px;display:grid;place-items:center}
.cartv .site{margin-left:auto;display:flex;align-items:center;gap:4px;border:1px solid #DEE1E6;border-radius:999px;padding:6px 10px 6px 12px;font-size:13px;font-weight:600}
.cartv .anc{display:flex;gap:20px;padding:14px 22px 0;border-bottom:1px solid #E6E7EA;overflow-x:auto;scrollbar-width:none;position:sticky;top:0;background:#fff;z-index:2}
.cartv .anc::-webkit-scrollbar{display:none}
.cartv .anc button{flex:none;font-size:15px;font-weight:500;color:#737884;padding-bottom:10px;border-bottom:2.5px solid transparent}
.cartv .anc button.on{font-weight:700;color:#111;border-color:var(--navy)}
.cartv .band{height:12px;background:#F2F3F5}
.cartv .sh{padding:30px 22px 16px;display:flex;flex-direction:column;gap:8px}
.cartv .sh .tt{display:flex;align-items:center;gap:8px;font-size:18px;font-weight:700;letter-spacing:-.02em}
.cartv .sh .bg{font-size:11px;font-weight:600;color:#737884;border:1px dashed #D7DADF;border-radius:999px;padding:3px 8px}
.cartv .sh p{margin:0;font-size:13px;color:#737884;font-weight:500}.cartv .sh p.o{color:var(--orange)}
.cartv .all{display:flex;align-items:center;gap:8px;font-size:13px;font-weight:500;padding-top:4px}
.ck{width:22px;height:22px;border-radius:6px;border:1.5px solid #D9DCE1;background:#fff;flex:none;display:grid;place-items:center}
.ck.on{background:var(--navy);border-color:var(--navy)}
.cartv .cr{padding:0 22px}
.cartv .crow{display:flex;align-items:center;gap:12px;padding:16px 0}
.cartv .crow img{width:56px;height:56px;border-radius:12px;object-fit:cover;flex:none}
.cartv .crow .t{flex:1;min-width:0;display:flex;flex-direction:column;gap:6px}
.cartv .crow .t b{font-size:15px;font-weight:700;letter-spacing:-.02em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cartv .crow .t span{font-size:13px;color:#8E9196;display:flex;align-items:center}
.cartv .crow .t .mm{display:inline-flex;align-items:center;gap:3px;margin-left:8px;color:#6B7280;font-size:12px}
.cartv .crow .tg{display:flex;align-items:center;gap:6px;font-size:12px;color:#6B7280}
.cartv .crow .tg i{font-style:normal;background:#FFEDE6;color:var(--orange);font-weight:700;font-size:11px;padding:2px 6px;border-radius:4px}
.cartv .crow .q{flex:none;display:flex;flex-direction:column;align-items:flex-end;gap:6px}
.cartv .crow .q small{font-size:13px;font-weight:500;color:#5F6368}
.cartv .acts{display:flex;gap:8px;padding:0 0 18px 90px}
.cartv .acts button{font-size:12px;font-weight:700;padding:7px 12px;border-radius:999px;background:#F2F3F5}
.cartv .acts button.o{background:#fff;box-shadow:inset 0 0 0 1.2px var(--navy);color:var(--navy)}
.cartv .cr .memo{margin:-6px 0 18px 90px}
.cartv .ln{height:1px;background:#EEEFF1}
.cartv .cbar{position:absolute;left:0;right:0;bottom:0;background:#fff;box-shadow:0 -4px 12px rgba(0,0,0,.06);border-top:1px solid #E6E7EA;padding:14px 22px 30px;display:flex;flex-direction:column;gap:8px;z-index:3}
.cartv .cbar .r1{display:flex;align-items:center;justify-content:space-between;font-size:14px;font-weight:600}
.cartv .cbar .r1 b{font-size:18px;font-weight:700}
.cartv .cbar .r2{text-align:right;font-size:12px;color:#737884}
.cartv .cbar button.go{height:52px;border-radius:26px;background:var(--navy);color:#fff;font-size:17px;font-weight:700}
/* date sheet */
.dts{position:absolute;inset:0;z-index:60;display:flex;flex-direction:column;justify-content:flex-end;pointer-events:none}
.dts .dim{position:absolute;inset:0;background:rgba(0,0,0,.42);opacity:0;transition:opacity .25s}
.dts .pane{position:relative;background:#fff;border-radius:24px 24px 0 0;padding:10px 22px 34px;transform:translateY(100%);transition:transform .32s cubic-bezier(.2,.8,.2,1)}
.dts.on{pointer-events:auto}.dts.on .dim{opacity:1}.dts.on .pane{transform:none}
.dts .grab{width:40px;height:4px;border-radius:2px;background:#D9DCE0;margin:0 auto 16px}
.dts h3{margin:0;font-size:20px;font-weight:700}.dts .ws{margin:4px 0 14px;font-size:13px;color:#8E9196}
.dts .op{display:flex;align-items:center;gap:10px;width:100%;text-align:left;border-radius:16px;padding:14px 16px;border:1px solid #DEE1E6;margin-bottom:8px;background:#fff}
.dts .op.on{border:1.6px solid var(--navy);background:#F3FCDF}
.dts .op[disabled]{opacity:.45}
.dts .op .l{flex:1}.dts .op .l b{font-size:17px;font-weight:700;margin-right:6px}.dts .op .l em{font-style:normal;font-size:11px;font-weight:700;background:#D9F84A;padding:2px 6px;border-radius:6px}
.dts .op .l small{display:block;font-size:13px;color:#8E9196;margin-top:3px}.dts .op.on .l small{color:var(--orange)}
.dts .op .c{font-size:12px;font-weight:600;background:#F2F3F5;border-radius:999px;padding:4px 8px}
.dts .op .rd{width:22px;height:22px;border-radius:50%;border:1.5px solid #D9DCE1;flex:none}.dts .op.on .rd{border:6px solid var(--navy)}
.dts .cal{display:block;width:100%;text-align:center;font-size:14px;font-weight:600;color:var(--navy);padding-top:10px}
@media (max-width:760px){.dts,.cartv{position:fixed}}
.panel .vtag{display:inline-block;margin:0 0 14px;font-size:12px;font-weight:700;color:#111;background:#C2EF81;border-radius:6px;padding:3px 8px}
'''
rep('.slide .tag{background:#fff}\n</style>', '.slide .tag{background:#fff}\n' + CSS + '</style>')

# ---------- HTML ----------
rep('''                <span class="hicon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20.5 20.5-4.5-4.5"/></svg></span>\n''', '')
rep('<span class="hicon"><svg width="25" height="25"', '<span class="hicon" id="cartBtn" style="cursor:pointer"><svg width="25" height="25"')
rep('''            <div id="home"></div>''', '''            <div class="dbar-wrap" id="dbarW"></div>
            <div id="home"></div>''')
SEARCH_TAB = '''<button class="tab" data-tab="search"><svg width="26" height="26" viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><path d="M3.8 7.8h5.2M3.8 13.1h5.2M3.8 19.3h11"/><circle cx="16" cy="9.5" r="5"/><path d="m19.6 13.1 3.3 3.3"/></svg>검색</button>
              '''
rep('<button class="tab" data-tab="orders">', SEARCH_TAB + '<button class="tab" data-tab="orders">')
rep('stroke-width="1.5"><circle cx="12" cy="12" r="9.5"/>', 'stroke-width="1.7"><circle cx="12" cy="12" r="9.5"/>')
rep('<svg class="off" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"><path d="M5.5', '<svg class="off" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"><path d="M5.5')
rep('stroke-width="1.5"><circle cx="12" cy="8" r="4"/>', 'stroke-width="1.7"><circle cx="12" cy="8" r="4"/>')
rep_between('  <aside class="panel" aria-label="시연 패널">', '</aside>', '''  <aside class="panel" aria-label="시연 패널">
    <span class="vtag">Ver. 2</span>
    <h1>시간대별 히어로 영역 정보</h1>
    <div class="times" id="times"></div>
    <h1 class="sub">기타 화면</h1>
    <div class="times">
      <button class="ov-btn" id="ovOrders" aria-pressed="false"><span class="d"><b>주문내역 · 담는 중</b></span></button>
      <button class="ov-btn" id="ovReturn" aria-pressed="false"><span class="d"><b>주문내역 · 도착·반품</b></span></button>
      <button class="ov-btn" id="ovCart" aria-pressed="false"><span class="d"><b>장바구니</b></span></button>
      <button class="ov-btn" id="ovDate" aria-pressed="false"><span class="d"><b>입고요청일 바꾸기</b></span></button>
      <button class="ov-btn" id="ovWx" aria-pressed="false"><span class="d"><b>날씨 바텀시트</b></span></button>
    </div>
    <div class="alt" hidden><button class="alt-pill" id="ovBleed" aria-pressed="false">대안</button></div>
    <button class="deck-link" id="openDeckBtn"><span>디자인 컨셉 문서 보기</span><i>→</i></button>
    <div hidden><span id="sceneK"></span><span id="sceneV"></span></div>
  ''')

# ---------- JS data ----------
STATES = r'''const STATES=[
 {id:'0700',t:'07:00',name:'담기 시작',desc:'어제 주문분이 도착했어요',scene:'',
  count:'2건',cart:'5',label:'10/29(목) 입고 · 담는 중',head:'5품목 담았어요,<br>더 필요한 건 없으세요?',lk:'발주마감까지',lv:'10시간 20분',rk:'장바구니',rv:'96,800원',av:'1,240,000원',
  prog:56,marks:[{type:'pin',x:91,text:'발주마감'},{type:'tick',x:191}],cap:'오전·점심 2번 도착',cargo:'c07',cx:4,cy:-17,
  slots:[['오전','07:00','3품목 · 아워홈 탑차','출고 후 실시간 위치',1],['점심','11:00','2품목 · 협력사 배송','업체가 직접 배송해요',0]],
  btn1:'장바구니 보기',btn2:'품목 담기',dbar:['10/29(목)','오늘 17:20 발주마감'],ins:'부침가루 주문이 평소보다 늘고 있어요',
  now:[{icon:'box',t:'오늘 아침 17품목 도착',s:'입고검수 · 문제 품목은 클레임으로',warn:true,b:'입고검수'}],
  mini:{thumb:'start',html:'<em>17:20</em> 발주마감 · 내일 07:00 도착',bar:18}},
 {id:'1500',t:'15:00',name:'마감 임박',desc:'장바구니 18품목, 주문 전',scene:'',
  count:'3건',cart:'18',label:'10/29(목) 입고 · 담는 중',head:'장바구니 18품목,<br>주문을 마무리해 주세요',lk:'발주마감까지',lv:'1시간 58분',rk:'장바구니',rv:'312,400원',av:'1,240,000원',
  prog:84,marks:[{type:'pin',x:91,text:'발주마감'},{type:'tick',x:191}],cap:'오전·점심·저녁 3번 도착',cargo:'c15',cx:33,cy:-17,
  slots:[['오전','07:00','12품목 · 아워홈 탑차','출고 후 실시간 위치',1],['점심','11:00','4품목 · 아워홈 탑차','내일 08:30 출고',1],['저녁','17:00','2품목 · 협력사 배송','업체가 직접 배송해요',0]],
  btn1:'주문하기',btn2:'품목 담기',dbar:['10/29(목)','오늘 17:20 발주마감'],ins:'부침가루 주문이 평소보다 늘고 있어요',
  now:[{icon:'trend',t:'대파 10단, 평소의 2배예요',s:'과발주 · 10/29 입고분',b:'확인'},{icon:'clock',t:'떡 수정마감 임박',s:'10/29 입고분 · 16:30 수정마감',b:'주문 수정'}],
  mini:{thumb:'full',html:'발주마감까지 <span class="tp" id="cd">1:58:00</span> 남았어요',bar:84}},
 {id:'1900',t:'19:00',name:'출고 대기',desc:'발주마감, 포장 중',scene:'',
  count:'2건',cart:'2',label:'10/29(목) 입고 · 발주마감됨',head:'18품목 주문 완료,<br>내일 3번 나눠 도착해요',lk:'출고까지',lv:'3시간',rk:'주문 금액',rv:'312,400원',av:'927,600원',
  prog:132,marks:[{type:'passed',x:94},{type:'pin',x:188,text:'22:00 출고'}],cap:'오전·점심·저녁 3번 도착',cargo:'c19',cx:80,cy:-18,
  slots:[['오전','07:00','12품목 · 아워홈 탑차','22:00 출고 후 실시간 위치',1],['점심','11:00','4품목 · 아워홈 탑차','내일 08:30 출고',1],['저녁','17:00','2품목 · 협력사 배송','업체가 직접 배송해요',0]],
  btn1:'주문내역 보기',btn2:'주문 수정',dbar:['10/30(금)','10/29(목) 17:20 발주마감'],ins:'입고 때 비 소식, 냉장품 먼저 들여 주세요',
  now:[{date:['금요일','30'],t:'10/30 입고분 2품목 담는 중',s:'10/29(목) 17:20 발주마감',b:'이어 담기'}],
  mini:{thumb:'sealed',html:'주문 완료 · 내일 07:00 도착',bar:45}},
 {id:'0600',t:'06:00',name:'배송 중',desc:'트럭이 매장으로 오는 중',scene:'',
  count:'2건',cart:'5',label:'10/28(수) 입고 · 어제 주문한 17품목',head:'오늘 입고분이 오고 있어요,<br>07:00 도착 예정',lk:'도착까지',lv:'58분',rk:'실린 상품',rv:'17품목',
  prog:270,marks:[{type:'passed',x:94},{type:'passed',x:191}],cap:'07:00 도착',cargo:'c06',cx:206,cy:-1,
  trk:['아워홈 탑차 15품목 · 실시간','협력사 2품목은 도착 예정만'],
  btn1:'배송조회',btn2:'실린 상품 보기',dbar:['10/29(목)','오늘 17:20 발주마감'],ins:'부침가루 주문이 평소보다 늘고 있어요',
  now:[{date:['목요일','29'],t:'5품목 담는 중',s:'오늘 17:20 발주마감',b:'이어 담기'}],
  mini:{thumb:'truck',html:'17품목 배송 중 · 도착까지 <em>58분</em>',bar:92}},
 {id:'0705',t:'07:00',name:'도착',desc:'물건 도착, 검수할 차례',scene:'',
  count:'1건',cart:'5',label:'10/28(수) 입고 · 06:52 도착',head:'오늘 아침 물건이<br>도착했어요',lk:'도착',lv:'17품목',rk:'도착 시각',rv:'06:52',
  prog:293,marks:[{type:'passed',x:94},{type:'passed',x:191}],cap:'반품 접수 오늘 18:00까지',cargo:'cAR',cx:253,cy:-20,
  btn1:'입고검수',btn2:'반품·클레임',dbar:['10/29(목)','오늘 17:20 발주마감'],ins:'부침가루 주문이 평소보다 늘고 있어요',
  now:[{date:['목요일','29'],t:'5품목 담는 중',s:'오늘 17:20 발주마감',b:'이어 담기'}],
  mini:{thumb:'sealed',html:'17품목 도착 · <em>입고검수</em>해 주세요',bar:100}}
];
'''
rep_between('const STATES=[', 'const SOON=', STATES)
rep("{date:['월요일','2'],t:'단호박은 11/2로',s:'리드타임 때문에 10/31엔 못 받아요',l:'담기'}", "{date:['금요일','30'],t:'단호박은 10/30으로',s:'리드타임 때문에 10/29엔 못 받아요',l:'담기'}")
rep("l:'다시 담기'}];", "l:'다시 주문'}];")
rep("{bg:'#FFE8D4',tag:'정기주문',h:'매주 자동으로<br>담아 드려요',p:'요일만 정하면 끝',img:'bn5'}", "{bg:'#FFE8D4',tag:'금Day 기획전',h:'매주 금요일<br>새 기획전이 열려요',p:'이번 주 아워홈 신상 12종',img:'bn5'}")

# rail caption -> button when slots
rep('''${cargo({...s,cx:s.cx+(pw-s.prog)})}<span class="cap" style="--d:${dC}s">${s.cap}</span></div>`;''',
    '''${cargo({...s,cx:s.cx+(pw-s.prog)})}${s.slots?`<button class="cap capb" style="--d:${dC}s" aria-expanded="false">${s.cap}<i class="cv"><svg width="8" height="5" viewBox="0 0 8 5"><path d="M1 1l3 3 3-3" fill="none" stroke="#2E3A4F" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></i></button>`:`<span class="cap" style="--d:${dC}s">${s.cap}</span>`}</div>`;''')

# ---------- orders ----------
ORDERS = r'''const ORD_TOTAL=312400;
const MEMO_IC='<svg width="13" height="13" viewBox="0 0 15 15" fill="none" stroke="#6B7280" stroke-width="1.3" stroke-linejoin="round" stroke-linecap="round"><path d="M2 12v2h2l8-8-2-2Z"/><path d="m8.5 5 2 2"/></svg>';
const ORDERS=[
 {g:'일반주문',c:16,meta:'· 17:20 발주마감',mc:'var(--orange)',link:'다시 주문',items:[
  {img:'p1',n:'도톰한 사각어묵',u:'390g',p:5180,q:10},
  {img:'p2',n:'프레스트 미트볼',u:'300g',p:6980,q:4,st:'16:30까지 수정 가능',memo:'찌개용으로 두툼하게 썰어 주세요'},
  {img:'p4',n:'친환경 깐양파',u:'300g',p:3480,q:8},
  {img:'p6',n:'상하 프로틴 스트링 치즈',u:'200g(10입)',p:12582,q:3,st:'수정 마감 · 공급사 14:00',lock:1},
  {img:'p1',n:'사각어묵 슬라이스',u:'1kg',p:8900,q:3}],more:'일반주문 11품목 더보기'},
 {g:'세트주문',c:2,meta:'확정',mc:'#9AA0A6',items:[
  {img:'p3',n:'[해동] 손질 오징어 (대, 마리)',u:'',p:3180,q:6,lock:1},
  {img:'p3',n:'손질 쭈꾸미',u:'500g',p:7900,q:2,lock:1}]}];
const won=n=>n.toLocaleString('ko-KR')+'원';
const ordSum=()=>ORDERS.reduce((a,g)=>a+g.items.reduce((b,it)=>b+it.p*it.q,0),0);
const ORD_HIDDEN=ORD_TOTAL-ordSum();
function setTab(k){document.querySelectorAll('.tab').forEach(t=>t.toggleAttribute('aria-current',t.dataset.tab===k));document.querySelectorAll('.tab[aria-current]').forEach(t=>t.setAttribute('aria-current','page'));}
function press(id){document.querySelectorAll('.panel [aria-pressed]').forEach(b=>b.setAttribute('aria-pressed','false'));const b=id&&document.getElementById(id);if(b)b.setAttribute('aria-pressed','true');}
let ordMode='d29';
function showOrders(mode){
 mode=mode||'d29';ordMode=mode;closeCart();closeDts();
 setBleed(false);view='orders';setTab('orders');press(mode==='d28'?'ovReturn':'ovOrders');
 document.getElementById('dbarW').hidden=true;
 const sel=mode==='d28'?28:29;
 const days=[['수',28,1],['목',29,1],['금',30,1],['토',31,0],['일',1,0],['월',2,1],['화',3,0]];
 const del=mode==='d28';
 const el=document.getElementById('orders');
 const memoBox=(m,edit)=>`<div class="memo"><b>내 메모</b>${m}${edit?'<div class="op"><span><i></i>계속 사용</span><u>삭제</u></div>':''}</div>`;
 const head=del?`<div class="ocard"><div class="ohead"><span class="l"><b>10/28(수) 입고</b><span class="stchip">도착</span></span><small>06:52 도착</small></div>
   <div class="odiv"></div>
   <div class="onums"><div><small>반품 접수</small><div class="big">오늘 18:00까지</div></div><div class="r"><small>17품목 합계</small><b>298,200원</b></div></div>
   <div class="oacts"><button class="p">입고검수 →</button><button class="s">반품·클레임</button></div>
   <div class="olinks"><span>배송조회 ›</span><span>명세서 ›</span><span>다른 사업장으로 복사 ›</span></div></div>`
  :`<div class="ocard"><div class="ohead"><span class="l"><b>10/29(목) 입고요청</b><span class="stchip">미확정</span></span><small>내일 07:00 도착</small></div>
   <div class="odiv"></div>
   <div class="onums"><div><small>수정마감시간</small><div class="big">17:20까지</div></div><div class="r"><small>18품목 합계</small><b id="otot"></b><span class="av">주문가능 <b>1,240,000원</b></span></div></div>
   <div class="oacts"><button class="p">주문하기 →</button><button class="s">품목 담기</button></div></div>`;
 el.innerHTML=`<div class="ptitle"><h2>주문내역</h2><span class="olink">지난 주문 검색${chev('#4E5560')}</span></div>
  <div class="dates">${days.map(d=>`<div class="day${d[1]===sel?' on':''}" data-d="${d[1]}"><small>${d[0]}</small><b>${d[1]}</b><i class="${d[2]?'':'n'}"></i></div>`).join('')}</div>
  ${head}
  <div class="ilist">${ORDERS.map((g,gi)=>{const gc=del&&gi===0?g.c-1:g.c,meta=del?'· 확정':g.meta;return `<div class="ghead${gi?'':' first'}"><span class="l"><b>${g.g}</b><span class="c">${gc}</span><span class="meta" style="color:${del?'#9AA0A6':g.mc}">${g.link?meta:''}</span></span>${g.link?`<span class="olink" style="font-size:13px">${g.link}${chev('#4E5560')}</span>`:`<span class="meta" style="color:${g.mc}">${g.meta}</span>`}</div>
   ${g.items.map((it,ii)=>{const lock=del||it.lock;return `<div class="irow${it.lock&&!del?' lock':''}"><img src="${IMG[it.img]}" alt=""><div class="t"><b>${it.n}</b><span class="sp">${it.u?it.u+' · ':''}${won(it.p)}${!del&&!it.memo?`<i class="mm">${MEMO_IC}메모</i>`:''}</span>${it.st&&!del?`<em>${it.st}</em>`:''}</div>
    <div class="q">${lock?`<b>×${it.q}</b>`:`<div class="step"><button data-g="${gi}" data-i="${ii}" data-d="-1" aria-label="빼기">−</button><b id="q${gi}_${ii}">${it.q}</b><button data-g="${gi}" data-i="${ii}" data-d="1" aria-label="더하기">+</button></div>`}<small id="s${gi}_${ii}">${won(it.p*it.q)}</small></div></div>${it.memo?memoBox(it.memo,!del):''}`;}).join('')}
   ${g.more?`<div class="omore"><button>${del?'일반주문 10품목 더보기':g.more}${chev('#111')}</button></div>`:''}`;}).join('')}</div>
  <div class="spacer"></div>`;
 const upd=()=>{const t=document.getElementById('otot');if(t)t.textContent=won(ORD_HIDDEN+ordSum());};upd();
 el.querySelectorAll('.step button').forEach(b=>b.onclick=()=>{const it=ORDERS[+b.dataset.g].items[+b.dataset.i];it.q=Math.max(1,it.q+ +b.dataset.d);document.getElementById(`q${b.dataset.g}_${b.dataset.i}`).textContent=it.q;document.getElementById(`s${b.dataset.g}_${b.dataset.i}`).textContent=won(it.p*it.q);upd();});
 el.querySelectorAll('.day').forEach(d=>d.onclick=()=>{const n=+d.dataset.d;if(n===28)showOrders('d28');else if(n===29)showOrders('d29');});
 document.getElementById('home').hidden=true;el.hidden=false;
 const m=STATES[1].mini,mini=document.getElementById('mini');
 mini.innerHTML=`<span class="mth">${cargoMini(STATES[1])}</span><span class="mtx">${m.html}</span><span class="bar"><i style="width:${m.bar}%"></i></span>${chev('#111')}`;
 mini.classList.add('on');startCountdown();startCargo();
 document.getElementById('scroll').scrollTop=0;if(isM())window.scrollTo(0,0);
}

/* ---------- date bar & sheet ---------- */
const CAL='<svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#111" stroke-width="1.6" stroke-linecap="round"><rect x="2" y="3.5" width="14" height="12.5" rx="3"/><path d="M2 7.5h14M6 1.5v3M12 1.5v3"/></svg>';
const DV='<i class="dv"><svg width="7" height="5" viewBox="0 0 7 5"><path d="M1 1.2 3.5 3.7 6 1.2" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></i>';
let dSel=null;
function dbar(d){const w=document.getElementById('dbarW');dSel=d;w.hidden=false;w.innerHTML=`<button class="dbar" id="dbar">${CAL}<b>${d[0]} 입고요청</b>${DV}<span class="dl">${d[1]}</span></button>`;document.getElementById('dbar').onclick=openDts;}
const DOPTS=[['10/29(목)','오늘 17:20 마감','담는 중 5품목','가장 빠른 날'],['10/30(금)','10/29(목) 17:20 마감','담는 중 2품목',''],['11/2(월)','10/30(금) 17:20 마감','',''],['11/3(화)','11/2(월) 17:20 마감','','']];
function openDts(){let el=document.getElementById('dts');if(!el){el=document.createElement('div');el.id='dts';el.className='dts';el.innerHTML='<div class="dim"></div><div class="pane"></div>';document.querySelector('.app').appendChild(el);el.querySelector('.dim').onclick=closeDts;}
 const closed=view==='home'&&STATES[cur].id==='1900';
 el.querySelector('.pane').innerHTML=`<div class="grab"></div><h3>언제 받으실 건가요?</h3><p class="ws">날짜마다 발주마감 시간이 달라요</p>
  ${DOPTS.map((o,i)=>{const dis=closed&&i===0;const on=dSel&&o[0]===dSel[0];return `<button class="op${on?' on':''}" data-i="${i}" ${dis?'disabled':''}><span class="l"><b>${o[0]}</b>${o[3]&&!dis?`<em>${o[3]}</em>`:''}<small>${dis?'발주마감됨 · 배송 준비 중':o[1]}</small></span>${o[2]&&!dis?`<span class="c">${o[2]}</span>`:''}<span class="rd"></span></button>`;}).join('')}
  <button class="cal">더 먼 날짜는 달력에서 고르기 ›</button>`;
 el.querySelectorAll('.op').forEach(b=>b.onclick=()=>{const o=DOPTS[+b.dataset.i];const dl=o[1].replace('마감','발주마감');dbar([o[0],dl]);setTimeout(closeDts,180);el.querySelectorAll('.op').forEach(x=>x.classList.toggle('on',x===b));});
 el.offsetWidth;el.classList.add('on');}
function closeDts(){const el=document.getElementById('dts');if(el)el.classList.remove('on');}

/* ---------- cart ---------- */
const CART={
 closed:[{img:'p4',n:'친환경 깐양파',u:'300g',p:3480,q:8,alt:2},{img:'p1',n:'사각어묵 슬라이스',u:'1kg',p:8900,q:3,alt:1}],
 d29:[{img:'p1',n:'도톰한 사각어묵',u:'390g',p:5180,q:10,on:1},{img:'p2',n:'프레스트 미트볼',u:'300g',p:6980,q:4,on:1,memo:'신선한 걸로 부탁드려요'},{img:'p1',n:'사각어묵 슬라이스',u:'1kg',p:8900,q:3,on:1}],
 d30:[{img:'p4',n:'친환경 깐양파',u:'300g',p:3480,q:8},{img:'p1',n:'사각어묵 슬라이스',u:'1kg',p:8900,q:3}]};
const CK='<svg width="12" height="9" viewBox="0 0 12 9"><path d="M1 4.5 4.5 8 11 1" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
let cartFrom=null;
function cartRow(it,sec,i){
 const closed=sec==='closed';
 return `<div class="crow"><button class="ck${it.on?' on':''}" data-s="${sec}" data-i="${i}">${it.on?CK:''}</button><img src="${IMG[it.img]}" alt=""><div class="t"><b>${it.n}</b><span>${it.u} · ${won(it.p)}${!closed&&!it.memo?`<i class="mm">${MEMO_IC}메모</i>`:''}</span>${closed?'<span class="tg"><i>발주마감</i>다음 입고일 10/30(금)</span>':''}</div>
  <div class="q">${closed?'':`<div class="step"><button data-s="${sec}" data-i="${i}" data-d="-1">−</button><b>${it.q}</b><button data-s="${sec}" data-i="${i}" data-d="1">+</button></div>`}<small>${won(it.p*it.q)}</small></div></div>
  ${closed?`<div class="acts"><button class="o">10/30(금)으로 옮기기</button><button>대체상품 ${it.alt}개 ›</button></div>`:''}
  ${it.memo?`<div class="memo"><b>내 메모</b>${it.memo}<div class="op"><span><i></i>계속 사용</span><u>삭제</u></div></div>`:''}<div class="ln"></div>`;}
function cartHTML(){const sum=k=>CART[k].filter(x=>x.on).reduce((a,x)=>a+x.p*x.q,0),cnt=k=>CART[k].filter(x=>x.on).length,all=k=>CART[k].reduce((a,x)=>a+x.p*x.q,0);
 const sec=(id,title,badge,lines,k)=>`<div class="sec" id="cs_${id}"><div class="sh"><div class="tt">${title}${badge?`<span class="bg">${badge}</span>`:''}</div>${lines}<div class="all"><span class="ck${CART[k].every(x=>x.on)?' on':''}">${CART[k].every(x=>x.on)?CK:''}</span>${k==='closed'?'전체 선택 · 2품목':`전체 선택 · ${CART[k].length}품목 · ${won(all(k))}`}</div></div><div class="cr">${CART[k].map((it,i)=>cartRow(it,k,i)).join('')}</div></div>`;
 const tk=cnt('d30')&&!cnt('d29')?'d30':'d29';
 return `<div class="cs" id="cs"><div class="chd"><button class="back" id="cBack"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5 8 12l7 7"/></svg></button><h2>장바구니</h2><span class="site">아딸 강남점 <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg></span></div>
  <div class="anc" id="anc"><button data-t="closed" class="on">발주마감 2</button><button data-t="d29">10/29(목) 3</button><button data-t="d30">10/30(금) 2</button><button data-t="d2">11/2(월) 1</button></div>
  <div class="band"></div>
  ${sec('closed','발주마감된 상품 2','','<p>다른 입고요청일로 옮기거나 대체상품으로 바꿔 주문할 수 있어요.</p>','closed')}<div class="band"></div>
  ${sec('d29','10/29(목) 입고요청','미확정','<p class="o">발주마감까지 1시간 58분 · 오늘 17:20</p>','d29')}<div class="band"></div>
  ${sec('d30','10/30(금) 입고요청','미확정','<p>발주마감 10/29(목) 17:20</p>','d30')}</div>
  <div class="cbar"><div class="r1"><span>${tk==='d29'?'10/29':'10/30'} 입고요청 · 선택 ${cnt(tk)}품목</span><b>${won(sum(tk))}</b></div><div class="r2">주문가능 1,240,000원 · 14:20 기준</div><button class="go">주문하기</button></div>`;}
function bindCart(){const v=document.getElementById('cartv');
 v.querySelector('#cBack').onclick=closeCart;
 v.querySelectorAll('.crow .ck').forEach(b=>b.onclick=()=>{const it=CART[b.dataset.s][+b.dataset.i];if(b.dataset.s==='closed')return;const other=b.dataset.s==='d29'?'d30':'d29';if(!it.on)CART[other].forEach(x=>x.on=0);it.on=!it.on;rerender();});
 v.querySelectorAll('.step button').forEach(b=>b.onclick=()=>{const it=CART[b.dataset.s][+b.dataset.i];it.q=Math.max(1,it.q+ +b.dataset.d);rerender();});
 const cs=v.querySelector('#cs'),anc=v.querySelector('#anc');
 anc.querySelectorAll('button').forEach(b=>b.onclick=()=>{const t=v.querySelector('#cs_'+b.dataset.t);if(t)cs.scrollTo({top:t.offsetTop-anc.offsetHeight+2,behavior:'smooth'});});
 cs.onscroll=()=>{let on='closed';for(const k of ['closed','d29','d30']){const t=v.querySelector('#cs_'+k);if(t&&t.offsetTop-anc.offsetHeight-10<=cs.scrollTop)on=k;}anc.querySelectorAll('button').forEach(b=>b.classList.toggle('on',b.dataset.t===on));};
 function rerender(){const st=cs.scrollTop;v.innerHTML=cartHTML();bindCart();v.querySelector('#cs').scrollTop=st;v.querySelector('#cs').onscroll();}}
function showCart(){closeDts();closeWx();let v=document.getElementById('cartv');if(!v){v=document.createElement('div');v.id='cartv';v.className='cartv';document.querySelector('.app').appendChild(v);}
 cartFrom=view;view='cart';press('ovCart');v.innerHTML=cartHTML();v.hidden=false;bindCart();}
function closeCart(){const v=document.getElementById('cartv');if(v&&!v.hidden){v.hidden=true;if(view==='cart'){view=cartFrom||'home';if(view==='home')render(cur);else if(view==='first')showFirst();else if(view==='orders')showOrders(ordMode);}}}
'''
rep_between('const ORD_TOTAL=312400;', '\n\nconst GREET=', ORDERS)

# ---------- first screen ----------
rep("setBleed(false);view='first';setTab('home');\n document.querySelectorAll('.time-btn').forEach(b=>b.setAttribute('aria-pressed','false'));document.getElementById('ovOrders').setAttribute('aria-pressed','false');document.getElementById('ovBleed').setAttribute('aria-pressed','false');document.getElementById('ovFirst').setAttribute('aria-pressed','true');",
    "closeCart();closeDts();setBleed(false);view='first';setTab('home');press('ovFirst');dbar(['10/29(목)','오늘 17:20 발주마감']);")
rep('<b>자주 쓰는 품목 담아 두기</b>', '<b>자주 사는 상품 즐겨찾기</b>')
rep('담아 두기${chev', '즐겨찾기${chev')
rep('월~토 오전 7시 전 매장 도착', '월~금 오전 7시 전 매장 도착')

# ---------- weather ----------
rep("{d:'내일 · 토',ic:'rain',w:'비 70%',t:'12° / 18°',in:'10/31'", "{d:'내일 · 목',ic:'rain',w:'비 70%',t:'12° / 18°',in:'10/29'")
rep("{d:'모레 · 일',ic:'cloud',w:'흐림 30%',t:'9° / 15°',in:'11/1'", "{d:'모레 · 금',ic:'cloud',w:'흐림 30%',t:'9° / 15°',in:'10/30'")
rep("{d:'글피 · 월',ic:'sun',w:'맑고 쌀쌀',t:'4° / 13°',in:'11/2'", "{d:'다음 주 · 월',ic:'sun',w:'맑고 쌀쌀',t:'4° / 13°',in:'11/2'")
rep('기상청 단기예보 · 11/6 14:00 발표', '기상청 단기예보 · 10/28 14:00 발표')
rep("const b=document.getElementById('ovWx');if(b&&b.getAttribute('aria-pressed')==='true'){b.setAttribute('aria-pressed','false');document.querySelectorAll('.time-btn').forEach(x=>x.setAttribute('aria-pressed',String(+x.dataset.i===cur)));}",
    "const b=document.getElementById('ovWx');if(b&&b.getAttribute('aria-pressed')==='true'&&view==='home'){press(null);document.querySelectorAll('.time-btn').forEach(x=>x.setAttribute('aria-pressed',String(+x.dataset.i===cur)));}")

# ---------- render ----------
RENDER = r'''function render(i){
 closeWx();closeDts();const cv=document.getElementById('cartv');if(cv)cv.hidden=true;cur=i;const s=STATES[i];if(location.hash==='#first')try{history.replaceState(null,'',location.pathname+location.search)}catch(e){}view='home';document.getElementById('home').hidden=false;document.getElementById('orders').hidden=true;setTab('home');
 document.getElementById('cartBadge').textContent=s.cart;document.getElementById('cartBadge').hidden=!s.cart;
 dbar(s.dbar);
 const now=s.now.length?`<div class="now"><div class="task-card">${s.now.map(r=>row(r,'now')).join('')}</div></div>`:'';
 const INS=`<div class="insight"><span class="wchip"><span class="wx"><img src="${IMG.cloud}" alt=""><i></i><i></i><i></i></span>내일 비 70%</span><span class="txt">${s.ins}</span>${chev('#111')}</div>`;
 const SLOTS=s.slots?`<div class="slots" id="slots" hidden>${s.slots.map(r=>`<div class="sr"><div class="tm"><small>${r[0]}</small><b>${r[1]}</b></div><div class="if"><b>${r[2]}</b><small>${r[3]}</small></div><span class="bd${r[4]?' on':''}">${r[4]?'<i></i>추적 가능':'도착 예정만'}</span></div>`).join('')}</div>`:'';
 const TRK=s.trk?`<div class="trk"><span class="b"><i></i>${s.trk[0]}</span>${s.trk[1]}</div>`:'';
 const RW=railW();
 document.getElementById('home').innerHTML=`
  <div class="sec-title first q">지금 할 일이 <span class="cnt">${s.count}</span> 있어요</div>
  <div class="hero-wrap"><section class="hero" id="hero">
   <div class="label"><i></i>${s.label}</div>
   <h2>${s.head}</h2>
   <div class="nums"><div class="l"><small>${s.lk}</small><b>${s.lv}</b></div><div class="r"><small>${s.rk}</small><b>${s.rv}</b>${s.av?`<span class="av">주문가능 <b>${s.av}</b></span>`:''}</div></div>
   ${rail(s,RW)}${SLOTS}${TRK}
   <div class="actions"><button class="btn primary">${s.btn1} <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button><button class="btn secondary">${s.btn2}</button></div>
   ${INS}
  </section></div>
  ${now}
  <div class="soon-wrap"><div class="sec-title q">곧 할 일이 <span class="cnt">3건</span> 있어요</div>
  <div class="soon">${SOON.map(r=>row(r,'soon')).join('')}</div></div>
  <div class="banner-wrap"><div class="banner" id="banner"><div class="btrack" id="btrack">${[...BANNERS,BANNERS[0]].map(b=>`<div class="slide" style="background:${b.bg}"><span class="tag">${b.tag}</span><h3>${b.h}</h3><p>${b.p}</p><img class="pent" src="${IMG[b.img]}" alt=""></div>`).join('')}</div>
   <div class="bctl"><button id="bprev" aria-label="이전 배너"><svg width="8" height="10" viewBox="0 0 8 10"><path d="M6 1 2 5l4 4" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button><span id="bpage">1 | 5</span><button id="bpause" aria-label="자동 넘김 멈춤"><svg width="8" height="10" viewBox="0 0 8 10"><rect x="1" y="1" width="2" height="8" fill="#fff"/><rect x="5" y="1" width="2" height="8" fill="#fff"/></svg></button><button id="bnext" aria-label="다음 배너"><svg width="8" height="10" viewBox="0 0 8 10"><path d="m2 1 4 4-4 4" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button></div></div></div>
  <div class="sec-title q">지금 담기 좋아요 <span class="more">전체보기${chev('#8E9196')}</span></div>
  <div class="chips" id="chips">${CHIPS.map((c,j)=>`<button class="chip" aria-pressed="${j===chipIdx}" data-j="${j}"><span class="th"><img src="${IMG[c.img]}" alt=""></span><span><b>${c.t}</b><span>${c.s}</span></span></button>`).join('')}</div>
  <div class="grid" id="grid">${productsHTML(CHIPS[chipIdx].set)}</div>
  <div class="spacer"></div>`;
 const mini=document.getElementById('mini');
 mini.innerHTML=`<span class="mth">${cargoMini(s)}</span><span class="mtx">${s.mini.html}</span><span class="bar"><i style="width:${s.mini.bar}%"></i></span>${chev('#111')}`;
 press(null);document.querySelectorAll('.time-btn,.sheet .time-btn').forEach(b=>b.setAttribute('aria-pressed',String(+b.dataset.i===i)));
 document.getElementById('fabT').textContent=s.t;
 document.getElementById('scroll').scrollTop=0;if(isM())window.scrollTo(0,0);mini.classList.remove('on');
 const cb=document.querySelector('.capb');if(cb)cb.onclick=e=>{e.stopPropagation();const sl=document.getElementById('slots');sl.hidden=!sl.hidden;cb.setAttribute('aria-expanded',String(!sl.hidden));};
 bindHome();startCountdown();startCargo();fitRail();
}
'''
rep_between('function render(i){', 'let bleed=false;', RENDER)

# ---------- panel bindings ----------
rep("document.getElementById('ovOrders').onclick=()=>showOrders();", "document.getElementById('ovOrders').onclick=()=>showOrders('d29');\ndocument.getElementById('ovReturn').onclick=()=>showOrders('d28');\ndocument.getElementById('ovCart').onclick=()=>{if(view==='cart')return;render(1);showCart();};\ndocument.getElementById('ovDate').onclick=()=>{render(2);openDts();press('ovDate');};\ndocument.getElementById('cartBtn').onclick=()=>showCart();")
rep("document.getElementById('ovWx').onclick=()=>{setBleed(false);render(1);openWx();document.querySelectorAll('.time-btn').forEach(b=>b.setAttribute('aria-pressed','false'));document.getElementById('ovWx').setAttribute('aria-pressed','true');};",
    "document.getElementById('ovWx').onclick=()=>{setBleed(false);render(1);openWx();press('ovWx');};")
rep("document.querySelectorAll('.tab').forEach(t=>t.onclick=()=>{if(t.dataset.tab==='orders')showOrders();else if(t.dataset.tab==='home'&&view==='orders')render(cur);});",
    "document.querySelectorAll('.tab').forEach(t=>t.onclick=()=>{if(t.dataset.tab==='orders')showOrders('d29');else if(t.dataset.tab==='home'&&view==='orders')render(cur);});")
rep(" if(!e.target.closest('#hero'))return;", " if(!e.target.closest('#hero')||e.target.closest('.capb,.slots,.trk'))return;")
rep("document.getElementById('orders').addEventListener('click',e=>{if(e.target.closest('.ocard')&&!e.target.closest('button')){setBleed(true);render(0);}});", "")
rep("const s=Math.min(1,(innerHeight-72)/844);", "const s=Math.min(1,(innerHeight-72)/844);")

s = s.replace('<title>', '<title>')
open(P, 'w', encoding='utf-8').write(s)
print('ok', len(s))
