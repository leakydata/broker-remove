# eMerges.com

- **Email:** ~~data@emerges.com~~ — **hard-bounces 550, do not use.**
- **Method:** web_form — a Google Form is the only route found; no working email.
- **Opt-out:** https://docs.google.com/forms/d/e/1FAIpQLSdi3KjEPMsVnXQL-KllxvgOQWxvLpLfuz30-Z_eqXDHGEbX6w/viewform ("Remove Me/Opt Out", linked from their privacy policy)
- **Domain:** emerges.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-28)
- Reference: `gmail:1a041c369d5cdf43`
- Note: 2026-08-28: The 2026-08-27 first-contact letter (reasoning below, kept because it's the right argument if email ever works again) looked like a normal submission and was logged `submitted` — it had in fact hard-bounced the same day (550, address not found). Checked the site directly: emerges.com's own homepage now states **"As of July 1, 2025 eMerges ceased operating as a List Broker"** and that "eMerges is neither acquiring, publishing, processing or selling any lists," adding that **"the opt out resource has been disabled."** But the privacy policy page, fetched separately, still links a live "Remove Me/Opt Out" Google Form, and a `/contact/` page with a working contact form also exists. That's a contradiction worth putting to them directly — a cessation notice that disables an opt-out mechanism can plausibly mean "we no longer need an opt-out because we've stopped," but the linked form still being live says otherwise. No working email address exists (data@ hard-bounces, and no other address is published anywhere on the site), so the remaining routes are both web forms — out of this project's email-only reach. Queued for a human.

## Steps

**No email route works.** `data@emerges.com` hard-bounces and no alternate
address is published anywhere on the site.

1. Try the "Remove Me/Opt Out" Google Form linked from the privacy policy
   (URL above) first — ask it to confirm cessation as a list broker, whether
   any historical data was purged or transferred/sold to a successor and to
   whom, and to process a deletion regardless.
2. If that form itself is dead (their own homepage claims it's "disabled"),
   fall back to the `/contact/` form at emerges.com/contact/ (Full Name,
   Phone, Email, Subject fields) with the same three questions.

## Gotchas

**A bounced send can still get logged `submitted`.** This entry was marked
`submitted` on the same day the letter hard-bounced — the send succeeded, the
delivery didn't, and nobody checked the bounce folder before recording the
status.

**"We ceased operating" is not the same claim as "we hold nothing."** eMerges
says it stopped operating as a list broker on 2025-07-01 and disabled its
opt-out resource — but the resource it named is still linked and live on its
own privacy policy page. Take the cessation claim as a starting point for a
question (what happened to data already collected? sold, transferred,
purged?), not as a completed removal.

**Email-append business — argue the derived record, not just the address.**
The email address in an append file is not something the subject gave anyone
— it's output the system produced, matched, constructed or inferred from a
name+postal record. Consequences worth keeping in any letter here if the
email route ever reopens: (1) search on the *addresses*, since the file is
keyed name+postal with email as output — an email-only search can return
nothing while a record exists; (2) he cannot enumerate addresses he never
owned, and a *wrong* appended address is arguably worse, since mail sent to
it reaches a stranger; (3) suppression must be keyed to name+address, because
an append begins from those and produces the email at the end — suppressing
the output alone doesn't stop the next run producing it again.

## Verification

No confirmation received yet. If the web form is completed, their stated
timeframe (if any) should be recorded here once known.
