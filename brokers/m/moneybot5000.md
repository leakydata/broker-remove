# Moneybot5000

- **Opt-out:** https://www.moneybot5000.com/svc/optout/search/optouts
- **Email:** support@moneybot5000.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** moneybot5000.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-19)
- Note: PRODUCT-BY-PRODUCT CARVE-OUT. 'At this time, we are unable to remove data from the unclaimed money feature.' They then offer TWO working opt-out routes - Property Search and possible-resident - so the refusal covers one surface while the offer covers two, which is very easy to read as 'the removal'. Asked which kind of 'unable' it is: a technical limitation with no place to store a suppression, or a policy position on public record - and whether display-level suppression exists even if the upstream lookup cannot change. Their scope wording is honest and worth keeping: 'Information about the property may still be available, but details about your identity and any association to the property will be removed' - the linkage is the right unit. Two opt-out flows still to run.

## Steps

1. Email `support@moneybot5000.com`. They reply within the minute, via a ticket desk.
2. Expect a partial answer: removal offered on two surfaces, refused on a third.
3. Run BOTH opt-out flows — resident and property — each is search, select, then
   click a verification link.
4. Push on the carve-out separately; the flows do not touch it.

## Gotchas

The refusal is one clause inside two pages of helpful instructions, which is exactly
how it gets missed. Below.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Two routes offered, one product refused

> *"At this time, we are unable to remove data from the unclaimed money feature."*

Then two working opt-out routes, with clear instructions: **Property Search**
(`/svc/optout/search/optouts/property`) and **possible resident**
(`/svc/optout/search/optouts`).

The shape is the hazard. Most of the reply is cooperative and specific; the refusal is a
single clause near the top. Complete both flows, collect both confirmations, and it
feels finished — while the refused product carries on. See `_SILENT_FAILURES.md` §34.

**Ask which kind of "unable" it is.** A live external lookup with nowhere to store a
suppression is a different problem from a policy position that unclaimed-property data is
public record. The first invites asking for **display-level suppression** even where the
source cannot be changed; the second is a position to record and stop pressing. The word
covers both and only they know which they meant.

## Their scope wording is honest, and it is the right unit

> *"Information about the property may still be available, but details about your
> identity and any association to the property will be removed."*

The property record persists; **the person and the link between person and property**
are what go. That is precisely the correct thing to remove — the linkage is what turns a
public filing into a way to find someone — and saying so plainly is better than most
companies manage.

The resident flow also claims something prospective: they will *"instruct our data
partners not to return your record in future search results."* Worth getting confirmed,
and worth asking whether the property flow does the same.

## What the flows will not cover

Neither opt-out touches an **attribute**. If a financial inference is attached to the
record — income band, creditworthiness, debt, distress, likelihood to respond to an
offer — it is not a listing and will not be removed by opting a listing out. That has to
be asked for separately, and it is the part that actually gets sold.

