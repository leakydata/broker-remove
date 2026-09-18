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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Insightbridge LLC
- **Registered address:** 1309 Coffeen Avenue, Suite 14998, Sheridan, WY,
  82801
- **Filed contact email:** membersupport@mylife.com
- **Filed phone:** 8884661066
- **Website:** https://www.mylife.com

*Source: `data/registries/registry.csv`.*

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.mylife.com/ccpa/index.pubview
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `membersupport@mylife.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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
