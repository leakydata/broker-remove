# Governmentregistry Org

- **Opt-out:** https://www.governmentregistry.org/opt-out
- **Email:** privacy@governmentregistry.org (verified)
- **Method:** web_form — Web form.
- **Domain:** governmentregistry.org
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-20)
- Note: Listing-URL follow-up on a CONFIRMED removal (SF 185 cohort). Framed explicitly as NOT a fresh request and NOT a complaint -- three questions about a removal they already did right. (1) THE URL, with the reason that makes it more than pedantry: without one, THE ONLY WAY TO VERIFY A REMOVAL IS TO SEARCH FOR MYSELF ON THEIR SITE -- running the exact query I asked them to stop answering, on a site where doing so may log a search, surface me in a 'recently viewed' feature, or prompt the index to refresh the very profile I want gone. VERIFYING A REMOVAL SHOULD NOT REQUIRE GENERATING A NEW RECORD. With a URL I can check in a browser now and again in three months without touching their search. 'There was never a public page' accepted explicitly as a GOOD answer, because 'removed from a listing' and 'removed from a database' are different facts and the ledger should not blur them. (2) WHAT THE SUPPRESSION IS KEYED TO -- the question that decides whether it survives one build cycle. A suppression keyed to an exact NAME STRING is defeated by the next source file that spells it differently, so asked for coverage of all five name forms and for a key more durable than the string. Prior identifiers supplied as the things an OLDER record is actually keyed to. SF 193 limit stated in its operational form: suppress the ASSOCIATION, not the bare value, because other people live at those addresses and several of those numbers have been reassigned -- blocking the value takes away a stranger's listing. (3) SURVIVAL of refresh + migration + acquisition (SF 224). Common-name limit and DOB-to-rule-out both carried. GOVERNMENTREGISTRY-SPECIFIC, AND THE MOST VALUABLE ASK OF THE FOUR: a fourth question on SOURCE PROVENANCE, because their product is aggregated public records and THEIR SUPPRESSION STOPS THEIR COPY WITHOUT TOUCHING THE SOURCE -- the record is still in whatever roll, register or licensed feed it came from, still available to the next aggregator AND to them on the next refresh, from the same place. Asked which categories: court indexes, property/deed, voter files, licence registers, vital records, motor vehicle, credit-header or utility, commercial compilations. And flagged the part that matters most -- if any of it came from a COMMERCIAL compiler rather than a government body, that part is not public-record data at all and carries ordinary rights.

## Steps

Email alone, to `privacy@governmentregistry.org`. **No form, no account, no
verification step, no identity document.** Confirmed in about two days.

The reply was unqualified:

> "We can confirm that GovernmentRegistry has processed and completed the
> removal of your data from our services."

## Gotchas

- **It confirms and explains nothing.** The letter asked four scoped questions —
  the source of any criminal or court entry attributed to me, whether removal was
  suppression or point-in-time, whether it reaches my name where it appears on
  *other people's* listings as a related person, and whether the site shares an
  index with sibling properties. None was answered.
- **The onward-sighting brush-off is standard.** "If you continue to see your
  information online... contact those sites directly about their privacy policies
  and compliance." That is the aggregator's universal answer and it is not
  informative: it is equally consistent with a standing suppression and with a
  single row deleted from an index that re-ingests from government sources on a
  cycle. Since the confirmation reads identically either way, treat the
  suppression question as still open regardless of how clean the confirmation
  looks.
- **Not a family member of the sites it resembles.** Route 53 nameservers,
  independent A records, no shared URL path with `staterecords.org` or
  `statecourts.org`. Registrar/DNS-provider defaults are not family signals.

## Verification

Re-check in seven days, and again after a plausible ingest cycle — the failure
mode for a public-records aggregator is not a removal that never happened, it is
one that silently reverses at the next ingest. A REAPPEARED result here is
escalation-worthy: it converts the unanswered suppression question into a
demonstrated fact.
