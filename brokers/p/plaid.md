# Plaid

- **Opt-out:** https://my.plaid.com/data-subject-request-form
- **Email:** none published — `email_verified_by: no_address_published`
- **Method:** web_form
- **Priority: 4.**

## Status

- Current: `manual_required` (updated 2026-09-16)
- Note: Adopted from the shared ledger: another agent recorded 'manual_required' on 2026-09-06. No detail is carried across — re-read the broker's own reply before relying on this.

## Steps

<!-- Not yet attempted. The form needs a browser; the extension was unavailable
     on 12 September. -->

1. Open https://my.plaid.com/data-subject-request-form.
2. Values are in `data/profile.json`. Requesting **on behalf of myself**, never
   as an authorised agent. Use the correspondence address from that file for
   every field and for the confirmation link.
3. Ask for deletion, opt-out of sale/sharing, and a forward-looking suppression.

## Gotchas

- **Read this before deciding what to ask for.** Plaid is a financial data
  aggregator: it sits between a consumer's bank and an app, and holds account
  and transaction data obtained *with* the consumer's permission, granted inside
  whichever app asked for it. That makes it a very different case from a
  compiler, and the registry's `category: compiler` (normalised from `financial`
  on 2026-09-01) understates the difference.

  Two consequences:

  - **Much of what they hold is probably held as a SERVICE PROVIDER** for an app
    the subject connected, not as a controller in their own right. A deletion
    request answered honestly from the processor side achieves nothing (§444).
    Ask them to say which side each holding falls on, and to name the app, so
    the request can be directed rather than assumed.
  - **Some of it is likely subject to financial retention obligations** and
    cannot be deleted. That is a legitimate limit. Ask them to state which parts
    and on what basis, and to apply the request to the rest — an accurate
    partial answer is worth more than an over-broad one.

- **The useful question here is which connections exist at all.** If the subject
  connected an account years ago through an app he no longer uses, the link may
  still be live and he has no way to see it from outside. Ask for a list of
  connected institutions and the apps that hold a token, and for those tokens to
  be revoked. That is the outcome that matters; deletion of stored transaction
  data is secondary to cutting the ongoing access.

- Do NOT supply bank credentials, account numbers or a Social Security number,
  whatever the form asks for. If the form will not proceed without them, stop:
  that is the finding, and it is worth more than the submission.

## Verification

Their own answer, plus — if they list connected institutions — whether that list
is empty on a re-check. There is no public page to search.

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
