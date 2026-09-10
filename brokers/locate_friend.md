# Locate Friend

- **Opt-out:** https://www.locate-friend.com/optout
- **Email:** support@locate-friend.com — **unreachable, connect-level timeout on every published address**
- **Method:** web_form (broken) — no working email route
- **Domain:** locate-friend.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-09-09)
- Note: 2026-09-06 emailed support@locate-friend.com, framed as both a removal
  request and a bug report (see below). Got a Gmail "delivery incomplete" delay
  for 46 hours, then a terminal failure: the recipient server did not accept
  the connection on any of the four published A/AAAA records (all Cloudflare
  anycast IPs). This is not a full-mailbox or rejected-recipient bounce — it's
  a connection timeout on every address the domain resolves to, which reads as
  no mail service actually running behind this Cloudflare-proxied domain at
  all, regardless of what the contact page claims.

## Steps

Do not bother re-emailing; the domain does not appear to receive mail. If
someone with a browser wants to pursue this further, the web route is also
broken (see Gotchas) — there may be no working channel at all.

## Gotchas

- **The opt-out form is unreachable, not merely hard to use.** It requires a
  hidden `people_id` field that is only populated by clicking into a specific
  listing from search results. Submitting the form directly returns "The
  people id field is required."
- **Search doesn't index first names.** Searching a full name returns "No
  results were found." Searching the surname alone returns surname-level
  buckets (e.g. "[SURNAME] (64,448)") rather than individual records.
- **The only path to an individual listing is blocked by Cloudflare.** Paging
  into `/names/[X]/[XXX]/[SURNAME]` to find one record among 64,448 hits an
  interactive Cloudflare challenge, so there is no automatable or realistically
  human-scale way to reach the record the opt-out form needs a `people_id`
  from.
- **A Laravel debug page was hit by accident while testing the form** —
  `APP_DEBUG` appears to be enabled in production, and one malformed request
  returned a full stack trace (framework/PHP versions, ~31 vendor frames,
  request details) to an anonymous visitor. Reported to the company in the
  same letter as a courtesy, not investigated further and not disclosed
  elsewhere.
- **Net result: both the email and web channels are broken in ways that look
  unintentional** (a two-stage click-through flow linked as a standalone page;
  a domain that doesn't appear to run mail) rather than a deliberate refusal.
  There is currently no way to complete this removal without the company
  fixing its own site.

## Verification

No route exists yet to verify against. Re-test the opt-out form and the mail
channel on a future pass in case either gets fixed.
