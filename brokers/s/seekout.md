# Seekout

- **Opt-out:** https://www.seekout.com/privacy/choices
- **Email:** privacy@seekout.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** seekout.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-20)
- Note: Autoresponder now loops: a third identical 'Automatic reply' arrived in response to my reply, so privacy@seekout.com is answering every inbound message with the same template rather than reading the thread (same pattern as _SILENT_FAILURES §56). Stop replying there. Both routes remain closed -- the portal renders no form, and the email route is refused without a LinkedIn URL. Next move is a re-test of the portal rather than another letter.

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
- **The email route is conditional**, and the condition is a LinkedIn URL. Refuse
  it: a live third-party profile is an enrichment key, not a verification token, and
  it stays useful to a talent-intelligence company after the request closes. See
  [[_DEFLECTIONS]] §38 — a second workforce dataset asked for exactly the same thing
  a day earlier.
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
