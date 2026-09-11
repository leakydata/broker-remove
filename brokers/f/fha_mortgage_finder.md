# Fha Mortgage Finder

- **Email:** unusubscribcfmf@seememail.net — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** seememail.net
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Statutory delete + opt-out + suppression letter sent to the published contact, covering every prior address, prior telephone number and alternate email address rather than only the current ones.

## The only published contact is an unsubscribe alias, on somebody else's domain

There is no privacy page, no opt-out URL and no privacy mailbox. The single
contact carried for this broker is `unusubscribcfmf@seememail.net`, and three
things about that address are worth stating plainly, because each one is a
different way for a request to disappear:

1. **The local part is misspelled** -- "unusubscribc", not "unsubscribe". That is
   almost certainly how the broker itself published it, transcribed faithfully by
   the directory we imported from. A typo'd alias may still be provisioned, since
   whoever created it made the same typo in both places, but it may equally be a
   transcription error two hops upstream, in which case every letter to it bounces.
2. **The domain is not the broker's.** `seememail.net` is a mail-sending domain,
   not `fhamortgagefinder`-anything. The suffix `cfmf` looks like a per-brand tag,
   which suggests one operator running many mortgage-lead brands through one
   sending platform. So the address probably reaches a service provider, not the
   company holding the record.
3. **It is an unsubscribe alias, not a rights mailbox.** Those are different
   systems with different outcomes. An unsubscribe suppresses *mailings*; it
   frequently does so by *keeping* your address on a suppression list, which is
   the opposite of deletion. Sending a deletion request there and receiving
   silence is easy to misread as compliance.

**So the letter says so explicitly.** It names the ambiguity rather than hoping:

> *"I am writing to this address because it is the only contact published for FHA
> Mortgage Finder. If it is an unsubscribe alias rather than a privacy mailbox,
> please treat this as a rights request and forward it to whoever handles those,
> or tell me where to send it. Please do not treat it as a mere mailing
> preference."*

That paragraph costs two sentences and converts three different silent failures
into a question somebody has to answer.

## What the outcomes mean here

- **A bounce** settles it: the address is wrong, and the broker publishes no
  working contact at all. That is a finding, not a dead end -- it is grounds to
  look for the operator behind `seememail.net` rather than the brand.
- **Silence** is the ambiguous case and must not be read as success. An
  unsubscribe robot that ingests and discards is indistinguishable from a mailbox
  nobody reads.
- **An unsubscribe confirmation** is a *deflection*, not a completion. See
  `_DEFLECTIONS.md` on suppression being recorded as an attribute of a retained
  record.

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
