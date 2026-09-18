# Outlogic (formerly X-Mode Social)

- **Opt-out:** https://outlogic.io/opt-out-form/
- **Email:** privacy@outlogic.io — live, Zendesk-backed
- **Method:** email → Zendesk ticket
- **Domain:** outlogic.io (formerly xmodesocial.com)
- **Priority: 2.**

## Status

- Current: `replied` (updated 2026-09-06)
- Reference: `gmail:1a079085a20779fc`
- Note: ANSWERED IN 27 MINUTES, the fastest response in the project, ticket #194364. Their words: 'Outlogic and its products only work with advertising identifiers for mobile devices and not with personal identifiers such as names, email addresses, telephone numbers, etc. Therefore, in order to fulfill your request, you must submit the mobile advertising identifiers of your device(s) to us.' THIS IS THE EXIT THE LETTER OFFERED THEM, and the promise to accept it has to be kept -- a letter that offers an exit and refuses to honour it when the company walks through is not an argument, it is a trap, and every later letter is worth less for it. See SILENT_FAILURES 386. But their sentence is PRESENT-TENSE AND PRODUCT-SCOPED and the question was neither, so one short reply asks the two things it does not cover, undertaking to close on either answer: (1) HAVE YOU EVER -- has Outlogic, X-Mode Social, or any predecessor or affiliate whose data was inherited, at any time held a linkage between an advertising identifier and a name, email, phone or postal address, a present-tense answer about current products not covering a historical table; (2) DID IT ARRIVE PRE-LINKED -- was data ever received from a supplier or partner in which the advertising id was ALREADY joined to a personal identifier, whether or not the products then used it. WHAT IS DIFFERENT ABOUT THIS REFUSAL: they are not asking the subject to prove who he is, they are saying they cannot look him up without the key. That is a lookup problem, not a verification wall; 11 CCR 7026(f) does not reach it; and the letter says so rather than pretending otherwise. The MAID still will not be sent, with the reason given: handing a live advertising id to a location data company in order to ask it to hold less gives it something it did not have a minute earlier -- if the id is not in their systems it would be put there, and if it is, they now know it is current and belongs to a real person who reads his privacy mail. The request is unresolvable on their side, that follows from the subject's own choice, and the letter concedes it. ALSO PUT TO THEM, not about this request: they are on the CA register for every year from 2020, and if their answer is right the register lists a company structurally incapable of answering a consumer request -- a gap in the register rather than a failing of theirs, and they are better placed than a consumer to raise it with the administrators. They were invited to.

## Steps

1. **Do not write to `privacy@xmodesocial.com`.** It hard-bounces 550 5.2.1
   even though the domain still publishes live Google MX. The company renamed to
   Outlogic; the old domain answers at the SMTP layer and has no mailbox behind
   the published local part.
2. Write to `privacy@outlogic.io`. A Zendesk ticket opens and a substantive reply
   comes back within about twenty minutes — faster and more specific than most.

## Gotchas

**A §66 near-miss on their own privacy page.** The page carries an appeals
contact whose `mailto:` href is `appeals@outlogic.io` while the visible link
text reads `ppeals@outlogic.io` — a dropped leading character in the text, the
mirror image of the SourceIT case where the *href* was the broken one. Neither
copy can be trusted on its face; run `check_mailto.py` and prefer whichever
address the prose also states unlinked.

**The reply is the MAID wall, stated cleanly.** Their answer:

> "Outlogic and its products only work with advertising identifiers for mobile
> devices and not with personal identifiers such as names, email addresses,
> telephone numbers, etc. Therefore, in order to fulfill your request, you must
> submit the mobile advertising identifiers of your device(s) to us. Without the
> advertising identifiers, we will not be able to process your request."

The first half is probably true and should be accepted. The second half is the
structural impossibility — a consumer cannot look up their own advertising
identifiers historically. Both mobile platforms show only the current value, and
only while the setting is on; a reset mints a new identifier without retiring the
old. So the IDs attached to data they already hold are precisely the ones that
can no longer be seen. A request that can only be made by supplying MAIDs is one
a consumer is structurally unable to make. See `_CATEGORY_VARIANTS.md`,
"MAID-only brokers: decide once, and reset afterwards".

**Their opt-out form has the same defect.** It also asks for the advertising
identifier, so it is not an alternative route — worth saying so in the reply, for
the record, without making it the argument.

**What was sent back: a geographic query.** The substitute ask, which requires
nothing the consumer cannot obtain and which a location database can answer as
easily as a MAID lookup — search for any device showing a **persistent overnight
dwell pattern** at the current residence and each prior one, delete what matches,
and suppress so it is not re-onboarded from a supply partner. Plus the legal
point that makes it a rights request rather than a favour: a device that appears
at the same dwelling every night for months is not anonymous, the address is the
identifier, and under CCPA as amended information reasonably capable of being
associated with a particular consumer *or household* is personal information.

Three follow-ons asked alongside it, all worth reusing for location brokers:

- treat device-to-home-address inference as **identifying**, not as derived
  analytics — that step is what converts the dataset into personal information
- name whether they hold data touching **sensitive location categories** for
  those coordinates: places of worship, medical and reproductive health
  facilities, addiction and mental health treatment, domestic violence shelters,
  union halls, immigration services offices. Ask specifically; the general phrase
  does not reach these.
- identify **supply partners** upstream and **downstream buyers**, since a
  deletion that leaves copies with a buyer is a deletion in name only

**Never send a MAID to establish that one is not held.** Supplying a current
advertising ID to a company that says it holds only advertising IDs hands them a
live identifier and a home email address to associate it with, in exchange for a
search of the one ID least likely to be in a historical file.

## Verification

Ticket `#187713` is the thread. Watch for a response to the geographic query
specifically — a reply that repeats the MAID requirement without addressing the
dwell-pattern search has not answered it, and should be pushed on once.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Outlogic, LLC
- **Registered address:** P.O. Box 17247, Arlington, VA, 22216
- **Filed contact email:** privacy@outlogic.io
- **Filed phone:** (866) 346-9602
- **Website:** outlogic.io

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
