# Clone of the pagesprovider painting-lead template (structure + look). All business details live in ONE config block per page.
import os, re
OUT = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(OUT, '..', 'model', 'build.py'), encoding='utf-8').read()
CSS = base.split("CSS = r'''")[1].split("'''")[0]
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&family=Barlow+Condensed:wght@600;700&display=swap" rel="stylesheet">'

EXTRA = r'''
<style>
  /* ---- extras for the clone ---- */
  .pp .pp-offer{display:inline-block;margin:0 auto 16px;padding:8px 16px;border-radius:999px;background:#fff7e6;border:1px solid rgba(245,166,35,.6);color:#8a5a0a;font-weight:700;font-size:15px}
  .pp .pp-offer[hidden]{display:none}
  .pp .ba{position:relative;max-width:560px;margin:0 auto 6px;border-radius:20px;overflow:hidden;box-shadow:0 18px 44px rgba(38,40,43,.22);background:#ddd;aspect-ratio:4/3;user-select:none;-webkit-user-select:none;touch-action:pan-y}
  .pp .ba img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;pointer-events:none}
  .pp .ba .ba-before{clip-path:inset(0 50% 0 0)}
  .pp .ba .ba-line{position:absolute;top:0;bottom:0;left:50%;width:3px;margin-left:-1.5px;background:#fff;box-shadow:0 0 8px rgba(0,0,0,.35);pointer-events:none}
  .pp .ba .ba-knob{position:absolute;top:50%;left:50%;width:42px;height:42px;margin:-21px 0 0 -21px;border-radius:50%;background:#fff;box-shadow:0 4px 14px rgba(0,0,0,.3);display:flex;align-items:center;justify-content:center;font-size:18px;color:var(--ink);pointer-events:none}
  .pp .ba .ba-tag{position:absolute;bottom:12px;padding:6px 12px;border-radius:6px;font-size:12px;font-weight:700;letter-spacing:.14em;color:#fff;pointer-events:none}
  .pp .ba .ba-tag.b{left:12px;background:rgba(38,40,43,.9)}
  .pp .ba .ba-tag.a{right:12px;background:var(--green)}
  .pp .ba input[type=range]{position:absolute;inset:0;width:100%;height:100%;margin:0;opacity:0;cursor:ew-resize}
  .pp .ba input[type=range]:focus-visible + .ba-ui{outline:3px solid rgba(245,166,35,.7)}
  .pp .pp-drag{margin:6px 0 24px;text-align:center;font-weight:700;font-size:13px}
  .pp .rv{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;max-width:820px;margin:18px auto 0}
  .pp .rv .rv-slot{display:flex;align-items:center;justify-content:center;min-height:200px;padding:20px;border:2px dashed var(--acc);border-radius:16px;background:#fff7e6;color:var(--accd);text-align:center;font-weight:700;font-size:15px}
  .pp .rv img{display:block;width:100%;height:auto;border-radius:16px;box-shadow:0 8px 24px rgba(38,40,43,.12)}
  .pp .pp-rate{text-align:center;color:var(--mut);margin:14px 0 0;font-weight:600}
  .pp .pp-sorry{margin:10px 0 0;padding:12px 14px;border-radius:10px;background:#fff3f3;border:1px solid #f1c0c0;color:#a12626;font-size:14.5px}
  @media(max-width:760px){.pp .rv{grid-template-columns:1fr}.pp .ba{border-radius:16px}.pp .pp-grid2{grid-template-columns:1fr}}
</style>
'''

LEGAL = '''  <div class="pp-foot">Copyrights 2026 | <span data-cfg="name">Your Painting Co</span> &nbsp;|&nbsp; <a href="PRIVACY-POLICY-URL">Privacy Policy</a> &nbsp;|&nbsp; <a href="TERMS-URL">Terms &amp; Conditions</a><br>
    Results and offers vary. <span data-cfg-offer-fine></span>
    This site is not affiliated with or endorsed by Facebook, Inc. FACEBOOK is a trademark of Meta Platforms, Inc.</div>
'''

COMMON_JS = r'''
  var $=function(id){return document.getElementById(id)};
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  /* fill every data-cfg="key" with the config value (keeps the sample text if the value is blank) */
  function applyCfg(C){
    document.querySelectorAll('[data-cfg]').forEach(function(e){var v=C[e.getAttribute('data-cfg')]; if(v!==undefined&&v!=='') e.textContent=v});
    document.querySelectorAll('[data-cfg-hide]').forEach(function(e){var k=e.getAttribute('data-cfg-hide'); if(!C[k]) e.hidden=true});
  }
'''

BUSINESS_CFG = r'''
  /* ============================ BUSINESS DETAILS — replace the SAMPLE values with real ones ============================ */
  var BIZ={
    name:'Your Painting Co',      // shown in the header, headline and footer
    city:'Your City',             // "YOUR CITY & SURROUNDINGS"
    owner:'Jon',                  // "Hey, I'm Jon"
    rating:'4.9',                 // SAMPLE: only use your real Google rating (leave '' to hide)
    reviews:'117+',               // SAMPLE: your real number of reviews
    warranty:'10',                // SAMPLE: years of workmanship warranty you really offer (leave '' to hide)
    offer:'$250 off any project booked this month',  // SAMPLE: leave '' to hide. Only keep it if it is true.
    minProject:'$1,000'           // used in the budget question
  };
'''

def top(btn_label, href):
    return f'''  <div class="pp-top"><div class="pp-top-in">
    <span class="pp-brand" data-cfg="name">Your Painting Co</span>
    <a class="pp-tbtn" href="{href}">{btn_label}</a>
  </div></div>
'''

# ============================================================= LANDING + SURVEY
LANDING_JS = r'''
<script>
(function(){
  if(window.__ppClone) return; window.__ppClone=true;
''' + BUSINESS_CFG + r'''
  /* ============================ FUNNEL SETTINGS ============================ */
  var CFG={
    WEBHOOK_URL:'',                                   // GHL workflow trigger "Inbound Webhook" URL. Leave '' to preview.
    BOOKING_URL:'REPLACE-WITH-BOOKING-PAGE-URL',      // the page with your calendar
    SERVICE_ZIPS:[],                                  // e.g. ['432','43215'] = prefixes you serve. [] = accept every ZIP / postal code.
    BEFORE_IMG:'', AFTER_IMG:'',                      // photo URLs for the slider ('' = sample drawing)
    REVIEW_IMGS:[],                                   // up to 4 Google review screenshot URLs ('' = placeholder boxes)
    OWNER_IMG:'',                                     // owner photo URL
    PRIVACY_URL:'PRIVACY-POLICY-URL', TERMS_URL:'TERMS-URL'
  };
''' + COMMON_JS + r'''
  /* ----- fill business details ----- */
  var C={name:BIZ.name,city:BIZ.city,owner:BIZ.owner,rating:BIZ.rating,reviews:BIZ.reviews,warranty:BIZ.warranty,offer:BIZ.offer,min:BIZ.minProject};
  applyCfg(C);
  document.querySelectorAll('[data-cfg-hide]').forEach(function(e){var k=e.getAttribute('data-cfg-hide');if(C[k])e.hidden=false});
  var fine=document.querySelector('[data-cfg-offer-fine]'); if(fine&&BIZ.offer) fine.textContent='Offer: '+BIZ.offer+'. ';

  /* ----- before / after slider ----- */
  function svgHouse(c1,c2,c3,label){
    var s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300"><rect width="400" height="300" fill="'+c1+'"/><rect y="215" width="400" height="85" fill="'+c3+'"/><polygon points="70,125 200,45 330,125" fill="'+c2+'" opacity=".85"/><rect x="85" y="125" width="230" height="110" fill="'+c2+'"/><rect x="170" y="165" width="60" height="70" fill="#3b3f46"/><rect x="105" y="150" width="45" height="38" fill="#e9edf2"/><rect x="250" y="150" width="45" height="38" fill="#e9edf2"/></svg>';
    return 'data:image/svg+xml;utf8,'+encodeURIComponent(s);
  }
  var bImg=$('ba-b'), aImg=$('ba-a');
  bImg.src=CFG.BEFORE_IMG||svgHouse('#cfd8e3','#8a8178','#7a8a6a');
  aImg.src=CFG.AFTER_IMG ||svgHouse('#bfe0ff','#f4f6f8','#5f9a63');
  var rng=$('ba-r');
  function setBA(v){bImg.style.clipPath='inset(0 '+(100-v)+'% 0 0)';$('ba-line').style.left=v+'%';$('ba-knob').style.left=v+'%'}
  rng.addEventListener('input',function(){setBA(+rng.value)}); setBA(50);

  /* ----- reviews / owner photo ----- */
  var rv=$('rv-grid');
  var sl=''; for(var k=0;k<4;k++){ sl+= CFG.REVIEW_IMGS[k] ? '<img src="'+esc(CFG.REVIEW_IMGS[k])+'" alt="Google review" loading="lazy">' : '<div class="rv-slot">Add a Google review screenshot here</div>' }
  rv.innerHTML=sl;
  if(CFG.OWNER_IMG) $('owner-img').innerHTML='<img src="'+esc(CFG.OWNER_IMG)+'" alt="'+esc(BIZ.owner)+'" width="220" height="220" loading="lazy" style="display:block;width:100%;height:auto;border-radius:14px">';

  /* ----- survey: 3 steps then contact (same as the template) ----- */
  var Q=[
    {id:'project_type',q:'What’s your main project?',o:[['🛋️','Interior Painting'],['🏡','Exterior Painting'],['🗄️','Cabinet Painting'],['🍿','Popcorn Ceiling Removal']]},
    {id:'timing',q:'When would you like to get started?',o:[['🚀','I’m ready now'],['📅','Within the next few weeks'],['🗓️','A few months out'],['👀','Just curious for now']]},
    {id:'budget_ok',q:'Does a budget starting at '+BIZ.minProject+' work for you?',o:[['👍','Yes'],['👎','No']]}
  ];
  var T=Q.length,A={},i=0,sel=null,busy=false;
  var host=$('pp-body'),bar=$('pp-barfill'),back=$('pp-back'),nextB=$('pp-next'),nav=$('pp-nav');
  function showQ(){
    var q=Q[i];sel=A[q.id]||null;bar.style.width=(i/(T+1)*100)+'%';back.hidden=(i===0);nav.hidden=false;nextB.disabled=!sel;
    var h='<fieldset class="pp-opts"><legend class="pp-q" style="grid-column:1/-1;padding:0">Step '+(i+1)+' of '+T+': '+esc(q.q)+' <span>*</span></legend>';
    q.o.forEach(function(o,k){var id='ppq'+i+'_'+k;h+='<label class="pp-opt" for="'+id+'"><input type="radio" name="'+q.id+'" id="'+id+'" value="'+esc(o[1])+'"'+(sel===o[1]?' checked':'')+'><span><u>'+o[0]+'</u>'+esc(o[1])+'</span></label>'});
    host.innerHTML=h+'</fieldset>';
    host.querySelectorAll('input').forEach(function(r){r.addEventListener('change',function(){sel=r.value;A[q.id]=sel;nextB.disabled=false})});
  }
  function showContact(){
    bar.style.width=(T/(T+1)*100)+'%';back.hidden=false;nav.hidden=true;
    host.innerHTML='<p class="pp-note">After this step, you’ll be redirected to pick a time for your free estimate!</p>'+
      '<form id="pp-form" novalidate>'+
      '<label class="pp-field"><b>Full Name *</b><input type="text" id="pp-fn" autocomplete="name"></label>'+
      '<label class="pp-field"><b>Phone *</b><input type="tel" id="pp-ph" autocomplete="tel" inputmode="tel"></label>'+
      '<label class="pp-field"><b>ZIP / Postal Code *</b><input type="text" id="pp-zip" autocomplete="postal-code"></label>'+
      '<label class="pp-consent"><input type="checkbox" id="pp-ok"><span>I agree to receive calls and text messages (including automated) from '+esc(BIZ.name)+' about my request. Consent is not a condition of purchase. Msg &amp; data rates may apply. Reply STOP to opt out. See our <a href="'+esc(CFG.PRIVACY_URL)+'">Privacy Policy</a> and <a href="'+esc(CFG.TERMS_URL)+'">Terms</a>.</span></label>'+
      '<div class="pp-err" id="pp-err" role="alert"></div>'+
      '<button class="pp-btn" type="submit" id="pp-go" style="width:100%">Book My Free Estimate →</button></form>';
    $('pp-form').addEventListener('submit',submit);
  }
  function served(zip){ if(!CFG.SERVICE_ZIPS.length) return true; zip=zip.replace(/\s+/g,'').toUpperCase(); return CFG.SERVICE_ZIPS.some(function(p){return zip.indexOf(String(p).replace(/\s+/g,'').toUpperCase())===0}) }
  function utm(){var o={},p=new URLSearchParams(location.search);['utm_source','utm_medium','utm_campaign','utm_content','utm_term','fbclid'].forEach(function(k){if(p.get(k))o[k]=p.get(k)});return o}
  function submit(e){
    e.preventDefault();if(busy)return;
    var fn=$('pp-fn'),ph=$('pp-ph'),zp=$('pp-zip'),ok=$('pp-ok'),err=$('pp-err'),bad=[];
    [fn,ph,zp].forEach(function(x){x.classList.remove('bad')});
    if(fn.value.trim().length<2)bad.push(fn);
    if(ph.value.replace(/\D/g,'').length<10)bad.push(ph);
    if(zp.value.trim().length<3)bad.push(zp);
    if(bad.length){bad.forEach(function(x){x.classList.add('bad')});err.textContent='Please fill in the highlighted fields.';bad[0].focus();return}
    if(!served(zp.value)){err.innerHTML='<span class="pp-sorry" style="display:block">Sorry, we don’t service that area yet. Please check the ZIP / postal code, or email us and we’ll let you know when we do.</span>';zp.classList.add('bad');return}
    if(!ok.checked){err.textContent='Please tick the box so we’re allowed to call or text you.';return}
    err.textContent='';busy=true;$('pp-go').disabled=true;$('pp-go').textContent='One moment…';
    var parts=fn.value.trim().split(/\s+/),first=parts.shift(),last=parts.join(' ');
    var d={first_name:first,last_name:last,phone:ph.value.trim(),postal_code:zp.value.trim(),sms_consent:true,page:location.href.split('?')[0]};
    Object.keys(A).forEach(function(k){d[k]=A[k]});var u=utm();Object.keys(u).forEach(function(k){d[k]=u[k]});
    try{sessionStorage.setItem('pp_lead',JSON.stringify({first_name:first,last_name:last,phone:d.phone}))}catch(x){}
    var dest=CFG.BOOKING_URL, url=dest+(dest.indexOf('?')>-1?'&':'?')+new URLSearchParams({first_name:first,last_name:last,phone:d.phone}).toString();
    function go(){
      bar.style.width='100%';back.hidden=true;var prev=/^REPLACE/.test(dest);
      host.innerHTML='<div class="pp-done"><h2>Thanks, '+esc(first)+'!</h2><p>Now pick a time for your free estimate.</p>'+(prev?'':'<div class="pp-spin"></div>')+'</div>';
      if(prev)host.firstChild.insertAdjacentHTML('beforeend','<div class="pp-prev"><b>Preview only.</b> In GHL this sends the lead to your webhook, then redirects to the booking page. Set BOOKING_URL in the settings block.<br><br><b>Data:</b> '+esc(JSON.stringify(d))+'</div>');
      else setTimeout(function(){location.href=url},900);
    }
    if(CFG.WEBHOOK_URL){var done=false,t=setTimeout(function(){if(!done){done=true;go()}},2500);
      fetch(CFG.WEBHOOK_URL,{method:'POST',mode:'no-cors',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams(d).toString(),keepalive:true})
        .then(function(){if(!done){done=true;clearTimeout(t);go()}}).catch(function(){if(!done){done=true;clearTimeout(t);go()}})}
    else go();
  }
  nextB.addEventListener('click',function(){if(!sel||busy)return;if(i<T-1){i++;showQ()}else showContact()});
  back.addEventListener('click',function(){if(busy)return;if(nav.hidden){i=T-1;showQ()}else if(i>0){i--;showQ()}});
  showQ();
})();
</script>
'''

def landing():
    return f'''<!-- ===== PAGE 1 — LANDING PAGE WITH SURVEY (clone of the template) — ONE Custom HTML/JS element on a blank GHL page =====
     Ad → this page → booking page. Replace the SAMPLE business details and the URLs in the settings block at the bottom. -->
{FONTS}
{CSS}
{EXTRA}
<div class="pp" id="pp-landing">
{top('<span class="lg">Book Free Estimate</span><span class="sm">Free Estimate</span>','#pp-survey')}
  <div class="pp-hero">
    <span class="pp-eyebrow"><span data-cfg="city">Your City</span> &amp; surroundings · Licensed &amp; Insured</span>
    <h1><span data-cfg="name">Your Painting Co</span>’s Highest-Rated <em>House Painters</em></h1>
    <div class="pp-meta"><span data-cfg-hide="rating">★ <b data-cfg="rating">4.9</b> On Google</span><span data-cfg-hide="reviews"><b data-cfg="reviews">117+</b> Reviews</span><span data-cfg-hide="warranty"><b data-cfg="warranty">10</b>-Yr Warranty</span></div>
    <span class="pp-offer" data-cfg-hide="offer">🎁 <span data-cfg="offer">$250 off any project booked this month</span></span>
    <div class="ba" id="ba">
      <img id="ba-a" alt="After painting" width="800" height="600"><img id="ba-b" class="ba-before" alt="Before painting" width="800" height="600">
      <span class="ba-tag b">BEFORE</span><span class="ba-tag a">AFTER</span>
      <input type="range" id="ba-r" min="0" max="100" value="50" aria-label="Drag to compare before and after">
      <span class="ba-line" id="ba-line"></span><span class="ba-knob" id="ba-knob">⇄</span>
    </div>
    <p class="pp-drag">Drag the slider</p>
  </div>

  <div class="pp-wrap" id="pp-survey" style="scroll-margin-top:12px">
    <div class="pp-card">
      <h2 style="text-align:center">Book Your Free Estimate</h2>
      <p class="pp-sm">Takes 30 seconds — pick a time that works for you on the next page.</p>
      <div class="pp-bar"><i id="pp-barfill"></i></div>
      <div id="pp-body"></div>
      <div class="pp-nav" id="pp-nav"><button type="button" class="pp-back" id="pp-back" hidden>← Back</button><button type="button" class="pp-btn" id="pp-next" disabled>Next →</button></div>
      <p class="pp-trust"><span>No spam</span><span>No pressure</span><span>No hidden fees</span></p>
    </div>
  </div>

  <div class="pp-wrap pp-sec">
    <span class="pp-eyebrow">Reviews</span>
    <h2>What Your Neighbors Say</h2>
    <div class="rv" id="rv-grid"></div>
    <p class="pp-rate" data-cfg-hide="rating">★ <span data-cfg="rating">4.9</span> from <span data-cfg="reviews">117+</span> Google reviews</p>
  </div>

  <div class="pp-wrap pp-sec">
    <div class="pp-about">
      <div id="owner-img"><div class="rv-slot" style="min-height:200px;border:2px dashed var(--acc);border-radius:14px;background:#2f3236;color:var(--acc);display:flex;align-items:center;justify-content:center;text-align:center;padding:12px;font-weight:700;font-size:14px">Add the owner’s photo here</div></div>
      <div>
        <h2>Hey, I’m <span data-cfg="owner">Jon</span></h2>
        <p>I started <span data-cfg="name">Your Painting Co</span> because too many homeowners were getting burned by unreliable, rushed work. We do it differently:</p>
        <ul><li>We’ll respect your home as our own</li><li>On time and on budget, every job</li><li>Done right, with a smile</li></ul>
      </div>
    </div>
  </div>

  <div class="pp-wrap pp-sec">
    <div class="pp-grid2" style="max-width:700px;margin:0 auto">
      <div class="pp-tile" data-cfg-hide="warranty"><span class="ic">🛡️</span><h3><span data-cfg="warranty">10</span>-Year Warranty</h3><p>Workmanship backed up to <span data-cfg="warranty">10</span> years, in writing.</p></div>
      <div class="pp-tile"><span class="ic">👍</span><h3>100% Satisfaction</h3><p>We don’t leave until you’re happy with the work.</p></div>
    </div>
  </div>

  <div class="pp-wrap pp-sec">
    <span class="pp-eyebrow">Questions?</span>
    <h2>Frequently Asked</h2>
    <div class="pp-faq" style="margin-top:18px">
      <details><summary>Am I going to get a high-pressure sales pitch?</summary><p>Absolutely not. We’ll give you an honest assessment of what the project involves and what it will cost, and answer any questions you have. No obligations.</p></details>
      <details><summary>How long does the estimate take?</summary><p>About 45 minutes for smaller projects like kitchen cabinets, and up to an hour and a half for a full interior or exterior. We walk the property with you (15–20 minutes), measure and evaluate conditions, then go through a written estimate line by line (15–20 minutes). We do it in person so changes can be made on the spot.</p></details>
      <details><summary>Do I need to be home during the estimate?</summary><p>Yes, we ask that all decision makers are present. We bring samples and ask questions most contractors don’t, so the proposal is as accurate as possible.</p></details>
      <details><summary>Can you help me choose colors?</summary><p>Yes, we’re happy to do a free color consultation. Just ask.</p></details>
      <details><summary>Are you insured?</summary><p>Yes, fully licensed and insured. We carry liability insurance and workers’ comp, so you’re protected from start to finish.</p></details>
    </div>
  </div>

  <div class="pp-close">
    <span class="pp-eyebrow" style="color:var(--acc)">Ready for a fresh coat?</span>
    <h2>Book Your Free Estimate</h2>
    <p data-cfg-hide="offer">Claim your free estimate and <span data-cfg="offer">$250 off any project booked this month</span>.</p>
    <a class="pp-btn" href="#pp-survey">Book My Free Estimate</a>
  </div>
{LEGAL}</div>
{LANDING_JS}'''

# ============================================================= BOOKING
BOOK_JS = r'''
<script>
(function(){
  if(window.__ppBook) return; window.__ppBook=true;
''' + BUSINESS_CFG + COMMON_JS + r'''
  applyCfg({name:BIZ.name,city:BIZ.city,owner:BIZ.owner,offer:BIZ.offer});
  var fine=document.querySelector('[data-cfg-offer-fine]'); if(fine&&BIZ.offer) fine.textContent='Offer: '+BIZ.offer+'. ';
  try{var n=new URLSearchParams(location.search).get('first_name');if(n){var e=$('pp-hi');if(e)e.textContent=n+', pick a time'}}catch(x){}
})();
</script>
'''
def booking():
    return f'''<!-- ===== PAGE 2 — PICK A TIME (booking page) =====
     BLOCK A (first part, with the CSS) goes ABOVE your GHL Calendar element, BLOCK B goes BELOW it.
     Set the GHL section background to #f6f5f0 so the calendar sits on the cream page. Edit the business details in the script at the end of block B. -->
{FONTS}
{CSS}
{EXTRA}
<div class="pp" id="pp-book">
{top('Pick A Time','#pp-cal')}
  <div class="pp-hero" style="padding-bottom:10px">
    <span class="pp-eyebrow" id="pp-hi">Step 2 of 2</span>
    <h1>Pick A Time For Your <em>Free Estimate</em></h1>
    <p class="pp-sub">Choose a day and time that works for you. We’ll confirm by text and email.</p>
    <p id="pp-cal" style="margin:0 0 8px;font-weight:700;scroll-margin-top:12px">👇 Select a date and time below</p>
  </div>
</div>

<!-- >>>>>>>>>>  PLACE YOUR GHL CALENDAR ELEMENT HERE  <<<<<<<<<<  -->

<!-- BLOCK B — paste in a Custom HTML element BELOW the calendar -->
<div class="pp" id="pp-book-b">
  <div class="pp-wrap pp-sec" style="padding-top:30px">
    <span class="pp-eyebrow">What to expect</span>
    <h2>Your Free Estimate, Step By Step</h2>
    <ol class="pp-steps" style="margin-top:16px">
      <li><div><h3>We walk the property with you</h3><p>About 15–20 minutes. You show us what you want done, and we talk about scope and problem areas.</p></div></li>
      <li><div><h3>We measure and evaluate</h3><p>We check existing conditions and take exact measurements to put together an accurate price on the spot.</p></div></li>
      <li><div><h3>We go through a written estimate</h3><p>Line by line, so you know exactly what’s included. No pressure.</p></div></li>
    </ol>
  </div>
  <div class="pp-wrap pp-sec">
    <ul class="pp-list">
      <li>The estimate is free and there’s no obligation</li>
      <li>Please have all decision makers there</li>
      <li>Fully licensed and insured</li>
    </ul>
  </div>
{LEGAL}</div>
{BOOK_JS}'''

# ============================================================= THANK YOU
TY_JS = r'''
<script>
(function(){
  if(window.__ppTy) return; window.__ppTy=true;
''' + BUSINESS_CFG + COMMON_JS + r'''
  applyCfg({name:BIZ.name,city:BIZ.city,owner:BIZ.owner,offer:BIZ.offer});
  var fine=document.querySelector('[data-cfg-offer-fine]'); if(fine&&BIZ.offer) fine.textContent='Offer: '+BIZ.offer+'. ';
})();
</script>
'''
def thankyou():
    return f'''<!-- ===== PAGE 3 — THANK YOU (after the estimate is booked) — ONE Custom HTML element. Edit the business details in the script at the end. ===== -->
{FONTS}
{CSS}
{EXTRA}
<div class="pp" id="pp-ty">
{top('<span class="lg">What To Expect</span><span class="sm">Next Steps</span>','#pp-next')}
  <div class="pp-hero">
    <div class="pp-big" aria-hidden="true">✓</div>
    <span class="pp-eyebrow">Your estimate is booked</span>
    <h1>You’re All Set. <em>We’ll See You Soon.</em></h1>
    <p class="pp-sub">We just sent a confirmation to your phone. Here’s how to get the most out of your free estimate.</p>
  </div>
  <div class="pp-wrap" id="pp-next" style="padding-top:8px;scroll-margin-top:12px">
    <ol class="pp-steps">
      <li><div><h3>Reply to the confirmation text</h3><p>It confirms your spot and makes sure our reminders reach you.</p></div></li>
      <li><div><h3>Have everyone who decides at home</h3><p>We go through the estimate together, so it helps when every decision maker is there.</p></div></li>
      <li><div><h3>Think about what you want done</h3><p>Rooms or areas, colors you like, and any problem spots. We’ll also happily help with colors.</p></div></li>
    </ol>
  </div>
  <div class="pp-wrap pp-sec">
    <span class="pp-eyebrow">On estimate day</span>
    <h2>What Happens</h2>
    <ul class="pp-list" style="margin-top:16px">
      <li>We walk the property with you and talk through the scope</li>
      <li>We measure and check the existing conditions</li>
      <li>We give you a written estimate and go through it line by line</li>
    </ul>
  </div>
  <div class="pp-wrap pp-sec">
    <h2>Need To Change Your Time?</h2>
    <p class="pp-sub" style="margin-bottom:0">Use the reschedule link in your confirmation text or email, and please give us a few hours’ notice.</p>
  </div>
{LEGAL}</div>
{TY_JS}'''

for name, fn in (('landing', landing), ('booking', booking), ('thankyou', thankyou)):
    open(os.path.join(OUT, name + '.html'), 'w', encoding='utf-8').write(fn())
    print(name)
