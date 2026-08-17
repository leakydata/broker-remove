# ReHold

- **Opt-out:** https://rehold.com/optout
- **Email:** support@rehold.com (verified)
- **Method:** web_form — Web form.
- **Domain:** rehold.com
- **Priority: 3.**

## Status

- Current: `unreachable` (updated 2026-08-17)
- Reference: `gmail:1a006814404c044f`
- Note: HARD BOUNCE - DNS failure: 'the domain rehold.com couldn't be found'. Not a bad mailbox; the domain itself does not resolve. Site appears defunct. Distinct from a 550 (address not found) which means the domain lives but the mailbox does not.

## Steps

1. Email `support@rehold.com`. It hard-bounces immediately.
2. Read the bounce text, do not just note that one arrived: *"the domain
   rehold.com couldn't be found"*. That is a DNS failure, not a mailbox failure.
3. Mark `unreachable`, set `email_verified=false`.

## Gotchas

The bounce names the domain, not the mailbox, and that single word decides the
classification:

> *"the domain rehold.com couldn't be found"*

A `550 address not found` would mean the company is alive and the address is
wrong — worth hunting for a second contact. This means there is no company left
to write to at this name. The site appears defunct.

Worth being precise about, because both arrive as "a bounce" and one of them is
a to-do while the other is an ending. See `officialusa.md` for the same failure
arriving in a slower and more confusing form, as a 48-hour retry that never
resolves into a verdict.

**Do not delete the record.** A defunct broker's data does not evaporate; it gets
sold, and the domain may reappear under a new operator. Keeping the entry with
its evidence means a reappearance is recognised rather than met as a new
discovery.

## Verification

dig +short A rehold.com

While that stays empty there is nothing to verify and nothing to chase. If it
resolves again, treat the site as new: re-check the index, and re-file.
