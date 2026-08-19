# Path2response

- **Email:** agents@path2response.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** path2response.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19) — email verification link clicked; OneTrust returned a confirmation page
- Note: Data co-operative. The letter is ordered around the one fact that makes a co-op different: the data did not originate with them and deleting their copy does not stop it arriving again. Asked first WHICH MEMBERS contributed records and when, then whether deletion stops future contributions or only removes today's copy, then recipients - with permanent do-not-add suppression at ingest as the actual ask. Also asked for transaction/response HISTORY and derived scores, not just name-and-address rows: in response data the behavioural history is the product and it survives a contact-record deletion. Sensitive inferences named individually rather than covered by a general phrase.

## Steps

1. Write to `agents@path2response.com` (verified). Ask them
   to forward it if there is a dedicated privacy mailbox.
2. Order the asks around **contribution**, not deletion — see below.

## Gotchas

**A co-operative is not a list owner, and the difference decides the letter.**
Records are contributed by participating members and pooled. So the data did not
originate here, and deleting the pooled copy does not stop the same member
re-contributing it next quarter. An unsuppressed deletion in a co-op simply
reverses itself, and the confirmation is worded identically either way.

Ask in this order:

1. **Which members contributed records about me, and when?** Names if possible;
   categories and a count if not, so the consumer knows how many separate parties
   they must write to.
2. **Does deletion stop future contributions?** Ask for a permanent do-not-add
   list applied *at ingest*, so a matching contribution is rejected rather than
   published and later removed.
3. Recipients, then deletion.

**Ask for the response history, not the contact row.** In response data the
behavioural record — transactions, purchases, donations, responses — is the
product. A deletion scoped to name-and-address leaves it, and leaves every
modelled score derived from it.

**Name sensitive inferences individually.** Health, financial distress, religion,
politics, ethnicity, presence and age of children, and life-event tags such as
bereavement, divorce or a new baby. A general phrase does not reach them because
they live in a different table from the contact record.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->


## Outcome: the published address is for agents only

`agents@path2response.com` auto-replies with authorized-agent instructions
**regardless of what the message says**. The letter opened by stating plainly
"I am the consumer, writing about my own data. I am not an authorized agent" —
and the reply demanded the consumer's signed permission form.

The address answered the wrong question, correctly, because it only knows one.
That is a distinct failure from a template that ignores content: this mailbox is
scoped to a role the sender explicitly disclaimed, and there is no consumer
address published beside it.

**Consumers should use the OneTrust portal** the auto-reply links to. It serves
consumers perfectly well; nothing on the way in says so.

## Gotchas

**Their production portal URL contains `/draft/`.** The link handed out by their
own autoresponder points at a draft-state OneTrust form. It works today. But a
draft can be republished at a different URL without notice, and anyone who
bookmarked it — or any playbook that recorded it — would find a dead link with no
announcement. Re-derive the URL from the autoresponder rather than trusting a
stored copy.

**Request type is single-select.** *Do Not Sell / Opt-Out*, *Delete My Data* and
*Access My Data* are mutually exclusive, so **deletion and opt-out need two
separate submissions**. Same trap as Data Axle: one run looks complete and asks
for half of what was intended.

**reCAPTCHA on submit**, plus a Yes/No affirmation that the submitter is the
consumer.

## Verified: request FYFSSK3KGS (updated 2026-08-19)

Email confirmation clicked; the portal redirected to `#/verify/verifySuccess/…`.

Request ID **FYFSSK3KGS**, type *Delete My Data*, submitted 2026-08-19 13:18 UTC,
footer "Path2Response Privacy Team", on the US `privacyportal.onetrust.com`
tenant.

The submission recorded an explicit attestation, which is worth quoting because it
is the form of words these portals use to distinguish a consumer from an agent:

> "By clicking 'Yes,' I affirm that I am the consumer (or authorized agent with
> attached signed permission form) whose personal information is the subject of
> this request."

> **Answer that question as the consumer, not as an agent, when it is your own
> data.** Ticking "authorized agent" invites a demand for a signed permission form
> that does not exist, and turns a one-step request into a rejected one.

One rough edge in the notification itself: the template shipped with its own
authoring placeholders still visible — *"Email notification content will be
inserted here. Go to Templates to edit content. Button Preview"* — rendered above
the real message. Harmless, but a useful reminder that the branding layer of these
portals is edited by hand and can be wrong without anything failing.

See [[_SILENT_FAILURES]].
