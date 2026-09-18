# Addresses.com

- **Opt-out:** https://www.peopleconnect.us/optout/ (PeopleConnect's shared tool)
- **Email:** privacy@peopleconnect.us
- **Method:** email — a statutory request by email was accepted and actioned
- **Domain:** addresses.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Reference: `gmail:1a0064addb7ed3d1`
- Note: Family-wide suppression confirmed in five identical replies within twelve minutes: 'We have completed the suppression of your publicly available information from appearing in background reports on the people search sites within our corporate family that we control when a user searches by your name.' Three scoped limits pushed back on: keyed to NAME SEARCH only (I had asked for phone/address/email lookups too), scope stated as 'sites we control' without naming them, and suppression expressly not deletion.

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
