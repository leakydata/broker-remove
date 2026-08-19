# Match And Append

- **Email:** privacy@matchandappend.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** matchandappend.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Match-and-append business, so the letter targets the LINKAGE rather than the row: appended phone/address/demographic values AND the linkage itself, hashed email as match key, household/persistent keys, derived attributes. Asked which source supplied the record and which clients received an appended output - an append already delivered is not recalled by deleting their copy.

## Steps

1. Do NOT use `privacy@matchandappend.com` — it hard-bounces 550.
2. There is no website to read for an alternative: the domain has no A record.
3. Write to `info@`, report the dead privacy mailbox as a fault, and target the
   linkage rather than the row.

## Gotchas

Live mail, dead website, and the published privacy mailbox does not exist. Below.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Live mail, no website

`privacy@matchandappend.com` returns a hard **550 — address not found**. That is not a
dead company: the domain publishes a healthy **Zoho** MX and accepts mail at other
local parts. What it does not have is a **website** — no A record, and every URL
returns nothing at all.

This is the same shape as `minervadata.xyz`, and exactly the case that a reachability
check keyed to web presence gets wrong (see `_SILENT_FAILURES.md` §30). A company can
receive mail perfectly well while having no site to read, and for an
append-and-match business — which sells to other businesses through direct
relationships — a public website is not a requirement of the trade.

**Consequence for finding a contact:** the usual move of reading the privacy policy for
a working address is unavailable. There is nothing to read. Writing to `info@` and
reporting the dead mailbox is the remaining option, and the report is worth making
regardless: an address published for rights requests that rejects them loses every
request anyone sends, and no sender can distinguish that from being ignored.

## Aim at the linkage, not the row

The product is attaching data to somebody else's record. So the request names the
**linkage** explicitly — the appended phone, email, address or demographic value *and*
the connection between it and the person — plus the hashed email used as a match key,
any household or persistent key, and any derived attribute.

Deleting an appended value while leaving the match key intact means the same append
happens again at the next run.

## Update: the domain does have a site again (2026-08-19, later same day)

A fresh check found the domain now resolving with a live web server: fetching
`matchandappend.com/privacy-policy` returned an HTTP 503 (service unavailable),
not a DNS failure, and the CA data broker registry
(oag.ca.gov/data-broker/registration/546620) publishes two web routes beyond the
dead `privacy@`/`info@` mailboxes:

- `https://www.matchandappend.com/do-not-sell-my-data/`
- `https://www.matchandappend.com/unsubscribe/`

Neither was reachable at check time (503), so this may be an intermittent outage
rather than the "no website at all" state found earlier the same day. Worth a
human retrying the two URLs above before falling back to the `info@` fault report
described above.

