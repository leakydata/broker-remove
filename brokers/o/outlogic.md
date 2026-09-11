# Outlogic (formerly X-Mode Social)

- **Opt-out:** https://outlogic.io/opt-out-form/
- **Email:** privacy@outlogic.io — live, Zendesk-backed
- **Method:** email → Zendesk ticket
- **Domain:** outlogic.io (formerly xmodesocial.com)
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-25)
- Reference: Zendesk ticket `#187713`

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
