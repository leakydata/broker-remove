# Nexxa

- **Email:** consumerchoice@nexxagroup.com — delivers, auto-replies immediately
- **Method:** email, then a OneTrust webform their auto-reply points to
- **Domain:** nexxagroup.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Reference: `FKB6FMP7GL`
- Note: Email verification link clicked 2026-08-19; OneTrust confirmation page rendered under NEXXA branding: 'Your request is confirmed!'. Request type: Opt-Out: Do Not Sell/Share. Footer of the OneTrust mail exposes a real consumer contact obfuscated across two mailto tags: ConsumerChoice@nexxagroup.com, plus Consumer Choice +1-800-566-1895 on the confirmation page (the email footer prints 800-566-1217 -- two different numbers).

## Steps

1. Write to `consumerchoice@nexxagroup.com`. It delivers. The reply is automatic
   and arrives within seconds.
2. The auto-reply gives a OneTrust webform:
   `privacyportal.onetrust.com/webform/c02129bc-.../156ac96a-...`
3. On the form: **Myself** → **Opt-Out: Do Not Sell/Share Request** → Country
   *United States*. The name, address, city, state, ZIP, email and phone fields
   do not exist until those first choices are made — the form builds itself as
   you answer it, so a reader who screenshots the empty form will conclude it
   asks for far less than it does.
4. Submit is gated on a distorted-text CAPTCHA (BotDetect, not reCAPTCHA — it has
   a "speak the code" link as well as a refresh).

## Gotchas

**The form offers only one right, and it is not deletion.** Under "Select the
Rights You Want to Exercise" there is exactly one option: *Opt-Out: Do Not Sell/
Share Request*. There is no delete option anywhere on it.

This is worth stating plainly because of what it means in practice: a company can
publish a rights portal, point every incoming request at it, and still not offer
the right the requester asked for. A consumer who follows the auto-reply and uses
the form instead of pressing the emailed request has quietly downgraded their own
request from *delete* to *do not sell* — and has done so without ever being told
that is what happened. **Send the letter as well as using the form, and treat the
letter as the request of record.**

**The intro carries the processor hedge.** Their own welcome text: requests are
honored *"in accordance with applicable law and our contractual obligations with
our clients."* That is the sell-side/identity-platform pattern — the second half
of that sentence is doing the work, and it reserves the position that some of what
they hold is a client's data rather than theirs. Ask which hat they are wearing.

**The Acknowledgement asks the requester to attest to their own jurisdiction.**
*"I am confirming and acknowledging. I am a resident of United States and a
Resident of a State with applicable Privacy Laws."* Where the requester's state
has no comprehensive consumer privacy statute this is not a box to tick without
thinking, and it is not a call an agent should make on someone's behalf. Note it
and leave it to them. The emailed request needs no such attestation, which is
another reason it is the better route.

**Selected-state styling is not reliable across OneTrust tenants.** On Nielsen's
form the same control turns solid purple when chosen. On this one both buttons
stayed grey after being clicked, yet the dependent fields appeared — which only
happens when a selection registered. Do not read grey as unselected on a tenant
you have not seen before; read the appearance of dependent fields instead.

## Verification

No search page to re-check — this is a list/data business, not a people-search
site, so the only evidence available is what they say. Chase the ticket if no
substantive reply follows the automatic one.

## The verification click, and two different phone numbers (updated 2026-08-19)

The OneTrust request lodged earlier reached the email-confirmation stage. Clicking
**Confirm email** returned, under Nexxa branding:

> "Your request is confirmed! We will review your request and contact you shortly."

Request ID **FKB6FMP7GL**, request type *Opt-Out: Do Not Sell/Share Request*,
submitted on the `privacyportal.onetrust.com` (US) tenant.

> **A OneTrust request is not lodged until the confirmation link is clicked.**
> Until then the tenant holds it unverified and the clock does not start. The
> confirmation mail is the artifact worth keeping — it carries the request ID,
> and it is the only place the ID appears.

### The contact address hidden in the footer

The confirmation email's footer prints what looks like ordinary text but is
actually a mail address split across two `mailto:` anchors with a bare word
between them, so that a naive scrape reads "Consumer", "Choice", "@",
"nexxagroup.com" as four separate tokens. Reassembled it is:

    ConsumerChoice@nexxagroup.com

Worth having independently of the portal, because a portal request that stalls has
no reply-to.

> **Read broker footers as markup, not as text.** Addresses in this industry are
> routinely split across tags, reversed in CSS, or emitted from a `data-cfemail`
> attribute specifically so that the rendered page and the source disagree.

### And a discrepancy worth noting

The email footer gives **(800) 566-1217**. The confirmation *page* gives
**Consumer Choice +1-800-566-1895**. Two different numbers for the same function,
published by the same vendor on the same day. Neither has been called; the
mismatch is recorded because a consumer picking one at random has a coin-flip
chance of reaching a line nobody is watching.

See [[_SILENT_FAILURES]] on contacts that exist but do not work.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Nexxa Group, Inc.
- **Registered address:** 13300-56 S Cleveland Ave, #708, Fort Myers, FL
- **Filed contact email:** Consumerchoice@nexxagroup.com
- **Website:** https://www.nexxagroup.com

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
