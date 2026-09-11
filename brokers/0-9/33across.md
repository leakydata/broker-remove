# 33across

- **Opt-out:** https://udp.33across.com/udp_opt_out
- **Email:** privacy@33across.com (verified)
- **Method:** web_form — Web form.
- **Domain:** 33across.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-17)
- Reference: `auto-reply 2026-08-15`
- Note: Auto-acknowledged. Adtech opt-out framing - they emphasise interest-based advertising choice rather than deletion; may need follow-up to distinguish opt-out-of-targeting from deletion of identifiers.

## Steps

1. Email `privacy@33across.com` with the **adtech variant** of the letter, not the
   people-search one. The difference matters — see below.
2. Demand deletion of the identifier types they actually hold: cookie IDs, mobile
   advertising IDs, hashed email identifiers, and inferred audience segments.
3. Ask them to search **hashed forms** of each address. An adtech platform that
   "has no record of your email" may hold its MD5 and SHA-256 digests, which is
   the same record by another name.
4. Ask them to propagate the deletion to DSP and SSP partners the identifiers were
   syndicated to, and to say which.
5. Their opt-out page at `https://udp.33across.com/udp_opt_out` is a separate,
   weaker action — take it as well, but do not let it stand in for the request.

## Gotchas

They auto-acknowledged, and the acknowledgement framed the request as **interest-
based advertising choice**. That framing is the thing to push back on.

An adtech opt-out and a deletion request are different in a way that is easy to
lose: opting out of targeting stops them *acting* on the profile while leaving the
profile intact, and it is usually implemented as a cookie — which dies with the
cookie jar, the browser or the device. Deletion removes the record. A reply that
says "you have been opted out" has answered a question you did not ask.

**Identity-keyed, not name-keyed.** This is the category distinction that governs
everything here (`_CATEGORY_VARIANTS.md`): a people-search site indexes a person
by name and address, and an adtech platform indexes a device or a hashed email.
Sending the people-search letter gets a truthful "we hold no record under that
name" that is completely uninformative.

Follow-up needed: press them to state, in writing, whether identifiers were
deleted or merely suppressed from targeting, and whether the deletion reached
downstream partners. An opt-out that only binds 33Across leaves copies wherever
the segments were sold.

## Verification

There is nothing to search — you cannot look yourself up in an adtech platform,
which is exactly why the written answer carries the whole weight here.

Ask for confirmation naming the identifier types deleted, and the downstream
partners notified. Re-check the opt-out cookie after any browser or device change;
if the opt-out was cookie-based, that change silently undid it.
