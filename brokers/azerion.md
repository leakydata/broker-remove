# Azerion US Inc.

- **Email:** dpo_hybridtheory@azerion.com (original), replies came from **dpo@azerion.com** — use that one going forward
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** azerion.com
- **Priority: 2.**

## Status

- Current: `replied` (updated 2026-09-11)
- **Reply (2026-09-11):** one of the more careful, substantive replies this project has received. *"Generally, where we collect information through cookies, we do not receive any real-world identifiers... we also do not store the hashed values of email addresses... As we do not collect names and email addresses, we do not send any sort of marketing or promotional materials."* To actually apply a deletion tied to their advertising profile, they asked for a **cookie ID or mobile advertising ID (IDFA/GAID)**. They also offered a self-serve browser opt-out page that they said takes effect within 7 days.
- **Our reply (2026-09-11):** declined to supply a cookie ID, IDFA or GAID — handing over a device/cookie identifier would create exactly the identity link the request is trying to prevent, and doing so purely to prove a negative isn't proportionate. Agreed to use the browser opt-out for what it covers. Asked two open questions: (1) whether a person-keyed do-not-add / do-not-onboard suppression is possible without ever supplying a cookie ID, and (2) which publisher/app categories their data about him typically originates from. Unanswered as of 2026-09-11.

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
