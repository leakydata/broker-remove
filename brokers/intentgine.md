# Intentgine

- **Opt-out:** https://intentgine.com/ccpa-privacy/
- **Email:** privacy@pharosiq.com (verified)
- **Method:** web_form — Web form.
- **Domain:** intentgine.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Scope extended on the existing thread to cover PharosIQ, which shares this mailbox. Also repeated the identity-graph ask: delete the LINKS between hashed email, device/MAID, cookie/CTV identifiers and IP-derived household associations and the person, not just the named row - in an intent business the edges are the product.

## Steps

1. Email `privacy@pharosiq.com` — Intentgine's privacy contact resolves to PharosIQ, a different brand than the registry domain (intentgine.com); this is a B2B intent-data / lead generation business, so ask who purchased or received the record in addition to deletion.
2. Note the brand relationship (Intentgine ↔ PharosIQ) in any follow-up so the request isn't mistaken as misdirected.

## Gotchas

- **Brand mismatch** like Firmfuel/BenefitsBunny: registry domain and privacy-contact domain differ (intentgine.com vs pharosiq.com). State the connection explicitly in the email so it isn't bounced as "wrong company."

## Verification

No public listing to check. Awaiting reply as of 2026-08-18.

## Outcome (2026-08-20): an honest negative, scoped to the wrong message

`Privacy@pharosiq.com` replied two days after the request:

> "This email is in response to your privacy opt-out request. We have reviewed
> our systems, and the information you provided is not present.
>
> No further action is required at this time.
>
> If you believe your data may exist under a different email address/company or
> spelling variation, please feel free to share it, and we will be happy to
> recheck."
>
> — PharosIQ Data Team

**Check what the reply quotes.** It quotes the *first* letter, which listed four
email addresses. It does not quote the follow-up sent eleven hours later, which
extended the request to cover both brands served by this mailbox and asked them
to search for records keyed to a hashed email, a mobile advertising or cookie
identifier, or an IP-derived household association.

So "the information you provided is not present" is true and narrow. It refers to
four plaintext addresses. In an intent-data business those are often not the key
the record is held under, so a lookup on them can correctly return nothing while
an identifier-keyed record exists. Written up as `_SILENT_FAILURES.md` §73.

**The promise was kept.** The follow-up had said an unqualified "we hold nothing"
would be a complete answer and close the matter. It was not re-argued. That
matters beyond this broker — pre-accepting the unflattering answer is only
effective as a technique because it is honoured.

**The invitation was accepted instead**, which is a different thing from
re-litigating. Sent: the other eight email addresses, four name variants, nine
prior localities, eight prior phone numbers. Plus two questions framed as
questions about *how the check ran*, not about whether it was right:

- does "not present" cover identifier-keyed records as well as contact records,
  or was it a lookup on the addresses given?
- does the answer cover both PharosIQ and Intentgine, and any other entity whose
  privacy requests come from this mailbox? If they are separate controllers
  sharing a desk, name the ones it covers and the rest get their own letters.

Both were offered as acceptable either way. Answering costs nothing; declining
would be conspicuous.

**Status:** left `submitted`, not `not_found`. The negative is real but partial
and a recheck is outstanding. Flip when it returns empty.

**Lesson for reuse:** put the scope in the first letter. A follow-up is not an
amendment — operationally it is a low-priority comment on a ticket that has
already been framed by the message that opened it.
