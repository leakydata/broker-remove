# Mobility Global; S&P Global

- **Email:** privacy@mobilityglobal.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** mobilityglobal.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-09-22)
- Reference: `gmail:1a0c4179b9fad43b`
- Note: 9/22 (second round). They answered the direct-email ask with the
  comment's content: "On September 10th, we requested a government issued ID
  to verify your identity. On September 21st, we informed you that your
  request has been closed because we did not receive your ID... To action your
  request, you will need to resubmit the request into our webform and provide
  a government issued ID." They also stated OneTrust needs no portal login to
  read comments — contradicting the earlier read that a login was required;
  the actual gate is the closed/ID-required status, not portal access. Replied
  9/22 declining the government ID (per this project's hard rule) and pushing
  back on proportionality specifically: this is a phone/email/address removal,
  not a sensitive-data request, and CCPA/CPRA verification is supposed to scale
  to the sensitivity and risk of the data, not default to the highest tier.
  Offered a one-time email code or a knowledge-based check instead, and asked
  them to confirm in writing if a government ID is genuinely their only
  verification tier for a request of this kind. Awaiting reply; if they hold
  firm, record as a genuine gov-ID-required refusal (not a portal/CAPTCHA
  block) and close out at `failed` rather than keep escalating — per project
  rules, never upload a government-issued ID.
- Prior (9/21): OneTrust notice: "A comment has been added to your request
  (Request ID: AV6KDQ7SS4)," link-only, portal login required to read the
  comment content — the request itself (the detailed DPPA-fork letter below)
  had gone unacknowledged since 8/29 until this. Rather than opening the
  portal, emailed privacy@mobilityglobal.com directly 9/22 asking them to
  state the comment's content by email, since this project does not use
  browser/portal logins, and repeating the core ask (delete/opt-out/direct
  third-parties/suppress) and the four email addresses for reference.
- Prior (2026-08-29): Emailed privacy@mobilityglobal.com 2026-08-29 (CA registry 2026 only -- a new registrant, consistent with the rename). Automotive intelligence; the site states S&P Global Mobility is now Mobility Global. FIRST USE OF THE DPPA FORK IN A LETTER OF THIS KIND. (1) Asked whether any data held, received or derived originated -- directly or through an intermediary -- in STATE MOTOR VEHICLE RECORDS (title, registration, lienholder, driver licence). If it did, the Driver's Privacy Protection Act, 18 U.S.C. 2721 et seq., governs, and two things follow: which enumerated permissible use they rely on, and -- the valuable one -- SECTION 2721(c) REQUIRES A RESELLER OR REDISCLOSER TO KEEP FOR FIVE YEARS RECORDS IDENTIFYING EACH RECIPIENT AND THE PERMITTED PURPOSE, so asked for those records as they relate to me: who received it, when, for what purpose, with a named exemption required if they decline. That is an access-log ask with a federal statutory hook rather than a request for goodwill. If NOT from motor vehicle records, asked where instead -- dealer management systems, service and repair, warranty registrations, telematics, finance and lease, or purchased marketing files. (2) THE VEHICLE IS THE KEY, NOT THE NAME: files of this type are indexed by VIN and by the registrant's details AT THE TIME OF EACH TRANSACTION, which means old addresses; asked them to search all sixteen and to treat as in scope any record where I appear as registered owner, co-owner, lessee, service customer, warranty registrant or PRIOR owner, with the 154 scope limit stated. (3) THE RENAME GAP: asked for confirmation the request reaches records under the former name, predecessor entities in the same lineage including the historic vehicle-registration data business, and any copy retained by S&P Global post-separation -- and said if a copy sits with a company that is no longer theirs, just say so and I will write to them. (4) Derived attributes: in-market and purchase-intent scores, loyalty and defection propensity, estimated income and household composition, segment membership. NO VIN AND NO DRIVER'S LICENCE NUMBER SUPPLIED, with an offer to reconsider the VIN if genuinely necessary.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@mobilityglobal.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

**A detailed, statute-specific letter (DPPA fork, access-log demand) still
routed through OneTrust and produced a portal-gated "comment," not a direct
reply.** The letter's substance didn't get a substantive email answer even
after three weeks — only an automated notice that a comment exists behind a
login. When that happens, email the direct contact and ask for the comment's
content by email rather than assuming a portal account is required; this
project does not create broker accounts as a matter of policy, and asking
costs nothing.

**They require a government-issued ID even for a low-sensitivity removal
(phone, email, mailing address), and close the request outright without
it.** Not a CAPTCHA or portal-access block — a genuine identity-verification
policy holding a hard line. A proportionality argument citing CCPA/CPRA
verification standards (Cal. Civ. Code 1798.130-140) and offering a lesser
method (one-time code, knowledge question) is the right counter, but do not
expect it to move a company whose stated policy has no lower tier. Never
upload the ID regardless of outcome.

## Verification

Watch for the comment's content to come back by email. If they insist on the
portal even after being told no browser/account is used, that becomes a
`captcha_blocked`-adjacent dead end worth flagging for human handoff — but try
the direct ask first.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** R.L. Polk & Co.
- **Trading as:** Mobility Global; S&P Global
- **Registered address:** 5860 Trinity Parkway, Suite 600, Centreville,
  Virginia, 20120
- **Filed contact email:** privacy@mobilityglobal.com
- **Filed phone:** 888-433-8408
- **Website:** www.mobilityglobal.com; www.spglobal.com

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
