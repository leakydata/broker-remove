# LiveRamp

- **Opt-out:** https://liveramp.com/privacy/my-privacy-choices
- **Email:** consumercare@liveramp.com — verified (published on their own
  my-privacy-choices page). `ukprivacy@liveramp.com` auto-replies that it is
  scoped to GDPR/services requests only — wrong desk for a US consumer request.
- **Method:** web_form — Web form.
- **Domain:** liveramp.com
- **Priority: 5.**

## Status

- Current: `submitted` (updated 2026-08-21)
- Note: 2026-08-20: first contact to ukprivacy@liveramp.com, tailored per
  _CATEGORY_VARIANTS.md. 2026-08-21: ukprivacy auto-replied confirming it only
  covers GDPR services requests, not this. Fetched liveramp.com/privacy/my-
  privacy-choices directly and found `consumercare@liveramp.com` published as
  the US contact, plus a toll-free line (844) 678-0045 and per-request-type
  TrustArc web forms (opt-out, access, correction, deletion — all browser/
  CAPTCHA gated). Re-sent the full request to consumercare@liveramp.com.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Thirteen privacy addresses, none of them American

LiveRamp's privacy pages publish `privacy.ar@`, `privacy.be@`, `privacy.br@`,
`privacy.de@`, `privacy.es@`, `privacy.it@`, `privacy.nl@`, `privacy.no@`,
`privacy.pl@`, `privacy.ro@`, `privacy.se@`, `ukprivacy@` and `cil@` — and no
unqualified `privacy@` anywhere. See `_SILENT_FAILURES.md` §75.

Every one of those is a live, monitored mailbox. The defect is jurisdictional
scope, which no reachability check can detect: `dig` passes, delivery succeeds,
and the letter lands at a desk with no authority over a US resident's records.
From the requester's inbox that is indistinguishable from silence.

**Sent to `ukprivacy@` with the routing problem stated in the first paragraph.**
Naming it converts a misroute into a routing request, which is something a
regional desk can actually action — forward it and say where it went, or reply
with the right address. Guessing at `privacy@liveramp.com` was the alternative
and would have been a guess.

**Do not read the absence as evasion.** A company with eleven European privacy
contacts and no American one has built its privacy function around GDPR, where
naming a per-country contact is ordinary practice. The correct inference is about
org structure, not motive.

## What the letter asks for beyond the standard four

LiveRamp is an identity resolution business, so a deletion scoped to rows rather
than edges achieves nothing:

- hashed email forms (MD5/SHA-1/SHA-256) as match keys — with the distinction
  drawn between hashes held for **suppression** (supported, not asked to be
  deleted: a suppression list that forgets you cannot suppress you) and hashes
  held as **saleable match inventory** (asked to be deleted);
- RampID and every identifier mapped to it;
- MAIDs, cookie IDs, CTV IDs;
- **the edges** between those identifiers and name, address, email, phone — not
  merely the identifier rows. In an identity business the graph is the product;
- household association derived from IP;
- **do-not-onboard as a standing entry** — this is the specific mechanism by
  which a deletion here is undone by somebody else's action rather than
  LiveRamp's. A client uploading a file containing these details causes
  re-resolution and re-distribution. Deletion without do-not-onboard is a
  deletion with a refill valve attached.
