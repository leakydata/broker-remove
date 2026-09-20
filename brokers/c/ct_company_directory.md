# Ct Company Directory

- **Email:** info@ctcompanydir.com (verified)
- **Method:** unknown — Route not yet established.
- **Priority: 1.**

## Status

- Current: `manual_required` (updated 2026-09-20)
- Note: The 2026-09-18 letter to info@ctcompanydir.com hard-bounced the same day
  ("address couldn't be found, or is unable to receive mail"). The address had
  been carried as `email_verified: true` with `email_verified_by:
  "optery_directory"` -- i.e. it was never actually verified, only assumed
  correct because a commercial directory (Optery) listed the company. See the
  note under Gotchas: this basis is not evidence of a working mailbox, and a
  fair number of addresses imported the same way are still asserting a
  verification nobody has done.
- The site (ctcompanydir.com) returns HTTP 403 to an automated fetch, which is
  consistent with Cloudflare or similar bot-blocking rather than a dead
  domain -- it may well be live to a real browser. Nobody has checked with one
  yet.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `info@ctcompanydir.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

- **`email_verified_by: "optery_directory"` is not verification.** It means a
  commercial people-search/directory aggregation service (Optery) listed this
  company as a broker, and the address is whatever Optery's page showed --
  nobody at this project independently confirmed it accepts mail. It hard
  bounced the first time it was used. If you find this note on another broker
  with the same basis, don't trust the address without checking; the
  legitimate bases are `delivery_evidence`, `privacy_policy`,
  `state_registry`, `broker_reply` (see CONTRIBUTING.md).
- A person with a browser needs to load ctcompanydir.com and its privacy
  policy (an automated fetch gets HTTP 403) to find whether a real contact
  address or web form exists.

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
