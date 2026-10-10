# Outreach Io

- **Opt-out:** https://preferences.outreach.io/form/opt_out?locationCode=US
- **Email:** security@outreach.io — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** outreach.io
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-10-10)
- Reference: `657692`
- Note: VERIFIED AGAINST THE MAIL (468 audit) -- THE STATUS IS NOW CORRECT BUT IT WAS NOT EARNED WHEN RECORDED. Outreach replied 2026-10-06: 'We have confirmed your identity through the email address associated with your request. We then conducted a search of Outreach systems. Based on that search, we do not currently process or...' A good nil: identity verified from the sending address with no ID demanded, and a search described rather than merely asserted. THE TIMING IS THE FINDING. The adopted note says another agent recorded not_found on 2026-09-24. THE REPLY IS DATED 2026-10-06 -- TWELVE DAYS LATER. On the day the row was closed there was no such answer in the mailbox, so whatever the status rested on, it was not this. It happens to have come true since, which is luck rather than method: had Outreach instead found a record, the row would have read not_found through the whole period a real record sat live. A NEW FAILURE MODE WORTH CHECKING SYSTEMATICALLY: not a status that is wrong now, but one that was UNEARNED WHEN RECORDED, and that the eventual answer quietly ratified. It is detectable without reading anything -- compare the adoption date against the date of the broker's reply, and flag every row where the status predates the evidence. ALSO WORTH NOTING: they sent FIVE IDENTICAL COPIES of the completion within three minutes, all still unread. Duplicate completion notices are a pattern in this corpus (heartbeat.ai sent three, allant_group sent many) and they inflate any count of 'replies received' that is not deduplicated by content.

## Steps

1. Write to `security@outreach.io` and copy `support@outreach.io`.
   The registry keeps the security address because it is purpose-built for this
   request type; the site publishes the support one. Using both costs nothing.
2. Same processor-first framing as `onemodel.md`.

## Gotchas

**Name the customer, not the role.** As with any platform holding
customer-uploaded contact data, "contact the controller" is unactionable until
the controller is named. Ask for the accounts by name and, failing that, for an
explicit statement that they will not name them plus a commitment to forward.

**Pre-empt the B2B carve-out rather than waiting for it.** The expected reply is
that business contact details sit outside consumer privacy rights. Ask them to
name the basis rather than decline quietly on it, and to apply the request in
full to everything outside whatever carve-out they claim. A business email
address is still an address that reaches the person, and it is still the join key
that assembles the rest of a profile.

**Old institutional addresses are the ones held.** Sales prospecting databases
are built from the address someone used at a previous employer or university, not
the one they use now. Every historical address needs to be in the letter.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Outcome (27 Aug 2026)

A long, careful reply from their Sr Director of Data Privacy — the best-argued
answer on the controller/processor line the project has had. Status stays
`submitted` (60–90 days notified), but the reasoning is worth more than the
outcome.

**All three pre-empts above got direct answers.** That is the reusable finding:
naming an expected deflection in advance, and asking them to state the basis
rather than decline quietly on it, produced explicit positions on all three
instead of silence on all three. In particular the B2B carve-out was *not*
claimed — they went out of their way to say that address, phone and DOB do not
fall outside CCPA, and that email is simply the key their systems search on. That
is an engineering constraint honestly labelled as one, and it is the first time
anyone has drawn that line the right way round.

**What they refused, and how.** They will not name customers, explicitly and on
the record — which is the fallback the gotcha above asks for, so it counts as an
answer rather than a dodge. The half that got dropped was the *other* half:
whether they will forward the request to those customers. Re-asked. **Expect the
forwarding question to need asking twice**; it is the one that falls out of a
reply that otherwise engages fully.

**Deletion and opt-out are mutually exclusive here, and they said why.** Marking
someone opted-out means keeping enough of them to recognise them again, so it
cannot be layered on top of a deletion. Any letter asking for both should expect
to be sent back to choose. Decide in advance which you want, and — the useful
move — reply with a *conditional* rather than a question, so the choice does not
cost a round trip: pick one, and name the single fact that would change the
answer.

**They cannot suppress against a customer re-upload, and volunteered it.** A
deletion on a platform fed by customer imports lasts until the next import. This
was point 4 of the letter, the point usually answered evasively or not at all.
See `_SILENT_FAILURES.md` §131.

**The verification gap.** Access requests are gated behind a confirmation link
sent to each address individually, with no consolidated response — so any address
you no longer control is one you cannot be authenticated for, and on a
prospecting platform those are precisely the addresses the records are keyed to.
The counter comes from their own rule: verification protects *disclosure*, and
deletion discloses nothing, so **ask for the deletion to apply to every address
regardless of what the verification links do**. Full analysis in
`_SILENT_FAILURES.md` §131.

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

## Outcome (6 Oct 2026)

Fully closed on the controller side: no match on any of twelve email addresses
for either access or deletion, and an explicit, repeated refusal to name or
contact customer instances. That refusal is final-sounding but not evasive --
they gave the reason (never disclosing personal data to a third party, even in
the form of a request) and stated it the same way twice, six weeks apart. If the
subject believes a specific Outreach customer holds their data, the only route
left is writing to that customer directly; Outreach itself is exhausted as a
contact point.
