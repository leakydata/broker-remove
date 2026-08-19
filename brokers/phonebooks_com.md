# Phonebooks Com

- **Opt-out:** https://www.phonebooks.com/opt-out
- **Email:** support@phonebooks.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** phonebooks.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Directory and reverse-lookup site. Keyed to numbers AND addresses, so the letter asks for removal in four directions rather than two: number-to-name, name-to-number, address-to-resident and resident-to-address. Also asked for household-member, relative, associate and PREVIOUS RESIDENT listings on other records, which is the directory-specific version of the relatives problem. Two questions: stored index or live pass-through from a supplier (if pass-through, an opt-out here buys nothing), and whether sibling sites share the index.

## Steps

1. **Do not email.** `support@` replies: *"This email address
   is dedicated to customer service inquiries and is not intended for
   privacy-related requests. We do not process privacy requests received via
   email."*
2. Of the three web routes they name, only one does anything:
   - `/opt-out` — **the real one.** CAPTCHA, then an emailed link (24h expiry),
     then a details form, then a confirmation page and email. 3 days to take
     effect.
   - `/do-not-sell` — notice page.
   - `/privacy-rights` — a dead end. See below.

## Gotchas

**The "Privacy Rights Form" has no submit button.** It is three cascading
dropdowns — *I want to access, delete, or correct my personal information* →
*Right to Delete* → *I have no direct relationship with the company* — and at the
end of that funnel there are no fields, no button, and no request. Just prose:

> *"Please note that state privacy laws... do not apply to all types of
> information. For instance, publicly available data is not included... while we
> cannot delete data held by third parties, you do have the option to prevent your
> information from appearing on our website."*

Three selections, then a refusal and a redirect to the opt-out. **A form that
cannot be submitted is not a form**, and this one exists to deliver an answer
rather than to take a request. See `_DEFLECTIONS.md`.

**They volunteer the pass-through claim** that other lookup sites have to be
asked for:

> *"the information you find is not stored by us. Instead, it is retrieved from
> third-party data providers at the time you perform the search."*

If that is true, the opt-out suppresses *display on their site* and the
underlying record sits with unnamed suppliers — which makes **"who are your
providers"** the question worth pressing, and makes any removal here narrower than
it sounds. Note the tension with their own opt-out page, which promises to *"remove
all your information from our site"* and asks for accurate details so they can
*"ensure we remove all your information"* — that is the language of a stored
record, not a live query.

**One point in their favour, worth recording as the counter-example.** Their
relationship dropdown includes **"I have no direct relationship with the
company"** — exactly the option Nielsen's rights form lacked, where every choice
presumed a prior relationship. It costs nothing and it is the difference between
a form a data subject can answer honestly and one they cannot.

**Cloudflare challenges `/opt-out` but clears itself** in about ten seconds. Wait
before concluding it is blocked.

**The `I am:` dropdown is a custom widget** that would not open under automation —
neither a ref click nor a coordinate click. Hand the flow to a human; the CAPTCHA
at step one makes that necessary anyway.

## Verification

Search the site for the name after 3 days. Given the pass-through claim, also
re-check a week later: if results are genuinely fetched live from suppliers, a
suppression on their side is the only thing standing between the query and the
answer, and it is worth confirming it holds.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
