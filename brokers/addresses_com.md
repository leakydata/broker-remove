# Addresses.com

- **Opt-out:** https://www.peopleconnect.us/optout/ (PeopleConnect's shared tool)
- **Email:** privacy@peopleconnect.us
- **Method:** email — a statutory request by email was accepted and actioned
- **Domain:** addresses.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- PeopleConnect processed it across their properties. **Suppression, not
  deletion** — stated by them explicitly, see below.

## This is a PeopleConnect brand, not a standalone site

Addresses.com is one property in the PeopleConnect group, alongside Intelius,
TruthFinder, Instant Checkmate and US Search. Write once, ask for all of them by
name, and read any confirmation for scope — a reply naming one hostname out of
five is the failure mode `_SILENT_FAILURES.md` §40 exists for.

Their shared opt-out tool is name-search based, which is the gap worth pressing:
**a name-search suppression does not necessarily cover reverse lookups by phone,
address or email**, and those are separate query paths into the same index.

## Steps

1. Email `privacy@peopleconnect.us` with a statutory deletion and opt-out
   request. No account needed and no ID demanded.
2. Assert **every** email identity and the date of birth, not just the current
   ones — the index is built largely from details a person no longer uses.
3. Ask explicitly for coverage **beyond name-search suppression**: phone,
   address and email reverse lookups, across every PeopleConnect property.
4. Include the standard fallback clause: if they consider no statute covers the
   request or the requester's state, honour it as company policy and say which
   basis was applied.

## What they actually said

PeopleConnect suppressed addresses, emails, telephone numbers and identifiable
background reports from display across their sites — and were unusually direct
that this is **suppression, not deletion**:

> *"does not delete or alter the underlying public record from its original
> source"*

**That sentence is the whole shape of this broker, and it is honest.** They are a
republisher: the source record persists at the county, the state or the upstream
aggregator, and PeopleConnect is switching off *their* display of it. That is the
most they can truthfully offer, and saying so plainly is better practice than an
unqualified "deleted" that means the same thing.

The consequence for verification: nothing here reaches the origin. Any removal is
undone if the record is re-ingested under a variant not covered by the
suppression key — which is precisely why step 3 matters.

They also **invited additional identifiers** to widen the suppression. Take that
invitation; it is the cheapest coverage available and most brokers do not offer
it.

## Verification

Re-run a name search plus a reverse phone search on each PeopleConnect property
separately. A name search alone will not detect the gap this playbook is about.
