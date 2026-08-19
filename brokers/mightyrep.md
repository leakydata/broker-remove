# Mightyrep

- **Email:** privacy@MightyRep.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** mightyrep.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: privacy@mightyrep.com hard-bounced 'address not found'. Only contact published anywhere on their site is a NAMED INDIVIDUAL at their own domain, in the site footer beside the privacy policy - which is different from the stranger's-personal-address case verify_emails guards against, because this is the company's own published contact. Wrote to it, apologised for using a named address, and asked him to pass it on and to get the privacy mailbox fixed.

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

## The bounced address is the state-registered one

MightyRep's CA data broker registration (oag.ca.gov/data-broker/registration/564387,
approved 2023-03-16) lists `privacy@mightyrep.com` as the contact - the exact
address that hard-bounces "address not found". So the earlier note about writing
to a named individual in the footer was working around a genuinely dead official
channel, not a wrong guess. Fallback web route: `https://www.mightyrep.com/contact`
(untested; needs a human, no CAPTCHA info known).

## "We are not a data broker" from a B2B lead-generation tool (updated 2026-08-19)

`privacy@mightyrep.com` hard-bounces. The only other published contact is a named
individual, so the request went there with an apology for the informality and a
request to treat the dead mailbox as a fault report. He answered within a day,
personally, and said he would look at it — which is more than most.

The substantive answer was the category refusal:

> "MightyRep doesn't aggregate any data, buy lists, and is not a data broker.
> This is a B2B tool to capture businesses publicly available information and is
> not allowed to capture private information on consumers."

### Why this is worth one push rather than acceptance

Nothing in that sentence is implausible, and arguing about the label "data
broker" is a waste of both parties' time. The load-bearing move is elsewhere: it
slides from **"business information"** to **"not personal information"**, and
those are different categories.

> **A B2B contact record is almost always a named human being.** A person's name,
> their work email, their direct line, their title, their employer. Every one of
> those is personal information *about that person*. "It is business data"
> describes the context in which it was collected, not the category it falls into.

And the statutory hook that people still get wrong: California's business-to-
business carve-out **sunset on 1 January 2023 and was not renewed**. Since then a
work address in a prospecting database has the same status as a home address in a
people-search database.

### The reply that gets an answer instead of an argument

Do not re-litigate the label. Narrow to the one question a search can settle:

> Does the company hold a record — in the product, in a CRM, in an enrichment
> cache, or in a suppression list — keyed to the name, to any listed email
> address, or to any listed telephone number?

Then explicitly hand them the cheap exit: *an unqualified "we searched those
identifiers and hold nothing" is a complete answer and closes it.* That converts a
defensive exchange into a one-minute lookup, and it is the honest outcome in most
of these cases.

> **Offer the null result as a win.** A company that believes it holds nothing
> will happily say so in writing if saying so ends the correspondence. A company
> that will not say it in writing has told you something.

### The fault report is part of the request

Worth restating to whoever answers, because they are usually the only person who
can fix it: a *published* address that hard-bounces is worse than no address at
all. From the sender's side a bounce that they never see and a request that was
received and ignored are the same event. Nobody finds out.

See [[_DEFLECTIONS]] for the wider family of scope refusals and
[[_SILENT_FAILURES]] for published-but-dead contacts.
