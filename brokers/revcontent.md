# RevContent, LLC

- **Email:** privacy@revcontent.com (state-registry / site-published address — unverified until a reply arrives)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** revcontent.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-06) — credible, architecture-explained nil
- Reference: `gmail:1a03d97de3ccf8b1`
- Note: 2026-08-26: emailed privacy@revcontent.com. Same ad-tech variant — hashed-email matching, cookie/device IDs, modelled segments, cross-context sharing opt-out.
- Reply (2026-09-05): nil against all twelve plaintext emails, but only searched their "registered advertiser/publisher" dataset. Since RevContent stated they hold no plaintext emails at all, a plaintext search proves nothing about a hash-keyed match — asked whether the hashes had actually been searched.
- Reply (2026-09-05, follow-up): DPO explained the architecture in full and it holds up. Two genuinely separate populations: (1) *registered* advertisers/publishers, held in plaintext — a hash search against this set "would yield the exact same result" as the plaintext one already run, so re-running on hashes is not a different question here; (2) *anonymous* widget viewers, keyed only to IP/user-agent/a rotating `__ID` cookie with a 72-hour TTL — no email or phone is ever collected for this group, by design, so an email-based lookup is genuinely not possible without the browser-level form data. Also disclosed unprompted: a stray, unrelated hyperlinked email address in the first reply was a copy-paste artifact from an old template, not a real record — apologised and said it was being fixed at the process level.
- **Accepted as complete.** This is the credible version of "we don't have a matching key," not a dodge: the explanation of *why* a hash search changes nothing for the registered population, combined with a specific, verifiable reason no email-linked data exists at all for the anonymous population, is a materially different (and better) answer than a bare "not found." Declined the per-browser/device form for the reason given in the thread — supplying an IP/user-agent/user_id to a company that holds device-keyed data would attach a name to identifiers that currently have none, which is the wrong direction for a request whose point is to reduce linkage, not add it.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

- **"We don't collect X" is worth pressing on the identifier type it implies, once.** RevContent's first reply said "we don't store plaintext emails" while reporting a nil on a plaintext search — asking "then did you search the hashes?" got a substantive architectural answer instead of a second round of the same boilerplate. Don't accept a nil at face value when the stated data model makes that nil the *only possible* outcome regardless of whether a match exists.
- **Declining their per-device verification form was the right call.** A form that collects IP/user-agent/cookie to "match" a request, at a company that holds exactly those as its primary keys, converts an anonymous record into a named one. The hash-based ask (get them to hash your identifiers server-side) avoids this because nothing new is disclosed.
- **A copy-paste artifact in a reply (a stray unrelated email address) is worth flagging, not assuming.** Could have been a mis-join exposing a stranger's data; here it was a template mistake, confirmed by asking rather than assuming either way.

## Verification

Credible nil, explained rather than asserted. Re-check only if a future broker or disclosure names RevContent as a recipient of matched data.
