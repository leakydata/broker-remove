# Billtrust

- **Email:** privacy@billtrust.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** billtrust.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-09-07)
- Note (2026-09-02): first reply was the flat processor deflection — "we do not engage directly with individual consumers... contact the business associated with your transaction" — unworkable since the requester cannot know which of hundreds of businesses might route receivables through Billtrust. Pushed back: conceded the B2B/no-direct-relationship point does not exempt them (CCPA's B2B carve-out expired 1 Jan 2023), conceded they cannot search a client's own instance, but asked them to name the client, forward the request, or confirm a platform-side search found nothing.
- Note (2026-09-03): Billtrust's rep (Humberto Vargas) responded well — explained the platform architecture (no standing cross-client query access), agreed to check Billtrust's own directly-held records, and asked the fair question: **what made you think Billtrust holds anything about you specifically?** Answered honestly: nothing did — this was a category-based letter prompted by Billtrust's CA data broker registration, not evidence of a real transaction. **Worth generalizing: when a company asks this, say so plainly if it's true.** Overclaiming a specific basis to sound more credible would have been a worse answer and harder to walk back.
- Note: Published privacy@ address is an internal-only Microsoft 365 distribution group; rejected with 550 5.7.133 SenderNotAuthenticatedForGroup. Resent to privacyrequests@billtrust.com from their privacy policy (2026-08-17), quoting the rejection so they can fix the published address — delivered without bouncing. A follow-up run (2026-08-22) resent again to the same address without checking Sent history first; also delivered fine, but was a redundant duplicate. **privacyrequests@billtrust.com is the working address — check Sent history before resending.**

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

