# NextRoll (AdRoll, RollWorks)

- **Email:** dpo@nextroll.com — delivers; auto-reply does **not** foreclose it
- **Method:** email, plus two self-service routes on `app.adroll.com`
- **Domain:** nextroll.com
- **Priority: 3.**

## Status

- Current: `captcha_blocked` (updated 2026-08-19)
- Note: Auto-reply routes to a Relyance portal (nextroll-privacy.relyance.ai) but does NOT foreclose the email: 'Otherwise, we will get back to you as soon as we can!' So the letter stands. The portal's own note - 'An Advertiser Identifier is required for customer requests' - is aimed at AdRoll advertisers, not consumers; consumers are pushed to two app.adroll.com routes instead. The valuable one is /optout/email, which is not an ad-cookie opt-out at all: it covers Contact Discovery, their B2B product that sells business email addresses and phone numbers to buyers for cold outreach. Filled with the .edu address and current mobile; reCAPTCHA gates submission, staged for one human click. The form takes ONE identifier per run, so each address needs its own pass.

## Steps

1. Write to `dpo@nextroll.com`. The auto-reply points at
   `nextroll-privacy.relyance.ai` **but ends** *"Otherwise, we will get back to
   you as soon as we can!"* — so the email is still live. Do not treat the portal
   as a redirect that closes the letter.
2. The Relyance portal's front page carries a note that reads like a blocker and
   is not one: *"An Advertiser Identifier is required for customer requests."*
   The instructions underneath make clear it means **AdRoll advertisers** — log
   in, take the last 22 digits of your dashboard URL. A consumer is not a
   customer in that sense and needs no such identifier.
3. The two consumer routes are on `app.adroll.com`:
   - `/optout` — cookie-based ad opt-out
   - `/optout/email` — **the one that matters** (below)

## Gotchas

**`/optout/email` is not an ad opt-out, despite living among them.** It covers
**Contact Discovery**, RollWorks' B2B product, described on the page as allowing
*"our customers to purchase business email addresses and/or business phone numbers
in order to contact businesses."* That is list resale for cold outreach, sitting
inside an adtech company's privacy page, reachable only by scrolling past the
cookie opt-out. It is a materially different product from retargeting and it has
its own separate opt-out, which is easy to miss precisely because of where it is.

**It takes one identifier per run.** One email address and one phone number per
submission, each behind its own reCAPTCHA. A person with several old addresses —
which is exactly who a B2B contact database holds — needs a separate pass for
each. Prioritise institutional and employer-issued addresses; those are what this
product traffics in.

**No visible Submit until the CAPTCHA is answered.** Same shape as the DTN form:
the control is absent rather than disabled, so the page looks like it has no way
to submit at all. Do not report it broken.

**The cookie opt-out under "Targeted Advertising" is one click and nearly
worthless on its own** — it is a browser-local preference, lost on clearing
cookies or changing device. Worth taking while you are there; not worth recording
as a removal.

## Verification

No public listing. Chase the DPO on the emailed request; the portal and the
self-service forms produce no artifact beyond an on-page confirmation.


## The phone field: area code in the dropdown, last seven digits in the box

Reported by the subject after the first staging attempt was filled wrongly, and
worth recording because the failure is silent until submission.

`/optout/email` presents what looks like one telephone field. It is two:

- a **"Code ..." combobox** to its left, which must have the **three-digit area
  code selected from its list** — click it, type the digits into its search box,
  then click the matching row (it shows as `(814) - Pennsylvania`);
- a **text field** which takes the **last seven digits only**.

Typing all ten digits into the text box leaves the code unset and the number
invalid. Correctly filled, the control reads `Code: (814)` and `4413265`.

> **A split phone control looks like one field and validates as two.** The
> giveaway is a narrow unlabelled button sitting flush against the left edge of
> the input. Check whether it holds a value before assuming the number is
> complete — nothing on the page says the field is incomplete until submit.
