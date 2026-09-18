# Sawyer Lists, LLC

- **Email:** ~~admin@sawyerdatadirect.com~~ — **hard-bounces 550, do not use.** It is
  the address in their own California registry filing; the mailbox does not exist.
- **Method:** email — no working route found.
- **Domain:** sawyerlists.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-28)
- Note: Recovered from the committed playbook brokers/s/sawyer_lists.md, because the ledger carries no notes and this row's status had no evidence behind it: 2026-08-28: The 2026-08-26 send to admin@sawyerdatadirect.com looked like a normal submission and was logged `submitted` — it had in fact hard-bounced the same day (550, address not found). Checked both domains behind this listing: `sawyerlists.com` (the company's own domain, per the registry filing) has no DNS record at all — it does not resolve. `sawyerdatadirect.com` (the contact-address domain) does resolve, but serves a GoDaddy parked-domain lander page (`traffic_target=gd`, `lander_type=parkweb`), not a real site — no privacy policy, no contact page, nothing to read for an alternative address. Two domains, one dead outright and one a placeholder wearing a live A record. No route currently exists.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Sawyer Lists, LLC
- **Registered address:** 2910 E. 57th Ave, Ste 5-135, Spokane, WA 99223,
  United States
- **Filed contact email:** admin@sawyerdatadirect.com
- **Website:** http://www.sawyerlists.com
- **Opt-out route they filed:** Go to www.sawyerlists.com or call
  800-327-3595
- **Route for protected individuals:** Go to www.sawyerlists.com or call
  800-327-3595 (Cal. Gov. Code 6208.1(b) / 6254.21(c)(1) — for survivors
  of domestic violence, stalking and similar, a stronger and faster route
  than the ordinary consumer request)

*Source: `data/registries/complete-reg-data-brokers.csv`.*

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
