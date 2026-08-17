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
them *appends*, producing "[PERSONAL][PERSONAL]" / "[PERSONAL][PERSONAL]". Clear each field before
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

## The route map, from their own customer-care reply

`customercare@peoplefinders.com` does **not** accept privacy requests — but it
auto-replies with the correct routes, which makes it useful anyway:

> *"This email address is dedicated to customer service inquiries and is not
> intended for privacy-related requests. We do not accept privacy requests
> submitted via email."*

| Right | URL | Notes |
|---|---|---|
| Opt-out | `/opt-out` | **Cloudflare page-load gate** — automation cannot reach it |
| Delete | `/dashboard/account/delete` | Only covers a PeopleFinders **account**, not the public record |
| Right to Know | `/request-my-info` | **Loads normally — no page-load gate** |

Phone: **(800) 718-8997**, Mon–Fri 7:00–18:00 PST, Sat–Sun 8:00–15:30 PST. A
phone route bypasses the CAPTCHA entirely and is the realistic option for anyone
who cannot complete the web flow.

**The Delete link is a trap.** It deletes the account you created, not the
profile assembled about you. Someone who has never registered has nothing there
to delete, and clicking it feels like progress while changing nothing.

### `/request-my-info` is the automatable route — up to the last click

Unlike `/opt-out`, this page loads without a Cloudflare challenge. The flow is
`Request My Info > Verify Identity > Confirmation`, and it opens with:

> *"There's no need to create an account in order to request your personal
> information."*

Worth quoting, because account creation is exactly what the Delete route implies.

Everything up to the CAPTCHA can be staged: choose **"I am requesting my own
information"**, which leaves only a reCAPTCHA checkbox and **Continue** for a
human. That is a genuine one-click hand-off rather than an abandoned flow.

## The opt-out email link expires in 24 hours

The `/opt-out` flow emails a completion link and states:

> *"If you waited longer than 24 hours to click the link below, you will need to
> start over and generate another link."*

Miss it and you get **"Opt-out Voucher Expired"** — *"This link has already been
used or has expired. Please restart the process."* Restarting means the
Cloudflare-gated page and a fresh CAPTCHA. The plain-text copy of that email also
arrives with the trailing `ticketid` parameter mangled, so copy the link from the
HTML version. See `_SILENT_FAILURES.md` §2.

