# Intentgine

- **Opt-out:** https://intentgine.com/ccpa-privacy/
- **Email:** privacy@pharosiq.com (verified)
- **Method:** web_form — Web form.
- **Domain:** intentgine.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-08-23)
- Note: ITEMISED NIL, second and better answer. 2026-08-31 from Privacy@pharosiq.com: 'We have searched our database for all instances of your email address, name, phone number and address, but have been unable to identify any records relating to you.' That names the FIELDS searched rather than asserting a bare negative -- the 198 shape. Their first reply (2026-08-20) was the weaker 'the information you provided is not present'; this one says what was looked for. Recorded as a clean nil.

## Steps

1. Email `privacy@pharosiq.com` — Intentgine's privacy contact resolves to PharosIQ, a different brand than the registry domain (intentgine.com); this is a B2B intent-data / lead generation business, so ask who purchased or received the record in addition to deletion.
2. Note the brand relationship (Intentgine ↔ PharosIQ) in any follow-up so the request isn't mistaken as misdirected.

## Gotchas

- **Brand mismatch** like Firmfuel/BenefitsBunny: registry domain and privacy-contact domain differ (intentgine.com vs pharosiq.com). State the connection explicitly in the email so it isn't bounced as "wrong company."

## Verification

No public listing to check. Awaiting reply as of 2026-08-18.

## Outcome (2026-08-20): an honest negative, scoped to the wrong message

`Privacy@pharosiq.com` replied two days after the request:

> "This email is in response to your privacy opt-out request. We have reviewed
> our systems, and the information you provided is not present.
>
> No further action is required at this time.
>
> If you believe your data may exist under a different email address/company or
> spelling variation, please feel free to share it, and we will be happy to
> recheck."
>
> — PharosIQ Data Team

**Check what the reply quotes.** It quotes the *first* letter, which listed four
email addresses. It does not quote the follow-up sent eleven hours later, which
extended the request to cover both brands served by this mailbox and asked them
to search for records keyed to a hashed email, a mobile advertising or cookie
identifier, or an IP-derived household association.

So "the information you provided is not present" is true and narrow. It refers to
four plaintext addresses. In an intent-data business those are often not the key
the record is held under, so a lookup on them can correctly return nothing while
an identifier-keyed record exists. Written up as `_SILENT_FAILURES.md` §73.

**The promise was kept.** The follow-up had said an unqualified "we hold nothing"
would be a complete answer and close the matter. It was not re-argued. That
matters beyond this broker — pre-accepting the unflattering answer is only
effective as a technique because it is honoured.

**The invitation was accepted instead**, which is a different thing from
re-litigating. Sent: the other eight email addresses, four name variants, nine
prior localities, eight prior phone numbers. Plus two questions framed as
questions about *how the check ran*, not about whether it was right:

- does "not present" cover identifier-keyed records as well as contact records,
  or was it a lookup on the addresses given?
- does the answer cover both PharosIQ and Intentgine, and any other entity whose
  privacy requests come from this mailbox? If they are separate controllers
  sharing a desk, name the ones it covers and the rest get their own letters.

Both were offered as acceptable either way. Answering costs nothing; declining
would be conspicuous.

**Status:** left `submitted`, not `not_found`. The negative is real but partial
and a recheck is outstanding. Flip when it returns empty.

**Lesson for reuse:** put the scope in the first letter. A follow-up is not an
amendment — operationally it is a low-priority comment on a ticket that has
already been framed by the message that opened it.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Intentgine Inc.
- **Registered address:** 316 California Ave #34, Reno, NV 89509, United
  States
- **Filed contact email:** [named individual]@intentgine.com
- **Website:** http://intentgine.com
- **Opt-out route they filed:** A consumer may make a request to
  privacy@intentmacro.com. They may also utilize an opt-out function via
  our website.
- **Route for protected individuals:** An individual can demand deletion
  of information through a request to privacy@intentmacro.com (Cal. Gov.
  Code 6208.1(b) / 6254.21(c)(1) — for survivors of domestic violence,
  stalking and similar, a stronger and faster route than the ordinary
  consumer request)

*Source: `data/registries/complete-reg-data-brokers.csv`.*

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
