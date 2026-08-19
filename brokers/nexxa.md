# Nexxa

- **Email:** consumerchoice@nexxagroup.com — delivers, auto-replies immediately
- **Method:** email, then a OneTrust webform their auto-reply points to
- **Domain:** nexxagroup.com
- **Priority: 2.**

## Status

- Current: `captcha_blocked` (updated 2026-08-19)
- Letter delivered and acknowledged. Form filled and verified; a distorted-text
  CAPTCHA is the only thing left, staged for one human click.

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
