# Citydata

- **Opt-out:** https://citydata.ai/privacy/do_not_sell_personal_information/
- **Email:** privacy@citydata.ai (verified)
- **Method:** web_form — Web form.
- **Domain:** citydata.ai
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-18)
- Note: Sent the SAME canned reply twice, word for word, ignoring a detailed message that answered its own question - so the email desk is a template loop, not a channel. Their form at /delrequest/form.php is the only real route; staged it with the address in the reason box, URL field left blank, text-image CAPTCHA remaining. Operator is Advameg, Inc.

## Steps

**Do not use email.** Their desk sent the identical canned reply twice, ignoring a
message that answered its own question — a template loop, not a channel
(`_SILENT_FAILURES.md` §19).

1. Go to `https://www.city-data.com/delrequest/form.php` — *Request to
   disassociate name from street-level assessment address*.
2. Fill name, email, state, county, city and the reason box. Put the **address**
   in the reason box, since the form has no address field.
3. The Address (URL) field wants a link to the specific page. If you cannot find
   one, leave it blank and see whether it submits — that settles whether the route
   is usable at all.
4. A text-image CAPTCHA sits on "Next step", so this is a hand-off.

Operator: **Advameg, Inc.**

## Gotchas

See the sections below: their reply searched by name while the pages are keyed to
address, the form needs a URL that is not discoverable from outside, and the email
desk repeats itself verbatim.


## Verification

Re-check the assessment page for the address, not a name search — and note their
own warning that search-engine caches update independently and slowly, which is
true and not something they control.

If the form is submitted successfully, ask on the confirmation whether it is a
permanent suppression or a one-time removal: county assessment data is re-ingested
on a cycle, and the form only promises the name "will be automatically erased".

## Their own form title answers their own search

They replied:

> *"We're unable to locate your name on our website, or your information has
> already been removed. To better assist you, could you please provide a direct
> link (URL) to the specific page on city-data.com where your details are
> displayed... Otherwise, we will have to close your request."*

And in the same message supplied a self-service route:

> *"If you meant Property Assessment pages, you can unlink your name using the
> respective link at page bottom, or directly via this form:
> https://www.city-data.com/delrequest/form.php"*

That form is headed **"Request to disassociate name from street-level assessment
address."**

**Read those two things together.** They searched by *name*. The pages they then
pointed at are organised by *address* — occupants listed under a property. A name
search does not necessarily surface them, so "we cannot find your name" and "there
is a page listing you at your address" are perfectly compatible statements.

This is `_SILENT_FAILURES.md` §17 in a new dress: the negative answered a narrower
question than the one asked, and the giveaway was in their own next sentence.

**The reply that fits:** supply the addresses, not more names, and ask them to look
those up.

## The URL catch-22, with a twist

Their form requires a direct link to the page. I could not find one — the obvious
street-page URL patterns 404 — which leaves the standard circularity: the form
needs a URL obtainable only by finding the page, and finding the page is half of
what the request was for.

The twist that makes it worth pressing rather than abandoning: **an address lookup
resolves it either way.** If the pages exist, they can send the URLs and the form
becomes usable. If they do not, there is nothing to remove and the written
negative closes the broker. Say both outcomes are acceptable; it makes the ask
cheap to grant.

## Two things the assessment form does not cover

- **Forum accounts.** City-Data hosts large discussion forums. An account is
  frequently a decade old and registered under an email address the person has
  stopped using — precisely what a name search misses and what an assessment-page
  form cannot touch. Ask by email address, and ask for the **username**, since a
  pseudonymous account is only pseudonymous until something links it to a name.
- **Suppression versus hiding.** Assessment data is re-ingested from county
  sources. The form says the name "will be automatically erased", which does not
  say whether it stays erased through the next refresh. Ask.

