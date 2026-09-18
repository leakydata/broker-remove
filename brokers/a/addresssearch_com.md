# Addresssearch Com

- **Opt-out:** https://www.addresssearch.com/remove-info.php
- **Method:** web_form — Web form.
- **Domain:** addresssearch.com
- **Priority: 2.**

## Status

- Current: `failed` (updated 2026-09-08)
- Reference: `positive control: Smith/PA and a nonsense surname both return no results`
- Note: RE-CHECK ATTEMPTED 2026-09-08 AND IT CANNOT SETTLE ANYTHING -- the search fails its own positive control. This row's note had set the next step: 'write to them about the 500, and re-check the directory by name/address in a few days -- that search is the only thing that can settle whether any of it took effect.' The re-check was due and was run. WHAT WAS DONE: found the real search endpoints from their own home page -- results.php with type=forward for a name lookup and type=address for an address lookup, the type parameter being required and a query without it falling through to an EMAIL lookup that reports the address 'doesn't seem valid'. Ran the subject's name filtered to PA, and the current address. Both returned 'no results'. THEN THE CONTROL, before believing it (SILENT_FAILURES 289): searched the surname SMITH in Pennsylvania, and a nonsense surname, through the same endpoint. ALL THREE RESPONSES ARE THE SAME -- 'no results', zero result links, and page lengths of 1406, 1408 and 1425 characters. The engine returns nothing to this client FOR ANYBODY. So the nil on the subject's name is an artefact of the client, not a fact about the directory, and it establishes nothing about whether the sixteen submissions took effect. Recording that plainly rather than as a removal. THE ROW THEREFORE STANDS AT: sixteen submissions on 2026-09-05, every one returning HTTP 500 behind a page reading 'Your information has successfully been removed', and no way to verify from outside. The only remaining route to ask them about the 500 is the contact form at contact.php, which is blocked on a distorted-text CAPTCHA and is staged in full at outbox/staged/addresssearch_contact.txt. Re-verification here belongs in the batched browser handoff, alongside the other twenty-four people-search rows (SILENT_FAILURES 409) -- a real browser may get results where this client gets none.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.addresssearch.com/remove-info.php
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

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
