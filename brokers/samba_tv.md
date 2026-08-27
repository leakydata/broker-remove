# Samba TV, Inc.

- **Email:** privacy@samba.tv (correct address, confirmed by a Samba TV employee)
- **Email fallback (wrong personal mailbox):** [named individual]@samba.tv — the address on their CA data broker registration is a named individual, not a role address
- **Method:** web — email reaches the right desk, but they route every request to a
  OneTrust DSAR form for email verification.
- **Opt-out:** https://privacyportal-cdn.onetrust.com/dsarwebform/87c5ee85-893d-4972-ba26-2e82b743d041/d84d9664-facb-4de3-85fd-a2e339b73dbf.html
- **Domain:** samba.tv
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-27)
- Note: 2026-08-26: emailed [named individual]@samba.tv (the CA registration contact). Named ACR data explicitly: viewing history, channel/programme tuning data, household device graphs, ad exposure/attribution events, and asked which TV manufacturer or platform supplied their data.
- Note: 2026-08-26: Mr. Sekhon (Director of Data Governance) replied personally that this is his individual mailbox, not the privacy-rights address, named privacy@samba.tv as correct, and said he was transferring the request to their portal. Resent the same letter directly to privacy@samba.tv 2026-08-27 to have a written record at the correct address regardless of what the internal portal transfer does.

## Gotchas

- **The CA registration lists a named employee, not a role address.** Confirmed with a real reply rather than a bounce — a different failure mode from the usual dead-mailbox pattern, but the same fix: find the actual privacy-team address on the company's own site or from whoever answers.

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


## The verification gap, and why it matters here

`privacy@samba.tv` reached the real privacy team on the first try (ticket #345295),
which closes out the registry correction: the filed contact was a named employee, and
he replied himself to say so. The role address was there all along, just never filed
(`_SILENT_FAILURES.md` §88).

Their reply routes to a OneTrust form that **verifies control of the email address
you submit**. That is an ordinary and reasonable verification step. But it comes
apart from the lookup in a way specific to this kind of company:

> **Samba TV's records are keyed to a television, not to an email address.**

Automatic content recognition identifies what is on a screen. The resulting
observations attach to a device, and from there to a household. So confirming you
control an email address proves *who you are* without necessarily locating *what they
hold* — and if you have never had a Samba account, the verified address may match
nothing at all while the household's viewing history sits under a device identifier
you cannot supply.

That is the Foursquare pattern from §127 in a different medium: a working process
attached to a key the consumer does not have. The difference is that here the
verification step and the lookup key have simply come apart from each other, rather
than both resting on an unobtainable identifier.

## Steps

1. Complete the OneTrust form as the **consumer**, using the address you actually
   read, and click the confirmation it emails.
2. In the free-text field, ask for the things the form has no box for:
   - **viewing history and ACR observations**, not just account data;
   - the **household graph** entry linking the television to people and devices;
   - any **inferred audience segments** built from viewing;
   - **forward-looking suppression**, so the set is not re-enrolled at the next sync.
3. Ask the question plainly: **if I have never had an account, what does the verified
   email match against?** Ask whether they can search by household address instead —
   and ask them to report matches before deleting, because a household television is
   shared and other people's viewing is not yours to remove.

## Gotchas

Do not write to the address on their California registration. It is a named
employee's mailbox, he is still there, and he will politely redirect you — which
costs a round trip and puts a stranger's inbox in the loop for no reason.
