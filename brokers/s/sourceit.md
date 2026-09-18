# Sourceit

- **Email:** dataprivacy@sourceitmarketing.com — verified against their own published page
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** sourceitmarketing.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-20)
- Note: COVERED BY THE LISTMATCH ANSWER 2026-08-31. Same operator (Jo[PERSONAL]), same dataprivacy2026@<domain> address convention. He confirmed the suppression hash 'applies to them all' across every company he manages, and that there are no registered entities beyond these two. So SourceIt is suppressed on the same basis as ListMatch without a separate request. See email_marketing_services for the full exchange.

## Steps

1. **Do not click the contact link on their privacy policy.** Its `mailto:` href
   and its visible text are different mailboxes, and the href is dead
   (`_SILENT_FAILURES.md` §66).
2. Mail the **year-stamped** address that appears in the policy's running text —
   the same local part with the current year appended. Three plain-text
   occurrences in the policy use it; only the anchor's href is stale.
3. Use the subject line their policy requires for opt-outs:
   **`CCPA Opt-out`**.
4. Second routes worth trying: their self-service portal at `/privacy`, and the
   "Do Not Sell My Info" link on the home page. Both are named in the policy.

## Gotchas

- **The address has an expiry date.** A year stamp in a privacy mailbox means a
  (CORRECTED: not rotation - a botched WordPress edit, fixed by them 2026-08-20. Record when
  you verified it, not only that you did.
- **Automated verification will confirm the wrong address.** Both mailboxes
  appear in the fetched HTML — one in the href, one in the link text — so an
  extractor that pools everything on the page will happily confirm the dead one
  and stop looking. Compare href against text explicitly.
- **The bounce is mailbox-level, not domain-level.** Office 365 answers with
  "Recipient Unknown" while the domain, MX and site are all healthy, so the
  failure reads like a typo on your side.

## Verification

No public profile. The observables are their answer on suppression-vs-deletion,
and whether they name the compiler that supplied the record — the request asked
for both separately and offered an explicit exit on the source question.

## Outcome: confirmed, and the most complete answer in the project so far

The operator replied personally within hours, and answered every question asked.

**The removal.**

> "We only had the record of [one old webmail address] which has been removed."

One old webmail address out of twelve supplied — which is itself the argument for
listing every historical address rather than the current one. A search of the
current details would have found nothing and closed the file.

**The hashed-email question, answered voluntarily and correctly.**

> "We keep a SHA1/SHA256 hash, and your other email records are hashed to not be
> added again."

This is the *right* use of a hash and it should be accepted rather than argued
with. A suppression list that forgets you cannot suppress you. The distinction to
hold onto is between a hash kept so a record is never re-added, and a hash kept
as saleable match inventory — the first is compliance, the second is the product
wearing a disguise. Asking the question as a fork ("confirm these are covered or
tell me plainly which are not") is what makes the good answer easy to give.

**The broken link was real, and they fixed it.**

> "Thanks for letting us know. We corrected the page, it was failed change in
> wordpress."

See `_SILENT_FAILURES.md` §66, including the correction — the year stamp was not
a rotation policy, it was a botched WordPress edit. Reporting the fault plainly
in the letter cost two sentences and bought a same-morning fix plus a full
answer to everything else.

**They named their suppliers, unprompted by anything but the standard ask.**

> "The email contact lists that we have is from other third parties/data brokers,
> which include L2 Data, Apollo, DatabaseUSA, Zoominfo, LinkedIn, GetProspects,
> ExactData. We do not operate websites that collect consumer email lists."

Five were already tracked. One (LinkedIn) is a platform the subject has an
account with rather than a broker to write to. **L2 Data was not in the registry
at all** — a 250-million-record voter and consumer broker, surfaced only because
a reseller was asked where its data came from. See `brokers/l/l2_data.md`.

**"We go by email addresses for all our records"** confirms the join key, and
"we do not operate websites that collect consumer email lists" places them as a
pure reseller — which is exactly why the supplier question mattered more here
than the deletion did.

## What to reuse

Ask every reseller, in the first letter: *if you licensed my information from a
supplier, please tell me which one.* It costs a sentence. When it is answered it
converts one confirmed removal into a list of upstream sources, and the upstream
is where the record actually originates. A deletion at the reseller is undone by
the next ingest; a deletion at the source is not.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** SourceIT Technologies, Inc
- **Registered address:** 2206 N Main Street, Suite 183, Wheaton, IL
  60187, United States
- **Filed contact email:** dataprivacy@sourceitmarketing.com
- **Website:** https://www.sourceitmarketing.com/
- **Opt-out route they filed:** The consumer can visit our website in the
  footer there is a link to Do not Sell My Personal Information and goes
  to https://www.sourceitmarketing.com/privacy, From that page they can
  request to opt out or view/manage their data. A consumer can also
  contact us via our toll free number 800-478-8089, or the contact form
  on our website.
- **Route for protected individuals:** A protected individual can visit
  https://www.sourceitmarketing.com/privacy to have their profile
  information deleted. Or give us a call at our toll free number
  800-478-8089 (Cal. Gov. Code 6208.1(b) / 6254.21(c)(1) — for survivors
  of domestic violence, stalking and similar, a stronger and faster route
  than the ordinary consumer request)
- **What they say they collect:** For our data collection policies please
  visit our privacy policy on our website for the most up to date
  information.

*Source: `data/registries/complete-reg-data-brokers.csv`.*

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
