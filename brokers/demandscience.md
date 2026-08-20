# DemandScience

- **Opt-out:** https://demandscience.com/privacy-policy/ → the *Privacy Rights Request Form* anchor (a PrivacyEngine-hosted form, not a form on their own site)
- **Email:** alerts@support.privacyengine.io is outbound-only; correspondence comes from "Global Data Privacy, Legal & Compliance Office, DemandScience"
- **Method:** web_form (third-party rights platform: PrivacyEngine)
- **Domain:** demandscience.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20) — request submitted and **email verified**

## How this broker was found

Not from any broker list. Terminus named DemandScience when asked where its data
came from — the supplier-disclosure technique in `_SILENT_FAILURES.md` §74. It
was absent from the registry entirely, which is the point of asking: a reseller
knows its upstream, and no public list does.

DemandScience is a B2B intent and contact-data business (previously PureB2B /
Leadiro). Its records are keyed to *work* identifiers, so read `leadiq.md` and
`_DEFLECTIONS.md` §44 before concluding a null result means anything.

## Finding the form (the part that wastes an hour)

The privacy page has three visible forms on it. **None of them is the rights
form.** Two are site search, one is a newsletter signup. The actual route is a
single text anchor in the running prose that leaves the domain entirely for
`portal.privacyengine.io`.

This is `_SILENT_FAILURES.md` §71 — a rights page with no rights form on it. The
practical rule that came out of it: **run the anchor sweep unconditionally**, not
only when no form is found. Counting forms on the page is the wrong test, because
the page can be full of forms and still have no route.

## The form demands things a member of the public does not have

See `_DEFLECTIONS.md` §43. The PrivacyEngine form requires a **Business Email
Address** and an **employer**, and its "Category of Data Subject" select offers
only: Current Employees, Former Employees, Job Candidates, Shift Workers,
Customers, Suppliers, Students, and "USA". There is no option for *a member of
the public whose details you bought from someone else* — which is what almost
everyone submitting the form actually is.

**Fill it, pick the least-wrong option, and disclaim the selection in the free
text.** Do not abandon the form over an unanswerable dropdown; a submitted form
with a stated caveat is worth infinitely more than an unsubmitted one, and the
caveat is what stops the selection being read back as a claim you made.

## Verification is required or the request is void

PrivacyEngine sends a verification link to the address on the form:

> *"Please verify your email address by clicking on the link below"*

Clicked 2026-08-20; the portal returned **"Your request has been successfully
verified."** under a "Request Received!" heading. No reference number is issued
at any point, which is worth knowing in advance — the verification page is the
only artifact there will be until they reply, so record the timestamp.

An unverified request is not a slow request, it is no request. Same failure mode
as Growbots (see the handoff queue) where the confirmation went to a mailbox the
requester had to open separately.

## What their acknowledgement actually promises

Quoted, because the suppression sentence is better than most and worth holding
them to:

> *"In the event that an individual has made an Opt-Out or deletion request, we
> retain an email address and phone number (if one is in our database) in a
> secure suppression file, which ensures that the data is not sold or processed
> for marketing, or other purposes in the future. This is processed under the
> legal basis of Legal Obligation."*

Three things to note:

1. **This is standing suppression, not point-in-time removal** — stated
   unprompted, which is rare. It is the answer to the question most brokers
   dodge.
2. **The retained fields are email and phone only.** So the suppression key does
   not include name or postal address, and a record arriving from a supplier
   under a work email not in the file would not be caught. Worth asking about.
3. **"Should we hold any"** in the preceding paragraph is the usual hedge. It is
   not a denial and should not be recorded as one.

## Verification

No public listing to re-check. The verification page is the only artifact so far.
If a reply names what was held, record which identifiers matched — for a B2B
intent business the interesting answer is whether they hold a work address, an
employer, and intent/topic scores, since those are inferred fields that no
consumer-shaped search would surface.
