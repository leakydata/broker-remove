# Dtn

- **Email:** privacy@dtn.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** dtn.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-18)
- Note: privacy@dtn.com auto-replied that consumer privacy requests sent there 'will not be processed and will be deleted' - the published privacy address explicitly destroys them. Real route is the Data Rights Exercise Request form at /do-not-sell-my-information-form/, which uses CHECKBOXES so one submission covers all six rights. Staged with all six ticked; only the arithmetic anti-bot dropdown and Submit remain. Phone alternative 1-800-485-4000, ask for the Legal Team of the DPO.

## Steps

**Do not email `privacy@dtn.com`.** Their autoresponder says, in terms, that a
consumer request sent there is destroyed. Use the form.

1. Go to `https://www.dtn.com/do-not-sell-my-information-form/` — the **Data
   Rights Exercise Request** form, despite the do-not-sell URL.
2. Fill first name, last name, email, telephone, ZIP.
3. **Tick every right you want.** They are checkboxes, not a single-select, so one
   submission covers all of them.
4. Answer the arithmetic anti-bot dropdown, tick the attestation, submit.

Phone alternative: **1-800-485-4000**, ask for the Legal Team of DTN's Data
Protection Officer. Postal address in section 23 of their Privacy Statement.

### The original approach, kept for the record

1. Email `privacy@dtn.com`.
2. Ask which system held a record — subscriber, marketing, event registration, or
   third-party compiled — and treat each as a separate request.
3. Raise the property-linked angle explicitly (see below).
4. Say plainly that a written "we hold nothing" is an acceptable and welcome
   answer.

## Gotchas

## The published privacy address deletes consumer requests

This is the starkest version of the auto-reply-as-gate pattern in this project.
Their autoresponder does not merely redirect — it tells you the request has been
destroyed:

> *"Persons or consumers trying to manage their personal data maintained by DTN
> cannot do so by this e-mail address. Please follow the process listed below to
> submit any requests to DTN involving the management of your personal data. Any
> privacy requests sent to this e-mail will not be processed and **will be
> deleted**."*

Two things worth separating here. The **honesty is genuinely useful** — most
brokers in this position send a vague redirect that a reader can easily mistake
for an acknowledgement, and this one leaves no room for that. But the underlying
arrangement is still that `privacy@` — the address every scraper, every registry
and every reasonable consumer will try first — is a hole in the floor.

Anyone who wrote there and did not read to the end of the auto-reply has a
destroyed request and a mailbox that appears to say otherwise. See
`_SILENT_FAILURES.md` §5 and §11.

## Their form is the counter-example worth knowing

The Data Rights Exercise Request form offers the rights as **checkboxes**:

    Delete My Personal Data
    Do Not Sell or Share My Personal Information
    Limit the Disclosure or Use of My Sensitive Personal Information
    Access to and/or correction of My Personal Data
    Objection or restriction to the processing of My Personal Data
    Transfer my Personal Data to another party
    Withdrawal of my consent previously provided to DTN
    Other

So one submission exercises **all** of them. Compare `dataaxle.md`, where the same
list is a single-select dropdown and each right costs a separate submission —
identical information, one interface choice apart, and the difference decides
whether a consumer who wanted deletion *and* opt-out gets both or one.

Worth ticking **"Withdrawal of my consent previously provided to DTN"** even where
you never gave any. Some brokers assert deemed consent through the privacy policy
itself (see `dataaxle.md`), and withdrawing a consent you are said to have given
costs nothing and forecloses that argument.

The anti-bot check is an arithmetic dropdown rather than an image challenge, plus
a Cloudflare widget that clears itself. Cheap for a person, so this is a one-minute
hand-off rather than a real obstacle.

## What to ask for

A business spanning agriculture, energy, weather and analytics, sold mostly to
companies. The useful move is to name the estates you want searched, because a
single privacy mailbox at a diversified company will otherwise answer for whichever
system the responder happens to own.

**The property-linked angle is the one worth raising.** Agricultural and energy
data is frequently keyed to a *thing* rather than a person — a farm, a holding, a
meter, a tank, a delivery point, a parcel. Where that thing is at the subject's
address, the record is reasonably linkable to them, and the consumption, yield or
delivery history attached to it is personal data in substance even though no name
appears in the row.

**Invite the negative explicitly.** For a broker who may genuinely hold nothing,
saying so in the letter — *"a statement that no record exists is a real and useful
answer and I will treat it as closing the matter"* — makes the cheap reply the one
you actually want, rather than leaving silence as the path of least resistance.
That converts a likely non-response into a recordable `not_found`.

## Verification

Nothing public to search. A written "we hold no record" closes this as
`not_found`; silence does not, and the two must not be recorded the same way.

## The Submit button is hidden until the arithmetic question is answered

The form appears to have no way to submit it. Fill in every field, tick every
right, watch the Cloudflare widget go green, scroll to the bottom -- and below the
widget there is nothing but the footer.

The button is not missing. It is in the page's markup as a normal
`<button type="submit">`, but it is not rendered, and it stays that way until the
anti-bot dropdown labelled **"What is 40+55?"** has an answer selected. That
dropdown sits in the top block of the form, beside the Zip Code field, well above
the rights checkboxes and about a screen and a half above where the button will
eventually appear. Nothing on the page connects the two.

**Why this is worth writing down.** The obvious reading of "there is no Submit
button" is that the form is broken, and the obvious response is to give up and use
email -- which for DTN is a dead end, because `privacy@dtn.com` discards consumer
requests unread. So a hidden button on the only working route reads as no route at
all.

The tell is that the field is optional-looking: it has no red asterisk, unlike
First Name, Email, Zip Code and Request Details. An unmarked field that gates
submission is the inverse of the usual pattern, where the asterisks tell you what
is required.

**Check the markup before concluding a form is broken.** A `<button>` that exists
but does not render is a different problem from a `<button>` that was never there,
and only the first one has a fix you can reach.

