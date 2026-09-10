# Cb Insights Inc

- **Email:** privacy@cbinsights.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** cbinsights.com
- **Priority: 1.**

## Status

- Current: `manual_required` (updated 2026-09-09)
- Note: Sent the B2B contact-database letter, phrased for a business-intelligence/research product rather than a pure contact-finder: asked about customer exports and re-enrichment suppression, phone/name search over personal email.
- **Reply (2026-09-01):** an email-verification gate. "You are receiving this email because someone submitted a privacy opt-out request for this email address. In order to process your request... you must verify your email address by clicking the above link." The link is DataGrail-hosted (`cbinsights.datagrail.io/verification`), a client-side SPA — a plain HTTP fetch of the redirect target shows only the bare page title "Verification | DataGrail", with no way to tell from outside whether visiting it actually completes the verification (it likely needs the page's own JS to fire a completion call, which a non-browser fetch won't trigger). Queued to `handoff.py` for a human to open in a real browser and confirm the on-page result. Two identical verify emails arrived a few minutes apart — treat as one verification link, not two separate requests.
- **Outcome (2026-09-09): "Privacy Request Denied."** The 7-day verification window closed with the link never clicked (predicted above, and confirmed): "We did not receive verification from you... during the 7 day verification period... If you believe this is in error, please try submitting another privacy request." **This is a hard proof-point for the pattern, not a new failure mode** — a JS-rendered DataGrail verification link is structurally impossible to complete without a browser, so resubmitting produces the identical outcome on the identical timer. Not resubmitted. Needs a human to (a) submit the request fresh and (b) click the resulting verification link within 7 days, in a real browser, in the same sitting.

## Steps

1. Email `privacy@cbinsights.com`.
2. A DataGrail verification email arrives. **This step cannot be completed without a browser** — the link is a client-side SPA with no visible confirmation from a plain fetch.
3. Click the verification link within 7 days or the request is silently denied and must be resubmitted from scratch.

## Gotchas

- **Email verification gate, JS-rendered, on a 7-day clock.** DataGrail's verification page cannot be confirmed or completed by a plain fetch — needs a human with a browser, and needs it promptly. A missed window doesn't degrade gracefully; it denies the request outright and resets to zero.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
