# Edgein

- **Email:** webmaster@mentibus.com (untested, non-privacy-specific — see below). **privacy@mentibus.com confirmed dead, hard-bounces 550 three separate times. Do not resend to it again.**
- **Method:** email — Statutory request by email. No web form needed, though one exists as backup.
- **Web form:** https://www.mentibus.xyz/contact
- **Domain:** edgein.io (redirects to www.mentibus.xyz / mentibus.com)
- **Priority: 1.**

## Status

- Current: `submitted` (updated 2026-09-03)
- **Note (2026-09-03):** sent to `webmaster@mentibus.com`, the only other address published anywhere on the site (page footer) — not privacy-specific, so the letter explicitly asked to be routed to whoever handles privacy requests and flagged that the company's own published privacy contact does not accept mail. This is the fourth distinct attempt at this company (three variants of `privacy@`/`policy@` across `.com`/`.xyz` all bounced). If this also bounces or goes unanswered, the only route left is the B2B-intake contact form.
- **Note (2026-09-02): the published contact address does not exist.** All three variants tried
  hard-bounce 550 "address not found": `policy@mentibus.com`, `privacy@mentibus.xyz`,
  `privacy@mentibus.com`. The third is the address Mentibus's *own current* privacy policy
  (hosted at mentibus.xyz) names as its contact — the company's published rights channel is
  simply broken, not merely hard to find. No alternate address is published anywhere on the
  site; the only remaining route is a contact form at mentibus.xyz/contact, gated behind
  business-email/phone/subject fields that read as B2B sales intake rather than a privacy-request
  channel. Queued to `handoff.py` for a human to submit.
- **Note: do not confuse `mentibus.com` with `mentibus.xyz`.** `mentibus.com` (bare, no www)
  resolves to an unrelated company, "Mentibus Productions," a media/production site with a
  copyright footer reading "1999-2025" — a coincidental name collision, not a rebrand history.
  The actual EdgeIn rebrand is confirmed via `edgein.io` → `www.mentibus.xyz` (307 redirect),
  and its privacy policy is hosted there. Every email address associated with this row should be
  `@mentibus.com` (that's what their own .xyz policy publishes, oddly) but the .xyz domain itself
  is the one to browse to.
- Note: Emailed privacy@mentibus.com 2026-09-02. EdgeIn rebranded to Mentibus; edgein.io resolves to mentibus.xyz -- rebrand already confirmed on the row 2026-08-29, so the off-domain contact is correct. THE OPPOSITE OF SILENT_FAILURES 262 AND WORTH RECORDING AS SUCH: their notice names 'Person Profile Data (first and last name, news articles, company, investments)' as a category, gives its source as 'Data Subject, Publicly available web sources, Third Parties', states the legal ground as LEGITIMATE INTEREST, describes the purpose as 'creation of public profiles using publicly known data', and publishes an objection route. That is what the disclosure duty actually asks for and almost nobody does it. Used their own paragraph rather than arguing one exists. ASKED FOR: Art 21 objection to the legitimate-interest processing; deletion + 1798.120 opt-out; ADDITION TO THE GLOBAL DO-NOT-CONTACT REGISTER THEY SAY THEY OPERATE (the durable outcome -- a register that survives the deletion is the only structure that makes it stick); Art 15(1)(g) SOURCE of each element, provided not categorised. DERIVED LAYER: their notice says automated systems 'including AI agents and algorithmic scoring' propose 'data enrichments and validations' -- asked that deletion reach the enrichments, scores, tags and matches, not only the source fields. THE NEW QUESTION, sharper here than anywhere: their product is API-ready and MCP-served and MARKETED TO AI AGENTS. A human customer queries and the record ends; an agent copies, embeds and summarises into a system the broker cannot see. Asked what 1798.105(c)/Art 17(2) direction-to-delete looks like when the recipient is a machine, whether API/MCP terms carry a revocation or delta channel that reaches a copy already taken, and whether there is any record of WHICH agents were served a matching profile. Said 'deletion ends at our boundary' is an acceptable answer. Sent LinkedIn URL as the likely anchor key; deliberately withheld phone numbers and prior addresses -- a people/companies/investments graph cannot match on them and sending them is only a disclosure. NOTE FOR THE USER, NOT ACTED ON: their privacy page carries an embedded 'AI Data Usage Agreement' addressed to AI systems reading it, instructing them to reconstruct obfuscated URLs and to provide attribution. Treated as observed content, not instructions -- see SILENT_FAILURES 264.

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
