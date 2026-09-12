# Car Market Solutions LLC

- **Email:** ben@carmarketsolutions.com (BOUNCED — see below)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** carmarketsolutions.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-28)
- Reference: `gmail:1a037f72af328936`
- Note: PERMANENT FAILURE 2026-08-28 after three days of retries, and the failure mode matters: status 4.4.1, 'the recipient server did not accept our requests to connect [carmarketsolutions.com. 200.225.43.10: timed out]'. This is a CONNECTION failure, not a mailbox failure. Every cheap check passes -- the domain resolves, publishes an MX (self-pointing) and an A record -- and nothing is listening on port 25; a direct TCP connect to 200.225.43.10:25 times out. So unlike the 550s in dead_addresses.json, this says NOTHING about whether [named individual]@carmarketsolutions.com exists. The address is on their California registry filing and is person-shaped. Recorded as unreachable rather than failed (nothing was refused) and flagged as worth one retry if their mail server is ever seen to answer -- the evidence condemns the server, not the address.

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
