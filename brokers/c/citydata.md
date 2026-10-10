# Citydata

- **Opt-out:** https://citydata.ai/privacy/do_not_sell_personal_information/
- **Email:** privacy@citydata.ai (verified)
- **Method:** web_form — Web form.
- **Domain:** citydata.ai
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-10-10)
- Reference: `no acknowledgement; 45-day window open until ~2026-10-01`
- Note: SENT 2026-10-10 to privacy@citydata.ai, cc dpo@citydata.ai -- both published in their policy for access, update and removal. THE BLOCKER IS A MAID REQUIREMENT AND IT WAS RAISED UP FRONT RATHER THAN AFTER A ROUND TRIP. Their policy states that deletion of DEVICE DATA requires the end user's mobile identifier -- IDFA on iPhone, ADID on Android. That will never be supplied, and the letter explains why rather than simply refusing: a mobile advertising ID is the most powerful key in a location dataset, stable and unique to a device, joining across every source that has ever seen it. Supplying one to obtain a deletion furnishes the identifier that makes a person findable AND creates a durable link between it and a named individual who has just confirmed his address, phone and email. IF NO RECORD KEYED TO HIM EXISTS, THE REQUEST DOES NOT TEST FOR A MATCH -- IT BUILDS ONE. Sixth company in this category after Adagio (463), Index Exchange (471b), Epieos (476b), Mobilewalla (477a) and Place Exchange (479a). THREE QUESTIONS PUT, each answerable in a line: can they act on the NON-device data (End User, Customer and Visitor records, which their policy describes without a device key); is there a suppression they can apply to device data WITHOUT the raw identifier, e.g. keyed to a hashed or derived value; and if the honest answer is that without an IDFA or ADID they cannot find or remove device data, will they say so outright -- with an undertaking to record that as final and not write again. Mobilewalla's one-line version of that answer was cited approvingly. ALSO FLAGGED THE RESIDENCY AMBIGUITY: their policy says CityData 'supports US State Privacy Rights beyond California' without naming the states, while the removal language covers 'an End User, Customer, or Visitor' with no residency condition. Asked them to correct the reading if it is wrong rather than pressing a point they never made. LOCATION-SPECIFIC LIMIT ADDED to the standing association rule: suppressing a bare address in a location dataset could affect everyone who has ever been at it, which makes key-to-the-association matter more here than anywhere. Postal: 548 Market Street, San Francisco CA 94104. Phone (650) 204-0028.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** CITYDATA Inc.
- **Trading as:** CityData.AI
- **Registered address:** 548 Market Street, San Francisco, CA, 94104
- **Filed contact email:** [named individual]@citydata.ai
- **Filed phone:** 6502040028
- **Website:** https://citydata.ai

*Source: `data/registries/registry.csv`.*

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
