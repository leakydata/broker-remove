# Old Friends Co

- **Email:** info@old-friends.co (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** old-friends.co
- **Priority: 1.**

## Status

- Current: `submitted` (updated 2026-11-19)
- Note: 2026-11-19 Burch (Old-Friends) asked for a screenshot of the reCAPTCHA before processing. Today the class page loaded with no CAPTCHA and the entry's Opt out / Remove Name form (remove.php) was reachable. Filled it (email, reason Privacy, no-re-import comment); left the 'I certify that I am...' box and Submit for the user per the no-certification rule. Replied that no CAPTCHA appeared, so there is no screenshot, and asked them to remove the entry directly from the email request.
- Earlier: 2026-11-16 Old-Friends replied with a form answer: click your name on the class page and use Remove. Found the matching class-list entry (prior-town high school, class year consistent with the date of birth). The class page sits behind a reCAPTCHA, so replied in-thread naming the exact entry and asked them to remove it and block re-import. User fallback is in the handoff queue.
- Earlier: 2026-11-16 Drove the site in a real browser (the cookie bot check cleared on its own). No privacy form; used Help > Contact Us > 'open a support ticket' (Birchwood Media). Asked for deletion, opt-out of sale/sharing and suppression against later class-list imports, searching name variants, four emails and past towns; answer by email. Page: 'Your question has been queued... typically within 48 hours.' No CAPTCHA was shown.
- Earlier: NOT UNREACHABLE -- THE SITE IS LIVE BEHIND A BOT CHALLENGE. old-friends.co returns HTTP 200, but the effective URL after redirects is /fn/botCookieChallenge.php?r=%2F&vid=... -- a cookie-based bot challenge, which a script cannot pass and a browser clears invisibly. So the server is up and serving; only automated access is refused. /privacy, /privacy-policy, /opt-out and /optout all 404, so whatever privacy route exists is not at a guessable path and must be found from the rendered page. Moving to manual_required rather than unreachable. Previously an adopted ledger line from 2026-10-06 -- only four days old, which makes the point sharper: this was not a stale record going bad over months, it was MISREAD AT THE TIME, because a bot challenge looks exactly like a broken site from a script.

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
