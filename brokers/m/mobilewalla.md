# Mobilewalla

- **Email:** [named individual]@mobilewalla.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** mobilewalla.com
- **Priority: 2.**

## Status

- Current: `replied` (updated 2026-10-10)
- Note: REOPENED 2026-10-10 WITH THE ONE QUESTION THAT WAS NEVER ASKED, after 489a worked it out at Elevar. Their September answer stands and is not disputed: 'No MAID. No way to help you.' That is architecture, not obstruction -- a device graph indexes on device identifiers, so a name-and-email search queries a field they do not use. WHAT CHANGES IS THE SHAPE OF THE ASK. The refusal to supply a mobile advertising ID rests on a specific harm: handing a device graph a stable device identifier together with a name and address CREATES the link the request is trying to break, and if they hold nothing keyed to him today the request does not test for a match, it builds one. THAT OBJECTION DOES NOT APPLY TO AN IDENTIFIER THEY ALREADY HAVE. So: can they HASH ONE OF THE TWELVE EMAIL ADDRESSES AT THEIR END and hold the hash on a suppression or do-not-ingest list? Hashed email is a standard match key in this sector alongside device IDs. A hash THEY compute, of a value HE HAS ALREADY GIVEN THEM, creates no identifier that did not exist -- and it is in the form their systems actually index on. Explicitly not asking whether it matches anything; asking whether it can keep him out of FUTURE ingestion, which a one-time nil does not cover. THREE ACCEPTABLE ANSWERS OFFERED AND ALL CLOSE THE ROW: yes/done; we can hash but suppression is device-keyed so it would do nothing; or no. The letter says a one-line no is welcome and praises their earlier bluntness over companies that send three paragraphs saying nothing -- which is true, and is also the thing most likely to get a terse company to answer. SAME LETTER SENT TO place_exchange on its existing thread.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `[named individual]@mobilewalla.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

- **The MAID dead-end is structural, not a stall tactic.** Mobilewalla's data is keyed to mobile advertising identifiers, not name/email/address. Refusing to supply one is correct (it would create the exact link being asked to remove), but it also means there is no way to confirm or exclude a device-level record from outside — the honest ceiling of what an email request can achieve here.
- Did not answer the FCRA-fork question (whether any output is used for credit/insurance/employment/housing eligibility) or the derived-layer questions (segments, scores, feature store) — the reply addressed only the identifiability problem and stopped there. Worth a narrower one-line follow-up in a future pass if this broker resurfaces, but not worth pursuing now given the terse tone.
- Replies are short and blunt (their own "No MAID. No way to help you. Have a nice day." is representative) — don't expect elaboration on a second ask.

## Verification

No further check possible without supplying a device identifier, which we won't do. Treat as closed on the identifiable side.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Mobilewalla, Inc.
- **Trading as:** Mobilewalla
- **Registered address:** 5170 Peachtree Road, Bldg 100 STE 100, Atlanta,
  Georgia, 30341
- **Filed contact email:** [named individual]@mobilewalla.com
- **Filed phone:** 7704026730
- **Website:** www.mobilewalla.com

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
