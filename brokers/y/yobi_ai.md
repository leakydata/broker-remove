# Yobi AI

- **Email:** privacy@yobi.ai (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** yobi.ai
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-11-10)
- **2026-11-10 reply — full, clean closure, the best outcome recorded in this project so far.** All three open points answered without deflection:
  1. **Non-CA residency resolved as company policy**: "As a matter of company policy, Yobi honors deletion and opt-out requests from consumers regardless of their state of residence, and we have processed your request on that basis." The pre-accept-the-unflattering-answer technique paid off directly — asking "if no, say so plainly, that's a complete answer too" made the honest "yes, by policy" easy to give.
  2. **All four addresses searched, nothing found on the remaining three**: "We have now searched our systems for all four email addresses in your request, and no records were found associated with any of them, so no deletion or further verification is required." Also clarified the verification architecture precisely: email is the only match key, so deletion verification by same-address-control is only invoked *when a record actually exists to delete* — with nothing found, there's nothing to verify control for. This resolves the opt-out/deletion verification-tier question from the prior entry; it was never an arbitrary double standard, it only looked that way because the leakydata@ search (which did need deletion-grade verification, moot since nil) ran first.
  3. **Forward-looking, both suppression and opt-out, stated plainly**: "The addresses from your request are applied as suppression records before rebuilds of our data, so records associated with them that we receive from data providers in the future will not be added... Your opt-out likewise applies to future records, not only to data held today."
  - "This completes our response to your request." Nothing further to chase. Record as `confirmed`: nil search (a real `not_found` for deletion, not a dodge — it was run against all four addresses, not just the sender's), opt-out of sale/sharing confirmed and forward-looking on all four, suppression confirmed forward-looking. The only item left unanswered across the whole exchange was which data providers supplied Yobi with records — declined on confidentiality grounds, and pre-accepted as complete per the original letter's own fallback framing.
- Prior (2026-11-05):
- Note: Minimised letter (--keys email-only): name and 12 email addresses only; DOB, postal addresses and phone numbers deliberately withheld because an identifier-keyed adtech platform cannot match on them and receiving them would only enlarge the footprint. Asks for plaintext AND hashed search (MD5/SHA-1/SHA-256, lowercased and trimmed), and for three things in the confirmation: which identifiers matched, which systems were searched, and whether suppression is keyed to me or to the sent keys.
- **2026-11-02 reply, but on the `yobi_ventures.md` thread, not this one** — see Gotchas. privacyops@yobi.ai (named human, Kelly Peterson) searched one address ([EMAIL]) only, found nothing, and confirmed the opt-out of sale/sharing for that one address "as of November 2, 2026." For the other three addresses supplied in that letter, they refused to search: "we are unable to verify your identity at this time for the additional email addresses provided. Please send your privacy requests from the email addresses contained within your privacy request." Replied pushing back on that verification method (see Gotchas) and asking two scope questions about the one address that was processed: is the nil result a forward-looking suppression or only a statement about today's holdings, and is the opt-out itself forward-looking. Also asked which upstream data providers supplied Yobi with records, since their own signature line describes them as "a data technology company that operates as a data intermediary... receive[s] consumer data through licensed agreements with third-party data providers" — i.e. a reseller, not a primary collector.
- **2026-11-05 reply.** Three new pieces, none of which resolved the two open scope questions:
  1. **Opt-out now processed for all three remaining addresses** on the declaration-under-penalty-of-perjury offered in lieu of a same-address email (Cal. Code Regs. tit. 11, § 7060) — so all four addresses are opted out of sale/sharing. But **deletion on those three is still held to the same-address-email standard**; the declaration was accepted for opt-out only, not for deletion. Worth recording as a real distinction: this broker's verification architecture treats "stop selling" and "erase" as different trust levels, not interchangeable rights.
  2. **New deflection: non-California residency.** "While you cite California regulations, the residential address you provided is not for California thus making your request subject to the rights and restrictions as outlined in our Privacy Notice." They did not say the request is refused — only that a different (unnamed) basis applies. Replied invoking the fallback clause from the original letter (honor as company policy if not covered by statute) and asked directly whether the privacy notice extends opt-out/deletion to non-CA consumers as policy, independent of CCPA.
  3. **Declined to name data providers**, citing confidentiality. Pre-accepted this as a complete answer rather than pressing — a stated confidentiality position is itself useful information, and the point was already made that email has no CAPTCHA, not that it has no limits.
  - Still unanswered after two asks: whether the [EMAIL] nil result and the opt-out are forward-looking (survive a future re-ingest) or only describe today's holdings. Asked a third time, framed as the closing question, with an explicit offer to accept "today only" as a complete answer if that's the truth.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@yobi.ai`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

**The reply landed on the predecessor's thread, not this one.** The original
letter to privacy@yobi.ai was sent noting the entity-name discrepancy
(Yobi Ventures LLC vs. Yobi Ventures Inc. dba Yobi AI) and asking only 4
identifiers (name, DOB, phone, 4 emails) — a *different*, fuller letter than
the 12-email-minimised one this file documents. The reply on 2026-11-02 answers
that older letter. Two separate letters to the same current address, with
replies tracked under two different registry rows (`yobi_ventures` and
`yobi_ai`) that both resolve to the same live company — check both files
before assuming either is current.

**Opt-out and deletion are not the same trust level.** A declaration under
penalty of perjury (in lieu of emailing from each address) was accepted for
the *opt-out of sale/sharing* on three addresses, but refused for *deletion*
on the same three — the same evidence, two different verification bars. Don't
assume one acceptance covers both rights; ask about deletion separately even
after an opt-out confirmation lands.

**"Not a California resident" is a scope claim, not a refusal.** On 2026-11-05
they wrote that a non-CA address makes the request "subject to the rights and
restrictions as outlined in our Privacy Notice" — without saying the request
is denied. Treat this as an opening to invoke the standing fallback clause
("honor this as company policy, and tell me which basis you applied"), not as
a closed door.

**Verify-by-resending-from-each-address.** They will search and action
whichever address the request was *sent from*, and refuse every other address
listed in the body unless each one separately emails them, or the consumer
uses the web form at yobi.ai/opt-out. See `_DEFLECTIONS.md` §77 for the
pushback: California's verification regs (11 CCR 7060) permit a signed
declaration under penalty of perjury in lieu of proving control of an address
by sending from it, and the whole reason to list several addresses is that the
disused ones are the likeliest to actually be in a data file — exactly the
ones that can never pass a same-address check.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Yobi Ventures, Inc.
- **Trading as:** Yobi AI
- **Registered address:** 136 E. 76th Street Suite 4B, New York, NY,
  10021
- **Filed contact email:** privacy@yobi.ai
- **Filed phone:** 6465737108
- **Website:** www.yobi.ai

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
