# PeopleFinders

- **Opt-out:** https://www.peoplefinders.com/opt-out  (Cloudflare-gated)
- **Email:** customercare@peoplefinders.com  ·  affiliate: privacy@peoplefindersdaas.com
- **Phone:** (800) 718-8997
- **`privacy@peoplefinders.com` does not exist — it hard-bounces with 550.**

## Gotchas
- The opt-out page sits behind a Cloudflare "security challenge" that fires on
  **page load**, not at submit. Automation cannot get to the form at all; a human
  has to open the page first.
- Their policy states opt-outs are **not accepted by mail or email** — the form is
  the sanctioned route. Email *is* accepted to document that the form failed, which
  is the correct framing when the challenge blocks access.
- Registered as a California data broker (reg. 186872), so CCPA deletion/opt-out
  obligations apply regardless of the form being unreachable.
- Affiliate **PeoplefindersDaaS** is a separate registration (191581) and is worth
  naming explicitly in the request.

## Lesson
Do not guess `privacy@<domain>`. Check the broker's privacy policy or their state
data-broker registration for the published contact, and watch for a bounce —
a silently failed request looks identical to a pending one in the tracker.
