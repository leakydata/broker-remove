# Customer Communications Group, Inc.

- **Email:** ccgprivacy@customer.com (bounced 2026-08-25 — no replacement found)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** customer.com
- **Priority: 2.**

## Status

- Current: `failed` (updated 2026-09-03) — re-classified from `unreachable`; see below
- Note: 2026-08-25: emailed ccgprivacy@customer.com. Direct-marketing services, so deletion-vs-suppression leads and both chain directions are asked for. Included the processor fallback (name the clients so I can approach them; confirm suppression regardless) and the LinkedIn suppression ask.
- Note: 2026-08-25 (later same day): that letter bounced ("address not found").
  customer.com itself was unreachable on every attempt (503 / connection failure)
  during follow-up research, so the company's own privacy page could not be
  checked. The CA data broker registry (oag.ca.gov/data-broker/registration/546651)
  lists the same bounced address as current, so it is not simply a stale
  registry entry. Registered office: 12081 W. Alameda Parkway #500, Lakewood,
  CO 80228 — worth a postal fallback if the site comes back up and still
  publishes nothing usable.

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
