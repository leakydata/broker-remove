# Leadpost

- **Opt-out:** https://client.leadpost.com/PrivacyRequest
- **Email:** delete_mydata@leadpost.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** leadpost.com
- **Priority: 2.**

## Status

- Current: `captcha_blocked` (updated 2026-09-06)
- Reference: `outbox/staged/leadpost_privacyrequest.txt`
- Note: FORM FOUND, FILLED OUT ON PAPER, AND STAGED FOR A HUMAN: outbox/staged/leadpost_privacyrequest.txt. client.leadpost.com/PrivacyRequest redirects to app.leadpost.com/OptOut/PrivacyRequest and carries reCAPTCHA v2 with a VISIBLE CHECKBOX -- div class=g-recaptcha, no data-size=invisible, api.js loaded without a render= parameter, so it is the tick-the-box variant rather than a scored background check. One human click; everything else is settled in the staged file. BEST-DESIGNED CONSUMER FORM SEEN IN THIS PROJECT SO FAR. It offers four rights as INDEPENDENT CHECKBOXES rather than one undifferentiated privacy request: Delete My Data; Send me a Copy of my Data; Send me Who Recieved my Data; Opt Out of Future Data Collection. The third is the unusual one -- most companies make you ask for the recipients list in prose and then answer in categories; LeadPost put 1798.115 on the form as a tick box. Staged instruction is to tick all four. THE FOURTH MATTERS MORE HERE THAN AT MOST BROKERS: LeadPost's business is identifying anonymous website visitors and resolving them to a named person with a postal address, so a deletion without an opt-out from future collection is undone the next time the subject loads a page carrying their pixel. Delete plus opt-out is the pair that holds; either alone does not. Fields staged: email, first and last name, street address, [PERSONAL], PA, [PERSONAL], United States. PHONE LEFT BLANK deliberately -- not needed to identify the record, and supplying a number to a visitor-identification company adds a key they may not hold; if the form insists, that refusal is itself worth recording. Staged file also carries the route history so nobody re-treads it: delete_mydata@ is an autoresponder pointing at this form signed 'Eric', privacy@ is an untested site-published fallback, amanda@ is the named contact, and support@leadpost.com is what the form itself names for technical problems -- which is the right escalation if the CAPTCHA or submission misbehaves, since a form that cannot be submitted IS a technical issue with the request.

## Steps

1. Email `delete_mydata@leadpost.com` — a dedicated address, so a real process is
   likely.
2. Ask for the **visitor-identification records**, not only the contact record.
3. Ask which clients received the details.
4. Ask for permanent suppression, and for do-not-contact entries held
   independently.

## Gotchas

**The visit records are the point, and they are not what "contact data" brings to
mind.** A visitor-identification service resolves an anonymous website visitor to a
named person and hands the details to the site operator. So there are two things: a
contact record, and a record that *this person was on that website at that time*.

The second is the more revealing of the two and the more likely to be missed,
because a deletion framed around "my contact details" reads as being about the
first. Ask for any record connecting you — by cookie, device, IP address, hashed
email or identity-graph edge — to a **visit**.

**The client copy is what actually mails you.** Deleting the source record removes
the least consequential copy; the export sitting in a client's CRM is what produces
the arriving mail. Ask for the client list in the same breath, so a processor
answer at least yields the next address to write to (`_DEFLECTIONS.md` §21).

## Verification

Nothing public to search. The practical check is negative and slow: if mail keeps
arriving from their clients, the exported copies were never addressed. Ask for the
client list so that becomes actionable rather than merely irritating.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** LeadPost LLC
- **Registered address:** 555 Washington Ave, St Louis, MO, 63101
- **Filed contact email:** [named individual]@leadpost.com
- **Filed phone:** (866) 456-6674
- **Website:** https://leadpost.com

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
