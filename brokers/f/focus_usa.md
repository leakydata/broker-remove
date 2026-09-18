# Focus Usa

- **Opt-out:** https://www.focus-usa.com/optout-form/
- **Email:** privacy@focus-usa.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** focus-usa.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: STRONG ARTIFACT. They confirmed 'a record was present on the database' - the conditional 'if present' resolved. And they committed in writing: 'Your full mailing addresses, email addresses and name(s) will be added to the delete/opt-out process and added to our permanent suppression list and suppressed in rebuilds, so if you choose not to continue with verification, those requests will be unaffected.' So deletion/opt-out/suppression are NOT gated on ID; only the access answers are. User uploaded a utility bill to their Dropbox file-request link. Asked them to delete the document and state retention, and pressed the three unblocked questions.

## Steps

1. Email `privacy@focus-usa.com`.
2. Ask for a **permanent suppression entry**, not deletion.
3. Ask which list renters received the data, and where it was acquired.
4. Ask explicitly about **sensitive-category selects** — see below.
5. Invite a written negative as an acceptable close.

## Gotchas

The standard list-broker asks apply — suppression rather than deletion, renters,
source; `dmdatabases_com.md` works those through.

**The addition worth making here is sensitive selects.** Consumer list businesses
routinely offer targeting by health interest, financial distress, ethnicity,
religion, political affiliation and similar — categories that are inferred and
sold without the person ever knowing they were assigned one.

Ask about them by name. Two reasons this is worth a separate paragraph rather than
trusting "delete all personal information" to cover it:

- **A select is a modelled attribute, not a field you gave them**, so a
  responder answering "what personal information do we hold" may not think of it
  at all.
- **Suppression from mailing does not remove a select.** The attribute can survive
  as a property of a record that is simply no longer mailed — and it is the
  attribute, not the mailing, that is sold on. Ask for deletion of the attribute
  specifically.

## Verification

No public listing. Ask which suppression list the entry was added to and whether
it is checked at every build, and ask separately for confirmation that any
sensitive-category attributes were deleted rather than suppressed.

## "If present" is not an answer

They replied within a day:

> *"Your optout request has been processed and if present you will be removed from
> our database within 24 hours."*

Fast, and worth noting for that. But read the conditional. **"If present"** leaves
it unknown whether they held a record and removed it, or held nothing and there was
nothing to remove — and those are different outcomes that a tracker has to record
differently.

This is a milder cousin of `_SILENT_FAILURES.md` §17: not a negative scoped to the
wrong noun, but a statement carefully constructed to assert nothing about whether a
record existed. It is probably not evasion — more likely the reply was sent before
the search ran — which is exactly why asking costs nothing.

**Also note the noun they chose.** The letter asked for deletion, permanent
suppression, disclosure of sensitive attributes, the acquisition source and the
list of renters. The reply calls it an **"optout request"**. Whatever was actually
done, the frame is narrower than the ask, and the ask most likely to fall outside
an opt-out is the sensitive-attribute one — a do-not-mail flag stops the mailings
while leaving the attribute on a record that stays licensable, and it is the
attribute rather than the mailing that gets sold.

Pressed on three points: was a record present, is this a permanent suppression
entry checked at every build or a removed row that returns at the next one, and do
any sensitive or modelled attributes exist and have they been deleted.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Focus USA, Inc.
- **Trading as:** Focus USA
- **Registered address:** PO Box 1782, Paramus, New Jersey, 07653
- **Filed contact email:** [named individual]@focus-usa.com
- **Filed phone:** 2014892525
- **Website:** focus-usa.com

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
