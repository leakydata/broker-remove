# Appily

- **Email:** privacy@eab.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** eab.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-10-11)
- Note: EMAIL ROUTE FOUND IN THEIR OWN REGISTRATION, SO THE CAPTCHA WAS NEVER THE ONLY ROUTE. This row sat on the subject's manual CAPTCHA list. data/register_profiles.json -- already in this repo -- lists legal@eab.com as the filed contact for EAB, Appily AND Cappex, all three. ONE LETTER SENT 2026-10-11 to legal@eab.com covering all three brands, asking them to say if any is a separate controller so it can be written to separately rather than having EAB answer for a business that is not theirs. Said plainly why email rather than the form: the web route is CAPTCHA-gated and cannot be completed, and a CAPTCHA-only route excludes anyone using assistive technology -- framed as an observation, not a demand to remove it, since the filing already provides an alternative. TWO ASKS TAILORED TO THE BUSINESS. (1) STUDENT-RECRUITMENT PROVENANCE: Appily and Cappex are college-search products and EAB's enrollment work runs on student lists from test registrations, scholarship searches, college fairs and high-school lists. Asked which source any record came from, by name. Also asked whether any part of it was created WHILE HE WAS A MINOR -- anything originating before January 1997 was collected when he was under 18 -- framed as a question about their own policy categories rather than a legal claim. The psu.edu closed mailbox is the likeliest match key here by a wide margin, so the letter asks specifically whether the match came from it. (2) CONTROLLER VS PROCESSOR: much of EAB's work is for client institutions, so asked them to name the university if a record is held on its behalf. Also asked which of four plausibly distinct stores was searched -- Appily, Cappex, EAB enrollment services, and legacy Cappex systems retained from before the acquisition.

## Steps

Covered by the EAB request — same privacy contact, same OneTrust forms. See
**`eab.md`**, which carries the whole story.

The short version: **the form cannot be completed from Pennsylvania.** Its State of
Residence dropdown lists only states with comprehensive privacy statutes, and the
type-ahead silently substitutes a different state rather than refusing. Do not
submit it. Use the email thread and ask them to honour the request as company
policy.

## Gotchas

**The privacy policy linked from the Appily form is hosted at `cappex.com`.** That
is a third brand in the chain — EAB → Appily → Cappex — and it turned up not from a
shared privacy address or a ticket number but from a **link target inside a form**.

Worth adding to the detection list in `_BROKER_FAMILIES.md`: where a form's own
"our Privacy Policy can be found here" points at a different domain, that domain is
part of the same operation. It is the same class of evidence as a cross-domain
privacy address, and just as unintentional.

Asked them to say which of the three systems held a record, since a request
processed against one brand's database is not self-evidently processed against the
others.

## Verification

As `eab.md`. Ask which of EAB, Appily and Cappex held a record, and which
institutions received the data — student-search records are distributed to
colleges, and those copies outlive any deletion at the source.

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
