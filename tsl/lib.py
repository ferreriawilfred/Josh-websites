# Plain-TSL page builder: shared CSS + tiny helpers. Run: python3 build.py
import re, html as _h

CSS = r"""
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,400;0,700;1,400&family=Noto+Serif:wght@700&display=swap" rel="stylesheet">
<style>
  /* ===== PLAIN TSL STYLE — edit the 3 colors here ===== */
  .tsl{--tsl-head:#e00000;--tsl-btn:#df3129;--tsl-hl:#fff200}
  .tsl,.tsl *{box-sizing:border-box}
  .tsl{display:block !important;width:100% !important;max-width:680px;margin:0 auto;padding:26px 20px 56px;
       background:#ffffff;color:#111111;font-family:'Noto Sans',system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif;
       font-size:20px;line-height:1.6;text-align:left}
  .tsl p{margin:0 0 1.05em}
  .tsl h1,.tsl h2,.tsl h3{font-family:'Noto Serif',Georgia,'Times New Roman',serif;font-weight:700;margin:0}
  .tsl h1{font-size:34px;line-height:1.2;margin:0 0 .55em;color:#000}
  .tsl h2{font-size:28px;line-height:1.25;margin:1.7em 0 .6em;color:var(--tsl-head)}
  .tsl h3{font-size:22px;line-height:1.3;margin:1.3em 0 .4em;color:#000}
  .tsl .kicker{display:inline-block;margin:0 0 10px;padding:1px 6px;background:var(--tsl-hl);font-style:italic;font-size:17px;line-height:1.5}
  .tsl .eyebrow{display:block;margin:1.9em 0 -.2em;color:#6b7280;font-size:14px;font-weight:700;letter-spacing:.14em;text-transform:uppercase}
  .tsl .eyebrow + h2{margin-top:.5em}
  .tsl .warn{margin:0 0 1.2em;padding:12px 14px;border:2px solid var(--tsl-head);color:var(--tsl-head);font-weight:700;font-size:18px;line-height:1.45;text-align:center}
  .tsl ul,.tsl ol{margin:0 0 1.1em;padding-left:1.3em}
  .tsl li{margin:0 0 .45em}
  .tsl ul.chk{list-style:none;padding-left:0}
  .tsl ul.chk li{position:relative;padding-left:1.5em}
  .tsl ul.chk li::before{content:"✓";position:absolute;left:0;font-weight:700}
  .tsl ul.no{list-style:none;padding-left:0}
  .tsl ul.no li{position:relative;padding-left:1.5em;color:#444}
  .tsl ul.no li::before{content:"✗";position:absolute;left:0;color:var(--tsl-head);font-weight:700}
  .tsl hr{border:0;border-top:1px solid #000;width:120px;margin:1.2em auto 1.4em}
  .tsl .center{text-align:center}
  .tsl .box{margin:0 0 1.3em;padding:16px 18px;border:1px solid #cfcfcf;background:#fafafa}
  .tsl .box.red{border:2px solid var(--tsl-head)}
  .tsl .box p:last-child,.tsl .box ul:last-child{margin-bottom:0}
  .tsl blockquote{margin:0 0 1.1em;padding:2px 0 2px 16px;border-left:4px solid #000;font-style:italic}
  .tsl .label{font-weight:700;text-transform:uppercase;letter-spacing:.08em;font-size:15px;color:var(--tsl-head)}
  .tsl .price{margin:1.4em 0 .5em;text-align:center;font-size:19px}
  .tsl .price s{color:#555}
  .tsl .price b{color:#0a7d12}
  .tsl .price small{display:block;margin-top:2px;font-size:15px;color:#444}
  .tsl .big{font-size:32px}
  .tsl .tsl-center-btn{text-align:center;margin:.4em 0 1.4em}
  .tsl .decline{margin:.9em 0 1.6em;text-align:center;font-size:15px;line-height:1.5;color:#555}
  .tsl .decline a{color:#555;text-decoration:underline}
  .tsl .fine{margin-top:2.2em;padding-top:1.1em;border-top:1px solid #d4d4d4;color:#666;font-size:13px;line-height:1.55}
  .tsl .fine a{color:#666}
  .tsl a{color:#0000ee}
  .tsl a.tsl-btn,.tsl-btn{display:inline-block;min-width:240px;padding:14px 28px;border-radius:5px;background:var(--tsl-btn,#df3129);color:#fff !important;
       font-family:Arial,Helvetica,sans-serif;font-size:22px;font-weight:700;letter-spacing:.01em;line-height:1.2;text-align:center;text-decoration:none !important;cursor:pointer}
  .tsl a.tsl-btn:hover{filter:brightness(.92)}
  .tsl .nobreak{white-space:nowrap}
  /* hidden native GHL buttons (one-click upsell triggers) */
  .tsl-trigger-hint{display:none}
  @media(max-width:560px){
    .tsl{padding:18px 16px 44px;font-size:18px}
    .tsl h1{font-size:28px}
    .tsl h2{font-size:24px}
    .tsl h3{font-size:20px}
    .tsl a.tsl-btn,.tsl-btn{display:block;min-width:0;font-size:20px;padding:14px 16px}
  }
</style>
"""

JS = r"""
<script>
/* Buttons with data-trigger="xyz" click the hidden native GHL button that has the Custom Class "xyz".
   (Needed for one-click upsells: payment must be fired by a real GHL button element.) */
(function(){
  if(window.__tslTrig) return; window.__tslTrig=true;
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('[data-trigger]'); if(!a) return;
    var t=document.querySelector('.'+a.getAttribute('data-trigger'));
    if(t){ e.preventDefault(); var inner=t.querySelector('a,button,[role=button]')||t; inner.click(); }
  });
})();
</script>
"""

def inline(s):
    s = re.sub(r'&(?![a-zA-Z#0-9]+;)', '&amp;', s).replace('<','&lt;').replace('>','&gt;')
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'~~(.+?)~~', r'<s>\1</s>', s)
    s = re.sub(r'__(.+?)__', r'<u>\1</u>', s)
    s = s.replace('\n', '<br>')
    return s

class Page:
    def __init__(self): self.parts=[]
    def raw(self,x): self.parts.append(x); return self
    def kicker(self,t): return self.raw(f'<span class="kicker">{inline(t)}</span>')
    def warn(self,t): return self.raw(f'<div class="warn">{inline(t)}</div>')
    def h1(self,t): return self.raw(f'<h1>{inline(t)}</h1><hr>')
    def h2(self,t,eyebrow=None):
        e = f'<span class="eyebrow">{inline(eyebrow)}</span>' if eyebrow else ''
        return self.raw(f'{e}<h2>{inline(t)}</h2>')
    def h3(self,t): return self.raw(f'<h3>{inline(t)}</h3>')
    def p(self,*ts):
        for t in ts: self.raw(f'<p>{inline(t)}</p>')
        return self
    def c(self,*ts):
        for t in ts: self.raw(f'<p class="center">{inline(t)}</p>')
        return self
    def ul(self,items,cls=''):
        c = f' class="{cls}"' if cls else ''
        return self.raw(f'<ul{c}>'+''.join(f'<li>{inline(i)}</li>' for i in items)+'</ul>')
    def chk(self,items): return self.ul(items,'chk')
    def no(self,items): return self.ul(items,'no')
    def ol(self,items): return self.raw('<ol>'+''.join(f'<li>{inline(i)}</li>' for i in items)+'</ol>')
    def quote(self,t): return self.raw(f'<blockquote>{inline(t)}</blockquote>')
    def box(self,*ts,red=False,items=None):
        inner=''.join(f'<p>{inline(t)}</p>' for t in ts)
        if items: inner+='<ul class="chk">'+''.join(f'<li>{inline(i)}</li>' for i in items)+'</ul>'
        return self.raw(f'<div class="box{" red" if red else ""}">{inner}</div>')
    def price(self,old,new,unit='',note=''):
        n = f'<small>{inline(note)}</small>' if note else ''
        return self.raw(f'<p class="price">Price: <s>{old}</s> <b class="big">{new}</b> {unit}{n}</p>')
    def btn(self,label,trigger=None,href='#'):
        t = f' data-trigger="{trigger}"' if trigger else ''
        return self.raw(f'<div class="tsl-center-btn"><a class="tsl-btn" href="{href}"{t}>{label}</a></div>')
    def decline(self,text,sub,trigger='trg-no',href='#'):
        s = f'<br>{inline(sub)}' if sub else ''
        return self.raw(f'<p class="decline"><a href="{href}" data-trigger="{trigger}">{inline(text)}</a>{s}</p>')
    def fine(self,support=True,legal=True):
        x='<div class="fine">'
        if support: x+='<p>Questions? Email us at <a href="mailto:info@homeprojobs.com">info@homeprojobs.com</a>. We respond within one business day.</p>'
        x+='<p><a href="PRIVACY-POLICY-URL">Privacy Policy</a> &nbsp;·&nbsp; <a href="TERMS-URL">Terms &amp; Conditions</a></p>'
        if legal:
            x+='<p>This site is not affiliated with or endorsed by Facebook, Inc. FACEBOOK is a trademark of Meta Platforms, Inc.</p>'
            x+='<p>Super Paint &amp; Close is an education and training product. Results depend on individual effort, market conditions, and execution. This is not a guarantee of income. Please ensure you are 18+ before purchasing.</p>'
        x+='</div>'
        return self.raw(x)
    def render(self,with_js=True,note=''):
        return (note+CSS+'\n<div class="tsl">\n'+'\n'.join(self.parts)+'\n</div>\n'+(JS if with_js else ''))
