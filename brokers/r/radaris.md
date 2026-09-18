# Radaris

- **Start here:** https://radaris.com/data_privacy_center
- **Removal wizard:** https://radaris.com/control-privacy
- **Email:** removal@radaris.com · removals@radaris.com (covered persons) ·
  customer-service@radaris.com (multiple records, general)
- **Phone:** (855) 723-2747
- **Status: CONFIRMED REMOVED** — approved by administrator, then verified by
  search (results went 4 → 3; the subject's record is gone).
- **Priority: 5.**

## The flow does work — but the timing misleads

**Correction to an earlier version of this file.** It previously stated that
Radaris never sends the promised verification email. That was wrong, and worth
explaining because the mistake is easy to repeat.

What actually happens after you submit:

1. You land on a page headed *"Remove info from 230+ sites… PROTECT YOURSELF NOW!
   POWERED BY ONEREP"*, and a **new tab opens at onerep.com pre-filled with the
   details you just typed**.
2. **A few minutes later**, the real verification email arrives from
   `customer-service@radaris.com`, subject *"Radaris Information Removal"*, with a
   confirm link (`/ng/control/confirm_request?id=…&code=…`) and a status URL.
3. Clicking it queues the request. Approval is stated at **up to 24 hours**.
4. A second email confirms: *"Your removal request has been approved."*

So the upsell page is **not** a failure signal — it is simply what they show while
the email is in flight. Checking the inbox immediately and concluding the flow is
broken is the trap. **Wait several minutes before judging.**

Two things remain true and worth knowing:
- Radaris does pass your query to OneRep, and a **OneRep account confirmation may
  arrive** for an account you did not knowingly create. Do not confirm it.
- The status URL (`/ng/control/request_status?id=…`) lets you check progress
  without waiting for email.

## Routes the wizard never mentions
From `/data_privacy_center`:
- **removals@radaris.com** — Covered Persons, defined as *"former, active or
  retired… judges, prosecutors, and members of law enforcement"*. **Former** is
  explicit. Note this sits under a **Daniel's Law** heading — a New Jersey statute
  — so a non-NJ resident should state their actual role and ask whether the process
  extends to them rather than asserting Covered Person status.
- **customer-service@radaris.com** — for **multiple records**. Their FAQ admits the
  online process removes only ONE, and that records they cannot match to an
  existing profile become *separate* profiles. Anyone with address history across
  several towns likely has more than one.
- **Appeal rights** for residents of CO, CT, DE, IA, MT, NE, NH, NJ, OR, TX, TN, VA.

## Route that worked
1. Search `radaris.com/ng/search?ff=First&fl=Last&fs=ST&fc=City`, click **View
   Profile** on the right record. Profile URLs sit on per-state subdomains:
   `pennsylvaniamaps.radaris.com/person/~Name/<id>`.
2. `/control-privacy` → NEXT → paste the profile URL → Radaris echoes back name,
   **age and birth month/year**, and city — an excellent identity cross-check.
3. START REMOVING → email → reCAPTCHA → SUBMIT.
4. **Wait for the email**, click the confirm link, wait up to 24h for approval.

## Gotchas
- The wizard **silently resets to step 1** on a near-miss click while stale element
  refs still resolve, so a chained batch of clicks can report success and do
  nothing. Screenshot after each step.
- reCAPTCHA at final submit — hand off to a human there.
- Verify by re-running the search URL and pressing **Ctrl+F5 / Cmd+R**; they warn a
  cached page will show a stale listing.

## radaris.de is a separate scope question (2026-09-12)

The confirmed removal above is for radaris.com. A follow-up letter went to
`customer-service@radaris.com` on 2026-09-12 asking, as a **Datenschutzanfrage
/ data protection request** specifically about **radaris.de**: (1) whether the
.com removal already propagated to the .de index or whether the two are
separate properties entirely, (2) which legal entity operates .de (relevant
because GDPR, not CCPA, would govern a genuinely separate EU/DE operator),
and (3) if a record still exists on .de, to delete and suppress it there too.
No reply yet as of 2026-09-12 — do not assume the .com confirmation covers
.de until this is answered. See `_FAMILIES.md` for the general pattern of a
removal confirmed for one hostname from a company that runs several.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://radaris.com/data_privacy_center
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `[named individual]@radaris.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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
