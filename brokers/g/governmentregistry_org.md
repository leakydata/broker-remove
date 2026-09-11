# Governmentregistry Org

- **Opt-out:** https://www.governmentregistry.org/opt-out
- **Email:** privacy@governmentregistry.org (verified)
- **Method:** web_form — Web form.
- **Domain:** governmentregistry.org
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-20)
- Note: CONFIRMED 2026-08-20 03:27 UTC. Reply from privacy@governmentregistry.org, signed by a named agent: 'We can confirm that GovernmentRegistry has processed and completed the removal of your data from our services.' Unqualified completion, no verification step, no ID demanded, ~2 day turnaround. They answered none of the four scoped questions I asked (source of any criminal entry, suppression-vs-one-time, relatives/associates cross-listing, shared index with sibling properties) and deflected onward sightings with 'contact those sites directly about their privacy policies' - the standard aggregator answer, which tells me nothing about whether the removal was point-in-time or standing.

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
