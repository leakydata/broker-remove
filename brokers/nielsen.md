# Nielsen

- **Email:** privacy.department@nielsen.com — delivers, auto-replies with a menu
- **Method:** email, then a OneTrust webform (the German tenant, `privacyportal-de`)
- **Domain:** nielsen.com
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-08-19) — email verification link clicked; OneTrust returned a confirmation page
- Form filled and verified with the full request in the free-text field. A
  distorted-text CAPTCHA is all that remains.

## Steps

1. Write to `privacy.department@nielsen.com`.
2. The auto-reply is a **menu of four routes, and only one of them is the rights
   process.** The other three are device or browser opt-outs:
   - `priv-policy.imrworldwide.com/priv/optout/digital-optout.html` (Digital
     Measurement, per-device)
   - the "Your Choices" section of the Marketing Cloud privacy statement
   - the NAI mobile opt-out page, which is an industry page and not theirs at all

   The rights portal is the last link in the message, introduced by
   *"Depending on your country (or U.S. state) of residence, there are laws..."*.
   **Take that one.** The others change a preference; they do not touch a record.
3. On the form: choose who you are, then First/Last/Email/Country. Selecting
   *United States* is what reveals State, ZIP, and the request-type selector —
   which includes **Delete my personal information**.
4. The **Request Details** box takes 5,000 characters. This is the useful part of
   the form: the whole letter fits, so nothing has to be dropped to fit a portal.
5. Submit is gated on a distorted-text CAPTCHA. Ignore the file-upload box; no
   document is required.

## Gotchas

**The form's own taxonomy has no slot for most of the people in the data.**
"I am a (an)" offers: *Prospective Employee, Former Employee, Panel Member, Former
Panel Member, Survey respondent, Other.* Every option presumes a prior
relationship with Nielsen — and the introduction reinforces it, asking for
*"any current or former interaction you have had with us."*

But Nielsen Marketing Cloud holds audience data about people who have never
interacted with Nielsen in any way. That is most of the people it holds data
about. The only available answer is *Other*, and it is worth saying so in the
free text rather than letting the form's framing stand: a request filed as
"Other" by someone with no relationship reads as a stray enquiry unless it
explains that the form had no honest option.

The same shape shows up elsewhere and is worth recognising: **a rights form built
from the customer-relationship side of a business, applied to the data-broker
side of the same business.** The questions it asks are the questions a panel
administrator would ask, not the ones an audience-data controller should.

**Scope the request across the entities by name.** Nielsen is several businesses.
Naming Nielsen Marketing Cloud (and Exelate-derived audience data) and Nielsen
Digital Measurement / imrworldwide.com explicitly costs one sentence and closes
the gap where a search of the panel systems alone comes back clean and honest.

**The email route survives the auto-reply.** *"If your request is not addressed by
the information above, we will route your email to the appropriate Nielsen support
team."* So the letter is not foreclosed by using the portal, and both can run.

## Verification

Nothing publicly searchable. Evidence is limited to their written answer, so the
two questions worth insisting on are which identifier types they matched on, and
which parts they hold as processor rather than controller.

## Verified: request RZ3AZVMFVW (updated 2026-08-19)

The OneTrust flow completed its email-confirmation step. The link returned:

> "Your request is confirmed! We will review your request and contact you
> shortly."

Request ID **RZ3AZVMFVW**, type *Delete my personal information*, submitted
2026-08-19 13:23 UTC, footer attributing it to **The Nielsen Company (US) LLC**.

Two details worth carrying forward.

**The tenant is the European one.** The confirmation link resolves on
`privacyportal-de.onetrust.com`, not the `.com` US tenant that most US brands use.
That is not a mistake to correct — it is simply where Nielsen's instance lives —
but it matters when matching a confirmation email to the request that produced it,
because the two tenants issue independent request IDs and a request lodged on one
is invisible on the other.

> **The OneTrust tenant is part of the request's identity.** "Request ID
> RZ3AZVMFVW" is only unique within its tenant. Record the hostname alongside the
> ID or a later follow-up has nowhere to go.

**The confirmation echoes the submission back, masked.** The mail reprints every
field as `XXXhan`, `XXnes`, `XX013` — first and last letters visible, middle
replaced. That is enough to verify the right record was created without exposing
the values, and it is a decent pattern. It also means the confirmation email is
safe to quote in a public write-up in a way the original submission is not.

See [[_SILENT_FAILURES]] and [[_BROKER_FAMILIES]].
