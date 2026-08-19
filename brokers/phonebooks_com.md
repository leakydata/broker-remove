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

## The 24-hour single-use link, and grey text that is not a placeholder (updated 2026-08-19)

Support refuses privacy mail outright — "This email address is dedicated to
customer service inquiries and is not intended for privacy-related requests. We
do not process privacy requests received via email" — but it does something more
useful than most refusals: it *generates a link* and mails it to you.

> "Here are the final steps for completing your privacy request on phonebooks. If
> you waited longer than 24 hours to click the link below, you will need to start
> over and generate another link."

So the route is two-step and time-boxed: write to support, get a personalised
form URL, fill it within 24 hours. That is a good route — but see the mangling
note below, because the link can arrive damaged.

### The link carries a ticket id, and an email client can eat it

The emailed URL is of the form:

    /opt-out-removal?fn=<first>&mn=<middle>&ln=<last>&email=<addr>&ticketid=<id>

Two things went wrong with it.

**First, `mn=undefined`.** Not "empty" — the literal seven-character string
`undefined`, leaked from the site's own JavaScript into the query string and then
pre-filled into the Middle Name box. Left alone it would have been submitted as a
middle name.

**Second, the ticket id did not survive.** The mail retrieved through an API came
back with `ticketid` followed by a Unicode replacement character and then a
partial number. The same corruption appears in the message's own `<head>` —
`content="width<?>vice-width"` for `width=device-width`, `content="IE<?>ge"` for
`IE=edge` — so it is the transport eating `=` plus the next two bytes, not the
sender's fault.

> **When a link arrives through a machine reader, check it against a known-good
> string in the same message before trusting it.** A meta tag you can predict
> (`width=device-width`) is a free calibration test: if *that* is mangled, every
> other `=` in the message is suspect, including the one carrying your ticket.

The form loaded and accepted input with the ticket omitted entirely, so it is
worth trying the truncated URL before asking for a fresh link.

### Grey text here means "we filled this", not "this is a placeholder"

The four fields that came from the query string — first, middle, last, email —
render in grey (`#92959a`). Everything typed afterwards renders black. The
obvious reading is the usual trap: grey text is placeholder text, the field is
actually empty, and it will submit blank.

That reading is wrong here, and checking cost one line:

    Array.from(document.querySelectorAll('form input'))
         .map(i => ({n: i.name, v: i.value, ph: i.placeholder}))

Every grey field had a real `.value` and an **empty** `.placeholder`. The site is
using colour to mark *provenance* — these came from your verified link, those you
typed — which is the inverse of the convention.

> **Grey is not evidence. `.value` versus `.placeholder` is.** Check before
> retyping: re-entering a field that was already correct is harmless, but
> concluding "the form lost my name" and abandoning a 24-hour link is not.

### A real defect worth knowing about

The inputs collide on `name`. Three of them are `name="firstName"` (first, middle
*and* last), and two are `name="address"` (street *and* date of birth). Anything
serialising this form by field name rather than by DOM order loses data silently.
It does not appear to break the site's own submission, which presumably reads the
nodes positionally — but it means the form cannot be safely reconstructed from
its names alone.

### Where it stops

A reCAPTCHA sits between the last field and **Submit**. Everything above it can be
staged; the last click cannot. Fill it all, tick the certification box, and hand
off one action.

Fields: first, middle, last, email, phone, street address, date of birth, city,
state, zip, plus a certification checkbox. The page asks for **no punctuation** —
"for the name James Brown, Jr. please put 'Brown Jr'" — and the phone box
reformats a bare ten-digit string into `(555) 123-4567` form by itself.

See [[_SILENT_FAILURES]] for the wider family of fields that look filled and are
not, and for published routes that fail without a signal.
