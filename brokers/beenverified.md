# BeenVerified

- **Opt-out:** https://www.beenverified.com/app/optout/search
- **Email:** privacy@beenverified.com
- **Method:** web form (search → select record → email confirm); email also accepted
- **Priority: 5.**

## Family properties — check each

BeenVerified operates several sibling brands that carry the same underlying data:

- **Ownerly** (property / home value) — `brokers/ownerly.md`
- **NeighborWho** (property + neighbour reports) — `brokers/neighborwho.md`
- **PeopleLooker**
- **NumberGuru**

A removal on one does **not** reliably clear the others. Request explicitly that
it apply across all properties they operate, and file separately for the siblings
where a distinct opt-out exists.

## Gotchas
- Web opt-out requires an emailed confirmation link — unconfirmed requests are
  void. Point the confirmation at a mailbox you can actually read.
- The web flow surfaces multiple candidate records for a common name. Match on
  prior cities and relatives, not the name alone.

## Verification
Re-search beenverified.com, and separately check Ownerly and NeighborWho, after
~7–14 days.

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

