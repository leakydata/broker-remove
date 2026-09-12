# Data Direct Marketing

- **Email:** info@datadirectmarketing.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** datadirectmarketing.com
- **Priority: 2.**

## Status

- Current: `failed` (updated 2026-08-17)
- Note: Published contact address hard-bounced (550, address not found). No alternative address published on the site — privacy and contact pages carry no email, or carry only the bounced address. Domain and MX resolve, so the domain is live and the mailbox is not. No usable email route; registry marked email_verified=false.

## Steps

1. Email the published address. It hard-bounces with a 550, "address not found".
2. Confirm what kind of failure it is before concluding anything:
   `dig +short MX <domain>` and `dig +short A <domain>`. Both answer here, so the
   domain is live and the mailbox is not.
3. Re-read the privacy and contact pages for any second address. There is none.
4. Mark `failed` with the bounce quoted, and set `email_verified=false` in the
   registry so the address is never silently reused.

## Gotchas

A **550 is not the same as a dead domain**, and the difference decides what to do
next. Here the domain resolves and its MX records answer — mail was accepted for
delivery and then refused by the receiving server because the mailbox does not
exist. The company is live. Only the address they publish is fiction.

That distinction matters because a dead domain means "stop, there is nobody to
write to", while a live domain with a dead published mailbox means "the route is
wrong, find another one" — and it is also the more damning of the two. Publishing
a privacy contact that bounces is not an accident of neglect in the same way a
lapsed domain is; it is a contact point offered to consumers that silently
discards what they send. Anyone who wrote to it and did not check their own
bounce folder believes a request is pending.

The site publishes no second address. Privacy and contact pages carry either
nothing or the same bounced mailbox, so there is no fallback to try.

## Verification

Nothing to verify: no request was ever delivered. Re-check the site periodically
for a working contact, and keep the bounce — a published privacy address that
does not accept mail is the substance of a regulator complaint, not a footnote to
one.
