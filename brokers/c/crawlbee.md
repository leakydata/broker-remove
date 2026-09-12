# CrawlBee Corp

- **Email:** privacy@crawlbee.com (bounced 2026-08-25 — domain no longer theirs)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** crawlbee.com — **do not trust this domain going forward.** It now
  redirects to a GoDaddy "domain for sale" parking page, confirmed 2026-08-25.
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-25)
- Note: 2026-08-25: bounced - 'the domain crawlbee.com couldn't be found'. Diagnosis: crawlbee.com publishes a NULL MX (RFC 7505: a lone '0 .' record), which is the domain owner stating explicitly that it accepts no mail. It still serves an A record and its SOA is ns2.afternic.com - an domain marketplace - so the domain is parked for sale and the company is likely defunct. THIS EXPOSED A BUG IN check_email_domains.py, now fixed: the checker returned True on any MX record present, so a null MX read as deliverable. That is worse than a missing record, because the send is refused immediately, the broker gets marked submitted, and nobody learns the letter never left.

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
