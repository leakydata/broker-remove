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
