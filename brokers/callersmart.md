# Callersmart

- **Opt-out:** https://www.callersmart.com/data
- **Email:** feedback@callersmart.com (verified)
- **Method:** web_form — Web form.
- **Domain:** callersmart.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-17)
- Note: Statutory delete/opt-out request emailed, tailored to the broker's data category; awaiting reply.

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

