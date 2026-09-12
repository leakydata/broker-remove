# RevContent, LLC

- **Email:** privacy@revcontent.com (state-registry / site-published address — unverified until a reply arrives)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** revcontent.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-06)
- Reference: `gmail:1a072d91db74a830`
- Note: CLOSED 2026-09-06 on the most detailed architecture disclosure this project has received, from RevContent's Software Developer and DPO. THE HASH QUESTION IS ANSWERED, AND THE ANSWER DISSOLVES IT. The 349 objection was that a nil on twelve PLAINTEXT addresses is worthless from a company that says it stores no plaintext addresses. Their answer: they hold TWO POPULATIONS. Registered advertisers and publishers, for whom they DO hold plaintext email, phone and postal address -- 'Because this is a plaintext dataset, we search it using plaintext; running a hash match against it would yield the exact same result.' And anonymous browsers of publisher pages, for whom they hold only IP address, user-agent and the __ID cookie -- 'Because email addresses are never accessed or available for this group, we cannot perform checks based on them.' So the nil was against a real plaintext table, and a hash search over it would return the same thing. Not a self-refuting nil after all; the original letter had assumed one population where there are two. THEY ALSO HASH WHEN IT MATTERS: 'For CCPA DROP requests, we end up hashing these very email and phone numbers and comparing the hash against those provided in DROP requests.' EMAIL-WIDGET HASHES EXPLAINED AND EXCLUDED FOR A GOOD REASON: publisher-supplied hashes exist to tie a click back to a served ad, are random UUIDs that ROTATE ON EVERY IMPRESSION, live in a temporary store with a 72-hour TTL and are purged every three days, so they identify an impression rather than a person. AD SERVING WITHOUT PII: bucketing on IP-derived geo and user-agent-derived device class, no email or phone retargeting; data shared with third-party DSPs limited to IP, user-agent and __ID. RETENTION: 90-day event logs for stat regeneration, audit and fraud, then purged; on deleting a registered user they keep user_id and transactional totals and redact the underlying PII so ledgers stay accurate. THEY ALSO OWNED A MISTAKE: the stray third-party address in their first reply was, in their words, 'entirely my fault' -- a template reused from a previous ticket with an old hyperlink left attached -- with an apology and safeguards promised. Recorded not_found rather than confirmed: nothing of the subject's was found and the remaining population is reachable only by submitting IP, user-agent and cookie ID through their form, which the standing rule refuses because it would attach a name to identifiers that currently have none. That is a declined route, not a failed one. Thread closed by the other writer on this mailbox at 10:17 UTC; no further reply needed.

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
