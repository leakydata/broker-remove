# Nativo, Inc.

- **Email:** privacy@nativo.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** nativo.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-09)
- Note: Emailed privacy@nativo.com 2026-08-29 (CA registry 2020-2025). Native advertising platform. Standard ad-tech concession up front (cookie/MAID/page-context keyed, so a name search returns nothing and that is a real answer), then three asks, one of which is specific to this format. (1) Identity layer: hashed emails, alternative IDs (UID2, RampID, ID5), or any device-to-person graph -- and if so, hash the twelve addresses themselves and search. (2) THE ONE THAT IS PARTICULAR TO NATIVE ADVERTISING: native measures what an individual READ and for how long, so an article-level engagement history is a materially more revealing record than an impression count -- it can indicate a health concern, a financial difficulty, a legal problem or a belief purely from which articles were opened and how long they held attention. Asked whether reading and engagement events are retained at individual or device level after a campaign ends, for how long, and whether they feed interest or intent segments; deletion asked for, and use-and-disclosure restriction asked separately. (3) Where the opt-out lives (cookie vs server-side) and whether GPC is recorded durably or honoured only in-session. Plus supplier and recipient categories. No IP and no device ID sent, reasons stated.

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

## Nativo is a Life360 brand — reply came from privacy-nativo@life360.com

**Reply (2026-09-09):** "We are confirming that we did not locate your information in our system" — a clean nil on the identity-keyed search, sent from `privacy-nativo@life360.com`. Life360 (the family-safety/location app company) evidently now owns or operates the Nativo ad platform under its own privacy program; this is worth cross-referencing against any direct Life360 entry, since a shared privacy team can mean a shared underlying data store even when the products look unrelated.

**The pseudonymous-data offer is browser-only and was not completed.** The same reply says Nativo/Life360 "may have additional 'pseudonymous' personal information about you, such as a Cookie ID, IP address, and associated reference data," and offers two routes to reach it:

1. Visit `https://ads.life360.com/legal/interest-based-ads` and click an "Opt Out" button — a client-side action that sets a cookie in the visiting browser. Not something a non-browser channel can do or verify.
2. Alternatively, retrieve the "Visitor ID" cookie stored under the `postrelease.com` domain from your own browser and email it back for a manual match-and-delete.

Both routes require a browser [FIRST] controls; neither is completable by email alone. **Do not send a cookie/Visitor ID here without deciding it's worth it** — handing over the exact identifier that links a browser to this profile is the same trade-off the letter to Nativo's own ad-tech peers argues against (see the identity-layer question in the original letter). Flagged as a browser-only follow-up for a human, not attempted.
