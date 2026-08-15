# Radaris

- **Removal:** https://radaris.com/control-privacy   (note: `control-privacy`,
  hyphenated — not `control/privacy`)
- **Email:** support@radaris.com → replies from customer-service@radaris.com
- **Priority: 5.**

## Route (no account needed, despite what the search UI implies)
1. `/control-privacy` → **NEXT**
2. "Please identify your personal page" — paste your **profile URL**.
   Find it by searching `radaris.com/ng/search?ff=First&fl=Last&fs=ST&fc=City`,
   then clicking **View Profile** on the right record. Profile URLs live on
   per-state subdomains, e.g. `pennsylvaniamaps.radaris.com/person/~Name/<id>`.
3. Radaris echoes back name, **age + birth month/year**, and city — an excellent
   identity cross-check before you commit. Confirm it matches before proceeding.
4. **START REMOVING** → enter email → **reCAPTCHA** → SUBMIT
5. Verification link + confirmation code arrive by email. Use a mailbox you can
   actually read; the email doubles as the status-tracking reference.

## STATUS: the web removal flow does not complete

**Confirmed over two full attempts with the CAPTCHA solved by a human.** The
`/control-privacy` wizard identifies the record correctly, accepts an email at the
"Begin verification" step — which explicitly promises *"We will send you a link and
confirmation code"* — and then sends nothing. No verification email, no code, on
either attempt.

What arrives instead is an email from **OneRep** asking the user to confirm an
account they did not knowingly create.

So the observable behaviour is: a consumer follows Radaris's own published removal
instructions and ends up enrolled with a third-party commercial service, with no
removal request on file. Whether that is a broken send or a deliberate funnel is
not something to assert from outside — but the outcome is the same either way, and
it is why this broker is marked `failed` rather than `submitted`.

**Do not confirm the OneRep email.** Confirming activates an account against the
requester's address at a company they never chose.

**Escalation:** reply on the `customer-service@radaris.com` thread asking them to
process the removal directly from the email, and to state in writing (a) that the
record is removed, (b) whether any data was transmitted to OneRep, and (c) that no
monitoring subscription was created.

## The OneRep trap — how to tell a real submission from a fake one

After the final SUBMIT you may land on a page reading *"Remove info from 230+
sites… PROTECT YOURSELF NOW! POWERED BY ONEREP"*. **That is a sales page, not a
confirmation.** Reaching it means the removal did **not** register.

Worse, it opens a new tab at `onerep.com/promo?fullName=…&city=…&state=…` with the
details you just typed — Radaris passes your query to a third-party commercial
service from inside its own privacy flow. Close that tab; don't fill it in.

**The only reliable success signal is the verification email** with a link and
confirmation code. If no email arrives within a few minutes, the request did not
go through — start over from `/control-privacy`.

## Gotchas
- **The email route is a dead end.** Support replies with a canned link to
  `/control-privacy` and ignores the substance — a protected-person request with
  full identifying detail got the same boilerplate as anyone else.
- **Watch the upsell.** The same reply recommends their free "Radar" monitoring
  service. Signing up means handing Radaris *more* data and an ongoing
  relationship, which is the opposite of the goal. Decline it.
- Their framing — *"Federal law does not require data brokers to delete publicly
  available information... we offer the option to remove it as a courtesy"* — is a
  positioning statement, not a limit on what you can ask for. The removal works.
- reCAPTCHA sits at the final submit, so everything up to it can be automated and
  handed off as a single click.
- **The wizard silently resets to step 1** if a click lands slightly off, and stale
  element refs from a previous step still resolve — so a batch of clicks can appear
  to succeed while going nowhere. Screenshot after each step rather than chaining
  blind clicks.

## Verification
Re-run the search URL above after ~7 days; the profile should no longer resolve.
