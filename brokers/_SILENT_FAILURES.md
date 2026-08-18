# Silent failures — requests that look filed but aren't

The dangerous failure in this work is not the broker who refuses you. That one is
loud: you get a bounce, a "we don't accept email", a form that won't submit. You
know to try something else.

The dangerous failure is the one that **looks exactly like success**. You fill the
form, the page says thank you, the tracker says `submitted`, and nothing was ever
filed. Months later you are still listed, still being sold, and you believe you
opted out. Every hour spent on the loud failures is wasted if the quiet ones go
uncounted.

This file catalogues the ones actually encountered, so you can check for them
rather than discover them.

## The rule that catches all of them

**Record `submitted` only when the broker has handed you something.** A reference
number, a ticket ID, a confirmation email, a named human replying. Something that
came *from them* and that you could quote back.

Your own screenshot of a thank-you page is not that. It proves the page rendered;
it does not prove a record was created, and — as below — it does not even prove
the request said what you thought it said.

---

## 1. The form recorded a different request than you selected

**Seen on:** Epsilon (see `epsilon.md`)

A portal offering several request types (delete / do-not-sell / do-not-share)
where the wrong one silently stays selected. Three consecutive "Delete" requests
were logged as "Do not sell". The confirmation page is identical for every type,
so nothing on screen distinguishes them.

Root cause there: clicking a radio **by element reference** gave it a focus ring
without checking it, and the default option remained selected. A focused radio and
a selected radio differ by a few pixels.

**Check:** screenshot the radio group and confirm the circle is *filled*, not
merely outlined, before you fill anything else. If the broker emails a request ID
that names the request type, read it — that is your only independent confirmation.

**Why it matters beyond one broker:** delete and do-not-sell are not
substitutes. Opting out of sale while believing you requested deletion leaves the
record in place indefinitely.

## 2. The request needs a confirmation click you never made

**Seen on:** Epsilon (Delete), Affinity Solutions, PeopleFinders, Radaris

Deletion requests very often require email verification. The pattern:

> "One More Step! Your identity needs to be verified."

Until the emailed link is clicked, **the request does not exist**. The submission
page still congratulated you. Two ways this goes wrong:

- **Nobody clicks it.** The mail lands in a mailbox nobody watches, or arrives
  after you've moved on. One request sat unverified for a day, indistinguishable
  in the tracker from a completed one.
- **The link expires first.** PeopleFinders gives **24 hours**, states so plainly,
  and on expiry says: *"This link has already been used or has expired. Please
  restart the process."* Restarting there means solving a CAPTCHA again.
- **The link is corrupted in the plain-text part of the email.** Multi-part mail
  carries an HTML body and a plain-text fallback, and the fallback is where
  verification links get mangled. Two observed in this project: one lost the `=`
  and the first two characters of its signature, producing *"Security error,
  signature doesn't match"*; another lost the `=` from a `ticketid` parameter.
  Both look like a rejected or expired request rather than a truncated URL.

  **Always take the href from the HTML part**, not the text you can read. If a
  verification link fails with a signature or token error on first use, suspect
  the copy before you suspect the request.

  Across five verification mails from one sender, three were intact and two were
  corrupted, so it is not a property of the sender — it is per-message, and the
  corruption always ate the `=` plus the first character or two after it
  (`&signature=fFoY...` arriving as `&signature<garbage>oY...`). A truncated
  signature produces a confident-looking rejection, not an obvious parse error,
  which is what makes it worth knowing.

**A variant that is easy to miss: the step is a *reply*, not a click.** One
broker's flow ends:

> *"An acknowledgement email will be sent to you immediately. **Respond to the
> acknowledgement email to authorize removal of your listing. If you do not
> respond to the email, your listing will NOT be removed.**"*

There is no link. An acknowledgement that reads like a receipt is the thing you
must answer, and treating it as confirmation leaves the listing live while your
mailbox appears to say otherwise.

**Check:** if a broker mentions verification at all, the request is not filed
until you have seen a page that says something like *"Your request is confirmed!"*
— or, in this variant, until you have **sent a reply**.
Treat submission and verification as **one** step. Search the mailbox for pending
"confirm your email" mail before every session — an unclicked link is a request
you have already paid for and not collected.

## 3. The address bounced

**Seen on:** several — see `_DEFLECTIONS.md` and CONTRIBUTING.md

A bounce arrives in a *different* mailbox thread from the one you sent, so it is
easy to miss. A bounced request and a pending request look identical in a tracker.

- **Hard bounce (550, "address not found")** — the published address is dead. The
  real contact is usually in the privacy policy or a state data-broker registry.
  `privacy@<domain>` published in a directory bounced while the working address
  was an ordinary support mailbox.
- **Soft bounce ("delivery incomplete", retrying)** — not yet a failure; the
  provider retries for ~48h. Don't re-send immediately, but don't just wait it
  out either — check the domain (below), because some of these never arrive.
- **DNS failure ("domain couldn't be found")** — the company is gone. Mark
  `unreachable`; there is nothing to chase.
- **`550 5.7.133 SenderNotAuthenticatedForGroup`** — the published address is a
  Microsoft 365 **distribution group configured to accept internal senders only**.
  It is not dead; it is structurally unable to receive mail from the public:

  > *"The group privacy only accepts messages from people in its organization or
  > on its allowed senders list, and your email address isn't on the list."*

  A company can publish `privacy@` as its privacy contact and have it silently
  reject every consumer who writes to it. The real address is usually in the
  privacy policy — in one case `privacyrequests@` at the same domain. Worth telling
  them about the misconfiguration when you resend; they generally do not know.
- **Google Workspace equivalent** — same failure, different wording:

  > *"the group you tried to contact (privacy) may not exist, or you may not have
  > permission to post messages to the group"*

  A Google Group that is not open to external posting. Note the phrasing invites
  you to conclude the address is wrong ("may not exist"); it exists, it just will
  not accept you. Two of the brokers in this project published such an address —
  one on Microsoft 365, one on Google Workspace — so check the privacy page for a
  second address (`dpo@`, `privacyrequests@`, `legal@`) before assuming the company
  is unreachable.

**Both variants are worth reporting back to the broker when you resend.** A
published privacy contact that rejects every consumer is almost never deliberate,
and a company that fixes it stops turning away everyone else's requests too.

**The soft bounce that is really a dead domain.** A broker whose DNS returns
SERVFAIL produces a *soft* bounce, not a hard one: the mail provider cannot tell
a broken nameserver from a temporarily unreachable one, so it reports "Delivery
incomplete... will retry for 47 more hours" and keeps trying. For two days the
request sits in the tracker looking pending, and only then fails — if you are
still watching by that point.

Check any soft bounce that survives its first day:

```bash
host <domain>            # SERVFAIL or NXDOMAIN means it will never arrive
host -t MX <domain>      # no MX means no mail route even if the domain resolves
```

Two brokers in this project turned out to be dead this way. One announced itself
immediately with "the domain couldn't be found"; the other spent 24 hours looking
like an ordinary slow delivery. Same outcome, very different visibility.

**Check:** search for delivery-status mail *first* in every pass, before replies.

## 4. The form silently discarded what you typed

**Seen on:** Epsilon, Spokeo, LexisNexis, Acxiom, PeopleSearchNow

Several variants, all ending with a field that is empty when you thought it was
filled:

- **`form_input` reports success and leaves the box empty.** Common on
  React-controlled inputs. The tool says it worked. It did not.
- **The page moves between your click and your keystrokes.** Content loading below
  re-anchors the viewport; the click lands correctly, the text goes nowhere. Worse,
  with no field focused those keystrokes can land on *other controls* and change
  them.
- **An entry was typed but never committed.** Forms with "Add Person" / "+" buttons
  discard the typed value unless you press the button, and only complain at the
  very end.
- **An ad overlay resets the form.** A vignette interstitial wiped a completed form
  on one site; a layout shift invalidated element references on another.
- **Values shift down by one field.** Dismissing a cookie banner mid-form moved
  every entry into the next box — the city landed in the State dropdown and
  silently set the wrong state, which would have misstated residency on a legal
  request.

**Check:** screenshot and read the values back before submitting. For fiddly
forms, click *one* field by coordinate, confirm the caret is in it, then **Tab**
between the rest — tab order is immune to the page moving. Verify dropdowns
individually; they often accept programmatic input when text boxes don't.

## 5. The auto-reply was a gate, not a receipt

**Seen on:** Brandwatch

An automated acknowledgement that reads like confirmation, and is actually a
conditional. Buried below the reassuring opening:

> *"If you believe we have collected data on you as a Content Author, please reply
> to this email indicating your desire for us to proceed with your request."*

Nothing happens until you reply. The message opens with *"We confirm receipt of
your message"*, which is exactly the artifact you were told to wait for, so it is
easy to file as done and move on. The request then sits unprocessed forever, with
a receipt in the mailbox proving it was received.

The tell is a conditional in the auto-reply: *if you believe... please reply*, *if
this applies to you, complete...*, *should you wish to proceed, confirm...* Any
sentence putting the next move back on you means the request is parked.

**Check:** read auto-replies to the end rather than filing them on the strength of
the first line. If the body asks for anything at all — a confirmation, a category
choice, a form — the request is not filed until you supply it.

**Then check that your confirmation reached a person.** Replying to the address
the auto-reply came *from* can simply trigger it again: a confirmation sent to
`PrivacyAutoreplyBW@` returned the identical canned message, leaving no way to
tell whether anyone saw it. Send confirmations to the **monitored** address you
originally wrote to, not to the auto-responder, and say you are re-sending and
why. Two identical auto-replies in a thread is the tell.

**Related trap: the category fork.** The same reply split requests into "Users"
(indexed on business email) and "Content Authors" (indexed on social handle), with
different scopes and different answers. Picking the wrong one, or not picking, gets
a truthful "we hold no data about you" that only answers the category you did not
mean. Answer both explicitly.

## 6. The submission failed on their end

Not every failure is subtle. A correctly completed form can return a plain
server-side error:

> *"Error submitting URL — Your request could not be submitted at this time,
> please try again later or contact us by email or phone."*

Worth stating because the instinct is to assume you did something wrong and go
looking for the mistake. Nothing was wrong with the request. The fix is to
re-stage and submit again, and — if it fails twice — use the phone or postal route
rather than continuing to feed a broken endpoint.

**Record it as unfinished, not submitted.** A form that errored is exactly as
unfiled as one never started, and the CAPTCHA you just solved is spent.

## 7. The request was filed against the wrong identity

Brokers index on prior addresses and disconnected phone numbers as much as current
ones. A request naming only your current details can be honestly processed and
still leave several records untouched — the broker will tell you they found
nothing, and be telling the truth.

**Check:** list every email, prior address, and old phone number on every request.

**The sharper version: some brokers index on *nothing* you sent.** Several
categories are searchable only by a key the standard letter never contains —
social handles, phone numbers, VIN or plate, device or advertising IDs. There the
letter is not merely incomplete, it is unanswerable, and a truthful "no records
found" is the expected reply. Read what the broker says it indexes on, and send
that. See `_CATEGORY_VARIANTS.md`.

**The mirror failure: the identifier you cannot produce.** Some forms require a
key the consumer does not have — a device ID for a TV-advertising deletion, a
profile URL that the public search never exposes. Check whether a *different*
request type on the same form has a lower bar: one broker gated Access and Delete
behind a device ID while offering a full household opt-out on address alone.
Picking the achievable request beats abandoning the form, as long as you record
which right remains unexercised and why.

---

## 8. The answer was phrased more broadly than the question

A people-search site with an address-keyed index required city **and** state to
run a removal search. The search for one former city came back:

> *"We were unable to find any search results for &lt;name&gt;."*

That sentence names a person and nothing else. The query named a person **and a
city**, and the answer is only true of that city. Read at face value it says the
index holds nothing about you; what it actually says is that the index holds
nothing about you *there*.

This is worth its own entry because it does not feel like a failure mode. There
is no error, no bounce, no unanswered mail — just a clean negative result that
invites a conclusion one size too large. Somebody with eight former addresses who
searches one of them and stops has recorded `not_found` against seven addresses
they never checked.

The same shape turns up in confirmation emails: *"your information has been
removed"* when what was removed was one profile among several, and *"we do not
sell your personal information"* answering a request that also asked for
deletion.

**Check:** write down the query, not just the answer. If the answer is not
scoped as narrowly as the question was, it has been generalised for you — and
generalising back down is your job, not theirs.

**The fix is usually not more searching.** Where a search is gated per query — a
CAPTCHA from the second search onward is a common arrangement — running it once
per address is exactly the expensive path the gating is designed to create. Put
the whole list of localities in one email to the operator instead and ask for
suppression at the record level. One message covers what eight searches would.

## 9. The validation error that does not say anything

A privacy-request form rejected a telephone number formatted with dashes. What
happened on submit: the field acquired a **red outline**. No message, no text
under the field, no scroll to the error, no change to the button. The page simply
did not advance.

The field was optional. So the shape of the failure was: an optional field,
filled in helpfully, silently blocked a request that would have gone through if
it had been left empty.

Two things follow.

**For a person:** a form that does not advance and does not say why reads as
broken, and the reasonable response is to give up and assume the company's site
is at fault. The removal does not happen. Nobody records a failure, because from
the outside nothing failed.

**For automation:** this is why a submit must be followed by a screenshot and an
inspection, never by an assumption. A click that returns success at the tool
level tells you the click landed, not that the form accepted it. Look for the
confirmation you expected — and if you do not see it, look for what turned red.

**Check:** after any submit, confirm the page actually changed. If it did not,
re-read the form fields before re-reading your input. Try the most
machine-friendly format for anything with a format (`+1XXXXXXXXXX` for phone,
ISO dates), and when a field is optional and awkward, leave it out.

## 10. The guard that could not see the file it was guarding

Not a broker's failure — ours, and worth recording because the shape recurs.

This repository is public, so a scanner checks every file for values from the
profile before anything is committed. It ran. It reported **zero**. In the same
commit, a real telephone number went public inside a new playbook.

The scanner listed files with `git ls-files`, which lists *tracked* files. A
brand-new file is not tracked until the commit that adds it. So the check was
structurally blind to exactly one category of file: **the ones being published
for the first time** — which is where new prose lives, and where personal data is
most likely to have been typed in by hand.

The fix is one flag: also list `git ls-files -o --exclude-standard`, which is
untracked-but-not-ignored, i.e. precisely "what would be published if you
committed everything". Gitignored paths stay out of scope; those are where
personal data is supposed to live.

**The general lesson is about how a guard reports success.** A check that says
"0 problems" when it examined nothing is worse than no check, because it
manufactures the confidence that stops you looking. When writing one, ask what it
does when the input set is empty — and prove it can fail by feeding it something
that should trip it. A guard you have never seen go red is a guard you have not
tested.

## 11. The published privacy address belongs to a mailbox nobody reads

One people-search site publishes another company's support address as its privacy
contact. Write there and you get:

> *"This is an automated message from Whitepages support. If you are trying to
> contact us, please submit a ticket using this form..."*

Follow the chain: a consumer reads the site's own privacy policy, sends a deletion
request to the address it names, and receives a prompt, polite, branded reply. It
is not an acknowledgement — it is a redirect — but it arrives within seconds and
looks like the system working. Nothing is filed. Nobody is told.

This is worse than a bounce in every respect. A bounce is loud, immediate and
unambiguous; this is quiet, plausible and reassuring.

**Two checks follow.**

First: **an auto-reply is not a receipt.** Read what it actually says before
recording anything as submitted (see §5). "We have received your message" and
"please use this form instead" are different sentences with very different
consequences, and both arrive in the same second.

Second — and this is the one that scales — **consolidating onto a shared contact
multiplies the failure.** `scripts/family_scan.py` groups brokers by contact
address precisely to send one letter instead of a dozen. If that address is a
dead channel, one bad contact silently voids a dozen requests, every one of which
reads as `submitted`. The scan now flags any group whose shared address nothing
has confirmed, because the leverage that makes consolidation worth doing is
exactly what makes an unverified shared address dangerous.

**The right move when you find one:** do not keep writing to it. Find the route
that opened a real ticket for the parent brand and raise the sibling *there* —
an existing ticket already carries the identity verification, and a reply to it
cannot be silently dropped in the way a fresh message to a dead mailbox can.

## 12. The form made you choose which right to exercise

A large compiler's privacy form has one dropdown labelled **Privacy Choice**, and
its options are not categories of data but *rights*:

    Request to opt out of sale/sharing
    Request to correct inaccuracies
    Request to delete
    Request to access
    Request to limit use/disclosure of sensitive personal information

It is a single-select. So one submission exercises **one right**, and nothing on
the page says that the others were not requested.

A consumer who wants their record deleted *and* wants it to stop being sold picks
"delete", submits, and receives an accurate confirmation that their request has
been processed. It has been. The sale continues.

This is a variant of the wrong-request-type trap (§1), but it is worse in one
respect: there is no misclick to notice afterwards. The form did exactly what was
asked. The gap is between what the consumer wanted and what the interface let them
say in one pass, and no artifact anywhere records the difference.

**Check:** wherever a form asks you to *choose* a right, assume every other right
was declined by omission. Submit once per right you actually want, and keep the
confirmations separately — two receipts reading "your request has been processed"
are not interchangeable, and only the pair shows both were asked for.

The same shape appears as separate form URLs rather than a dropdown: one broker's
autoresponder supplies three distinct OneTrust links for opt-out, deletion and
access, and "the privacy form" is whichever one you happened to open.

## 13. Checkbox or dropdown: the same rights, one interface choice apart

Two brokers, the same five or six statutory rights, and a difference that decides
whether a consumer gets what they asked for.

One presents them as a **single-select dropdown**. Pick "Request to delete",
submit, receive an accurate confirmation. The opt-out was never requested, and
nothing anywhere records that.

The other presents them as **checkboxes**. Tick all of them, submit once, done.

Neither interface is described anywhere as a policy choice. Neither company is
doing anything a regulator would obviously object to. But one of them turns a
complete request into a partial one by default, silently, at zero cost to itself,
and the other does not.

**Check, on any rights form:** count the request types, and count how many you can
select. If it is one, submit once per right and keep the confirmations separately.
If it is a checkbox list, read to the bottom of it — the useful ones are often
below the fold, and "withdrawal of consent previously provided" in particular is
worth ticking even where you gave none, since some brokers assert consent through
the privacy policy itself.

## 14. Our own checker called a live company dead

The address-verification sweep fetches each broker's privacy and contact pages. If
nothing answered, it recorded **UNREACHABLE** and marked the address unverified —
which reads, to anyone using the registry later, as "this company is gone, stop."

Seven brokers were written off that way and were not gone. Their sites sit behind
a CDN that refuses scripted requests: the connection is reset before any HTTP
status exists, which looks identical to nothing being there. DNS resolved. MX
records resolved. Mail would have been delivered.

The distinction the check was missing is small and decisive:

| Observation | Meaning |
|---|---|
| DNS does not resolve | Nobody is there. This is the only case that means "stop". |
| DNS resolves, connection refused | A CDN is refusing **us**. Says nothing about the address. |
| Connection accepted, 403 | The server is refusing us politely. Same conclusion. |

Now only a DNS failure yields UNREACHABLE; a resolving domain that will not talk
to us is BLOCKED, and BLOCKED deliberately leaves the existing verification flag
alone, because being unable to read a website is not evidence about a mailbox.

**The general lesson is about which way a check fails.** This one failed toward a
confident negative — it did not say "I could not tell", it said "unreachable", and
that word closed the question. A checker that cannot distinguish *absence* from
*being refused* should report uncertainty, not absence. Where it cannot, the
verdict it emits must be the one that costs least when wrong.

## 15. The route is a photograph of a route

A background-check site's privacy policy, dated **effective March 1, 2025**, has
essentially every actionable link rewritten to point at **web.archive.org
snapshots from October 2024** — the opt-out page, the help page, terms, and the
`mailto:` for its own privacy address.

Click "opt out" and you land on the Internet Archive's photograph of a form. It
renders. It has fields. It cannot submit anything. Click the privacy contact and
the Archive opens instead of a mail client. Meanwhile the live opt-out URL
redirects back to the privacy policy, so arriving from any other direction is a
loop. The address on the home page hard-bounces.

The site therefore publishes **no working removal route at all**, while presenting
a policy that is current-dated, professionally worded and comprehensive.

The likeliest cause is a lazy restore — the page rebuilt from an archived copy of
their own site with the Archive's link rewriting left in — not a designed
obstacle. **The cause does not matter to the outcome.** Anybody who has tried to
opt out since March has failed, and almost none of them will know: the form looked
right, it accepted their typing, and nothing said otherwise.

**Check:** before recording a route as available, confirm the links go somewhere
**live**. An `archive.org` URL inside a privacy policy is a dead route, not a
quirk. And a page that looks maintained — recent date, careful prose — is evidence
about the writing, not about the plumbing.

**Read the policy's text for an address rather than following its links** — that
much is right, and it is how the second address was found here. In this case it
bounced too, with the same 550: both published addresses are dead and the site has
no route in of any kind.

**A postscript on how I got that wrong.** Seeing live Google MX records for the
domain, I concluded mail was being delivered and wrote that down. It was not. An
MX record means the domain accepts mail *routing*; whether a given mailbox exists
is decided by the receiving server afterwards, which is exactly what a 550 is. §14
above is about not treating a refusal as an absence; this is the same error
inverted — treating infrastructure as evidence of a mailbox. Neither DNS nor MX
tells you an address works. **Only a delivered message does.**

## 16. Deleting the record can un-suppress the phone number

A perverse case, and one that produces the exact opposite of what was asked for.

If a telephone number sits on a marketing company's internal do-not-call or
do-not-text list, that entry is frequently **a property of the consumer record**
rather than a standalone row. Delete the record and the suppression goes with it.
The number becomes eligible for calling again — *because* the consumer asked for
their data to be deleted.

Nothing in the confirmation reveals this. The deletion was performed exactly as
requested, the reply is accurate, and the first sign anything is wrong is a call
some weeks later.

**Ask for both, as separate operations:** delete the record, **and** add the
telephone numbers to the do-not-call and do-not-text suppression lists as
standalone entries that survive the deletion. Then ask the confirmation to state
both separately — one sentence covering "your request has been completed" is not
enough, because these are different operations on different tables and only one of
them is the one you would notice missing.

The same shape applies to email addresses and unsubscribe lists, where the
consequences are milder but identical in kind: an unsubscribe flag attached to a
deleted record is a deleted unsubscribe flag.

**The general form:** where a suppression is stored *as an attribute of* the thing
being deleted, deletion destroys the protection. Any time you ask for both
deletion and suppression, ask which table each lives in.

## The pass that catches these

1. **Bounces before anything else.** A bounce invalidates a request you have
   already recorded as sent.
2. **Unclicked verification links.** Search for pending "confirm your email" mail;
   these expire.
3. **Request IDs against intent.** Where a broker names the request type back to
   you, read it rather than assuming.
4. **Re-check listings after the stated window.** See `verify_removals.py`. A
   submission is not a removal, and records reappear.

---

## Not every privacy email is a broker reply

Removal **services** — the paid subscriptions that offer to opt you out of
hundreds of sites — send mail that looks superficially like broker
correspondence: "N data broker sites expose your information right now",
scan results, progress reports.

They are not data brokers and do not belong in the registry or the tracker. Two
reasons to keep them out deliberately:

- **They inflate the numbers.** A scan result claiming a hundred exposures is
  marketing, not evidence, and mixing it into a tracker built on broker-issued
  artifacts corrupts the one thing that tracker is for.
- **An account may exist as a side effect.** Some broker opt-out flows funnel
  through a removal service and create an account in your name along the way. That
  account is worth dealing with — but as an account to close, not a broker to file
  against.

During an inbox pass, skip their mail the same way you skip newsletters. If a
removal service needs attention, it is a separate task with a separate goal.

---

## The "verified" flag that verified nothing

Worth recording because it happened here, in this project's own data, and it is
the same shape as everything else in this file.

The registry has an `email_verified` field, and `validate.py` warns when a
guessable address (`privacy@`, `support@`, `info@`) is used **without** it. Sound
design. But the bulk import set `email_verified: true` on every scraped entry —
**504 of 536 addresses claimed a verification nobody had performed.** The check
keyed off the flag, so it passed on all of them and reported zero warnings.

The cost showed up in a single afternoon: **four of thirteen** such addresses
hard-bounced with 550, and in three of those cases the site published no
alternative address at all. Each bounce is a request that never existed while
looking, in the tracker, exactly like one awaiting a reply.

**The general rule: a boolean that defaults to the reassuring value is worse than
no boolean.** It converts "unknown" into "fine" everywhere at once, and it does so
silently, which is precisely when nobody looks again.

**The fix, and what makes it stick:**

- `email_verified` now means *there is positive evidence this address accepts
  mail* — a reply, an acknowledgement, a ticket reference — derived from the
  tracker rather than asserted at import.
- A companion field, `email_verified_by`, records *how*: `delivery_evidence`,
  `privacy_policy`, `state_registry`, `broker_reply`, or `bounced`. `validate.py`
  now warns when `email_verified` is true with no `email_verified_by`, so the flag
  cannot be set again without saying on what basis.
- Rerunning that gave 166 verified on evidence and 368 honestly unverified, and
  turned 0 warnings into 281.

**When you inherit a dataset, check what its confidence fields were populated
from before trusting them.** A field named `verified` invites you to skip exactly
the check it was meant to prompt.

---

## Ranking that inverted its own purpose

The address-verification sweep proposed replacing these:

| Held | Proposed |
|---|---|
| `dataremoval@` | `info@` |
| `removalrequests@` | `info@` |
| `consumerchoice@` | `info@` |
| `americas.dpo@` (a Data Protection Officer) | `hello.marketing@` |

Every one is backwards. The last would have sent a deletion request to a
marketing team.

The cause was a one-line assumption. Local-parts were ranked by matching against
a preference list **anchored to the start of the string**, and the list contained
none of the purpose-built removal terms. So `dataremoval`, `removalrequests`,
`consumerchoice`, `delete_mydata` and `americas.dpo` all fell through to
"unrecognised" — which scored *worse* than a bare `info@` that did match. The
tool then confidently recommended the downgrade.

**What makes this the same failure as the rest of this file:** the output looked
authoritative. A verdict called `REPLACE`, with an arrow and a plausible address,
reads as a considered judgement rather than a fallthrough. Nothing said "I did not
recognise this."

**Three fixes, all worth copying:**

1. **Rank by intent, matched anywhere in the string.** `americas.dpo` is plainly a
   DPO address; `privacyanddatacompliancereview` is plainly a privacy one.
   Prefix-anchored matching cannot see either.
2. **Put purpose-built removal addresses at the top.** A broker publishing
   `dataremoval@` or `consumerchoice@` has built a channel for exactly this
   request. That beats a general mailbox even though both certainly exist.
3. **Never trade down.** A swap is only an improvement if the new address ranks at
   least as well. Where the published address is *worse* than the one held, keep
   the good one and record the published one as `email_alt` — a fallback, not a
   replacement. A deletion request to `sales@` is worse than one to an unpublished
   `privacy@` that might bounce, because **a bounce at least tells you it failed.**

Fifteen records now carry a fallback address instead of having lost one.

