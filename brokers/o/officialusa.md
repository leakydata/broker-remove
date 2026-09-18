# OfficialUSA

- **Opt-out:** https://www.officialusa.com/
- **Email:** info@officialusa.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** officialusa.com
- **Priority: 3.**

## Status

- Current: `unreachable` (updated 2026-08-18)
- Reference: `gmail:1a0064bc0464c58e`
- Note: HARD BOUNCE after 47h of retries: 'DNS Error: DNS type mx lookup of officialusa.com responded with code NXDOMAIN'. Verified independently: no MX, no A record, no HTTPS response. The domain is still REGISTERED (registrar Internet Invest / Imena.UA, clientTransferProhibited) but has no DNS records at all - the site is dark. This is the one bounce class that genuinely means nobody is there; a CDN refusing us or a full mailbox does not.

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

## Dark domain: the one bounce that really means unreachable

Mail to `info@officialusa.com` was retried by Gmail for 47 hours and then failed
permanently:

> *"DNS Error: DNS type 'mx' lookup of officialusa.com responded with code NXDOMAIN"*

Checked independently rather than taken on trust: no MX record, no A record, no
HTTPS response. The domain is still **registered** -- there is a registrar of record
and a `clientTransferProhibited` status -- but it publishes no DNS at all. The site
is dark.

**This is the only bounce class that genuinely means nobody is there.** Compare:

- a **CDN or WAF refusing the connection** means a live company behind a shield;
- a **full mailbox** means a real address nobody is emptying;
- a **550 unknown user** means the domain is alive and that one address is not.

Only NXDOMAIN says the name itself resolves to nothing. Recorded `unreachable`
rather than `failed`, and no further route is worth hunting: a registered domain
with no DNS has no web form, no privacy page and no second address to try.

Worth re-checking rather than closing forever, though. A registered domain can come
back, and if it does the data probably comes back with it.

## If they ignore you

Work down this list. Each rung costs them more than the one above it.

1. **Reply in the existing thread** after the statutory deadline. California
   allows 45 days for a deletion request (Cal. Civ. Code 1798.130), extendable
   once by a further 45 with notice. Quote the date you first wrote.
2. **Write to the legal entity at the registered address above**, by post, if
   email has failed. A letter to the address of record is harder to lose than a
   support ticket, and it establishes a paper trail.
3. **Complain to the California Attorney General**, who administers the data
   broker registry: <https://oag.ca.gov/contact/consumer-complaint-against-business-or-company>.
   A broker's registration is what obliges it to answer; a complaint referencing
   the registry entry is the pressure point.
4. **Complain to the FTC**: <https://reportfraud.ftc.gov>. Useful for a pattern
   of non-response rather than a single case.
5. **Your own state Attorney General.** Many states with no comprehensive
   privacy statute still have consumer-protection powers and will take a
   complaint about a business that ignores its own published policy.

**What not to bother with:** phoning a support line to argue. The person who
answers cannot change the policy and did not write it. The registry entry, the
statutory deadline and the regulator are what actually move a company.
