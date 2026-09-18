# PeopleSearchNow

- **Working route:** https://www.peoplesearchnow.com/privacy-rights
- **Also:** `/opt-out`, `/do-not-sell`
- **Email: REFUSED.** *"This email address is dedicated to customer service
  inquiries... We do not process privacy requests received via email."*
- **Priority: 3.**

## Status

- Current: `email_pending` (updated 2026-09-08)
- Reference: `ticket 11440330, expires ~2026-09-09 03:28 UTC`
- Note: STAGE 1 SUBMITTED AND THE STAGE-2 LINK HAS ARRIVED, 2026-09-08 03:28 UTC, ticket 11440330. The stage-1 form went in with the correct values -- the link's key encodes subject / [PERSONAL] / [PERSONAL] / [EMAIL] -- so the staged file was followed. THE 24-HOUR CLOCK IS RUNNING: their own email says 'If you waited longer than 24 hours to click the link below, you will need to start over and generate another link.' Expiry is approximately 03:28 UTC on 2026-09-09. Status moved from captcha_blocked to email_pending, which is the accurate description now: the CAPTCHA is behind us and the request is waiting on one human step that silently expires. Stage 2 is /opt-out/validate-record-info -- identifying WHICH record, so expect name, address and possibly age or date of birth. Handoff updated with the deadline and the instruction to open the link from the email rather than retyping it. CARRIED FORWARD SO THE ROW IS NOT CLOSED TOO EARLY: this site concedes on its own /do-not-sell page that 'we regularly receive new public records so even if you opt out, your publicly available information may appear in our data products again in the future. We recommend you periodically refresh your opt-out request.' Whatever stage 2 returns is a lease rather than a permanent removal, and the row should be diarised for a re-check rather than marked confirmed.

## Third member of the TruePeopleSearch platform family

The refusal email is **word-for-word identical** to TruePeopleSearch's and
FamilyTreeNow's, and `/privacy-rights` presents the same form. Everything in
`brokers/t/truepeoplesearch.md` applies:

- Select **"Right to Know"**, not "Right to Delete" — Delete renders no form.
- Context: *"I have no direct relationship with the company"*.
- The state dropdown lists **all 50 states including Pennsylvania**, despite the
  preamble implying only "covered" states qualify.

Known family members so far: **TruePeopleSearch, FamilyTreeNow, PeopleSearchNow**.
When a refusal email matches one you have seen before, try the sibling's route
straight away rather than re-deriving it.

## Form-filling notes

The form **collapses back to its initial state** if the top-level category dropdown
loses its value — which hides every field below it and looks like a total reset.
The lower dropdowns usually retain their values in the DOM even when hidden, so
re-selecting only the top dropdown restores the rest rather than requiring a full
refill. Check before retyping everything.

Fill in stages with a screenshot after each, rather than chaining a long batch: a
chained sequence reported success on every step here while the form silently reset.

## Gotchas
- **A Google vignette ad overlay can hijack the page mid-fill and reset every
  field.** It appeared here after the form was fully populated and wiped it. Fill
  quickly, screenshot to verify, and expect to redo it.

## Refused on jurisdiction; the opt-out route is a different door

The statutory "Right to Know" was refused because Pennsylvania has no comprehensive
consumer privacy law -- see `_DEFLECTIONS.md` §27 for the wording and for why
appealing that is a bad trade. The refusal arrived in the same minute, in the same
words, from TruePeopleSearch, FamilyTreeNow and PeopleSearchNow, which is the family
confirmation by itself.

Their self-service opt-out is a **separate mechanism** that never asks what state
you live in. It is an email-link flow: name and email plus a captcha, then a link
that **expires in 24 hours**, then a fuller form where the record details actually
go. Submitting only the first step achieves nothing while looking like progress.

## The one in the family that cannot be verified from here

Same three-stage self-service opt-out as its siblings, and the same jurisdictional
refusal on the statutory route. The difference is that **peoplesearchnow.com refuses
the automation both page-text reads and screenshots**, so the outcome cannot be read
off the screen.

After the final submit the tab sat on `/opt-out/validate-record-info` with no key --
which is what you would see after a successful submit-and-reload, and equally what you
would see after an error. No confirmation email arrived either, although the flow says
one will.

**Recorded as not-yet-confirmed rather than submitted.** The standing rule is that a
broker-issued artifact is required, and "the tab looks plausible" is not one. Its two
siblings both produced an explicit confirmation naming the record back, which is
exactly the artifact missing here -- and the contrast is the reason to be suspicious
rather than to generalise from them.

**A note on stage-two links.** The emailed link carries a base64 `key` **and** a
separate `ticketid`. Losing the second produces *"Opt-Out Request Expired - The data in
the request seems to have some errors"* on a link minutes old. See
`_SILENT_FAILURES.md` §27: take the URL from the HTML part of the message, not the
plaintext part.


## Part of the Mississippi Tornado Alley family

This site is one of **ten** named in a single 2026 California data broker
registration by **Mississippi Tornado Alley, LLC**, alongside
CyberBackgroundChecks, AdvancedBackgroundChecks, FastBackgroundCheck,
PeopleSearchNow, Phonebooks, SearchPeopleFree, SmartBackgroundChecks,
USA-People-Search, USPhoneBook and FastPeopleSearch.

Nothing on any of the sites connects them, and the legal entity's name appears on
none of them. See `mississippi_tornado_alley.md` for the consolidated letter sent
to `privacy@mtalley.zendesk.com` on 2026-08-23, and `_FAMILIES.md` for the
method.

**Read any confirmation from this site for scope.** One naming only this hostname
leaves nine siblings unaddressed, and that is indistinguishable from a complete
removal from the outside. The individual thread stays open until the family
answers for the estate.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.peoplesearchnow.com/opt-out
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `support@peoplesearchnow.zendesk.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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
