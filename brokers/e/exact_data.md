# Exact Data

- **Email:** privacyteam@data-axle.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** data-axle.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-26)
- Reference: `gmail:1a03d9e46d461dde`
- Note: 2026-08-26: supplementary letter sent with the four late email addresses, six prior postal addresses and three prior phone numbers. Framed as completing the request already on file, not a new one. Asked them to enumerate the identifiers searched.

## Steps

Do not write to Exact Data separately. It runs on `data-axle.com` and publishes
`privacyteam@data-axle.com`, so the route is Data Axle's Consumer Privacy Rights
Request form — see **`dataaxle.md`**, which covers the whole flow.

The one thing to carry over: their Privacy Choice dropdown is a single-select, so
**submit twice** — once for deletion and once for opt-out of sale/sharing.

## Gotchas

This one was found by the registry rather than by reading anything: `dataaxle`
had **no contact address at all**, while `exact_data` — a separate entry, a
separate brand — published `privacyteam@data-axle.com`. The subsidiary's record
supplied the parent's missing route.

Worth noting as a search technique. `scripts/family_scan.py` groups brokers by
shared contact address, which finds families where several entries name the same
mailbox. It does **not** find this case, where the useful information is that one
entry's contact lives on another entry's domain and that other entry has nothing
recorded. When a major broker shows a blank contact, check whether a smaller
sibling in the registry has already published one on the same domain.


## Verification

As `dataaxle.md`. Ask the confirmation to say whether it covers the Exact Data
brand by name — a submission through the parent's form is not self-evidently
scoped to a subsidiary, and nobody will volunteer that it was not.

## Resolution: covered by the Data Axle submissions

Exact Data shares its privacy contact and its removal route with Data Axle, and
Data Axle's own privacy-rights form names `exactdata.com` within its scope. Both
required submissions were made there — deletion and opt-out of sale are
single-select on that form, so each right needs its own run — and both returned
*"Thank you. Your privacy request has been received."*

Recorded as `submitted` rather than left `pending` for a specific reason. The
family scan flags a group where one member has been written to and another has
not, because **a sibling your letter did not name is a sibling nobody removed**.
But the inverse failure is just as easy: a sibling that genuinely *was* covered
sits in the tracker looking exactly like one that was missed, and gets re-flagged
every pass until somebody decides. Deciding, and writing down why, is the point.

The decision is conditional. If Data Axle replies with a confirmation scoped to
one brand only, this reverts to pending and Exact Data needs a request of its own.

See `dataaxle.md` for the form's behaviour and the deemed-consent clause in their
privacy policy.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Consumerbase, LLC
- **Trading as:** Exact Data
- **Registered address:** 2451 W Grapevine Mills Cir. #538, Grapevine,
  Texas, 76051
- **Filed contact email:** privacy@exactdata.com
- **Filed phone:** (402) 836-3377
- **Website:** https://www.exactdata.com

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
