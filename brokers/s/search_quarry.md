# Search Quarry

- **Opt-out:** https://members.searchquarry.com/terms?tab=optout
- **Email:** privacy@searchquarry.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** searchquarry.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-07)
- Reference: `searchquarry.com 'Database updated as of 09/06/2026'`
- Note: RE-VERIFICATION ATTEMPTED 2026-09-07 AND INCONCLUSIVE, but it surfaced a fact that matters more than the attempt. Their real search endpoint was discovered from their own form -- /namesearch/search with fname, lname and city -- and it returns a POLLING PAGE rather than results: 'Your Public Records Search is for [name] in ... 1% If the search is taking too long, please try searching again'. Results render in JavaScript, so no scripted verdict is possible. THE FACT WORTH RECORDING, from that same page: 'DATABASE UPDATED AS OF 09/06/2026' -- yesterday. A DAILY REBUILD. That is the durability question answered by the site itself: on an index rebuilt every day, a deletion has at most a day's shelf life unless a suppression entry persists across builds, and nothing in this row's history establishes that one does. The not_found status stands as a statement about what was published when it was checked, and no more. See SILENT_FAILURES 409. Re-verification here belongs in the batched browser handoff, not in a script.

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
