# Emailmovers

- **Email:** compliance@emailmovers.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** emailmovers.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: UK list broker. Pre-empted the jurisdictional deflection explicitly: stated that no UK/EU data-subject status is being claimed, and that the question is simply whether they will action a deletion request from the US person whose data they hold, as law or as policy - because a jurisdictional answer does not say whether the data was deleted. Also asked for hashed-form search, permanent suppression, recipients and source.

## Steps

1. Email `compliance@emailmovers.com`.
2. Pre-empt the jurisdictional deflection in the letter itself — see below.
3. Ask for hashed-form search, permanent suppression, recipients and source.

## Gotchas

A UK company holding US consumer data. The predictable reply is jurisdictional,
and the important thing about a jurisdictional reply is that **it does not answer
the question**: "you are not a UK data subject" tells you nothing about whether
your data still exists.

So concede the point you were never making, and put the real question in front of
them:

> *"I am not claiming to be a UK or EU data subject, and I am not asserting rights
> under the UK GDPR on the basis of residence. However, if you process the personal
> data of US individuals — as any holder of the addresses above necessarily does —
> then the question is simply whether you will action a deletion request from the
> person concerned."*

This costs one paragraph and removes the easiest exit. It also makes a refusal
legible: a company that declines after that framing has declined to delete, not
merely declined to agree about jurisdiction, and that is a materially different
thing to have in writing.

The same shape works for any residency-based deflection — see `_DEFLECTIONS.md`.

**Search hashed forms, and say so in the letter.** This industry exchanges
identity as MD5 and SHA-256 digests of email addresses, not as addresses. So
*"we hold no record of that email"* can be entirely true while the digest of that
same address sits in the file — the same record under a different key, and the
key the business actually trades on.

This is not a trick question to catch them out; most of the time nobody at the
company has thought about it, because to them the hash simply *is* the identifier.
Asking in plain terms — "please search hashed forms of each address as well as
plaintext" — usually gets a straight answer.

## Verification

No public listing. The written answer is everything. Ask which basis they applied
— law or policy — and whether the action was suppression or deletion.
