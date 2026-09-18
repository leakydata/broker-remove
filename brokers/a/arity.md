# Arity

- **Email:** privacy@arity.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** arity.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-09-02)
- Note: Test reverted; row restored to submitted, which the history supports (OneTrust verification clicked 2026-08-18 and the portal returned 'Your request is confirmed!').

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Arity 875, LLC
- **Registered address:** 222 W Merchandise Mart Plaza, Suite 875,
  Chicago, IL 60654, United States
- **Filed contact email:** privacy@arity.com
- **Website:** https://www.arity.com
- **Opt-out route they filed:** California consumers may opt out of the
  sale of their personal information by selecting the link toward the
  bottom of the Arity website www.arity.com or via Arityâ€™s privacy
  statement. Arityâ€™s sharing that may be considered a sale of personal
  information is limited.
- **Route for protected individuals:** California consumers may exercise
  their deletion right by visiting arity.consumerprivacyinfo.com or
  emailing us at [named individual]@arity.com. (Cal. Gov. Code 6208.1(b)
  / 6254.21(c)(1) — for survivors of domestic violence, stalking and
  similar, a stronger and faster route than the ordinary consumer
  request)
- **What they say they collect:** Arity uses advertising identifiers
  associated with consumerâ€™s mobile device (commonly known as a Mobile
  Ad ID) to serve third-party interest-based advertising based on their
  driving habits. Under California law, sharing these unique advertising
  identifiers for online advertising may be considered a â€œsaleâ€ of
  information. Except for this kind of sharing, Arity does not sell any
  personal information.

*Source: `data/registries/complete-reg-data-brokers.csv`.*

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
