# Connected Investors

- **Opt-out:** https://firstam.service-now.com/x_farf2_dp_request_fa_connected_investor.do?sysparm_id=6d6e7e8edb3e3158665f182813961985
- **Email:** dataprivacy@connectedinvestors.com (verified)
- **Method:** web_form — Web form.
- **Domain:** connectedinvestors.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-18)
- Note: Routes to a ServiceNow portal at firstam.service-now.com - FIRST AMERICAN. Connected Investors is a First American company; that tenant domain is the family signal. BOTH links in their email are corrupted: the sysparm_id separator is mangled and a character eaten, leaving 30-char ids where a ServiceNow sys_id is 32 - in the plaintext AND html parts, so not a client artefact. Loading the form bare reaches the portal, shows Connected Investors branding, then an EMPTY red error banner with no form and no explanation. Asked them to resend as plain text or process from the ticket, and to check whether the corruption is in their outbound template - if so every recipient gets a dead link and none can say why. Phone route 1-800-350-1502 exists but leaves no written record.

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

