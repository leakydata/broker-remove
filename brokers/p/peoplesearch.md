# Peoplesearch

- **Opt-out:** https://www.whitepages.com/privacy/ccpa
- **Email:** support@whitepages.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** peoplesearch.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Corrected route. support@whitepages.com, which peoplesearch.com publishes as its privacy contact, is an unmonitored autoresponder that redirects to a Zendesk form - so a consumer following peoplesearch.com's own privacy policy files nothing and gets a reply that reads like an acknowledgement. Re-raised on the existing Whitepages ticket #5402176 instead, asking them to extend it to peoplesearch.com or name the operator, and pointing out the broken published channel.

## Steps

Do not write to this site directly. It publishes **`support@whitepages.com`** as its privacy
contact — an address on another broker's domain — so a letter addressed to this
brand alone lands on somebody else's desk with no indication of what it covers.

1. Write **once**, to `support@whitepages.com`, naming every site that shares it:
   peoplesearch.com.
2. Ask which of the named properties actually held a record. A completion
   covering all of them with no detail does not say how many were searched.
3. Ask whether they operate the site at all. If they do not — if it merely
   references their address — ask **who does**. Either answer moves you forward.

See `_BROKER_FAMILIES.md` for how the grouping was found, and
`scripts/family_scan.py` to reproduce it.

## Gotchas

**A shared privacy address is the cheapest family signal there is.** It requires
no guesswork about corporate ownership, no WHOIS, no reading of terms: the site
has published, in its own privacy policy, the mailbox that handles it.

The practical consequence cuts both ways, and the second half is the one that
gets missed:

- **It saves letters.** One message naming every sibling is a single ticket with
  an unambiguous scope, instead of one ticket per brand, each re-verifying
  identity and each an opportunity to be refused.
- **It creates silent gaps.** A sibling your letter did not name is a sibling
  nobody removed — and in the tracker it looks exactly like one that was, because
  the request "went to the right address". Sharing a contact is evidence of a
  shared desk; it is not proof of a shared database, and no broker will volunteer
  that your request was narrower than you thought.

So name the brands. Do not rely on the address doing it for you.

## Verification

Verify per property, not per family. Re-run the public search on each named site
individually: a family index can be cleared centrally and still serve a cached
profile on one sibling, and that sibling is the one nobody will check.
