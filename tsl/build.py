import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import pages_tsl, pages_oto
from lib import Page, CSS, JS
out = os.path.dirname(os.path.abspath(__file__))
NOTE_TRIG = """<!-- ===== HOW THE BUTTONS WORK (GHL) =====
 Buttons marked data-trigger="trg-oto-yes" / "trg-ds-yes" / "trg-no" click a hidden NATIVE GHL button with that Custom Class.
 Add 3 native Button elements at the bottom of the page (Custom Class: trg-oto-yes, trg-ds-yes, trg-no) and set their actions
 (one-click upsell / Go to funnel step). Hide them with:  .trg-oto-yes,.trg-ds-yes,.trg-no{position:absolute;left:-9999px}
 Links that say CHECKOUT-URL / BOOKING-CALENDAR-URL / PRIVACY-POLICY-URL / TERMS-URL must be replaced with your real URLs. -->
"""
files = {}
files['tsl-landing.html'] = pages_tsl.landing().render(with_js=False)
a,b = pages_tsl.checkout()
files['tsl-checkout.html'] = ("<!-- BLOCK A: paste in a Custom HTML element ABOVE your GHL Order Form -->\n"+a.render(with_js=False)
    +"\n\n<!-- >>> PLACE YOUR GHL ORDER FORM ELEMENT HERE <<< -->\n\n<!-- BLOCK B: paste in a Custom HTML element BELOW the Order Form (CSS already loaded by block A) -->\n<div class=\"tsl\">\n"+"\n".join(b.parts)+"\n</div>\n")
files['tsl-oto1.html'] = pages_oto.oto1().render(note=NOTE_TRIG)
files['tsl-oto2.html'] = pages_oto.oto2().render(note=NOTE_TRIG)
files['tsl-oto3.html'] = pages_oto.oto3().render(note=NOTE_TRIG)
files['tsl-oto4.html'] = pages_oto.oto4().render(note=NOTE_TRIG)
files['tsl-thankyou-call.html'] = pages_oto.ty_call().render(with_js=False)
files['tsl-thankyou-only.html'] = pages_oto.ty_only().render(with_js=False)
for n,c in files.items():
    open(os.path.join(out,n),'w',encoding='utf-8').write(c)
    print(n, len(c))
