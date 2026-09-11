# VoterRecords.com

- **Opt-out:** —
- **Email:** admin@voterrecords.com (BLOCKED at verification — their page would
  not load for a scripted check, so the address is unconfirmed rather than wrong)
- **Method:** email
- **Domain:** voterrecords.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)

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
