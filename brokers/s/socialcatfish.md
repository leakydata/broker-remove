# Socialcatfish

- **Method:** unknown — Route not yet established.
- **Domain:** socialcatfish.com
- **Priority: 1.**

## Status

- Current: `manual_required` (updated 2026-09-06)
- Note: ROUTE FOUND AND FULLY MAPPED; NEEDS A BROWSER TO SUBMIT. socialcatfish.com/opt-out/?id=request_optout was discovered 2026-09-05. CORRECTION TO A FIRST READ: an earlier glance at the page's fields showed an email-and-password pair and I took the opt-out to be behind a login. It is not -- that is a site-wide login modal, and the opt-out is a separate form, id=request_optout_form, posting to /opt-out/?id=request_optout#step2. No account is required. FIELDS: firstname, lastname, email, and ccpa_url[] ('Enter profile URL here'), with an optional expandable section for ccpa_middle_name, ccpa_age as a RANGE (the subject falls in 45-53), ccpa_emails[] and ccpa_phones[], each repeatable, plus an image upload. Not submitted from a script: the submit control and csrf_token are injected by JavaScript and are not in the served markup, so a blind POST would be exactly the unverifiable submission today's failures warn about. Two browser attempts ended with the extension refusing script injection on this 245KB page. THEIR POLICY IS BETTER THAN MOST AND DESERVES SAYING SO: 'If you are a California, Colorado, Connecticut, Florida, Nevada, Oregon, Texas, Utah, or Virginia resident you may have specific rights related to privacy requests. However, Social Catfish is committed to extending the highest level of privacy rights offered under U.S. law to all U.S. residents. As such, we accept and honor requests from residents of all U.S. states.' That is the exact opposite of the state-gating seen at Whitepages and noon.ai -- they name the states with statutes and then explicitly decline to use that list to narrow who they will help. They also commit to a fifteen-day deadline. Pennsylvania residency is therefore not an obstacle here.

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
