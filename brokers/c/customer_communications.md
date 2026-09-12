# Customer Communications Group, Inc.

- **Email:** ccgprivacy@customer.com (bounced 2026-08-25 — no replacement found)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** customer.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-28)
- Note: Adopted from the shared ledger: another agent recorded 'unreachable' on 2026-08-28. No detail is carried across — re-read the broker's own reply before relying on this.

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

**Re-confirmed (2026-09-03):** customer.com now actively returns 403 Forbidden (openresty) on every path tried — root, www, /privacy-policy, /contact-us, /ccpa, /do-not-sell, multiple user agents — rather than being unreachable. That distinction matters: a 403 means something is answering and choosing to block, which is a different (and less final) situation than a dead domain. Re-classified from `unreachable` to `failed` on that basis. Not in the current CPPA registry either. No alternate contact found anywhere, on-site or third-party.
