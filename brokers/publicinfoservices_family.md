# Public Information Services / Public Data Check / Public Record Reports

- **Opt-out:** email to the support address of each brand
- **Email:** support@publicinfoservices.com, support@publicdatacheck.com,
  support@publicrecordreports.com (all Zendesk-fronted)
- **Method:** email → Zendesk
- **Priority: 2.**

## Status

- All **four**: `submitted` (updated 2026-08-22)
- References: `#3421273` (Public Information Services), `#3421272` (Public Data
  Check), `#3421281` (Public Record Reports)

## Steps

1. Email each brand's support address. Receipt arrives within about a minute
   from that brand's own Zendesk subdomain.
2. Wait. The next message is not an answer.

## Gotchas

**The ticket closes without a reply, and the only artifact is a satisfaction
survey.** Roughly thirty hours after the acknowledgement, all three brands sent
the same thing at the same minute:

> "We'd love to hear what you think of our customer service. Please take a
> moment to answer one simple question by clicking either link below: How would
> you rate the support you received?"

There was nothing in between. No outcome, no refusal, no request for further
information. Zendesk fires CSAT on transition to Solved, so the survey proves the
ticket was **closed** — it proves nothing about whether anything was removed.
"We removed the records", "we found nothing", and "we bulk-closed the queue"
produce identical mail to the requester. Full treatment in
`_SILENT_FAILURES.md` §70.

**Do not rate the survey.** Clicking a rating resolves the CSAT and hands the
desk a metric without giving you an answer.

**Reply into the ticket thread instead.** Replying to a Solved Zendesk ticket
reopens it, which is the point — but reply to the *acknowledgement* email, which
is the ticket thread. The survey is a separate notification and its links go to
a rating endpoint, not to a person.

**Make every possible answer acceptable.** What was sent:

> I am not complaining about the closure. I would just like one line, and any of
> these is a complete answer as far as I am concerned: "Removed" / "We hold no
> record matching what you sent" / "We need something more from you".

Offering "we hold nothing" as a *complete and accepted* answer is what makes the
one-line reply cheap enough to happen. A desk that bulk-closes does so because
answering feels like work with a downside.

**They are one queue.** Ticket numbers 3421272, 3421273 and 3421281 were issued
across three different Zendesk subdomains — sequential IDs on nominally
unrelated companies mean a single shared instance. Practical consequence: the
three follow-ups are read by the same person, so send one short question three
times rather than three different arguments. Do not ask them to confirm the
corporate relationship; it is not something a support agent should have to
answer, and the removal does not depend on it (`_DEFLECTIONS.md` §40).

## Verification

A CSAT survey is not a confirmation. Leave all three `submitted`, record the
ticket numbers, and let either the reply or the next verification sweep decide.
Re-run a name search on each of the three sites directly rather than trusting a
search-engine result.


## 2026-08-22: it is four sites, not three, and their own ticket numbers prove it

Quick Public Records belongs to this family. The evidence is the ticket numbers,
issued across four different Zendesk subdomains inside thirty-six hours:

| Ticket | Subdomain |
|---|---|
| 3421272 | `publicdatacheck` |
| 3421273 | `publicinfoservices` |
| 3421281 | `publicrecordreports` |
| 3421287 | `quickpublicrecords` |

**Zendesk numbers tickets per account, not per brand or help-centre subdomain.**
Four nominally unrelated companies do not draw from one sequence by coincidence.
Combined with the shared Cloudflare nameserver pair that opened the original
letters, the operator question is settled.

The neat part is that all four *generated this evidence while declining to answer
the question it settles*. Four automated closure emails proved what four support
agents would not say. See `_SILENT_FAILURES.md` §70.

**Quick Public Records was downgraded from `confirmed` back to `submitted`** on
that basis: its 19 August message confirmed removal from one hostname, and a
confirmation scoped to a quarter of the estate is not a confirmation. See
`quick_public_records.md`.

**All four closed their tickets via CSAT survey without answering.** Do not rate
the survey — clicking a rating resolves the CSAT and hands the desk a metric
instead of producing an answer. Reply into the acknowledgement thread, which
reopens the ticket; the survey's reply path goes to a rating endpoint.

## Cross-reference

This family was worked out from infrastructure and ticket counters. The state
registration filings do the same job *before* you write — see `_FAMILIES.md`.
The optOutLight siblings (`peoplesearcher.com`, `checksecrets.com`,
`weinform.org`, `privatereports.com`) each register several brands under one
statutory contact address, which is the same finding arrived at from a document
rather than an inference.
