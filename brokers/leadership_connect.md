# Leadership Connect

- **Email:** privacy@leadershipconnect.io — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** leadershipconnect.io
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Statutory delete + opt-out + suppression letter sent to the published contact, covering every prior address, prior telephone number and alternate email address rather than only the current ones.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

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

