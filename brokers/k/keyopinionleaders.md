# Keyopinionleaders

- **Email:** privacy@keyopinionleaders.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** keyopinionleaders.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-19)
- Note: Downgraded from submitted on DNS evidence, ahead of the bounce. Gmail reported a 'Delivery incomplete... temporary problem... will retry for 45 more hours' notice, which reads as transient. It is not: keyopinionleaders.com has NO NS RECORDS, NO SOA, NO A AND NO MX, on the apex and on www alike. The domain does not resolve at all - the registration has lapsed or been withdrawn - so the retries cannot succeed and the message will hard-bounce in two days. Worth recording as its own failure mode: a SOFT bounce can mask a permanently dead domain, and for 48 hours the tracker will happily show 'submitted' while the letter has nowhere to go. One dig settles it in a second.

## Steps

1. Email `privacy@keyopinionleaders.com` with the lead-gen variant. KeyOpinionLeaders appears to be a database of healthcare-professional/key-opinion-leader contacts for pharmaceutical and medical marketing — likely irrelevant unless the subject has a healthcare-professional history, but worth confirming rather than assuming.
2. Ask who purchased or received the record if a match is found.

## Gotchas

- If the reply confirms no matching record, record `not_found` rather than treating silence or a negative as a failure — this category (KOL/HCP databases) is a plausible true negative for most subjects.

## Verification

No public listing to check. Awaiting reply as of 2026-08-18.


## Outcome: the domain is gone, and the bounce said "temporary"

Gmail reported a **delivery delay**, not a failure:

> *"Delivery incomplete. There was a temporary problem delivering your message to
> privacy@keyopinionleaders.com. Gmail will retry for 45 more hours."*

The domain has **no NS records, no SOA, no A and no MX** — on the apex and on
`www` alike. There is no zone at all. The registration has lapsed or been
withdrawn, the retries cannot succeed, and the message hard-bounces in two days.

Downgraded to `unreachable` immediately rather than waiting for the bounce.
Waiting buys nothing: the outcome is already determined, and two days of a false
`submitted` is two days in which the entry looks handled and nobody re-checks it.

See `_SILENT_FAILURES.md` §44. `scripts/verify_emails.py` now checks NS before MX
and reports this state as **`NO_DOMAIN`**, so the next lapsed registration is
caught before a send rather than after one.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Key Opinion Leaders
- **Registered address:** 1078 6th Avenue SW, Calgary, AB
- **Filed contact email:** privacy@keyopinionleaders.com
- **Website:** https://www.keyopinionleaders.com

*Source: `data/registries/registry2024.csv`.*

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
