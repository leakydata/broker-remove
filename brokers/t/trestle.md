# Trestle

- **Opt-out:** https://portal.trestleiq.com/do-not-sell
- **Email:** privacy@trestleiq.com (verified)
- **Method:** email — statutory request by email. No web form needed.
- **Domain:** trestleiq.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-20)
- Both rights confirmed separately, in writing, about four and a half hours after
  the request.

## Steps

1. **Use `privacy@trestleiq.com`.** A registry entry of `data@trestleiq.com`
   appears nowhere on their site; the published address is `privacy@`.
2. Send the request by email. No form, no account, no ID document.
3. Confirmations arrive from `noreply@trustsuperset.com` — a different domain
   from the one written to, which is worth expecting so it is not filtered as
   unrelated.

## Gotchas

**They confirm each right separately, and that is a feature.** Four messages
arrived at 13:37 UTC, two saying:

> "We are writing to confirm that your request to exercise your right to opt out
> has been completed."

and two saying:

> "We are writing to confirm that your request to exercise your right to
> deletion has been completed."

Most brokers collapse deletion and opt-out into one sentence, which leaves it
ambiguous whether the opt-out is a standing state or just a side effect of the
delete. Separate confirmations remove that ambiguity. Record both.

**Lead with numbers and addresses, not the name.** Their own product description
names phone verification, phone validation, CNAM lookup, reverse phone lookup
and reverse address lookup. In a reverse-lookup business the identifier is the
key and the name is the value, so a request framed around the name asks them to
search the wrong column.

**Three asks that are specific to this product shape**, all worth reusing for
phone-validation brokers:

- Remove the mapping in **both directions**. A record unreachable from one
  direction but intact from the other is harder to query, not removed.
- Search the **disconnected** numbers specifically. A disconnected number
  persists *more* readily in a validation dataset than a live one, because
  nothing generates fresh evidence to contradict the stale mapping.
- Confirm **CNAM / caller-name separately** rather than folding it into a general
  deletion. Caller-name data lives in different systems and fails independently.

**On their do-not-sell portal.** `portal.trestleiq.com/do-not-sell` exists; the
email asked them to treat the letter as also constituting that request, while
explaining why the reverse-direction and CNAM answers were wanted in writing
rather than through a form. They completed the opt-out without requiring the
portal, so the form is not mandatory.

## Verification

Both rights are confirmed in writing. Re-check on the standard cadence rather
than immediately. Their outbound domain is `trustsuperset.com`, so any future
correspondence will come from there rather than from trestleiq.com.
