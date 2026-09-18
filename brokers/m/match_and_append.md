# Match And Append

- **Email:** privacy@matchandappend.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** matchandappend.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-19)
- Note: REFINED, and it explains why two agents saw two different things minutes apart. The cloud agent reported the privacy page now returns 503 rather than failing DNS; from here the apex fails to resolve entirely. Both observations are correct: matchandappend.com HAS NO A RECORD AT ALL, while www.matchandappend.com resolves to 34.106.169.43. Whoever hits the apex gets a resolution failure; whoever hits the www host reaches a server that is erroring. So the earlier 'no website' finding was right about the apex and wrong as a description of the domain. Neither host served a page to this session. Mail remains Zoho MX with both privacy@ and info@ hard-bouncing 550, so the email route is still dead regardless. Keeping unreachable. LESSON: check the apex AND the www host before declaring a site gone - they are separate records and either can exist without the other.

## Steps

1. Do NOT use `privacy@matchandappend.com` — it hard-bounces 550.
2. There is no website to read for an alternative: the domain has no A record.
3. Write to `info@`, report the dead privacy mailbox as a fault, and target the
   linkage rather than the row.

## Gotchas

Live mail, dead website, and the published privacy mailbox does not exist. Below.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Live mail, no website

`privacy@matchandappend.com` returns a hard **550 — address not found**. That is not a
dead company: the domain publishes a healthy **Zoho** MX and accepts mail at other
local parts. What it does not have is a **website** — no A record, and every URL
returns nothing at all.

This is the same shape as `minervadata.xyz`, and exactly the case that a reachability
check keyed to web presence gets wrong (see `_SILENT_FAILURES.md` §30). A company can
receive mail perfectly well while having no site to read, and for an
append-and-match business — which sells to other businesses through direct
relationships — a public website is not a requirement of the trade.

**Consequence for finding a contact:** the usual move of reading the privacy policy for
a working address is unavailable. There is nothing to read. Writing to `info@` and
reporting the dead mailbox is the remaining option, and the report is worth making
regardless: an address published for rights requests that rejects them loses every
request anyone sends, and no sender can distinguish that from being ignored.

## Aim at the linkage, not the row

The product is attaching data to somebody else's record. So the request names the
**linkage** explicitly — the appended phone, email, address or demographic value *and*
the connection between it and the person — plus the hashed email used as a match key,
any household or persistent key, and any derived attribute.

Deleting an appended value while leaving the match key intact means the same append
happens again at the next run.

## Update: the domain does have a site again (2026-08-19, later same day)

A fresh check found the domain now resolving with a live web server: fetching
`matchandappend.com/privacy-policy` returned an HTTP 503 (service unavailable),
not a DNS failure, and the CA data broker registry
(oag.ca.gov/data-broker/registration/546620) publishes two web routes beyond the
dead `privacy@`/`info@` mailboxes:

- `https://www.matchandappend.com/do-not-sell-my-data/`
- `https://www.matchandappend.com/unsubscribe/`

Neither was reachable at check time (503), so this may be an intermittent outage
rather than the "no website at all" state found earlier the same day. Worth a
human retrying the two URLs above before falling back to the `info@` fault report
described above.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** MatchAndAppend.com LLC
- **Registered address:** 16125 Zagros Way, Austin, TX 78738, United
  States
- **Filed contact email:** info@matchandappend.com
- **Website:** http://www.matchandappend.com
- **Opt-out route they filed:** Consumers may contact us at
  privacy@matchandappend.com or use the links on our website
  https://www.matchandappend.com., , Access, Deletion and Do Not Sell
  Right, , Under the CCPA, California consumers have the right to:, â€¢
  Request that a business that collects a consumer's personal data
  disclose the categories and specific pieces of personal data that a
  business has collected about consumers., , â€¢ Request that a business
  delete any personal data about the consumer that a business has
  collected., , â€¢ Request that a business that sells a consumer's
  personal data, not sell the consumer's personal data., If you make a
  request, we have one month to respond to you. If you would like to
  exercise any of these rights, please contact us using the link to Do
  Not Sell My Data. (https://www.matchandappend.com/do-not-sell-my-data/)
- **Route for protected individuals:** Consumers may contact us at
  privacy@matchandappend.com or use the links on our website
  https://www.matchandappend.com, , An individual has the right to
  request that Match and Append unpublish, remove, or make unavailable to
  third parties any information about him or her from the Databases or
  disconnect a link to another site. , , If you make a request, we have
  one month to respond to you. If you would like to exercise any of these
  rights, please contact us using the link to Unsubscribe.
  (https://www.matchandappend.com/unsubscribe/) (Cal. Gov. Code 6208.1(b)
  / 6254.21(c)(1) — for survivors of domestic violence, stalking and
  similar, a stronger and faster route than the ordinary consumer
  request)
- **What they say they collect:** Please visit our privacy policy at
  https://matchandappend.com/privacy-policy-3/ for additional information
  about data collecting practices.

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
