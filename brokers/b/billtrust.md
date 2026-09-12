# Billtrust

- **Email:** privacy@billtrust.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** billtrust.com
- **Priority: 2.**

## Status

- Current: `replied` (updated 2026-09-02)
- Note: PUSHED BACK 2026-09-02 on a closure that neither searched nor forwarded. Billtrust's reply made three separable claims and I answered them separately. (1) 'As a B2B service provider we do not engage directly with individual consumers' -- accepted as description, refused as reasoning: NOT ENGAGING DIRECTLY IS THE CONDITION THE STATUTES ARE WRITTEN FOR, since the broker definition turns on having no direct relationship, and the CCPA B2B exemption expired 1 Jan 2023 while GDPR never had one. (2) 'we do not control the personal information involved' -- ACCEPTED, and said so plainly: a processor cannot delete a controller's records on a stranger's say-so and a vendor that did would be doing something worse than refusing. But 1798.140(ag) and CPPA regs 7050-7051 require a service provider to ASSIST the business in responding -- the duty is not to decide the request, it is not to be the place it stops. (3) THE ONE THAT CANNOT BE RIGHT: 'contact the business associated with your transaction.' I DO NOT KNOW WHICH BUSINESS THAT IS AND THEY DO. No invoice names the vendor's accounts-receivable software, so the instruction resolves to 'guess, from a list only we can see, which company routes receivables through us'. A redirection to a party only the redirector can identify ends the request while appearing to continue it. Offered three closures, any of which I would accept: name the client instance, forward it without naming them, or state that a search across client instances returned nothing. NEW CATEGORY ASK from their own words -- the service runs 'from CREDIT APPLICATIONS to the processing of invoices and payments', and a trade credit application routinely names a natural person as owner, officer or PERSONAL GUARANTOR with home address and DOB. That is consumer data inside a B2B product, it is a different store from payment transactions, and 'ask your card issuer' cannot reach it because no card was involved. Also re-reported that privacy@billtrust.com REJECTS MAIL FROM OUTSIDE THEIR ORGANISATION -- a privacy address closed to the only population it exists for, invisible from inside because bounces reach only the sender.

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

## The published privacy address cannot receive external mail

`privacy@billtrust.com` rejects everything from outside the company:

> *"The group privacy only accepts messages from people in its organization or on
> its allowed senders list, and your email address isn't on the list."*
> `550 5.7.133 RESOLVER.RST.SenderNotAuthenticatedForGroup`

It is a Microsoft 365 distribution group set to authenticated senders only. Not a
dead address — a live one that structurally cannot be reached by a consumer, which
is worse, because it looks entirely normal until you try.

**Use `privacyrequests@billtrust.com`**, given in their privacy policy.

Worth flagging the misconfiguration when you write; a company publishing a privacy
contact that bounces every consumer almost certainly does not intend to.

## Other contacts in the policy

- **UK/EEA representative:** VeraSafe, contactable instead of or in addition to
  the address above, by web form or on +44 (20) 4532 2003.
- **DPO (Belgium):** a named individual at Billtrust Belgium BV, Ghent.

Not relevant to a US consumer request, but useful if a US route stalls — an EU
representative is obliged to engage and is usually more responsive.

