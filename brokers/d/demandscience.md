# DemandScience

- **Opt-out:** https://demandscience.com/privacy-policy/ → the *Privacy Rights Request Form* anchor (a PrivacyEngine-hosted form, not a form on their own site)
- **Email:** alerts@support.privacyengine.io is outbound-only; correspondence comes from "Global Data Privacy, Legal & Compliance Office, DemandScience"
- **Method:** web_form (third-party rights platform: PrivacyEngine)
- **Domain:** demandscience.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-09-02)
- Note: REVERTED 2026-09-02, SAME DAY (SILENT_FAILURES 287). I moved this row to email_pending an hour earlier on the strength of an unconfirmed-looking verification email sitting in the inbox. THE ROW'S OWN HISTORY ALREADY SAID THE VERIFICATION WAS COMPLETED -- variously 'email verification clicked', 'Your request is confirmed!', 'successfully verified', or a later substantive reply that could only have followed confirmation. A verification mail stays in the inbox forever because nobody archives it; ITS PRESENCE IS NOT EVIDENCE THAT IT WAS NEVER USED. Nine of the ten rows I downgraded were already verified. Restored to submitted, which is what the evidence supports.

## How this broker was found

Not from any broker list. Terminus named DemandScience when asked where its data
came from — the supplier-disclosure technique in `_SILENT_FAILURES.md` §74. It
was absent from the registry entirely, which is the point of asking: a reseller
knows its upstream, and no public list does.

DemandScience is a B2B intent and contact-data business (previously PureB2B /
Leadiro). Its records are keyed to *work* identifiers, so read `leadiq.md` and
`_DEFLECTIONS.md` §44 before concluding a null result means anything.

## Finding the form (the part that wastes an hour)

The privacy page has three visible forms on it. **None of them is the rights
form.** Two are site search, one is a newsletter signup. The actual route is a
single text anchor in the running prose that leaves the domain entirely for
`portal.privacyengine.io`.

This is `_SILENT_FAILURES.md` §71 — a rights page with no rights form on it. The
practical rule that came out of it: **run the anchor sweep unconditionally**, not
only when no form is found. Counting forms on the page is the wrong test, because
the page can be full of forms and still have no route.

## The form demands things a member of the public does not have

See `_DEFLECTIONS.md` §43. The PrivacyEngine form requires a **Business Email
Address** and an **employer**, and its "Category of Data Subject" select offers
only: Current Employees, Former Employees, Job Candidates, Shift Workers,
Customers, Suppliers, Students, and "USA". There is no option for *a member of
the public whose details you bought from someone else* — which is what almost
everyone submitting the form actually is.

**Fill it, pick the least-wrong option, and disclaim the selection in the free
text.** Do not abandon the form over an unanswerable dropdown; a submitted form
with a stated caveat is worth infinitely more than an unsubmitted one, and the
caveat is what stops the selection being read back as a claim you made.

## Verification is required or the request is void

PrivacyEngine sends a verification link to the address on the form:

> *"Please verify your email address by clicking on the link below"*

Clicked 2026-08-20; the portal returned **"Your request has been successfully
verified."** under a "Request Received!" heading. No reference number is issued
at any point, which is worth knowing in advance — the verification page is the
only artifact there will be until they reply, so record the timestamp.

An unverified request is not a slow request, it is no request. Same failure mode
as Growbots (see the handoff queue) where the confirmation went to a mailbox the
requester had to open separately.

## What their acknowledgement actually promises

Quoted, because the suppression sentence is better than most and worth holding
them to:

> *"In the event that an individual has made an Opt-Out or deletion request, we
> retain an email address and phone number (if one is in our database) in a
> secure suppression file, which ensures that the data is not sold or processed
> for marketing, or other purposes in the future. This is processed under the
> legal basis of Legal Obligation."*

Three things to note:

1. **This is standing suppression, not point-in-time removal** — stated
   unprompted, which is rare. It is the answer to the question most brokers
   dodge.
2. **The retained fields are email and phone only.** So the suppression key does
   not include name or postal address, and a record arriving from a supplier
   under a work email not in the file would not be caught. Worth asking about.
3. **"Should we hold any"** in the preceding paragraph is the usual hedge. It is
   not a denial and should not be recorded as one.

## Verification

No public listing to re-check. The verification page is the only artifact so far.
If a reply names what was held, record which identifiers matched — for a B2B
intent business the interesting answer is whether they hold a work address, an
employer, and intent/topic scores, since those are inferred fields that no
consumer-shaped search would surface.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Demand Science US, LLC
- **Trading as:** Demand Science
- **Registered address:** 230 Independence Way, STE 1 #1030, Danvers,
  Massachusetts, 01923
- **Filed contact email:** legal@demandscience.com
- **Filed phone:** 8577701744
- **Website:** demandscience.com

*Source: `data/registries/registry.csv`.*

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://demandscience.com/privacy-policy/
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `legal@demandscience.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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
