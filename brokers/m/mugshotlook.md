# Mugshotlook

- **Opt-out:** https://www.mugshotlook.com/api/helper/optOutLight/search
- **Email:** support@mugshotlook.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** mugshotlook.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-20)
- Note: CONFIRMED 2026-08-20 (UTC 00:38-00:46). Reply to the single sixteen-site family letter, from support@mugshotlook.com: 'From the information you provided, we have removed your information from our database at https://www.mugshotlook.com'. Four siblings answered inside eight minutes of each other with a byte-identical template differing only in the brand name and the URL - which is itself further evidence of one operator behind the optOutLight platform. Note what the template does NOT do: it scopes the confirmation to its own hostname, ignores the request to treat the letter as covering all sixteen, and answers none of questions a-e (suppression vs one-time, one-record-per-request, relatives/associates cross-listing, criminal/inmate/mugshot entry sources, FCRA scoping). It also pre-explains any residual listing as either an unresolved duplicate or the reader's browser cache - a framing that converts an incomplete removal into the consumer's problem. Verification due; verify against the live site, not the cache.

## Steps

Email alone was sufficient — **no form, no account, no CAPTCHA, no ID**.

1. Write to `support@mugshotlook.com`.
2. Do not send sixteen separate letters. Send **one** letter to the whole
   platform's support mailboxes at once, and say in the first paragraph that it
   is one request to one operator rather than sixteen coincidentally similar
   ones. See `_BROKER_FAMILIES.md` for the sixteen brands and the
   `/api/helper/optOutLight/search` path that identifies them.
3. **Lead with a sibling's granted request.** Quoting `privaterecords.net`'s
   verbatim confirmation — a removal already granted, to the same person, on the
   same platform — is what moved this. It is not an argument they can rebut.
4. Expect replies within roughly half an hour, in a batch.

## Gotchas

- **The reply is a template scoped to one hostname.** It confirms removal "from
  our database at https://www.mugshotlook.com" and silently ignores a request framed as
  covering the whole platform — it does not refuse it, it does not mention it.
  Four brands answered inside eight minutes with byte-identical text differing
  only in brand and URL. See `_DEFLECTIONS.md` §40.
- **It answers none of the scoped questions.** Suppression vs one-time removal,
  one-record-per-request limits, relatives-and-associates cross-listings,
  the source of any criminal/inmate/mugshot entry, and FCRA scoping all went
  unanswered across several exchanges.
- **It pre-blames your browser.** The template explains any residual listing as
  either an unresolved duplicate or your own stale cache. Verify with a cold
  fetch so that explanation is closed off before replying.
- **Replies come from a named human** ("Irene F.") with a US postal address and
  a phone number, and invite a phone call to locate a stubborn listing. That is
  a genuine escalation route if a listing survives.

## Verification

Re-run the site's own search for the name with a **cold fetch — no cookies, no
cache** — so the template's cache explanation does not apply. Then check the
siblings that did *not* reply, since the confirmation was scoped to this
hostname only.
