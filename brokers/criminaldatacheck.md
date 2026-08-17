# Criminaldatacheck

- **Opt-out:** https://www.intelius.com/privacy-center
- **Email:** support@criminaldatacheck.com (verified)
- **Method:** web_form — Web form.
- **Domain:** criminaldatacheck.com
- **Priority: 2.**

## Status

- Current: `failed` (updated 2026-08-17)
- Note: Published contact address support@ hard-bounced ('address couldn't be found'), and it is the ONLY address on their site — contact page offers just a search form and that address. Domain and MX resolve, so the domain is live and the mailbox is not. Appears to be the same affiliate/lead-gen pattern as Criminal.com: funnels searches to a background-check provider rather than holding records. No usable route.

## Steps

1. Email `support@criminaldatacheck.com` — the only address the site publishes.
   It hard-bounces: "address couldn't be found".
2. Check the contact page for anything else. It offers a search form and that
   address, and nothing more.
3. `dig` the domain: MX and A both answer. Live domain, dead mailbox.
4. Read what the site actually does before assuming it holds records — see below.
5. Mark `failed`, set `email_verified=false`, and file the request against the
   provider the searches actually reach.

## Gotchas

The bounce is the visible problem; the more useful finding is underneath it.

This is the **affiliate front** pattern, the same shape as Criminal.com. The site
presents itself as a background-check service, but a search does not query a
database it owns — it funnels the visitor to a background-check provider that
does. A deletion request aimed here is aimed at a shopfront.

That has a practical consequence worth stating plainly: **a bounce from a front
site is nearly harmless, and a "we hold nothing" from one is nearly useless.**
Neither tells you anything about the records that actually exist. What matters is
which provider the funnel terminates at, and whether a request has been filed
there. Follow the opt-out link, or the destination of a search, and file against
the name you land on.

Here the searches reach the Intelius/PeopleConnect privacy center, which is
covered separately — see `peopleconnect.md`.

So: no usable route, and also nothing much lost. Record the dead address because
a published contact that discards consumer mail is worth documenting, then spend
the effort on the provider behind it.

## Verification

Nothing to verify at this domain. Verification belongs to the provider the site
funnels into: re-run a search there, on their timetable, not this one's.
