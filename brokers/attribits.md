# Attribits

- **Opt-out:** https://www.attribits.com/do-not-sell
- **Email:** compliance@allgoodmediagroup.com (verified)
- **Method:** web_form — Web form.
- **Domain:** allgoodmediagroup.com
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

## The mailto: that points at a domain which does not exist (updated 2026-08-19)

Their announcement bar publishes a contact address. The rendered text is correct.
The link is not:

    <a href="mailto:info@attritbits.com"><em>info@attribits.com</em></a>

    attribits.com    NS: dns1.registrar-servers.com   MX: aspmx3.googlemail.com
    attritbits.com   NS: (none)                       MX: (none)

Two letters transposed in the `href`, onto a domain with no zone at all. Read the
address and type it and the mail arrives; click it and it hard-bounces.

A neighbouring field in the same CMS record (`clickthroughUrl`) holds the correct
`mailto:info@attribits.com`, so this is a data-entry slip, not obfuscation.

> **Harvest contact addresses from the `href`, not from the rendered text — then
> check that the domain resolves.** Here the two disagree, and only a `dig NS` on
> each says which side is wrong.

See [[_SILENT_FAILURES]] §61.

## Routes

- `compliance@allgoodmediagroup.com` — the contact already on file, apparently a
  parent or agency address rather than the brand's own.
- `info@attribits.com` — **the working address**, typed rather than clicked. Worth
  using as a second route, and worth telling them the link is broken while doing
  so.

Their privacy page carries no dedicated privacy mailbox, so `info@` is the whole of
the brand-level route.
