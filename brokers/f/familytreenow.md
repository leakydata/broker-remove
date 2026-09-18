# FamilyTreeNow

- **Working route:** https://www.familytreenow.com/privacy-rights  ← use this
- **Bot-gated:** https://www.familytreenow.com/optout (Cloudflare hangs on load)
- **Email: refused.** support@familytreenow.com replies that privacy requests are
  not processed by email.
- **Priority: 4.** Genealogy angle means relatives and address history are exposed.

## Status

- Current: `submitted` (updated 2026-08-26)
- Reference: `gmail:1a03bebec6d54a2e`
- Note: 2026-08-26: replied to the supplementary letter asking for 'the URL/web address of your profile details page so we can identify your profile' - which is circular, because they removed the profile on 2026-08-18 and confirmed it on screen. The only way to produce that URL would be for the removal to have FAILED. Answered by naming the circularity plainly, pointing out that a page URL is a front-end artifact while the request is about the index behind it, and asking them to search the supplied identifiers instead - which is what a back-end search takes anyway. Also asked the family question directly. Added the FamilyTreeNow-specific argument: it is a RELATIONSHIP index inferring family links from co-residence over time, so the six prior addresses are each a point where a link may have been recorded, and asked to be removed as a LINKED RELATIVE on other people's records, not only as the subject of his own.

## Same platform as TruePeopleSearch

FamilyTreeNow and TruePeopleSearch run the same privacy-request system: identical
form structure, identical auto-reply wording, and FamilyTreeNow's footer links to
TruePeopleSearch.com. **The same workaround applies to both** — see
`brokers/t/truepeoplesearch.md`.

Their confirmation page even leaks an unrendered template variable
("Thank you for sending your Context.Request"), which is a good tell that these
are one codebase.

## Route
`/privacy-rights` → *access, delete, or correct* → **Right to Know** (not Delete —
Delete renders no form) → *no direct relationship* → First/Last/Email/
*subject of this request*/Phone/Street/City/State/Zip → Submit.
Confirms at `privacy/privacyrightsconfirmation?success=True`.

## Gotchas
- Ask separately about **family-tree records**, which expose relatives and address
  history beyond a standard listing.
- State dropdown includes all 50 states — don't be deterred by the "if you live in a
  state with an applicable privacy law" preamble.

## Refused on jurisdiction; the opt-out route is a different door

The statutory "Right to Know" was refused because Pennsylvania has no comprehensive
consumer privacy law -- see `_DEFLECTIONS.md` §27 for the wording and for why
appealing that is a bad trade. The refusal arrived in the same minute, in the same
words, from TruePeopleSearch, FamilyTreeNow and PeopleSearchNow, which is the family
confirmation by itself.

Their self-service opt-out is a **separate mechanism** that never asks what state
you live in. It is an email-link flow: name and email plus a captcha, then a link
that **expires in 24 hours**, then a fuller form where the record details actually
go. Submitting only the first step achieves nothing while looking like progress.

## The self-service door worked where the statutory one was refused

The Right to Know submission was refused on jurisdiction -- Pennsylvania has no
comprehensive consumer privacy law (see `_DEFLECTIONS.md` §27). The self-service
opt-out, which never asks what state you live in, went through the same afternoon.

The confirmation page is a real artifact rather than a pleasantry, because it **names
the record back**:

> *"The following information was submitted to our system successfully. We will locate
> and remove your record based on the information you provided. Expect your
> information to be fully removed in 3 days or less."*

followed by the submitted name, city, ZIP and email. That distinguishes a completed
submission from a form that merely accepted a POST.

**Three stages, and only the last one counts.** Name and email plus a captcha; then an
emailed link that expires in 24 hours; then the fuller form carrying date of birth,
telephone, address, city, state and ZIP. Stopping after stage one looks like progress
and achieves nothing.

Their own warning explains why completeness matters here: *"If we receive new data
connected to a record that we were unable to identify based on your original request,
information you submit here may appear on our site in the future."* Partial
identifiers buy a removal that does not stick.

## A later letter with additional identifiers hit the customer-service wall

2026-08-26: wrote again — after the original opt-out was already confirmed
(above) — with four email addresses, six prior postal addresses and three
phone numbers that were not in the original submission, since FamilyTreeNow is
a relationship index and prior addresses are co-residence evidence, not just
contact details. Support first asked for the profile URL (circular: the
profile no longer exists precisely because the earlier removal worked), then,
on push-back, gave the real answer: `support@familytreenow.com` is
customer-service-only and does not process privacy requests — use
https://www.familytreenow.com/removal (the same self-service opt-out door
documented above) or https://www.familytreenow.com/privacy-rights.

**Needs a human to re-run the self-service opt-out with the additional
identifiers.** The route is already known and working (see above); this is not
a new investigation, just a resubmission with a longer identifier list.

## How to verify, and how not to

The confirmation page carries an unusually candid instruction about checking the work:

> *"Please make sure you clear your browser cache before attempting to confirm
> removal, or your device may pull up an old, stored version of our website. Also make
> sure you initiate a new search. Please do not attempt to verify removal by clicking
> on a saved link."*

Fresh search, clean session, live site. See `_SILENT_FAILURES.md` §31 -- a cached page
can report the removal failed when it succeeded, and a stale search-engine result can
report the opposite.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Family Tree Now, LLC
- **Registered address:** PO Box 515381 PMB 29296, Los Angeles, CA, 90051
- **Filed contact email:** privacy@familytreenow.com
- **Filed phone:** 8778384889
- **Website:** familytreenow.com

*Source: `data/registries/registry.csv`.*

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.familytreenow.com/optout
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `privacy@familytreenow.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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
