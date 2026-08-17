# Cision

- **Email:** privacy@cision.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** cision.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-17)
- Note: Auto-reply gate (same template as sister company Brandwatch): nothing proceeds without an explicit confirmation reply. Sent to the monitored privacy@ address. KEY DIFFERENCE from Brandwatch: Cision indexes journalist/influencer records by NAME, EMAIL and social handle, not handles alone, so the standard letter is directly actionable here.

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

## Same auto-reply gate as Brandwatch — and the same trap

Cision owns Brandwatch, and both use an identical auto-responder template. It
opens *"We confirm receipt of your message"* and then, further down:

> *"If you believe we have collected data on you as a Journalist or Influencer,
> please reply to this email indicating your desire for us to proceed with your
> request."*

**Nothing is processed until you send that reply.** See `_SILENT_FAILURES.md` §5.
Send the confirmation to `privacy@cision.com`, not to the `PrivacyAutoreply`
address it arrives from — replying to the auto-responder just triggers it again.

## Crucial difference from Brandwatch: they index on name and email

This is the sentence that matters, and it is the opposite of its sister company's:

> *"We index your information by your name, email address, and social handle."*

Brandwatch indexes **social handles only** and says so explicitly, which makes a
standard opt-out letter unanswerable there. Cision indexes **name and email as
well**, so the ordinary request — name, addresses, every email address — is
directly actionable. No handles required.

Do not assume sister companies share a data model. The two auto-replies are
word-for-word identical in structure and differ on exactly the point that decides
whether your letter can be answered.

## The two categories

**Users (customers/prospects)** — *"we only process and index upon business email
addresses. If your email address is a personal email address, we can confirm that
we would not have collected any data related to you."* Genuinely empty for a
private individual; accept it.

**Journalists and Influencers** — the category that applies to anyone whose byline,
public profile or published content has been scraped. *"The Cision product collects
only publicly available contact details and articles and content you have
published."*

Answer both explicitly, or a truthful "no records" may address only the category
you did not mean.

## What to ask for

Beyond the contact record: **beat and topic classifications, outlet affiliations,
and influence/reach/engagement scores.** These are Cision's own inferences, they
are what subscribers pay for, and they outlive a deleted contact row.

Also ask for platform-level **do-not-contact suppression** — subscribers run
outreach campaigns through the platform, so suppression stops the email even where
a record legitimately remains.

## On "it was already public"

> *"The data that we collect is available publicly for anyone to find via any
> search engine."*

True of the source articles, irrelevant to the request. Concede the point about
the originals — they are not Cision's to remove — and distinguish the compiled
profile, the contact details as held, and the derived scores, which are.

