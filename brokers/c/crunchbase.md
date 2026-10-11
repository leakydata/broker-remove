# Crunchbase

- **Opt-out:** https://preferences.crunchbase.com/form/opt_out
- **Email:** legal@crunchbase.com (verified)
- **Method:** web_form — Web form.
- **Domain:** preferences.crunchbase.com
- **Priority: 3.**

## Status

- Current: `replied` (updated 2026-10-11)
- Note: THE NIL IS VERIFIED BUT MAY BE A FALSE NIL ON KEYS, AND THEY SAID SO THEMSELVES. 2026-09-03 from Frank at support@crunchbase.com, ticket 2820893: 'We have completed our review and were unable to locate any information about you based on the details provided. IF YOU BELIEVE WE HOLD INFORMATION UNDER A DIFFERENT NAME, EMAIL ADDRESS, EMPLOYER, OR PROFILE URL, please reply with those details and we will reassess.' So not_found was honestly recorded for the keys supplied -- but Crunchbase is organised around companies, people's roles in them, and profile URLs, which means a search on a personal name and personal email ran against the fields LEAST likely to hold a record while the fields most likely to hold one were never searched, because we never sent them. This is the SeekOut shape from 450: three refusals to act without the LinkedIn URL, then deletion the same day it was supplied, and withholding it had produced false nils. REPLIED 2026-10-10 taking up the offer: supplied the LinkedIn profile URL (authorised 2026-09-13) and asked for it to be treated as a SUPPRESSION key, not just a search hint, because a continuously re-crawled public profile undoes a deletion at the next ingest. Also supplied [EMAIL] as a historic institutional key WITH AN EXPLICIT WARNING THAT IT IS A CLOSED MAILBOX and must not be used as a reply address. Asked two further things: which fields the second search actually covered, since a nil after a profile-URL search is a far stronger nil than one after a name search; and for the disclosure BEFORE any deletion, access first. Status moved off not_found to replied because the question is reopened by their own invitation, not because their answer was wrong. CREDIT WHERE DUE, AND WORTH COPYING: their nil NAMED THE FOUR FIELDS THAT WOULD CHANGE THE ANSWER. Most nils stop at 'no records found', which leaves the requester unable to distinguish a true absence from a missed key. This one turned a dead end into a next step.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://preferences.crunchbase.com/form/opt_out
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `legal@crunchbase.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Crunchbase, Inc.
- **Trading as:** Crunchbase
- **Registered address:** 564 Market St., Suite 500, San Francisco,
  California, 94104
- **Filed contact email:** legal@crunchbase.com
- **Filed phone:** 4158490002
- **Website:** crunchbase.com

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
