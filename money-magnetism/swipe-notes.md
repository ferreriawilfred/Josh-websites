# Swipe notes — hisforbiddenobsession.com/1-get-him-in-3-days-page

Reference notes only (read from the page's public HTML). Used to guide our own build, not to reuse their assets.

## Platform
Built on GoHighLevel (LeadConnector). Page is step 1 of the funnel (`1-get-him-in-3-days-page`). Footer pages: terms-of-service, privacy-policy, refund-policy.
The next step (checkout / order form) is triggered by the CTA buttons via JavaScript, so its URL is not visible in the HTML. To map steps 2+ someone has to click through the live funnel.

## Fonts
| Use | Font | Weights |
|---|---|---|
| Headlines / display | **Fraunces** (serif, Google Fonts) | 400, 500, 600, italic 500 |
| Body text | **DM Sans** (Google Fonts) | 400, 500, 700 |
| Form fields (opt-in / order form) | **Mulish** (Google Fonts) | 400, 600 |
| Icons | Font Awesome 5 (Free + Brands) | — |

Sizes: body 16–18px, small 12–15px, big headline 48px (desktop), sub-headline 26px. Content container 660px, breakpoints 767px / 1024px.

## Colors (most used)
| Hex | Likely role |
|---|---|
| `#3b2756` | deep purple (text / dark sections) |
| `#7150a9`, `#9b72cf` | purple accents |
| `#6e5e86` | muted purple (secondary text) |
| `#d9a441` | gold (stars, accents) |
| `#f6efe7`, `#fbf6ef` | warm cream backgrounds |
| `#1b7d45` | green ("Verified") |
| `#241030`, `#2e1b3f` | very dark purple |
| `#188bf6` | blue (form / link default) |

## Images and media on the page (26 files, all hosted on GHL's CDN)
| Group | Count | Size / type | Where |
|---|---|---|---|
| Testimonial photos, set 1 (swipe cards) | 11 PNG | 80×80 round avatars (`uhh-tst-photo`) | Top testimonial swipe, 9 visible cards + extras |
| Video testimonials | 4 MP4 + 4 PNG posters | vertical video cards (`uhh-vc-video`), preload metadata | "Watch Rachel / Steph / Danielle / Megan" row |
| Founder photo | 1 PNG | served via leadconnector image resizer (320–1200px WebP) | Founder story section |
| Testimonial photos, set 2 ("Real women · Real messages") | 6 PNG | small avatars beside the "Verified" badge | Second testimonial wall |
| Hero | none | text only | Above the fold |

No logo, no hero image, no product shots.

## What this means for our page
- Match the **structure** (text-only hook, avatar swipe cards, video testimonial row, founder photo, avatar wall) — already done in `tsl-page.html`.
- Fonts to consider for a closer feel: Fraunces + DM Sans (ours currently: Cormorant Garamond + Inter).
- Colors: theirs is purple + gold on cream; ours is gold on white/off-white. Switching is a CSS variable change.
- Assets we still need of our own: ~17 testimonial avatars, 4 video testimonials + posters, 1 Kaia photo. Use real customers' photos and videos (with permission) — do not reuse theirs.
