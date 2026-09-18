# AdeptID, Inc.

- **Email:** privacy@adept-id.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** adept-id.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-24)
- Note: 2026-08-24: routed to an Osano form (my.datasubject.com) that geo-detects Pennsylvania and renders NO fields at all - 'a jurisdiction that does not currently support privacy rights'. No submit path. The jurisdiction dropdown would open the form if set to another state; declined to misstate residency. Replied on the email thread asking them to honour it under their published policy and to report the vendor gate.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@adept-id.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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


## Ask for the derived layer, not the contact fields

AdeptID predicts suitability for work. A deletion scoped to name and email leaves
the consequential part intact, so the letter asks specifically for:

- skills inference, competency mapping, role-transition prediction
- employability, retention or attrition scores
- **inferred demographics** — gender, ethnicity, age band, socioeconomic class —
  including where inferred for bias measurement rather than targeting
- the employment and education history the above is derived from, **and where
  each element came from**

These are model outputs, not facts anyone supplied, and they are the elements a
person can least easily discover while employers act on them.

**The customer-upload question is the one that decides who to write to next.** If
an employer or staffing customer supplied the record, deleting AdeptID's copy
does not reach theirs. Asked them to name the customer or confirm they directed
deletion.


## 2026-08-24: the form will not open for a Pennsylvania resident

The email was received and routed to an Osano form (`my.datasubject.com`) with
*"you must fill out the following form"*. The form detects the jurisdiction and
renders **nothing** — no fields, no submit control:

> *"We have detected that you are attempting to submit a request from a
> jurisdiction that does not currently support privacy rights."*

Full write-up in `_DEFLECTIONS.md` §45. Three things to carry forward:

- **The gate is Osano's, not AdeptID's.** Any broker whose rights link lands on
  `my.datasubject.com` will do this to a requester in a state without a
  comprehensive privacy law. Check for it before spending time on the form.
- **The jurisdiction is a dropdown and it must not be changed.** Setting it to
  California would open the form and would be a false statement of residency made
  while asserting a legal right. Declined, and said so in the reply — naming it is
  what makes it fixable.
- **The email channel works.** Replied there asking them to treat the original
  message as the request, honour it under their published privacy policy, and
  raise the vendor gate with Osano.

**Status stays `submitted`**, not `failed` — a reply is outstanding on a live
channel. Recorded that the web route is closed to this requester so nobody
retries the form.

The substance of the request is unchanged and never depended on the form: the
derived layer, not the contact fields.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** AdeptID, Inc.
- **Registered address:** 184 High St, Suite 602, Boston, MA, 02110
- **Filed contact email:** privacy@adept-id.com
- **Filed phone:** 508-377-3103
- **Website:** www.adept-id.com

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
