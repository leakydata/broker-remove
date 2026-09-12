# Secretinfo

- **Email:** support@secretinfo.org
- **Opt-out:** https://www.secretinfo.org/api/helper/optOutLight/search
- **Method:** email, with a bot-gated self-service form as the documented alternative
- **Domain:** secretinfo.org
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: Sent 2026-08-20 07:20 UTC as ONE letter to the eleven optOutLight brands that have not confirmed, citing the five that have. This is the _DEFLECTIONS.md 40 move executed: the four same-template confirmations of 20 August, plus privaterecords on 19 August, quoted verbatim with their dates, and then a single yes/no question a database can answer - 'Was this site included in the removal that was applied for me on those five sites?' Explicitly does NOT ask anyone to confirm corporate structure, which is the thing a support agent cannot answer and which invites escalation to someone who says less. Three exits offered, all of which close the matter: yes (recorded complete), no (apply it now), or an unqualified we-hold-nothing. Plus the suppression-vs-one-time question framed so that 'one-time, we do not suppress' counts as a good answer rather than a refusal, the relatives/associates cross-listing question, and - specific to the inmate/sealed-record/mugshot brands in this group - a request for the SOURCE of any criminal entry whether or not it is removed, since an entry hidden rather than corrected returns on the next ingest.

## Steps

1. **Do not write to this site alone.** It is one of sixteen brands on a single
   platform — see Gotchas — so a letter scoped to one domain buys a removal scoped
   to one domain.
2. Email `support@secretinfo.org` with the full identifier list, naming all sixteen sites
   and asking which were actioned.
3. **Cite the precedent.** [[privaterecords]], on the same platform, granted this
   same request for this same person on 2026-08-19 and did it *from the email
   thread* without any form being completed.
4. Expect the platform's standard reply: no account needed, a search URL, and a
   two-step confirmation whose second step is easy to miss.
5. If pushed to the form, note that it is bot-gated and can refuse silently — see
   [[_SILENT_FAILURES]] §59.

## Gotchas

- **Sixteen brands, one platform.** Every one serves the same non-obvious route,
  `/api/helper/optOutLight/search`. DNS is no help: they all sit on Namecheap's
  shared registrar-default nameservers, which is not a family signal at all.
- **The reply-to-acknowledge trap.** The platform's own wording: *"Respond to the
  acknowledgement email to authorize removal of your listing. If you do not respond
  to the email, your listing will NOT be removed."* Check spam and trash.
- **Fronts are deliberately differentiated** — different signer names, phone
  numbers and postal addresses per brand. Disagreeing contact details are not
  counter-evidence to the family.
- Two sibling sites were each asked directly whether they operate a named sibling.
  Neither said yes and neither said no; the question was simply not addressed.

## Verification

Re-run the site's own search after a few days with cache cleared — the platform
pre-empts the cache trap in its own replies.

Their stated meaning for an empty result is worth quoting back if needed:

> "If you are unable to locate your listing then it means your information was
> never collected, or has already been removed."

**But only trust an empty result you watched load.** The search form carries a
hidden `captchaId` and can reject a submission silently, rendering a page
identical to a genuine negative.

See [[privaterecords]] for the fully worked example and [[_BROKER_FAMILIES]] for
the sweep that found this site.

> **Update 2026-08-19: the family is SIXTEEN, not thirteen.** Mining the A-record
> sweep found `checksecrets.com`, `inmatessearcher.com` and `sealedrecords.net`
> sharing an address with an already-confirmed member, and the path test then held
> for all three. Note that these three are branded around **inmate searches, sealed
> records and mugshots** — so the criminal-record question in the standard letter
> stops being boilerplate for this family. See [[_BROKER_FAMILIES]].
