# Searchsystems Public Records

- **Opt-out:** https://publicrecords.searchsystems.net/opt-out.php
- **Email:** webmaster@searchsystems.net — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** publicrecords.searchsystems.net
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-20)
- Note: NO WORKING CONTACT ROUTE AT ALL, verified three ways on 2026-08-20. (1) webmaster@searchsystems.net hard-bounces 550 5.1.1. (2) info@searchsystems.net - the address printed on their own /contact page and repeated in the page body - hard-bounces 550 5.1.1 as well; the domain has live Zoho MX and answers on 443, so this is a live domain with no live mailboxes (see _SILENT_FAILURES.md 65). (3) The contact form on /contact is decorative: document.forms.length is 0, there is no form element anywhere on the page, the SEND MESSAGE control is <button type="button"> with onclick null and no ancestor form, there are no hidden inputs, and the three inline scripts contain no addEventListener, fetch, XMLHttpRequest or any reference to the button or the field ids. Nothing is wired to it - this is 62, the pure-markup contact form, and it works for nobody. What remains is telephone only: (805) 574-9367 and toll-free 1-888-717-3223, trading as Search Systems SR LLC. Note also that the mismatch between the reason dropdown and a privacy request is real - the options are broken link, add a database, search help, Premium Search account, data correction, media, other - so 'Other' would be the only honest selection even if the form worked. Their privacy policy claims they do not sell or share personal information and the site is a directory of links to government sources rather than a name-keyed people index, so the honest ask here is narrow and the right outcome is probably a written confirmation that no person-level index exists.

## Steps

**Email is not a route here.** Both published addresses are dead:

| address | source | result |
|---|---|---|
| `webmaster@searchsystems.net` | aggregator listing | `550 5.1.1` |
| `info@searchsystems.net` | **their own /contact page** | `550 5.1.1` |

The domain is healthy — live Zoho MX, site answers on 443. Two 5.1.1 rejections
including the one they publish themselves means the domain accepts no mail at
all; do not spend a third send guessing local parts (`_SILENT_FAILURES.md` §65).

The remaining route is the **contact form** at `/contact` (fields `cf-name`,
`cf-email`), which is a plain form with real named inputs rather than the
decorative markup of §62.

## Gotchas

- **The contact form is decorative — it submits nothing.** Verified in the page,
  not inferred: `document.forms.length === 0`, no `<form>` element anywhere,
  the SEND MESSAGE control is `<button type="button">` with `onclick` null and
  no ancestor form, no hidden inputs, and the three inline scripts contain no
  `addEventListener`, `fetch`, `XMLHttpRequest`, or any reference to the button
  or to the field ids. This is `_SILENT_FAILURES.md` §62 — it works for nobody,
  so do not hand it off to a human either.
- **Check that before typing anything into it.** Fields that accept input and a
  button that highlights on hover are not evidence a request will be sent. One
  `javascript_tool` call settles it.
- **The reason dropdown has no privacy option.** Broken link, add a database,
  search help, Premium Search account, data correction, media, other. "Other"
  would be the only honest selection even if the form worked — do not pick
  "data correction" to make a request fit a menu.
- **The advertised opt-out URL is a redirect.** `publicrecords.searchsystems.net/opt-out.php`
  returns 200 but lands on `/privacy`. Check the effective URL, not the status.
- **Read what they actually are before writing.** Their policy claims they do
  not sell or share personal information, and the site is a directory of links
  to government sources rather than a name-keyed index of people. If that holds,
  the honest ask is narrow — server logs, contact-form submissions, and written
  confirmation that no person-level index exists. Asking a link directory to
  delete a profile it does not hold invites a truthful "we have no record of
  you" that costs a send and proves nothing (§52).

## Verification

Nothing name-keyed to re-check. The verification that matters is the negative
one: a written or spoken confirmation that no person-level index exists, which
converts this from `unreachable` to `not_found`. Telephone is the only channel
left — Search Systems SR LLC, 1-888-717-3223 or (805) 574-9367.
