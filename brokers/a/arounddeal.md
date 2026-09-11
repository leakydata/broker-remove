# AroundDeal

- **Opt-out:** https://www.arounddeal.com/remove-profile
- **Method:** web_form — Web form.
- **Domain:** arounddeal.com
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-09-02)
- Note: Emailed support@arounddeal.com 2026-09-02 (the address their own privacy policy names; no dedicated privacy mailbox published). Row previously had ONLY a form URL (/remove-profile) and no email, so this is new coverage rather than a re-send. THE THING THEY GOT RIGHT, quoted back to them: 'To avoid irrelevant contact data in the B2B database, we have set up an excluding contact list (Opt-out List) OUTSIDE THE B2B DATABASE.' A suppression that lives outside the record it protects is the only structure that survives its own success -- a flag ON a record is deleted along with the record, and the next ingest re-creates the person cleanly because nothing remains that recognises them as having asked. Almost nobody in this sector has built it. THE QUESTION THAT DECIDES WHETHER IT WORKS: does the Opt-out List fire AT INGEST (reject the incoming record) or AFTER (accept into the database, hide from results)? Identical from outside, not the same thing -- the second means they keep and refresh a record indefinitely and anything reading the database rather than the search results (export, partner feed, migration, bug) reaches it. Said 'it filters at query time, not at ingest' is a perfectly good answer. ALSO: asked that the opt-out entry NOT EXPIRE, since their policy sets a retention period for the list, and gave the reason -- an expiring opt-out is not a shorter protection, IT IS A DELAYED RE-ADDITION, with the person put back and never told; 1798.105(d)(1) expressly permits retaining the minimum to give effect. Plus the full 267 intake set (extension/CRM/mailbox store searched separately, name the store searched, do-not-contribute at ingest, asking WHETHER not WHO), the derived-address ask, sources per element, 1798.120 opt-out, and 1798.105(c)/Art 17(2) direction to customers with the honest fallback offered.

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
