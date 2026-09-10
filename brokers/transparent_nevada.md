# Transparent Nevada

- **Opt-out:** https://transparentnevada.com/contact (web form) — see FAQ at
  https://transparentnevada.com/faq for their stated removal policy
- **Email:** ~~info@nevadapolicy.org~~ — **not sent; unconfirmed off-domain
  address, see below**
- **Method:** web_form
- **Domain:** transparentnevada.com
- **Priority: 1.**

## Status

- Current: `manual_required` (updated 2026-09-09)
- Note: The registry carried `info@nevadapolicy.org` as the contact,
  sourced from a removal-service directory rather than the broker's own site,
  flagged from the start as needing confirmation before sending a full
  identifier set to a domain the site itself never names. Checked directly
  this session: `transparentnevada.com/about/` describes the site only as "a
  public records platform that collects, organizes, and publishes official
  government salary and pension data" with **no mention of Nevada Policy
  Research Institute or nevadapolicy.org anywhere** on the about or contact
  pages. The relationship the registry guessed at is not confirmed by the
  site, so the email was **not sent** — sending a full name/DOB/address/phone
  set to an unconfirmed third-party domain on the strength of a directory
  listing is exactly the mistake `CONTRIBUTING.md` warns against.

## Steps

1. The site publishes its own contact route: `transparentnevada.com/contact`
   is a web form (name, email, subject, message; "1–2 business days"
   response), not an email address. This needs a human with a browser — not
   yet attempted.
2. The contact page points to an FAQ (`transparentnevada.com/faq`) that
   references a removal/change process for records, but the FAQ content is
   JavaScript-rendered and did not return actual text on a plain fetch — a
   human needs to read it directly before drafting the request, since the
   site's own stated removal criteria (if any) should shape the ask.

## Gotchas

- **Do not resurrect `info@nevadapolicy.org`** without independently
  confirming Nevada Policy Research Institute actually operates this site —
  the site itself makes no such claim anywhere checked so far.
- FAQ content requires a real browser to read; a plain HTTP fetch returns an
  unrendered "Loading…" shell.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
