# NeighborWho

- **Opt-out:** https://www.neighborwho.com/optout
- **Email:** support@neighborwho.com (verified)
- **Method:** web_form — Web form.
- **Domain:** neighborwho.com
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-08-15)
- Reference: `gmail:1a0064b93acf05ab`
- Note: Statutory deletion + opt-out emailed from [EMAIL]. All 4 email identities + DOB asserted. Includes explicit fallback: if broker claims no covering statute or non-covered state, honor as company policy and state which basis was applied. Covers property/ownership/neighbour reports tied to the address.

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

## Email is answered by a named human, and partially actioned

A Zendesk ticket answered by a named agent within days. The reply pattern is worth
knowing because it looks like a refusal and is not:

> *"We are unable to locate a full record that directly corresponds with the
> combination of the first name, last name, age, and/or address information you
> provided."*

followed, further down, by:

> *"In the meantime, we have opted-out the other individual pieces of information
> that you provided to us"*

— listing the email addresses and telephone number, which **were** suppressed. So a
standard letter gets the identifiers actioned even when the person record is not
matched. Record it as partial, not failed.

## They match on name + age + city/state

That is the join key, and it is not what a standard opt-out letter contains. When
they ask for more, send:

- **age as a number**, not only a date of birth;
- a **bare list of cities and states**, separate from full postal addresses;
- the **complete address history** — with a long one, the record is most likely
  filed under a former address, which is usually why the match failed;
- every alias form of the name.

See `_DEFLECTIONS.md` §15.

## The profile-URL ask

They also offer *"provide a link to the page where you see your name"*. Reasonable,
but declining is fine: say you have not located the listing and would rather not
buy a report to exercise a privacy right, then give the identifier combination that
disambiguates you.

## Ask whether it is suppression

*"We have opted-out the other individual pieces of information"* does not say
whether those identifiers are blocked against future ingestion or merely removed
now. Ask explicitly, and ask how many records matched.

## Scope

Part of a group operating several people-search brands. Ask for the request to be
applied across all group properties — one ticket can cover several sites, and the
same reply template appeared from two of their brands on the same afternoon.

