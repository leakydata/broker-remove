# Privateeye

- **Method:** unknown — Route not yet established.
- **Domain:** privateeye.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-19)
- Note: No route of any kind, and this one is worse than phonenumberinfo.us because it does not even pretend. Three independent dead ends: (1) privateeye.com publishes NO MX RECORD, so support@privateeye.com and any other address at the domain are undeliverable - did not spend a send. (2) Every URL path returns the homepage, a catch-all 200, so /privacy and /optout 'exist' and are the front page - the trap recorded as _SILENT_FAILURES 41. (3) All three footer legal links - Privacy Policy, Terms, Disclaimers - are href='#'. Not broken links pointing at a missing page; PLACEHOLDER ANCHORS that were never wired up. A live people-search site indexing names, phones and emails, with no privacy policy, no terms, no opt-out and no reachable contact. Nothing to write to and nothing to submit. Recorded unreachable; the only remaining routes would be the domain registrar or a regulator, neither of which is a removal.

## Steps

**There is nothing to do.** Recorded so nobody re-derives it.

1. `dig +short MX privateeye.com` returns **nothing** — the domain cannot receive
   mail, so `support@privateeye.com` and any other address at it are
   undeliverable.
2. Every URL path returns the homepage. `/privacy`, `/optout`, `/do-not-sell` all
   answer **200** with the front page (see `_SILENT_FAILURES.md` §41 — compare
   titles, not status codes).
3. The footer carries **Privacy Policy**, **Terms** and **Disclaimers**. All three
   are `href="#"`.

## Gotchas

**The legal links are placeholders, not broken links.** This is the part
worth being precise about. A broken link points at a page that has moved or been
deleted — a mistake. `href="#"` is an anchor that was **never wired to anything**:
the footer was built with the labels in place and the destinations left as
stubs.

So there is no privacy policy to read, no terms to check a disclaimer against, no
opt-out to use, and no address to write to — on a live people-search site indexing
names, telephone numbers and email addresses.

> **Three independent dead ends is a finding, not an accident.** One missing route
> is an oversight. No mail exchanger, a catch-all that makes every path look
> alive, and three placeholder legal links together describe a site built to be
> searched and not to be answered.

**Do not spend a send.** A domain with no MX is undeliverable by definition; the
DNS is conclusive without a bounce to prove it.

**What is left is not a removal route.** The registrar, the hosting provider, or a
state attorney general are the only remaining addresses, and none of them takes
opt-out requests. Recorded `unreachable` rather than `failed`, because nothing was
refused — there was nothing there to refuse.

**Watch for the reverse of this pattern.** A site with a polished privacy policy
and a broken opt-out is common. A site with *no* policy at all is rarer and worth
noting, because it means the usual levers — quoting their own commitments back at
them, holding them to a published process — do not exist here.

## Verification

Re-check the footer links and `dig MX` periodically. If any of the three ever
resolve to a real page, a route may have appeared.


