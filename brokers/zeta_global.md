# Zeta Global

- **Email:** privacy@zetaglobal.com (verified)
- **Method:** unknown — Route not yet established.
- **Domain:** zetaglobal.com
- **Priority: 3.**

## Status

- Current: `manual_required` (updated 2026-09-05)
- Reference: `gmail:1a03f92bcd642f64`, `gmail:1a0708992bd2e4b2`
- Note: 2026-08-26: FIRST CONTACT, and the address was found rather than known. zeta_global was one of 280 Optery rows with no email and no opt-out URL - a lead, not a broker we could write to. discover_contacts.py found privacy@zetaglobal.com published as a linked mailto on their own privacy-policy page. Letter tailored to an identity-graph business: hash the twelve addresses yourself rather than concluding no-match from plaintext, delete the EDGES as well as the nodes since in an identity business the linkage is the product, separate collected from MODELLED attributes and delete the modelled ones, and say which of the two lists any retained suppression hash sits on. Their privacy page also names dpo@hewardmills.com, an outsourced DPO firm - correctly ranked below the first-party address but worth knowing if this thread stalls.
- Reply (2026-09-05, second letter): identical canned deflection to the first contact -- "These requests cannot be made through privacy@zetaglobal.com." Two named alternative routes, split by data type: (1) an email/PII-linked DSAR OneTrust webform (requires email verification) for delete/access/do-not-email requests, and (2) a *separate* cookie-rights page (zetaglobal.com/rights-request/) for cookie-linked data. California residents can also phone 1.866.709.0840. This is the standard "we don't accept privacy requests by email" deflection (see `_DEFLECTIONS.md`) -- the ungated second route exists and is named explicitly, so this is not a dead end, just not an email-completable one.

## Steps

1. Email privacy@zetaglobal.com first anyway -- worth trying, and the auto-reply itself surfaces the two form URLs in one message rather than requiring a form hunt.
2. For email-linked data: OneTrust DSAR webform at the URL in the auto-reply (private, tokenized per-recipient -- see handoff queue rather than reusing the link above). Requires email ownership verification.
3. For cookie-linked data: zetaglobal.com/rights-request/, a separate flow from step 2.

## Gotchas

- **Two separate forms for two data types.** Submitting only one (e.g. the DSAR form) leaves the cookie-linked profile untouched and vice versa -- both are needed for a full opt-out.
- **Canned auto-reply, not a human response.** The same boilerplate came back on both the first and second email; do not expect substantive engagement by continuing to write to the inbox.
- **Email verification required** on the DSAR form -- expect a confirmation-link step.

## Verification

No web-form completion attempted (email-only channel per this project's rules). Handoff queued for a human to complete both forms; re-check after the stated CCPA response window once submitted.
