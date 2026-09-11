# TruePeopleSearch

- **Working route:** https://www.truepeoplesearch.com/privacy-rights  ← use this
- **Do Not Sell / Opt-out:** https://www.truepeoplesearch.com/removal — this DOES
  work. Earlier note said Cloudflare blocked it; see the correction below.
- **Do Not Sell:** https://www.truepeoplesearch.com/do-not-sell
- **Email: refused.** support@truepeoplesearch.com replies that it "does not process
  privacy requests received via email."
- **Priority: 5.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Reference: `TPS Right to Know ticket`
- Note: STAGE TWO CONFIRMED on-screen: 'The following information was submitted to our system successfully. We will locate and remove your record based on the information you provided. Expect your information to be fully removed in 3 days or less.' It names the record back - 'Submitted: [name] - [PERSONAL], PA [PERSONAL] | [email]' - which is the artifact. Note this is the SELF-SERVICE opt-out succeeding after the statutory Right to Know was refused on jurisdiction; two different doors, per _DEFLECTIONS.md 27.

## The circular trap — and the way out

Three routes, two of which dead-end:

1. **Email** → auto-reply: privacy requests not processed by email, use the form.
2. **`/privacy-rights` → "Right to Delete"** → *no form appears at all*, just text
   saying they can't delete third-party data, redirecting you to `/removal`.
3. **`/removal`** → Cloudflare challenge that blocks the page from loading.

**The way through:** on `/privacy-rights`, select **"Right to Know"** instead of
"Right to Delete". That reveals the full form and submits successfully. The
Turnstile widget on this page auto-passes; the one on `/removal` does not.

A Right to Know still has teeth — it compels disclosure of what they hold, creates
a dated record, and the same form offers **"I want to appeal the handling of my
privacy request"**, which gives you a documented basis to escalate.

## Form
`/privacy-rights` → Request category: *access, delete, or correct* → Request type:
**Right to Know** → Context: *no direct relationship* → First/Last/Email/
Requestor type (*subject of this request*)/Phone/Street/City/State/Zip → Submit.
Success page: `privacyrightsconfirmation?success=True`.

## Gotchas
- Their state dropdown lists **all 50 states including Pennsylvania**, even though
  their email implies only "states with a consumer privacy law" qualify. Fill it in
  regardless of state.
- They claim data "is not stored by us... retrieved from third-party data providers
  at the time you perform the search." Treat that as a position, not a fact — the
  listing still displays and still needs suppressing.

## The statutory route and the opt-out route are different doors

The "Right to Know" submission was refused on jurisdiction (see `_DEFLECTIONS.md`
§27) -- and the refusal arrived in the same minute, in the same words, from
FamilyTreeNow and PeopleSearchNow, which is the family confirmation.

Their `/removal` page is a **separate mechanism** and never asks what state you live
in. It is titled "Do Not Sell/Right to Opt-out" and it works like this, in their
words:

> *"Enter your email address and name and complete the captcha below. We will send a
> link to your email address that will take you to the opt-out form."*

> *"Click the link sent to your email. It may take some time to arrive. If you wait
> more than 24 hours to click this link you will need to request a new one."*

Two hazards in that. The link **expires in 24 hours**, so a staged request left over
a weekend is a request that has to be started again. And the first form is not the
real form -- the record details are entered at step three, so submitting step one
and stopping achieves nothing at all while looking like progress.

Their own warning is worth heeding as well:

> *"Omitting information or providing inaccurate information on the opt-out form
> will only hinder the opt-out process."*

## The page is Cloudflare-gated and slow to render

`/removal` first paints as a bare search header with an empty body, and the actual
opt-out content appears several seconds later once the bot check clears. Screenshot
too early and it looks like a broken page with no form. Wait, then look again.

## Correction: /removal is not blocked, it is slow

An earlier note in this file recorded `/removal` as "Cloudflare blocks page load".
That was wrong, and the way it was wrong is worth keeping.

The page first paints as a bare search header with an **empty body** while the bot
check runs, and the opt-out content appears several seconds later. A screenshot
taken at the four-second mark shows a page with no form on it, which reads exactly
like a block. Waiting another eight seconds shows the full "Do Not Sell/Right to
Opt-out" flow.

**A page that has not finished rendering and a page that refuses to render look
identical in a single screenshot.** When a page appears empty behind a bot check,
wait and look again before recording it as gated -- the cost is a few seconds, and
the cost of the error is writing off a working route for three days.

## The self-service door worked where the statutory one was refused

The Right to Know submission was refused on jurisdiction -- Pennsylvania has no
comprehensive consumer privacy law (see `_DEFLECTIONS.md` §27). The self-service
opt-out, which never asks what state you live in, went through the same afternoon.

The confirmation page is a real artifact rather than a pleasantry, because it **names
the record back**:

> *"The following information was submitted to our system successfully. We will locate
> and remove your record based on the information you provided. Expect your
> information to be fully removed in 3 days or less."*

followed by the submitted name, city, ZIP and email. That distinguishes a completed
submission from a form that merely accepted a POST.

**Three stages, and only the last one counts.** Name and email plus a captcha; then an
emailed link that expires in 24 hours; then the fuller form carrying date of birth,
telephone, address, city, state and ZIP. Stopping after stage one looks like progress
and achieves nothing.

Their own warning explains why completeness matters here: *"If we receive new data
connected to a record that we were unable to identify based on your original request,
information you submit here may appear on our site in the future."* Partial
identifiers buy a removal that does not stick.

## How to verify, and how not to

The confirmation page carries an unusually candid instruction about checking the work:

> *"Please make sure you clear your browser cache before attempting to confirm
> removal, or your device may pull up an old, stored version of our website. Also make
> sure you initiate a new search. Please do not attempt to verify removal by clicking
> on a saved link."*

Fresh search, clean session, live site. See `_SILENT_FAILURES.md` §31 -- a cached page
can report the removal failed when it succeeded, and a stale search-engine result can
report the opposite.
