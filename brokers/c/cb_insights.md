# Cb Insights Inc

- **Email:** privacy@cbinsights.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** cbinsights.com
- **Priority: 1.**

## Status

- Current: `email_pending` (updated 2026-09-02)
- Note: Sent the B2B contact-database letter, phrased for a business-intelligence/research product rather than a pure contact-finder: asked about customer exports and re-enrichment suppression, phone/name search over personal email.
- **Reply (2026-09-01):** an email-verification gate. "You are receiving this email because someone submitted a privacy opt-out request for this email address. In order to process your request... you must verify your email address by clicking the above link." The link is DataGrail-hosted (`cbinsights.datagrail.io/verification`), a client-side SPA — a plain HTTP fetch of the redirect target shows only the bare page title "Verification | DataGrail", with no way to tell from outside whether visiting it actually completes the verification (it likely needs the page's own JS to fire a completion call, which a non-browser fetch won't trigger). Queued to `handoff.py` for a human to open in a real browser and confirm the on-page result. Two identical verify emails arrived a few minutes apart — treat as one verification link, not two separate requests.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

- **Email verification gate, JS-rendered.** DataGrail's verification page cannot be confirmed as completed by a plain fetch — needs a human with a browser.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
