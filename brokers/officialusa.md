# OfficialUSA

- **Opt-out:** https://www.officialusa.com/
- **Email:** info@officialusa.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** officialusa.com
- **Priority: 3.**

## Status

- Current: `unreachable` (updated 2026-08-17)
- Reference: `gmail:1a0064bc0464c58e`
- Note: Domain does not resolve (DNS SERVFAIL on both A and MX); site unreachable over HTTPS. Gmail classified this as a temporary 'Delivery incomplete' and retried for 48h rather than hard-bouncing, so the request looked pending for over a day. Nothing to chase.

## Steps

1. Email `info@officialusa.com`, the address the registry held.
2. Watch for the delivery outcome rather than assuming one. Gmail classified this
   as a temporary "Delivery incomplete" and retried for 48 hours.
3. `dig +short A officialusa.com` and `dig +short MX officialusa.com` — both
   return SERVFAIL. The domain does not resolve; HTTPS is unreachable too.
4. Mark `unreachable` and set `email_verified=false`. There is nothing to chase.

## Gotchas

This one hid for over a day, and the way it hid is the lesson.

A **DNS failure does not produce a hard bounce.** Gmail cannot tell a domain that
has vanished from a domain whose nameservers are briefly unwell, so it does the
conservative thing: reports "Delivery incomplete", keeps retrying for 48 hours,
and only then gives up. For that whole window the request sits in Sent looking
exactly like every request that is genuinely in flight, and the tracker agrees
with it.

Compare the failure modes, because the tracker should not treat them alike:

| What you see | What it means | What to do |
|---|---|---|
| `550 address not found` | domain lives, mailbox does not | find another address |
| `domain couldn't be found` | domain has no DNS at all | `unreachable`, stop |
| "Delivery incomplete", retrying | **unknown yet** — could be either | resolve it yourself |

The third row is the trap: it is not a status, it is the absence of one. Do not
wait 48 hours to be told. One `dig` answers it immediately.

`unreachable` is the honest status here. It is not `failed` — nobody refused
anything — and it is emphatically not `pending`.

## Verification

Re-resolve the domain before spending any further effort:

    dig +short A officialusa.com ; dig +short MX officialusa.com

If it ever answers again, the site is back and the request needs re-sending from
scratch — a mail that never reached a nameserver reached nobody, so there is no
partial delivery to build on.
