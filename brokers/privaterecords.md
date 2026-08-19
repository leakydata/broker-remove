# Privaterecords

- **Opt-out:** https://www.privaterecords.net/api/helper/optOutLight/search
- **Email:** support@privaterecords.net — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** privaterecords.net
- **Priority: 2.**

## Status

- Current: `captcha_blocked` (updated 2026-08-19) — search form staged; an invisible CAPTCHA silently swallows the submit, and a reply-to-acknowledge step follows
- Note: People search. Consolidated ask covering privaterecords.net AND privatereports.com: the two share nameservers (Namecheap's registrar-servers.com) and sit on adjacent IPs at the same cloud provider, with closely similar branding. Stated the inference and its evidence and invited correction rather than asserting it. Wrote to both sites so either can answer for both. Standard five people-search asks including the criminal/court-entry disclosure, since 'private records' branding usually implies court data.

## Steps

1. Email `support@privaterecords.net`. A named human replies within a day with the
   full process — worth having in writing before touching the form.
2. Go to `privaterecords.net/api/helper/optOutLight/search`. Enter first name, last
   name, city, state. Zip / phone / email are optional.
3. Press SEARCH. **Expect a CAPTCHA challenge** — see Gotchas if nothing happens.
4. Identify **your own** listing. Do not pick a same-name stranger; check city and
   age against what you know.
5. Submit the email address to validate ownership.
6. **Find the acknowledgement email and REPLY to it.** This is the step that
   actually authorises removal; without it nothing happens.
7. Phone fallback, staffed 8am–11pm EST: **(888) 270-9304**. A human who can locate
   the record sidesteps the form entirely.

## Gotchas

- **The submit can fail silently.** A hidden `captchaId` field sits empty and the
  page simply does not respond — no error, no message. See [[_SILENT_FAILURES]]
  §59. Do **not** read that as "no listing found".
- **The reply-to-acknowledge step is easy to miss**, and they say so themselves:
  *"If you do not respond to the email, your listing will NOT be removed."* Check
  spam and trash.
- **No account is needed** — if anything asks you to register, you are on the wrong
  flow.
- They pre-empt the cache trap: if the name still appears, *"you may need to clear
  your browser cache or try your search a few days later."*
- Scope questions went unanswered on the first pass. Ask them again explicitly; the
  process answer is thorough but says nothing about what the removal covers.

## Verification

Re-run the same search after a few days, with cache cleared — their own suggested
method.

Their definition of an empty result is the useful part, and it is quotable:

> "If you are unable to locate your listing then it means your information was
> never collected, or has already been removed."

That converts a blank search into a recordable negative — **but only once you know
the search actually ran.** Confirm the results page rendered before trusting an
empty one, for the reason in Gotchas.

Keep the email thread: there is no ticket number, so the correspondence and the
acknowledgement reply are the only artifacts.

## A clear process, a silent form, and a second step that decides everything (updated 2026-08-19)

Support replied within a day, signed by a named person, with the most complete
process description in this project so far. Three parts are worth quoting.

**No account required — stated unprompted:**

> "You do not need to have an account with us to remove your listing."

**The null result is given a meaning**, which is unusual and genuinely useful:

> "If you are unable to locate your listing then it means your information was
> never collected, or has already been removed."

**And the step that actually decides the outcome:**

> "When you locate your listing, submit your email address to validate your
> ownership of the information. An acknowledgement email will be sent to you
> immediately. **Respond to the acknowledgement email to authorize removal of your
> listing. If you do not respond to the email, your listing will NOT be removed.**
> If you do not see your acknowledgement email, check your SPAM and TRASH folders."

> **A one-step opt-out that silently requires a second confirmation is the most
> common way a removal request dies.** The requester submits, sees a success page,
> and stops. The acknowledgement lands in spam. Nothing further happens, and
> nothing ever says so.

Credit where due: they wrote that sentence down. Most operators running the same
double-opt-in do not, and the failure is then invisible from both ends.

## The form does nothing, and the reason is a hidden field

The search page at `/api/helper/optOutLight/search` takes first name, last name,
city, a state dropdown, and optional zip / phone / email. Filled correctly and
submitted, it does **nothing** — no results, no error, no validation message. The
page simply sits.

The form posts to its own URL and carries:

    <input type="hidden" name="captchaId" value="">

Empty. So the submission is almost certainly being rejected for want of a CAPTCHA
token that was never issued to an automated session.

> **An invisible CAPTCHA fails by doing nothing at all.** There is no challenge to
> see and no error to read — and on *this* site that is especially bad, because
> "your search returned nothing" is a meaningful answer per their own message. A
> broken form and a clean record look identical.

Check for a hidden `captcha*` field before concluding a search found nothing:

    Array.from(document.querySelectorAll('input[type=hidden]'))
         .map(i => ({n: i.name, v: i.value}))

An empty one where a token belongs means the answer on screen is not an answer.

## What to hand off

The whole flow, because it cannot be split: press SEARCH (expect a challenge),
identify **your own** listing rather than a same-name stranger, submit the email
address, then **find and reply to the acknowledgement email**. There is a phone
fallback staffed 8am–11pm EST, which is worth knowing — a human who can locate a
record sidesteps the form entirely.

## What the reply did not cover

Nothing about scope: suppression versus one-time removal, whether multiple matching
records are handled together, whether removal reaches the subject's name where it
appears on **other people's** listings as a related person, whether any criminal or
court entry is attributed, or FCRA scoping. All re-asked.

The sibling-site question also went unanswered — and it had arrived as two mangled
`google.com/url?q=…` redirects rather than two domain names (see
[[_SILENT_FAILURES]] §51), so it may simply have been illegible. Re-sent as plain
text with no links.

> **When a broker ignores one question but answers the rest carefully, check how
> that question arrived before assuming it was dodged.**
