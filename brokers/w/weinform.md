# Weinform

- **Email:** support@weinform.org
- **Opt-out:** https://www.weinform.org/api/helper/optOutLight/search
- **Method:** email, with a bot-gated self-service form as the documented alternative
- **Domain:** weinform.org
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-20)
- Note: CONFIRMED 2026-08-20 (UTC 00:38-00:46). Reply to the single sixteen-site family letter, from support@weinform.org: 'From the information you provided, we have removed your information from our database at https://www.weinform.org'. Four siblings answered inside eight minutes of each other with a byte-identical template differing only in the brand name and the URL - which is itself further evidence of one operator behind the optOutLight platform. Note what the template does NOT do: it scopes the confirmation to its own hostname, ignores the request to treat the letter as covering all sixteen, and answers none of questions a-e (suppression vs one-time, one-record-per-request, relatives/associates cross-listing, criminal/inmate/mugshot entry sources, FCRA scoping). It also pre-explains any residual listing as either an unresolved duplicate or the reader's browser cache - a framing that converts an incomplete removal into the consumer's problem. Verification due; verify against the live site, not the cache.

## Steps

Email alone was sufficient — **no form, no account, no CAPTCHA, no ID**.

1. Write to `support@weinform.org`.
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
  our database at https://www.weinform.org" and silently ignores a request framed as
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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** We Inform LLC
- **Registered address:** 7860 W Commercial Blvd #829, Lauderhill, FL
- **Filed contact email:** support@weinform.org
- **Website:** https://www.weinform.org

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
