# AroundDeal

- **Opt-out:** https://www.arounddeal.com/remove-profile
- **Method:** web_form — Web form.
- **Domain:** arounddeal.com
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-09-02)
- Note: Emailed support@arounddeal.com 2026-09-02 (the address their own privacy policy names; no dedicated privacy mailbox published). Row previously had ONLY a form URL (/remove-profile) and no email, so this is new coverage rather than a re-send. THE THING THEY GOT RIGHT, quoted back to them: 'To avoid irrelevant contact data in the B2B database, we have set up an excluding contact list (Opt-out List) OUTSIDE THE B2B DATABASE.' A suppression that lives outside the record it protects is the only structure that survives its own success -- a flag ON a record is deleted along with the record, and the next ingest re-creates the person cleanly because nothing remains that recognises them as having asked. Almost nobody in this sector has built it. THE QUESTION THAT DECIDES WHETHER IT WORKS: does the Opt-out List fire AT INGEST (reject the incoming record) or AFTER (accept into the database, hide from results)? Identical from outside, not the same thing -- the second means they keep and refresh a record indefinitely and anything reading the database rather than the search results (export, partner feed, migration, bug) reaches it. Said 'it filters at query time, not at ingest' is a perfectly good answer. ALSO: asked that the opt-out entry NOT EXPIRE, since their policy sets a retention period for the list, and gave the reason -- an expiring opt-out is not a shorter protection, IT IS A DELAYED RE-ADDITION, with the person put back and never told; 1798.105(d)(1) expressly permits retaining the minimum to give effect. Plus the full 267 intake set (extension/CRM/mailbox store searched separately, name the store searched, do-not-contribute at ingest, asking WHETHER not WHO), the derived-address ask, sources per element, 1798.120 opt-out, and 1798.105(c)/Art 17(2) direction to customers with the honest fallback offered.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.arounddeal.com/remove-profile
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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

## If they ignore you

Work down this list. Each rung costs them more than the one above it.

1. **Reply in the existing thread** after the statutory deadline. California
   allows 45 days for a deletion request (Cal. Civ. Code 1798.130), extendable
   once by a further 45 with notice. Quote the date you first wrote.
2. **Write to the legal entity at the registered address above**, by post, if
   email has failed. A letter to the address of record is harder to lose than a
   support ticket, and it establishes a paper trail.
3. **Complain to the California Attorney General**, who administers the data
   broker registry: <https://oag.ca.gov/contact/consumer-complaint-against-business-or-company>.
   A broker's registration is what obliges it to answer; a complaint referencing
   the registry entry is the pressure point.
4. **Complain to the FTC**: <https://reportfraud.ftc.gov>. Useful for a pattern
   of non-response rather than a single case.
5. **Your own state Attorney General.** Many states with no comprehensive
   privacy statute still have consumer-protection powers and will take a
   complaint about a business that ignores its own published policy.

**What not to bother with:** phoning a support line to argue. The person who
answers cannot change the policy and did not write it. The registry entry, the
statutory deadline and the regulator are what actually move a company.
