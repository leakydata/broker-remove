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
