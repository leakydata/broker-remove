# Intent IQ LLC

- **Email:** privacy@intentiq.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** intentiq.com
- **Priority: 2.**

## Status

- Current: `failed` (updated 2026-09-05)
- Note: OPT-OUT LINK IS BROKEN AT BOTH ENDS, 2026-09-05. Intent IQ replied from privacy@intentiq.com with a button, 'Click to opt-out of this email address being shared, sold or used for targeted advertising'. Two defects. (1) THE HREF CONTAINS A RAW CONTROL CHARACTER: the URL in the HTML source is ...ProfilesEngineServlet?at=7&mi<0x10>&email=...&emailVoucher=..., with a literal DLE byte where the mi parameter's value should be. That is in the message as they sent it, not an artefact of reading it. (2) THE SERVLET ANSWERS 200 WITH A REDIRECT HEADER: every request to it returns HTTP 200 carrying 'Location: https://www.intentiq.com/opt-out-failed'. A 200 is a success status and browsers only follow Location on a 3xx, so the two audiences see opposite things -- a person clicking the button lands on a BLANK PAGE with no message at all, while anything that follows the header (curl -L, a scanner, a link checker) is told the opt-out FAILED. Verified in the real browser as well as with curl: the tab stays on the servlet URL with an empty body. Tried the parameter three ways (mi=, mi, and mi%10 preserving the control byte); identical result each time, so the control character is not the discriminator. WHETHER THE OPT-OUT WAS RECORDED CANNOT BE DETERMINED FROM OUTSIDE, which is why this is failed and not submitted -- and note that a consumer who clicks once and sees a blank page has no way to tell either. Writing to them. This is the third distinct success/failure disagreement found today, after AddressSearch's HTTP 500 behind a success page and Juicebox gating an opt-out on a verification email.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
