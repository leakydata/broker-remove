# Unearth Campaigns

- **Email:** Privacy@UnearthCampaigns.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** unearthcampaigns.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: Sent 2026-08-20 09:15 UTC to Privacy@UnearthCampaigns.com. FIRST LETTER WRITTEN IN THE SHORT PLAIN REGISTER after _DEFLECTIONS.md 42 - no bold, no headers, no numbered ask-list, no em dashes, short sentences, about 350 words of argument instead of 700. Unearth Campaigns LLC, offices in Washington DC and Sacramento; political/advocacy campaign data. Their privacy policy is JS-rendered so no address could be scraped; the registry address was unverified but the domain has Google MX, so a bounce would be recoverable. Substance unchanged from the True Blue letter: concede the state voter file, target the modelled layer (partisanship, ideology, turnout and persuasion models, issue affinity, donor capacity, inferred religion and ethnicity), and press suppression because states republish the file on a cycle. Kept the 'if you only do one-time deletions, just say so, that is a useful answer' construction, which survives the shortening because it is a sentence rather than a structure.

## Steps

**Email is refused outright.** Their autoresponder:

> "we're no longer able to process privacy requests submitted by email"

and points at an online form or a toll-free number. Note the sending address is
`privacy+noreply@` — it accepts mail and processes nothing, so a request sent
there and never followed up is indistinguishable from a pending one.

Reaching the form is not obvious, and a scripted fetch of the page will tell you
there is no form at all — `document.forms.length` is 0 because the rights links
are `javascript:void(0)` handlers that open a **Ketch** modal:

1. `https://www.unearthcampaigns.com/privacy-policy/#rights`
2. Click **Submit a Privacy Request** (the anchor alone renders nothing useful)
3. **Requests** tab
4. **Delete your data**

## Gotchas

- **The free-text "Request Details" box is the whole value here.** Everything
  else is name, email, country, state. Put the full identifier set and the
  substantive argument in that box — otherwise a political-data request gets
  scoped to one name and one email address, which will match almost nothing in a
  voter file keyed to old registration addresses.
- **The declaration is under penalty of perjury.** Stage it and hand off; that
  attestation belongs to the person.
- **reCAPTCHA here is invisible v3** — the badge text at the foot of the form is
  the only sign of it. Nothing to solve, so this is a one-click handoff rather
  than a CAPTCHA handoff.
- **The cookie banner is notice-only** ("I understand"), with no reject option
  and nothing to consent to. Leave it; it does not block the form.
- **`document.forms.length === 0` on the policy page is a false negative here.**
  Unlike §62, the form does exist — it is inside a modal that has not been
  opened yet. Check for `javascript:void(0)` rights links before concluding a
  page has no route.

## Verification

No public profile. The observables are the Ketch confirmation, and their answer
on suppression versus one-time deletion — asked in the form in the phrasing that
makes "we only do one-time deletions" an acceptable answer.
