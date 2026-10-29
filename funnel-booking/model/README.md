# Booking funnel — model version (inspired by the pagesprovider template)

Same flow as before: **Ad → Landing page with survey → Booking page → Thank-you page**, but the survey now sits *inside* the landing page (like the template), with proof, About, FAQ and a closing CTA around it.

```
Ad ─► landing.html (hero + 3-step survey + proof + about + FAQ)
         ├─ good fit ─► booking.html (calendar) ─► thankyou.html
         └─ low fit  ─► your $17 Playbook page
```

## Files (each one is a Custom HTML/JS element, paste-ready for GHL)
- `landing.html`: header, hero, survey card (3 questions, then name / phone / email), what we do, real numbers, About Lanty, FAQ, closing CTA.
- `booking.html`: **Block A** above the GHL Calendar element, **Block B** below it. Set the GHL section background to `#f6f5f0` so the calendar sits on the same cream as the page.
- `thankyou.html`
- `build.py`: regenerates the three files (shared CSS lives there). Run `python3 build.py`.

## What was kept from the template
Charcoal header with a button, cream page, amber button, condensed uppercase headings (Barlow Condensed), "Step 1 of 3" with big tap buttons and a Next button, trust line ("No spam · No pressure · No hidden fees"), "After this step you'll be redirected…" on the contact step, FAQ accordion, dark About card, closing CTA.

## What is different (on purpose)
- **No made-up reviews, ratings or warranties.** The template's "4.9 / 117 reviews / 10-year warranty" are not copied. The proof section uses your own numbers ($4M+, $1M, 25%, $15 per lead). Add real client reviews later if you have them.
- **No fake urgency** ("before this month's schedule fills up").
- Contact step asks **email** too (needed for the calendar and follow-up).

## Set up in GHL
1. Paste each file into one Custom HTML element on a blank page (booking = two elements + the Calendar between).
2. In `landing.html`, edit the CONFIG block (bottom): `WEBHOOK_URL` (GHL Inbound Webhook), `BOOKING_URL`, `LOWFIT_URL`, `PRIVACY_URL`, `TERMS_URL`. Replace `PRIVACY-POLICY-URL`, `TERMS-URL`, `PLAYBOOK-PAGE-URL` in the three files.
3. Custom fields, workflows, calendar and pixel events: same as `../README.md`.
4. Without a webhook URL the survey runs in preview mode (shows what it would send, no redirect).

Not tested inside your GHL account: webhook intake, calendar prefill, SMS.
