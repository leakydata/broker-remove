# Backgroundcheckers

- **Opt-out:** https://www.backgroundcheckers.net/api/helper/optOutLight/search
- **Email:** support@backgroundcheckers.net (verified)
- **Method:** web_form — Web form.
- **Domain:** backgroundcheckers.net
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

## A self-service route, and a second step that is automatable

Support answers email helpfully and points at a removal tool:

> *"If you are unable to remove your listing from
> https://www.backgroundcheckers.net/api/helper/optOutLight/search please call us
> between 8am and 11pm EST"*

The flow they describe is worth quoting in full, because the second step is the
one that gets missed:

> *"When you locate your listing, submit your email address to validate your
> ownership of the information. An acknowledgement email will be sent to you
> immediately. **Respond to the acknowledgement email to authorize removal of your
> listing. If you do not respond to the email, your listing will NOT be
> removed.**"*

Not a link to click — a **reply to send**. Anyone treating the acknowledgement as
a receipt has an unremoved listing and a mailbox that says otherwise. See
`_SILENT_FAILURES.md` §2; this is that trap in an unusual form.

Good news for automation: replying to an email is something a helper with mailbox
access can do unattended. Only the search itself needs a person.

## The CAPTCHA arrives on the second search

The **first** search runs clean. A text-image CAPTCHA — *"Please enter the
characters exactly as shown above"* — appears from the **second** onward. That
matters when you have address history: one city is free, the rest are gated.

Search by `first / last / city / state`, with optional ZIP, phone and email. No
account needed — they say so explicitly:

> *"You do not need to have an account with us to remove your listing."*

## Reading an empty result

> *"If you are unable to locate your listing then it means your information was
> never collected, or has already been removed."*

Useful, and unusually honest. But treat it per-city: a search of the current city
returning nothing says nothing about a former one, and this is a broker whose
index is address-keyed. Work the prior-address list before recording `not_found`.

They also warn that a stale result can be a cache:

> *"you may need to clear your browser cache or try your search a few days later"*

## Same operator as CheckSecrets

CheckSecrets replied to a separate request with a **word-for-word identical**
template on the same afternoon — same opening line, same paragraphs, same closing.
Two brands, one support desk. Expect the same tooling and the same two-step
acknowledgement flow, and treat a lesson learned on one as applying to both.

Phone: **(833) 714-0641**, 8am–11pm EST. Postal address published in Orlando, FL.

