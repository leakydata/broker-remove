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
