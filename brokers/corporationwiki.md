# Corporationwiki

- **Opt-out:** https://www.corporationwiki.com/profiles/public
- **Method:** web_form — Web form.
- **Domain:** corporationwiki.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-09-02)
- Note: corporationwiki.com returns 410 GONE on every path tried (home, /profiles/public, /contact) and 520 on the apex, while DNS resolves to Cloudflare and MX points at Google Workspace. So the mail tenant is live but the SITE IS DELIBERATELY SERVING GONE -- 410 is not a 404: it is the status a server returns to say a resource has been intentionally removed and will not return. No opt-out form is reachable and no contact address is published anywhere I can read. Row had only an optout_url (/profiles/public) and no email. Not guessing a mailbox at a company whose site has been withdrawn: the letter would carry a full identifier set to an unverified address. Re-check later -- a live MX behind a withdrawn site is the succession signature from 163, so this may be a rename rather than a closure.

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
