# Sync Me

- **Opt-out:** https://sync.me/unsubscribe/
- **Email:** privacy@sync.me — verified against their own published page
- **Method:** web_form — Web form.
- **Domain:** sync.me
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-09-04)
- Note (2026-09-04): Full, specific answer to all three follow-up questions. (1) They won't send the listing URL for already-removed data, but offered a self-search as the alternative (not useful — that's the thing being avoided — but a reasonable limit to state). (2) **Confirmed a durable opt-out, not a one-time deletion**: "That opt-out entry is what persists after the deletion, and it's designed to survive future data refreshes," and listed the *complete* set of identifiers now on the opt-out (all 12 phone numbers, all 11 email addresses) — actual proof rather than a general assurance. (3) Confirmed the architecture: data comes from other users' uploaded contact books, "due to the anonymous nature of our platform, we're not able to disclose who shared your information" — a real and understandable limit, distinct from a refusal. Confirmed suppression covers every number sent, not only ones that matched an existing record.
- Note: Sent 2026-08-20 05:35 UTC to privacy@sync.me (published on their site). Tailored as reverse-phone/caller-ID: led with the eleven phone numbers rather than the name, and asked three things separately rather than accepting one 'removed'. The distinctive ask is contact-book uploads - Sync.me builds its directory from address books uploaded by other users, so a number and name can be present without the subject ever installing the app or agreeing to anything, filed under someone else's account. That is the part most likely to survive a deletion, and I asked them to say plainly if their architecture treats another user's uploaded contacts as that user's data rather than mine. Also asked about spam reports/tags/comments attached to a number, and for suppression rather than deletion, since a crowdsourced directory rebuilds on every new sync.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

- **Crowdsourced-directory architecture means "who uploaded this" is genuinely
  unanswerable** — Sync.me states this plainly rather than deflecting, and it's a
  real limit, not a stonewall. The useful ask here is the opt-out/suppression, not
  the source, since the source is anonymous by design.
- **They will list every identifier they've added to the opt-out if asked** — a
  good verification pattern to request from any broker claiming a suppression:
  make them enumerate what's actually on the list rather than asserting "handled."
- The opt-out is display/collection-only and explicitly does not block calls from
  those numbers — a caller-ID service's opt-out has a narrower scope than it might
  sound like; worth stating clearly to avoid a false expectation.
- Support runs through a Zendesk ticket (support@syncme.zendesk.com), not the
  original privacy@sync.me address once a thread is open.

## Verification

They provided the complete list of suppressed identifiers in writing 2026-09-04
— no further check needed unless a listing reappears under a number/email not
on that list.
