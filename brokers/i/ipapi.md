# ipapi

- **Email:** privacy@kloudend.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** ipapi.co
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-05)
- Note: Emailed privacy@kloudend.com 2026-08-28 (Kloudend, Inc. -- ipapi.co, CA registry 2024-2026). IP-range-vs-individual framing: conceded up front that an IP geolocation DB is keyed to network blocks, not people, and asked three answerable questions instead -- (1) is there any subscriber/household or IP-to-identity layer, and if so delete+optout+suppress; (2) is the LOOKUP LOG retained and keyed to the queried IP, which is the part people miss; (3) what would per-person removal even mean for a range-keyed dataset, with 'it does not apply' accepted as a legitimate answer. DELIBERATELY SENT NO IP ADDRESS -- doing so would hand a geolocation company a fresh dated IP-to-named-person association, i.e. create the exact record the letter exists to prevent.
- Reply (2026-09-04): answered all three questions plainly, in order. (1) "We do not link IP data to individual identifiers like name / email / phone etc." -- no subscriber/identity layer exists, so nothing to delete on that front. (2) Query logs are "kept strictly for security, operation and maintenance purposes" and "automatically deleted after a 30 day period" -- so the lookup-log question the letter flagged as "the part people miss" has a real, bounded answer here: 30 days, security-purpose only. (3) Per-person removal for a range-keyed dataset does have one narrow form after all: submit the request FROM the IP to be removed, at https://ipapi.co/donotsell/ -- which only works for the current occupant of an address and is why the letter never asked for a name-based removal path. Also volunteered, unprompted, that they will "continue to honor" a going-forward do-not-collect request.

## Steps

1. Email privacy@kloudend.com. No web form for the name/DOB-based request -- ipapi.co/donotsell/ is a *different*, IP-address-keyed opt-out, not a substitute route for this one.
2. Ask the three questions above rather than a blanket "delete my record" -- a geolocation API has no name-keyed record to delete, and a generic letter draws either a confusing reply or a bare "not found" that teaches nothing.

## Gotchas

- **This is not a people-search site despite the CA registry listing.** ipapi.co sells IP-to-network-block geolocation. A letter that asks it to search by name is asking the wrong question of the wrong database; asking about the query-log retention period is the question that actually has an answer.
- **The one real per-person removal path requires sending the IP that should be removed, from that IP** (https://ipapi.co/donotsell/). Never do this for someone else's current address/IP -- it degrades the data for whoever holds that IP next. Skip this step entirely unless the person specifically wants their current home IP suppressed and understands the tradeoff.
- **Do not send an IP address in the removal letter itself.** Doing so creates a fresh, dated IP-to-named-person record at exactly the company you're trying to avoid being linked to.

## Verification

Company states query logs are deleted after 30 days on their own; no further action needed unless a subscriber/identity layer is later added to the product.
