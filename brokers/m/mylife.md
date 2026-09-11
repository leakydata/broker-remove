# MyLife

- **Email:** privacy@mylife.com  (verified — replies via `support@mylifecs.atlassian.net`)
- **Opt-out:** https://www.mylife.com/ccpa/index.pubview
- **Priority: 5.**

## What makes MyLife different

MyLife publishes a **"Reputation Score"** — a scored, editorialised profile page,
not a plain directory listing. Ask for the **page removed in full**, not merely
delisted from search: a page that no longer appears in results but still resolves
at its URL has not been removed.

## Gotchas
- **Watch for paid-subscription gating.** MyLife has a long history of steering
  people toward a paid account to "manage" their profile. The statutory request
  costs nothing. State up front that you will not create an account and will not
  pay — the letter template does this.
- Their reply arrives from **`support@mylifecs.atlassian.net`**, which looks
  unrelated to MyLife at a glance and is easy to mistake for spam. Ticket refs
  look like `MCC-3027423`.
- They handle requests "in the order received" with **no stated SLA**, so expect
  to follow up rather than assume silence means progress.

## Verification
Search mylife.com for name + city after ~14 days, and check the profile URL
directly — not just search results.

## Confirmed — with a caveat in their own wording

Ticket `MCC-3027423`, handled through an Atlassian/Jira service desk rather than a
privacy platform:

> *"We searched using the name and/or email address provided and have deleted your
> user account and access to MyLife.com along with any profiles that may have been
> published on MyLife.com containing your information. This note confirms that your
> user account has been deleted. As part of your deletion and opt-out, we have
> unsubscribed your email address. Please allow 3-5 business days for your account
> and profile to be completely removed."*

Good: it names the account **and** any published profiles, it treats deletion and
opt-out together, and it gives a timeframe rather than leaving it open.

**The caveat is the first clause.** *"using the name and/or email address
provided"* — name and email only. The letter supplied ten addresses and twelve
telephone numbers, and none of them appears to have been used as a search key.

For a people-search index that is a real gap, because the index is built on
address and phone history: a record filed under a former address, with a name
variant or an old number and no email attached, is exactly what a name-and-email
search does not reach. The confirmation is honest about its own scope, which is
more than most manage — but the scope is narrower than the request was.

**So: `confirmed`, and follow up anyway.** Ask them to re-run the search against
the former addresses and disconnected numbers, and to say whether anything
additional was found. A confirmation that tells you which keys it used is a
confirmation you can check; treat the disclosure as an invitation.

Re-check after the stated 3-5 business days rather than immediately — a removal
with a propagation window will still be visible on the day it is granted.

> **Correction (2026-08-25):** A duplicate-detection error in that day's run sent an unnecessary second request to `membersupport@mylife.com`, on top of the already-open thread documented above. The exclusion check matched only exact addresses seen in a partial Sent-folder scan, and this broker's registry `email_to` had drifted from the address actually used historically — so it looked unsent when it wasn't. No new information was requested; treat the status above as authoritative. **Lesson: check this playbook's own `Current:` status before treating a registry email_to as evidence a broker is unsent — it is not reliable on its own.**
