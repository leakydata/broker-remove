# Quadrant Global Pte. Ltd.

- **Email:** privacy@quadrant.io (state-registry / site-published address — unverified until a reply arrives)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** quadrant.io
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-08-27)
- Note: 2026-08-26: emailed privacy@quadrant.io. Asked for advertising/device identifiers, location and movement history, inferred home/work location, and the identity-graph linkage, and asked them to name the identifier types they matched on since a name-and-address search will not reach device-keyed records.
- Note: 2026-08-26/27: two replies, consistent both times — *"Please note that Quadrant does not collect personally identifiable information (PII) such as name, date of birth, phone number, email addresses"* and *"Our database can only search using MAID/Device ID."* Pushed back once asking them to at least confirm no name/email/phone-keyed record exists; they held the line that MAID/Device ID is the only search key. Declined to supply a MAID or IDFA (would be handing them a new identifier rather than removing one — against the "never submit more personal data than required" rule). Treated as closed: a device-ID-only ad-tech vendor genuinely cannot search on the identifiers this project uses, and this is a believable true negative rather than a stonewall.

## Gotchas

- **Device-ID-only matching is a real architectural limit, not a deflection** — several ad-tech/identity-graph brokers in this registry are built this way. Don't supply a MAID/IDFA to "help" the search; that hands them a working key to a record that otherwise can't be found.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
