# Unearth Campaigns

- **Email:** Privacy@UnearthCampaigns.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** unearthcampaigns.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-20)
- Note: Email route refused, portal route found and staged 2026-08-20 09:40 UTC. Their autoresponder from privacy+noreply@unearthcampaigns.com: 'we are no longer able to process privacy requests submitted by email' - pointing at an online form and a toll-free number, 855-456-2646. The form is a KETCH privacy centre, and reaching it is not obvious: the rights-section links in the privacy policy are javascript:void(0) handlers that open a modal, so navigating to the #rights anchor renders nothing useful and a scripted fetch of the page finds no form at all. Path: /privacy-policy/#rights, click 'Submit a Privacy Request', Requests tab, 'Delete your data'. The form has a free-text Request Details box, which is the useful part - the whole identifier set and the modelled-layer argument went in there rather than being lost to a name-and-email-only intake. Left for the human: a declaration under penalty of perjury, and Submit. reCAPTCHA is invisible v3, nothing to solve. NOTE the email autoresponder itself is a null route: privacy+noreply@ accepts mail and processes nothing, so a request sent there and not followed up looks identical to a pending one.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Unearth Campaigns, LLC
- **Registered address:** 555 Capitol Mall, Suite 640, Sacramento, CA
- **Filed contact email:** privacy@unearthcampaigns.com
- **Website:** https://www.unearthcampaigns.com

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
