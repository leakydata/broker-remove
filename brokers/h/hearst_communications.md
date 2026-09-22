# Hearst Communications Inc

- **Opt-out:** https://www.hearst.com/-/us-magazines-privacy-notice
- **Email:** magsdatarequests@hearst.com (verified)
- **Method:** unknown — Route not yet established.
- **Priority: 1.**

## Status

- Current: `manual_required` (updated 2026-09-22)
- Reference: `gmail:1a0b415257fea3b0`
- Note: 9/21 reply from magsdatarequests@hearst.com: "we process privacy
  rights requests through our online privacy portals to account for
  cookie-level data... unless a request is submitted through the appropriate
  form or device-level mechanism, we may not be able to apply the request to
  this device-specific cookie-level data." Pointed to the "Your Privacy
  Choices (Opt Out of Sale/Targeted Ads)" footer link on each Hearst
  Magazines site/app, which is per-browser/per-device — this is a genuine
  no-email-route case (see `_DEFLECTIONS.md`), not a boilerplate deflection,
  since the stated reason (cookie/device scoping) is a real technical
  constraint an email can't carry. Queued in `scripts/handoff.py` for a
  human with a browser (`hearst_communications`, ~5 min, `form`). No further
  email action here — the identity/deletion portion of the letter may still
  get answered separately; watch for a second reply.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.hearst.com/-/us-magazines-privacy-notice
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `magsdatarequests@hearst.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

**Cookie/device-level opt-out cannot be carried by an emailed letter, and
Hearst says so plainly rather than hiding behind it.** Their reply explains
the actual reason a form is required for the sale/targeted-ads opt-out: it's
tied to a specific browser/device via cookies, and there is no way to apply
that from an emailed identifier list. This is a legitimate technical
constraint, not a designated-method stonewall — treat it as `manual_required`,
not as a deflection to argue with. Requires opening each Hearst site/app you
use, clicking the footer's "Your Privacy Choices" link, and repeating per
device/browser.

## Verification

Once the human handoff is done, there's no server-side confirmation beyond
the form's own "your preference has been saved" — re-check by loading the
same footer link on the same browser/device and confirming it still shows
opted out.

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
