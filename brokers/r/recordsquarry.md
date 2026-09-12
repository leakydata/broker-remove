# Recordsquarry

- **Opt-out:** https://www.truthfinder.com/opt-out/v2/submit/
- **Email:** help@truthfinder.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** recordsquarry.com
- **Priority: 2.**

## Status

- Current: `replied` (updated 2026-09-07)
- Reference: `gmail:1a079bb74d838606`
- Note: QUESTION PUT TO PEOPLECONNECT 2026-09-06, one letter covering all seven rows in this cluster rather than seven investigations. Their suppression was scoped to 'the people search sites within our corporate family that we control', and whether this domain sits inside that phrase is a question only they can answer. Asked for one of three answers per domain, any of which closes the row: (a) within the family and already covered by the suppression -- close, write nothing further; (b) an affiliate or referral site holding no records of its own -- nothing to suppress, close; (c) an independent operator they have no relationship with -- write to them separately and do not trouble PeopleConnect again. Told them plainly that the only evidence linking these seven to them is that all seven point at TruthFinder's opt-out page, and that AN OUTBOUND LINK TO AN OPT-OUT PAGE IS NOT PROOF THAT THE LINKING SITE IS THEIRS, which is why the question is being asked rather than the answer assumed. Also told them what was checked first: criminalrecords.com, snoopstation.com and peoplefind.com say 'powered by Intelius' on their own pages and have been closed as covered; these seven say no such thing, two carry affiliate disclosures pointing toward (b), and three say nothing at all. The three standing caveats were restated as carried forward rather than re-argued -- display suppression not deletion, keyed to a name search only, and coverage stated at family level rather than domain by domain. See SILENT_FAILURES 391.

## Steps

Do not write to this site directly. It publishes **`privacy@truthfinder.com`** as its privacy
contact — an address on another broker's domain — so a letter addressed to this
brand alone lands on somebody else's desk with no indication of what it covers.

1. Write **once**, to `privacy@truthfinder.com`, naming every site that shares it:
   instantcheckspy.com, recordsquarry.com and sheriffsdepartment.net.
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
