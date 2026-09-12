# Venntel

- **Email:** privacy@venntel.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** venntel.com
- **Priority: 2.**

## Status

- Current: `replied` (updated 2026-09-03)
- Note: NIL PRESSED ON THE KEY-SET POINT 2026-09-03 (SILENT_FAILURES 193/289). Venntel replied 2026-09-02: 'Our team has received the information you have previously submitted, and is unable to find that information in our databases. Thus, we confirm that we do not process any personal data associated with this information.' CREDITED THE ONE UNUSUALLY GOOD SENTENCE: 'Venntel is committed to honoring privacy requests ACROSS OUR ENTERPRISE, AND REGARDLESS OF WHICH STATE OR COUNTRY YOU HAIL FROM' -- which removes the residency question entirely for a PA resident with no comprehensive statute. THE PROBLEM: item 4 of the original letter asked them to NAME THE IDENTIFIER TYPES MATCHED ON, and that is unanswered. I supplied name, DOB, postal address, phone and four emails; Venntel's business is MOBILE LOCATION DATA KEYED TO ADVERTISING AND DEVICE IDENTIFIERS. If the index is IDFA/GAID-keyed then a search across everything I gave could not have matched no matter what they hold -- the nil would be accurate and uninformative. Asked either which identifier types were searched, or for them to say plainly that a name-based search cannot reach a device-keyed index, which is a MORE useful answer than a nil. NO DEVICE ID SENT, with the reason stated. Asked for the two things needing no match: forward-looking suppression on name and addresses, and the 1798.120 opt-out which requires no verification. ADDED THE 289 CONTROL QUESTION -- whether a positive control was run, framed with the exit that if not, I record the result as unverified rather than asking them to redo work. AND A ROUTING FIND: their signature displays privacy@venntel.com but the underlying mailto points at PRIVACY@GRAVYANALYTICS.COM -- so a reader who clicks writes to a different company than the one named, and it corroborates that Venntel, Gravy Analytics and Unacast are answered from one desk. Asked whether the search covered the group or only Venntel, since I have written to all three.

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
