# Buildertrend

- **Opt-out:** https://buildertrend.com/privacy-policy/
- **Email:** privacy@buildertrend.com (verified)
- **Method:** web_form — Web form.
- **Domain:** buildertrend.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-17)
- Reference: `form entry ID on file`
- Note: Web form completed and submitted end to end with no human step; confirmation page returned an entry ID. Their emailed redirect said to use 'the form linked in Section X of our Privacy Notice' — Section X is real (Roman numeral ten, 'Contact Us'), and the form is embedded on that page. Cloudflare Turnstile self-cleared without interaction.

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

## Email is redirected, but the form is genuinely automatable

`privacy@buildertrend.com` answers within a minute:

> *"It looks like your request wasn't submitted through the designated method
> outlined in Section X of our Privacy Notice. To make sure we can process your
> request properly, please resubmit using the form linked in Section X."*

**"Section X" reads like an unfilled template placeholder. It isn't.** It is
Roman numeral **ten** — the *Contact Us* section of the Privacy Notice, which is
numbered I through X. The form is embedded directly on that page:

> *"To exercise your legal rights regarding your personal information... please
> call our toll-free number at 1-888-415-7139 or fill out this form"*

Their *Additional U.S. State Privacy Disclosures* page uses the same phrasing,
which makes the placeholder reading tempting. Check the section numbering before
concluding a broker's instructions are broken.

## Route

<https://buildertrend.com/privacy-notice/> → scroll to **X. Contact Us**.

Fields: First name, Last name, Email, Country, State (the state dropdown swaps
depending on country — there are five of them in the DOM, so select Country first,
then re-locate the visible one), **"I am a (an)"**, and a free-text **Request
details** box.

The "I am a (an)" options are worth reading:

- Buildertrend customer
- CBUSA customer
- CoConstruct customer
- SquareTakeoff customer
- Buildertrend guest / invited user (subcontractor, homeowner, employee)
- Marketing recipient
- Other

**The brand list is the useful part** — one form covers CoConstruct, CBUSA and
SquareTakeoff as well. If you have never dealt with them directly, *Other* is the
honest choice; do not claim a customer relationship you cannot evidence.

**No human step is required.** The Cloudflare Turnstile self-clears, and the
confirmation page returns an entry ID:

> *"Thank you! We will review and, if a data privacy right is applicable, contact
> you through email."*

Phone alternative: **1-888-415-7139**.

