# NeighborWho

- **Opt-out:** https://www.neighborwho.com/optout
- **Email:** support@neighborwho.com (verified)
- **Method:** web_form — Web form.
- **Domain:** neighborwho.com
- **Priority: 3.**

## Status

- Current: `replied` (updated 2026-10-10)
- Reference: `gmail:1a0064b93acf05ab`
- Note: DELIBERATE REGRESSION FROM confirmed, part of the 468 audit of adopted statuses. This row carried 'confirmed' from another agent's ledger with nothing but the boilerplate note, and THERE IS NO CORRESPONDENCE FROM THIS COMPANY IN THE MAILBOX AT ALL. Being careful about what that does and does not prove: people-search opt-outs are often web flows that generate no email, so silence is NOT evidence the work was never done -- it is evidence that this mailbox cannot establish either way, which is a different and weaker claim. What tips it is the sibling. OWNERLY, NEIGHBORWHO AND BEENVERIFIED ARE ALL THE LIFETIME VALUE CO. The BeenVerified row carried the same adopted 'confirmed' and, when checked today, rested on nothing but a generic customer-service feedback auto-reply that never mentions a search, a record or a removal. Three sibling rows marked complete at the same time by the same process, one of them demonstrably on no evidence, is reason enough to stop treating the other two as finished. A SINGLE LETTER MAY COVER ALL THREE: the request sent to privacy@beenverified.com on 2026-10-10 asks in terms whether it reaches Ownerly and NeighborWho or whether each brand must be filed separately, and asks where. Hold this row at 'replied' until that answer comes back; if they say the brands are separate, file here directly rather than assuming the parent's answer travels. ONE THING THEIR OWN FAQ MAKES LIKELY: BeenVerified states that a People Search opt-out may leave a name in their other search services. Ownerly is property-focused and NeighborWho is address-focused, so they are precisely the 'other services' that an opt-out keyed to a people-search record would miss.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.neighborwho.com/optout
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `support@neighborwho.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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
