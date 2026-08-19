# Real Performance Marketing

- **Email:** ConsumerInquiries@RPMleader.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** rpmleader.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Performance marketing and lead generation. Same provenance-first structure as reallygreatrate - exact form URL and consent wording, recipients with a direction to delete, do-not-resell suppression, internal DNC list as a separate ask, and aged/recycled inventory held apart from the live database. Opened by asking them to enumerate every brand and domain they operate, since the parent name shares nothing with the consumer-facing sites in this sector and only they can list them.

## Steps

**There is no route a member of the public can use.** Recorded so nobody
re-derives it.

1. **All three addresses on their own privacy policy are rejected by their own
   mail server** — `ConsumerInquiries@`, `connect@` and `info@rpmleader.com`, each
   with `550 5.7.1 Recipient address rejected: User email address is marked as
   invalid` from `mx1-us1.ppe-hosted.com`.
2. The only form on the site is a **sales enquiry form** at `/contact-us-1`, and
   its required `I am` dropdown offers *Agency, Affiliate, Affiliate Network,
   Brand Platform* — **no consumer option**.
3. What is left is their own admission that they are a registered California data
   broker.

## Gotchas

**Note the SMTP code: 5.7.1, not 5.1.1.** That distinction matters and it
is easy to skim past. `5.1.1` is *user unknown* — the mailbox does not exist.
`5.7.1 ... address is marked as invalid` is a **policy rejection**: the mail
system knows about the address and is configured to refuse it. All three
published addresses fail the same way, which points at a recipient-validation
list that simply does not include the addresses the company publishes.

Practical consequence: **there is no address worth guessing at this domain.** A
`privacy@`, `legal@` or `dpo@` probe will fail identically, because the failure is
not about which mailbox exists.

**The sales form cannot be completed truthfully.** Its required capacity dropdown
has four business categories and nothing for a member of the public — the same
shape as Nielsen's rights form, but here it blocks submission outright rather
than merely misfiling the request. The full request was written into its
free-text box and the form was submitted; it errored on the missing dropdowns.

> **Do not tick "Agency" to get past it.** It is a false statement about who is
> asking, it is exactly the misrepresentation these forms exist to prevent, and a
> request obtained that way is worth less than no request — it hands them a clean
> reason to disregard it.

**The lever that remains is their own privacy policy**, which states:

> *"Company acts as a data broker, as that term is defined in California Civil
> Code section 1798.99.80 et seq."*

That is a self-declaration of registration with the California Privacy Protection
Agency, and registration carries statutory obligations about being contactable.
A broker that publishes three addresses and refuses all three is a straightforward
complaint — see the handoff note. Whether it is worth filing is the subject's
call, not an agent's.

**Trading name worth recording:** the site header links to an Inc. profile for
**Best Case Leads**, a name the privacy policy never mentions. Company badges and
award links in a header are a cheap source of alternate trading names.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
