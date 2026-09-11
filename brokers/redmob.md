# Redmob

- **Email:** privacy@redmob.io (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** redmob.io
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-09-10)
- Note: 2026-08-30 Sent the AD TECH variant to privacy@redmob.io (mobile advertising). Same identifier set as other ad-tech letters this batch: cookie IDs, MAIDs, hashed email, audience segments.
- **Reply (2026-09-10):** "we do not process personally identifiable information such as names, surnames, or email addresses… unable to identify the person" — the standard ad-tech "wrong key" deflection, pointing to a cookie-based opt-out in Section 4 of their privacy policy.
- **Rebuttal sent (2026-09-10):** their own policy lists MAIDs (GAID/IDFA) and CTV device identifiers as held categories, but the opt-out they offered is a **browser cookie** — a namespace that cannot express a preference about a mobile advertising ID or a television at all. Asked four things: (1) does the cookie opt-out actually join to the MAID/CTV records behind the scenes, or is it cosmetic; (2) what is the CTV opt-out mechanism, since there's no browser or advertising-ID reset on most televisions; (3) do they hold hashed (MD5/SHA-256) email identifiers or LiveRamp/ID5/UID2-style derived IDs — cited Criteo's same-day plaintext-email deletion as proof this is an architectural choice, not an industry constraint; (4) does resetting the GAID/IDFA sever their linkage to the old identifier, or does the profile re-associate at the next bid request. None of these three questions requires them to locate the sender in their systems.
- Their next reply arrived **blank** (no text, no attachment) — flagged and a resend requested. No answer yet as of 2026-09-11.

## Gotchas

**"We can't identify you from a name/email" and "we hold nothing about you" are different claims, and ad-tech companies routinely let the first one imply the second.** Redmob's own privacy policy discloses MAIDs and CTV identifiers as held categories in the same document that says it can't process names or emails — both can be true at once. The useful move is not to supply the device identifier (that recreates the exact linkage being contested) but to ask whether their *published opt-out mechanism* actually reaches the *categories they say they hold*. Here it plainly doesn't: a browser cookie cannot touch a GAID or a CTV box.

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
