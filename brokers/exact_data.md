# Exact Data

- **Email:** privacyteam@data-axle.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** data-axle.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-18)
- Note: Exact Data operates on data-axle.com and publishes privacyteam@data-axle.com. Covered by the Data Axle Consumer Privacy Rights Request form rather than a separate letter.

## Steps

Do not write to Exact Data separately. It runs on `data-axle.com` and publishes
`privacyteam@data-axle.com`, so the route is Data Axle's Consumer Privacy Rights
Request form — see **`dataaxle.md`**, which covers the whole flow.

The one thing to carry over: their Privacy Choice dropdown is a single-select, so
**submit twice** — once for deletion and once for opt-out of sale/sharing.

## Gotchas

This one was found by the registry rather than by reading anything: `dataaxle`
had **no contact address at all**, while `exact_data` — a separate entry, a
separate brand — published `privacyteam@data-axle.com`. The subsidiary's record
supplied the parent's missing route.

Worth noting as a search technique. `scripts/family_scan.py` groups brokers by
shared contact address, which finds families where several entries name the same
mailbox. It does **not** find this case, where the useful information is that one
entry's contact lives on another entry's domain and that other entry has nothing
recorded. When a major broker shows a blank contact, check whether a smaller
sibling in the registry has already published one on the same domain.


## Verification

As `dataaxle.md`. Ask the confirmation to say whether it covers the Exact Data
brand by name — a submission through the parent's form is not self-evidently
scoped to a subsidiary, and nobody will volunteer that it was not.
