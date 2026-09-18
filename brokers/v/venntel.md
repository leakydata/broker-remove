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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Venntel, Inc.
- **Trading as:** Venntel
- **Registered address:** 44679 ENDICOTT DR STE 333, Ashburn, Virginia,
  20147
- **Filed contact email:** privacy@venntel.com
- **Filed phone:** 8555455623
- **Website:** www.venntel.com

*Source: `data/registries/registry.csv`.*

## If they ignore you

Work down this list. Each rung costs them more than the one above it.

1. **Reply in the existing thread** after the statutory deadline. California
   allows 45 days for a deletion request (Cal. Civ. Code 1798.130), extendable
   once by a further 45 with notice. Quote the date you first wrote.
2. **Write to the legal entity at the registered address above**, by post, if
   email has failed. A letter to the address of record is harder to lose than a
   support ticket, and it establishes a paper trail.
3. **Complain to the California Attorney General**, who administers the data
   broker registry: <https://oag.ca.gov/contact/consumer-complaint-against-business-or-company>.
   A broker's registration is what obliges it to answer; a complaint referencing
   the registry entry is the pressure point.
4. **Complain to the FTC**: <https://reportfraud.ftc.gov>. Useful for a pattern
   of non-response rather than a single case.
5. **Your own state Attorney General.** Many states with no comprehensive
   privacy statute still have consumer-protection powers and will take a
   complaint about a business that ignores its own published policy.

**What not to bother with:** phoning a support line to argue. The person who
answers cannot change the policy and did not write it. The registry entry, the
statutory deadline and the regulator are what actually move a company.
