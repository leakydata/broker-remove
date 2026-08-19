# Mogean

- **Email:** info@mogean.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** mogean.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Location/mobility data. Asked for MAID, cookie and device identifiers, location/visit/trip/dwell records derived from them, IP-derived household associations and the LINKS between identifiers. Deliberately supplied no advertising ID and said why, noting the decision is being made once across the whole category rather than piecemeal. Only published contact is info@, so asked them to forward internally.

## Steps

1. Email `info@` — the only contact published. They answer within the hour.
2. Expect the MAID gate. Send the letter anyway; the refusal arrives with a
   negative attached, which is the point.
3. Ask them to hold the ticket open — they close it by default.
4. Decide the advertising-identifier question once, across all four such brokers.
   See `_CATEGORY_VARIANTS.md`.

## Gotchas

They close the ticket in the same breath as refusing, and the negative they give is
wider than it first appears. Below.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## The refusal comes with a negative attached

> *"Mogean does not have any of the information that you provided. We deal exclusively
> in mobile advertising identifiers, so if you reply back with your valid advertising
> identifier GUID we will check our systems."*

The first sentence is the valuable half, and it is easy to read past on the way to the
gate. It is an **unqualified negative covering every identifier supplied** — the name and
its variants, sixteen current and prior addresses, eleven telephone numbers, twelve email
addresses.

That is the strongest argument for writing to a MAID-only broker at all. They cannot
match a person by name, so asking them to try yields the cleanest `not_found` available
anywhere — for everything except the one identifier space they actually use. Recorded as
`not_found` **for the supplied identifiers**, explicitly not for the MAID space, which
remains untested.

## Check-then-tell, and a ticket that closes itself

Mogean is the **second** of four to offer *"we will check our systems"* rather than
simply ingesting the value — the CityData.AI shape, and a materially better trade than
Matchbook's, because the disclosure buys an answer rather than only an action.

But note the last line:

> *"Without this information, we are unable to process your request and are considering
> this request closed."*

A closed ticket means any later reply begins again from the top. Asking them to hold it
open costs one sentence and preserves everything already established.

## Two questions that cost nothing to ask

Neither depends on supplying an identifier, and both bound whatever answer eventually
comes:

  - **If an identifier is supplied and there is no match, will they say so?** A confirmed
    no-match is a real result and should be requested in advance.
  - **Does deletion cover the derived records** — location, visit and dwell histories,
    audience segments, inferred attributes keyed to that identifier — **or only the
    identifier row?** Deleting the key while retaining the history keyed to it is not a
    deletion in any sense that matters.
