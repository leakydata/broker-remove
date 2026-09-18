# Criminalrecords Com

- **Opt-out:** https://www.intelius.com/privacy-center
- **Email:** support@mailer.intelius.com (verified)
- **Method:** web_form — Web form.
- **Domain:** criminalrecords.com
- **Priority: 2.**

## Status

- Current: `covered_by_sibling` (updated 2026-09-07)
- Reference: `peopleconnect family suppression 2026-08-27; key set extended 2026-08-31`
- Note: RESOLVED 2026-09-06 AS AN INTELIUS-BRANDED FRONT END. The site says so itself, on its own About page: the service is described as "powered by Intelius", and the search, the report format and the FCRA disclaimer are Intelius. It is not an independent holder of records. THE PARENT IS ALREADY SUPPRESSED: PeopleConnect confirmed a family-wide suppression on 2026-08-27, applied in ONE ACTION across Intelius.com, InstantCheckmate.com, TruthFinder.com and USSearch.com, and Intelius extended the key set on 2026-08-31 to cover four further email addresses, six prior addresses including two PO boxes, and three prior phone numbers. THE CAVEATS THAT CAME WITH IT CARRY OVER TO THIS ROW UNCHANGED, and they matter more than the closure: (1) it is a DISPLAY SUPPRESSION, NOT A DELETION, and they explained why in architectural terms -- "background reports are compiled in real time via live calls to data providers... Because we do not retain reports, we cannot delete them"; (2) the suppression is keyed to a NAME SEARCH, so a lookup by phone, address or email may still surface a report; (3) PeopleConnect scoped it to "the people search sites within our corporate family that we control", and a powered-by brand is within that scope on the plain reading, but nobody at PeopleConnect has confirmed THIS domain by name. METHOD, so this is not mistaken for a bulk close: checked individually against the SILENT_FAILURES 390 test -- read what the site says it is. Three sites in this cluster say "powered by Intelius" on their own pages and are closed on that. The others sharing the same recorded route do NOT, and have been left open with their findings recorded rather than swept up in the same verdict.

## Steps

Do not write to this site directly. It publishes **`support@mailer.intelius.com`** as its privacy
contact — an address on another broker's domain — so a letter addressed to this
brand alone lands on somebody else's desk with no indication of what it covers.

1. Write **once**, to `support@mailer.intelius.com`, naming every site that shares it:
   criminalrecords.com, peoplefinder.com, publicrecords.com, reversephonelookup.com and snoopstation.com.
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
