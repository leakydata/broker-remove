# Locate Friend

- **Method:** unknown — Route not yet established.
- **Domain:** locate-friend.com
- **Priority: 1.**

## Status

- Current: `submitted` (updated 2026-09-06)
- Reference: `gmail:1a078a9dded1005b`
- Note: OPT-OUT FORM IS UNREACHABLE BY CONSTRUCTION; wrote to support@locate-friend.com instead, 2026-09-06. Address was obfuscated on their contact page by Cloudflare and decoded from the data-cfemail attribute. THE CHAIN, in the order it was walked: (1) full-name search returns 'No results were found'; (2) that nil is meaningless, because the search does not index first names -- a surname query returns surname BUCKETS, [PERSONAL] 64,448 / [PERSONAL]ON 367 / [PERSONAL]JR 156; (3) the only path to an individual listing is browsing /names/J/JON/[PERSONAL] and paging through sixty-four thousand entries, and that page returns a Cloudflare interactive challenge; (4) submitting the opt-out form anyway with name, email and an explanation returns one validation error -- 'The people id field is required.' people_id is a HIDDEN field populated by clicking a listing. It cannot be typed, guessed or looked up. Not a refusal, not a verification wall, not bot detection aimed at the consumer: it is the second half of a click-this-listing-then-report-it flow that somebody also linked from the nav bar as a standalone page, where the first half never runs. NEARLY RECORDED AS not_found ON THE FALSE NIL -- the same evidence shape that criminalregistry was legitimately closed on an hour earlier. Establish what a search indexes before believing what it returns. See SILENT_FAILURES 383 and 380. WHAT WAS SENT: the removal request on name, email and location with a promise to close the matter on an unqualified nil; the chain above; and two fixes -- make people_id optional for requests arriving at /optout directly, or index first names. Also flagged, separately and without going looking: their first POST returned an unhandled Laravel exception page to an anonymous visitor, full stack trace, framework and PHP versions, thirty-one vendor frames with paths and line numbers. APP_DEBUG is on in production, on their privacy page. Told them to turn it off; not reported anywhere else. The three refusals were stated: no account, no government ID, no SSN. NOTE FOR ANY REPLY: two POSTs were made to /optoutnow during testing, so a duplicate may exist on their side; both failed the same validation, so probably neither was recorded.

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
