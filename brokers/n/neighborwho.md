# NeighborWho

- **Opt-out:** https://www.neighborwho.com/optout
- **Email:** support@neighborwho.com (verified)
- **Method:** web_form — Web form.
- **Domain:** neighborwho.com
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-08-17)
- Reference: `gmail:1a0064b93acf05ab`
- Note: Second 'unable to locate a full record' despite having every identifier they asked for. Replied pressing for a plain written negative or the identifier that would work, and raised the point specific to this brand: NeighborWho is address-centric, so a name-keyed search can return nothing while an address page still lists the subject as a current or former resident. Asked them to search all ten addresses AS addresses.

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

## Same template, same impasse, one brand-specific difference

Two searches, both "unable to locate a full record", after being given name,
variants, date of birth, age, eight cities, ten addresses, twelve phone numbers
and eight email addresses. The wording is word-for-word what BeenVerified sent on
the same afternoon, from the same Zendesk instance — see `beenverified.md` for
the two-outcome reply that applies here too.

The difference worth acting on is what NeighborWho actually indexes.

**It is address-centric.** The product publishes who lives, or has lived, at a
given address, together with neighbours and prior residents. A name-keyed search
can therefore return nothing while an address page still names the subject as a
current or former resident — and that page is what a stranger typing an address
into the site would see.

So the request has to be phrased twice: delete any name-keyed profile, **and**
delete the association between the subject and each address. Ask them to search
all ten addresses *as addresses*. A reply that only reports on emails and phones
has not answered the question that matters at this brand.

This is the general shape of the category (`_CATEGORY_VARIANTS.md`): where the
index key is not a person, a person-shaped request misses.
