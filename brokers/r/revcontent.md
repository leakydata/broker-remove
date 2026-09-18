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

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@revcontent.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** RevContent, LLC
- **Registered address:** 1680 Fruitville Rd, Ste 400, Sarasota, Florida,
  34236
- **Filed contact email:** privacy@revcontent.com
- **Filed phone:** 941-225-6132
- **Website:** https://www.revcontent.com

*Source: `data/registries/registry.csv`.*

## If they ignore you

Work down this list. Each rung costs them more than the one above it.

1. **Reply in the existing thread** after the statutory deadline. California
   allows 45 days for a deletion request (Cal. Civ. Code 1798.130), extendable
   once by a further 45 with notice. Quote the date you first wrote.
2. **Write to the legal entity at the registered address above**, by post, if
   email has failed. A letter to the address of record is harder to lose than a
   support ticket, and it establishes a paper trail.
3. **Complain to the California Attorney General**, who administers the data
   broker registry: <https://oag.ca.gov/contact/consumer-complaint-against-business-or-company>.
   A broker's registration is what obliges it to answer; a complaint referencing
   the registry entry is the pressure point.
4. **Complain to the FTC**: <https://reportfraud.ftc.gov>. Useful for a pattern
   of non-response rather than a single case.
5. **Your own state Attorney General.** Many states with no comprehensive
   privacy statute still have consumer-protection powers and will take a
   complaint about a business that ignores its own published policy.

**What not to bother with:** phoning a support line to argue. The person who
answers cannot change the policy and did not write it. The registry entry, the
statutory deadline and the regulator are what actually move a company.
