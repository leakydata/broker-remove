# Teads

- **Opt-out:** https://privacy-policy.teads.com
- **Email:** dpo@teads.com (verified)
- **Method:** web_form — Web form.
- **Domain:** privacy-policy.teads.com
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-08-23)
- Note: Statutory opt-out/deletion email sent 2026-08-23, category-tailored.

## Steps

Email `ob-privacy@teads.com` (Outbrain's post-merger privacy address, covers both
Outbrain and Teads estates per their own routing).

## Gotchas

- **A genuine "we cannot search on that" answer, not a deflection.** Their reply
  (2026-09-03) states plainly they "do not process, retain, or associate data
  with traditional personal identifiers" and operate exclusively on cookie IDs
  and mobile advertising identifiers — so a name/email/address/phone request
  cannot be matched to anything in their systems. This is the honest ad-tech
  answer described in `_DEFLECTIONS.md`, not a stall.
- **They will ask for the cookie/MAID to proceed — decline it.** Supplying a
  device identifier to get a search done creates the exact device-to-name link
  the request exists to sever. The letter should say this up front (it did) and
  hold the line when they ask anyway.
- **Self-serve routes exist but are cookie-scoped, not identity-scoped**: Outbrain
  Interest Profile (find your own cookie ID) and Teads privacy policy §5. Neither
  helps a person trying to opt out by name/email rather than by browser session —
  flag for a human with a browser to check, but expect no name-based result.
- Worth asking once whether a hashed-email suppression list exists independent of
  cookie/device matching — some ad-tech platforms maintain one specifically so a
  consumer can opt out without surrendering a device ID. If the answer is no,
  that's a complete and final answer for this channel.

## Verification

No name-based verification is possible; this is a structural property of the
company, not something a recheck will resolve.
