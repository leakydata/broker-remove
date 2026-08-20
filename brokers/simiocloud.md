# Simiocloud

- **Email:** Privacy@simiocloud.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** simiocloud.com
- **Priority: 2.**

## Status

- Current: `captcha_blocked` (updated 2026-08-20)
- Note: Autoreply refused the emailed request -- 'your request was not submitted in the manner required by our Product & Services Privacy Policy' -- but pointed to a genuinely good route and described their business: data-driven marketing to 'existing and prospective donors and customers'. KEY POINT, quoted: 'Consumers, REGARDLESS OF THEIR STATE OF RESIDENCE, may opt-out of SimioCloud's database at any time and at no cost via our website: simiocloud.com/optout. Exercising this opt-out right will prevent SimioCloud from selling your personal information, processing your personal information for targeted advertising or profiling, and will result in the removal of your personal information from SimioCloud's database.' That is broader than most state-gated routes and sidesteps the Pennsylvania problem entirely. Separate state-gated deletion and access forms exist at /deletion-form and /access-form for residents of covered states. WPForms form staged with both opt-out boxes ticked; reCAPTCHA handed off. GOTCHA: the form carries a wpforms[hp] HONEYPOT field labelled 'Email' -- it must be left blank or the submission is silently treated as spam.

## Steps

1. Email `privacy@simiocloud.com` if you like, but it will not process the request —
   the autoreply says the request "was not submitted in the manner required by our
   Product & Services Privacy Policy". It is still worth sending, because the
   autoreply itself carries the routing below.
2. **Use `simiocloud.com/optout`.** This is the broad route and it is open to
   everyone — see Gotchas.
3. Select **Myself**, then first / middle / last / email / confirm email / phone /
   address / city / state / zip.
4. **Tick BOTH boxes**: "Opt-out of promotional communications" *and* "Opt-out of
   SimioCloud products". They are separate rights on one form.
5. Solve the reCAPTCHA and submit.
6. Only if you live in a covered state, the narrower statutory routes are
   `simiocloud.com/deletion-form` and `simiocloud.com/access-form`.

## Gotchas

- **There is a honeypot.** The form carries a hidden `wpforms[hp]` field *labelled
  "Email"* near the bottom. It must be left blank — filling it silently marks the
  submission as spam, with no error shown. Anything auto-filling every field by
  label will trip it.
- **Both tick-boxes, not one.** Promotional communications and product inclusion are
  separate, and only ticking the first leaves the data in the products.
- The state-gated `/deletion-form` looks like the "real" statutory route and is
  therefore tempting, but for a resident of a state without a comprehensive privacy
  law it is the *worse* option — see below.

## Verification

No public lookup — a donor and customer marketing data business, so nothing to
search yourself in. The written statement is the evidence.

**The opt-out route here is unusually broad, and their own wording is why it is
worth using in preference to the statutory form:**

> "Consumers, **regardless of their state of residence**, may opt-out of
> SimioCloud's database at any time and at no cost via our website... Exercising
> this opt-out right will prevent SimioCloud from selling your personal
> information, processing your personal information for targeted advertising or
> profiling, and will result in the **removal of your personal information from
> SimioCloud's database**."

That is sale, targeted advertising, profiling *and* database removal — offered to
everyone, not only residents of covered states.

> **When a broker offers both a statutory route and a voluntary one, read the
> voluntary one before assuming it is weaker.** Statutory forms are gated on
> residency and scoped to the statute; a company-wide opt-out can be broader and
> available to people the statute does not cover. For a Pennsylvania resident this
> one is strictly better.

Keep the autoreply — it is where that commitment is recorded.
