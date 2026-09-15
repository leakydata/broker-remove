# Ispot Tv

- **Email:** privacy@ispot.tv (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** ispot.tv
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-15)
- **Reply (2026-09-14):** *"We have completed our review of your data subject
  request using the information you provided. We did not identify any
  personal information associated with you in our systems. Accordingly, no
  further action was taken."* Took nearly a month (letter sent 2026-08-18);
  no breakdown of which identifiers or systems (device/household vs name)
  were searched, so this is recorded as a plain `not_found` rather than a
  verified-negative — see the device-graph caveat in Gotchas.
- Note: Acknowledged receipt of the DSR; response promised within the statutory timeframe.

## Steps

1. Email `privacy@ispot.tv` with the connected-TV/ACR variant — viewing history, channel/programme tuning data, automatic content recognition data, household device-graph entries, ad exposure/attribution events, and ask which TV manufacturer or platform supplied the data.
2. iSpot.tv is a TV-ad-measurement company (not a consumer-facing broker) — data is held against device/household identifiers, so a name-only search may truthfully return nothing while ACR data on a household device remains; the category-variant language is what avoids that trap.

## Gotchas

- Classic **ACR/device-graph** case per `_CATEGORY_VARIANTS.md` — a plain "delete my name" letter would likely get an honest "no record" that misses the real data. Keep the household/device framing in any follow-up.
- The 2026-09-14 nil doesn't say whether the ACR/device-graph side was
  actually searched separately from a name-only lookup — the same
  scoped-confirmation risk as IDnotify. Worth a one-line follow-up if this
  broker is revisited, asking specifically whether household/device data was
  searched or only name/email.

## Verification

No consumer-facing listing to check — written confirmation is the only
evidence, and the 2026-09-14 nil is it. Not pressed further this pass since
the value of a third round on an ACR search-scope technicality is low.
