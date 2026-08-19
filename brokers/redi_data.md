# Redi Data

- **Email:** privacy@redidata.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** redidata.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Compiled consumer and business marketing data - postal, email, telephone, segments and appends. Suppression-at-ingest first, then source-and-consent-wording, then recipients WITH the downstream question (are customers who already licensed a file contractually required to delete it, and if not say plainly that delivered copies are permanent), then deletion. Sensitive selects named individually with the delete-not-flag distinction. Three closing questions: which identifier types matched, whether derived and modelled attributes are covered, and archived/aged/recycled inventory held apart from the live database.

## Steps

1. Write to `privacy@redidata.com`.
2. Suppression at ingest, then source, then recipients, then deletion.

## Gotchas

Standard compiled-data shape (see `outward_media.md`), with one addition worth
carrying everywhere in this category:

**Ask whether customers who have already licensed or downloaded a file containing
the record are contractually required to delete it** — and invite them to say
plainly that the delivered copies are permanent if that is the truth. A compiled-
data business ships files; deletion at source does nothing about the copies
already shipped, and most confirmations quietly decline to mention that.

Also: name the sensitive selects individually and insist on deletion rather than
a do-not-mail flag, ask which identifier types they matched on, ask whether
derived and modelled attributes are in scope, and ask about archived, aged and
recycled inventory held apart from the live database.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
