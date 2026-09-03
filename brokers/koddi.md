# Koddi, Inc

- **Email:** dataprivacy@koddi.com — accepts mail but the replies are an autoresponder.
- **Method:** web_form — `koddi.com/dsr-form` is the only route that reaches a human.
- **Domain:** koddi.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-28)
- **2026-09-03 (§296):** WEDGE TESTED AND REFUSED, AND I SAID I WOULD STOP -- SO I AM STOPPING (SILENT_FAILURES 290/295). The 1798.120 letter drew the same macro back from dataprivacy+noreply@koddi.com, addressed 'Dear Privacy Team' (a template artifact -- it is addressed to ME as the privacy team). It states the position I asked for: 'we are unable to accept privacy rights requests via email'. That is a clear statement of policy, I undertook to record it and stop asking, and this row is now form-only. THREE REQUIREMENTS RESTATED IN THE MACRO, ALL OF WHICH A CONSUMER STRUCTURALLY CANNOT MEET, recorded because the pattern matters more than this row: (1) 'we do not process consumer information submitted as ALIAS EMAIL ADDRESSES' -- which excludes anyone using a plus-address or a forwarding service, and is unfalsifiable from outside since only Koddi decides what counts as an alias; (2) 'or UNHASHED NAMES' -- they will not accept a name unless it is hashed, which is not an operation a consumer can perform in the format a company uses, and hashing one's own name is not a thing anyone does; (3) 'we require the specific email address associated with your DIGITAL COMMERCE ACTIVITIES to identify you within our reco
- **2026-09-02 (§290):** OPT-OUT WEDGE SENT 2026-09-02 (SILENT_FAILURES 290). This company refuses email as a channel and designates a web form. Rather than argue the channel, pressed the ONE RIGHT THE FORM IS NOT A PREREQUISITE FOR: 1798.120 opt-out of sale and sharing REQUIRES NO VERIFICATION OF IDENTITY -- the CCPA regulations are explicit that a business shall not require a consumer to verify themselves as a condition of honouring one, because requiring proof of identity to stop a sale would defeat the right. And there is nothing to verify: the consumer is not asking to receive data or alter a record, only to be excluded, so A WRONGLY-HONOURED OPT-OUT DISCLOSES NOTHING AND HARMS NO ONE -- which is exactly why the regulations treat it differently from access and deletion, where a mistaken match hands one person's information to another. Asked for the position IN WRITING if they disagree, explicitly not to arg
- Note: 2026-08-28: Emailed dataprivacy@koddi.com, got the canned "use our web form" autoreply, and sent one follow-up asking three specific clarifying questions about their stated submission requirements. The follow-up got back the **exact same canned paragraph, verbatim**, ignoring every question asked. Confirmed this is a template autoresponder, not a person — see Gotchas. Queued the DSR form for a human.

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
