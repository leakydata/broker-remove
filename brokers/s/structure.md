# Structure (structure.ac)

- **Opt-out:** —
- **Email:** support@structure.ac (KEEP_BETTER — no dedicated privacy address
  published)
- **Method:** email
- **Domain:** structure.ac
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-24)
- Note: 2026-08-23: hard bounce after three days of retries - 'The recipient server did not accept our requests to connect.' support@structure.ac is dead. No alternative route found.

## Gotchas

**Check what they actually do before writing.** The registry carried no category
for this one. Their own homepage H1 reads:

> "Discover rich information on people and companies"

which places them as a people-and-company enrichment API. That was established by
fetching the page and reading the headings, *before* the letter went out — the
`_SILENT_FAILURES.md` §67 correction exists precisely because a letter once
asserted a product line a company did not have, and the recipient was right to
push back. Category inference is a hypothesis; the site is the evidence.

**Say so in the letter, and leave the door open:**

> Your site describes the product as discovering rich information on people and
> companies, so I take it you compile and serve enrichment records keyed to
> individuals. If that is wrong, please tell me and I will correct my
> understanding rather than argue with you about it.

That sentence costs nothing and converts a possible mis-fire into a corrected
registry entry.

**Ask for the edges.** Enrichment scope list: hashed email forms as match keys;
employer, job title and company affiliation; social and professional profile
URLs; and the edges linking any identifier to name, address or phone. Deleting
endpoint rows while keeping linkage means the record reassembles on the next
match.

**Two questions that matter more than the deletion:** where the record came from
(licensed supplier or scraped public source — name it), and who has it now
(records served through an API live in customers' systems, where a deletion at
the origin does not reach).

**Pre-empt the B2B refusal.** California's business-to-business carve-out sunset
on 1 January 2023, so a business contact record is personal information on the
same footing as a consumer one. Raising it first is cheaper than an exchange
about it.

**No published privacy mailbox**, so ask them to forward rather than bounce the
request back.

## Verification

Written answer only. If they deny being an enrichment business, take the
correction, record it, and reclassify — do not argue.


## Dead: hard bounce after three days of retries

`support@structure.ac` bounced on 2026-08-23:

> *"The recipient server did not accept our requests to connect."*

Three days of Gmail retries preceded it, each producing a *delay* notice rather
than a failure. That is the pattern from `_SILENT_FAILURES.md` §65 — a connection
that is refused rather than a recipient that is rejected produces a temporary
delay, so the tracker reads `submitted` for 48 hours while the letter has
nowhere to go. **A delay notice is not delivery.**

Marked `unreachable`, which is the only status meaning nobody is there. No
alternative route found on the domain.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Structure
- **Registered address:** 1041 N Dupont Hwy, #1047, Dover, DE 19901,
  United States
- **Filed contact email:** support@structure.ac
- **Website:** https://www.structure.ac
- **Opt-out route they filed:** http://structure.ac/opt_outs/new
- **Route for protected individuals:** http://structure.ac/opt_outs/new
  (Cal. Gov. Code 6208.1(b) / 6254.21(c)(1) — for survivors of domestic
  violence, stalking and similar, a stronger and faster route than the
  ordinary consumer request)

*Source: `data/registries/complete-reg-data-brokers.csv`.*

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.structure.ac/opt_outs/new
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `support@structure.ac`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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
