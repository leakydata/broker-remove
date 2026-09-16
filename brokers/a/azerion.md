# Azerion US Inc.

- **Email:** dpo_hybridtheory@azerion.com (original), replies came from **dpo@azerion.com** — use that one going forward
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** azerion.com
- **Priority: 2.**

## Status

- Current: `replied` (updated 2026-09-11)
- Note: DETAILED AND UNUSUALLY HONEST REPLY 2026-09-11 from dpo@azerion.com, covering AZERION AND HYBRID THEORY TOGETHER. THE SENTENCE WORTH QUOTING AT EVERY OTHER AD-TECH COMPANY: 'we do not receive any real-world identifiers (what we refer to as Contact Data or Identity Data), such as name, contact details or address. FURTHERMORE, WE ALSO DO NOT STORE THE HASHED VALUES OF EMAIL ADDRESSES.' That second clause is the one almost nobody answers -- the usual formulation denies holding 'email addresses', which is comfortably true while holding many in hashed form (SF 430, and the reason the Criteo counter-example matters). Azerion closed it in a sentence, unprompted. THEY ALSO EXTENDED THE ANSWER TO A SEPARATE REQUEST WITHOUT BEING ASKED: 'As you correctly pointed out Hybrid Theory was acquired by Azerion. Therefore, the below explanation also applies for your request sent to privacy@hybridtheory.com on August 28, 2026.' So one answer closes two rows, and the consumer would not otherwise have known. THEIR PROCESS: opt-out at hybridtheory.com/opt-out stops processing within 7 days and needs nothing disclosed; DELETION requires the browser's cookie ID, which that same page displays ('You are currently Opted-In with cookie ID ...'), and they 'also recommend sharing your mobile advertising ID (Apple IDFA or GAID)' for a full search. They engaged with the browser-opt-out objection rather than repeating the link: 'us referencing you to our opt-out page is not only for an opt-out but also to enable you to find your cookie identifier in a convenient way.' DECLINED BOTH IDENTIFIERS, with the reasoning stated plainly: the MAID is an absolute standing refusal; the COOKIE ID is refused on the narrower ground that Azerion already holds that cookie and setting it is not the issue -- emailing it from a named address would create, permanently and in a ticket, the link between a named person and a profile they say is currently anonymous. Bad trade in both branches: if deletion succeeds they keep a record that a named person was that cookie; if it fails they keep that AND the profile. Same analysis as the Madhive IP question (SF 144/150). ASKED THE ONE QUESTION THAT WOULD CLOSE IT: can they record a do-not-add/do-not-onboard suppression against the PERSON, with no cookie or device identifier, so a future partner feed or acquisition creates nothing -- the one thing a cookie-scoped opt-out cannot do, since it dies when storage is cleared. An explicit no offered as a complete answer. Also asked, only if easy, which publisher or app CATEGORIES the data originates from. QUEUED: the browser opt-out, which is the safe half and discloses nothing.

## Steps

1. Email `dpo@azerion.com` (not the original `dpo_hybridtheory@azerion.com` —
   that address is what we sent to, but their own replies come from `dpo@`).
   Ask for hashed-email search, cookie/device/CTV IDs, audience segments
   (including sensitive-category inferences), and publisher/app-partner
   sources.
2. Expect them to say plaintext identifiers (name, email) aren't something
   they collect at all — this is a cookie/device-keyed adtech platform, not
   a name-keyed compiler. Don't be surprised if a `--keys email-only`-style
   letter would have been more appropriate from the start (see
   CONTRIBUTING.md's identifier-keyed guidance).
3. If asked for a cookie ID or mobile ad ID to "complete" a deletion,
   **decline** — see Gotchas.

## Gotchas

- **"We need your cookie ID to delete your data" is a real trap for a
  cookie-keyed adtech platform.** Supplying it hands them exactly the kind
  of fresh, verified identifier link the request exists to prevent. The
  honest alternative to ask for is a **do-not-add / do-not-onboard rule**
  applied without ever collecting the identifier — whether that's actually
  possible is the open question on this thread.
- **The browser opt-out and the deletion request are different tools.** The
  opt-out page stops future targeting tied to a browser; it says nothing
  about records already built from past cookie/device activity or from a
  publisher-partner's data feed. Getting both requires asking separately —
  don't let the opt-out link substitute for an answer to the deletion
  request.

## Verification

Browser opt-out said to take effect within 7 days — no independent way to
verify from outside. Re-check the two open questions above if they answer.
