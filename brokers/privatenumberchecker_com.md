# Privatenumberchecker Com

- **Opt-out:** https://www.privatenumberchecker.com/removal-request/
- **Email:** support@privatenumberchecker.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** privatenumberchecker.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Reverse phone lookup. Standard number-keyed asks: every prior number, both directions, carrier/line-type/portability/location enrichment, related-person appearances on other numbers' pages, suppression-vs-one-time, and stored-index-vs-live-pass-through. Also asked which sibling properties share the index, given three other 'private*' people-search brands surfaced in the same batch.

## Steps

1. **Do not email.** `support@privatenumberchecker.com`
   hard-bounces "address not found" — even though the domain publishes its own
   mail exchanger (`mail.privatenumberchecker.com`). Healthy MX, absent mailbox.
2. Use **`/removalrequest/`**. Cloudflare challenges it; wait ~10 seconds and it
   clears itself.
3. Fields: first name, last name, phone, email, a free-text **Removal reason**,
   and a confirmation checkbox. **No CAPTCHA.**
4. Success page reads: *"Removal request success! Thank you! Your removal request
   has been sent!"*

## Gotchas

**The phone field rejects hyphens, and the failed validation disables the
submit button.** This is the trap, and it is worth spelling out because it looks
like the site is broken rather than picky.

Submit a number written the normal way — `555-123-4567` — and you get `Error: Phone Number must be numeric` — the
hint text does say `ex:4445556666`, in small italics below the field. Fair enough.
But after that error:

- the **confirm checkbox is cleared**, and
- the **Remove Information button is left disabled** and never re-enables.

So correcting the field and pressing submit does nothing at all. The only way
through is to reload the page and fill the whole form again. A person who types a
phone number the way people type phone numbers hits an error, fixes it, clicks,
watches nothing happen, and reasonably concludes the removal form does not work.

**The free-text box is the valuable part.** "Removal reason" accepts a long
message, so the whole request fits — every telephone number rather than the
single one the phone field takes, name variants, and the substantive asks:
both-directions removal, carrier/line-type/location enrichment, related-person
appearances on other numbers' pages, and standing suppression rather than
one-time deletion. **A one-identifier form with a free-text field is not a
one-identifier form.** Look for the box before accepting the constraint.

**Use it to report faults too.** Both problems above went into that box along with
the request; it costs nothing and it is the only channel that reaches them.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
