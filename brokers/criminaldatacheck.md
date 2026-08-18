# Criminaldatacheck

- **Opt-out:** https://www.intelius.com/privacy-center
- **Email:** priorityoptout@intelius.com, naming CriminalDataCheck.com specifically (verified — broker_reply, same shared address used successfully for addresses_com and zabasearch)
- **Method:** web_form — Web form.
- **Domain:** criminaldatacheck.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: FAMILY CONSOLIDATION, no cap spend. CriminalDataCheck.com publishes priorityoptout@intelius.com - the PeopleConnect family mailbox already serving Intelius, ZabaSearch, EasyBackgroundChecks and Addresses.com. Named it on the open PeopleConnect thread rather than sending a fresh letter, and used it as a concrete test of their unverifiable scope claim ('sites within our corporate family that we control'): CriminalDataCheck was found by following a published contact back to them, not by being named. Also re-raised the three still-unanswered points - name the sites, the name-search-only limitation, and deletion versus suppression.

## Steps

1. Do **not** email `support@criminaldatacheck.com` — it hard-bounces ("address
   couldn't be found") and is the only address the site itself publishes.
2. This site's own `optout_url` already names `intelius.com/privacy-center` —
   that is the tell that it is an Intelius/PeopleConnect affiliate front rather
   than an independent data holder.
3. File instead against `priorityoptout@intelius.com`, naming
   "CriminalDataCheck.com" explicitly in the subject and body, the same
   pattern used for `addresses_com` and `zabasearch` (both share this
   recipient and are separate PeopleConnect-family properties).
4. `dig` the domain if you want to confirm: MX and A both answer. Live domain,
   dead mailbox — the front is up, the funnel is just server-side.

## Gotchas

The bounce is the visible problem; the more useful finding is underneath it.

This is the **affiliate front** pattern, the same shape as Criminal.com. The site
presents itself as a background-check service, but a search does not query a
database it owns — it funnels the visitor to a background-check provider that
does. A deletion request aimed here is aimed at a shopfront.

That has a practical consequence worth stating plainly: **a bounce from a front
site is nearly harmless, and a "we hold nothing" from one is nearly useless.**
Neither tells you anything about the records that actually exist. What matters is
which provider the funnel terminates at, and whether a request has been filed
there. Follow the opt-out link, or the destination of a search, and file against
the name you land on.

Here the searches reach the Intelius/PeopleConnect privacy center, which is
covered separately — see `peopleconnect.md`.

So: no usable route, and also nothing much lost. Record the dead address because
a published contact that discards consumer mail is worth documenting, then spend
the effort on the provider behind it.

## Verification

Nothing to verify at this domain. Verification belongs to the provider the site
funnels into: re-run a search there, on their timetable, not this one's.
