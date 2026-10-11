# Outbrain

- **Email:** ob-privacy@teads.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** outbrain.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-10-11)
- Note: THE ROW SAID unreachable; THE FILED ADDRESS WAS privacyquestions@outbrain.com ALL ALONG. Outbrain is a major content-recommendation platform, so unreachable was never plausible -- it was an adopted ledger line with no detail, and data/register_profiles.json held the contact. LETTER SENT 2026-10-11 AND DELIBERATELY SHORT ON IDENTIFIERS: name and four email addresses only, no postal history, no phone numbers. Explained why in the letter rather than leaving it to inference -- a platform keyed to cookies and device identifiers cannot match on an address, so sending sixteen former addresses would hand them personal data they did not hold about a person they cannot identify, which is the wrong outcome from a privacy request. That is the email-only doctrine of the letter generator applied with its reasoning stated out loud. FIVE ASKS, all architectural. (1) WHAT DO YOU KEY ON -- if profiles are keyed to cookies or MAIDs, a name-and-email nil is STRUCTURALLY GUARANTEED and says nothing; asked for that answer in preference to a clean 'no records found'. (2) THE HASH QUESTION of 489a -- hash the addresses already supplied and suppress against those hashes, deriving nothing new rather than acquiring a new identifier. (3) QUERY-TIME ARCHITECTURE -- if results are assembled on demand there is no record to suppress, only keys, and everything outside them is un-searched rather than suppressed; said explicitly that this is an acceptable and more useful answer than a confirmation implying a deletion that never happened. (4) WHICH SYSTEMS -- own recommendation data, licensed advertiser segments, and anything from the Teads combination are distinct. (5) IS THE OPT-OUT ONLY A COOKIE -- a cookie-stored opt-out dies on browser clear and does not travel between devices, so it is not a durable suppression. REFUSED THE IDENTIFIER CATEGORY IN WRITING: no MAID, no device ID, no cookie ID, no IP, with the reason given -- better a limited result than handing over the identifiers that make cross-site tracking work -- and invited them to say if that makes the request unfulfillable, which would itself be a real answer.

## Steps

1. **Check the contact before writing.** The registry's
   `privacy@outbrain.com` is stale. Their published privacy contact is now
   **`ob-privacy@teads.com`** — the rights desk moved onto the domain of the
   company they acquired.
2. Write there, and scope the request to **both estates explicitly**.

## Gotchas

**The rights address names the parent, or in this case the acquisition.**
This is the same signal recorded in `_BROKER_FAMILIES.md`, running in the
opposite direction: usually a small brand's privacy address points at the parent
that owns it. Here a large acquirer's privacy address points at the company it
bought. Either way the hostname of the contact is telling you about corporate
structure that nobody published as such — and it is worth reading, because it
tells you what a confirmation might silently exclude.

**Scope across the merger by name.** Ask them to say which estates they searched.
Where two businesses have been combined but the systems have not, a completely
truthful confirmation about one side is indistinguishable, from outside, from a
complete removal. Asking costs a sentence.

**Pre-empt the cookie answer.** Adtech firms frequently answer a deletion request
with an opt-out cookie. Say up front that a browser-local preference is not a
deletion — it dies with the cookie jar and leaves the record untouched.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Teads Holding Co
- **Registered address:** 111 West 19th Street, New York, New York, 10011
- **Filed contact email:** privacy@teads.com
- **Filed phone:** 7823771890
- **Website:** https://www.outbrain.com

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
