# WINR Data

- **Email:** privacyoffice@winrdata.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** winrdata.com
- **Priority: 2.**

## Status

- Current: `acknowledged` (updated 2026-09-16)
- Note: Register-sourced, blank-site row -- and the REGISTER FILING ITSELF supplied the letter. WINR's 2024 entry describes the business in their own words: 'As a controller and third-party data company, we source non-sensitive personal data from our data partners from ONLINE COMPETITIONS, SALES PROMOTIONS, PRIZE DRAWS, SURVEYS, COUPON AND SAMPLE WEBSITES. We provide multinational FinTech and AdTech companies with data driven IDENTITY VERIFICATION AND IDENTITY RESOLUTION services.' Registered 2024, 2025 AND 2026. Wrote the letter around that rather than a template, and note they call themselves a CONTROLLER -- conceding the posture unasked. PRIMARY ASK -- THE CONSENT CHAIN. That sourcing is the co-registration model, whose distinguishing feature is that the data subject HAS NO MEMORY OF THE TRANSACTION AND NO COPY OF WHAT THEY AGREED TO. Asked four precise things: which partner (the site or promotion, not the category); on what date and from what IP or page URL; the EXACT consent language shown and whether the box was PRE-TICKED; and whether the transfer to WINR was NAMED or hidden behind 'carefully selected partners'. 'No record of the originating consent was retained' offered as a real answer I would record. Rationale given: their deletion cannot reach the partner feed, so the record arrives again on the next delivery unless the partner is named. GDPR ART 15(1)(g) invoked deliberately alongside CCPA -- WINR Data B.V. is established in the Netherlands and Art 15(1)(g) REQUIRES the source to be provided, not merely characterised. ON 'NON-SENSITIVE': taken in good faith, then limited -- identity resolution is definitionally the LINKING of identifiers to one person, and a unique/probabilistic identifier and an identifier graph are personal information under 1798.140(v)(1)(A) and (aj) whether or not any individual field is sensitive. The rights attach to THE LINK, not only the fields. REAL-WORLD CONSEQUENCE, which makes 1798.106 correction non-formal here: they supply IDENTITY VERIFICATION to fintechs, so a wrong record can cause a bank or payment provider to FAIL MY IDENTITY CHECK with neither side told the reason. Asked separately whether they have ever supplied an IDV/identity-resolution response about me, how many times and over what period -- a deletion going forward does not undo a wrong answer already given. Also pointed out that a company selling identity verification should be able to verify me from what I supplied, which is why no SSN and no ID scan. Twelve addresses individually AND hashed (MD5/SHA-1/SHA-256), with the four dead-service addresses flagged as likeliest because a prize-draw record is keyed to the address used THEN. Closed-mailbox caveat on [EMAIL] marked inline. COURTESY NOTE: their registered privacy-policy URL and site both sit behind a bot-challenge page, so a consumer following the CA register to their policy may not arrive. Raised as something they may not know, not as an accusation.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Verification link expired unclicked — resent by direct email (2026-09-15)

**Predicted outcome confirmed.** On 2026-09-15 WINR's DataGrail system sent:
*"We did not receive verification of your privacy request within the 7-day
verification period, so we were unable to process it."* Exactly the
CB Insights failure mode this file flagged as urgent on 2026-09-09 — the
request existed only as an unclicked SPA link and died silently on schedule.

**Do not resubmit through the same web form a second time** — it's the same
trap. Instead sent a fresh request directly to `privacyoffice@winrdata.com`
(the CA-registry-verified address, bypassing the DataGrail portal entirely),
explicitly asking for a written confirmation or reference number rather than
another verification link. Status held at `submitted`, changed 2026-09-15.
If this also produces only a portal link, this broker converts to
`manual_required` — email alone cannot close it if every route funnels back
through a SPA verification step nobody clicks in time.

## Direct-email route worked around the SPA trap (2026-09-15) — status `acknowledged`

`privacy@winrdata.com` (a human, not the DataGrail bot) replied same-day:
*"We have taken note of the confirmation in your email... We will manually mark
the request as verified and process it accordingly. Please ignore the
verification attempt that you'll receive afterwards."* So the fix for the
unclicked-SPA-link failure mode is exactly what was tried: email a human
address directly and ask them to bypass their own portal's verification step.

**A second, separate request ID (`0b38c45a`) also closed the same day** with
*"your request is actioned and resolved"* — no detail on what was searched or
found. Two different request IDs for the same person on the same day strongly
suggests a webform submission (possibly from the other agent working this
project, who cannot see this file) ran in parallel with the direct-email route.
Neither reply states which identifiers matched or what categories of data were
held, so this is recorded as `acknowledged` rather than `confirmed` — a
"resolved" notice is not itself the broker affirming what happened.
