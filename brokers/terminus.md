# Terminus

- **Opt-out:** https://portal.privacyengine.io/app/0CEB4BAE-BBE7-4DD9-BD70-4E2DBB01D64D/4F5BED3F-8BFB-4BF4-A1F8-8A2261BDE0CE
- **Email:** privacy@terminus.com — no address published on any reachable page
- **Method:** web_form (third-party portal, reCAPTCHA v2 at submit)
- **Domain:** terminus.com → demandscience.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Submitted and email-verified 2026-08-20. Awaiting substantive response.

## Steps

Finding the route took three redirects and one dead end, so in order:

1. `terminus.com` privacy links redirect to `demandscience.com`. Terminus was
   acquired; the brand still exists, the privacy function does not.
2. `terminus.com/privacy-rights/` **404s.** This is the dead end — it is linked
   from Terminus pages and does not exist.
3. `demandscience.com/privacy-rights/` returns 200, titled "California Consumer
   Privacy Act (CCPA)". **There is no rights form on it.** It has three `<form>`
   elements: two copies of the site-search box and a newsletter signup. See
   `_SILENT_FAILURES.md` §71 — counting forms is not finding the right one.
4. The actual mechanism is a single anchor in the body text, "Click here to
   submit a Data Subject Rights Request", pointing at a **PrivacyEngine** portal.
5. That portal is a real, working form. Fill it, then hand off the reCAPTCHA.

## Gotchas

**Do not conclude the vendor from a substring match.** Scraping the rights page
for known privacy vendors hits `trustarc` — that is the cookie banner. The
rights vendor is PrivacyEngine. Resolve the vendor from the link the rights text
points at, not from anything else on the page.

**The form is built for corporate data subjects, not consumers.** Mandatory
fields include *Business Email Address*, *What is the name of the company you
work for?*, and two *Business Phone* fields. The mandatory *Category of Data
Subject* dropdown offers only: Current Employees, Former Employees, Job
Candidates, Shift Workers, Customers, Suppliers, Students, "USA". None describes
a member of the public whose data was compiled without any relationship — which
is every consumer writing to a data broker. Handling in `_DEFLECTIONS.md` §43:
complete it, pick the least-wrong option, and disclaim the selection explicitly
in the free text so it is not later read as an admission of a commercial
relationship.

**One request type only.** The radio group is single-select across know /
rectify / delete / object-and-opt-out. Select deletion and record the opt-out in
the Request Details as an additional request, stating that the form permitted
only one selection.

**Ask explicitly whether it reaches Terminus.** The portal is branded
"Privacy Rights - Demand Science US, LLC". Because Terminus's own route is a
404, this portal is the only apparent path to Terminus records, but nothing on
the form says it covers that brand. Put the question in the free text and ask
for an explicit yes or no — a removal scoped to one brand of a group is
indistinguishable from a complete one until somebody finds you on a sibling
(`_DEFLECTIONS.md` §40).

**Field names are numeric and unstable.** The inputs are named `10652`, `10661`,
`Email_10653` and so on — form-builder IDs, not semantic names, and they will
differ on any other PrivacyEngine tenant. Do not hardcode them. Derive labels by
walking the DOM in document order and pairing each text node with the next input:
several fields have no `<label for>` at all, so `element.labels` returns nothing
and a naive label lookup yields only `"*"`.

**There are two DOB inputs** (`Date_10654` and `peDate_10654`) and two separate
phone country-code selects. Fill both of each; leaving the shadow copy empty
fails validation with no visible message.

**Verification is by email.** The page states: "You will receive an email to
validate your privacy rights request. We can not proceed until we have valid
verification." Expect a confirm link after submission.

## Verification

Watch for the PrivacyEngine validation email, click through it, then watch for a
response naming which brands the request covered. If the reply is scoped to
Demand Science only, write back asking specifically about Terminus.

## Outcome: submitted, verified, and an unprompted answer to the hardest question

The staged form was submitted by a human (reCAPTCHA + Submit), and the emailed
verification link was clicked the same hour. The portal confirms:

> "We have received your 'Right to Erasure (Right to be Forgotten)' Request, and
> will be in touch shortly."

**The verification email is the interesting part.** Before verification, before
any search, their autoresponder volunteers this:

> "In the event that an individual has made an Opt-Out or deletion request, we
> retain an email address and phone number (if one is in our database) in a
> secure suppression file, which ensures that the data is not sold or processed
> for marketing, or other purposes in the future. This is processed under the
> legal basis of Legal Obligation."

That is the answer to the question this project asks nearly every broker and
almost never gets: **is this a suppression that survives the next ingest, or a
one-time removal?** They say suppression, name the retained fields (email and
phone), explain the mechanism (not sold or processed in future), and give the
legal basis — unprompted, in a template, to someone who had not yet asked.

Worth holding onto for two reasons. First, it means no follow-up is needed here.
Second, it is the shape to quote at brokers who treat the question as unanswerable
or as an accusation: a suppression file that retains the minimum identifiers
needed to stay suppressed is the *correct* answer, it is easy to state, and one
data vendor states it in an autoresponder.

**Note the tension it also concedes**, and do not pretend otherwise: a deletion
request results in their retaining an email address and a phone number
indefinitely. That is legitimate and necessary — a suppression list that forgets
you cannot suppress you — but it means "deleted" and "no longer held" are not the
same state, and their wording is honest about which one applies.

**Still unanswered:** whether this covers Terminus records specifically. The
portal is branded "Demand Science US, LLC", the question was put in the Request
Details free text, and the response so far is a generic acknowledgement. That is
the thing to watch for in the substantive reply.
