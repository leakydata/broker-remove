# Veripages

- **Opt-out:** https://veripages.com/optout
- **Email:** support@veripages.com (verified)
- **Method:** web_form — Web form.
- **Domain:** veripages.com
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-08-26)
- Reference: `gmail:1a03d9ebd6db6258`
- Note: 2026-08-26: supplementary letter sent with the four late email addresses, six prior postal addresses and three prior phone numbers. Framed as completing the request already on file, not a new one. Asked them to enumerate the identifiers searched.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://veripages.com/optout
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `support@veripages.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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

## Email is answered by a human, and points at a web form

`support@veripages.com` replies quickly and usefully:

> *"Veripages has a tool to remove information on the homepage labeled Do Not Sell
> My Info. You can submit your removal request here,
> https://veripages.com/inner/control-privacy"*

## The form needs a profile URL you cannot get

The same reply insists on an exact URL format:

> *CORRECT FORMAT: `https://veripages.com/profile/Tom-Lee/HTHQAoBB`*
> *wrong format: `https://veripages.com/name/Tom/Lee/`*

**That format is not present in their public search results.** Inspecting the
result pages for every anchor, the only person links are `/name/First/Last/` — the
format the email calls wrong. "View all details" does not resolve to a
`/profile/<Name>/<ID>` address, and clicking through raises a **"$1 – 7 day trial
access"** modal before any detail appears.

So the removal route requires an identifier that the free site does not hand out.
See `_DEFLECTIONS.md` §12 for how to answer this without simply giving up.

## Search notes

- `/inner/profile/search?fname=<First>&lname=<Last>&state=<ST>` works, and accepts
  `&city=<City>`. The city filter is loose: results include people who merely
  *lived* in that city at some point, so unrelated records from other states
  appear.
- Result cards show aliases, cities, relatives and partial phone numbers, but
  **no date of birth**, and age is missing on some. With a common name that leaves
  very little to disambiguate on.
- A common first-and-last-name search returned **214 people in one state** over 20
  pages.

## Scope note

Cards are labelled "Data provided by Veripages" alongside sponsored panels for
TruthFinder and BeenVerified. Removal here does not touch those services — they
are separate brokers with their own opt-out routes.

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
