# Windfall

- **Opt-out:** none published
- **Email:** privacy@windfall.com — **unpublished guess.** No contact address
  appears anywhere on their privacy policy, /privacy/ or /contact/ pages.
- **Method:** email (by elimination)
- **Domain:** windfall.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: Sent 2026-08-20 to privacy@windfall.com (unpublished guess). Their privacy policy offers ONLY DAA/NAI/Google Analytics industry opt-out links and no first-party rights route or contact address - flagged that to them. Letter targets modelled/inferred attributes (net worth, propensity, giving capacity) since clearing source fields leaves the score.

## Gotchas

**There is no first-party rights route.** Their privacy policy publishes no
privacy contact and offers, as its only opt-out mechanism, links to:

```
optout.aboutads.info      (DAA)
optout.networkadvertising.org  (NAI)
tools.google.com/dlpage/gaoptout
```

Those govern advertising cookies in a browser. They do not touch a compiled
consumer record and they are not a mechanism for deletion, access, or opt-out of
sale. Pointing at them is a rights-shaped object in the place where the route
should be — see `_DEFLECTIONS.md` §43. Say so plainly in the letter; it is both
true and useful to them.

**Write to a guessed `privacy@` anyway.** A bounce and a silence are different
findings and both are worth recording. Guessing here is defensible precisely
because there is nothing published to trade down from.

**Attack the score, not the source fields.** Windfall builds wealth and
propensity estimates. A deletion that clears the inputs and leaves the model
output is not a deletion, and the output is what gets used:

> Net worth, income, giving capacity, propensity and any lifestyle or life-event
> scores are inferences drawn about me, and inferences are personal information
> under CCPA as amended in the same way the underlying data is.

**Ask for suppression against re-modelling, not just deletion.** In a modelling
business the inputs are public and licensed and still out there, so the record
will simply be recomputed on the next refresh unless a suppression entry stops it.
This matters more here than the deletion itself.

**Ask whether they assign a persistent identifier** that would let a customer
re-match the person after deletion. In a business whose product is delivered
*into* the customer's CRM, that identifier is what makes deletion reversible.

**Search the older addresses.** Wealth models lean heavily on property records,
so the prior addresses are the ones most likely to be driving the estimate.

**B2B point applies:** California's business-to-business carve-out sunset on
1 January 2023, so any part of the record held as a business contact is on the
same footing as a consumer one.

## Verification

Watch for a bounce first — that determines whether email is a route at all. If
it delivers and a reply confirms deletion without mentioning modelled attributes
or re-modelling, push once on those two points.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Windfall Data, Inc.
- **Registered address:** 595 Pacific Ave, Fl 4, San Francisco, CA, 94133
- **Filed contact email:** privacy@windfall.com
- **Filed phone:** 8009466710
- **Website:** www.windfall.com

*Source: `data/registries/registry.csv`.*

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.windfall.com/do-not-sell-my-info
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `privacy@windfall.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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
