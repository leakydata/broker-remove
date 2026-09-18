# Samba TV, Inc.

- **Email:** privacy@samba.tv (correct address, confirmed by a Samba TV employee)
- **Email fallback (wrong personal mailbox):** [named individual]@samba.tv — the address on their CA data broker registration is a named individual, not a role address
- **Method:** web — email reaches the right desk, but they route every request to a
  OneTrust DSAR form for email verification.
- **Opt-out:** https://privacyportal-cdn.onetrust.com/dsarwebform/87c5ee85-893d-4972-ba26-2e82b743d041/d84d9664-facb-4de3-85fd-a2e339b73dbf.html
- **Domain:** samba.tv
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-06)
- Reference: `gmail:1a0766192b26833b`
- Note: CATEGORICAL NIL, AND AN INFORMATIVE ONE, 2026-09-06. Samba TV closed the ticket with a statement about what they collect rather than about what a search returned: 'Samba TV is a television and data analytics company. We do not collect a consumer's name, physical or email address, or telephone number. Based on information provided in the request we have not collected or processed any personal information related to the requester.' THAT IS THE 330 ANSWER -- a nil that is a statement about the KEYS rather than about the file. Every identifier the letter supplied is of a type they say they do not hold, so the nil follows from their data model instead of resting on an unverifiable lookup, and it is consistent with what the company is: an automatic-content-recognition business whose graph is built on TV device and household signals, not on names and postal addresses. NOT REOPENED, DELIBERATELY, even though they invited it ('You may reopen this ticket at any time'). The only way to be found in a file keyed to device and household signals is to supply a device identifier or an IP address, and the standing rule refuses both -- so the residual holding, if any, is unreachable by design rather than by their obstruction. Pressing further would mean either asking a question already answered or handing over the exact identifier class that must not be handed over. They also noted that closing the ticket does not affect a request filed through their web form, which is tracked separately in the queue as a device-level opt-out. CONTRAST WORTH KEEPING: the sibling row semasio shares this Zendesk and sent the same portal-deflection macro four times on the hour and never engaged (336). Same company group, same helpdesk, one thread answered properly and one answered by a cron.

## Gotchas

- **The CA registration lists a named employee, not a role address.** Confirmed with a real reply rather than a bounce — a different failure mode from the usual dead-mailbox pattern, but the same fix: find the actual privacy-team address on the company's own site or from whoever answers.
- **Cross-reference (2026-09-16):** Fyllo's privacy team named Samba TV, in writing, as the party that holds the historic Fyllo data-broker consumer database — current Fyllo management "did not acquire a data-broker business... no consumer databases were transferred to us and remained with the seller. Please contact SambaTV which is the owner of the prior Fyllo data-broker business." (See `fyllo.md`.) Worth citing back to Samba TV if their OneTrust ticket stalls again: it is independent, broker-supplied evidence that Samba TV holds a *second* data source about the same person — the acquired ad-tech/broker database, separate from the ACR/device-graph data already being asked about.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `[named individual]@samba.tv`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->


## The verification gap, and why it matters here

`privacy@samba.tv` reached the real privacy team on the first try (ticket #345295),
which closes out the registry correction: the filed contact was a named employee, and
he replied himself to say so. The role address was there all along, just never filed
(`_SILENT_FAILURES.md` §88).

Their reply routes to a OneTrust form that **verifies control of the email address
you submit**. That is an ordinary and reasonable verification step. But it comes
apart from the lookup in a way specific to this kind of company:

> **Samba TV's records are keyed to a television, not to an email address.**

Automatic content recognition identifies what is on a screen. The resulting
observations attach to a device, and from there to a household. So confirming you
control an email address proves *who you are* without necessarily locating *what they
hold* — and if you have never had a Samba account, the verified address may match
nothing at all while the household's viewing history sits under a device identifier
you cannot supply.

That is the Foursquare pattern from §127 in a different medium: a working process
attached to a key the consumer does not have. The difference is that here the
verification step and the lookup key have simply come apart from each other, rather
than both resting on an unobtainable identifier.

## Steps

1. Complete the OneTrust form as the **consumer**, using the address you actually
   read, and click the confirmation it emails.
2. In the free-text field, ask for the things the form has no box for:
   - **viewing history and ACR observations**, not just account data;
   - the **household graph** entry linking the television to people and devices;
   - any **inferred audience segments** built from viewing;
   - **forward-looking suppression**, so the set is not re-enrolled at the next sync.
3. Ask the question plainly: **if I have never had an account, what does the verified
   email match against?** Ask whether they can search by household address instead —
   and ask them to report matches before deleting, because a household television is
   shared and other people's viewing is not yours to remove.

## Gotchas

Do not write to the address on their California registration. It is a named
employee's mailbox, he is still there, and he will politely redirect you — which
costs a round trip and puts a stranger's inbox in the loop for no reason.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Samba TV, Inc.
- **Registered address:** 118 King Street Suite 100, San Francisco, CA,
  94107
- **Filed contact email:** [named individual]@samba.tv
- **Filed phone:** 4158896404
- **Website:** https://www.samba.tv

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
