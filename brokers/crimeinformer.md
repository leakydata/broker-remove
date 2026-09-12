# CrimeInformer

- **Opt-out:** none found
- **Email:** ~~support@crimeinformer.com~~ — **hard-bounces 550 "No such user"**
- **Method:** email (guessed — unverified) — do not reuse
- **Domain:** crimeinformer.com
- **Priority: 2.** Background-check / people-search style listing.

## Status

- Current: `unreachable` (2026-09-12)
- Note: A consumer request sent to `support@crimeinformer.com` hard-bounced.
  The domain resolves in DNS (199.103.62.205 — the mail server is rejecting
  the mailbox, not refusing the connection), but every page fetched
  automatically — the site root, `/privacy-policy`, `/contact-us` — returned
  HTTP 404. That's inconsistent with a genuinely dead site (a resolving
  domain with a working mailer usually serves *something*), so the more
  likely explanation is bot-blocking rather than total abandonment.

## Steps

1. Do not resend to `support@crimeinformer.com` — confirmed dead mailbox.
2. **Needs a human with a real browser.** Load `crimeinformer.com` directly
   and see what's actually there — a live site with a different contact
   page, a parked domain, or a bot-detection wall that only blocks
   automated fetches. Whatever's found determines the next move; guessing a
   second address without seeing the real site would repeat this mistake.

## Gotchas

- No privacy policy, contact page, or opt-out form was reachable by
  automated fetch — nothing here to say who runs this site, whether it's
  part of a larger network, or what the CCPA/state-privacy posture is.

## Verification

Nothing submitted. Re-check once a human confirms whether the site is live.
