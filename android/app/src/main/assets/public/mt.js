class F{
constructor(n,d=1){if(d===0)throw 0;if(d<0){n=-n;d=-d;}
let g=F.gcd(Math.abs(n),d);this.n=n/g;this.d=d/g;}
static gcd(a,b){return b?F.gcd(b,a%b):a;}
static of(x){return x instanceof F?x:(typeof x==='string'?F.parse(x):new F(x,1));}
toString(){return this.d===1?''+this.n:this.n+'/'+this.d;}}
function decToFrac(s){let neg=false;if(s.startsWith('-')){neg=true;s=s.slice(1);}
let[i,f]=s.includes('.')?s.split('.'):[s||'0',''];let den=Math.pow(10,f.length);
let num=+(i||'0')*den+(+f||0);return new F(neg?-num:num,den);}
F.parse=function(s){if(s instanceof F)return s;if(typeof s!=='string')s=String(s);
s=s.trim();if(s.includes('/')){let p=s.split('/');return new F(+p[0],+p[1]);}
if(s.includes('.'))return decToFrac(s);return new F(+s,1);};
const FW={};for(let i=0;i<10;i++)FW[String.fromCharCode(0xFF10+i)]=String(i);
FW['\uFF0C']=',';FW['\uFF1B']=';';FW['\uFF0F']='/';FW['\uFF0D']='-';
FW['\u2212']='-';FW['\uFE63']='-';FW['\u3000']='';FW['\uFF05']='';FW['\uFF08']='(';FW['\uFF09']=')';
function norm(s){return[...String(s)].map(c=>FW[c]??c).join('').trim().replace(/ /g,'');}
function check(u,a){u=norm(u);a=norm(a);if(u===a)return true;
try{if(a.indexOf(';')>=0||u.indexOf(';')>=0){
let pl=s=>s.split(';').filter(Boolean).map(x=>F.parse(x));
return pl(u).length===pl(a).length&&pl(u).every((x,i)=>x.n===pl(a)[i].n&&x.d===pl(a)[i].d);}
if(a.indexOf(',')>=0||u.indexOf(',')>=0){
let pl=s=>s.replace('[','').replace(']','').split(',').filter(x=>String(x).trim()!=='').map(x=>F.parse(x.replace(';',',')));
let lu=pl(u),la=pl(a);
return lu.length===la.length&&lu.every((x,i)=>x.n===la[i].n&&x.d===la[i].d);}
return F.parse(u).n===F.parse(a).n&&F.parse(u).d===F.parse(a).d;
}catch(e){return false;}}
const R={randint:(a,b)=>a+Math.floor(Math.random()*(b-a+1)),
choice:a=>a[Math.floor(Math.random()*a.length)]};
function fmt(v){let f=F.of(v);return f.d===1?''+f.n:f.toString();}
function fact(n){let r=1;for(let i=2;i<=n;i++)r*=i;return r;}
const G={};function add(g,n,fn){(G[g]||(G[g]=[])).push([n,fn]);}

add('小一','二位數加法',()=>{let a=R.randint(11,98),b=R.randint(1,a-1);return[a+' + '+b+' = ?',String(a+b)];});
add('小一','二位數減法',()=>{let a=R.randint(11,98),ones=a%10,b;
if(ones>=2&&ones<=8)b=R.randint(ones+1,9);else{a=R.randint(18,98);b=R.randint(1,a-1);}
return[a+' - '+b+' = ?',String(a-b)];});
add('小一','乘法進位',()=>{let a=R.randint(2,9),b=R.randint(2,9),c=R.randint(2,9),d=R.randint(2,9);
return[a+'×'+b+' + '+c+'×'+d+' = ?',String(a*b+c*d)];});
add('小一','乘加混合',()=>{let a=R.randint(2,9),b=R.randint(2,9),c=R.randint(2,9);
return[a+'×'+b+' + '+c+' = ?',String(a*b+c)];});
add('小一','乘減混合',()=>{let a=R.randint(2,9),b=R.randint(2,9),c=R.randint(2,9);
return[a+'×'+b+' - '+c+' = ?',String(a*b-c)];});
add('小一','十以內加減',()=>{if(Math.random()<0.5){let a=R.randint(1,8),b=R.randint(1,10-a);
return[a+' + '+b+' = ?',String(a+b)];}let b=R.randint(1,9),a=R.randint(b+1,10);
return[a+' - '+b+' = ?',String(a-b)];});
add('小一','應用題',()=>{let b=R.randint(2,6),a=R.randint(7,10);
return['水果攤有 '+b+' 顆蘋果，媽媽又買了 '+a+' 顆，一共有幾顆？',String(a+b)];});
add('小一','整十加減',()=>{let t=[10,20,30,40,50,60,70,80,90];
if(Math.random()<0.5){let a=R.choice([10,20,30,40,50]),b=R.choice(t.filter(x=>x<=100-a));
return[a+' + '+b+' = ?',String(a+b)];}let a=R.choice([20,30,40,50,60,70,80,90]),
b=R.choice(t.filter(x=>x<a));return[a+' - '+b+' = ?',String(a-b)];});

add('小二','乘法算式',()=>{let a=R.randint(2,9),b=R.randint(2,9),c=R.randint(2,9);
return[a+'×'+b+' × '+c+' = ?',String(a*b*c)];});
add('小二','乘數求法',()=>{let b=R.randint(2,9),q=R.randint(2,9);
return[b+' × □ = '+b*q+'，□ ＝ ?',String(q)];});
add('小二','九九乘法',()=>{let v=R.choice([7,8,9]),d=R.randint(2,9);
return['九九乘法：'+['七','八','九'][v-7]+'×'+d+' = ?',String(v*d)];});
add('小二','數的組成',()=>{let a=R.randint(20,98);
return[String(a)+' = '+Math.floor(a/10)+'個十＋'+(a%10)+'個一，□個十＋□個一？',Math.floor(a/10)+'個十＋'+(a%10)+'個一'];});
add('小二','購物問題',()=>{let c=R.randint(3,18)*50;
return['甲有 '+c+' 元，乙有 '+(c+200)+' 元，共幾元？',String(2*c+200)];});
add('小二','時間換算',()=>{let h=R.choice([1,2,3,5,6]);return[h+' 小時 = 幾分鐘？',String(h*60)];});
add('小二','裝箱問題',()=>{let a=R.randint(2,9),f=R.randint(3,9);
return[a*f+' 顆糖果，每'+a+'顆一裝，可裝幾袋？',String(f)];});
add('小二','應用題',()=>{let k=R.randint(2,6),m=R.randint(2,5);
return['把 '+k*m+' 顆糖果平分給 '+m+' 位小朋友，每人幾顆？',String(k)];});

add('小三','周長問題',()=>{let a=R.randint(3,9),b=R.randint(2,6);
return['長方形長 '+a+'、寬 '+b+'，周長 = ?',String(2*(a+b))];});
add('小三','因數倍數',()=>{let a=R.randint(2,9),b=R.randint(2,9);
return[a+'×'+b+' = '+a*b+' = □×'+a+' ＝ □×'+b,String(a)+' 或 '+String(b)];});
add('小三','倒數',()=>{let n=R.randint(1,3),d=R.randint(2,9);
return['分數 '+n+'/'+d+' 的倒數 = ?',fmt(new F(d,n))];});
add('小三','整十除法',()=>{let a=R.randint(10,30)*10;return[String(a)+'÷10 = ?',String(a/10)];});
add('小三','圓周長',()=>{let r=R.randint(3,12);
return['圓形半徑 '+r+',周長（3.14） = ?',String(Math.round(3.14*2*r*10)/10)];});
add('小三','帶分數化假分數',()=>{let w=R.randint(2,5),d=R.choice([3,4,5,6]),n=R.randint(1,d-1);
return['帶分數 '+w+' 又 '+n+'/'+d+' 化成假分數 = ?',(w*d+n)+'/'+d];});
add('小三','應用題',()=>{let p=R.randint(6,24),n=R.randint(2,4);
return['一枝筆 '+p+' 元，買 '+n+' 枝給 100 元，找回多少？',String(100-p*n)];});

add('小四','裝盒問題',()=>{let q=R.randint(10,49),d=R.randint(2,9);
return[q*d+' 顆糖裝成每盒 '+d+' 顆，可裝幾盒？',String(q)];});
add('小四','整數大小',()=>{let a=R.randint(10,99),b=R.randint(10,99);
return['比 '+a+' 大的最小整數 + '+b+' = ?',String(a+1+b)];});
add('小四','時間加法',()=>{let h=R.randint(2,5),m=R.randint(1,5)*10;
return[h+'時'+String(m).padStart(2,'0')+'分 ＋ 30分 = 共幾分鐘？',String(h*60+m+30)];});
add('小四','次方計算',()=>{let a=R.randint(2,9),k=R.randint(2,5);
return[String(a)+' 的 '+k+' 次方 = ?',String(Math.pow(a,k))];});
add('小四','長方面積',()=>{let a=R.randint(20,49),b=R.randint(5,19);
return['長方形長 '+a+' 寬 '+b+'，面積 = ?平方公分',String(a*b)];});
add('小四','四則混合',()=>{let a=R.randint(2,9),b=R.randint(2,9),c=R.randint(2,9);
return[a+' + '+b+' × '+c+' = ?',String(a+b*c)];});
add('小四','分配律簡算',()=>{let a=R.randint(2,9),b=R.randint(2,9),c=R.randint(2,9);
return['用分配律：'+a+'×'+b+' + '+a+'×'+c+' = ?',String(a*(b+c))];});
add('小四','應用題',()=>{let v=R.choice([45,60,75,80,90]),t=R.randint(2,5);
return['巴士時速'+v+'公里行駛'+t+'小時，共多少公里？',String(v*t)];});

add('小五','分數倒數',()=>{let n=R.randint(2,8),d=n+R.randint(1,5);
return['分數 '+n+'/'+d+' 的倒數 = ?',fmt(new F(d,n))];});
add('小五','分數加法',()=>{let n1=R.randint(1,4),d1=R.randint(5,9),n2=R.randint(1,4);
return[n1+'/'+d1+' + '+n2+'/'+d1+' = ?',fmt(new F(n1+n2,d1))];});
add('小五','分數減法',()=>{let n1=R.randint(2,8),d1=9,n2=R.randint(1,n1-1);
return[n1+'/'+d1+' - '+n2+'/'+d1+' = ?',fmt(new F(n1-n2,d1))];});
add('小五','小數化分數',()=>{let p=R.choice([[3,4],[1,2],[1,5],[3,5],[1,4],[2,5]]);
return[String(p[0]/p[1])+' 化成最簡分數 = ?',fmt(new F(p[0],p[1]))];});
add('小五','長方體體積',()=>{let a=R.randint(2,9),b=R.randint(2,9),c=R.randint(2,9);
return['長方體長'+a+'寬'+b+'高'+c+'，體積 = ?立方公分',String(a*b*c)];});
add('小五','分數化小數',()=>{let p=R.choice([[1,2],[1,4],[3,4],[1,5],[2,5],[3,5],[4,5],[1,8],[1,10],[7,10]]);
return['分數 '+p[0]+'/'+p[1]+' 化成小數 = ?',fmt(new F(p[0],p[1]))];});
add('小五','質數判斷',()=>{let n=R.randint(2,29),ok=true;
for(let i=2;i*i<=n;i++)if(n%i===0){ok=false;break;}
return[String(n)+' 是質數嗎？（回答「是」或「否」）',ok?'是':'否'];});
add('小五','應用題',()=>{let p=R.choice([40,50,60,80,120,150]),d=R.choice([['八',8],['五',5],['九',9]]);
return['原價'+p+'元打'+d[0]+'折，特價多少元？',String(p*d[1]/10)];});

add('小六','百分率',()=>{let n=R.randint(1,4),d=R.randint(2,9);
return['分數 '+n+'/'+d+' 用百分率表示 = ?%',String(Math.round(n/d*100))];});
add('小六','比例',()=>{let a=R.randint(2,8),b=R.randint(2,9),c=a*R.randint(2,5);
return['比例 '+a+':'+b+' = '+c+':□，□ = ?',String(c*b/a)];});
add('小六','圓面積',()=>{let r=R.randint(3,12);
return['半徑 '+r+' 的圓面積（3.14） = ?',String(Math.round(3.14*r*r*10)/10)];});
add('小六','速率時間',()=>{let t=R.randint(10,60),v=R.randint(50,100);
return['速率'+v+'km/h 行駛'+t+'分鐘，距離 = ?km',String(Math.round(v*t/60))];});
add('小六','百分率成數',()=>{let v=R.choice([25,40,50,60,75,80]);
return[v+'% 化成最簡分數 = ?',fmt(new F(v,100))];});
add('小六','百分率求值',()=>{let pct=R.choice([5,10,15,20,25,30,35,40,45,50,60,70,75,80,90,95]),k=R.randint(1,9);
return[pct+'% 的 '+(k*100)+' = ?',String(pct*k)];});
add('小六','比例尺',()=>{let x=R.randint(2,9),k=R.choice([10000,50000,100000]);
return['地圖比例 1:'+k+'，圖上'+x+'公分，實際 = ?公尺',String(x*k/100)];});
add('小六','應用題',()=>{let r=R.choice([10,20,30]);
return['半徑'+r+'公分的圓面積（3.14） = ? 平方公分',String(Math.round(3.14*r*r*10)/10)];});

add('國一','一元一次',()=>{let c=R.randint(-9,9),r=R.randint(2,5);
return['方程 '+r+'x + ('+c+') = 0，x = ?',fmt(new F(-c,r))];});
add('國一','正負數加',()=>{let a=R.randint(-9,9),b=R.randint(-9,9);return[a+' + ('+b+') = ?',String(a+b)];});
add('國一','正負數混合',()=>{let a=R.randint(1,9),b=R.randint(1,9),c=R.randint(1,9);
return['(-'+a+')×(-'+b+')+(-'+c+') = ?',String(a*b-c)];});
add('國一','一元方程',()=>{let a=R.randint(-5,5)||1,b=R.randint(-5,5);
return['x 的 '+a+' 倍加 '+b+' = 0，x = ?',fmt(new F(-b,a))];});
add('國一','科學記號',()=>{let m=R.choice([1.2,2.5,3.5,4.8,6.4,8.2,9.6]),n=R.randint(2,4);
return[m+' × 10^'+n+' 用一般數字 = ?',String(Math.round(m*Math.pow(10,n)))];});
add('國一','一元一次不等式',()=>{let k=R.randint(-9,9),c=R.randint(1,9);
while(k===c)k=R.randint(-9,9);
let op=R.choice(['>','<','≥','≤']),sym=(op==='>'||op==='≥')?'>':'<';
return['x + '+k+' '+op+' '+c+'，求 x（如 x>3）',sym==='>'?'x>'+(c-k):'x<'+(c-k)];});
add('國一','聯立方程組',()=>{let x0=R.randint(-5,5),y0=R.randint(-5,5);
let m=R.choice([1,2,-1,3]),n=R.choice([-1,2,0,3]);while(m===n)n=R.choice([-1,2,0,3]);
return['解聯立：y='+m+'x+('+(y0-m*x0)+')、y='+n+'x+('+(y0-n*x0)+')，交點 = ?（x,y）',x0+','+y0];});
add('國一','年齡應用',()=>{let a=R.randint(8,12),b=R.randint(2,7);
return['小明今年'+a+'歲，哥哥比他大'+b+'歲，5年後哥哥幾歲？',String(a+b+5)];});
add('國一','應用題',()=>{let a=R.randint(8,12),b=R.randint(2,7);
return['今年'+a+'歲，比哥哥小'+b+'歲，5年後哥哥幾歲？',String(a+b+5)];});

add('國二','斜率',()=>{let x1=R.randint(-5,5),y1=R.randint(-5,5),m=R.randint(-3,3)||1;
let dx=R.randint(1,3),x2=x1+dx,y2=y1+m*dx;
return['('+x1+','+y1+') 與 ('+x2+','+y2+') 的斜率 = ?',String(m)];});
add('國二','行列式',()=>{let a=R.randint(1,9),b=R.randint(1,9),c=R.randint(1,9),d=R.randint(1,9);
return['行列式 |'+a+' '+b+'; '+c+' '+d+'| = ?',String(a*d-b*c)];});
add('國二','畢氏定理',()=>{let k=R.choice([1,2,3]),p=R.choice([[3,4],[5,12],[8,15]]);
return['直角三角形兩股 '+p[0]*k+'、'+p[1]*k+'，斜邊 = ?',String(Math.hypot(p[0]*k,p[1]*k))];});
add('國二','等差數列',()=>{let a=R.randint(10,49),d=R.randint(1,9);
return['等差：首項'+a+'，公差'+d+'，第三項 = ?',String(a+2*d)];});
add('國二','函數求值',()=>{let m=R.randint(-3,3)||2,c=R.randint(-9,9);
return['直線 y = '+m+'x + ('+c+')，x=2 時 y = ?',String(2*m+c)];});
add('國二','三角形內角和',()=>{let a=R.randint(30,60),b=R.randint(30,110-a);
return['三角形兩內角 '+a+'°、'+b+'°，第三個內角 = ?度',String(180-a-b)];});
add('國二','平均速率',()=>{let v=R.choice([60,75,90,105]),t=R.choice([2,3,4]);
return['共行駛 '+v*t+' 公里花了 '+t+' 小時，平均時速 = ?',String(v)];});
add('國二','應用題',()=>{let v=R.choice([60,75,90,105]),t=R.choice([2,3,4]);
return['開車 '+v*t+' 公里花 '+t+' 小時，平均時速 = ?公里',String(v)];});

add('國三','等比數列',()=>{let a=R.randint(1,5),r=R.randint(2,3);
return['等比：首項'+a+'，公比'+r+'，第三項 = ?',String(a*r*r)];});
add('國三','判別式',()=>{let a=R.randint(1,9),b=R.randint(-9,9),c=R.randint(-9,9);
return['二次方程 '+a+'x²+('+b+')x+('+c+')=0，判別式 = ?',String(b*b-4*a*c)];});
add('國三','兩根之和',()=>{let r1=R.randint(-5,5),r2=R.randint(-5,5);
return['兩根為 '+r1+'、'+r2+'，兩根之和 = ?',String(r1+r2)];});
add('國三','兩根之積',()=>{let r1=R.randint(-6,6),r2=R.randint(-6,6);
return['兩根為 '+r1+'、'+r2+'，兩根之積 = ?',String(r1*r2)];});
add('國三','對稱軸',()=>{let a=R.randint(1,9),c=R.randint(-9,9);
return['y='+a+'x²+('+0+')x+('+c+') 的對稱軸 x = ?',String(0)];});
add('國三','拋物線頂點x',()=>{let a=R.choice([1,2,3]),k=R.randint(-4,4),b=-2*a*k,c=R.randint(-9,9);
return['y='+a+'x²+('+b+')x+('+c+')，頂點 x 座標 = ?',String(k)];});
add('國三','影子相似',()=>{let h=R.choice([140,150,160,170]),s=h/2,k=R.randint(2,7);
return['身高'+h+'影長'+s+'，旗杆影長'+(s*k)+'，旗杆高 = ?',String(h*k)];});
add('國三','應用題',()=>{let h=R.choice([140,150,160,170]),s=h/2,k=R.randint(2,7);
return['身高'+h+'公分影子'+s+'公分，旗杆影子'+(s*k)+'公分，旗杆高？',String(h*k)];});

add('高一','對數',()=>{let a=R.randint(2,5),b=R.randint(1,5);
return['log₍'+a+'₎'+Math.pow(a,b)+' = ?',String(b)];});
add('高一','對數相加',()=>{let a=R.randint(2,5),b=R.randint(1,5),c=R.randint(1,4);
return['log₍'+a+'₎'+Math.pow(a,b)+' + log₍'+a+'₎'+Math.pow(a,c)+' = ?',String(b+c)];});
add('高一','指數次方',()=>{let a=R.randint(2,5),b=R.randint(1,4);
return[String(a)+'^? = '+Math.pow(a,b)+'，求次方 = ?',String(b)];});
add('高一','展開係數',()=>{let a=R.randint(1,8),b=R.randint(1,8);
return['（x+'+a+'）（x+'+b+'）展開後 x 的係數 = ?',String(a+b)];});
add('高一','兩點距離',()=>{let k=R.randint(1,2),p=R.choice([[3,4],[5,12],[8,15]]);
return['A(0,0) 與 B('+p[0]*k+','+p[1]*k+') 的距離 = ?',String(Math.hypot(p[0]*k,p[1]*k))];});
add('高一','單利本利和',()=>{let P=R.choice([10000,20000,50000]),r=R.choice([1,2,3,5]),n=R.choice([2,3,5]);
return['定存 '+P+' 元年利率'+r+'%，存'+n+'年單利，本利和 = ?',String(P+P*r*n/100)];});
add('高一','應用題',()=>{let P=R.choice([10000,20000,50000]),r=R.choice([1,2,3,5]),n=R.choice([2,3,5]);
return['存款 '+P+' 元年利'+r+'%，單利'+n+'年共領回多少？',String(P+P*r*n/100)];});

add('高二','等差級數和',()=>{let a=R.randint(1,5),d=R.randint(2,5),n=R.randint(6,12),s2;
do{a=R.randint(1,5);d=R.randint(2,5);n=R.randint(6,12);s2=n*(2*a+(n-1)*d);}while(s2%2!==0);
return['等差級數 a₁='+a+'，d='+d+'，S('+n+') = ?',String(s2/2)];});
add('高二','等比級數和',()=>{let a=R.randint(1,3),r=2,n=R.randint(4,6);
return['等比級數 a₁='+a+'，r='+r+'，S('+n+') = ?',
String(a*(Math.pow(r,n)-1)/(r-1))];});
add('高二','三角函數值',()=>{let e=R.choice([[0,'0'],[30,'1/2'],[90,'1']]);
return['sin'+e[0]+'° = ?',e[1]];});
add('高二','組合',()=>{let n=R.randint(3,8),r=R.randint(2,3);
return['C('+n+','+r+') = ?',String(fact(n)/fact(r)/fact(n-r))];});
add('高二','向量長度',()=>{let k=R.choice([1,2,3]),p=R.choice([[3,4],[5,12],[8,15]]);
return['向量（'+p[0]*k+'，'+p[1]*k+'）的長度 = ?',String(Math.hypot(p[0]*k,p[1]*k))];});
add('高二','期望值',()=>{let c=R.choice([[3,1,100],[1,1,50],[2,2,60],[4,1,80]]);
return['紅'+c[0]+'白'+c[1]+'，抽中紅得'+c[2]+'元，期望值 = ?元',String(c[0]*c[2]/(c[0]+c[1]))];});
add('高二','排列P進階',()=>{let n=R.randint(5,8),r=R.randint(2,3),v=1;
for(let i=0;i<r;i++)v*=n-i;return['P('+n+','+r+') = ?',String(v)];});
add('高二','應用題',()=>{let c=R.choice([[3,1,100],[1,1,50],[2,2,60],[4,1,80]]);
return['袋中紅'+c[0]+'白'+c[1]+'，抽中紅得'+c[2]+'元（放回），期望值？',String(c[0]*c[2]/(c[0]+c[1]))];});

add('高三','判別式',()=>{let a=R.randint(1,9),b=R.randint(-9,9),c=R.randint(-9,9);
return['二次方程 '+a+'x²+('+b+')x+('+c+')=0，判別式 b²-4ac = ?',String(b*b-4*a*c)];});
add('高三','等比級數和',()=>{let a=R.randint(1,3),r=R.choice([2,3]),n=R.randint(4,6);
return['等比級數 a₁='+a+'，r='+r+'，S('+n+') = ?',
String(a*(Math.pow(r,n)-1)/(r-1))];});
add('高三','極限值',()=>{let a=R.randint(1,9),k=R.randint(-5,5),b=R.randint(-9,9);
return['lim(x→'+k+')（'+a+'x+'+b+'） = ?',String(a*k+b)];});
add('高三','排列 P',()=>{let n=R.randint(3,8),r=R.randint(2,3);
return['P('+n+','+r+') = ?',String(fact(n)/fact(n-r))];});
add('高三','組合 C',()=>{let n=R.randint(3,8),r=R.randint(2,3);
return['C('+n+','+r+') = ?',String(fact(n)/fact(r)/fact(n-r))];});
add('高三','骰子機率',()=>{let c=R.choice([['偶數',1,2],['質數',3,6],['大於4',2,6],['6的倍數',1,6]]);
return['擲骰子出現「'+c[0]+'」的機率 = ?',fmt(new F(c[1],c[2]))];});
add('高三','行列式面積',()=>{let a=R.randint(1,5),b=R.randint(1,5),c=R.randint(1,5),d=R.randint(1,5);
return['以向量('+a+','+b+')、('+c+','+d+')為鄰邊平行四邊形面積 = ?',String(Math.abs(a*d-b*c))];});
add('高三','應用題',()=>{let a=R.randint(1,5),b=R.randint(1,5),c=R.randint(1,5),d=R.randint(1,5);
return['向量('+a+','+b+')、('+c+','+d+')張出的平行四邊形面積？',String(Math.abs(a*d-b*c))];});

function getTopics(g){return G[g]||[];}
function randomQ(g){let ts=getTopics(g);if(!ts.length)return['',''];return R.choice(ts)[1]();}

if(typeof process!=='undefined'&&typeof require!=='undefined'){
let bad=0,total=0;
for(let g in G){G[g].forEach(function(p){let n=p[0],fn=p[1];
for(let i=0;i<150;i++){let qa=fn();
if(!qa||!qa[0]||!qa[1]){bad++;console.log('EMPTY',g,n,qa);}
else if(!check(qa[1],qa[1])){bad++;console.log('FAIL',g,n,qa);}else total++;}});}
console.log('topics:',Object.keys(G).reduce(function(s,v){return s+G[v].length;},0),
'checks:',total,'bad:',bad);}