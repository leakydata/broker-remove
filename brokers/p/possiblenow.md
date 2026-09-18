# Possiblenow

- **Email:** privacy@possiblenow.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** possiblenow.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Autoresponder, but a revealing one. Three findings. (1) THE OPT-OUT LINK IN THEIR OWN AUTORESPONDER IS DEAD: it points at site.possiblenow.com/do-not-sell-my-personal-information, which 404s onto what looks like a hosted knowledge base - the page title is 'How do I set up an NPS survey?'. The working page is the same path on www. One wrong subdomain, in the automated reply a consent-management company sends to every privacy request. (2) A CAPTCHA gates the form BEFORE the fields are shown - 'Verify & Continue to Form' - so nothing can be pre-filled or even inspected without solving it. (3) 'If you have multiple addresses or email addresses, please submit a separate request for each.' With 16 addresses and 12 emails that is 28 submissions, each behind its own CAPTCHA. Recorded as submitted on the EMAIL route, which is the substantive one: the letter asked them to KEEP suppression records and delete everything else, and a per-identifier do-not-sell form cannot express that distinction at all. Their reply confirms email is not foreclosed - 'We will respond to your questions or concerns in a timely manner.'

## Correction (2026-08-27): a duplicate second letter was sent to a sibling address

A separate registry row (`possiblenow` in `data/curated_brokers.json`, `email_to`
`californiadrop@possiblenowmarketing.com` — note `possiblenowmarketing.com`, not
`possiblenow.com`) was picked as a "fresh" batch candidate and emailed the same
day this playbook was written up, without checking this file first. It is the same
company under a second CA-registered brand address, already `submitted` above
since 2026-08-19.

**Lesson, restated from the AcademixDirect playbook because it just repeated
itself with a different broker:** diffing Gmail Sent against a domain list is not
a substitute for reading each candidate's own playbook `Current:` status before
sending. A domain-only diff misses a second registered address for the same
company on a sibling domain. `queue_batch.py`'s "spoken-for address" and
duplicate-family logic exists precisely to catch this and was not used for this
batch — `data/removal_status.json` doesn't exist in a fresh clone, so the script
has nothing to check against, and a manual domain diff is a weaker substitute.
No harm beyond one redundant email; recorded here rather than treating the
second thread as a new, unrelated submission.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.possiblenow.com/do-not-sell-my-personal-information
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `[named individual]@possiblenowmarketing.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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

- **Legal entity:** PossibleNOW, Inc.
- **Registered address:** 4400 River Green Parkway, Suite 100, Duluth,
  Georgia, 30096
- **Filed contact email:** [named individual]@possiblenowmarketing.com
- **Filed phone:** 7702551020
- **Website:** possiblenow.com

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
