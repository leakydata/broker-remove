# Dealfront

- **Opt-out:** https://privacycockpit.leadfeeder.com/
- **Method:** web_form — Web form.
- **Domain:** privacycockpit.leadfeeder.com
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-09-02)
- Note: Emailed dpo@leadfeeder.com 2026-09-02 -- a real DPO address found on dealfront.com/gdpr/. Row previously had ONLY a portal URL (privacycockpit.leadfeeder.com) and no email, so new coverage. Dealfront = Leadfeeder + Echobot, established Germany and Finland, so Art 3(1) attaches regardless of my US residence (pre-answered in the letter). THREE THINGS THEY PUBLISH THAT DO MY WORK FOR ME. (1) 'each record can be traced back to one or more specific sources, OFTEN WITH ACTUAL DEEP LINKS to where the data was collected' -- stronger than B2BHint's citation claim and it satisfies Art 15(1)(g) by their own architecture, since the article requires the source be PROVIDED not that a category be described. Asked for the deep links. (2) A UNIFIED BLOCKLIST marketed as a feature, with the correct diagnosis attached: data subjects 'will be annoyed by having to opt out with many parties'. Asked to be added, asked whether it fires AT INGEST or after, and asked that the entry not expire since an expiring opt-out is a DELAYED RE-ADDITION. (3) THE CRM CONNECTOR, and this is the sharpest question: they say CRM-connected data is processed AS A PROCESSOR on the customer's behalf under a DPA. Accepted that framing for data handled on the customer's behalf and then asked what happens next -- DOES ANYTHING INGESTED FROM A CUSTOMER'S CRM, MAILBOX OR EXTENSION EVER FLOW INTO DEALFRONT'S OWN DATASET to enrich or verify a record other customers can see, or is it strictly siloed? Siloed means the processor framing covers it and I should write to that customer. If it enriches, they are a CONTROLLER as to that use, the DPA does not reach it, and it is inside the request. Plus the do-not-contribute-at-ingest ask, WHETHER not WHO. ALSO: Art 21 objection with a request for the OUTCOME OF THE BALANCING AS APPLIED TO ME, since they publish the test's steps; deletion reaching buying-intent signals and scores as generated data; 1798.120; and the MCP-server question (third company this week serving data to AI agents), with 'deletion ends at our boundary' offered as an acceptable answer.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://privacycockpit.leadfeeder.com/
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
