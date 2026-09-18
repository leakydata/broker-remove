# Data Axle (infoUSA)

- **Opt-out:** https://www.data-axle.com/privacy-rights-request/
- **Email:** privacyteam@data-axle.com — **unverified, may bounce**
- **Method:** web_form_captcha — Web form with a CAPTCHA — see where it sits (page load vs submit).
- **Domain:** data-axle.com
- **Priority: 5.**

## Status

- Current: `replied` (updated 2026-09-06)
- Reference: `gmail:1a0773393cdcf4e0`
- Note: UNITEMISED NIL 2026-09-06 from PrivacyTeam@data-axle.com: 'We have conducted a search for your personal information in the Data Axle database and your information has not been located.' Covers opt-out, correction, deletion, access and limit-use in one line. THIS IS THE HARDEST NIL IN THE SET TO READ, and that is why it was queried rather than accepted. Data Axle compiles from public-record, directory and business sources keyed largely on NAME AND ADDRESS HISTORY -- the subject has sixteen addresses across PA, MD and AL going back to the 1990s, four name variants and eleven prior phones. If any US compiler held a record it would be one built that way, so the nil is genuinely informative IF it ran on the right keys, and near-guaranteed if it did not. TWO QUESTIONS ASKED, each with an explicit undertaking to close on any answer. (1) WHICH IDENTIFIERS: the 18 August letter carried a short list; the 25 August supplementary letter added the sixteen prior addresses, eleven prior phones, eight obsolete emails and the name variants. A search against the first list only would return nil regardless of holdings. Cited the 330 demonstration -- six current identifiers found nothing at another company, a closed university mailbox and a prior address found a record immediately, same week. (2) WHICH DATABASE: their reply says 'the Data Axle database', singular. Data Axle runs a consumer file AND a large business and professional file, indexed differently. The subject has a public professional profile and a former institutional address at an educational domain -- exactly what a B2B contact file is keyed on and what a consumer household file would never carry. 'Consumer only' is an acceptable answer and would mean re-requesting against the business file. ALSO RE-ASSERTED THE ASK THAT SURVIVES A NIL: a forward-looking do-not-add suppression. In a compiled business a record absent today arrives in the next refresh from a supplier who has it, and a deletion does nothing about that -- while they hold nothing is the only moment the suppression is free. Full identifier set restated inline so nothing depends on retrieving the earlier letters.

## Steps

1. Use the **Consumer Privacy Rights Request** form at
   `https://www.data-axle.com/privacy-rights-request/`. Do not use the
   Authorized Agent form — that is for agents acting for someone else, and this
   is a first-party request.
2. Fill first/last name, address, city, state, ZIP, email and phone. All are
   required.
3. Choose the **Privacy Choice**. It is a single-select — see below.
4. Tick the attestation box, then submit. A reCAPTCHA sits on the submit.
5. **Submit the form a second time** with a different Privacy Choice, for the
   second right you want.

One form covers Exact Data as well; it runs on the same domain and publishes the
same privacy address.

## Gotchas

**The Privacy Choice dropdown is a single-select, and its options are rights, not
categories:**

    Request to opt out of sale/sharing
    Request to correct inaccuracies
    Request to delete
    Request to access
    Request to limit use/disclosure of sensitive personal information

So one submission buys **one right**. A consumer who wants their data deleted
*and* wants to stop it being sold has to submit twice, and nothing on the page
says so. Pick "Request to delete", submit, then do the whole thing again with
"Request to opt out of sale/sharing".

This is the same shape as Belardi Wong's three separate OneTrust form UUIDs, and
it is worth treating as a general rule: **wherever a form asks you to choose a
right, assume the others were not requested.** The confirmation will be accurate
and will cover only what you picked. See `_SILENT_FAILURES.md`.

## The consent clause

Their privacy policy contains a claim worth reading twice:

> *"By agreeing to this privacy policy, you hereby consent to Data Axle using your
> personal information for commercial purposes now, and at all times in the
> future, regardless of when or how Data Axle acquired your personal information,
> unless and until you opt out."*

Read plainly: a person who has never visited the site, never agreed to anything,
and whose data was acquired from a third party is deemed to have consented —
permanently, and to any future use — with an opt-out as the only exit.

Whatever its legal weight, it tells you how the business is structured, and it is
the reason the opt-out submission matters as much as the deletion. Deletion
removes what they hold today; the opt-out is what addresses the standing
permission they assert for tomorrow. **Do both.**

The policy also states outright that the entity maintaining the site is a data
broker — useful, since a self-declaration forecloses the "we are not a data
broker" deflection before it is offered.

## Verification

Nothing public to search. Ask the confirmation to state **which right** was
actioned, and keep both confirmations separately — one per submission. Two
confirmations that both say "your request has been processed" are not
interchangeable, and only the pair together shows deletion and opt-out were both
requested.

## Scope: Exact Data is covered here

Data Axle's privacy-rights form names `exactdata.com` within its own scope, so
the two submissions made through it (deletion and opt-out of sale, which are
single-select and therefore need one run each) cover Exact Data as well.

`exact_data` is recorded as submitted and aliased to this playbook rather than
left pending, because a sibling that is genuinely covered looks identical in a
tracker to one nobody named — and the family scan flagged the pair every pass
until it was resolved one way or the other.

If a reply comes back scoped to one brand only, this reverts and Exact Data needs
its own request.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Data Axle Inc.
- **Trading as:** Data Axle
- **Registered address:** 2451 W Grapevine Mills Cir. #538, Grapevine,
  Texas, 76051
- **Filed contact email:** privacyteam@data-axle.com
- **Filed phone:** (402) 836-3377
- **Website:** https://www.data-axle.com

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
