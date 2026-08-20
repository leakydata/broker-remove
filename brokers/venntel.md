# Venntel

- **Email:** privacy@venntel.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** venntel.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: Emailed privacy@venntel.com. Mobile-location broker; sent the full mobility-category letter rather than the standard one.

## Steps

1. Email `privacy@venntel.com`.
2. Use the "Mobile location / mobility data" letter from
   `brokers/_CATEGORY_VARIANTS.md` — a name-and-address request achieves
   little here, since the record is keyed to device/advertising identifiers.
   Ask by name for: the MAIDs/device IDs themselves, location and movement
   history (not just derived segments), inferred home/work location, and the
   identity-graph linkage joining device to person.
3. Require them to state which identifier types they matched on — otherwise a
   "no records found" is uninterpretable.

## Gotchas

- Venntel has a documented history of supplying location data to government
  and law-enforcement-adjacent contractors, so the "downstream recipient"
  ask matters more here than at an ordinary ad-tech firm.
- Do not volunteer a mobile advertising ID (IDFA/GAID) to "help them locate
  a record" — ask first whether they hold one at all. Supplying it up front
  creates the very identifier the request is trying to get deleted, and
  hands them a fresh device-to-email join. See `_CATEGORY_VARIANTS.md`,
  "Do not hand over a device identifier to establish that one is not held."

## Verification

No public profile. The only real evidence is their written answer to which
identifier types were searched and whether the deletion reaches location and
movement history, not just the identifier row.
