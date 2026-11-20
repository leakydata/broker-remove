# Inbound Insight

- **Email:** privacy@inboundinsight.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** inboundinsight.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-11-20)
- 2026-11-20: Reply arrived, 84 days after the original letter (generic, did not quote or reference the chase): "Your privacy opt-out request has been processed. We have added your information to our suppression records so that it will not be used in future applicable data processing or marketing data services." It is a company-level statement, not a per-identifier one -- it does not say which of the twelve supplied identifiers matched, and it does not distinguish "suppressed going forward" from "existing activity records/resolutions deleted." Replied asking both questions directly: (1) which identifier types were searched, (2) whether the suppression also covers deletion of prior activity records, intent scores, or identity resolutions created before the request, or only blocks future use. Treating this as `submitted`, not `confirmed`, until that's answered -- see _SILENT_FAILURES on suppression vs. deletion.
- 2026-11-16 CHASED in-thread: over 80 days with no reply to the August request; asked one line, did it arrive, and if this mailbox is wrong, which address or form handles privacy requests.
- Earlier: Sent the INTENT / WEB-VISITOR variant. If the business is identifying or scoring anonymous website visitors, the record is not a contact row but observed behaviour joined to an identity, so the letter asks for: (1) the ACTIVITY RECORDS themselves -- pages viewed, content downloaded, searches, sessions -- not merely the intent score derived from them; (2) THE RESOLUTION ITSELF, since if an anonymous visit was resolved to the subject by hashed email, cookie, device ID, IP or an identity-graph partner then THAT JOIN IS THE RECORD and the endpoints reassemble without it; (3) COMPANY-LEVEL ATTRIBUTION where visits are resolved to an employer by IP or email domain and reported to a vendor as research from that organisation; (4) hashed email match keys. B2B carve-out pre-empted with the sunset date; identifier-types-matched question asked.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@inboundinsight.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

- The confirmation reply is a boilerplate one-liner that does not quote or
  reference any of the specific questions asked (identifier-by-identifier
  match, activity-record deletion vs. forward suppression, hashed-identifier
  handling). Don't read "opt-out request has been processed" as answering
  those questions — it answers only "did you receive and act on a request,"
  which is a narrower claim. Worth one more email naming the unanswered
  points explicitly before treating the row as closed.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Inbound Insight, LLC
- **Trading as:** Inbound Insight
- **Registered address:** 157 E 57th St, Ste 15E, New York, NY, 10022
- **Filed contact email:** privacy@inboundinsight.com
- **Filed phone:** 212-655-9807
- **Website:** inboundinsight.com

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
