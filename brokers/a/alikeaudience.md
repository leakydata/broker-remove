# AlikeAudience

- **Email:** privacy@alikeaudience.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** alikeaudience.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-24)
- Note: 2026-08-24: audience-data letter. Substituted the geographic query for the MAID the consumer cannot supply, asked for the graph edges not just identifier rows, named the sensitive inference categories explicitly, and asked which app SDK any segment originates from.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@alikeaudience.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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


## The consumer cannot supply the key, so give them a query they can run

Audience businesses index on device and hashed identifiers. A name lookup returns
a true nothing while a full profile exists, and the requester cannot close the
gap: **nobody can look up their own advertising ID historically** — it is
resettable and was never disclosed to them.

The letter therefore supplies queries the broker *can* run: hashed forms of each
email address, the phone numbers, and **any device with a persistent overnight
dwell pattern** at the current and prior addresses. A residential overnight
pattern identifies a household member about as reliably as a name field.

Stated with the reason attached, so a name-keyed null result cannot be used to
close the request.

**Sensitive categories are named rather than left to a general assurance** —
health, finances, religion, politics, sexuality, household composition. A
blanket "we hold no sensitive data" does not reach an inference the broker does
not classify as sensitive.

**One ask specific to app-derived data:** which SDK or category of app a segment
originates from. That is a collection point the subject never knowingly agreed to
and cannot discover independently.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** AlikeAudience Inc
- **Trading as:** AlikeAudience
- **Registered address:** 440 N Wolfe Road, Sunnyvale, California, 94085
- **Filed contact email:** privacy@alikeaudience.com
- **Filed phone:** 852-6172-7413
- **Website:** alikeaudience.com

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
