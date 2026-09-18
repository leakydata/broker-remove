# Quick Public Records

- **Opt-out:** https://www.quickpublicrecords.com/help-center/privacy-requests
- **Email:** support@quickpublicrecords.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** quickpublicrecords.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Reference: `04YVZX-6DK0Z`
- Note: 2026-08-20: ticket #3421287 closed without answering follow-up (CSAT fired). Reopened. Sequential Zendesk ticket IDs 3421272/3/81/87 across four sibling subdomains = one Zendesk account = one operator; put that to them as settled and asked only whether removal spans all four properties.

## Steps

1. Write to `support@quickpublicrecords.com` — Zendesk,
   answers within hours, and a human replies.
2. Ask the four-site scope question up front (below), and the suppression
   question explicitly. Both got useful answers here.

## Gotchas

**Ask the suppression question in a form that invites a caveat.** This operator
gave the best answer in the project — a standing suppression with its limits
stated — and that shape is what a truthful answer looks like. See the outcome
section below.

**They confirm across aliases without being asked twice**, which is unusual and
worth noting when comparing operators.

**They do not volunteer the sibling relationship.** The confirmation names one
domain. Four share a Cloudflare nameserver pair (see `_BROKER_FAMILIES.md`), and
the scope question went unanswered on the first pass — so ask it again, framed so
that a denial is as useful as a confirmation.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->


## Outcome: confirmed — and the model answer on suppression

Their confirmation gets right the two things most confirmations leave ambiguous.

**Scope across aliases, stated:**

> *"the public data provided in your request has been removed from
> www.QuickPublicRecords.com **under all your aliases**."*

**And suppression, answered honestly with its limits:**

> *"We will also use commercially reasonable efforts to ensure that your
> information will not be made available in the future... **however we cannot
> guarantee** that these efforts will 100% guarantee that we can block your
> future Public Records from appearing on our site."*

That is a **qualified standing suppression** — and it is a better answer than a
clean unqualified "removed" would have been, because it tells the subject what to
expect and when to re-check. Hold it up as the model reply to the
suppression-versus-one-time question: the honest answer to that question has a
caveat in it, and a reply without one is more likely to be avoiding the question
than answering it.

## Still open: which sites?

The confirmation names **only** `www.QuickPublicRecords.com`. The request set out
the evidence that four domains share one Cloudflare nameserver pair and asked
them to confirm or deny the relationship. Neither happened.

Followed up asking for one sentence either way — *these are ours too*, or *those
are unrelated companies* — since **both answers are useful** and only silence is
not. Also asked for `noindex` confirmation and for the relatives-and-associates
listings on other people's pages.

Support line, from the confirmation: 1-833-202-2626, Pacific hours.

## 2026-08-20: closed without answering, and the ticket number answered it anyway

The follow-up above was never replied to. What arrived instead, thirty hours
later, was a satisfaction survey for request **#3421287** — the ticket went
Open → Solved with the scope question still open. That is `_SILENT_FAILURES.md`
§70, for the fourth time in this family.

**The four ticket numbers are the finding.**

| Ticket | Zendesk subdomain |
|---|---|
| 3421272 | `publicdatacheck` |
| 3421273 | `publicinfoservices` |
| 3421281 | `publicrecordreports` |
| 3421287 | `quickpublicrecords` |

Zendesk numbers tickets **per account**, not per brand or help-centre subdomain.
Four nominally unrelated companies do not draw 3421272, 3421273, 3421281 and
3421287 from one sequence within a day and a half. Combined with the shared
Cloudflare nameserver pair that opened the original letter, the operator question
is settled: one company, four brands, one help desk.

The elegant part is that **they generated the evidence while declining to answer
the question it settles.** Four automated closure emails proved what four support
agents would not say.

**Downgraded from `confirmed` to `submitted`.** The 19 August message did confirm
removal — "under all your aliases", with an honest commercially-reasonable-efforts
caveat on suppression, which remains better practice than most. But it confirmed
removal from **one hostname**, and it is now established that the hostname is one
of four served by one operator. A confirmation scoped to a quarter of the estate
is not a confirmation, and leaving this at `confirmed` would record the exact
illusion §40 exists to warn about.

**Reopened by replying into the acknowledgement thread, not the survey.** The
survey's reply path is a rating endpoint; the acknowledgement is the ticket. The
rating was not clicked — clicking resolves the CSAT and hands the desk a metric
without producing an answer.

**What the reply asks for**, keeping it a question rather than an accusation:
confirm in one sentence that the removal spans all four properties — *or* say
plainly that it does not and four separate removals are needed. Both answers
close it. The `noindex` and relatives-and-associates points were carried forward
unchanged.

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
