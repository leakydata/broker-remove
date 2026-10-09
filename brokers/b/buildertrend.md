# Buildertrend

- **Opt-out:** https://buildertrend.com/privacy-policy/
- **Email:** privacy@buildertrend.com (verified)
- **Method:** web_form — Web form.
- **Domain:** buildertrend.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-10-09)
- Reference: `entry_id=1938911 form_id=25`
- Note: SUBMITTED 2026-10-09 through the designated method, confirmation page 'Thank you! We will review and, if a data privacy right is applicable, contact you through email.' entry_id=1938911, form_id=25. TWO FINDINGS, AND THE SECOND IS THE SERIOUS ONE. (1) THEIR MACRO WAS ACCURATE AND I SHOULD SAY SO. Buildertrend refused two emailed requests saying they were not sent through 'the designated method outlined in Section X of our Privacy Notice', and the staged handoff was written expecting Section X not to exist. It does: 'X. Contact Us' is the final numbered section and it carries both a toll-free number and the request form. The suspicion was unfounded and the route is real. (2) THE DESIGNATED METHOD CANNOT ACCEPT A DATA-SUBJECT REQUEST. The first submission, carrying twelve email addresses, eleven phone numbers and sixteen prior addresses in the Request Details box, was rejected outright with '*** Forbidden. Contains contacts. Anti-Spam by CleanTalk. ***'. The identical form submitted successfully the moment those identifiers were removed, which isolates the cause exactly. So CleanTalk is configured to treat any message containing an address or telephone number as spam -- and identifiers are precisely what a deletion request must carry to be actionable. The only channel they accept structurally cannot receive a complete request. A consumer hitting this sees a generic spam refusal, not an explanation, and would reasonably conclude the site is broken rather than that their request was silently blocked. WHAT WAS ACTUALLY SENT: the four asks, the non-customer framing (selected 'Other'; the dropdown otherwise assumes you are a customer), the PA-has-no-statute disclosure with a request to honour it under their published notice and name the basis, and an explicit request that they EMAIL ME TO COLLECT THE IDENTIFIERS, with the CleanTalk rejection quoted to them as a defect report rather than a complaint.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://buildertrend.com/privacy-policy/
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `privacy@buildertrend.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Buildertrend Solutions, Inc.
- **Registered address:** 11818 I Street, Omaha, NE
- **Filed contact email:** privacy@buildertrend.com
- **Website:** https://www.buildertrend.com

*Source: `data/registries/registry2024.csv`.*

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
