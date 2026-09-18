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

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `[named individual]@seememail.net`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## If they ignore you

Work down this list. Each rung costs them more than the one above it.

1. **Reply in the existing thread** after the statutory deadline. California
   allows 45 days for a deletion request (Cal. Civ. Code 1798.130), extendable
   once by a further 45 with notice. Quote the date you first wrote.
2. **Write to the legal entity at the registered address above**, by post, if
   email has failed. A letter to the address of record is harder to lose than a
   support ticket, and it establishes a paper trail.
3. **Complain to the California Attorney General**, who administers the data
   broker registry: <https://oag.ca.gov/contact/consumer-complaint-against-business-or-company>.
   A broker's registration is what obliges it to answer; a complaint referencing
   the registry entry is the pressure point.
4. **Complain to the FTC**: <https://reportfraud.ftc.gov>. Useful for a pattern
   of non-response rather than a single case.
5. **Your own state Attorney General.** Many states with no comprehensive
   privacy statute still have consumer-protection powers and will take a
   complaint about a business that ignores its own published policy.

**What not to bother with:** phoning a support line to argue. The person who
answers cannot change the policy and did not write it. The registry entry, the
statutory deadline and the regulator are what actually move a company.
