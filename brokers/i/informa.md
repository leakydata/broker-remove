# Informa Group Limited

- **Email:** groupdpo@informa.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** informa.com
- **Priority: 2.**

## Status

- Current: `replied` (updated 2026-09-22)
- Reference: `gmail:1a045d613ce03f97`
- Note: 9/21 reply from b2bprivacyteam@informa.com: "your profile and data were
  not located in our records. On this basis we could not action your
  request." This is a textbook **scoped confirmation** (see
  `brokers/_SILENT_FAILURES.md`) — the original letter explicitly asked which
  Informa businesses were searched, since Informa runs distinct brands under
  separate privacy notices (Informa TechTarget alone has its own privacy
  contact, `privacy@techtarget.com`, tracked separately as
  `informa_techtarget`), and the reply answered none of that. Replied 9/22
  pressing specifically for which businesses were searched before treating
  this as a real `not_found`. Left as `replied` rather than `not_found` until
  that's answered — a nil that doesn't say what it covers isn't a result yet.
- Older note (8/28), for the letter that produced this reply: Sent to the GROUP DPO deliberately, and the letter opens on SCOPE rather than on the request. Informa runs many distinct brands across B2B media, market research, academic publishing and events, each with its own privacy notice, so a request answered correctly for one brand leaves identical records under a sibling. Asked them to treat it as covering every Informa business holding personal data and to SAY WHICH ONES THEY SEARCHED -- or, if group policy requires per-brand requests, to name the brands so they can be written to individually. The point put to them plainly: from outside, a partial answer and a complete one look identical.

Named the four places a record would most plausibly sit: event and conference registration including EXHIBITOR BADGE-SCAN records, which are routinely retained and onward-supplied; publication and newsletter subscriber lists including lapsed ones; market research panels and contact databases; and any assembled B2B prospect file. Flagged [EMAIL] as the university address most likely to key an academic-publishing or conference record. B2B carve-out pre-empted with the sunset date.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `groupdpo@informa.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

**The Group DPO inbox answers fast, but its "not located" answer does not say
what was searched.** Asking explicitly "which businesses did you search" in
the original letter did not produce an answer to that question in the reply —
it produced a plain negative. Do not treat a Group-level nil as covering the
whole group unless a follow-up makes them say so explicitly; a large
multi-brand holding company is exactly the case `_SILENT_FAILURES.md`'s
"scoped confirmation" entry warns about. Informa TechTarget in particular is
tracked as a **separate registry entry** (`informa_techtarget`,
privacy@techtarget.com) precisely because it looks likely to sit outside
whatever the Group DPO's system actually queries.

**No CAPTCHA, no web form, no account** — pure email exchange, reasonably
fast turnaround (about three weeks from first letter to reply).

## Verification

Watch for the follow-up naming which Informa businesses were actually
searched. If they confirm it covered every brand (including TechTarget,
events/exhibitor systems, and market-research panels), upgrade to
`not_found`. If they name only a subset, write to the brands outside it
individually.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Informa Group Limited
- **Registered address:** 5 Howick Place, London, United Kingdom, SW1P
  1WG
- **Filed contact email:** groupdpo@informa.com
- **Filed phone:** 20 8052 0400
- **Website:** https://www.informa.com

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
