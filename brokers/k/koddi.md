# Koddi, Inc

- **Email:** dataprivacy@koddi.com — accepts mail but the replies are an autoresponder.
- **Method:** web_form — `koddi.com/dsr-form` is the only route that reaches a human.
- **Domain:** koddi.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-09-03)
- Note: WEDGE TESTED AND REFUSED, AND I SAID I WOULD STOP -- SO I AM STOPPING (SILENT_FAILURES 290/295). The 1798.120 letter drew the same macro back from dataprivacy+noreply@koddi.com, addressed 'Dear Privacy Team' (a template artifact -- it is addressed to ME as the privacy team). It states the position I asked for: 'we are unable to accept privacy rights requests via email'. That is a clear statement of policy, I undertook to record it and stop asking, and this row is now form-only. THREE REQUIREMENTS RESTATED IN THE MACRO, ALL OF WHICH A CONSUMER STRUCTURALLY CANNOT MEET, recorded because the pattern matters more than this row: (1) 'we do not process consumer information submitted as ALIAS EMAIL ADDRESSES' -- which excludes anyone using a plus-address or a forwarding service, and is unfalsifiable from outside since only Koddi decides what counts as an alias; (2) 'or UNHASHED NAMES' -- they will not accept a name unless it is hashed, which is not an operation a consumer can perform in the format a company uses, and hashing one's own name is not a thing anyone does; (3) 'we require the specific email address associated with your DIGITAL COMMERCE ACTIVITIES to identify you within our records' -- an identifier only they can determine, since which of twelve addresses appears in their file is precisely what the request exists to find out. That is the 260 shape at its sharpest: every one of the three is a requirement whose answer is held by the company and demanded of the requester. Form remains queued.

## Steps

**Do not email follow-up questions — they go nowhere.** Go straight to
`https://koddi.com/dsr-form`. Their auto-reply states three requirements
worth knowing before filling it in (verbatim, unclear in places — see
Gotchas): no unhashed names, no "alias" email addresses, and a "specific
email address associated with your digital commerce activities."

## Gotchas

**`dataprivacy+noreply@koddi.com` is a template autoresponder, confirmed by
direct test.** Two different threads to this address — a fresh submission and
a detailed follow-up asking it to clarify its own stated requirements — both
got back byte-for-byte the same canned paragraph. It does not read the
incoming message; it fires on receipt. Recognise the pattern generally: a
sender address with a `+noreply` local-part suffix is a strong signal this
will happen (see also `kargo_global.md` and `pmg_worldwide.md` — same
canned-template shape, possibly the same vendor).

**Their stated requirements are stricter than they can mean literally.**
"We do not process ... unhashed names" and "Alias Email addresses" are hard
to satisfy as written — a consumer cannot hash a name the same way Koddi's
system does without knowing their salt/normalisation, and "alias" is
undefined (does it mean an ordinary but no-longer-used mailbox, or only
relay/masking services?). Worth asking directly on the web form's free-text
field if one exists, since email won't get an answer.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Koddi, Inc
- **Registered address:** 2845 W 7th St, Fort Worth, TX, 76107
- **Filed contact email:** dataprivacy@koddi.com
- **Filed phone:** 8187258248
- **Website:** http://www.koddi.com

*Source: `data/registries/registry.csv`.*

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
