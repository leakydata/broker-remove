# PeopleFinders

- **Email: refused.** "We do not accept privacy requests received via email."
  Reply still useful — it enumerates the working routes.
- **Verified contact:** customercare@peoplefinders.com  ·  (800) 718-8997
  (`privacy@peoplefinders.com` **hard-bounces with 550** — do not use)
- **Affiliate:** PeoplefindersDaaS (separate CA registration 191581)
- **Priority: 5.**

## Three routes, only some usable

| Right | URL | Gated? |
|---|---|---|
| Opt-out | `/opt-out` | **Cloudflare challenge on page load** — automation can't reach it |
| Right to Know | `/request-my-info` | **Open.** Not gated. reCAPTCHA only at auth step |
| Right to Delete | `/dashboard/account/delete` | Account holders only — irrelevant if you never signed up |

**Use `/request-my-info`.** Same asymmetry as TruePeopleSearch: the opt-out door is
bot-gated while a different privacy door is open.

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
