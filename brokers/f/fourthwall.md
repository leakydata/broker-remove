# Fourthwall

- **Email:** privacypolicy@fourthwall.tv — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** fourthwall.tv
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-24)
- Note: 2026-08-24: 'Any and all personal information pertaining to you has been deleted from our systems where present, and you have been opted out of any future sale or sharing.' Was marked failed after privacypolicy@fourthwall.tv bounced (mailbox full); the californiadrop@ resend worked and they answered BOTH threads from privacymailbox@fourthwall.tv.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** FourthWall Media, Inc.
- **Trading as:** FourthWall
- **Registered address:** 20130 Lakeview Center Plaza, Suite 400,
  Ashburn, VA, 20147
- **Filed contact email:** [named individual]@fourthwall.tv
- **Filed phone:** 5712669787
- **Website:** www.fourthwall.tv

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
