# Driveniq

- **Email:** support@drivenIQ.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** driveniq.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: VisitIQ side of the same desk refused email: 'we do not process data requests via email. Please navigate to https://visitiq.io/data-rights-and-privacy/'. That page is a Ketch privacy centre containing ONLY prose - heading, two paragraphs, an Exit button, a link to Ketch's marketing site. No form, no request types, no submit. Their footer link labelled 'Opt-Out Form' points at the SAME page. Closed loop. Reported it, offering three acceptable answers: process from email, send a working form link, or state plainly they decline requests from states without a comprehensive statute.

## Steps

1. Email `support@driveniq.com` with the identity-resolution framing below.
2. Ask for deletion of the **identifier graph**, not just the named record.
3. Ask them to search **hashed** forms of every email address.
4. Ask which clients and platforms the data was syndicated to.

## Gotchas

The product here is not a list of people; it is a set of **links between
identifiers** — this hashed email is that device is that household is that
address. Once you see that, the standard deletion request is obviously
insufficient: delete the name and the edges remain, ready to be re-attached to a
name the next time one arrives.

So the request has to name the graph explicitly: device identifiers, mobile
advertising IDs, cookie IDs, IP-derived household associations, hashed
identifiers, **and the linkage records joining them**. Ask for the linkages by
name, because a company answering literally will delete what you asked for.

**Hashed identifiers are the specific trap.** A truthful "we have no record of
that email address" is entirely compatible with holding its MD5 and SHA-256
digest — which is the same record under a different key, and is how these
businesses exchange identity in the first place. Ask for hashed forms to be
searched, in those words.

Also ask for **inferred attributes**: income and vehicle estimates, life-event
predictions, propensity scores, segment memberships. Nobody supplied those; the
system generated them about you, which makes them personal information about you.
Deleting the fields a person could have provided while keeping the model output
is not deletion. See `_CATEGORY_VARIANTS.md` on identity-keyed brokers.

## Verification

Nothing public to search — you cannot look yourself up in an identity graph,
which is exactly why the written answer carries the whole weight.

Ask for the confirmation to name the **identifier types** deleted and the
downstream recipients notified. "Your data has been deleted" from a company whose
product is linkage does not say whether the linkage went with it.

## VisitIQ: the page they send you to has no form on it

The DrivenIQ and VisitIQ names share a support desk, and the VisitIQ side answers
email with a refusal:

> *"we do not process data requests via email. Please navigate to
> https://visitiq.io/data-rights-and-privacy/ to review and submit your data
> request"*

That page opens a **Ketch** privacy centre whose entire content is prose: a heading,
two paragraphs, a section called "About Your Privacy". The only interactive elements
are an Exit button and a link to Ketch's own marketing site. No form, no request
types, no fields, no submit control.

Their main site's footer carries a link labelled **"Opt-Out Form"**. Its href is the
same URL. So the link named "Opt-Out Form" leads to a page with no opt-out form on
it.

Email refused, plus a named route with no mechanism, is a **closed loop** -- and from
the consumer's side it is indistinguishable from being ignored.

## The likely cause, and how to report it

Ketch privacy centres are commonly configured to render rights options only to
visitors whose jurisdiction matches a configured regulation, falling back to
informational text otherwise. If so, the page is working exactly as configured and
the **configuration** is the fault, because the refusal email sends everyone there
regardless of where they are.

Phrase the report accordingly. *"Your page is broken"* invites a reply saying it
works fine -- which will be true when they test it from a covered state. *"Your page
renders no form for a visitor outside a covered jurisdiction, and your email sends
those visitors there anyway"* is the accurate version, and it cannot be answered
with a screenshot.

Offering three acceptable outcomes also makes it hard to leave unanswered: process
from email, send a working link, or say plainly that requests from residents of
states without a comprehensive statute are declined. The third is a legitimate
position and recording it is a real result -- what cannot be worked with is a route
that silently cannot accept the request.
