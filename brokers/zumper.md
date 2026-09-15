# Zumper

- **Email:** privacy@zumper.com (discovered 2026-09-12 — not yet verified by a reply)
- **Method:** email
- **Domain:** zumper.com — rental-listing marketplace.
- **Priority: 1.**

## Status

- Current: `submitted` (2026-09-15) — opt-out-of-sale confirmed; deletion
  stuck behind an unclicked email-verification link (see handoff).
- **Two separate reply channels, two different outcomes (2026-09-14):**
  - `privacy@zumper.zendesk.com` (ticket 1263030 — reply to the letter sent
    to `privacy@zumper.com`): an apology for a delayed response, then *"For
    your convenience, we have submitted the request on your behalf, and it
    has been processed."* Vague about which request.
  - `privacy@tr.zumper.com` (a TrustArc/OneTrust-style privacy portal, not
    the Zendesk queue): sent **two separate emails** the same minute — one
    headed "Confirm your Zumper Privacy Request" for the **delete** request,
    requiring a click on a confirmation link before any deletion proceeds
    (*"we are required by law to verify your identity... Please confirm
    your request here [link]"*), and a second stating the **opt-out-of-sale**
    request was *"successfully completed"* with no confirmation step needed.
  - So: opt-out of sale is done. Deletion is not — it is gated behind a
    one-time confirmation link, queued to handoff (see below) since this
    project does not click browser links autonomously.

## Steps

1. Email `privacy@zumper.com`. Do not use the press-contact address if
   found first — it is not the same channel.
2. Expect **two independent reply systems** — a Zendesk support queue and a
   separate `tr.zumper.com` privacy portal — answering the same letter on
   different tracks. Don't assume one system's reply covers the other's.
3. The deletion side requires clicking a confirmation link sent to the
   requester's email; queue that for a human rather than treating the
   Zendesk "processed" reply as covering it.

## Gotchas

- **The Zendesk "we have submitted the request on your behalf, and it has
  been processed" reply is not evidence the deletion happened.** It arrived
  from a different system than the one that actually gates deletion behind
  a confirmation click, and does not mention that click requirement at all.
  Treat it as an acknowledgement, not a completion.
- Confirmation links from `clicks.zumper.com` are one-time-use and likely
  time-limited (not stated how long) — see handoff.py entry.

## Verification

Opt-out-of-sale: confirmed by broker reply 2026-09-14, no further action.
Deletion: pending the confirmation-link click — re-check after it's clicked,
or after ~7 days if it lapses unclicked (in which case treat as the same
"final verification attempt" trap seen at WINR Data / CB Insights and resend
by direct email instead of relying on the portal a second time).
