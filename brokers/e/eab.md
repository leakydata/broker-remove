# Eab

- **Email:** privacy@eab.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** eab.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-25)
- Note: 2026-08-25: legal@eab.com redirects to a privacyportal form: 'In order to begin the verification process for your request, please complete and submit the data request form available here'. Staged as a self-contained handoff. Scope note written into the handoff: EAB owns Cappex and Appily, which are COLLEGE-RECRUITMENT products collecting data from prospective students - often minors - through scholarship searches and college-match quizzes. The asks that matter are the student profile itself, whether any of it was collected while the subject was under 18 and what retention applies, and WHICH INSTITUTIONS received the profile as a recruitment lead, since a student list sold to colleges is the product and the consumer has no other way to learn where it went.

## Steps

1. Email `privacy@eab.com`, naming **both EAB and Appily** — Appily publishes the
   same address.
2. Ask them to search the `.edu` address specifically.
3. Ask where any record was acquired from.
4. Ask whether the deletion covers derived and inferred data.

## Gotchas

Education-sector marketing data is usually **licensed rather than collected**,
which shapes the useful questions. A person has often never knowingly given their
details to the company holding them — the data came from a testing programme, a
student-search service, an institution's list, or a college-search product the
person used years earlier as a teenager.

That makes "where did this come from?" the highest-value question in the letter.
The answer names an upstream holder you did not know to write to.

**Search the university address explicitly.** A `.edu` address is a strong key in
this sector and is easy to overlook in a list of consumer addresses; it is also
frequently the *only* identifier under which an education-marketing record is
held.

Ask about **inferred data** as well: enrolment propensity scores, fit models,
predicted interests, segment membership. Those are generated about the person and
are personal information about them; deleting the source fields while keeping the
model output is not deletion.

Appily shares the contact address, so one letter covers both. Name them both
anyway — see `_BROKER_FAMILIES.md` on why the address will not do that for you.

## Verification

No public listing. Ask which properties held a record, whether the action is
suppression against re-listing or one-time deletion, and what the acquisition
source was.

## Their form cannot be completed from Pennsylvania — and picks a state for you

`Privacy@eab.com` replies with two OneTrust links, unlabelled. The first is branded
**Appily** and carries a required **State of Residence** dropdown.

**Pennsylvania is not in it.** The options are the states with comprehensive
consumer privacy statutes; the list runs Oregon straight to Rhode Island. There is
nothing a Pennsylvania resident can honestly select, so the form cannot be
submitted at all. That is the residency gate as a control rather than an argument —
no reply to push back on, no position to quote, just a dropdown that has no row for
you.

**The part that turns an obstacle into a hazard:** the field is a type-ahead, and
typing "Pennsylvania" **silently resolved to "Colorado"** and left it in the box. It
did not reject the entry. It did not say the state was unavailable.

Somebody filling this at normal speed types their state, sees the box accept
something, and submits — recording a Pennsylvania resident as a Colorado resident,
on a privacy request, under a notice saying the information is used to verify
identity, where residence decides which statute applies. Nobody intended it and
nobody would notice. Written up as `_SILENT_FAILURES.md` §20.

**Do not submit a false state**, even when the form leaves no alternative. These
forms carry certifications, and a false statement of residence turns a lawful
request into a defective one — and hands the company grounds to void it later.

## What to do instead

Go back to the email thread, report both faults, and ask them to process the
request as a matter of **company policy**, stating the basis in writing. Two things
make that ask harder to refuse:

- **Their own form carries a non-discrimination notice.** Declining a deletion
  request solely because of the state someone lives in sits oddly beside it, and
  quoting it back costs one sentence.
- **Concede the statutory point first.** Pennsylvania has no comprehensive privacy
  law and pretending otherwise invites a correction rather than an answer. Ask for
  policy, not law, and ask them to say which they applied — see `_DEFLECTIONS.md`
  §20 and §23 for why a documented refusal beats an unanswered request.

## The chain of brands

The policy linked from the Appily form is hosted at **cappex.com** — a third name.
EAB → Appily → Cappex, revealed by a link target rather than anything anyone
published deliberately. See `_BROKER_FAMILIES.md`, which now records where to look
for this, including the OneTrust tenant UUID in the form URL.

Ask which of the three held a record. A request processed against one brand's
database is not self-evidently processed against the others, and nobody will
volunteer that it was not.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** EAB Global, Inc.
- **Registered address:** 2445 M ST NW, Washington, DC, 20037
- **Filed contact email:** legal@eab.com
- **Filed phone:** 2027471000
- **Website:** www.eab.com

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
