# Privatenumberchecker Com

- **Opt-out:** https://www.privatenumberchecker.com/removal-request/
- **Email:** support@privatenumberchecker.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** privatenumberchecker.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: SUBMITTED AND CONFIRMED on-page: 'Removal request success! Thank you! Your removal request has been sent!' The emailed route was dead - support@privatenumberchecker.com hard-bounces 'address not found' even though the domain publishes its own MX - but /removalrequest/ is a real form with NO CAPTCHA and, importantly, a free-text 'Removal reason' box that took the entire request: all 12 phone numbers, five name variants, the current address, and the asks for both-directions removal, carrier/line-type/location enrichment, related-person appearances on other numbers' pages, and standing suppression rather than one-time deletion. Two faults reported to them in that box. First the dead support address. Second: the phone field rejects hyphens with 'Phone Number must be numeric', and THE FAILED VALIDATION LEAVES THE SUBMIT BUTTON DISABLED - so correcting the field and pressing submit does nothing, and the only way through is to reload and start over. Anyone who types a phone number the normal way hits that and may well conclude the site is broken.

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
