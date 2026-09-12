# TruthFinder

- **Opt-out:** https://suppression.peopleconnect.us
- **Email:** privacy@truthfinder.com (verified)
- **Method:** web_form — Web form, email also accepted.
- **Domain:** truthfinder.com
- **Priority: 5.**

## Status

- Current: `confirmed` (updated 2026-09-11)
- Reference: `gmail:1a00618203742083`
- Note: RE-VERIFICATION 2026-09-11 RAISED A QUESTION IT COULD NOT ANSWER -- status deliberately UNCHANGED pending a human check, not downgraded on a keyword. The read-only public search returned LISTED: an entry reading '[PERSONAL] Bradford, ME 47 Years Old Locations Include: Bradford, ME Shermans Dale, PA [PERSONAL], PA Lehi, U...'. [PERSONAL] IS THE SUBJECT'S CITY, which is what tripped the locality test; BRADFORD MAINE IS NOT, and prior analysis of the same-named cluster on Radaris identified a Bradford ME [PERSONAL] aged 47 and a Shermans Dale PA [PERSONAL] (deceased) as NOT the subject. Age does not separate them -- the subject is also 47. So this is genuinely undecided from outside, and SF 409 is the standing warning against resolving it either way from a name and a town. A direct re-read is not possible: truthfinder.com now returns a Cloudflare 'Just a moment' 403 to a scripted fetch, so the page the scanner saw cannot be re-opened without a browser. QUEUED with a decidable test -- the subject's address history is distinctive (sixteen addresses, nearly all in a narrow band of Pennsylvania), so several of Waynesboro/State College/Shippensburg/Philipsburg/Bellefonte/Blue Ridge Summit/Hagerstown MD/Mobile AL means it is him, while [PERSONAL]-plus-Shermans-Dale amid Maine, Utah and Indiana means it is not. THE REASON IT MATTERS BEYOND THIS ROW: the same run shows INSTANTCHECKMATE at NAME-ONLY -- the name page exists, the subject's city is absent -- and both brands are covered by ONE PeopleConnect suppression applied in a single action on 2026-08-27 across Intelius, InstantCheckmate, TruthFinder and USSearch. If the TruthFinder cluster is the subject, one suppression is holding on one brand and not on another. PeopleConnect's own model makes that mechanically plausible: 'background reports are compiled in real time via live calls to data providers... Because we don't retain reports, we cannot delete them.' A display suppression keyed to one identity cluster would not catch the same person's data arriving inside a different one. See _SILENT_FAILURES 439.

## Steps

1. Email `privacy@truthfinder.com` directly with the standard statutory deletion/
   opt-out request.
2. TruthFinder is a PeopleConnect property (same family as Intelius, Instant
   Checkmate, US Search) — if email stalls, PeopleConnect's own suppression
   portal (https://suppression.peopleconnect.us) is the fallback, though other
   playbooks in this family report it scopes suppression to **name search only**
   (see `peopleconnect.md`) — push for phone/address lookup suppression too if
   they try to narrow the request that way.

## Gotchas

- Same PeopleConnect family as Intelius/Instant Checkmate/US Search/ZabaSearch —
  check `intelius.md` and `peopleconnect.md` before treating a reply here as new
  information; the shared-infrastructure pattern (one contact address serving
  several branded sites) recurs across this family.

## Verification

Re-search truthfinder.com directly for the profile once a reply arrives. No
stated timeframe yet as of 2026-08-18.
