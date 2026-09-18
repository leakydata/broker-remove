# Nielsen

- **Email:** privacy.department@nielsen.com — delivers, auto-replies with a menu
- **Method:** email, then a OneTrust webform (the German tenant, `privacyportal-de`)
- **Domain:** nielsen.com
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-09-02)
- Reference: `RZ3AZVMFVW`
- Note: REVERTED 2026-09-02, SAME DAY (SILENT_FAILURES 287). I moved this row to email_pending an hour earlier on the strength of an unconfirmed-looking verification email sitting in the inbox. THE ROW'S OWN HISTORY ALREADY SAID THE VERIFICATION WAS COMPLETED -- variously 'email verification clicked', 'Your request is confirmed!', 'successfully verified', or a later substantive reply that could only have followed confirmation. A verification mail stays in the inbox forever because nobody archives it; ITS PRESENCE IS NOT EVIDENCE THAT IT WAS NEVER USED. Nine of the ten rows I downgraded were already verified. Restored to submitted, which is what the evidence supports.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** eXelate, Inc.
- **Trading as:** Nielsen Marketing Cloud
- **Registered address:** 675 Avenue of the Americas, New York, NY, 10010
- **Filed contact email:** privacy.department@nielsen.com
- **Filed phone:** (410) 717-7134
- **Website:** www.nielsen.com

*Source: `data/registries/registry.csv`.*

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
