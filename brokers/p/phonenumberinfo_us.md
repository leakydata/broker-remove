# Phonenumberinfo Us

- **Opt-out:** https://phonenumberinfo.us/contact.php
- **Email:** info@phonenumberinfo.us — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** phonenumberinfo.us
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-19)
- Note: No route of any kind. The only address published anywhere is info@phonenumberinfo.us, obfuscated behind Cloudflare email protection on both /privacy.php and /contact.php - and the domain publishes NO MX RECORD, so it cannot receive mail. Did not spend a send on it; a domain with no MX is undeliverable by definition and the DNS is conclusive. What makes this one worth writing up is the privacy policy: it promises 'a quick and easy process to allow individuals to remove their information from our People Search results, whether or not they are a user of the Site', and then the very next sentence reads in full: 'If you would like to opt out of our People Search results.' That is where it stops. No link, no address, no instruction - the sentence that should carry the route simply ends. Probing nine likely paths (/optout.php, /opt-out, /remove.php, /do-not-sell.php, /ccpa.php and others) returns the homepage every time, because the site serves a catch-all 200. So the promised process does not exist and the mailbox cannot be reached.

## Steps

**There is no route.** Recorded here so nobody spends
another hour finding that out.

1. `dig +short MX phonenumberinfo.us` returns **nothing**. The domain cannot
   receive mail, so no address at it can work.
2. The only address published anywhere is `info@phonenumberinfo.us`, hidden
   behind Cloudflare email obfuscation (`data-cfemail`) on `/privacy.php` and
   `/contact.php`. Decoding it just yields the same undeliverable address.
3. Every URL path returns the homepage — the site serves a catch-all 200 — so
   probing for an opt-out page produces nine false positives and no page.

## Gotchas

**The privacy policy promises a route and then stops mid-instruction.** In full:

> *"phonenumberinfo.us also provides a quick and easy process to allow
> individuals to remove their information from our People Search results, whether
> or not they are a user of the Site. If you would like to opt out of our People
> Search results."*

That is where the sentence ends. No link, no address, no next step. The paragraph
that exists to carry the removal route is a dangling conditional — the sort of
thing left behind when a template is copied and the link never pasted in.

> **A promised process is not a process.** Sites in this category are routinely
> catalogued as having an opt-out because their policy says so. The claim and the
> mechanism are separate things, and only one of them can be tested.

**Decoding a Cloudflare-obfuscated address is worth doing anyway.** `data-cfemail`
is a hex string XORed with its own first byte:

    b = bytes.fromhex(cfemail); key = b[0]
    addr = ''.join(chr(c ^ key) for c in b[1:])

Here it only confirmed the dead end, but on other sites it is the fastest way to
recover a contact that scraping for `@` will never find.

**Watch for catch-all 200s before trusting a path probe.** Nine plausible opt-out
paths all "existed". Compare page titles or content length, not status codes.

**Recorded `unreachable`, not `failed`.** No send was spent: a domain with no MX
is undeliverable by definition and the DNS is conclusive on its own. Revisit only
if they publish a working contact.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
