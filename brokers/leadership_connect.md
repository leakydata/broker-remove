# Leadership Connect

- **Email:** privacy@leadershipconnect.io — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** leadershipconnect.io
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Statutory delete + opt-out + suppression letter sent to the published contact, covering every prior address, prior telephone number and alternate email address rather than only the current ones.

## Steps

1. Do NOT email `privacy@leadershipconnect.io`. It hard-bounces.
2. Open `https://leadershipconnect.io/opt-out/` -- "Do Not Sell My Information".
   Enter a name and an email address; the reCAPTCHA is invisible, no challenge.
3. It returns "Please check your email for further instructions."
4. Open the emailed link. It is not a confirmation -- it is stage two of the form.
   Fill in phone, address, city, state and zip, and Submit.
5. Read the result carefully. See below: the answer is scoped to the email address.

## Gotchas

The published privacy mailbox is dead, the "confirmation" link is really a second
form, and the negative it returns names only the email address. All three are
covered in detail below.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## The published privacy address does not exist; the form does

`privacy@leadershipconnect.io` hard-bounces -- *"Address not found"*. There is no
point retrying it.

Their site carries a working route that the registry did not: **`/opt-out`**,
titled "Do Not Sell My Information". It asks for a name and an email address and
nothing else, which is a genuinely minimal ask, and it carries an invisible
reCAPTCHA -- a badge, not a challenge, so it submits without a human step.

On submit it returns:

> *"Please check your email for further instructions."*

**That sentence is the whole risk.** A confirmation link is coming, and until it is
clicked the request does not exist. This is the first and most expensive silent
failure in `_SILENT_FAILURES.md`: an unconfirmed request is indistinguishable from
a submitted one from the sender's side, and it looks *more* finished, because a
form said something reassuring.

So the status here is not "done" until the email arrives and the link is clicked.

**The general lesson.** A hard bounce on the published privacy address is a reason
to go look at the site, not a reason to record the broker as unreachable. The
opt-out page was one level down from the homepage and was never linked from the
privacy policy that named the dead mailbox.

## The confirmation link is not a confirmation

Clicking *"Click to proceed with your optout request"* does not confirm anything.
It opens a **second, longer form** -- name and email pre-filled from stage one,
then phone, address, address 2, city, state and zip.

So the two-stage design is not verification-then-submit. It is
collect-a-little-then-collect-a-lot, with the email round trip in between proving
control of the mailbox as a side effect. Worth knowing before deciding whether to
supply the second tranche: at stage one they had a name and an email, and at stage
two they are asking for a street address and a telephone number they did not
previously have.

## The answer names one identifier, and the form collected seven

On submit:

> *"We have no record of &lt;the email address&gt; in our service."*

That is **not** the same statement as "we have no record of you", and the gap
between the two is the whole point. The form had just been given a name, a
telephone number, a street address, a city, a state and a zip. The answer mentions
none of them. Either the lookup is keyed on email alone -- in which case six of the
eight fields were collected for nothing -- or the lookup was broader and the
*message* is narrow. From outside there is no way to tell, and both readings mean
the negative covers less than it appears to.

**Why it matters here in particular.** Leadership Connect is a directory of
government and corporate leadership. A record about a person in that database would
be keyed to their professional identity -- a work email address, an employer, a
title -- not to a personal Gmail account. Searching a leadership directory by
someone's personal webmail and reporting no match is close to the least likely way
to find them.

So this is recorded as `not_found` **with the qualifier attached**, not as a clean
negative. See `_SILENT_FAILURES.md` on answers phrased more broadly than the
question, and on scoped negatives: the noun in the sentence is the thing that was
actually searched.

**Testing another address costs a round trip.** Each run emails its confirmation to
whatever address was entered at stage one, so checking a work or university
address requires access to that mailbox. That is a judgement call rather than a task, and it is
queued as one.

