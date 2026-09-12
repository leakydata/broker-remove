# Moneybot5000

- **Opt-out:** https://www.moneybot5000.com/svc/optout/search/optouts
- **Email:** support@moneybot5000.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** moneybot5000.com
- **Priority: 2.**

## Status

- Current: `replied` (updated 2026-09-03)
- Note: A PRIVACY REQUEST ROUTED TO BILLING, AND A REQUEST FOR CARD DETAILS -- REFUSED (2026-09-03). MoneyBot5000 support replied: 'we are unable to locate an account under your name or email address' and then asked for THE LAST FOUR AND TYPE OF CARD CHARGED, THE BILLING ZIP, the charge date and amount, and whether another name is connected to the card. TWO PROBLEMS. (1) CATEGORY ERROR, and the 205 pattern in its purest form: they searched the CUSTOMER-ACCOUNT system. I have never been a customer, never had an account and never been charged -- which is the whole premise, since a data broker holds information about people with NO relationship to it, and that is why MoneyBot5000 is on the California register at all. A search of the account system returns nothing no matter what the consumer data holds. Asked them to route it to whoever handles the data broker registration and search the PEOPLE-SEARCH AND UNCLAIMED-PROPERTY records instead, using the identifiers already supplied. (2) CARD DETAILS REFUSED, with the reasoning stated: there is no charge for them to match; payment-card data is more sensitive than anything the request concerns and sits in the same category as the SSN and ID document already declined; and A PRIVACY REQUEST SHOULD NEVER END WITH THE REQUESTER HAVING HANDED OVER MORE SENSITIVE INFORMATION THAN THEY STARTED WITH. Noted their own footer says 'Please do not send your social security number, complete credit card, or pin via email. We will never ask for that information' -- so read as the billing macro firing rather than policy, but worth someone looking at, because a consumer who complies has emailed card details to a company they have no relationship with. Restated the four unanswered questions -- group scope, brand list, unclaimed-property records and retention, suppression durability -- and applied the 290 wedge for the 1798.120 opt-out, which needs neither an account nor verification. FLAG FOR THE USER: a company asked for payment card details in response to a privacy request; I declined and will not supply them.

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

