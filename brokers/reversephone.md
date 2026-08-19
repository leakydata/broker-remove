# Reversephone

- **Opt-out:** https://www.reversephone.com/svc/optout/search/optouts
- **Email:** privacy@reversephone.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** reversephone.com
- **Priority: 2.**

## Status

- Current: `pending`

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

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
