# MyPropertyRecs

- **Opt-out:** https://dashboard.mypropertyrecs.com/opt-out/
- **Method:** web_form — bot-blocked to automated fetch, needs a human
- **Email fallback:** none published/found
- **Priority: 2.**

## Status

- Current: `manual_required` (registered 2026-09-13)
- Note: Not found by the original fingerprint/family scan that grouped
  courtrec.com, publicrecords.info, publicrecords.us, propertyrecord.com and
  propertyrecs.com under one LiveChat license (see `courtrec_com.md`). Surfaced
  instead by the courtrec.com/publicrecords.info support desk itself, which
  named it in the same helpdesk.com ticket (1746136851, 2026-09-13) that
  confirmed removal at those two sites — one of the reply messages was nothing
  but this URL. Never contacted directly; queued for handoff rather than
  emailed because no contact address is published and the opt-out URL is the
  only route offered.

## Steps

1. Open https://dashboard.mypropertyrecs.com/opt-out/ in a real browser — it
   returns HTTP 403 to an automated fetch (Cloudflare or similar), so this
   step cannot be done headlessly.
2. **Before filling anything in, check whether the "dashboard." subdomain
   requires creating an account or logging in.** If it does, stop — this
   project's hard rule is never to create an account with a broker — and
   instead look for an account-free contact route (email, a plain contact
   form) on the marketing side of mypropertyrecs.com, or ask the courtrec.com
   support desk (already an open, responsive channel) to action the removal
   on this sibling directly instead.
3. If it's a plain form, submit [FIRST LAST]'s name, DOB and address as given
   in `scripts/make_optout_email.py`'s identity block. Do not add anything
   the form doesn't ask for.

## Gotchas

- The site is part of a public-records/property-records family that has
  already been fully cooperative through one support channel (courtrec.com's
  helpdesk.com desk) — worth trying that channel again for this sibling
  before fighting the bot-blocked form, since it may be faster than solving
  the account-or-not question in Step 2.

## Verification

No public search page confirmed yet. Re-check via the courtrec.com support
thread (helpdesk.com ticket 1746136851) if the form route stalls.
