# Dstillery, Inc.

- **Email:** privacy@dstillery.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** dstillery.com
- **Priority: 2.**

## Status

- Current: `email_pending` (updated 2026-08-28)
- Reference: `gmail:1a04146b00c89bdc`
- Note: 2026-08-27: first contact. Tailored to a behavioural-audience adtech business, where a name search correctly returns nothing while the record persists: hash the twelve addresses themselves rather than concluding no-match from plaintext; delete the EDGES joining a hashed email to a cookie, device or household ID, not only the identifier rows; treat MODELLED attributes - segments, propensity and affinity scores, predicted interests - as in scope for deletion rather than suppression from outbound use, since they exist nowhere else and are acted on whether or not accurate. Also asked which of the two lists any retained suppression hash sits on.
- Update 2026-08-28: Their reply misclassified the request as coming from an "Authorized Agent" (a business submitting on someone else's behalf) — an automated classifier false-positive, since the original letter states plainly "I am the consumer... not an authorized agent". Replied asking for reprocessing as a direct consumer request rather than being routed through agent-verification (which asks for things like enacting Global Privacy Control, a mechanism for acting on someone else's browser).

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

**Watch for the Authorized Agent misclassification.** Dstillery's intake system
can flag an ordinary first-person letter as coming from an agent acting for a
third party — plausibly triggered by specific phrasing (a long identifier
list, formal request-letter structure) rather than anything about the sender.
If it happens, don't argue the classification in the abstract — state plainly
"I am the data subject, not an agent" and ask for reprocessing as a direct
request. Cite back their own dsarwebform link and offer to resubmit through
it marked as yourself.

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
