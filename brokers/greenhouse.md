# Greenhouse Software

- **Email:** privacy@greenhouse.io (verified — replies)
- **Email (dead, receive-only):** ~~dsr@greenhouse.io~~ — sends completion
  notices FROM this address but a reply TO it hard-bounces: *"550 5.1.1 The
  email account that you tried to reach does not exist."* Never reply here.
- **Method:** email
- **Domain:** greenhouse.io — applicant-tracking system (ATS) used by
  employers; holds candidate records on behalf of the companies that use it.
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-09-15) — recorded on the strength of the
  repeated, consistent "completed" notices; still genuinely unclear whether
  anything was actually found (see below), so treat as "request honored,"
  not "record definitely existed."
- Note: original request 2026-08-27 (ticket 17235). Since then, Greenhouse
  has sent **three separate "Your deletion request has been completed"
  notices** (2026-09-11 14:53, 2026-09-11 16:10, 2026-09-12 10:15) plus
  several duplicate "we have received your request" acks under distinct
  ticket numbers (17235, 17870, 17888) — all from `dsr@greenhouse.io`, all
  boilerplate, none distinguishing "we found and deleted something" from
  "there was nothing there."
- **Reply-to-completion attempt bounced (2026-09-11):** sent two follow-up
  questions to `dsr@greenhouse.io` in reply to a completion notice; the reply
  hard-bounced ("550 5.1.1 the email account that you tried to reach does not
  exist"), confirming this address is send-only — see Gotchas. Questions
  remain unanswered and the channel to ask them (`privacy@greenhouse.io`)
  only auto-replies with the standing not-a-data-broker position.
- `privacy@greenhouse.io` separately auto-replied with Greenhouse's
  standing position: *"Greenhouse is not a data broker, does not sell or
  share personal data of job candidates or individuals with whom it does
  not have a direct relationship, and is not subject to data broker laws
  or registries,"* and *"we cannot delete or alter candidate profiles
  unless we do so at the explicit instruction of those customers, who are
  the data controllers... contact the company or companies you applied to
  directly."*
- We asked twice, unanswered as of 2026-09-12: (1) was there actually
  anything to delete, or is "completed" being sent regardless; (2) does
  any of this cover candidate/ATS records Greenhouse holds *for* its
  customers (where Greenhouse is a processor, not the controller), and is
  any suppression forward-looking against re-ingest.

## Steps

1. Email `privacy@greenhouse.io` — **never `dsr@greenhouse.io`**, which
   only sends and cannot receive.
2. Expect the not-a-data-broker / processor-not-controller position by
   default. It's a legitimate position as far as it goes (per SKILL.md's
   "pre-accept the unflattering answer" — Greenhouse genuinely may not be
   the controller for most of what it holds), but it doesn't answer
   whether Greenhouse's own systems (marketing lists, its own recruiting
   of candidates, sales prospecting) hold anything outside the
   customer-controlled ATS data.

## Gotchas

- **A "completed" notice that never says what was found is unfalsifiable.**
  Three of these arrived and none said whether a record existed. Don't
  record as `confirmed` on the strength of boilerplate language alone —
  see SKILL.md's "the unconfirmed request" pattern.
- **The reply channel is broken.** `dsr@greenhouse.io` sends notices but
  bounces replies — a dead-mailbox trap in the opposite direction from the
  usual one (this is the BROKER's outbound-only address, not the
  requester's). Worth naming explicitly in any letter to this company so
  they know their own notification system misroutes.
- **Repeated tickets for one request (17235 → 17870 → 17888) may indicate
  each follow-up reply spawned a fresh ticket** rather than threading —
  similar in shape to the Choreograph hourly-duplicate pattern, though
  unconfirmed here.

## Verification

No specific answer received as of 2026-09-12. Re-check after ~7 days; if
still only boilerplate, consider directing the request to the specific
employer(s) this candidate applied through instead, per Greenhouse's own
stated position.
