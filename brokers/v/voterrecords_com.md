# VoterRecords.com

- **Opt-out:** —
- **Email:** admin@voterrecords.com (BLOCKED at verification — their page would
  not load for a scripted check, so the address is unconfirmed rather than wrong)
- **Method:** email
- **Domain:** voterrecords.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: Letter sent 2026-08-20, tailored to category.

## Gotchas

**Do not send the generic letter.** This site republishes voter registration
data that is genuinely public at source. Pretending otherwise invites a correct
refusal and wastes the exchange. Concede it in the first paragraph, then draw the
line that actually matters:

> A county voter roll is public in the sense that it can be inspected. Your site
> makes the same information retrievable by name from anywhere, alongside address
> history and, on many profiles, apparent household members and party
> affiliation. Those are different things, and only the second one follows a
> person around.

**Three asks, in this order:**

1. Remove the pages **and** apply `noindex` to those URLs. A page whose content
   is gone but whose URL stays indexed remains findable through cached results
   for months, and that is the state most removals actually end in.
2. Make it a **standing suppression**. A voter index is continuously refreshed
   from state and county files, so a point-in-time opt-out is undone by the next
   ingest — and the confirmation email reads identically either way. Explicitly
   accept "we do not suppress" as a useful answer that will not be treated as a
   refusal; it tells you to re-check rather than to argue.
3. Remove **household and co-registrant appearances** on other people's profiles.
   Those are indexed independently and are frequently how someone is found after
   a profile-scoped deletion.

**Ask which state or county file the record came from, and when it was last
refreshed.** Several states offer confidentiality or address-protection programs
at source; that is the only fix that survives, and the republisher is the only
party who knows which file they pulled.

**Anticipate the public-records exemption.** Rather than let it be a whole-request
refusal, ask them to say *which part* it covers and to honour the remainder.

**Common-name caution.** Ask them to match on date of birth and explicitly not to
remove records belonging to other people.

## Verification

Search the site directly for the name against the current and two longest-held
prior localities. Then re-check after the next election-cycle refresh, since a
one-time removal will not survive it.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://voterrecords.com/faq
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `admin@voterrecords.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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
