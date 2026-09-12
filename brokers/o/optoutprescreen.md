# OptOutPrescreen (credit offers)

- **Opt-out:** https://www.optoutprescreen.com/
- **Method:** web_form — Web form.
- **Domain:** optoutprescreen.com
- **Priority: 4.**

## Status

- Current: `manual_required` (updated 2026-09-08)
- Note: CORRECTION, SAME DAY, TO THE ENTRY DIRECTLY ABOVE THIS ONE. That entry said this row had 'NO STATUS -- never written to' and was 'invisible until today'. Both are false. It has been in the handoff queue since 2026-08-29 as item 74, with the SSN requirement already established as fact ('the form requires a SOCIAL SECURITY NUMBER'), both routes described, the permanent postal option identified as the stronger one, and a caution I had not thought of -- that a site asking for an SSN is exactly the shape a lookalike phishing domain imitates, so the URL should be verified independently before anything is entered. My replacement item would have been a REGRESSION and handoff.py's duplicate guard refused it. WHAT I READ WRONG: I queried removal_status.json for rows with no status, found this one, and concluded the project had never touched it. The project had; the record lived in data/handoff_queue.json. Three stores hold state here -- the ledger, the registry, and the queue -- and no one of them is the project's memory. THE ONE GENUINELY NEW FACT, kept because it is small and true: the URL returns HTTP-403 to a plain fetch and 200 with a real form to a browser-shaped header set, so automated route checks have been recording this route as blocked when it is not. Only 4 of 65 403s behaved that way. See _SILENT_FAILURES 429.

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
