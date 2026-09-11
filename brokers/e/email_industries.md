# Email Industries

- **Email:** privacy@emailindustries.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** emailindustries.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Email-data/hygiene variant. Core ask: search HASHED forms as well as plaintext, since a digest is the same record under a different key and 'we hold no record of that address' is compatible with holding its hash. Also asked for validation/deliverability/engagement records - a record that consists only of 'this address exists and is good' is still personal data - plus permanent suppression, source and recipients.

## Steps

1. Email `privacy@emailindustries.com`.
2. Ask for **hashed forms** of every address to be searched as well as plaintext.
3. Ask for validation, deliverability and engagement records, not only a
   "profile".
4. Ask for permanent suppression, the acquisition source, and the recipients.

## Gotchas

**Search hashed forms, and say so in the letter.** This industry exchanges
identity as MD5 and SHA-256 digests of email addresses, not as addresses. So
*"we hold no record of that email"* can be entirely true while the digest of that
same address sits in the file — the same record under a different key, and the
key the business actually trades on.

This is not a trick question to catch them out; most of the time nobody at the
company has thought about it, because to them the hash simply *is* the identifier.
Asking in plain terms — "please search hashed forms of each address as well as
plaintext" — usually gets a straight answer.

**A validation record is still a record.** The instinctive framing of a deletion
request is "delete my profile", which invites the answer "we hold no profile for
you". But an email-hygiene business may hold something narrower and still
personal: that this address exists, is deliverable, is active, is engaged, belongs
to a real person, belongs to *this* person. Each of those is an assertion about
me. Ask for them by name, because "profile" will not reach them.

Suppression rather than deletion applies here as everywhere that files are rebuilt
from partners — see `dmdatabases_com.md` for the same point at greater length.

## Verification

No public listing. Ask for the confirmation to state **which forms were searched**
— plaintext, MD5, SHA-256 — and what was found under each. A confirmation that
does not distinguish them has not answered the question.
