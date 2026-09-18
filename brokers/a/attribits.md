# Attribits

- **Opt-out:** https://www.attribits.com/do-not-sell
- **Email:** compliance@allgoodmediagroup.com (verified)
- **Method:** web_form — Web form.
- **Domain:** allgoodmediagroup.com
- **Priority: 2.**

## Status

- Current: `replied` (updated 2026-09-08)
- Reference: `4x identical macro 00:05:17-20; attritbits.com still unregistered`
- Note: Route metadata for the entry above: their reply arrived by email reply, and my answer went by email reply to info@attribits.com. Recording --via separately because the substantive entry omitted it.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.attribits.com/do-not-sell
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `compliance@allgoodmediagroup.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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

## The mailto: that points at a domain which does not exist (updated 2026-08-19)

Their announcement bar publishes a contact address. The rendered text is correct.
The link is not:

    <a href="mailto:info@attritbits.com"><em>info@attribits.com</em></a>

    attribits.com    NS: dns1.registrar-servers.com   MX: aspmx3.googlemail.com
    attritbits.com   NS: (none)                       MX: (none)

Two letters transposed in the `href`, onto a domain with no zone at all. Read the
address and type it and the mail arrives; click it and it hard-bounces.

A neighbouring field in the same CMS record (`clickthroughUrl`) holds the correct
`mailto:info@attribits.com`, so this is a data-entry slip, not obfuscation.

> **Harvest contact addresses from the `href`, not from the rendered text — then
> check that the domain resolves.** Here the two disagree, and only a `dig NS` on
> each says which side is wrong.

See [[_SILENT_FAILURES]] §61.

## Routes

- `compliance@allgoodmediagroup.com` — the contact already on file, apparently a
  parent or agency address rather than the brand's own.
- `info@attribits.com` — **the working address**, typed rather than clicked. Worth
  using as a second route, and worth telling them the link is broken while doing
  so.

Their privacy page carries no dedicated privacy mailbox, so `info@` is the whole of
the brand-level route.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Attribits
- **Registered address:** 881 Worcester St Ste 1, #1089, Natick, MA,
  01760
- **Filed contact email:** compliance@allgoodmediagroup.com
- **Filed phone:** 6179917065
- **Website:** attribits.com

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
