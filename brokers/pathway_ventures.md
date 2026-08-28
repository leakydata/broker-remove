# Pathway Ventures, LLC

- **Email:** ~~privacyofficer@indivizio.com~~ — **hard-bounces 550, do not use.** It
  is the address in their own California registry filing; the domain behind it
  does not exist.
- **Method:** email — no working route found.
- **Domain:** indivizio.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-28)
- Note: 2026-08-28: The 2026-08-27 first-contact letter looked like a normal submission and was logged `submitted` — it had in fact hard-bounced the same day (550, address not found). `indivizio.com` has **no A record at all**: the domain does not resolve, so there is no site to read for an alternative address and no route of any kind. Registry has no other notes on Pathway Ventures / Indivizio, so there is no clue what the business actually does either.

## Steps

No route exists. The registered contact domain does not resolve, so nothing was
ever, and can currently be, delivered. If the domain is ever reinstated, or a
successor entity files a later state registration under the same legal name,
re-run `scripts/check_email_domains.py` and the route reopens.

## Gotchas

**A bounced send can still get logged `submitted`.** This entry was marked
`submitted` on the same day the letter hard-bounced — the send succeeded, the
delivery didn't, and nobody checked the bounce folder before recording the
status. Check `check_email_domains.py` (or just resolve the domain) *before*
spending a send on an entry sourced only from a state registry filing — a
filing records an address at the time it was made, not that the domain still
exists.

## Verification

Nothing to verify. Re-check the domain periodically; a dead domain can mean a
lapsed registration, a wound-up company, or a rebrand that left the filing
behind, and only the last of those reopens.
