# Matchbook

- **Email:** privacy@matchbookdata.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** matchbookdata.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Identity matching. Match keys, household keys, hashed email in three algorithms, device/cookie/CTV identifiers, appended attributes, and the links between them. Asked which identifier types they matched on and where the record was sourced.

## Steps

1. Email `privacy@matchbookdata.com` — answers within a minute via Zendesk.
2. Expect the MAID gate. It is not a deflection; it is what they actually hold.
3. Decide the advertising-ID question ONCE across every broker in this category —
   see `_CATEGORY_VARIANTS.md`.
4. Their opt-out form is at `/opt-out-form/`.

## Gotchas

They can only find you by mobile advertising ID, and unlike CityData.AI they will not
tell you whether there was a match. Below.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## The MAID gate, in its weakest form

> *"Matchbook Data and its products only work with advertising identifiers for mobile
> devices and not with personal identifiers such as names, email addresses, telephone
> numbers, etc. Therefore, in order to fulfill your request, you must submit the mobile
> advertising identifiers of your device(s) to us. Without the advertising identifiers,
> we will not be able to process your request to determine if we hold any relevant
> data."*

Third company to say this, after Foursquare and CityData.AI. **This is not a
deflection** — it is a description of what the business actually holds, and it is
useful precisely because it says so plainly.

But it is the **weakest of the three offers**. CityData.AI offered check-then-tell:
hand over the identifier, they hash it, check it, and report whether there was a match.
Matchbook offers nothing back — the identifier is required even to learn whether
anything is held. So the exchange is: disclose a live identifier to a company that may
never have had it, and receive no information in return.

**The resettability of the MAID is what makes this tractable.** Supply once across all
three, let each delete against it, then reset the advertising ID on the device — what
they retain is a dead value. That converts a permanent disclosure into a time-boxed
one, and it argues for deciding the whole category in a single go rather than three
separate times. See `_CATEGORY_VARIANTS.md`.

Ticket reference #187177.
