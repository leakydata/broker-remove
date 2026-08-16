# PeopleFinders

- **Email: refused.** "We do not accept privacy requests received via email."
  Reply still useful — it enumerates the working routes.
- **Verified contact:** customercare@peoplefinders.com  ·  (800) 718-8997
  (`privacy@peoplefinders.com` **hard-bounces with 550** — do not use)
- **Affiliate:** PeoplefindersDaaS (separate CA registration 191581)
- **Priority: 5.**

## STATUS: no working self-service route

As of the last attempt, **every route fails**:

| Route | Result |
|---|---|
| `/opt-out` | Cloudflare challenge on page load — never reaches the form |
| `/request-my-info` | Loads, but submitting returns *"An unexpected error occurred"* — twice, with CAPTCHA solved. Server-side fault |
| Email | Explicitly refused: *"We do not accept privacy requests received via email"* |
| `/dashboard/account/delete` | Account holders only — doesn't reach a public listing |

The combination — a bot-gated opt-out, a broken rights form, and a refusal to take
email — leaves a consumer with no functioning way to exercise their rights. Worth
stating plainly in the ticket, since it is unlikely to be intentional and is the
kind of thing that gets fixed once someone internally notices.

**Escalation:** reply on ticket **2585053** documenting both failures and asking
them to process from the ticket, or to confirm the telephone route
**(800) 718-8997** as the working path.

## Three routes, only some usable

| Right | URL | Gated? |
|---|---|---|
| Opt-out | `/opt-out` | **Cloudflare challenge on page load** — automation can't reach it |
| Right to Know | `/request-my-info` | **Open.** Not gated. reCAPTCHA only at auth step |
| Right to Delete | `/dashboard/account/delete` | Account holders only — irrelevant if you never signed up |

**Use `/request-my-info`.** Same asymmetry as TruePeopleSearch: the opt-out door is
bot-gated while a different privacy door is open.

## The opt-out is a FOUR-stage flow

1. `/opt-out` → **Next** → name + email + authorization checkbox + reCAPTCHA →
   **Send Request**
2. A link arrives by email: `/opt-out/removal-identification/<uuid>/<email>`.
   **It expires in 24 hours** — after that you start over.
3. That link opens the **Record Suppression Form**: first/middle/last, email,
   phone, full DOB, street, city, state, certification checkbox, reCAPTCHA.
4. Submit → confirmation page + confirmation email. Removal within 3 days.

**Trap: the link URL pre-fills the name fields** via `?fn=…&ln=…`. Typing into
them *appends*, producing "NathanNathan" / "JonesJones". Clear each field before
typing, and screenshot to verify — their own page warns that inaccurate
information hinders the match, so this silently costs you the removal.

Fill the **middle name and full date of birth** here even though they are optional.
The page states plainly that incomplete information means they may not locate all
records, and that unmatched records can reappear later from new data.

Their flow also spawns a **BrandYourself** referral tab mid-process — an upsell,
same pattern as Radaris→OneRep. Close it.

## Opt-out flow (per their Customer Care)
`/opt-out` → enter name + email → submit → **click the link emailed to you** →
read instructions and fill the form → submit → confirmation email.
Two-stage with an email hop in the middle, so budget for the round trip.

## Right to Know flow
`/request-my-info` → *Request My Information* → `/request-my-info/auth-selection`
→ select **"I am requesting my own information"** → reCAPTCHA → Continue →
Verify Identity → Confirmation. **No account required** (they say so explicitly).
Requests may take up to 45 days; repeatable every 6 months.

## Gotchas
- Cookie banner offers **only "Accept"** with no decline control. Leave it
  untouched rather than consenting.
- They state deletion applies to *account* information; public-record listings are
  handled through opt-out instead. Pushing only the Right to Delete link will miss
  the listing entirely.
