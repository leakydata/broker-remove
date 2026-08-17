# Brandwatch

- **Email:** privacy@brandwatch.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** brandwatch.com
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

## The auto-reply is a gate — you must reply to it

`privacy@brandwatch.com` answers within minutes from `PrivacyAutoreplyBW@`. It
opens with *"We confirm receipt of your message"* and then, further down:

> *"If you believe we have collected data on you as a Content Author, please reply
> to this email indicating your desire for us to proceed with your request."*

**Nothing is processed until you send that reply.** The receipt looks like the
artifact you were waiting for. See `_SILENT_FAILURES.md` §5.

## Two categories, two different answers

The same reply splits requests in a way that matters:

**Users (customers/prospects)**

> *"Our products are not meant for use by private individuals and therefore we
> only accept and index upon business email addresses. If your email address is a
> personal email address, we can confirm that we would not have collected any data
> related to you as part of our services, sales, or marketing efforts."*

So for a private individual with personal addresses, this category is genuinely
empty. Worth accepting rather than arguing.

**Online content authors** — the category that actually applies:

> *"The Brandwatch product collects only publicly available online content and
> stores it based on the social handle/username associated with the content. We
> only index on your social handles. We do not have any content indexed by your
> proper name, email address, or phone number."*

**This is why a standard opt-out letter achieves nothing here.** Name, email and
phone — the entire contents of the usual request — are not searchable fields.
Without social handles there is nothing for them to match on, and a truthful "no
records" reply is the likely outcome.

## What to send

1. Reply confirming you want the request processed (the gate above).
2. **Ask which platforms they hold author content from before volunteering
   handles.** Sending a speculative list adds identifiers to a broker's systems
   that may not correspond to anything they hold — the opposite of the goal.
3. Ask for the archived content, the author profile, and derived attributes
   (sentiment, demographic, interest, influence, segment membership) — not just
   the posts.
4. Ask for written confirmation if nothing matches. There is no public listing to
   re-check, so their letter is the only available evidence.

## On "it was already public"

Their note that the data *"is available publicly for anyone to find via any search
engine"* is accurate about the source posts and irrelevant to the request. The
archive, the author-level aggregation, and the inferences drawn from it are their
processing of personal information about an identifiable person. Framing it that
way — agreeing about the posts, distinguishing the derived record — keeps the
exchange cooperative, which matters with a team that is clearly willing to engage.

