# Nymblr, Inc.

- **Email:** privacy@nymblr.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** nymblr.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-09-03)
- **Correction (2026-09-03):** the 2026-08-29 reasoning below concluded sending was safe because the mail infrastructure looked actively maintained even though the website loops — that conclusion turned out to be about the wrong signal. privacy@nymblr.com hard-bounced (no_such_mailbox) the same day it was sent, which the working MX records didn't rule out (a healthy mail *domain* says nothing about whether a specific *mailbox* exists on it). Re-confirmed today: nymblr.com and www. still loop infinitely on every path (verified independently via curl and a headless-browser fetch), so there is no way to browse to an alternate address, and the company is absent from the current CPPA registry (consistent with a lapsed filing). No alternate route found. **Lesson: a live mail domain is evidence the domain isn't dead, not evidence the specific mailbox works — only a send (or a bounce) settles that.**
- Note: Emailed privacy@nymblr.com 2026-08-29 (CA registry 2020-2023 ONLY -- lapsed, so the 163 domain check ran first). DIAGNOSIS: nymblr.com serves an infinite 301 redirect loop to itself with a zero-byte body, so the website is effectively dead -- BUT it has five Google Workspace MX records and Cloudflare-fronted A records, which is an actively maintained tenant rather than a leftover. Nobody re-registers a domain and configures Workspace plus Cloudflare in order to serve a redirect loop, so this is NOT the 157 danger case (stranger owns the domain); it is 'company still exists, website is broken, mail works'. Same shape as the earlier minerva finding. Sending is therefore safe and email is the only channel available, which the letter says explicitly so the choice is not mistaken for skipping a form -- and it asks them to name the acquirer if the data has passed to another company. Substance is the B2B contact-data variant: the derived work addresses the subject cannot list and they can generate from the public profile; enumerate title/seniority/function/employer/tenure/skills plus scores; name the sources (public profiles, crawled pages, licensed compilers, contributed address books, email-verification traffic); whether a record matching me has ever been in a DELIVERY to a customer, since contact data is sold by the record and a deletion cannot reach a delivered copy; and the B2B carve-out pre-empted.

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
