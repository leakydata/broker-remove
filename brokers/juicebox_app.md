# Juicebox App, Inc.

- **Email:** privacy@juicebox.work (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** juicebox.ai
- **Priority: 2.**

## Status

- Current: `email_pending` (updated 2026-09-06) — Privacy Center requests filed and email-verified, awaiting substantive answers
- Reference: `gmail:1a047b6c7b819602`
- Note: Emailed privacy@juicebox.work 2026-08-28 (Juicebox App, Inc.; domain of record juicebox.ai). Standard letter plus two questions for a search product built over profile data: does deletion remove the profile or only hide it from results (both get called 'deleted'), and is the index a stored copy or assembled live from third-party sources at query time -- with query-time suppression plus upstream source names offered as the substitute if it is the latter.
- **Reply (2026-08-28): email is not the intake channel.** "We process all data privacy requests through our Privacy Center" (juicebox.ai/privacy-center) -- a mandated web form, but critically NOT a CAPTCHA-gated one and NOT account-creating, so within this project's rules to complete (see `_DEFLECTIONS.md` "we don't accept requests by email").
- **Filed 2026-09-05: all four available request types** (access/"summarize my info", do-not-sell-or-share, limit use of sensitive PI, opt-out of sensitive PI use) through the Privacy Center, deliberately in that order -- access first, because a deletion would destroy the record an access request needs to disclose. The form has no free-text/general-inquiry route that reaches a person, so the two open questions from the original email had to travel back through email instead, addressed to the same privacy@juicebox.work thread that first deflected to the form -- a workable pattern for "form-only intake, but the company still reads its inbox."
- **Self-inflicted error, worth the general lesson: used the wrong contact email on the form.** Entered a dead-mailbox search-key address instead of the live confirmation address actually read. All four Privacy Center verification emails went to a mailbox nobody checks, so all four requests would have sat unverified and silently expired, looking from Juicebox's side like four abandoned consumers. **Caught before expiry only because the mistake was reported proactively** rather than discovered by an eventual "did this ever go anywhere?" check. Juicebox's answer: they won't edit a submitted request's contact address, but refiling with the correct address does not create duplicates on their side since the originals simply expire unverified. Lesson for any form that emails a verification link: confirm which of the subject's several addresses is the one being typed BEFORE submitting, not after.
- **"Technical error" on submit was not a failure.** Filing the do-not-sell request produced "we're unable to process your request at this time due to a technical error... please try re-submitting" -- the kind of message that tells a person to assume nothing happened. A verification email for a second, unlabelled request ID arrived in the same minute from `request@datasubject.com` (their DSR processor) and verified normally when clicked. Two submissions were made, one is independently accounted for, so the "failed" one almost certainly went through anyway. **An error page is not itself evidence of failure** -- check for an unexplained side effect (a verification email, a new ticket ID) before concluding a submission needs redoing, since redoing a request that actually landed creates the exact duplicate the earlier lesson above was trying to avoid.
- **A real, useful answer on suppression architecture:** "We do not hold email addresses for the profiles in our index. Contact data is retrieved live, only when a customer requests it for a specific profile. Any email addresses you provide through a verified request are added to our suppression list, which means we will never provide them to customers." This is an EXCLUDE-ONLY suppression against a live-retrieval product, the good-outcome shape described in `_SILENT_FAILURES.md` -- confirmed rather than assumed.
- **A wording bug that undersells their own compliance:** the Privacy Center's do-not-sell/share confirmation panel tells the consumer their opt-out requires an email verification click to take effect, but Juicebox confirmed in writing that "Your Do Not Sell or Share request will be honored for the identifiers you've provided" independent of the verification step (11 CCR §7026(f) does not permit gating an opt-out on identity verification the way an access or deletion request can be). Flagged it to them as a wording problem that costs them nothing to fix and currently tells every unverified consumer their protection didn't work when it did.

## Steps

1. Email privacy@juicebox.work first if starting fresh -- it deflects to the Privacy Center, but the deflection message itself is useful (states the form is the only intake) and the inbox does keep reading follow-ups on open questions the form can't take.
2. File the Privacy Center's four request types in this order: access/summarize first, then do-not-sell-or-share, then the two sensitive-PI options -- so a deletion never precedes the disclosure it would otherwise erase.
3. Triple-check the contact email typed into the form before submitting -- it is the verification-link target, and this project's subject has multiple valid addresses that are search keys only, not mailboxes he reads.
4. If a submission returns a "technical error," do not assume it failed -- check for a verification email or new ticket ID arriving around the same timestamp before resubmitting.

## Gotchas

- **Form-only intake without a CAPTCHA is still an email-completable route** for this project's purposes -- don't treat "we don't accept requests by email" as a dead end without checking what the form itself actually gates on.
- **No free-text field on the Privacy Center** -- open questions have to go back through the original email thread, not the form.
- **Verification-link expiry is silent and asymmetric**: the company sees an abandoned request, the sender may not realize the address was wrong at all unless they think to check.

## Verification

Two of at least three filed requests are email-verified as of 2026-09-06 (access/summarize, and one other pending type confirmation); do-not-sell-or-share has an unresolved "technical error" likely masking a real, verified submission. Re-check the thread for Juicebox's answer on request-type confirmation and the outstanding upstream-source question (who supplies contact data at query time).
