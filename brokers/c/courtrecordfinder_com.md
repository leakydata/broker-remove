# Courtrecordfinder Com

- **Email:** privacy@cisnationwide.com (verified)
- **Method:** unknown — Route not yet established.
- **Domain:** courtrecordfinder.com
- **Priority: 1.**

## Status

- Current: `confirmed` (updated 2026-10-20)
- Note: THE FOLLOW-UP WORKED. The 2026-09-17 reply answered about the wrong
  site (cisnationwide.com instead of courtrecordfinder.com — see history
  below for why), so the prior agent correctly regressed the status from
  `confirmed` back to `replied` and sent a plain-text, no-links follow-up
  naming the domain explicitly and asking three questions. CIS Nationwide
  replied again on 2026-10-20, this time explicitly: *"Thank you for your
  follow-up and for the clarification regarding courtrecordfinder.com. The
  site is no longer active and cannot be accessed. The information relating
  to your request has been deleted in accordance with applicable privacy
  laws, and will not be republished... there is nothing further retained on
  our side, and we will consider this matter closed."* This names the
  right domain this time, so `confirmed` is earned. It does not answer the
  other two questions from the follow-up (where the data went, which other
  properties were searched) — treat those as open if this operator is ever
  recontacted, but a dead, delisted domain with an explicit non-republication
  statement is as complete an outcome as this one gets.
- Prior (2026-09-17, now understood to be about the wrong site): CIS
  Nationwide wrote 'Your request relates to the website hosted on
  cisnationwide.com. That website is no longer active and all information
  has been removed from that domain... This is our final response.' THE
  LINKIFIER BUG DID REAL DAMAGE: `scripts/letter_html.py` exists because
  Gmail rewrites bare domains into `google.com/url` tracking redirects AND
  REPLACES THE VISIBLE TEXT. That letter went as plain text, so the
  protection did not apply, and the site name was buried inside a redirect —
  a reader skimming it could easily read "courtrecordfinder.com" as the
  sender's own domain. EVERY letter naming a specific site must go as HTML.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@cisnationwide.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

- **The operator's own address is shared with an unrelated domain.**
  `privacy@cisnationwide.com` handles mail for both `courtrecordfinder.com`
  (this id) and `cisnationwide.com` itself (a separate registry row,
  `cisnationwide`, if one exists). A generic reply about "the website" is
  ambiguous between the two — always name the domain explicitly, in the
  subject line and the opening sentence, and send the letter as HTML (see
  `scripts/letter_html.py`) so Gmail's link-rewriting doesn't bury the
  domain inside a `google.com/url` redirect. A plain-text letter here
  produced exactly that ambiguity and got answered about the wrong site.
- No CAPTCHA was ever encountered — the whole exchange happened over email.
- The outcome here was "the site is dead, so the request is moot" rather
  than an active deletion against a live index. That is a legitimate
  closure, but it says nothing about whether the underlying court-record
  data moved to a successor site or was returned to a supplier — see the
  Status note above.

## Verification

The company itself says courtrecordfinder.com is no longer active, so the
usual "re-run the search URL" check does not apply -- the site is gone, not
merely the listing. If the domain is ever reactivated (by CIS Nationwide or a
successor), re-check for a listing under the same name/address set before
assuming this stays closed.

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
