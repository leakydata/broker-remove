# South Dakota Arrests

- **Method:** web_form — Web form.
- **Domain:** southdakotaarrests.org
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-09-08)
- Note: CORRECTED 2026-09-08, SAME DAY, BEFORE ANY TIME WAS SPENT ON IT. This row was briefly set to 'pending' with a /ccpaOptOut/ route on the strength of an HTTP 200. That was wrong. A negative control -- requesting /zzz-not-a-real-page-9137/ on the same host -- also returns 200, with byte-identical content. Nine of these domains serve a 114-byte parking stub for every path; four serve a ~32KB generic landing page for every path. THERE IS NO ROUTE AND NO SECOND FAMILY. The contrast is decisive: every real InfoTracer sibling (california, nevada, pennsylvania, texas, ohio, alabama, georgia, wyoming) returns 404 on the same nonsense path while returning 200 on its genuine /ccpaOptOut/ or /contact-form. So the network is 33 operating InfoTracer front-ends plus these parked domains, not two operations. Recorded unreachable: the domain resolves and answers, and there is nothing behind it a consumer can use. See _SILENT_FAILURES 427.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **No route is confirmed for this broker yet.** Check the registry block above for a filed contact, and see `## Gotchas`.
2. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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
