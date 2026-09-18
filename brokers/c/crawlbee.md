# CrawlBee Corp

- **Email:** privacy@crawlbee.com (bounced 2026-08-25 — domain no longer theirs)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** crawlbee.com — **do not trust this domain going forward.** It now
  redirects to a GoDaddy "domain for sale" parking page, confirmed 2026-08-25.
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-25)
- Note: 2026-08-25: bounced - 'the domain crawlbee.com couldn't be found'. Diagnosis: crawlbee.com publishes a NULL MX (RFC 7505: a lone '0 .' record), which is the domain owner stating explicitly that it accepts no mail. It still serves an A record and its SOA is ns2.afternic.com - an domain marketplace - so the domain is parked for sale and the company is likely defunct. THIS EXPOSED A BUG IN check_email_domains.py, now fixed: the checker returned True on any MX record present, so a null MX read as deliverable. That is worse than a missing record, because the send is refused immediately, the broker gets marked submitted, and nobody learns the letter never left.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@crawlbee.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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

- **Legal entity:** CrawlBee Corp
- **Registered address:** 11700 Mukilteo Speedway Ste 201-2025, Mukilteo,
  WA
- **Filed contact email:** Privacy@crawlbee.io
- **Website:** https://crawlbee.com

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
