# D Dots

- **Email:** support@ddotslab.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** ddotslab.com
- **Priority: 2.**

## Status

- Current: `failed` (updated 2026-08-17)
- Note: Published contact address hard-bounced (550, address not found). No alternative address published on the site — privacy and contact pages carry no email, or carry only the bounced address. Domain and MX resolve, so the domain is live and the mailbox is not. No usable email route; registry marked email_verified=false.

## Steps

1. Email the published address. It hard-bounces with a 550, "address not found".
2. Confirm what kind of failure it is before concluding anything:
   `dig +short MX <domain>` and `dig +short A <domain>`. Both answer here, so the
   domain is live and the mailbox is not.
3. Re-read the privacy and contact pages for any second address. There is none.
4. Mark `failed` with the bounce quoted, and set `email_verified=false` in the
   registry so the address is never silently reused.

## Gotchas

A **550 is not the same as a dead domain**, and the difference decides what to do
next. Here the domain resolves and its MX records answer — mail was accepted for
delivery and then refused by the receiving server because the mailbox does not
exist. The company is live. Only the address they publish is fiction.

That distinction matters because a dead domain means "stop, there is nobody to
write to", while a live domain with a dead published mailbox means "the route is
wrong, find another one" — and it is also the more damning of the two. Publishing
a privacy contact that bounces is not an accident of neglect in the same way a
lapsed domain is; it is a contact point offered to consumers that silently
discards what they send. Anyone who wrote to it and did not check their own
bounce folder believes a request is pending.

The site publishes no second address. Privacy and contact pages carry either
nothing or the same bounced mailbox, so there is no fallback to try.

## Verification

Nothing to verify: no request was ever delivered. Re-check the site periodically
for a working contact, and keep the bounce — a published privacy address that
does not accept mail is the substance of a regulator complaint, not a footnote to
one.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** D Dots LLC
- **Registered address:** 210 Rockview, Irvine, CA
- **Filed contact email:** support@ddotslab.com
- **Website:** https://www.ddotslab.com

*Source: `data/registries/registry2024.csv`.*

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
