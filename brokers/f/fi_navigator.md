# FI Navigator Corporation

- **Email:** privacy@fi-navigator.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** fi-navigator.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-08-31)
- Note: PROOF, not inference (SF 209). At 00:35:57 I sent a re-ask whose entire content was the question 'did a search actually run?'. It contained NO identifiers -- no emails, no addresses, no phone numbers, nothing to search against. Thirty seconds later, at 00:36:26 and 00:36:27, trustsuperset returned the identical template twice: 'We were unable to find any matching records given the information provided in your right to erasure request' and the same for opt-out. A no-match verdict on a message that supplied nothing to match. Combined with the 2026-08-31 00:05 RevOptimal result (two completions, including a right never exercised, 55s after a defect report), this reproduces across two independent tenants: the outcome is generated from RECEIPT OF MAIL, not from a query. Email does not reach a person at any trustsuperset tenant. Queued for a non-email route.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

**Their privacy mail runs through a third-party vendor, trustsuperset.com, and
the vendor appears unreliable.** Two "no matching records" replies arrived
2026-08-27 (erasure and opt-out-of-sale). A follow-up letter (2026-08-31) noted
that the SAME platform, acting for a different company that same week, sent an
internal end-to-end test fixture ("this is the 404-not-found email (e2e test)")
to a real inbox, followed by two unrequested "request completed" confirmations
sent 55 seconds after a message that contained no request at all. That's
evidence the pipeline can emit a "no matching records" outcome with no search
behind it. The follow-up asked three closing questions — did a search actually
run, which fields were searched (12 emails / 16 addresses / 11 phones were
supplied, most a search on current details alone would miss), were hashed forms
checked — and got back **the same templated "no matching records" text**,
unresponsive to any of it. Treat FI Navigator's nil result as *unconfirmed*
rather than closed; a human reply engaging with the specifics never arrived.
Worth flagging trustsuperset.com's reliability generically if it turns up as
the vendor behind other brokers' privacy mail.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
