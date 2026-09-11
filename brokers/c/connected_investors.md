# Connected Investors

- **Opt-out:** https://firstam.service-now.com/x_farf2_dp_request_fa_connected_investor.do?sysparm_id=6d6e7e8edb3e3158665f182813961985
- **Email:** dataprivacy@connectedinvestors.com (verified)
- **Method:** web_form — Web form.
- **Domain:** connectedinvestors.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-19)
- Note: CORRECTION SENT. I had told them their links were 'corrupted in transit' and cited as proof that the damage appeared in both the plain-text and HTML parts. That argument is worthless: both parts reach me through the same retrieval path, so a fault there corrupts both identically and cannot distinguish their outbound mail from my inbound processing. They replied 'Both links are working links' and they are almost certainly right -- the same '=' plus two bytes corruption shows up in unrelated messages' boilerplate meta tags. Apologised and withdrew the claim. Their route is a First American ServiceNow portal (firstam.service-now.com/x_farf2_dp_request_ci_opt_out.do) keyed by a 32-char sysparm_id I cannot read. Asked them to either process from the thread (they hold every identifier already) or send the sys_id as plain unlinked text. Queued as a human click. Substantive asks re-stated: the motivated-seller/distressed CLASSIFICATION as the personal information, skip-traced appended contact data plus the vendor name, and which subscribers already received a lead.

## Steps

1. Email `dataprivacy@connectedinvestors.com`.
2. They reply routing you to a ServiceNow portal on **firstam.service-now.com**.
3. Check the links before clicking — see below, both were corrupted.
4. Ask for a resend as plain text, or for the request to be processed from the
   ticket. Phone 1-800-350-1502 exists but leaves no written record.

## Gotchas

The portal links arrive broken in both parts of the message, and the portal host
names the parent company. Both below.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## The hostname names the parent

Their rights portal is `firstam.service-now.com` — a **First American** ServiceNow
tenant, carrying Connected Investors branding inside it. The brand on the page is the
subsidiary; the hostname is the parent. See `_BROKER_FAMILIES.md`.

Worth using: ask First American to apply the request across the group rather than to
the one brand, and name the siblings you know about.

## Both links arrived corrupted

The `?sysparm_id=` separator had been replaced by a stray character, and at least one
further character eaten with it — leaving 30-character identifiers where a ServiceNow
sys_id is 32. In **both** the plain-text and HTML parts, which rules out reading the
wrong half and points at their outbound template.

Loading the bare form URL is the useful diagnostic: it reaches the portal, renders the
Connected Investors branding, and then shows an **empty red error banner with no
text**. That proves the endpoint is live and the parameter is the only thing missing,
which makes the fault report specific instead of "your link is broken".

Do not try to reconstruct the identifier. A wrong guess either 404s or lands on
somebody else's request.

## What this platform holds that a generic opt-out will miss

Connected Investors supplies "motivated seller" leads to investors. The three asks
that matter, and that a standard form will not cover:

  - the **classification itself** — distressed, pre-foreclosure, probate, vacancy,
    equity-based. That label is an inference about an identifiable person, it is what
    is actually being sold, and it survives the deletion of a bare contact record;
  - **skip-traced** phone numbers and emails appended to a property record, plus the
    vendor that supplied them;
  - **which subscribers already received a lead.** A record in an investor's list
    keeps generating calls, texts and mail long after the platform's copy is gone —
    the downstream copy is the one that actually reaches the person.

Property records are keyed to the address, so every prior address must be searched.


## I accused them of a fault that was mine (updated 2026-08-19)

Their reply routes consumers to a First American **ServiceNow** portal:

    firstam.service-now.com/x_farf2_dp_request_ci_opt_out.do?sysparm_id=<32 hex>

Read through the mail API, that `sysparm_id` arrives destroyed — the `=` and the
two bytes after it are gone, leaving 30 characters where a ServiceNow sys_id needs
32. The URL is unusable.

I told them the links were **"corrupted in transit"** and offered what I thought
was clinching evidence: the damage appears in *both* the plain-text and the HTML
parts, so it could not be my client reading the wrong half.

They replied, in full: **"Both links are working links."**

They were right, and my argument was worthless.

> **Both MIME parts arrive through the same retrieval path. A fault in that path
> corrupts both identically — so "it's broken in both parts" cannot distinguish
> the sender's outbound mail from my inbound processing.** It is exactly the
> question at issue, and I offered it as the answer.

The confirming evidence was available and I had already recorded it elsewhere:
unrelated messages arrive with boilerplate `<meta>` tags reduced from
`content="width=device-width"` to `content="width` + `<?>` + `vice-width"`. Same
signature — `=` plus two bytes — in text nobody at any broker wrote. See
[[_SILENT_FAILURES]] §48.

Withdrawn and apologised for.

### What actually unblocks it

The corruption happens before the URL reaches me, so no amount of care on their end
helps *me* directly. Two routes, both asked for:

1. **Process from the email thread.** They already hold every identifier a verified
   request needs — it was in the original message. A ticket containing the
   identifying detail does not obviously need a second submission through a form
   that collects the same detail.
2. **Send the `sysparm_id` as plain, unlinked text**, broken into groups so nothing
   auto-links it. The URL can then be assembled by hand.

Otherwise it is a human click on the original mail in a normal client — queued as
such. Telephone fallback **1-800-350-1502**, though a call leaves no written record
of what was asked or answered.

### The substance, still unanswered

Two rounds in, nothing has addressed the actual request. Worth restating each time,
because these are the parts a generic opt-out form does not reach:

- **The classification *is* the personal information.** A "motivated seller",
  distressed, pre-foreclosure, probate, vacancy or equity-based label is an
  inference generated about an identifiable person. It is the thing being sold, and
  it survives the deletion of a bare contact record.
- **Skip-traced contact details are not public record** — delete the appended
  number or address *and the linkage*, and name the vendor that supplied it.
- **Leads already distributed keep working.** A record in an investor's list
  generates calls and mail long after the platform's copy is gone.

Property records are keyed to the address, so every prior address must be searched.
