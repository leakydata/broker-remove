# Focus Usa

- **Opt-out:** https://www.focus-usa.com/optout-form/
- **Email:** privacy@focus-usa.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** focus-usa.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: List-compilation/rental. Permanent suppression rather than deletion, list renters who received the data, acquisition source. Added a SENSITIVE-CATEGORY ask: whether they hold or model health interest, financial distress, ethnicity, religion or political affiliation selects, and asked for those to be deleted rather than merely suppressed from mailing. Invited a written negative as an acceptable close.

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

