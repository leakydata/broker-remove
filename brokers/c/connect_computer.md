# Connect Computer LLC

- **Email:** support@calltruth.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** calltruth.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-28)
- Note: PERMANENT FAILURE CONFIRMED 2026-08-28, third and final bounce (26th, 27th, 28th Aug). 'DNS Error: DNS type mx lookup of calltruth.com responded with code SERVFAIL', status 4.4.3 -- a TEMPORARY code that simply never resolved, which is why it took three days to become final. Verified by hand: calltruth.com SERVFAILs on NS, SOA, MX and A, from two independent resolvers. The domain is still REGISTERED (eNom, clientTransferProhibited) and still delegated to DNS1-4.NAME-SERVICES.COM, but those nameservers do not answer. So this is a third distinct shape alongside the ones already in dead_addresses.json: NXDOMAIN means the name does not exist, no-MX-no-A means the name exists with no mail route, and SERVFAIL means the name is delegated to nameservers that are broken or gone. Practically undeliverable and slow to prove, because a resolver cannot tell a broken nameserver from a briefly unreachable one -- which is also why check_email_domains.py cannot pre-empt this class the way it pre-empts the other two. Retry only if the delegation is ever seen to answer.

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

> **Correction (2026-08-25):** That same day's run sent another request to `support@calltruth.com`, which this playbook already recorded as `unreachable` earlier the same day. Same root cause as the note above (registry email_to didn't reflect this playbook's own status) — no new information, no status change.

> **Correction (2026-08-29):** the same thing happened again, later. A letter reached `support@calltruth.com` around 2026-08-26, sat as a "delivery incomplete, will retry" notice for two days — exactly the pattern this playbook already warned about for a SERVFAIL domain — and hard-failed on 2026-08-28. The registry's `email_verified` flag was still `true` (`ca_data_broker_registry`) at the time, which is presumably why it went out; corrected the flag to `false`/`bounced` here so the queue itself carries the finding, not only this file's prose.
