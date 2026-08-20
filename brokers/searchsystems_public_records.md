# Searchsystems Public Records

- **Opt-out:** https://publicrecords.searchsystems.net/opt-out.php
- **Email:** webmaster@searchsystems.net — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** publicrecords.searchsystems.net
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-20)
- Note: ALL THREE PUBLISHED ROUTES ARE DEAD. (1) webmaster@searchsystems.net -> 550 address not found. (2) info@searchsystems.net, printed on their own Contact page -> 550 5.1.1 address not found. Domain has live Zoho MX, so mail is accepted for the domain and refused at the mailbox. (3) The Contact page form is DECORATIVE: there is no <form> element on the page at all, the Send Message control is <button type='button'> with onclick null, and no script references the field ids. Filling it and clicking Send makes no request of any kind and produces no error -- the page simply sits. Only remaining routes are two telephone numbers, (805) 574-9367 and 1-888-717-3223. MITIGATING: their own homepage FAQ states unprompted that they hold nothing -- 'SearchSystems.net is a directory - it links you directly to the official government source where records are maintained. We do not aggregate, scrape, or resell personal information.' So the practical exposure is likely nil; what is unreachable is the ability to have that confirmed.

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
