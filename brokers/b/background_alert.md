# Background Alert Inc

- **Email:** info@BackgroundAlert.com (verified)
- **Method:** unknown — Route not yet established.
- **Domain:** backgroundalert.com
- **Priority: 1.**

## Status

- Current: `unreachable` (updated 2026-09-12)
- Note: HARD BOUNCE 2026-09-12, two seconds after sending: '550 5.1... the address couldn't be found, or is unable to receive mail' for info@backgroundalert.com. That address came from the Optery directory (SF 445) and is the first of the four test letters to fail. THE DOMAIN IS NOT DEAD, WHICH IS THE INTERESTING PART: backgroundalert.com has live MX records (mx1/mx2.emailsrvr.com, Rackspace), so mail is configured -- it is the specific local-part that does not exist. But the WEBSITE does not respond at all: both the front page and a control path return no HTTP response whatsoever (curl exit with 000, not a 4xx or 5xx). So the picture is a domain whose mail is provisioned and whose site is gone, which usually means a company that has folded or moved without releasing the domain. NO ALTERNATIVE ROUTE FOUND and none guessed: with the site down there is nothing to scrape for a form or a different address, and firing probes at privacy@ and support@ would produce more indistinguishable bounces, which is exactly the failure mode the enrichment script's own docstring warns about. Recorded unreachable rather than failed: there is no route a consumer can use today. Worth a re-probe if the site returns.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `info@backgroundalert.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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

- **Legal entity:** Background Alert
- **Registered address:** 9692 Melinda Circle, Huntington Beach, CA
- **Filed contact email:** [named individual]@backgroundalert.com
- **Website:** https://www.backgroundalert.com

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
