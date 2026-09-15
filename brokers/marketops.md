# Marketops

- **Email:** privacy@marketops.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** marketops.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-09-15)
- **Reply (2026-09-14, from Rory Sutherland, Chief Privacy Officer):** personally corrected the earlier nil — *"the search was conducted against all of the identifiers you provided, not solely the email address... your information has been suppressed in accordance with your request and applicable privacy laws."* Clarified the 2026-09-12 "no records found / please resubmit" reply was a **standard response template, not a statement that the search was scoped narrowly** — his words: *"was not intended to suggest that you had failed to provide sufficient information."* Also volunteered MarketOps' own read of its regulatory position: *"does not operate as a traditional data broker... certain state privacy laws define the term 'data broker' broadly, and aspects of our operations fall within those statutory definitions."*
- Note: Standard letter plus the processor-vs-controller split: apply to everything held as controller, and name the client for anything held on their behalf so the request can be redirected rather than silently answered from the wrong side.
- **Reply (2026-09-12):** *"We have received your request for the removal of your personal data. However, we were unable to process your request as no records were found matching the information you provided,"* and pointed to a resubmission form at marketops.com/data-inquiries/ — which would only re-run the identical search, not add anything.
- **Our reply (2026-09-12):** thanked them for stating the nil plainly rather than sending an ambiguous "request completed" notice, then asked two follow-ups: (1) was the search actually run against the full identifier set in the original letter, or only the sending address, and (2) will they apply a suppression against this identifier set regardless of the nil, so a future data purchase doesn't silently re-add him.

## Steps

1. Email `privacy@marketops.com`. If the auto-reply says "no records found,
   please resubmit," don't take that at face value — ask explicitly whether the
   full identifier set was searched. The template wording here overstated a
   narrower search than what was actually run.

## Gotchas

- **The first-line auto-reply template overstates what actually happened.**
  "No records found matching the information you provided" reads like a scoped
  or partial search, but here the CPO confirmed all identifiers were searched
  and the record was in fact found and suppressed. Worth asking a human to
  confirm scope before recording a `not_found` from a templated nil.
- Has a named, responsive Chief Privacy Officer who will personally correct a
  templated reply on request — worth escalating past the auto-responder if a
  first reply looks inconsistent with what was asked.

## Verification

Confirmed by direct reply from the Chief Privacy Officer 2026-09-14. No
consumer-facing lookup to independently re-check.
