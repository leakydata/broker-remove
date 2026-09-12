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

<!-- Replace once the route is confirmed. What actually worked, in order. -->

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
