# Booking funnel: Ad → Survey → Booking → Thank You

Design: the project's main look (white, orange `#ff6a00`, black `#111`, DM Sans + JetBrains Mono).

```
Facebook / Instagram Ad
        │
        ▼
1. SURVEY PAGE  (survey.html)           7 qualifying questions + contact step
        │   submits lead to GHL (webhook), then redirects:
        ├── good fit ──► 2. BOOKING PAGE (booking.html: calendar element in the middle)
        │                         │
        │                         ▼
        │                  3. THANK YOU PAGE (thankyou.html)
        └── low fit ──► Playbook page ($17), so nobody leaves empty-handed
```

Files: `survey.html`, `booking.html`, `thankyou.html`, `ad-copy.md`.

## Who counts as a "good fit"
Low fit = "I'm not running a painting business yet" **or** "Not right now" to the monthly investment question (typically $500–$2,500/mo, from your own TSL). Everything else goes to booking. Edit `isFit()` in `survey.html` to change the rule.

## GHL setup
1. **Pages:** create 3 blank pages (Survey, Booking, Thank You). Paste each file into one Custom HTML element. For Booking, add the native **Calendar** element between block A and block B.
2. **Custom fields (Contacts):** `business_type`, `avg_job`, `lead_source`, `estimates_month`, `bottleneck`, `goal`, `investment`, `city`, `fit`, `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`.
3. **Inbound webhook:** Automation → Workflow → trigger **Inbound Webhook** → action **Create/Update Contact**, mapping the fields above plus `first_name`, `last_name`, `email`, `phone`. Copy the webhook URL into `CFG.WEBHOOK_URL` in `survey.html`. Then add tags: `survey-completed`, and `fit-qualified` or `fit-low` (If/Else on `fit`).
4. **URLs to set** (CONFIG in `survey.html`): `BOOKING_URL`, `LOWFIT_URL` (your Playbook page), `PRIVACY_URL`, `TERMS_URL`. Replace `PRIVACY-POLICY-URL`, `TERMS-URL` and `PLAYBOOK-PAGE-URL` in the three files.
5. **Calendar:** Calendars → create a 30-minute "Strategy Call" calendar. Redirect after booking → the Thank You page. The survey sends `first_name`, `last_name`, `email`, `phone` in the URL so the calendar can prefill them (**not tested in your account**, check it once).
6. **Workflows:**
   - Booked → confirmation text + email (ask them to reply to the text), reminders 24h / 3h / 30 min before.
   - No-show → text "Sorry we missed you, want to grab another time?" with the booking link.
   - Survey completed but not booked after 1 hour → text with the booking link, then 24h and 48h follow-ups.
   - Low fit → email with the Playbook link.
7. **Pipeline:** New Lead → Booked → Showed → Proposal → Won / Lost.
8. **Tracking:** Meta pixel on all pages; Lead event on survey submit, Schedule event on the thank-you page.

## Before you launch
- SMS consent: the survey has an opt-in checkbox with the standard wording. Make sure your Privacy Policy and Terms cover SMS (A2P 10DLC registration).
- The webhook is sent in "no-cors" mode, so the page cannot read the response. The page redirects after 2.5 seconds even if GHL is slow. Test with a real submission and check the contact appears.
- Without a webhook URL the survey runs in **preview mode** (shows what it would send, doesn't redirect).
- Check the headline and every claim against what you can prove. No income guarantees.
