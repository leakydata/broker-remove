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

