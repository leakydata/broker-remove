# The AutoMiner, TruPayments, PureCars

- **Email:** privacy@purecars.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** purecars.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-10-29)
- 2026-10-29: **Correction to this row's own history, and to SILENT_FAILURES
  §205/§425 as applied to PureCars: `privacy@purecars.com` is not dead.**
  Both the original 2026-09-11 letter (sent to `hello@purecars.com` because
  the registry address's autoresponder had claimed to be unmonitored) and a
  separate letter sent directly to `privacy@purecars.com` both received
  substantive replies **from `privacy@purecars.com` itself**, cc'ing
  `privacy+response@purecars.com`. Quoted in full: *"After conducting a
  diligent search of our records, we have not found any data related to
  you in our systems... PureCars has also acknowledged your request to opt
  out of the processing of your personal data for purposes of: targeted
  advertising; the sale of personal data; and/or profiling... We have also
  notified any service providers, contractors, and/or third parties to
  which we disclosed your information about your opt-out request, and
  instructed them to comply... We will continue to honor your opt-out
  request for at least twelve (12) months."* This is a genuine
  `not_found` on the identifiers searched plus an opt-out acknowledgement
  with a stated 12-month forward-looking honor period and third-party
  notification — about as complete an answer as this kind of letter gets.
  **The prior autoresponder claiming the mailbox was unmonitored was either
  stale, scoped to a different submission channel, or simply wrong — a
  human-reviewed mailbox can still fire a dead-channel autoresponder on
  receipt before a person reads it.** Do not take an autoresponder's claim
  about its own channel at face value without a later data point; this is
  the second time in this project an "unmonitored" autoresponder preceded a
  real human reply (see `_SILENT_FAILURES.md` for the general pattern).
  Nothing further needed here; record applies to PureCars, AutoMiner and
  TruPayments jointly per the entity's own reply.
- Note: NEW ROUTE FOUND AND USED 2026-09-11 -- hello@purecars.com, their general contact, because it is the only address a consumer can actually reach. THE REGISTER ADDRESS IS DECLARED DEAD BY THE REGISTRANT: privacy@purecars.com is the contact on their California data broker registration, and their own autoresponder says 'this email address is no longer part of our data subject request process and it is not being monitored' (SILENT_FAILURES 205, recorded under dead_addresses as kind declared_unmonitored -- not a bounce, not a restricted group, not a departed employee; the mailbox works, answers, and the company states nobody reads it). AND THERE IS NO ALTERNATIVE ROUTE ON THEIR SITE. purecars.com/privacy-policy is real (negative control: a nonsense path returns 404, so the page discriminates) and publishes exactly four opt-out links: tools.google.com/dlpage/gaoptout, optout.networkadvertising.org, optout.aboutads.info and app.retention.com/optout/. The first three are other companies' advertising-cookie opt-outs and the fourth is a vendor's own form. NONE removes anything PureCars holds -- SILENT_FAILURES 425 exactly, the route that resolves and loads and removes nothing. No consumer-rights form, no portal, no working privacy mailbox. LETTER SENT covering PureCars, TruPayments and AutoMiner together, asking them to say which brands were searched; requesting delete, opt-out, third-party direction and forward-looking suppression; and asking two things they are uniquely placed to answer -- whether any of the data derives from a dealership, vehicle record, service visit or finance enquiry rather than web activity, and where privacy requests should actually go, with a suggestion to update the register to match. Prior addresses deliberately NOT pasted into a general mailbox; offered on request. SUPPLY-CHAIN NOTE: linking app.retention.com/optout/ from their own policy discloses that PureCars uses RETENTION.COM, the identity-resolution vendor. Both Retention.com rows are already tracked -- retention_com is confirmed, retention_com_rb2b is submitted -- so no new broker, but the dependency is now evidenced from PureCars' side.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@purecars.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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

- **Legal entity:** PureCars Technologies, LLC
- **Trading as:** The AutoMiner, TruPayments, PureCars
- **Registered address:** 931 Monroe Drive NE Suite A102 #359, Atlanta,
  GA
- **Filed contact email:** privacy@purecars.com
- **Website:** https://www.purecars.com

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
