# Callersmart

- **Opt-out:** https://www.callersmart.com/data
- **Email:** feedback@callersmart.com (verified)
- **Method:** web_form — Web form.
- **Domain:** callersmart.com
- **Priority: 2.**

## Status

- Current: `replied` (updated 2026-08-17)
- Note: THE AUTORESPONDER ANSWERED THE QUESTIONS I EMAILED TO ASK. [named individual]@callersmart.com replies 'This is an unmonitored inbox' -- so the address is DEMOTED to declared_unmonitored_by_company (SF 205 shape) -- but the template itself contains the substance: (a) 'CallerSmart users search listings BY PHONE NUMBER ONLY (not by name, email, or physical address)' -- which answers question 2, what the suppression is keyed to, and means a name-based removal does nothing; (b) 'If you see a listing that you would like to remove, please use the phone number associated with it' -- the listing IS the number, which answers question 1 about the URL as well as it can be answered; (c) opt-outs submitted through the /data form are 'processed immediately'. THE COST IS THE STRUCTURE, NOT THE POLICY. Because the index is keyed to the number and the form takes ONE number plus one email confirmation per submission, a person with ten former numbers must file ELEVEN SEPARATE REQUESTS with eleven confirmation links. The burden scales with how many times someone has moved -- which is precisely the population most likely to be listed. That is a 7004 minimal-steps problem created by the index design rather than by any unwillingness to remove. STAGED TO HANDOFF, split so the human part is small: the /data page is Cloudflare-gated (403 to any non-browser) so the eleven submissions must be made by hand, but every confirmation link lands in [EMAIL] and I can click those.

## Steps

1. Do not email — the inbox is unmonitored. Its auto-reply is still worth
   triggering once, because it names the route.
2. Use the opt-out form, and use it **once per phone number**. Listings here are
   keyed to phone numbers, not to a person.
3. Solve the CAPTCHA per submission, or batch them; each number is a separate
   submission with its own CAPTCHA.
4. Avoid the "self-opt-out" route entirely — see below.
5. Collect the per-number confirmations. They arrive individually.

Detail for each of these is in the sections below; this is the order, not the
whole story.

## Gotchas

Three things, each expanded further down:

- **The published inbox is unmonitored**, but its auto-reply is not useless — it
  is where the real route is documented (*Unmonitored inbox, but the auto-reply is
  useful*).
- **Listings are keyed to phone numbers only**, so a name-based request matches
  nothing and one submission clears one number (*Listings are keyed to phone
  numbers only*, *The cost: one submission per number*).
- **The "self-opt-out" route is the wrong one** and should not be used (*Do not
  use the "self-opt-out" route*).

## Verification

See *Verifying afterwards* below — the outcome here was confirmed number by
number, and that is the granularity the check has to work at too.

## Unmonitored inbox, but the auto-reply is useful

`feedback@callersmart.com` answers with `[UNMONITORED INBOX REPLY]` in the subject:

> *"This is an unmonitored inbox... If you would like to automatically remove a
> phone book listing from our website, please visit our Do Not Sell My Personal
> Data page."*

## Listings are keyed to phone numbers only

> *"CallerSmart users search listings **by phone number only** (not by name, email,
> or physical address). If you see a listing that you'd like to remove, please use
> the phone number associated with it to submit your request."*

**This makes a standard opt-out letter useless here.** Name, address and email —
the whole content of the usual request — are not searchable fields.

## The cost: one submission per number

`/data` takes **one phone number and one email**, then emails a confirmation link.
So the work is `N` numbers × (fill + reCAPTCHA + confirmation click). Anyone with a
long list of old numbers should budget for that, and should include disconnected
ones — those are the most likely to still carry a listing and the least likely to
be noticed.

The emailed confirmation click can be handled by anyone with mailbox access; only
the reCAPTCHA needs a person.

> *"Opt-out requests submitted through the Do Not Sell My Personal Data page are
> processed immediately."*

## Do not use the "self-opt-out" route

The page offers a "self-opt-out option" that looks like a shortcut. It is not:

> *"Step 1: Create a CallerSmart Account"*

It requires registering an account and verifying the number by SMS or automated
call. Creating an account with a data broker to leave it means handing over more
data and a durable identifier. Use the `/data` form instead — it needs no account
and the auto-reply itself presents it as the primary route.

## Working the list efficiently

Confirmed working, repeatedly. The rhythm per number:

1. `/data` → email + one 10-digit number → **reCAPTCHA** (needs a person) → SEND
2. Verification mail arrives in under a minute; open the link → *"Verification
   Completed! Thank you for verifying! Requested number was opted out."*
3. A separate confirmation mail follows, naming the number:
   > *"The phone book listing on (XXX) XXX-XXXX has been automatically removed
   > from our website. No personally identifying information will display with
   > this phone number in our phone book."*

Only step 1 needs a human. Steps 2 and 3 are doable by anyone with mailbox access,
so a helper can queue the next number while the confirmations land.

**Two practical gotchas:**

- **The page finishes rendering late.** Clicking a field immediately after
  navigation lands before the form is interactive and the keystrokes go nowhere —
  or worse, both values land in whichever box has focus. Wait, click, then verify
  the caret before typing. Once focused, **Tab** from email to phone is reliable.
- **The plain-text copy of the verification mail is inconsistently corrupted.** One
  message dropped the `=` and the first two characters of the signature, producing
  *"Security error, signature doesn't match"*; the next two were intact. Take the
  href from the HTML part every time rather than guessing which kind you got.

The number is reformatted to `(XXX) XXX-XXXX` on entry, which is a useful signal
that the field actually received the digits.

## Outcome: complete removal, confirmed number by number

All nine telephone numbers were individually confirmed, each by its own email
naming the number:

> *"The phone book listing on (XXX) XXX-XXXX has been automatically removed from
> our website. No personally identifying information will display with this phone
> number in our phone book."*

This is one of the cleanest outcomes in the project, and worth noting why: the
broker indexes on a **single, enumerable identifier**. There is no ambiguity about
whether the right record was found, no "we could not locate you", and no need to
re-verify by searching — the confirmation names exactly what was removed.

**Budget nine CAPTCHAs for nine numbers.** There is no bulk route. Repeated
submissions from one IP also escalate the challenge: after several in a row the
plain "I'm not a robot" checkbox is replaced by an image-selection challenge and
a Cloudflare interstitial appears. Spacing the submissions out avoids that.

## Verifying afterwards

Listings are searchable by phone number at the site's own search box, so a spot
check is easy and cheap — unlike the many brokers with nothing to search. Worth
re-checking a couple of numbers after a few weeks, since nothing here was
described as suppression against future re-ingestion, only removal of the current
listing.

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
