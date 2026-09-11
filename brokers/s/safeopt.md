# Safeopt

- **Method:** unknown — Route not yet established.
- **Domain:** safeopt.com
- **Priority: 1.**

## Status

- Current: `submitted` (updated 2026-09-03)
- Note: 2026-09-03: Opt-out letter sent to privacy@addshoppers.com (delete + opt out of sale/sharing + direct downstream recipients + standing suppression), all four email addresses listed for individual search. Flagged the routing assumption openly in the first line -- writing to the parent because SafeOpt's own pages publish the AddShoppers mailbox -- and asked them to name the correct entity if that inference is wrong. Included the hashed-input wedge (a hash of my address is still personal information; a plaintext-only comparison returns a false negative) and the three-question close: (a) was there anything to delete or did the search find nothing, since 'completed' reads identically either way, (b) which supplier did it come from, citing 1798.110 on categories of sources, (c) is the suppression STANDING, since a deletion without one is undone by the next file loaded.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Status

- Current: `submitted` (2026-09-03)
- **How this route was found (§306).** SafeOpt was one of 279 catalogue rows with no route at all. A sweep of the 121 such rows that at least had a domain produced **exactly one published address in 121 domains**, and this was it: `privacy@addshoppers.com`, in plain text on SafeOpt's own pages.
- **The address is off-domain, and that is expected rather than a mis-scrape.** SafeOpt is an AddShoppers product, so the parent's privacy mailbox is the right destination. It is still a different claim from a first-party address (§109), so the letter says so in its first line and asks them to name the correct entity if the inference is wrong.

## Gotchas

- Off-domain contact: mail goes to `addshoppers.com`, not `safeopt.com`. If a reply comes back scoped only to AddShoppers' own site visitors, that is the §262 shape — a policy about the wrong data subject — and the follow-up is to ask specifically about the SafeOpt product's consumer records.
- SafeOpt's business is identity resolution on site visitors, so **hashed email is the likely storage form.** The letter includes the hashed-input wedge for that reason: a hash of an address is still personal information, and a plaintext-only comparison returns a false negative that looks exactly like a nil.

## Verification

- No public search page to re-run. Verification is limited to what they state, so the letter asks the three questions that make a reply checkable: was there anything to delete, which supplier did it come from (§ 1798.110 categories of sources), and is the suppression standing.
