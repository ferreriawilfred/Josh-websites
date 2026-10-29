# Clone of the pagesprovider painting-lead template

Flow: **Ad → Landing page with survey → Pick-a-time (booking) page → Thank-you page**. Same structure and look as the template: dark header with a button, cream page, amber buttons, condensed uppercase headings, before/after slider, "Book Your Free Estimate" card (Step 1 of 3 → contact), reviews, About, FAQ and a closing CTA.

## Files (each is one Custom HTML/JS element, paste-ready for GHL)
- `landing.html` header, hero, slider, 3-step survey + contact (Full Name, Phone, ZIP), reviews, About, tiles, FAQ, CTA.
- `booking.html` **Block A** above the GHL Calendar element, **Block B** below it. Set the GHL section background to `#f6f5f0`.
- `thankyou.html`
- `build.py` regenerates the three files (`python3 build.py`). The shared CSS is read from `../model/build.py`.

## Replace the SAMPLE details (one block at the bottom of each file)
`BIZ`: business name, city, owner name, rating, review count, warranty years, offer text, minimum project.
**Everything marked SAMPLE (4.9 rating, 117+ reviews, 10-year warranty, "$250 off this month") is placeholder text.** Only keep a rating, review count, warranty or offer that is real; leave the value blank to hide it.

`CFG` (landing only): `WEBHOOK_URL` (GHL Inbound Webhook), `BOOKING_URL`, `SERVICE_ZIPS` (prefix list, blank = accept all; others get a "we don't service that area yet" message), `BEFORE_IMG` / `AFTER_IMG`, `REVIEW_IMGS` (up to 4 real Google review screenshots), `OWNER_IMG`, `PRIVACY_URL`, `TERMS_URL`. Also replace `PRIVACY-POLICY-URL` and `TERMS-URL` in the HTML.

## Survey fields sent to GHL
`project_type`, `timing`, `budget_ok` (Yes/No), `first_name`, `last_name`, `phone`, `postal_code`, `sms_consent`, UTM fields. Create matching custom fields and an Inbound Webhook workflow (Create/Update Contact, tag `survey-completed`, tag `budget-no` when `budget_ok` = No).

## Not tested in GHL
Webhook intake, calendar prefill from the URL (`first_name`, `last_name`, `phone`), and SMS. With no webhook URL the survey runs in preview mode.
