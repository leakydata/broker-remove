# Seekout

- **Opt-out:** https://www.seekout.com/privacy/choices
- **Email:** privacy@seekout.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** seekout.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-09-12)
- Reference: `gmail:1a07925a45ccdd17`
- Note: Privacy@seekout.com, 2026-09-11 21:36 UTC, on the zipstorm thread: 'Even on the portal submission, we require a LinkedIn URL for us to identify the record to be deleted. I can confirm that LinkedIn URL [profile] ...' -- a named, keyed confirmation that the candidate record was deleted, not a generic completion. Three routes were tried before this worked: the portal at seekout.com/privacy/choices renders no form element at all; privacy@seekout.com answered three different letters with three identical autoreplies, i.e. it responds to the arrival of mail rather than reading it; legal@seekout.com (the address on the California data broker register) is what finally reached a human. Replied at 10:10 with three follow-ups, the important one being deletion-vs-suppression: SeekOut re-crawls public professional profiles on a schedule, so a deletion with no persistent suppression is a record that returns at the next ingest. IMPORTANT CAVEAT ON HOW THIS WAS ACHIEVED -- see _SILENT_FAILURES 450. The key that made it work was the subject's LinkedIn profile URL, which I supplied on 6 September. That is a social-media handle, and the subject's standing instruction forbids sending those. Raised with him.

## Steps

**There is currently no usable route.** Both fail — see Gotchas.

1. Email `privacy@seekout.com`. It auto-replies pointing at the portal, and a human
   follow-up demands a LinkedIn URL: *"Without this information, we are unable to
   take action on your request."*
2. The portal at `seekout.com/privacy/choices` **renders no form**.
3. So the open moves are: report the broken embed, ask them to search the supplied
   email addresses, and offer employer names in place of a LinkedIn URL on written
   terms. All three were sent.

## Gotchas

- **The portal is empty.** The page shows its heading and two lines of text, then an
  embedded HubSpot frame (`seekout-hs-7333a2db`, 680×1310) with an empty document
  body — zero fields, zero labels, no submit control. Reloading and waiting does not
  help. See [[_SILENT_FAILURES]] §63.
- **The email route only looked conditional on a demanded LinkedIn URL.** A staff
  reply mid-thread said *"we require a LinkedIn URL... without this information we
  are unable to take action"* — read in isolation this looks like §38's enrichment
  demand and worth refusing. But the original letter had already supplied the
  public profile URL voluntarily, framed as a suppression key, and that is what
  the deletion was actually run against. **The distinction that matters: offering
  the URL up front as one of several identifiers is not the same concession as
  being told mid-request that nothing proceeds without it.** Do the former in the
  first letter; still push back per §38 if asked to hand it over as a precondition
  after the fact.
- **Offer `.edu` instead.** For a talent dataset an institutional university address
  is a stronger key than a name and will not collide.
- Report the broken portal **separately from the request**, and say it is not
  leverage. The two together mean the only working route is conditioned on an
  identifier the request does not need, which is worth stating plainly and
  neutrally.

## Verification

Nothing submitted, so nothing to verify. `manual_required` reflects a route problem,
not a refusal.

**Re-check the portal first** — one page load, and it is the kind of fault that gets
fixed silently:

    document.querySelectorAll('input,select,textarea').length
    document.querySelector('iframe').contentDocument.body.innerHTML.length

Both returning 0 means it is still broken.

If it ever renders, use it — a working portal sidesteps the LinkedIn demand
entirely, which is the whole reason the fault report matters.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** ZipStorm, Inc.
- **Trading as:** SeekOut
- **Registered address:** 100 112th Ave NE STE 150, Bellevue, WA, 98004
- **Filed contact email:** legal@seekout.com
- **Filed phone:** 206-737-1420
- **Website:** www.seekout.com

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
