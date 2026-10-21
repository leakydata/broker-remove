# Catalist LLC

- **Email:** privacy@catalist.us (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** catalist.us
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-10-20)
- 2026-10-20 CORRECTION to the 10-09 note below: the form WAS submitted
  after all. Catalist's reply of 2026-10-20 quotes the full "My Privacy
  Choices Form Submission" back verbatim, including "Verified on:
  2026/10/09 19:20:17" -- so the one-time code sent at 19:11 UTC *was*
  used, contrary to what was recorded here eleven days ago. Recording the
  correction rather than editing it away, per project convention. The
  outcome is still good news either way: Catalist's reply is "We are
  unable to find a match in our records using the information provided,"
  which is exactly what should happen to a fresh search run against a
  record already deleted on 28 August -- a second, independent nil that
  corroborates the original deletion rather than contradicting it. Status
  stays `confirmed`; this is supporting evidence, not a regression.
- Prior (2026-10-09, DUPLICATE SUBMISSION, PARTIALLY WRONG -- SEE ABOVE): The browser loop drove the stale handoff item, filled the full privacy form and requested a verification code; privacy@catalist.us sent one-time code at 19:11 UTC. Catalist confirmed deletion on 28 August with an itemised four-identifier match list, and confirmed a minimal forward-looking suppression on 31 August -- there was nothing here to re-request, and re-filing put a broker that answered well through the work twice. See _SILENT_FAILURES 455 for how the stale item came to be driven at all, and handoff.py --prune for the fix.

## Steps

1. Email is not accepted for processing — privacy@catalist.us auto-replies that
   requests must go through their form.
2. Form (queued in `handoff.py`): `https://catalist.us/your-privacy-choices`
3. Phone fallback: (800) 938-9516.

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

- **Legal entity:** Catalist LLC
- **Registered address:** 1310 L St NW, Ste. 500, Washington D.C., DC,
  20005
- **Filed contact email:** privacy@catalist.us
- **Filed phone:** 2029627200
- **Website:** http://catalist.us

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
