# Adsquare

- **Email:** privacy@adsquare.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** adsquare.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-07)
- Reference: `4XA7NCDD84`
- Note: PORTAL LOGGED THE FOLLOW-UP AS A NEW REQUEST. The reply asking whether the geographic dwell-pattern query was run came back as 'Your request has been successfully submitted. Your Request ID is 4XA7NCDD84' -- a SECOND request id, not a continuation of 8WN6LE4TGK. So their intake treats any inbound mail on the thread as a fresh DSAR. Consequence to watch: the geographic question may be answered as a new request against the same identifiers, which would produce the same identifier-keyed nil and never reach the point. If the next reply is another 'did not find any match in our databases', that is the intake behaviour rather than an answer, and the question will need putting again with the request id quoted. Not a complaint -- auto-logging is better than silent discard -- but it is a route where a follow-up cannot be distinguished from a first contact. The substantive position is unchanged: nil on the identifiers supplied, geographic query unconfirmed. Request ids on file: 8WN6LE4TGK (original, completed) and 4XA7NCDD84 (the follow-up).

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->


## The geographic query, because the consumer cannot supply a MAID

Adsquare is a location and audience exchange. The record is keyed to a mobile
advertising identifier, and **no consumer can look up their own advertising ID
historically** — it is resettable, it was never disclosed to them, and asking for
it is asking them to produce something the industry generated.

So the letter substitutes a query they *can* run: **any device showing a
persistent overnight dwell pattern at the current address**, and at each prior
address for the period of residence. A residential overnight pattern identifies a
household member about as reliably as a name field.

Stated with the reason attached, so a name-keyed null result cannot be used to
close the request: *"please answer the geographic question before concluding a
name search found nothing, because a name-keyed search is the wrong query for a
location dataset."*

Standard identity-graph asks also apply: hashed email match keys (separating
suppression hashes, which are fine, from matchable inventory, which is not),
device and CTV identifiers, **the edges** between identifiers and name/address,
IP-derived household association, and inferred segments.
