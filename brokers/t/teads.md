# Teads

- **Opt-out:** https://privacy-policy.teads.com
- **Email:** dpo@teads.com (verified)
- **Method:** web_form — Web form.
- **Domain:** privacy-policy.teads.com
- **Priority: 3.**

## Status

- Current: `unreachable` (updated 2026-09-08)
- Note: CLOSED 2026-09-08 ON A CLEAN NO, AND THE PROMISE TO CLOSE WAS KEPT. My 4 Sept follow-up asked ONE question and said in writing: 'One question, and then I will treat this as closed regardless of the answer... If the honest answer is that no such mechanism exists on your systems, that is a complete answer too.' They answered it on 8 Sept 10:59 UTC, plainly: 'No such mechanism does exist in our systems. Because we do not collect or process email addresses in any form, we do not maintain a suppression list keyed to them.' WHAT IS SETTLED: no email addresses processed in any form; no hashed-email suppression list; therefore no route by which the subject can be deleted or opted out WITHOUT supplying a cookie ID or MAID, which is a standing refusal. THE STATUS IS 'unreachable' IN THE SENSE THAT NO USABLE ROUTE EXISTS FOR THIS PERSON -- it is NOT a communication failure and should not be read as one. Outbrain/Teads replied twice, promptly, with the clearest architectural explanation in the ad-tech cohort, and named the reason rather than gesturing at policy. Contrast Foursquare (submitted, most complete technical answer) and Outlogic. Closing letter sent 2026-09-08 confirming the three settled points, thanking them for a falsifiable no, and suggesting -- explicitly as a no-reply-needed offer, not a request -- that the policy say in as many words that the opt-out requires an identifier the careful consumer will not have. See _SILENT_FAILURES 426.

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
