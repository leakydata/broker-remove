# Old Friends Co

- **Email:** info@old-friends.co (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** old-friends.co
- **Priority: 1.**

## Status

- Current: `manual_required` (updated 2026-10-11)
- Note: NOT UNREACHABLE -- THE SITE IS LIVE BEHIND A BOT CHALLENGE. old-friends.co returns HTTP 200, but the effective URL after redirects is /fn/botCookieChallenge.php?r=%2F&vid=... -- a cookie-based bot challenge, which a script cannot pass and a browser clears invisibly. So the server is up and serving; only automated access is refused. /privacy, /privacy-policy, /opt-out and /optout all 404, so whatever privacy route exists is not at a guessable path and must be found from the rendered page. Moving to manual_required rather than unreachable. Previously an adopted ledger line from 2026-10-06 -- only four days old, which makes the point sharper: this was not a stale record going bad over months, it was MISREAD AT THE TIME, because a bot challenge looks exactly like a broken site from a script.

## Steps

1. **Do not email `info@old-friends.co`** — it hard-bounces (user unknown)
   despite being the only address the site publishes.
2. No alternate contact channel has been found (no contact page, no state
   registry filing). If this needs to move further, postal mail to the
   registered agent (not yet looked up) or re-checking the site after some
   time for a working address are the remaining options.

## Gotchas

- **A published address can be dead even when the site around it is current.**
  The homepage still advertises `info@old-friends.co` for support issues; the
  mailbox itself doesn't exist server-side. Don't treat "the site lists this
  address" as equivalent to "this address accepts mail" — check for a bounce
  every time, even when the source `email_verified_by` is `privacy_policy`.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
