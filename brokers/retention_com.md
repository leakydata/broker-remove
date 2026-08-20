# Retention Com

- **Opt-out:** https://app.retention.com/optout/
- **Email:** support@retention.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** retention.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-19)
- Note: PROCESSED: 'We have processed your Opt-Out removal request. [EMAIL] has been marked for removal in our vendor database.' Cc'd optouts@retention.com. SCOPE IS NARROW AND WORTH NOTING: the confirmation names ONE email address, and says 'marked for removal' in a 'vendor database' rather than deleted. Retention.com's product is identity resolution on hashed email, so the other eleven addresses in the request -- and any hashed forms -- are not covered by that sentence. Follow up to confirm all addresses and whether this is deletion or suppression.

## Steps

1. Write to `support@retention.com` — the only address
   published. Ask to be redirected to a privacy mailbox.
2. Ask for the **resolution** to be deleted, not a row. See below.

## Gotchas

**Name what the product actually does, or the request misses it.** This
category identifies an anonymous website visitor and returns their email address
to the site's owner — so the person being identified never gave that owner
anything and has no account to delete. A request phrased as "delete my account"
or "unsubscribe" touches none of it.

**The ask is the resolution, not the record:** the mapping between a cookie
identifier, device identifier, IP address or hashed email and a name or email
address; the pixel- or tag-based match; and the graph edges underneath.

> **Retaining the ability to re-resolve someone from their next page load is not
> a deletion.** It is a pause that ends the moment they visit a customer's site.
> So the operative ask is a permanent **do-not-resolve / do-not-identify**
> suppression — and it is worth demanding a direct yes or no on whether the
> system supports one.

**Three questions that locate the actual holder:**

- Which of their **customers** is the record associated with? A consumer cannot
  know whose website produced a match, so "contact the controller" is
  unactionable without a name.
- **Where does the underlying identity graph come from?** Resolving a cookie to
  an email requires a pre-existing graph, built or licensed. If licensed, that
  provider holds the record and a suppression here does not reach it.
- Has the address already been **supplied to a merchant**? That copy does not
  come back.

**Search hashed, not plaintext.** The match is made against the hash. A search of
the plaintext address alone can come back clean and be perfectly truthful.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Acknowledged, with a stated clock (updated 2026-08-19)

> "We have received your Opt-Out removal request. We will process your request
> within 7 business days.
> -The Retention.com Privacy Team"

Short, unambiguous, and it names a deadline — which makes it more useful than the
usual "we have received your message". Re-check on or after **2026-08-28**.

> **An acknowledgement that states a number is worth recording as a date, not as a
> status.** "Within 7 business days" is a commitment you can hold them to; "we
> appreciate your patience" is not. The difference decides whether a follow-up has
> anything to cite.

Note the wording: they call it an **Opt-Out removal request**. The original letter
asked for deletion, opt-out *and* suppression, so the confirmation — when it comes
— needs reading for which of the three it actually covers, and following up if it
has quietly narrowed to the opt-out alone.

See [[_DEFLECTIONS]].

## Processed — and read the scope of the sentence (updated 2026-08-19)

> "We have processed your Opt-Out removal request. `<one email address>` has been
> marked for removal in our vendor database."

Recorded `confirmed`, because it names a completed action. But three details in one
short sentence narrow it considerably, and all three are worth chasing.

**It names one address.** The request listed twelve. A confirmation that echoes
back a single identifier has confirmed that identifier — see [[checkpeople]] for
the same shape. For this company the gap matters more than usual, because the
product resolves identity across addresses: the eleven not named are exactly the
ones a match would have found.

**"Marked for removal" is not "deleted".** It describes a flag set, with the
deletion implied and unstated. That may be an accurate description of a queue, or
it may be the whole of what happens.

**"Vendor database" is a scope, not a synonym for "our systems".** An identity
company holds hashed email, cookie and device identifiers, and the graph edges
between them. Nothing in that sentence reaches any of it.

> **A confirmation is a sentence about a specific store. Read which store it
> names.** "Marked for removal in our vendor database" and "deleted from our
> systems" are different claims, and the first is fully compatible with the record
> surviving everywhere that matters.

**Follow-up worth sending:** all twelve addresses confirmed, hashed forms included;
deletion versus suppression; and whether the identity graph edges go with it.

Note the reply arrives from `support@` with `optouts@retention.com` on **Cc** —
the latter is the better address for the follow-up.
