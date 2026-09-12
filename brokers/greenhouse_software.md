# Greenhouse Software, Inc.

- **Email:** privacy@greenhouse.io (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** greenhouse.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-09-12)
- Note: Opt-out letter sent by email to privacy@greenhouse.io (delete + opt out of sale/sharing + direct downstream recipients + suppress against future ingestion). All twelve email addresses, sixteen prior addresses and eleven prior phone numbers listed for search. Sent as HTML per letter_html.
- **Confirmed 2026-09-11**, but from a different address than the one contacted: `dsr@greenhouse.io` sent *"Your deletion request has been completed."* Not `privacy@greenhouse.io` — Greenhouse's DSAR (data subject access request) pipeline apparently runs its own outbound address, separate from the inbound privacy contact.
- **`dsr@greenhouse.io` is send-only.** A reply asking two standard follow-up questions (was there anything to delete; is this a standing suppression) sent to it hard-bounced 550 5.1.1 the same second. Re-sent the same two questions as a fresh message to `privacy@greenhouse.io` instead — that thread is open as of 2026-09-12.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

- **Two different addresses, two different jobs.** `privacy@greenhouse.io` takes
  the initial request; `dsr@greenhouse.io` sends the completion notice but
  cannot receive replies. Any follow-up question belongs back at `privacy@`,
  quoting the DSR completion rather than replying to it directly.
- The completion notice ("Your deletion request has been completed") does not
  say whether anything was actually found, nor whether it's a standing
  suppression — see the two open questions above.

## Verification

Re-check with `privacy@greenhouse.io` for the answers to the two open
questions. No public search surface to independently re-verify against —
Greenhouse is an ATS vendor, not a people-search site with its own listing
page.
