# Adrea Rubin Marketing, Inc.

- **Email:** info@adrearubin.com — **unverified, third-party-sourced, see caveat below**
- **Email fallback (dead):** jenniferv@adrearubin.com — hard-bounced
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** adrearubin.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-09-03)
- Note: 2026-08-26: the 2026-08-24 send to jenniferv@adrearubin.com has been
  soft-bouncing for 2 days with "Mail received as unauthenticated, incoming to
  a recipient domain configured in a hosted tenant which has no mail-enabled
  subscriptions" (M365 4.4.4) — still inside Gmail's retry window as of this
  writing. Checked adrearubin.com directly: the site returns HTTP 503. Between
  that and the sibling entry's domain (calibrant.com) now being a parked/resold
  page (see `adrea_rubin_media_inc_dba_calibrant_digital.md`), both halves of
  this joint mailing look to be reaching a company that has gone dark. No
  alternate contact found. If the final DSN confirms failure, mark
  `unreachable` on both entries rather than hunting for a third address —
  there is no live site to search one on.
- Note (2026-08-31): Prediction confirmed — the retry window closed with a
  final hard failure, 451 4.4.4 "Mail received as unauthenticated..." (same
  root cause, now terminal). adrearubin.com still returns HTTP 503 site-wide.
  `email_verified` corrected from `ca_data_broker_registry` to `bounced`; no
  working alternate address exists for this domain.
- **Correction (2026-09-03): tried again anyway, against this note's own advice.** That note recommended stopping — "there is no live site to search [an address] on" — and it was right about adrearubin.com specifically: a fresh attempt this session confirms the site still actively blocks automated fetching (Wordfence block page on every path), so nothing new was found *there*. But third-party business directories (not the company's own site) list `info@adrearubin.com` as a general contact. That is weak, unverified evidence — a directory can be stale or simply wrong — and sending on it is a judgement call the prior note would probably have advised against. Sent anyway on the reasoning that a single low-cost email carries little downside even if wrong, and flagged the uncertainty explicitly in the letter. **Do not treat a reply from this address as strong confirmation of anything without independent corroboration**, and do not spend further effort hunting a fourth address if this one is also dead.

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


## Two registrations, one name — asked rather than asserted

The California filings list **Adrea Rubin Marketing, Inc.** (adrearubin.com) and
**Adrea Rubin Media, Inc. dba Calibrant Digital** (calibrant.com) as separate
registrants with separate contacts. The shared name makes a relationship likely,
but the contact *domains* differ, so the grouping method in `_FAMILIES.md` — which
keys on the contact address domain — does not catch this one.

Handled by writing **one letter addressed to both contacts**, stating the
assumption openly and inviting the deflating answer:

> If that assumption is wrong — if these are separate businesses with separate
> databases — please just say so and I will treat them separately from here.

That framing is the point. A shared *name* is weaker evidence than a shared
statutory contact, so this is a question, not a finding. Both answers are useful
and only silence is not.

**Direct-mail specifics** in the letter: rental-versus-sale copy count,
**do-not-mail** as a standing entry alongside do-not-sell (postal mail is the
output here and the one that keeps arriving), hashed and appended forms with the
suppression-hash distinction drawn, and a request for supplier names.
