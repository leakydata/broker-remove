# LiveRamp

- **Opt-out:** https://liveramp.com/privacy/my-privacy-choices
- **Email:** consumercare@liveramp.com — verified (published on their own
  my-privacy-choices page). `ukprivacy@liveramp.com` auto-replies that it is
  scoped to GDPR/services requests only — wrong desk for a US consumer request.
- **Method:** web_form — Web form.
- **Domain:** liveramp.com
- **Priority: 5.**

## Status

- Current: `submitted` (updated 2026-08-27)
- Reference: `gmail:1a042df1aea836ab`
- Note: 2026-08-27 CORRECTION TO MY OWN PREVIOUS NOTE. The full request was resent to [named individual]@liveramp.com after their UK Privacy Team named it as the US desk. But the registry note ALREADY recorded that address as published on liveramp.com/privacy/my-privacy-choices, so the UK team confirmed what was known rather than revealing it - I overstated that in the note written minutes ago. It also means the fault report in the letter, that none of their published privacy addresses is American, is WRONG: consumercare@ is published, just not alongside the thirteen region-scoped ones. Sending a short correction rather than leaving an inaccurate criticism standing. The substance of the request is unaffected.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://liveramp.com/privacy/my-privacy-choices
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `[named individual]@liveramp.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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

## Thirteen privacy addresses, none of them American

LiveRamp's privacy pages publish `privacy.ar@`, `privacy.be@`, `privacy.br@`,
`privacy.de@`, `privacy.es@`, `privacy.it@`, `privacy.nl@`, `privacy.no@`,
`privacy.pl@`, `privacy.ro@`, `privacy.se@`, `ukprivacy@` and `cil@` — and no
unqualified `privacy@` anywhere. See `_SILENT_FAILURES.md` §75.

Every one of those is a live, monitored mailbox. The defect is jurisdictional
scope, which no reachability check can detect: `dig` passes, delivery succeeds,
and the letter lands at a desk with no authority over a US resident's records.
From the requester's inbox that is indistinguishable from silence.

**Sent to `ukprivacy@` with the routing problem stated in the first paragraph.**
Naming it converts a misroute into a routing request, which is something a
regional desk can actually action — forward it and say where it went, or reply
with the right address. Guessing at `privacy@liveramp.com` was the alternative
and would have been a guess.

**Do not read the absence as evasion.** A company with eleven European privacy
contacts and no American one has built its privacy function around GDPR, where
naming a per-country contact is ordinary practice. The correct inference is about
org structure, not motive.

## What the letter asks for beyond the standard four

LiveRamp is an identity resolution business, so a deletion scoped to rows rather
than edges achieves nothing:

- hashed email forms (MD5/SHA-1/SHA-256) as match keys — with the distinction
  drawn between hashes held for **suppression** (supported, not asked to be
  deleted: a suppression list that forgets you cannot suppress you) and hashes
  held as **saleable match inventory** (asked to be deleted);
- RampID and every identifier mapped to it;
- MAIDs, cookie IDs, CTV IDs;
- **the edges** between those identifiers and name, address, email, phone — not
  merely the identifier rows. In an identity business the graph is the product;
- household association derived from IP;
- **do-not-onboard as a standing entry** — this is the specific mechanism by
  which a deletion here is undone by somebody else's action rather than
  LiveRamp's. A client uploading a file containing these details causes
  re-resolution and re-distribution. Deletion without do-not-onboard is a
  deletion with a refill valve attached.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** LiveRamp Holdings, Inc.
- **Registered address:** 225 Bush Street, 17th Floor, San Francisco, CA,
  94104
- **Filed contact email:** [named individual]@liveramp.com
- **Filed phone:** (888) 987-6764
- **Website:** www.liveramp.com

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
