# Leadership Connect

- **Email:** privacy@leadershipconnect.io — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** leadershipconnect.io
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-09-05)
- Note: 2026-09-05 (§337): THE FORM ANSWERED A QUESTION THE EMAIL COULD NOT -- 'This is a duplicate optout request.' After privacy@leadershipconnect.io hard bounced, I went looking for another route. THREE ARE PUBLISHED AND ONLY ONE WORKS: the privacy policy's DSAR link (/dsar/) REDIRECTS TO THE HOMEPAGE; the 'Privacy Portal' page offers only a POSTAL ADDRESS for the Chief Privacy Officer in Washington DC; and the footer's Do Not Sell link (/opt-out/) is a live two-field form -- name and email, invisible reCAPTCHA, no challenge to solve. Submitted it and the page returned 'This is a duplicate optout request.' THAT IS CORROBORATION IN THE §138 SENSE: it is a fact only a pre-existing record could have produced, and it means an opt-out for this address IS on file -- so the earlier work on this row, adopted from the shared ledger with no detail, did land, and it landed through the form rather than the dead mailbox. Recorded confirmed on that basis. THE LIMITS, STATED: it confirms an OPT-OUT keyed to ONE EMAIL ADDRESS. It says nothing about deletion, nothing about the fifteen prior addresses, and nothing about the former public office that §331 argued would be the likeliest key in a directory of people in ROLES. Those remain unasked, and with the email route dead and the form taking only two fields there is currently no channel that can carry them -- the postal address is the only one left. Registry corrected: email_to cleared, method web_form, optout_url set.

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


## 2026-08-20: the negative was scoped to one address, and the plan to test a second one died

The opt-out returned:

> *"We have no record of [EMAIL] in our service."*

The plan was to re-run the form with the institutional address, since a
government-and-corporate leadership directory keys records to a **work**
identity — an employer address, a title, an organisation — not to personal
webmail. A lookup on a gmail address is a real search on a key the index does
not use, and returns a true nothing whatever they hold.

**That plan is dead.** The confirmation link goes to whichever address is typed
into the form, so a second address can only be tested by someone who can read
its mail. The institutional mailbox is closed.

Same shape as `growbots.md`: the confirmation channel and the search key are the
same field, so an address you cannot read is an address you cannot use — even
though it is the only one likely to match.

**Taken back to email, with a caveat.** There is no email route: the published
`privacy@leadershipconnect.io` hard-bounces, and a fresh sweep of both
`leadershipconnect.io` and `leadershipconnect.com` found **no published address
of any kind** — not a privacy contact, not a support address, nothing. So the
follow-up went to the `noreply@` address that sent the negative, on the reasoning
that a bounce is itself a finding and the send costs nothing.

**What it asks:** search the name, date of birth, current and prior addresses and
the eight telephone numbers, rather than the email address. And it offers three
acceptable answers, including the one that is bad for me — *"our index is keyed
to work identity and we cannot search those fields"* — because that answer tells
me the negative I already hold means less than it appears to, and converts the
ask into a suppression request instead.

**Handoff item cleared.** It asked the user to decide whether a psu.edu round
trip was worth it. It isn't available, so the decision no longer exists.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Leadership Connect
- **Registered address:** 1667 K St., NW, Washington, DC 2006, United
  States
- **Filed contact email:** privacy@leadershipconnect.io
- **Website:** http://leadershipconnect.io
- **Opt-out route they filed:** California consumers may now easily
  submit an opt-out request by submitting an online request via our
  webform, found here:
  https://www.leadershipconnect.io/privacy-portal/california-consumers-protection-act-ccpa-supplement/
  or calling us @ 1-800-627-0311. Mail requests need to be sent to the
  Chief Privacy Officer, 1667 K St, NW, Washington, D.C., 20006. Detailed
  information and instructions on how a California consumer may exercise
  their rights under CCPA can also be found in our Privacy Policy
  https://www.leadershipconnect.io/privacy-portal/. Please describe your
  request with sufficient detail that allows us to properly understand,
  evaluate, and respond to it. As required by law, we may take steps to
  verify your identity before granting you access to your information or
  completing your request to exercise your rights. Under CCPA regulations
  we will acknowledge your request within 10 days and confirm this has
  been done within 45 days of your request submission. We do not charge a
  fee for processing your request to exercise your rights.
- **Route for protected individuals:** California consumers and/or
  elected or appointed officials may submit an opt-out request online via
  our webform, found here:
  https://www.leadershipconnect.io/privacy-portal/california-consumers-protection-act-ccpa-supplement/
  or calling us @ 1-800-627-0311. Mail requests need to be sent to the
  Chief Privacy Officer, 1667 K St, NW, Washington, D.C., 20006. (Cal.
  Gov. Code 6208.1(b) / 6254.21(c)(1) — for survivors of domestic
  violence, stalking and similar, a stronger and faster route than the
  ordinary consumer request)
- **What they say they collect:** A complete overview of Leadership
  Connectâ€™s data collection/processing practices can be found at
  https://www.leadershipconnect.io/privacy-portal/. Although Leadership
  Connect does not collect information directly from consumers. We are a
  business-to-business service provider.

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
