# Andrews Wharton

- **Opt-out:** https://www.andrewswharton.com/your-privacy-choices
- **Email:** privacy@andrewswharton.com (verified)
- **Method:** web_form — Web form.
- **Domain:** andrewswharton.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-08-19) — upgraded from `failed`; the acquirer searched and suppressed prospectively (Stirista ticket #139443)
- Note: Acquired by Stirista; their auto-reply redirects all DSARs to stirista.com and says it will honor only Andrews Wharton requests received before January 1, 2025. Re-filed at Stirista.

## Steps

1. Email `privacy@andrewswharton.com`. An auto-reply answers immediately.
2. Read it for the redirect: all data-subject requests now go to Stirista, which
   acquired them.
3. **Re-file at Stirista.** The request does not carry over; see below.
4. Mark this record `failed` — not because the company ignored it, but because
   this route no longer reaches anyone — and track the outcome under `stirista`.

## Gotchas

Acquired by **Stirista**. Their auto-reply redirects every DSAR to stirista.com,
and adds a condition worth reading twice: they will honour Andrews Wharton
requests only if received **before January 1, 2025**.

That cut-off is the interesting part. A request sent to the acquired brand after
that date is not queued, not forwarded and not refused — it is simply outside
what the auto-reply says it will act on, while still producing a friendly
acknowledgement. Everything about the exchange looks like a filed request.

**The general rule:** an acquisition does not merge the two companies' privacy
queues, and the acquirer's obligations under an acquired brand are whatever the
acquirer decides to publish. Treat a redirect as an instruction to start over at
the new name, and never let the redirect email itself stand in as the receipt.
The data survived the acquisition; the request did not.

Related patterns in `_BROKER_FAMILIES.md` — cross-domain privacy addresses are
the usual way a rebrand or acquisition gives itself away before anyone announces
it.

## Verification

Verify at **Stirista**, not here. This domain has no queue of its own left to
check, and a confirmation from Andrews Wharton — if one ever arrives — would be
about a request the acquirer has already said it will not action.

## Resolved by the acquirer, without arguing the cutoff (updated 2026-08-19)

Previously recorded as `failed`. The reason was a date:

> Stirista, as acquirer, auto-replied that it would honor Andrews Wharton
> requests **only if received before 1 January 2025**.

That is an unusually hard deflection to attack. It is not a claim about the law,
it is a claim about what the acquirer took on — and a consumer has no way to
contradict it.

The way through was not to contradict it.

> **Against an acquirer's cutoff date, stop arguing the date and ask for the
> search.** The letter to the parent simply named both brands and asked for one
> query across the identifiers. Running a query costs them nothing and concedes
> no policy, which is precisely why they will do it.

Stirista ticket **#139443** came back:

> "Your information was not found in our system, and it has been added to our
> CCPA Opt-outs to keep your information out of our system in the future."

That covers both brands, and it is better than winning the argument would have
been: a standing prospective suppression rather than a grudging one-off.

Upgraded `failed` → `not_found`. See [[stirista]] for the four-brand family and
[[_DEFLECTIONS]].
