# Verinext

- **Email:** dpo@verinext.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** verinext.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: Emailed dpo@verinext.com. Verinext's own site describes an IT consulting / digital-transformation firm (cloud, data protection, automation, security, AI implementation) — another likely false positive on the broker list it came from.
- **Note (2026-09-03): a second copy of the same request landed here** via the `anexinet` row — Anexinet rebranded to Verinext, its own registered address hard-bounced, and a bounce-correction pass resent to this same dpo@verinext.com without checking this row existed first. Harmless duplicate; see `anexinet.md` for the full account. `anexinet` is now marked `covered_by_sibling` pointing here.
- **Note (2026-09-06): the 2026-09-03 duplicate send itself bounced** — 550 5.4.1 "Recipient address rejected: Access denied" (Exchange Online), same failure code Anexinet's own address gave. Recorded in `data/dead_addresses.json` as `rejected_ambiguous`, deliberately NOT `no_such_mailbox`: this is the address verinext.com's own privacy policy names as correct (Section 13, "Contacting Us"), confirmed independently by a fresh fetch of that page, and the *original* 2026-08-20 send to the identical address produced no bounce at all. Two sends, one silent success and one hard rejection, is the signature of a server filtering a repeat-looking sender rather than a dead mailbox. Do not send a third letter here — the 8/20 request is presumed in flight — and do not mark this row unreachable on the strength of one ambiguous rejection.

## Steps

1. Email `dpo@verinext.com` — a named DPO address, which is usually a live
   route even at firms with no consumer-facing privacy program.
2. Use the "professional-services" short letter (see
   `brokers/_CATEGORY_VARIANTS.md`): say plainly a "no records outside a
   business relationship" answer is complete, and concede any retention
   obligation up front.

## Gotchas

Same pattern as `td_cowen.md` — an IT services vendor holding client and
vendor contact data under a business relationship, not a data broker with a
consumer-facing product. Don't escalate the ask; the honest answer here is
very likely a negative.

## Verification

No public profile to search. A written negative is the expected and complete
outcome.
