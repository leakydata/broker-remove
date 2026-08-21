# FastPeopleSearch

- **Opt-out:** https://www.fastpeoplesearch.com/removal
- **Email:** support@fastpeoplesearch.com (verified)
- **Method:** web_form_captcha — Web form with a CAPTCHA — see where it sits (page load vs submit).
- **Domain:** fastpeoplesearch.com
- **Priority: 5.**

## Status

- Current: `submitted` (updated 2026-08-21)
- Note: 2026-08-20: first contact to support@fastpeoplesearch.com. 2026-08-21:
  auto-reply deflection — "This email address is dedicated to customer service
  inquiries... We do not process privacy requests received via email" — pointing
  at `/removal` for opt-out and `/privacy-rights` for other requests. Both are
  CAPTCHA-gated web forms; this project has no browser, so this stays
  `submitted` rather than progressing further without a human. `/removal` and
  `/privacy-rights` are the two URLs a human session should complete.

## Steps

1. Do not expect a reply from `support@fastpeoplesearch.com` beyond the canned
   deflection above — it is automated and identical regardless of what the
   letter asks.
2. A human with a browser needs to complete `https://www.fastpeoplesearch.com/removal`
   (opt-out) and, if a broader request is wanted, `https://www.fastpeoplesearch.com/privacy-rights`.

## Gotchas

- **Email is refused outright, not just unmonitored.** The reply explicitly
  states they do not process privacy requests by email at all — this isn't a
  wrong-address problem, so there's no alternate mailbox to hunt for.
- CAPTCHA is present on the form per the registry's `web_form_captcha` method;
  not yet confirmed whether it gates page load or only submission.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
