# Buildertrend

- **Opt-out:** https://buildertrend.com/privacy-policy/
- **Email:** privacy@buildertrend.com (verified)
- **Method:** web_form — Web form.
- **Domain:** buildertrend.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-09-03)
- Reference: `form entry ID on file`
- Note: 2026-09-03 (§308): STOPPED ASKING BY EMAIL. Two letters to privacy@buildertrend.com produced two copies of an identical macro: 'It looks like your request wasn't submitted through the designated method outlined in Section X of our Privacy Notice.' My second letter said plainly that I WANTED to use the designated method and could not find Section X in the notice at buildertrend.com/privacy-notice/ -- and was answered with the same macro naming the same section. A pointer to a section that cannot be located is not a designated method; it is a dead end that reads like an instruction. DO NOT PRESS AGAIN BY EMAIL: a third letter reaches the same macro. Note also 11 CCR 7026(f) -- to the extent this is an OPT-OUT, a business may not condition it on using a particular verification route. Separately corrected a registry error found by the same audit: the row carried legal@buildertrend.com, an address never actually used; all real correspondence went to privacy@.

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
