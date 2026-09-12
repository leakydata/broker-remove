# Seekout

- **Opt-out:** https://www.seekout.com/privacy/choices
- **Email:** privacy@seekout.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** seekout.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-09-12)
- Note: **Turned around after the LinkedIn URL was supplied as a suppression key.** The original letter (2026-08-31) already included the public LinkedIn profile URL, framed explicitly as a suppression key rather than a search hint (see CONTRIBUTING.md's B2B-letter guidance — this is the case it's for). SeekOut's human reply on 2026-09-11 confirmed: *"I can confirm that LinkedIn URL nathanejones has been deleted from our system."* So the email route was never actually blocked on withholding the URL — it needed the URL supplied on our own terms, up front, as one identifier among several, not surrendered on demand mid-thread. Two follow-up questions sent 2026-09-12 (deletion vs. standing suppression; whether any customer's saved/exported copy is reachable; whether the email addresses were also searched) are open.
- Prior note (2026-08-20, superseded): Autoresponder loop and empty portal — see Gotchas below, which still describes real historical friction even though the email route eventually worked.

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
