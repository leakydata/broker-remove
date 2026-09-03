# Adrea Rubin Media, Inc. dba Calibrant Digital

- **Email:** info@adrearubin.com — **the sibling's address; calibrant.com itself has no mail server, see below**
- **Email fallback (dead):** jennifer@calibrant.com — bounced, connection timeout
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** calibrant.com (dead for mail — see below); using adrearubin.com's contact instead
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-09-03)
- Note: 2026-08-26: the 2026-08-24 send to jennifer@calibrant.com has been
  bouncing with a connection timeout for 2 days (still inside Gmail's retry
  window). Checked calibrant.com directly: it now serves a **parked domain
  page** ("protected by copyright spaceship.com", a domain registrar's default
  placeholder) with no privacy policy, no contact email, nothing related to
  Calibrant Digital at all. The domain has almost certainly lapsed and been
  re-registered by someone else. Treat this as the same failure mode as
  `crawlbee.md` — do not trust this domain for a `privacy@<domain>` guess going
  forward. No alternate contact found; the only registered address is
  jennifer@calibrant.com, now unreachable at the source.
- Note (2026-08-31): Retry window closed with a final hard failure ("recipient
  server did not accept our requests to connect"). `email_verified` corrected
  from `ca_data_broker_registry` to `bounced`. Confirmed via a fresh fetch that
  calibrant.com still serves the domain-parking page — the lapse is real, not
  transient, and no alternate contact exists for either sibling entry.

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


## Covered by the Adrea Rubin Marketing letter

One letter addressed to both entities' registered contacts. See
`adrea_rubin_marketing.md` for the reasoning and the asks. If they reply
confirming the two are unrelated, split the threads and treat this separately.

**Correction (2026-09-03):** the current send is again one combined letter to
`info@adrearubin.com`, covering both brands — see `adrea_rubin_marketing.md`
for the full account of where that (unverified, third-party-sourced) address
came from and why it was tried despite this file's own prior recommendation
to stop. calibrant.com's parked-domain status is unchanged and still worth
treating as possibly re-registered by a stranger — do not derive any contact
from that domain directly.
