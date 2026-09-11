# Possiblenow

- **Email:** privacy@possiblenow.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** possiblenow.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Autoresponder, but a revealing one. Three findings. (1) THE OPT-OUT LINK IN THEIR OWN AUTORESPONDER IS DEAD: it points at site.possiblenow.com/do-not-sell-my-personal-information, which 404s onto what looks like a hosted knowledge base - the page title is 'How do I set up an NPS survey?'. The working page is the same path on www. One wrong subdomain, in the automated reply a consent-management company sends to every privacy request. (2) A CAPTCHA gates the form BEFORE the fields are shown - 'Verify & Continue to Form' - so nothing can be pre-filled or even inspected without solving it. (3) 'If you have multiple addresses or email addresses, please submit a separate request for each.' With 16 addresses and 12 emails that is 28 submissions, each behind its own CAPTCHA. Recorded as submitted on the EMAIL route, which is the substantive one: the letter asked them to KEEP suppression records and delete everything else, and a per-identifier do-not-sell form cannot express that distinction at all. Their reply confirms email is not foreclosed - 'We will respond to your questions or concerns in a timely manner.'

## Correction (2026-08-27): a duplicate second letter was sent to a sibling address

A separate registry row (`possiblenow` in `data/curated_brokers.json`, `email_to`
`californiadrop@possiblenowmarketing.com` — note `possiblenowmarketing.com`, not
`possiblenow.com`) was picked as a "fresh" batch candidate and emailed the same
day this playbook was written up, without checking this file first. It is the same
company under a second CA-registered brand address, already `submitted` above
since 2026-08-19.

**Lesson, restated from the AcademixDirect playbook because it just repeated
itself with a different broker:** diffing Gmail Sent against a domain list is not
a substitute for reading each candidate's own playbook `Current:` status before
sending. A domain-only diff misses a second registered address for the same
company on a sibling domain. `queue_batch.py`'s "spoken-for address" and
duplicate-family logic exists precisely to catch this and was not used for this
batch — `data/removal_status.json` doesn't exist in a fresh clone, so the script
has nothing to check against, and a manual domain diff is a weaker substitute.
No harm beyond one redundant email; recorded here rather than treating the
second thread as a new, unrelated submission.

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
