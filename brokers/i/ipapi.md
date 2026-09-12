# ipapi

- **Email:** privacy@kloudend.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** ipapi.co
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-05)
- Note: 2026-09-04/05 (§326): ALL THREE QUESTIONS ANSWERED, AND THE THIRD ANSWER IS THE BEST VERIFICATION DESIGN IN THE CORPUS. Kloudend, Inc. (ipapi.co) replied: (1) 'We do not link IP data to individual identifiers like name / email / phone etc.' -- no identity or subscriber layer, which is the whole of question 1; (2) 'The queried IPs are written to webserver logs and are kept strictly for security, operation and maintenance purposes. They are automatically deleted after a 30 day period' -- an actual retention period, and confirmation that the lookup log is not an identity record; (3) removal IS possible and is keyed to the IP: 'please submit the request from the IP that needs to be removed at ipapi.co/donotsell/'. THAT THIRD ONE IS THE ELEGANT PART: verification BY CHANNEL rather than BY DISCLOSURE -- you do not send them your IP, you connect from it, so the proof is already in the packet and NO NEW IDENTIFIER IS CREATED. Exactly inverse to the cookie-ID, social-handle, phone/SMS and government-ID demands refused elsewhere this week (§303, §317, §319, §323). They also searched the supplied identifiers and matched nothing, which was expected and which my letter had said in advance would be a complete answer. DID NOT USE THE DONOTSELL LINK: it would suppress this automation host's IP rather than the subject's, and my own letter had already said I was not asking for a residential IP to be suppressed because a carrier reassigns it and the suppression would then degrade the data for whoever holds the address next -- that reasoning does not stop being true because they offered. FILE CLOSED with thanks; nothing outstanding, no further letter.

## Steps

1. Email privacy@kloudend.com. No web form for the name/DOB-based request -- ipapi.co/donotsell/ is a *different*, IP-address-keyed opt-out, not a substitute route for this one.
2. Ask the three questions above rather than a blanket "delete my record" -- a geolocation API has no name-keyed record to delete, and a generic letter draws either a confusing reply or a bare "not found" that teaches nothing.

## Gotchas

- **This is not a people-search site despite the CA registry listing.** ipapi.co sells IP-to-network-block geolocation. A letter that asks it to search by name is asking the wrong question of the wrong database; asking about the query-log retention period is the question that actually has an answer.
- **The one real per-person removal path requires sending the IP that should be removed, from that IP** (https://ipapi.co/donotsell/). Never do this for someone else's current address/IP -- it degrades the data for whoever holds that IP next. Skip this step entirely unless the person specifically wants their current home IP suppressed and understands the tradeoff.
- **Do not send an IP address in the removal letter itself.** Doing so creates a fresh, dated IP-to-named-person record at exactly the company you're trying to avoid being linked to.

## Verification

Company states query logs are deleted after 30 days on their own; no further action needed unless a subscriber/identity layer is later added to the product.
