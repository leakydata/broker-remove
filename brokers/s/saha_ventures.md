# Saha Ventures LLC

- **Email:** ops@findtrueowner.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** findtrueowner.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-26)
- Note: 2026-08-25: contact domain publishes no MX and no A record - nothing can be delivered. The broker's own domain is equally dead, so there is no alternative route by mail. Never written to; marked before spending a send. Re-check if the domain is ever reinstated.
- Note: 2026-08-26: a later run sent to ops@findtrueowner.com anyway without checking this file first, and got the expected NXDOMAIN bounce ("domain findtrueowner.com couldn't be found"). No new information — confirms the 2026-08-25 finding rather than superseding it. Left as `unreachable`. Lesson for next time: check for an existing playbook before adding a broker to a send batch, not only the ledger and Gmail Sent — the ledger had no entry for this id at all.

## Steps

No route exists. Both the registered contact domain and the company's
own domain publish no MX and no A record, so nothing was ever sent.

If the domain is ever reinstated, or a successor entity files a later state
registration under the same legal name, re-run
`scripts/check_email_domains.py` and the route reopens.

## Gotchas

**Do not "just try it".** A domain with no mail records produces a
*delayed delivery* notice and roughly 48 hours of retries before failing, so a
letter here would sit at `submitted` for two days and teach nobody anything. That
is the whole reason the deliverability check runs before the send rather than
after — see `_SILENT_FAILURES.md` §86.

## Verification

Nothing to verify. Re-check the domain periodically; a dead
domain can mean a lapsed registration, a wound-up company, or a rebrand that left
the filing behind, and only the last of those reopens.


## Unreachable: no mail route exists

Both the contact address published in their California data broker registration
**and** the company's own domain have no MX record and no A record. There is
nowhere to deliver a message, so no letter was ever sent.

Found by `check_email_domains.py`, which asks whether a contact domain can
receive mail at all before a send is spent on it. See `_SILENT_FAILURES.md` §86.

**Why this is `unreachable` rather than `failed`.** Nothing was attempted and
nothing was refused. A domain with no mail records produces a *delayed delivery*
notice and roughly 48 hours of retries before it finally fails, so writing here
would have shown `submitted` for two days and taught nobody anything.

**Re-check rather than treating this as final.** A dead domain can mean a lapsed
registration, a company that has wound up, or a rebrand that left the filing
behind. If the domain is ever reinstated, or a successor entity appears in a
later state registration under the same legal name, the route reopens.
