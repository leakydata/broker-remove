# Buxton Company, LLC

- **Email:** consumerprivacy@buxtonco.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** buxtonco.com
- **Priority: 2.**

## Status

- Current: `captcha_blocked` (updated 2026-10-10)
- Note: THE DEFLECTION TEMPLATE CONTAINED THE ROUTE THE PRIVACY POLICY DOES NOT. Their auto-reply of 2026-10-10 refuses email outright -- 'Audiense does not accept privacy requests submitted by email, so this request will not be processed' -- but it then supplies TWO WORKING URLS that nothing on the policy page reaches: the Consumer Personal Information Request Web Form at audiense.com/legal/consumer-personal-information-requests/ and an OPT OUT form at audiense.com/legal/privacy-opt-out/. It also confirms the corporate position in terms: 'We're now Audiense, the new name for our combined entities -- Audiense, Elevar, and Buxton.' SO THE AUTORESPONDER IS MORE USEFUL THAN THE POLICY. 488 recorded that the policy's own 'Your Privacy Choices' link is circular; the template that rejects your email hands you the working address. Worth generalising: when a company refuses email and redirects, READ THE REDIRECT -- it may contain the route the published policy lost in a migration. THE OPT-OUT FORM IS REAL AND NEARLY DRIVABLE. Fields: first name, alternative first name, middle initial, last name, suffix, email, phone, address, address 2, city, state (PA present), zip, and MOBILE ADVERTISING ID -- which is NOT a required field, so it can be left as N/A, which is what the form's own instruction says to do for inapplicable fields. Company is a MULTI-SELECT offering Buxton and Elevar; Audiense itself is not listed. There is a penalty-of-perjury declaration. PRESS-SUBMIT TESTED (457a): filled completely with Buxton selected and MAID as N/A, clicked Submit Request, page did not change, no validation message, no console errors. A reCAPTCHA is present on the page. Not attempting further -- 484's rule. HANDED OFF with the exact values; it is a one-minute job for a person, and the only non-obvious step is CTRL+CLICK to select Buxton AND Elevar rather than one.

## Steps

1. Do not expect a reply at consumerprivacy@buxtonco.com for a direct consumer
   request — buxtonco.com's privacy policy now redirects (301) to
   `audiense.com/legal/privacy`, and reading it shows `consumerprivacy@buxtonco.com`
   is documented as being for **authorized-agent requests specifically**, not
   direct consumer ones. That is consistent with the auto-reply saying "we do
   not accept privacy requests submitted by email."
2. Use the web form at `https://www.audiense.com/legal/privacy` instead — queued
   in `handoff.py` for a human to complete (browser required).
3. Phone fallback published on the same page: 1-888-228-9866.

## Gotchas

**Buxton now operates under the Audiense brand.** Audiense, LLC (with
subsidiaries Elevar, LLC and Audiense, LTD) is the current legal entity;
`buxtonco.com`'s own privacy policy repeatedly references "Buxton" internally
while redirecting to audiense.com for the actual policy text and request form.
Nothing on buxtonco.com's homepage announces this — you only find it by
following the privacy-policy link.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Buxton Company, LLC
- **Registered address:** 2651 S Polaris Drive, Fort Worth, TX, 76137
- **Filed contact email:** consumerprivacy@buxtonco.com
- **Filed phone:** 8173323681
- **Website:** www.buxtonco.com

*Source: `data/registries/registry.csv`.*

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
