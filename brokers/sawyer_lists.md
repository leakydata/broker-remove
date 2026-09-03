# Sawyer Lists, LLC

- **Email:** ~~admin@sawyerdatadirect.com~~ — **hard-bounces 550, do not use.** It is
  the address in their own California registry filing; the mailbox does not exist.
- **Method:** email — no working route found.
- **Domain:** sawyerlists.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-28)
- Note: 2026-08-28: The 2026-08-26 send to admin@sawyerdatadirect.com looked like a normal submission and was logged `submitted` — it had in fact hard-bounced the same day (550, address not found). Checked both domains behind this listing: `sawyerlists.com` (the company's own domain, per the registry filing) has no DNS record at all — it does not resolve. `sawyerdatadirect.com` (the contact-address domain) does resolve, but serves a GoDaddy parked-domain lander page (`traffic_target=gd`, `lander_type=parkweb`), not a real site — no privacy policy, no contact page, nothing to read for an alternative address. Two domains, one dead outright and one a placeholder wearing a live A record. No route currently exists.

## Steps

No route exists. The state-registered contact address bounces, the company's own
domain has no DNS, and the fallback domain in the registry contact address is a
parked placeholder with no content. Nothing to send to and nowhere to read an
alternative from.

If either domain is ever reinstated with real content, re-check for a working
address before writing again.

## Gotchas

**A bounced send can still get logged `submitted`.** This entry was marked
`submitted` on the same day it hard-bounced — the send succeeded, the delivery
didn't, and nobody checked the bounce folder before recording the status. That
gap is exactly what this project's own inbox-first pass exists to catch.

**A live A record does not mean a live company.** `sawyerdatadirect.com`
resolves and returns HTTP 200 — but the 200 is a GoDaddy parking lander, not a
website. Check the response body, not just whether the domain resolves.

## Verification

Nothing to verify. Re-check both domains periodically for signs of a real site.

**Re-confirmed (2026-09-03):** still the same picture — sawyerlists.com has no MX and no A record at all (confirmed via DNS-over-HTTPS lookup), and every path on sawyerdatadirect.com, including /privacy-policy, client-side-redirects to the same GoDaddy parking lander. No change.
