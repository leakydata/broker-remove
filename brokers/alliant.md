# Alliant

- **Opt-out:** https://privacyportal-cdn.onetrust.com/dsarwebform/591ac1c1-3a1e-496f-9e43-ff4afb5fef85/2b52262e-8ada-4725-b86e-e4b960336f96.html
- **Email:** compliance@alliantdata.com (verified)
- **Method:** web_form — Web form.
- **Domain:** alliantdata.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Reference: `gmail:1a01042e8332c7f7`
- Note: OneTrust logged BOTH requests with reference IDs and emailed them: 'Your marketing data opt out and/or marketing data deletion request has been successfully submitted. Your Request ID is 3GBWVNXAA5' and a second, A6PP4DHC2W. Two IDs for two forms, which is the artifact that proves the deletion and the opt-out were recorded separately rather than deduplicated.

## Steps

1. Email `compliance@alliantdata.com`. They reply with four OneTrust links.
2. **Take the opt-out link first** — it is the only one not behind challenge
   questions. Fill name, email and address; a visible reCAPTCHA and Submit remain.
3. **Deletion, records and correction** each need knowledge-based "challenge
   questions", so each is a separate human task.
4. **Press the suppression ask on the email thread**, not through a form — no form
   they offer expresses it, and in a co-operative it is the ask that matters most.

## Gotchas

See the two sections below: four separate forms with only the opt-out ungated, and
a co-operative suppression ask that no form on offer can carry.


## Verification

Nothing public to search. Keep the opt-out confirmation and each gated-form
confirmation **separately** — four rights means four artifacts, and a single
"your request has been processed" covers whichever one it came from.

Ask on the email thread whether a permanent suppression entry was added, since no
form captures that and a deletion alone will not survive the next member
contribution.

## Four forms, one of which is not gated

Their reply supplies **four separate OneTrust links** — opt out of sale, delete,
records, correct — so each right costs its own submission. The Data Axle and
Belardi Wong pattern again (`_SILENT_FAILURES.md` §12), in its most explicit form:
here nobody even pretends one submission covers the set.

The important asymmetry is in the gating. Their own wording:

> *"You may also utilize the following links in order to exercise your other
> rights. They will take you to verify your identity using 'challenge questions'
> which should be known by you."*

So **opt-out is ungated; deletion, records and correction sit behind
knowledge-based authentication.** That ordering is worth noticing. The right that
merely stops them selling is easy; the rights that would remove the data, or show
you what they hold, require answering questions drawn from a credit-style file.

Practically: take the opt-out immediately — it is a staged form plus a reCAPTCHA —
and treat the other three as a separate, human task. Knowledge-based questions
cannot be answered by anyone but the person, by construction.

## What their reply did not address

The original letter made one ask specific to their structure, and the reply is
silent on it. Alliant is a **co-operative**: members contribute transaction and
behavioural data and receive modelled audiences back. In that model a deletion
without a suppression entry is close to meaningless — the next member contribution
re-supplies the record, and it will have been deleted exactly as requested.

The letter said so, and offered the concession that makes it easy to grant:

> *"I understand suppression may require you to retain the minimum data needed to
> honor it. That is acceptable to me."*

No form on offer expresses that. A form-based flow can only capture the rights the
form was built for, so the structural ask has to be pressed on the email thread
regardless of which links they send. See `five_by_five.md` for the same shape at
another co-operative.

## The challenge questions do not exist

Alliant's reply routes each right to its own OneTrust form and says of three of
them:

> *"You may also utilize the following links in order to exercise your other
> rights. They will take you to verify your identity using 'challenge questions'
> which should be known by you."*

The deletion form has **no challenge questions**. It asks for first name, last
name, email, phone, country, state, address, city and zip, and then submits. That
is the same information as the opt-out form plus a phone number and a country.

This matters because the sentence is a deterrent. A challenge-question gate sounds
like knowledge-based authentication -- previous addresses, loan amounts, the kind
of quiz that is both intrusive and easy to fail on your own data. Someone reading
that line may reasonably skip the deletion link and take only the opt-out, which
is the one right Alliant volunteered without a warning attached.

**Open the form before believing the description of the form.** The cost of
checking is one page load.

## Deletion here requires retention, and that is the right outcome

The deletion form says so directly:

> *"our deletion process requires us to retain certain identifying information
> that allows us to ensure your information is not inadvertently added back into
> our database in the future. Such residual information will not be used for any
> purpose other than to ensure the continued fulfillment of your request."*

Ordinarily that sentence deserves suspicion -- see `_DEFLECTIONS.md` on suppression
being recorded as an attribute of a record that was never deleted. Here it is
exactly what to ask for. Alliant is a **co-operative**: members contribute data and
receive modelled audiences back. A record deleted cleanly, with nothing left to
match against, is a record a member re-contributes next cycle, and the deletion
silently undoes itself.

So both forms are worth submitting, and the order does not matter much, but the
**opt-out is the load-bearing one**. It is the one Alliant describes as suppression
from future sales or sharing.

