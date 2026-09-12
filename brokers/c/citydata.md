# Citydata

- **Opt-out:** https://citydata.ai/privacy/do_not_sell_personal_information/
- **Email:** privacy@citydata.ai (verified)
- **Method:** web_form — Web form.
- **Domain:** citydata.ai
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-09-07)
- Reference: `no acknowledgement; 45-day window open until ~2026-10-01`
- Note: RESTS ON A SEND AND NOTHING ELSE, flagged 2026-09-07. No acknowledgement, no reference number, no reply since the 17-19 August letter -- and the company's published opt-out URL now returns HTTP 404, so if the email did not land there is no second channel to fall back on. 'submitted' is doing more work for this row than the evidence supports; treat it as sent, not as received. See SILENT_FAILURES 393. NOT CHASED YET, DELIBERATELY: at 19-21 days this is well inside a 45-day response window and nothing is overdue. Telling a company it is late when it is not is both wrong and costs credibility on every later letter. DIARISED FOR THE FIRST WEEK OF OCTOBER 2026, when the ask is an acknowledgement rather than an accusation, and the dead route becomes a fact to report to them rather than a grievance -- your published opt-out URL returns 404, so if my email did not reach you there is now no route at all. A NOTE ON WHY THIS ROW IS NOT AN ERROR: a cross-reference of dead routes against submitted rows initially looked like fourteen requests filed through doors that no longer exist. All fourteen went by EMAIL; the dead URL is a stale field on the broker record, not the channel used. The route field describes the company, the via field describes the transaction, and joining on the wrong one manufactures an alarm.

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

## They answered the question that matters, and made a fair offer

Note: this is **CityData.AI**, the location-data company — distinct from
City-Data.com, the community-forums site covered in `citydata.md`'s other sections.
Two unrelated businesses with near-identical names, which is itself worth flagging
when working a registry.

Their reply is one of the more useful in this project:

> *"CityData.AI does not collect personal data attributes like names, phone
> numbers, addresses, email contact information, or dates of birth. In other words,
> we cannot look up an individual based on your name, email address, physical
> address, or phone number. If we have any data about you, it would only be a hashed
> (or anonymized) identifier in our cloud based on the Mobile Advertising ID."*

That answers the question the letter actually asked — *is there any other key?* —
and the answer is no. It is worth much more than a deletion confirmation would have
been, because it tells you what a deletion could even mean here.

**And the offer is better than the industry norm:**

> *"If you send the mobile phone's MAID, we will hash it, check it against our
> database of hashed IDs, and let you know if there is a match."*

**Check-then-tell, not blind ingest.** Compare `foursquare.md`, where the
advertising ID goes into an opt-out form and nothing comes back. Here the
identifier is used to answer a question and the answer is returned to you.

That does not make it free — sending a MAID still discloses a MAID, and their
stated process is unverifiable from outside. But it converts the decision from
"hand over an identifier and hope" into "hand over an identifier to get an answer",
which is a materially better trade and worth putting to the person whose device it
is.

**Still unanswered**, and worth chasing: whether deletion removes the underlying
location observations or only the mapping; whether device data has been sold or
licensed onward; and which basis they applied to a resident of a state with no
comprehensive privacy statute.

