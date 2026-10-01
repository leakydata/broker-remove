# Blis Global Ltd

- **Email:** privacy@blis.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** blis.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-24)
- Note: 2026-08-25: UK-headquartered location audience business; letter states US-resident scope up front so it is not answered under GDPR. Geographic query in place of a MAID with confirm-before-delete, visitation history as the core ask, and the question of whether suppression can be keyed to anything but a resettable advertising ID.
- **2026-09-24 reply: genuine structural nil.** "After thorough checks of our systems, including our HR, CRM, and Accounts systems, as well as our Marketing database, we have not found any information relating to the personal data you provided. At Blis, we do not process emails, addresses, date of birth, or phone numbers. We share IP addresses and mobile identifiers with our partners to enable programmatic advertising." They explicitly didn't run the overnight-dwell-pattern geographic query from the original letter (no mention of it), but the broader point stands on its own: Blis's stated architecture holds **no directly-identifying PII at all** to search in the first place — only device/IP identifiers. Offered to add a device ID to their suppression list if we can find one ("browse using your favourite search engine and the search term 'find my device ID'"), which is not something a consumer can reliably produce. Recorded `not_found` rather than pushing further — there's no identifier left to search on, and if they do not hear back by 2026-10-24 they'll close the ticket as resolved by default.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@blis.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

- **Checks HR/CRM/Accounts/Marketing systems, not just the ad-tech store.**
  Their nil reply listed all four internal systems searched, which is more
  thorough than most ad-tech companies bother to state — a useful template to
  ask for explicitly elsewhere.
- **They hold no directly-identifying PII at all by design** — no email,
  address, DOB or phone. Only IP and mobile ad IDs. So a geographic
  dwell-pattern query (the ask in the original letter) is the only thing that
  could theoretically surface a match, and they didn't say whether they ran
  it — don't assume they did just because the overall answer was a nil.
- **Suppression can only be keyed to a device ad ID.** They explicitly suggest
  searching "find my device ID" to locate one — not something to do for
  verification purposes. No durable, identifier-free suppression is possible
  here.
- Closes automatically if unanswered by their stated date (30 days from their
  reply) — no action needed to keep the nil on record.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Blis Global Ltd
- **Registered address:** 15th Floor, The Shard, London, UK, SE1 9SG
- **Filed contact email:** privacy@blis.com
- **Filed phone:** 02034754660
- **Website:** https://www.blis.com

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
