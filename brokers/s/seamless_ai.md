# Seamless Ai

- **Opt-out:** https://login.seamless.ai/personalDataRequest
- **Email:** privacy@seamlessleads.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** seamlessleads.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-10-10)
- Note: ERASED, WITH THE FULLEST PRE-ERASURE DISCLOSURE THIS PROJECT HAS RECEIVED -- replied 2026-09-17, found unread 2026-10-10, 23 days later. Seamless.AI confirmed erasure, listed what they held before deleting it, named the retention basis, and recorded the opt-out and suppression as complete: 'We retain only your name and email address for recordkeeping purposes... We also retain this information to support your suppression request, and to prevent re-collection of your data.' THE DISCLOSURE ITSELF IS THE FINDING, AND IT IS NOT GOOD NEWS. The file was a COMPOSITE OF AT LEAST FOUR OR FIVE DIFFERENT PEOPLE sharing the name. It listed roughly 47 job positions, around 50 email addresses and 13 phone numbers. Only a handful of the positions are the subject's -- the university ones and two real employers. The rest belong to other [PERSONAL]es: a law firm, a sports agency, a real-estate company, a music-rights organisation, a food-service company, an equipment dealer, a bank collections role and a military research fellowship. Several phone numbers are not his at all; one is a university main switchboard and another is a repeated-digit placeholder. A CONFLATED RECORD IS WORSE THAN AN ACCURATE ONE -- sold to a subscriber it attaches a stranger's employment history to his name and number, and his to theirs. AND THE ACCESS RESPONSE ITSELF DISCLOSED THIRD-PARTY PERSONAL DATA. At least two addresses in the list belong to identifiable other people -- a woman at a managed-services firm and a man with a different first name at a consumer ISP -- sent to an unrelated requester because the file was disclosed in full. Raised with them directly and privately, with an explicit statement that the information will not be used and is not being reproduced, and a suggestion that access responses be screened for identifiers that do not match the requester. NOT ESCALATING; the point is that it gets fixed. DELIBERATELY NOT RECORDING THE THIRD-PARTY IDENTIFIERS ANYWHERE IN THIS REPOSITORY. redact.py only knows the subject's own values, so it would not have caught them -- this is a category of leak the guard cannot see, and the only protection is not writing them down. THE SUPPRESSION QUESTION NOW ASKED, and it cuts against the subject's own interest: if the suppression is keyed to ALL identifiers from the deleted record rather than just his name and address, it should be NARROWED, because suppressing strangers' addresses on his account is not his decision to make. Also asked whether suppression prevents re-assembly of the same composite from the same sources, since two retained identifiers will not stop a rebuild keyed on employer and job title. ONE PUSH ON RECIPIENTS, then letting it go: they say they cannot identify recipients (accepted) and do not know HOW MANY (asked them to check rather than assume, since export events are usually logged for billing even when not logged against the record).

## Steps

1. Email `privacy@seamlessleads.com` first. It will not process the request, but the
   autoresponder is worth having: it names the portal **and** offers an explicit
   email fallback (see Gotchas).
2. Go to `preferences.seamless.ai` — a **DataGrail** Privacy Request Center.
3. Pick country **United States**, then state. The state picker defaults to
   *Virginia*; change it. Pennsylvania is accepted and does not reduce the options.
4. Choose **Start Delete My Information/Opt-Out of the Sale or Sharing** — the
   broadest card.
5. Fill first name, last name, email, phone. A phone number is required: *"please
   include a phone number or a direct line (general corporate phone numbers not
   applicable)."*
6. **Relationship**: Business Contact / Customer / Employee / Former Employee / Job
   Applicant / **Other**. Pick Other if none is true.
7. **Request type**: Deletion request, or Opt-out. Deletion is broader.
8. Put everything the form has no field for into **Additional comments** — the
   other identifiers, suppression, and the provenance and recipient questions.
9. Review Request → tick the **hCaptcha** → Submit Request.

## Gotchas

- **The state picker silently defaults to Virginia.** Change it before anything
  else; the choice is carried in the URL as `locationCode=US-PA` and shapes what
  the form will accept.
- **Pennsylvania is accepted here**, and all five request types remain available —
  worth noting, because PA is the usual trigger for a jurisdiction refusal.
- **Do not misstate the relationship to satisfy the dropdown.** "Other" is honest
  for a compiled record; "Business Contact" or "Customer" implies a relationship
  that does not exist.
- **hCaptcha at submit** — but this form behaves well: it renders an explicit
  *"Complete the Captcha"* error rather than failing silently. Contrast
  [[_SILENT_FAILURES]] §59.
- **There is a documented email fallback**, which is rare and worth keeping:
  *"If you are unable to complete the Privacy Request Center, kindly respond to
  this email with the following information so that we may process your request"* —
  full name, country and state, city, email, phone.

## Verification

No public lookup — this is a B2B contact database, so nothing to search yourself in.

They state their own clock: *"generally 45 days under the California Consumer
Privacy Act or 30 days under the General Data Protection Regulation, unless we need
to extend that timeframe as permitted by applicable law."*

Keep the request ID from the confirmation email; the portal issues one and it is
the only artifact. When a response arrives, check it against the three questions
put in the comments box — provenance, recipients, and whether a mobile or
direct-dial number is held — because a generic completion notice will address none
of them.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Seamless Contacts, Inc.
- **Trading as:** Seamless.AI
- **Registered address:** 7652 Sawmill Road, Suite 341, Dublin, OH
- **Filed contact email:** privacy@seamlessleads.com
- **Website:** https://www.seamless.ai

*Source: `data/registries/registry2024.csv`.*

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
