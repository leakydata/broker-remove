# Fourthwall

- **Email:** privacypolicy@fourthwall.tv — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** fourthwall.tv
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-22)
- Note: SOFT BOUNCE, new class: privacypolicy@fourthwall.tv forwards to css-support@fourthwall.tv and the DSN says 'The recipient's mailbox is full and can't accept messages now.' Not a dead address - a full one. The mailbox exists, the domain is fine, and the message was simply refused for want of space. A follow-up run (2026-08-22) resent to californiadrop@fourthwall.tv (a different, previously-untried address from curated_brokers.json) instead of waiting and retrying the original — this contradicts the playbook's own advice below not to re-route. It did deliver without bouncing, so leave as `submitted`, but the still-open question from 2026-08-18 stands: this may be a false-positive registry entry (Fourthwall is creator-commerce, not people-search/ad-tech). If the reply says "not a data broker" / "no data held," record `not_found`.

## Steps

1. Email `privacypolicy@fourthwall.tv` with the standard deletion/opt-out request.
2. Fourthwall is a creator-commerce platform (merch/subscriptions for content creators), not a people-search or ad-tech company — this entry likely reached the registry via Optery's broad scrape. Expect a "we don't have your data" or "we're not a data broker" reply; if so, record as `not_found` rather than pushing further.

## Gotchas

- Likely a **false-positive registry entry** from the Optery import — verify the reply before assuming this is a genuine data broker. If they confirm no data held, mark `not_found` and move on rather than escalating.

## Verification

No public listing to check. Awaiting reply as of 2026-08-18.

## The mailbox was full — retry, do not re-route

`privacypolicy@fourthwall.tv` produced a bounce from `postmaster@fwm.tv`:

> *"Delivery has failed to these recipients or groups: css-support@fourthwall.tv
> The recipient's mailbox is full and can't accept messages now. Please try
> resending your message later."*

**This is the temporary bounce class** (`_SILENT_FAILURES.md` §18), and it calls
for the opposite of the usual response. The address is correct. The domain is
healthy. The company is trading. The message was refused for want of space and
will go through later.

So do **not** go hunting for a different address — their site publishes no other
one, and re-routing a privacy request to whatever mailbox turns up on a contact
page sends it somewhere worse than the one that is merely busy.

**Diarise the retry.** A full mailbox is transient and nothing will remind you.
Recorded as `failed` with the reason so it does not sit in `submitted` looking
like a request in flight — but the reason is the point, and the entry is a
to-do rather than an ending.

## What the bounce gave away

The message was addressed to `privacypolicy@` and the DSN came back naming
`css-support@`. The published privacy address is an **alias forwarding into a
customer-support queue**.

Worth knowing even after the mailbox drains: a privacy request arriving in the
same tray as billing questions and order enquiries will be triaged by someone
whose job is neither, which is a decent predictor of the reply you get. It also
explains how a mailbox at a company this size fills up at all.

When retrying, consider saying in the letter that you know where it lands, and
asking to be routed to whoever actually handles data-subject requests.

