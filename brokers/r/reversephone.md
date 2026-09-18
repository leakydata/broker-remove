# Reversephone

- **Opt-out:** https://www.reversephone.com/svc/optout/search/optouts
- **Email:** privacy@reversephone.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** reversephone.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Name-index search returned 'No exact match for [PERSONAL]' across all states -- no PA record, none born Jan [YEAR]. Did NOT click Proceed to Opt Out on any of the ~100 same-name strangers. NOT marked not_found, because the opt-out tool searches by NAME while the product is a REVERSE PHONE lookup: the number-keyed index is not reachable from that form, so a clean name search does not prove absence. Replied pressing (a) whether name opt-out also clears number records, (b) direct search of 12 numbers, (c) both-direction removal, (d) suppression-vs-one-time, (e) stored-vs-pass-through. Better contact found published twice on the opt-out page itself: privacy@reversephone.com (support@ answered with a form link).

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.reversephone.com/svc/optout/search/optouts
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `privacy@reversephone.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## The name search that cannot reach the number index (updated 2026-08-19)

Customer care answered a detailed privacy letter with the standard self-service
redirect:

> "If you would like to remove your listing from ReversePhone's people search
> results, we provide an easy online opt-out process. ... click the link and use
> the search to locate and select your record. You will then receive an email
> asking you to click to verify your request."

The form works. Cloudflare interstitial for ~8 seconds, then First Name / Last
Name / a state combobox, then a result list with a **Proceed to Opt Out** button
per record. The state control is a custom `DIV` — `form_input` refuses it — but
leaving it on **All** is better anyway, because it catches records filed under a
prior state.

The search returned:

> **"No exact match for `<first> <last>`"**

followed by roughly a hundred other people of the same name. No record in any of
the subject's current or prior cities, and none with the right birth month.

### Nothing was clicked, and that is the point

Every one of those ~100 rows has a live opt-out button next to a stranger's name,
date of birth, relatives and address history.

> **Do not opt out a record you have not positively identified.** Suppressing
> someone else's listing is not a harmless over-reach — it is acting on a third
> party's data without their knowledge, from a page that invites you to do it
> with one click and asks for no proof at all.

### Why "no exact match" is not `not_found` here

This is the trap the whole entry turns on, and it is a property of the *product*,
not of this site's honesty.

> **The opt-out tool searches by name. The product is a reverse phone lookup.**
> Those are not the same index, and one is not reachable from the other.

A reverse-lookup index is built from *numbers* — including disconnected and
reassigned ones, which may sit in the data attached to a stale name string, a
carrier record, or no name at all. A person can search the name index, read "no
exact match", conclude they are absent, and still be sitting in the phone index
under a number they gave up twenty years ago. A clean name search does not prove
absence; it proves absence *from the name index*.

So the tracker keeps this as `submitted` with the negative recorded in the note,
not as `not_found`. The negative is real and worth having. It is just not the
question that was asked.

### What to press for, since the form cannot do it

1. **Does a name opt-out clear the number-keyed records, or only the profile?**
   If those are separate stores, the support template is telling consumers a name
   search is the whole answer when it is not.
2. **A direct search of the numbers themselves**, supplied in the reply, with a
   count of matches. Zero, stated unqualified, closes it.
3. **Removal in both directions** — number-to-name *and* name-to-number. Clearing
   one leaves the fact retrievable from the other side, and no confirmation email
   will ever say which was done.
4. **Carrier, line-type, portability and location enrichment** on those numbers,
   and any appearance as a "related person" on somebody else's number page — a
   relative-graph entry is a record about you living on a page that is not yours,
   and a search of your own name will never surface it.

### The better address is printed on the opt-out page itself

The opt-out page publishes **privacy@reversephone.com** twice, in its own footer.
The letter had gone to `support@`, which is why it came back as a form link from
customer care.

> **Before accepting the support queue's answer, read the opt-out page's own
> footer.** These sites routinely publish a real privacy address on the page they
> send you to, and it is a different queue from the one that answered you.

Template note: the wording of this reply is **byte-for-byte the wording
PeopleLooker sent on the same day**, down to "Thanks for reaching out" and the
"If you are having trouble with the online process" paragraph. That is
[[_BROKER_FAMILIES]] signal 7 — identical support templates — and it means the
questions above should be put to the family once, not per brand.

See also [[_DEFLECTIONS]] on "here are the steps to use our form".

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
