# Crexi

- **Email:** privacy@crexi.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** crexi.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-10-12)
- Note: PORTAL SUBMITTED 2026-10-12 BUT STUCK AT EMAIL VERIFICATION, which needs a browser and cannot be completed from here. Two separate BigID requests now exist against this email: Request ID 2605666032 (a deletion request) and Request ID 8554488771 (an access/"view your data" request), each with its own "Verify your email" message. The verification link is not a plain confirmation GET — it resolves to a hash route on a single-page app (`https://crexi.bigidprivacy.cloud/consumer/...#/o2TCsG9LJ7/2605666032/confirmation/<token>/...`), so the actual confirmation call happens in client-side JS after the page boots; fetching the URL without a browser loads the empty app shell and does nothing. Both verification emails state a review against Crexi's own records before anything is actioned, and both warn in the same breath that deletion/opt-out "may impair some features and functionality of our service, including the possible deletion of your user account and delisting of your listings" — worth noting because that sentence implies Crexi expects requesters to sometimes hold an active marketplace account with listings, which is a different animal from a data-broker listing and worth confirming with the subject before anyone clicks through, in case they do not want an account or listings removed. Queued to `handoff.py` for a human click; links not yet expired as of 2026-10-15 (3 days old).
- Prior: REVERTED 2026-09-11 to manual_required, COMPLETING A CORRECTION I SAID WAS FINISHED AND WAS NOT. An adoption on 2026-08-28 overwrote a deliberate downgrade and set this row to submitted, where it has read ever since as though a request went in. It did not -- the company refused the email route, which is why the downgrade was made. _SILENT_FAILURES 434 recorded this for seventeen rows and claimed all seventeen were corrected; only seven were, and this is one of the ten that was left reading 'submitted' for another hour. THE EVIDENCE THE ADOPTION ERASED, from 2026-08-25: 2026-08-25: form-only. privacy@crexi.com auto-replies: 'in order to process data subject access requests, we require that individuals submit such requests through our online Privacy Portal (https://crexi...)'. The substantive letter was already sent and is on the thread; the portal submission needed doing, and has now been done (see above) — it just cannot be verified without a browser.

## Steps

1. Do not expect email to work — privacy@crexi.com auto-replies that the inbox
   is unmonitored and DSARs must go through their BigID portal.
2. Portal (queued in `handoff.py`): `https://crexi.bigidprivacy.cloud/consumer/#/o2TCsG9LJ7`
3. General support fallback (their auto-reply's words: "for any questions
   needing an immediate response"): support@crexi.com.

## Gotchas

`privacy@crexi.com` is unmonitored for DSARs — it auto-replies and routes to
the BigID portal. The portal itself is a two-step SPA: submit, then click an
emailed "Verify your email" link before anything is searched. That link is
not a plain confirmation GET — it resolves to a hash route
(`#/<company>/<request-id>/confirmation/<token>/...`) that a single-page app
reads client-side, so fetching the URL without executing JS loads an empty
shell and verifies nothing; this one needs an actual browser, not just a
non-interactive HTTP client. No CAPTCHA seen on either step. Worth flagging
before clicking through: Crexi's verification email warns that deletion "may
impair ... including the possible deletion of your user account and
delisting of your listings" — phrasing aimed at people with an active
marketplace account, which is a different thing from a data-broker-style
listing and worth confirming is wanted before anyone completes this.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Commercial Real Estate Exchange, Inc.
- **Trading as:** Crexi
- **Registered address:** 5510 Lincoln Blvd., Suite 400, Playa Vista, CA
- **Filed contact email:** privacy@crexi.com
- **Website:** https://www.crexi.com/

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
