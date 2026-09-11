# Windfall

- **Opt-out:** none published
- **Email:** privacy@windfall.com — **unpublished guess.** No contact address
  appears anywhere on their privacy policy, /privacy/ or /contact/ pages.
- **Method:** email (by elimination)
- **Domain:** windfall.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)

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
