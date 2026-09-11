# Arity

- **Email:** privacy@arity.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** arity.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-23)
- Reference: `KP96PDJR5Q`
- Note: 2026-08-21: OneTrust replied 'Request cannot be completed (KP96PDJR5Q) — unable to verify your identity,' pointing to an appeals web form (arity-appeals.consumerprivacyinfo.com). 2026-08-23: emailed privacy@arity.com directly (not the appeals form) declining to submit a government ID, asking what specifically failed verification and whether a lighter check (phone/ZIP on file) would work. Awaiting reply.

## Steps

1. Do not bother with a plain letter first -- `privacy@arity.com` answers by
   routing you to the intake form at `arity.consumerprivacyinfo.com`.
2. On the form: pick the state by CLICKING it out of the dropdown (see below),
   then Delete Data, then Yes on the delete declaration, then For Myself.
3. Fill name, email twice, and telephone number.
4. Leave Mobile Ad ID blank. It is optional and it is the identifier you are
   trying to break, not one to volunteer.
5. Answer the mobile-number question, tick the reCAPTCHA, Submit.

## Gotchas

The state combobox substitutes a different state if its value is set rather than
selected, and the "not for monetary value" line in their email is narrower than it
sounds. Both are covered below.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Telematics: what the form is actually asking for

Arity's own delete declaration says what the data is:

> *"Arity may have collected personal information from mobile phone applications to
> offer features such as driving behavior feedback, fuel efficiency, insurance
> offers, and driving score."*

So the record is keyed to a **phone**, not to a name -- which is why their form asks
"Is the number provided a mobile number?" and offers an optional **Mobile Ad ID**
field.

**Leave the Mobile Ad ID blank.** It is optional, and supplying it to a company that
may not currently hold it hands over a fresh identifier rather than removing an
existing one. If they hold something keyed to the device, they can find it from the
telephone number; if they cannot, the advertising ID is the link, and volunteering
it is the opposite of the request. Same reasoning as the Foursquare and CityData.AI
decisions.

## Their email answer redefines the question

> *"We do not sell personal information for monetary value."*

Note the qualifier. The next sentence gives it away:

> *"This activity may also be considered the 'sharing' of personal information,
> cross-context behavioral advertising, or targeted advertising in some
> jurisdictions."*

"Not for monetary value" is not "not sold" under the CPRA, which covers exchange for
**other valuable consideration**, and it is silent on sharing, which is a separate
right. The company is being accurate rather than evasive here -- they volunteer the
sharing point themselves -- but the first sentence is the one a reader remembers,
and read alone it means less than it appears to.

## The state field will lie to you

See `_SILENT_FAILURES.md` §24. Pennsylvania **is** in their list. Setting the field
programmatically produced "Arkansas" on submit. Click the option out of the
dropdown and re-read the field before submitting.

## After confirmation, a second gate: "unable to verify your identity"

Confirming the email did not end the process. Two days later OneTrust sent a
second message on the same request ID:

> *"Unfortunately, we are unable to verify your identity at this time. We can
> only honor requests if we are able to verify the identity of the individual
> making the request... If you would like to submit an appeal, please visit our
> Appeals webpage and include the Request ID."*

The appeals route is another web form (`arity-appeals.consumerprivacyinfo.com`),
gated behind whatever verification failed the first time — not obviously more
forgiving than the intake form.

**Do not send a government ID to clear this.** Per the project's hard rules,
that is off the table regardless of what the form asks for. Instead, wrote
directly to `privacy@arity.com` (bypassing the appeals form) asking what
specifically failed to match, and offering a lighter verification (phone or
ZIP on file) instead of a document. Awaiting reply as of 2026-08-23.

**This is worth tracking as its own failure mode**: a request can clear email
verification and still be refused at an identity-match gate with no visibility
into what mismatched. If the next reply also demands a document, record
`manual_required` and stop — that is the hard line, not a negotiating position.

