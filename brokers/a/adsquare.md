# Adsquare

- **Email:** privacy@adsquare.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** adsquare.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-07)
- Reference: `4XA7NCDD84`
- Note: PORTAL LOGGED THE FOLLOW-UP AS A NEW REQUEST. The reply asking whether the geographic dwell-pattern query was run came back as 'Your request has been successfully submitted. Your Request ID is 4XA7NCDD84' -- a SECOND request id, not a continuation of 8WN6LE4TGK. So their intake treats any inbound mail on the thread as a fresh DSAR. Consequence to watch: the geographic question may be answered as a new request against the same identifiers, which would produce the same identifier-keyed nil and never reach the point. If the next reply is another 'did not find any match in our databases', that is the intake behaviour rather than an answer, and the question will need putting again with the request id quoted. Not a complaint -- auto-logging is better than silent discard -- but it is a route where a follow-up cannot be distinguished from a first contact. The substantive position is unchanged: nil on the identifiers supplied, geographic query unconfirmed. Request ids on file: 8WN6LE4TGK (original, completed) and 4XA7NCDD84 (the follow-up).

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@adsquare.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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


## The geographic query, because the consumer cannot supply a MAID

Adsquare is a location and audience exchange. The record is keyed to a mobile
advertising identifier, and **no consumer can look up their own advertising ID
historically** — it is resettable, it was never disclosed to them, and asking for
it is asking them to produce something the industry generated.

So the letter substitutes a query they *can* run: **any device showing a
persistent overnight dwell pattern at the current address**, and at each prior
address for the period of residence. A residential overnight pattern identifies a
household member about as reliably as a name field.

Stated with the reason attached, so a name-keyed null result cannot be used to
close the request: *"please answer the geographic question before concluding a
name search found nothing, because a name-keyed search is the wrong query for a
location dataset."*

Standard identity-graph asks also apply: hashed email match keys (separating
suppression hashes, which are fine, from matchable inventory, which is not),
device and CTV identifiers, **the edges** between identifiers and name/address,
IP-derived household association, and inferred segments.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** adsquare GmbH
- **Trading as:** Adsquare
- **Registered address:** Saarbrücker Str. 36, Berlin, BE
- **Filed contact email:** legal@adsquare.com
- **Website:** https://www.adsquare.com

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
