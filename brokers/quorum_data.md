# Quorum Data, Inc

- **Email:** privacy@quorum.inc (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** quorum.inc
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-15)
- **Reply (2026-09-14, from Karl Polifka-Rivas, COO):** answered all five questions at once by describing the architecture rather than dodging it — *"Our records are pseudonymous and are keyed to device and household identifiers. We do not collect or maintain consumer names, email addresses, telephone numbers, or postal addresses."* Explicitly invoked **CCPA § 7024** as the reason they will not re-identify pseudonymous data to search it: *"we are not reasonably capable of associating your request with any record we hold... Consistent with CCPA § 7024, we are not required to re-identify or link pseudonymous data in order to respond, and we will not do so, as that would create an association between you and our data that does not presently exist."* Recorded the opt-out anyway and closed the matter.
- Note: Emailed privacy@quorum.inc 2026-08-29 (CA registry 2026, new). 'The ground truth behind every screen' -- independent real-world measurement and targeting. The letter's hinge is THE AGGREGATE-VS-INDIVIDUAL DISTINCTION, which is the whole question for any measurement business: measuring what an ad moved means linking exposure to a subsequent act (a store visit, a purchase, a sign-up, a tune-in), and aggregate lift is a statistic about a population while AN INDIVIDUAL-LEVEL LINK BETWEEN 'was shown this' AND 'then did that' IS A BEHAVIOURAL RECORD ABOUT A PERSON, materially more revealing than an impression log. Five asks: which outcome signals are used and at what level the linkage happens; retention after a campaign ends, individual vs device vs household, and rejoinability to a name, postal address or hashed email by them or a partner; THE SCREEN SIDE -- whether they hold or derive connected-TV or content-recognition data, with the argument that what a household watches indicates political leaning, religious observance, language, health concerns and the presence of children as a straightforward inference from the content; the hashed-email wedge with device ID and IP both refused and the reason stated; and supplier and client categories, since a deletion cannot reach a delivered copy. Standard concession offered first: if nothing is keyed to a name, say so and it is recorded as a real result.

## Steps

1. Email `privacy@quorum.inc`. Expect a genuine, architecture-level answer rather
   than a template — this company answers what was actually asked.

## Gotchas

- **§ 7024 is a real, citable reason to refuse re-identification, not a dodge.**
  A pseudonymous ad-measurement platform genuinely may have no name/email/phone/
  address keys at all, and CCPA's own regulations (§ 7024) say a business is not
  required to re-identify data to satisfy a deletion request if doing so would
  itself create a new privacy risk. Worth citing back if another adtech company
  tries to use "we can't find you" as a stall rather than backing it with this
  or an equivalent provision.
- The letter's device/CTV/IP-refusal framing (asking what they key on rather than
  supplying a fresh identifier) is exactly what let them give a specific, credible
  negative instead of a boilerplate one — see azerion.md and ipqualityscore.md for
  the same pattern.

## Verification

No consumer-facing lookup — pseudonymous device/household-keyed data, so nothing
to search from outside. The opt-out-of-sale/share instruction was recorded on
their side per the 2026-09-14 reply; no further action needed.
