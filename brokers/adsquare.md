# Adsquare

- **Email:** privacy@adsquare.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** adsquare.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-09-07)
- Note: 2026-09-07 reply: "we received your Data Subject Request and did not find any match in our databases... Adsquare does not process any personal data associated with the personal data provided" — a nil, but scoped to the identifiers supplied (advertising IDs, hashed emails, name/address/phone). THE GEOGRAPHIC ASK WAS NOT ANSWERED: the original letter's point (c) deliberately asked a non-identifier query — any device showing a persistent overnight dwell pattern at the home address and each prior address — on the reasoning that a location-keyed dataset has no name field to search, so a name/email nil says nothing about it. Replied same day asking directly whether that query was run, offering three acceptable closing answers (ran it and nothing matched; don't hold place-queryable dwell data; can't run that query type) — awaiting a considered reply, not yet chased further. Also asked that the archived request data not become matchable inventory, and that a standing do-not-sell/do-not-share/do-not-append bind even against a nil.

  Separately, two OneTrust portal ticket confirmations arrived alongside this email thread — Request ID 8WN6LE4TGK (opened 2026-08-24, the same day as the original letter; marked "completed" 2026-09-07 with no detail in the email body, only a JS portal link that could not be fetched headlessly) and Request ID 4XA7NCDD84 (opened 2026-09-07, "logged successfully", no content yet). Adsquare's system appears to auto-generate a portal ticket per inbound message on this thread rather than these being separate requests initiated elsewhere. Left uninvestigated this pass since the live email thread already carries the substantive exchange; worth checking on the next pass whether 8WN6LE4TGK's portal page (browser-only) states anything the email reply didn't.
- Note (2026-08-24): first contact via the address nominated in the California data broker registration. Tailored per _CATEGORY_VARIANTS.md.

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
