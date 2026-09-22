# Babel Street, Inc.

- **Email:** privacy@babelstreet.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** babelstreet.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-09-22)
- Reference: `gmail:1a0c5d620865108c`
- Note: 9/21, a new OneTrust auto-notice (still Request ID P7MJRE69RA): "Your
  request cannot be completed at this time... we have not received sufficient
  information to complete the identity verification process." No specifics on
  what was missing, and no portal login used to check (see below on why).
  Rather than opening the portal, emailed privacy@babelstreet.com directly
  9/22 — the address that has previously worked for reaching an actual
  person here (see the prior ticket-opened-on-our-behalf history below) —
  re-stating name/DOB/phone/address/4 emails, offering a utility-bill proof
  of address, and explicitly declining to upload a government ID (per this
  project's hard rule and the CPRA's necessary-and-proportionate standard for
  a request of this scope). Asked them to say what would actually satisfy
  verification short of an ID. **Do not treat "insufficient verification" as
  a dead end that requires escalating to ID upload** — try the direct email
  route to the human contact first, since the portal notice reads like a
  generic OneTrust template rather than a considered judgment about this
  specific request.
- Prior (2026-09-17): `submitted`, reference `gmail:1a078cb4896ef047`. noreply@m.onetrust.com, 2026-09-15 14:52 UTC: "A comment has been added
  to your request (Request ID: P7MJRE69RA). Please click the button below to
  access your request in the privacy portal." The email carries no content
  beyond that — same shape as the Merkle/dentsu OneTrust notice — and the
  comment text is only visible after logging into the portal. **Needs a human
  with a browser** to open it and read the comment, including checking the
  masked-phone discrepancy flagged below. Nothing to action by email alone.
- Prior: TICKET OPENED BY THEM, ON OUR BEHALF, 2026-09-10 -- the opposite of the usual designated-method refusal. Sequence: 06 Sept letter to privacy@babelstreet.com; 10 Sept 04:22 auto-reply inviting submission through their DSR portal; 10 Sept 10:12 reply confirming the request and asking to proceed BY EMAIL rather than the portal, on the ground that the portal asked for nothing the letter had not already supplied; 10 Sept 14:05 they answered that they had opened a ticket on our behalf, noting the necessary information was already provided; 14:06 OneTrust confirmation email for NEW request ID P7MJRE69RA. Most companies treat pointing at a form as discharging the obligation (SILENT_FAILURES 148 and the designated-method pattern); Babel Street did the transcription themselves. Queued for the confirm click, superseding the stale TGWANMEESR item from 28 August. ONE THING TO VERIFY AT THE PORTAL: the confirmation email shows the request contents partly masked and the phone reads 'XXXXXXXXXX651'. No number in profile.json ends 651 -- not the current one and none of the eleven prior. That may only mean OneTrust's masking is not 'last three characters', so it is flagged rather than asserted; if the portal shows a full value that is not the subject's, it needs correcting before the request is actioned.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://privacyportal.onetrust.com/webform/43f52ed9-df36-44dc-94b6-ce2f8458ca29/2ddc0d62-7d6a-4de2-b5c4-9f9f68116970
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `privacy@babelstreet.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

**A OneTrust "insufficient verification" notice can be a template, not a
considered decision — email the human address directly rather than escalating
into the portal.** This ticket already has a documented history of Babel
Street staff doing extra work by hand (opening a ticket on the requester's
behalf) once reached directly by email. When the automated notice arrives with
no specifics on what's missing, replying to `privacy@babelstreet.com` with the
identifiers already given, plus an offer of a lesser proof-of-address document,
is worth trying before assuming an ID upload is required.

**Never upload a government ID for this kind of request.** Babel Street is an
OSINT/identity-aggregation product; removing a name/phone/address match does
not require government-ID-level assurance under CPRA's necessary-and-
proportionate standard. State that explicitly and ask what lesser verification
would work.

**Masked confirmation data is worth checking against the actual profile
before assuming the request matched the right person** — see the flagged
phone-number-ending discrepancy in the superseded note below; it was never
resolved because the ticket moved on to a new ID, so if it recurs on a future
OneTrust confirmation, check it again.

## Verification

Watch for Babel Street's reply naming what verification would suffice. If it
again names only "the portal," push back once more on the ground that the
portal's own request already required nothing beyond what's already been
supplied by email.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Babel Street, Inc.
- **Registered address:** 1900 Reston Metro Plaza, Suite 950, Reston, VA,
  20190
- **Filed contact email:** privacy@babelstreet.com
- **Filed phone:** 7039563572
- **Website:** https://www.babelstreet.com

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
