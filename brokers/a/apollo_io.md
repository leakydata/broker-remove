# Apollo.io

- **Opt-out:** https://www.apollo.io/privacy-policy/remove
- **Email:** privacy@apollo.io (verified)
- **Method:** web_form — Web form.
- **Domain:** apollo.io
- **Priority: 4.**

## Status

- Current: `confirmed` (updated 2026-08-22)
- Note: privacy@apollo.io replied within minutes: "we have successfully actioned
  the deletion request you submitted. We have also added the individual to our
  suppression files to ensure that they are not re-added to the Apollo database
  in the future." Unusually fast and a genuine confirmation, not an auto-ack —
  and it names suppression specifically, not just deletion. No mention of the
  LinkedIn/work-email pushback documented below, so this may have matched on the
  phone number or name variant alone. Worth a re-check at the 7-14 day mark
  given how little friction this one had compared to the deflection this
  category usually produces.

## Steps

1. Email `privacy@apollo.io`. That is the whole route — no form, no account, no
   verification round trip.
2. Tailor per the "B2B contact & sales prospecting" section of
   `_CATEGORY_VARIANTS.md`: redirect the search to telephone numbers and name
   variants, decline the profile URL, ask for suppression regardless of result.
3. Wait. The reply came in **four minutes**.

## Gotchas

**There are almost none, and that is the finding.** Apollo is the best-behaved
broker in this project so far. Recorded here as a benchmark to hold others to,
because "nobody does that" is the standard deflection and Apollo is the
counter-example.

<!-- Original scaffold prompts, kept for reference:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

No public profile page to re-check. The confirmation is the artifact, and it is
unusually specific — it states the suppression, the downstream notice, and the
categories held. Re-verify by watching for renewed cold contact on the
`.edu`-era identifiers rather than by searching a site.

## The reply, quoted, because it is the standard to hold others to

Four minutes after the letter, from `privacy@apollo.io`:

> *"We are writing to inform you that we have successfully actioned the deletion
> request you submitted. We have also added the individual to our suppression
> files to ensure that they are not inadvertently added back to our database in
> the future."*

**That is deletion plus standing suppression, volunteered.** Most brokers have to
be asked twice and then answer ambiguously; the distinction between a one-time
removal and a suppression entry is the single most common silent failure in this
whole project, and Apollo closed it in one sentence without being pressed.

Then the part almost nobody does:

> *"When we remove the individual's data as per the request, we automatically
> provide notice to our customers that the individual opted out of Apollo's
> database, and they should delete the contact unless they have a separate legal
> basis for processing."*

**Downstream propagation, automatic and by default.** The exported copy sitting
in a customer's CRM is the copy that actually produces the calls, and it is
beyond the broker's own deletion — this is the ask that gets refused, deflected
or ignored everywhere else. Apollo does it as a matter of course. Quote this at
any prospecting database that says customer copies are out of its hands: it is
not a technical impossibility, it is a choice, and a competitor has made the
other one.

And unprompted, the categories held:

> *"Name; contact information such as business email address or phone number;
> information about the individual's role with the business (including the name
> of the business, title, professional responsibilities and functions, office
> location, and education); professional social media profile information; job
> history and title(s)."*

> *"We may also make inferences about these business contacts, such as their
> likelihood to be interested in a B2B product or service offered by one of our
> customers."*

**Note the last line.** An intent inference is not a fact anyone supplied — it is
generated, it is personal information under the same statutes as the contact
fields, and disclosing it without being asked is rare. Compare the scope question
put to Revelio Labs, where the delivered "raw data" was scraped profile text and
the derived layer had to be asked for separately.

## Category: B2B contact & sales prospecting

See `_CATEGORY_VARIANTS.md`, section "B2B contact & sales prospecting databases",
and `_DEFLECTIONS.md` §44 for the deflection to expect ("which email format is it
under?" / "we can search under your LinkedIn URL").

**Address discovered, not curated.** `privacy@apollo.io` came from the
`verify_emails.py --no-email` sweep on 2026-08-20; Apollo had a live domain and
no route in the registry until then.

**What the letter asks that the standard one does not:**

- states up front that a search over personal webmail will return nothing even
  if a record exists, because the index is keyed to work addresses that are
  frequently pattern-generated or captured by a customer's browser extension —
  identifiers the subject never chose and cannot reproduce;
- redirects the search to **telephone numbers and name variants**; the phone
  number is the most person-shaped field a prospecting database holds, because a
  direct dial follows someone between jobs;
- asks **which mechanism created the record** — supplier feed or extension
  capture. This matters because supplier suppression does not stop the second
  one: any customer repeating the action recreates it;
- asks which customers exported the record into a CRM or sequencer, since that
  copy is beyond Apollo's deletion and is what produces the calls;
- asks for a **do-not-add suppression entry that survives a null result**, citing
  SourceIT's SHA-1/SHA-256 practice as precedent — naming another firm's
  practice moves the ask from favour to norm;
- **declines to supply a LinkedIn URL, with the reason given.** A profile URL is
  a stable, unique, employer-linked key; supplying one to a contact database
  furnishes an identifier they may not hold plus a link to everything else in the
  letter. If no record exists, that search assembles the match it claims to test.

**A null result here is not `not_found`.** It is a search run on the wrong keys
with the suppression request outstanding.
