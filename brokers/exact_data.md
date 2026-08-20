# Exact Data

- **Email:** privacyteam@data-axle.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** data-axle.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Covered by the Data Axle submissions, not by a separate letter. Data Axle's own privacy-rights form names exactdata.com within its scope, and both required submissions were made there (deletion and opt-out of sale are single-select on that form, so each right needs its own run). Recording it as submitted rather than leaving it pending, because a sibling that is genuinely covered looks identical in the tracker to one nobody named - and the family scan was flagging this pair every pass. Playbook lives under dataaxle via the alias file. If Data Axle answers scoped to one brand only, this reverts to pending.

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

## Resolution: covered by the Data Axle submissions

Exact Data shares its privacy contact and its removal route with Data Axle, and
Data Axle's own privacy-rights form names `exactdata.com` within its scope. Both
required submissions were made there — deletion and opt-out of sale are
single-select on that form, so each right needs its own run — and both returned
*"Thank you. Your privacy request has been received."*

Recorded as `submitted` rather than left `pending` for a specific reason. The
family scan flags a group where one member has been written to and another has
not, because **a sibling your letter did not name is a sibling nobody removed**.
But the inverse failure is just as easy: a sibling that genuinely *was* covered
sits in the tracker looking exactly like one that was missed, and gets re-flagged
every pass until somebody decides. Deciding, and writing down why, is the point.

The decision is conditional. If Data Axle replies with a confirmation scoped to
one brand only, this reverts to pending and Exact Data needs a request of its own.

See `dataaxle.md` for the form's behaviour and the deemed-consent clause in their
privacy policy.
