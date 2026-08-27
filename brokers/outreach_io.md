# Outreach Io

- **Opt-out:** https://preferences.outreach.io/form/opt_out?locationCode=US
- **Email:** security@outreach.io — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** outreach.io
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Sales engagement platform; sent to security@ with support@ copied, since verify_emails rated the published support address better while the registry kept the purpose-built one. Same processor-first framing as onemodel: name the customer accounts holding the record, because 'contact the controller' is unactionable without knowing which controller. Carried the business-vs-consumer-data pre-empt - if they claim a B2B carve-out, name the basis rather than declining quietly, and apply the request in full to everything outside it. A business email address is still an address that reaches the person and still the key that joins the rest of a profile.

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
