# DMAchoice (direct mail)

- **Opt-out:** https://dmachoice.thedma.org/
- **Method:** account_required — **and this is why the row is open.**
- **Priority: 4.**
- **Fee:** $6, covering direct-mail marketing broadly.

## Status

- Current: `manual_required` (updated 2026-09-16)
- Note: Adopted from the shared ledger: another agent recorded 'manual_required' on 2026-09-06. No detail is carried across — re-read the broker's own reply before relying on this.

## Steps

<!-- Only if the subject says yes. Do not do this unprompted. -->

1. He creates the account himself at https://dmachoice.thedma.org/ and pays the
   $6. I do not create accounts with brokers and do not handle payment details.
2. Registration covers direct-mail marketing for ten years and is keyed to
   name and address.
3. Record the expiry date in `data/reverify.json` — a ten-year registration that
   nobody diarises is a nine-year protection and a silent lapse.

## Gotchas

- **What it is and is not.** DMAchoice is a mail-preference service run by the
  DMA's successor body. It asks participating mailers to stop sending to a
  registered name and address. It is a **preference registration, not a
  deletion**: the brokers still hold the record, and a non-participating mailer
  is unaffected. It is worth having and it is not what a §1798.105 request is.
- **It is address-keyed, so it does not follow the person.** Moving house ends
  the protection without notice, and each prior address would need its own
  registration — which is not something to do, since other people live at those
  addresses now (the same limit every letter on this project states).
- The ten-year term makes this the longest-dated item in the project. It is the
  one most likely to lapse unnoticed, which is exactly why the expiry belongs in
  `reverify.json` on the day it is registered and not later.

## Verification

None available from outside — there is no public list to check. The account's
own dashboard is the only record, which is a further reason the expiry has to be
diarised locally rather than trusted to a login nobody will make again for a
decade.
