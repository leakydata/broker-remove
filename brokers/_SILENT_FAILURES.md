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

### One broker publishes this in its own opt-out form

Not an inference — a B2B prospecting company states it on the form itself:

> *"Please note that if you would like to request deleting all information we may
> have connected to your email, we may not be able to keep a record of your opt-out
> preference and **add information to the database again**."*

And describes the alternative correctly:

> *"we will remove the profile and business information linked to this email from
> our database, **keeping the email address for purposes of respecting your
> opt-out preference in the future**"*

So there, **asking for deletion makes you re-addable and opting out does not.**
The usual advice inverts, and it is only safe to invert because they said so.

**Do not generalise it.** At a broker with no persistent suppression list, deletion
remains the stronger request; the point is that the right choice depends on how
suppression is stored, which is invisible from outside unless the broker says.
So: **read what the route tells you before choosing which right to exercise.** The
information is occasionally right there, and where it is, it changes the answer.

## 17. The negative that answers a narrower question than you asked

A market-research company replied within half an hour:

> *"upon checking no records or data found connected to this account."*

A written negative, promptly given, and it looks like a clean close. Read the last
two words again.

**"This account"** is not what was asked. The letter did not ask whether the
subject had an account — at a panel business you would expect not — and an account
lookup returning nothing is entirely consistent with data existing. Panel and
survey records are commonly held against a **panellist ID** with identifying
details in a separate table, and firms of this kind also hold third-party-acquired
data about people who never registered for anything.

So the reply may be completely true and completely uninformative. Nobody is being
evasive; somebody typed a name into the system they administer and reported what it
said.

**Check the noun.** A negative is only as broad as the thing it was searched
against, and the reply usually names it: *this account*, *our customer database*,
*your profile*, *the name and email provided*. Each of those is narrower than "any
record about this person", and the gap is where the record sits.

**How to press without being unreasonable.** Ask the narrower question back, and
offer a form of words that would close it:

> *"If the answer is still none, please say so in those terms — 'we hold no record
> corresponding to this person, under any identifier' — and I will treat the matter
> as closed and not write again."*

That is easy to grant if true, and it converts an account lookup into a real
answer. It also makes the second request obviously reasonable rather than
persistent for its own sake.

**Do not record `not_found` on a scoped negative.** `not_found` should mean the
operator says they hold nothing; a reply that says they found nothing *in one
place* is a partial answer, and filing it as an outcome retires a broker that was
never actually searched.

## 18. The mailbox was full

A third bounce class, and the only one that is **temporary**:

> *"Delivery has failed to these recipients or groups: css-support@... The
> recipient's mailbox is full and can't accept messages now. Please try resending
> your message later."*

Not a dead address and not a dead domain. The mailbox exists, the domain is
healthy, the company is trading — the message was refused for want of space.

Three bounce classes now, and they call for three different actions:

| What the DSN says | What it means | What to do |
|---|---|---|
| `550 address not found` | Domain lives, mailbox does not | Find another address |
| `domain couldn't be found` | No DNS at all | Record `unreachable`, stop |
| **`mailbox is full`** | **Address is real, temporarily refusing** | **Retry later — do not re-route** |

**Why it deserves naming.** The instinct on any bounce is to go looking for a
different address, and here that is the wrong move: the published address is
correct and will start working again. Re-routing to some other mailbox found on
the site sends the request somewhere worse.

**And it is the easiest of the three to lose.** A full mailbox is a transient
state, so the retry has to be *diarised* — nothing will remind you, and a request
recorded as `failed` and never revisited is indistinguishable from one that was
refused. Record it as failed with the reason, and set a date.

One more thing this DSN gave away: the address written to was `privacypolicy@`,
and the bounce came back naming `css-support@`. The published privacy address is
an alias forwarding into a customer-support queue — so privacy requests land in
the same tray as billing questions, which is worth knowing even after the mailbox
empties.

## 19. The same reply, twice — you are talking to a template

A site's support desk answered a detailed request with a canned message. The reply
was answered point by point: it had asked for a page URL, so the follow-up
explained that the URL patterns 404, supplied eleven addresses to search instead,
and pointed out that their own form's title showed they had searched by *name*
while the pages are keyed to an *address*.

The response was the **same message again**. Word for word. Same greeting, same
request for a URL, same closing.

**Two identical replies mean nobody read either one.** Not indifference —
mechanism. Somewhere between the mailbox and the person there is a template that
fires on inbound, and the thread will produce that template indefinitely. A third
message will get a fourth copy.

**Check:** before writing a considered reply, compare it with the last one you
received. If they are byte-identical, the channel is a loop and the effort is
wasted. Diff them; do not skim them — canned replies are designed to read as
personal, and the tell is exactness rather than tone.

**What to do instead:**

1. **Switch channel.** A form, a phone number, a postal address, a regulator
   complaint — anything that is not the mailbox that is looping.
2. **Use whatever the template gave you.** The canned reply is usually not
   worthless: this one contained a working self-service form URL that the first
   message would never have produced.
3. **Record it as `manual_required`, not `submitted`.** A request sitting in a
   template loop has not been received by anyone, and filing it as in-flight means
   it is never revisited.

**And keep both copies.** Two identical replies to substantively different
messages is good evidence that a company's stated privacy channel does not
function, which is precisely what a regulator complaint needs.

## 20. The state dropdown that omits your state — and picks another one for you

An education-data company's privacy request form has a required **State of
Residence** dropdown. Its options are only the states with comprehensive consumer
privacy statutes: the list runs Oregon straight to Rhode Island. A Pennsylvania
resident has nothing to select, so the form cannot be submitted at all.

That much is the residency gate in its most concrete form — not a policy argued in
a reply, but a control that will not accept you (`_DEFLECTIONS.md` §3, §23).

**The second half is worse.** The field is a type-ahead. Typing "Pennsylvania" did
not reject the entry and did not say the state was unavailable. It silently
resolved to **"Colorado"** and left that sitting in the box.

Follow what that does to somebody filling the form at normal speed: they type their
state, the box accepts *something*, they move on, they submit. The form now records
a Pennsylvania resident as a Colorado resident — on a privacy request, under a
notice saying the information is used to verify identity, where state of residence
decides which statute is applied. Nobody intended it and nobody would notice.

**Check, on any form with a state or country selector:**

- **Read the option list before typing.** If your state is missing, that *is* the
  answer, and no amount of filling in the rest will change it.
- **Re-read the field after typing.** A type-ahead that substitutes rather than
  refuses is not rare, and the substitution looks exactly like a successful entry.
- **Never submit a state you do not live in**, even where the form leaves you no
  other option. These forms frequently carry a certification, and a false statement
  of residence turns a lawful request into a defective one — and hands the company
  a reason to void it later.

**What to do instead:** report both faults in writing, and ask them to process the
request as a matter of company policy while stating the basis they applied. A
non-discrimination notice on the same form is worth quoting back: declining a
deletion request solely because of where somebody lives sits oddly beside it.

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

## 21. The only contact is an unsubscribe alias

A broker with no privacy page and no opt-out URL sometimes carries exactly one
published address, and it is an **unsubscribe** alias -- often on a mail-sending
domain that is not theirs, with a per-brand tag in the local part.

Three failures hide in that one address, and they look identical from outside:

- The alias may not exist. `unusubscribcfmf@seememail.net` -- note the misspelling
  -- is either the broker's own typo, faithfully copied, or a transcription error
  introduced upstream. One of those bounces and one does not.
- It probably reaches a **service provider**, not the company holding the record,
  so even a delivered message may never meet anyone who can delete anything.
- Unsubscribing and deleting are **different systems**. An unsubscribe suppresses
  mailings, frequently by *keeping* your address on a suppression list. A cheerful
  "you have been unsubscribed" therefore reads as success while the record stands.

**The fix is one paragraph in the letter**, naming the ambiguity and refusing the
narrow reading: say that if this is an unsubscribe alias rather than a privacy
mailbox, it should be forwarded or redirected, and that it is not to be treated as
a mailing preference. Silence afterwards still means nothing -- but a reply now has
to pick one of the three, and every one of those is a usable answer.

## 22. The click that lands somewhere else

Filling a form by clicking a coordinate and typing assumes the page is still where
the screenshot said it was. On several privacy forms it is not: focusing a field
scrolls it into view, a sticky header collapses, a cookie banner appears and
reflows the body. Every one of those moves the *next* field by tens of pixels
between the screenshot and the click.

The failure is silent in the worst way, because the typing still succeeds -- into
whatever is now under the cursor. One staged form ended up with the first name in
the **email** field and five other fields empty. Had it been submitted, it would
have been a well-formed request for a person who does not exist, and the response
would have been a truthful "no records found".

Three habits that fix it:

- **Prefer `form_input` with an element reference over click-then-type.** It
  addresses the field by identity rather than by position, so scrolling cannot
  misdirect it. It is also immune to the cookie banner that appears mid-batch.
- **Never batch more than one click-and-type on a page that scrolls on focus.**
  Coordinates inside a batch all refer to the screenshot taken *before* the batch.
  The first action can invalidate every coordinate after it.
- **Screenshot before submitting, and read the values, not the layout.** A form
  that looks filled is not the same as a form that is filled correctly.

The same reasoning applies to checkboxes. Three request-type boxes reported
"clicked" and were still unchecked, because the page had shifted under each one.

## 23. The form collects eight identifiers and the answer names one

A removal form asks for name, email, phone, address line 1, address line 2, city,
state and zip. It then answers:

> *"We have no record of <email address> in our service."*

Six of the eight fields do not appear in the answer. Two readings, and no way to
distinguish them from outside:

- the lookup really is keyed on email alone, and everything else was collected for
  a purpose other than the search; or
- the lookup used everything, and only the *message* is narrow.

Either way the negative covers less than it looks like it covers, and the more
identifiers a form collects, the more confident its negative sounds.

**The tell is arithmetic**: count the fields the form asked for, then count the ones
the answer mentions. When those numbers differ, the answer is scoped to the smaller
set until somebody says otherwise.

**It gets worse when the identifier is a poor key for that broker.** A directory of
government and corporate leadership, searched by a personal webmail address,
returns no match almost by construction -- the record, if it exists, is filed under
a work address and an employer. A negative is only as strong as the identifier it
was run against, so ask what this particular broker would file you under before
believing it.

## 24. Setting a type-ahead's value is not choosing from it

OneTrust privacy forms render the state field as a **type-ahead combobox**, not a
`<select>`. Writing a value into it programmatically -- the thing that works
perfectly on every ordinary text input -- puts the right text on screen and leaves
the widget's internal selection unset.

The failure is not a blank field, which would be caught. On submit the widget
**resolves to a different entry entirely**. Typing "Pennsylvania" into Arity's form
this way produced **"Arkansas"** after submission. An earlier form produced
"Colorado" from the same input. The substituted value is not adjacent
alphabetically, not a prefix match, and not predictable -- it is whatever the
component falls back to.

Read that again, because the consequence is worse than a failed submission: it
files a **false residency claim**, on a form whose whole purpose is to establish
which state's privacy law applies, under a declaration you are signing. And the
screenshot taken a moment earlier shows the correct state, so it looks verified.

**The rule: for a type-ahead, click the option out of the dropdown.** Type one or
two characters to filter, screenshot, click the row, then screenshot again and read
the field. Never `form_input` it, and never trust the value you see before submit.

Note the diagnosis matters as much as the fix. The first time this happened it
looked like "Pennsylvania is not in their list", which would have been a finding
about the broker -- PA has no comprehensive privacy law, so it is entirely plausible
a form would omit it. It was not that. Typing a single "P" showed Pennsylvania
present alongside Mississippi and New Hampshire. **A tool failure had been about to
be recorded as a fact about the world.**

## 25. The route they name has nothing on it

A broker refuses email and names a URL instead. The URL loads, looks official, and
carries a heading like "Data Rights and Privacy" -- and contains no form, no request
types and no submit control. In one case the footer link literally labelled
**"Opt-Out Form"** pointed at that same empty page.

This is the most complete dead end in the collection, because both halves look like
progress. The refusal is polite and specific. The page exists and is on-topic. Only
by reading the page for **interactive elements** rather than for text does it become
clear there is nothing to do there.

**Check what a page can do, not what it says.** An accessibility-tree read that
returns only an Exit button and an outbound marketing link is the finding.

**The usual cause is jurisdiction configuration, not breakage.** Consent-platform
privacy centres commonly render rights options only for visitors whose state matches
a configured regulation and fall back to informational prose otherwise. So the page
works perfectly when the company tests it, and shows nothing to a consumer in a
state with no comprehensive statute -- while the refusal email sends everyone there
regardless.

That distinction changes how to report it. "Your form is broken" gets answered with
a screenshot proving it is not. "Your page renders no form for a visitor outside a
covered jurisdiction, and your email directs those visitors there anyway" cannot be.

## 26. The confirmation that is a reply, not a click

Nearly every broker confirms an opt-out by **clicking a link**. At least one requires
you to **reply** to the acknowledgement email instead, and says so plainly:

> *"Respond to the acknowledgement email to authorize removal of your listing. If
> you do not respond to the email, your listing will NOT be removed."*

A reply is much easier to leave undone than a click. A link is one action in the
mailbox you are already looking at; a reply means composing a message. Worse,
anyone habituated to the click pattern will open the acknowledgement, scan for a
link, find none, and close it -- having done the exact thing that leaves the request
void.

**Read the acknowledgement for the verb.** "Click", "confirm", "respond" and "reply"
are not interchangeable, and the one broker in twenty who wants a reply will not
send a link for you to find.

## 27. The error message that blames the wrong thing

A stage-two opt-out link, opened nine minutes after it was issued, returned:

> *"Opt-Out Request Expired — The data in the request seems to have some errors,
> visit the Opt Out Form to start the process again."*

It had not expired. The link carries two query parameters -- a base64 `key` and a
separate `ticketid` -- and only the `key` had been used. Adding the `ticketid` back
loaded the form immediately.

**Two ways this wastes a request.** The message names the wrong cause, so the
obvious response is to go back to step one and burn another round trip. And it says
"expired", which is plausible on a flow that genuinely does expire in 24 hours --
the true explanation is available and wrong.

**The cause was upstream, in the email.** The plaintext rendering of the message had
mangled the separator: `&amp;ticketid` with the `=` replaced by a replacement
character. Anyone reading the plaintext part, or any tool extracting the URL from
it, silently loses the second parameter.

**Take the link from the HTML part, not the plaintext part.** And when a
freshly-issued link claims to be expired, check the URL against the one in the email
character by character before accepting the diagnosis -- the site is guessing at why
its own validation failed, and it guessed the most reassuring reason.

## 28. Automation attachment can make a bot check unpassable

One broker's opt-out page entered an endless loop -- Cloudflare challenge, page,
challenge, page -- that only occurred while a browser-automation tool was attached
to the tab. The challenge cannot be satisfied because the thing being detected is
the debugger connection, not the visitor.

This is worth separating from the ordinary bot gate. A normal challenge is a
hand-off: stage the form, a person clears it, work continues. This one **cannot be
handed off in the same tab**, because the loop resumes the moment the page reloads
under automation. Detaching -- closing the tab entirely -- is what stops it.

**When a challenge loops rather than blocks, suspect the tool before the site.**
Then look for the route that does not involve the browser at all. In this case the
broker's own support email had already offered one: *"If you are unable to remove
your listing from [the opt-out URL] please call us... and we will be happy to assist
you in locating and removing your listing."* The fallback was in hand before the
loop started.

## 29. The dead link that is dead in every copy of the message

A broker's reply carried two links to its rights portal. Both were unusable: the
`?sysparm_id=` separator had been replaced by a stray character and at least one
further character eaten with it, leaving a 30-character identifier where the platform
uses 32.

The important detail is that the corruption was present in **both the plain-text and
the HTML parts** of the message. That rules out the usual explanation -- see §27,
where taking the link from the HTML part fixed it -- and points upstream, to the
sender's own template or mail pipeline.

**Which makes it a fault worth reporting rather than a puzzle worth solving.** If the
corruption is in their outbound mail, every consumer who receives that reply gets a
dead link, and not one of them will be able to explain why. They will click, get
nothing, and give up. From the company's side that looks like a queue of people who
did not follow through, which is exactly the wrong lesson.

**Do not try to reconstruct the identifier.** Guessing a 32-character sys_id from a
30-character fragment is not going to work, and a wrong guess either 404s or -- worse
-- lands on somebody else's request.

**Do load the bare form URL**, because what it does is diagnostic. Here it reached the
portal, rendered the broker's branding, and then displayed an **empty red error banner
with no text**: enough to prove the endpoint is live and the parameter is the only
thing missing, which is what makes the report specific rather than "your link does not
work".

## 30. Our own checker asked the wrong question, again

`verify_emails.py` decided whether a broker was reachable by looking for an **A
record** on the apex or `www`. It found none for one domain and reported
**UNREACHABLE** -- the verdict that writes a broker off.

The domain published a **Microsoft 365 MX record** and was registered until 2027. Its
mail worked. What had actually happened was that the `www` CNAME pointed at a CDN
distribution that no longer resolved, and the apex had never carried a web host at
all.

**The script verifies email addresses. For that purpose an MX record is the relevant
signal and an A record is a proxy at best.** Asking "does it have a website?" to
decide "can I email them?" conflates two things that come apart routinely: a company
with no website on the domain it receives mail on is ordinary, not suspicious.

This is the **second** time this check has been wrong in the same direction. The first
was CDN-fronted hosts refusing the connection, fixed by separating BLOCKED from
UNREACHABLE. That fix covered *"the host did not answer"* and left uncovered *"there
is no host to answer"* -- a narrower repair than it looked.

The check now consults MX before condemning anything, and when the mail record cannot
be determined it returns **unknown rather than no**, resolving to BLOCKED. That
asymmetry is deliberate: a broker wrongly marked reachable costs one bounced email,
which is visible and recoverable. A broker wrongly marked unreachable is never
contacted again, and nothing ever surfaces the mistake.

**A correction to this entry, made ninety minutes after writing it.** The fix above
consults MX before condemning a domain, and that is right — but MX is **necessary, not
sufficient**. `matchandappend.com` publishes a healthy Zoho MX and rejects both
`privacy@` and `info@` with a hard 550: the exchanger answers and refuses every
recipient, because the records are configured and no mailboxes are provisioned.

So the corrected rule is the one this project already learned once, from a different
direction: **neither DNS nor MX tells you an address works. Only a delivered message
does, and only a bounce naming the address tells you one does not.** MX is a reason not
to condemn a domain prematurely; it is not evidence anybody is there.

**Generalising: when a tool of ours condemns a broker, verify the condemnation by
hand before acting on it.** Every verdict that closes off future work deserves the
scepticism we apply to a broker's own negatives -- ours are not better evidence
merely because we wrote them.

## 31. Verifying a removal against your own browser cache

Two brokers volunteered the same warning on their confirmation page, and it is the
clearest statement anyone has given of how a removal check goes wrong:

> *"Please make sure you clear your browser cache before attempting to confirm
> removal, or your device may pull up an old, stored version of our website. Also
> make sure you initiate a new search. Please do not attempt to verify removal by
> clicking on a saved link."*

Three distinct traps in one paragraph:

- **A cached page** shows the listing after it is gone. Read as "the removal failed",
  or worse, as a REAPPEARED, which is the finding we treat as escalation-worthy.
- **A saved link** returns the old record URL directly, bypassing the search index
  that was actually updated.
- **A repeated search** may be served from the site's own result cache rather than
  re-run.

**So a verification is only worth something if it is a fresh search, from a clean
session, on the live site.** Anything else can report either direction wrongly.

**And the inverse trap is worse**, because nobody warns about it: a cached *empty*
result, or a search-engine result that has not yet re-crawled, reads as a successful
removal when the record is still there. Kids Live Safe flagged the search-engine lag
explicitly -- *"several days to several weeks"* -- which is why the rule is to verify
against the broker's own site and never against a search engine.

**Practical consequence for `verify_removals.py`:** the re-check interval exists to
let the removal happen, but it must also outlast the caches. Three days is what these
brokers quote for the removal itself; the seven-day re-check is the right order of
magnitude, and a listing still present at seven days is meaningful in a way that one
present at one day is not.

## 32. Your own identifier list is the thing most likely to be incomplete

Every letter in this project asserts a set of identifiers, and every negative it
receives is bounded by that set. A broker that searches diligently on what it was
given, and finds nothing, produces a `not_found` that is only as wide as the list.

**The list was materially short.** A single broker profile the subject happened to
find carried **six addresses, three telephone numbers and four email addresses** that
were not in it — including a street address last reported in 1999, an out-of-state
address, and three email addresses on providers that no longer exist as consumer
services. Nobody had withheld them; they had simply been forgotten, which is the
ordinary case. Broker files reach further back than personal recall does, and that is
precisely what they are for.

**So a broker's own listing is a SOURCE, not only a target.** The profile tells you
what *other* brokers will have keyed you under — and those are the keys most likely to
survive a removal, because they are the ones nobody thinks to name.

Two consequences worth acting on:

- **Every negative already received is provisional.** It was answered against the
  short list. That does not make it wrong, but it means "no record found" should be
  re-tested against the enlarged set rather than treated as closed.
- **Feed found profiles back into the identifier set before the next batch.** The cost
  is a few minutes; the benefit applies to every letter sent afterwards, and it
  compounds — each new profile can surface identifiers that unlock the next.

There is a real tension here, and it should be named: sending more identifiers to more
companies is itself a disclosure. The justification is that these are identifiers the
industry demonstrably already holds — they were read off a broker's own page — so
naming them buys a wider search without revealing anything the recipient could not
already buy.

## 33. The privacy address that is a closed mailing list

A request to a published `privacy@` address bounced with this, from the broker's own
domain administrators:

> *"the group you tried to contact (privacy) may not exist, or you may not have
> permission to post messages to the group... This group may not be open to posting."*

The address is not dead. It is a **Google Group configured to accept mail only from
inside the organisation** — published for consumers, and refusing the only people it
exists to serve.

**This is worse than a 550 in two ways.** The bounce is ambiguous by design: it offers
four possible causes, three of which blame the sender ("you might have spelled the group
name incorrectly", "you may need to join the group"). Someone acting in good faith reads
that as their own error and retypes it. And because the failure is a *permission* rather
than a *missing recipient*, it will not appear on any list of dead addresses — the group
resolves perfectly well.

**Report it explicitly, because the company almost certainly does not know.** A closed
group is a default, not a decision: somebody created an internal alias and never
switched on external posting. Saying so in one paragraph is more likely to fix it than
any amount of escalation.

## 34. The carve-out that hides inside an offer

A broker replied with two working opt-out routes and one refusal:

> *"At this time, we are unable to remove data from the unclaimed money feature."*

Followed by detailed, genuinely helpful instructions for removing from Property Search
and from the resident search.

**The shape is the risk.** Two thirds of the reply is cooperative, specific and
actionable, and the refusal is a single clause near the top. Work through the two flows,
receive two confirmations, and the natural conclusion is that the removal is done — while
the product that was refused carries on unchanged.

**So separate the offer from the scope every time.** Count the surfaces the company has,
count the ones the reply covers, and name the difference back to them.

And ask **which kind of "unable"** it is. "We cannot" spans a technical limitation — a
live external lookup with nowhere to store a suppression — and a policy position that
the data is public record. Those need different follow-ups: the first invites asking for
**display-level suppression** even where the source cannot change; the second is a
position to record and stop pressing. A single word covers both, and only the company
knows which it meant.

## 35. A null MX is a refusal, and a resolving domain hides it

`verify_emails.py` was taught in §30 to consult MX records, because a domain with
no A record can still publish a perfectly healthy mail exchanger. Today the same
check ran into the opposite shape and would have missed it.

The registry carried `contact@nprofile.com` for a broker whose site is
`npiprofile.com`. Two separate problems, one address:

**The domain was wrong by one character.** `nprofile` is `npiprofile` minus the
`i`. It is not a typo anybody notices in a list of six hundred contacts, and it
does not look like a guess — it looks like a real address at a plausible domain.
The right domain, `npiprofile.com`, publishes healthy Google MX records; the wrong
one resolves too. Nothing about either fact distinguishes them.

**The wrong domain publishes a null MX.** `dig +short MX nprofile.com` returns:

    0 .

A single dot as the exchange is RFC 7505: *this domain accepts no mail.* It is
not a misconfiguration and not an outage. It is an explicit, deliberate
declaration, and it is the strongest negative available short of a bounce — far
stronger than "no MX at all", which is merely an absence.

The trap is that every cheap check passes. The domain resolves. It has an MX
record — one row, returned by `dig`, non-empty. A checker that asks *"are there
any MX records?"* and treats a non-empty answer as healthy will call this address
fine, because the code is asking whether the list is empty rather than what is in
it.

> **A null MX is a positive statement of refusal that a truthiness test reads as
> a positive statement of health.** Check for the value `.`, not for a non-empty
> list.

And the third-order lesson, which is the one that keeps recurring: §30 concluded
that MX is necessary but not sufficient. This is the other half — MX can also be
*present and yet a refusal*. Neither DNS nor MX tells you an address works. Only
a delivered message does.

## 36. Two unrelated vendors froze identically, so it was neither of them

A OneTrust webform stopped responding to every read the moment a key was pressed.
Screenshots timed out, the accessibility tree never settled, `document_idle` never
arrived. The obvious reading was a heavy tenant running a long-poll or a
never-settling script, and the write-up was half-drafted: *the form is
unverifiable under automation, hand it off.*

Then the same thing happened, in the same tab, on a completely different vendor's
portal — a different company, a different framework, a different domain. A third
navigation to an ordinary page could not screenshot either. At that point the
common factor was not the sites.

**The tab was wedged.** Closing it and opening a fresh one fixed everything
immediately: the same OneTrust form filled, read back, and verified without a
single timeout.

Two things worth keeping:

- **When two unrelated vendors fail in exactly the same way, stop diagnosing the
  vendors.** Identical symptoms across independent systems are evidence about the
  thing they share, which is the harness. The instinct to explain each site's
  behaviour is what wastes the time.
- **The cost of being wrong here is asymmetric and quiet.** The half-written
  conclusion would have entered the playbook as a fact about the broker — *"their
  form cannot be automated"* — and would have sent every future pass straight to a
  human handoff for a form that works fine. Same shape as the TruePeopleSearch
  `/removal` error that cost three days: a transient local failure recorded as a
  permanent property of somebody else's site.

Closing the tab costs one call. Try it before writing anything down.

## 37. The portal that offers fewer rights than the letter asked for

A broker's auto-reply pointed at a OneTrust webform. The form worked, was
straightforward, and asked for a sensible amount of information. Under *"Select
the Rights You Want to Exercise"* it offered exactly one option:

> *Opt-Out: Do Not Sell/ Share Request*

There was no deletion option anywhere on it.

The letter had asked for deletion, opt-out, downstream direction and suppression.
The portal accepts one of those four. A requester who does the sensible thing —
follows the auto-reply, uses the official route, abandons the email thread as
superseded — has **downgraded their own request from *delete* to *do not sell*,
and has not been told that is what happened.** The confirmation they get back will
be perfectly genuine.

This is not the same as a broker refusing deletion. Nobody refused anything. The
request simply cannot be made through the channel they direct you to, and the
channel does not say so.

> **Read the rights menu before treating a portal as the better route.** A form
> is not a superset of a letter. Where it offers less, send both and say in the
> letter that the form is a supplement, not a replacement.

Related: §34, the carve-out that hides inside an offer. Same mechanism — the
narrowing is in the shape of what is offered rather than in anything anyone says.

## 38. The add-a-row modal, and how to know a row actually landed

A self-service opt-out took names, addresses, phone numbers and email addresses
as repeatable rows: click **+ ADD**, fill a small modal, click **Add**, and the
value appears in a table. Forty items went in this way. Several did not.

Nothing announced the failures. The click tool reported success on every Add. The
modal simply stayed open, and the next **+ ADD** click — landing on a modal that
was already open — did nothing, so the next value was typed *over* the one that
had not yet committed. Two items were lost this way before the pattern was
visible, and one more later.

**Two distinct causes, both silent:**

**A required field lost its default.** The Address modal's State selector was
pre-filled on first use and **blank on every subsequent use**. A blank required
field made Add do nothing at all — no error text, no red outline, no shake, no
console message. The modal just sat there looking ready. Set every required
field explicitly on every iteration; never rely on a default you saw once.

**Speed.** Batched click-fill-Add sequences with no pauses failed almost every
time. The modal needs a beat to close and to reopen. Roughly two seconds after
opening and three after Add made it reliable.

### The commit detector

This is the part worth carrying to every other add-a-row form:

> After clicking Add, re-open the modal and write the next value. If the tool
> reports the field's **previous content as empty**, the modal was freshly
> opened — which means the last Add committed. If it reports the **previous
> item's text**, the modal never closed: the last Add failed silently, and you
> are in the act of overwriting the lost value.

`form_input` returns `(previous: "...")` on every call, and that string is a free,
per-item receipt. It caught `225 Buckhout St` going missing in a batch of five
that otherwise looked perfect, and it distinguished the two names that committed
from the two that did not in an earlier batch of four.

Belt and braces: extract the page text every few rows and read the committed
table. It costs one call and it is the only ground truth. **Never submit a
multi-row form without reading back the rows.**

The general shape, which is §22 and §23 again in a new costume: *a tool reporting
that it clicked something is not evidence that the something happened.*

## 39. The address named for the thing it refuses

Two in one night, at unrelated companies:

- `ccpa@paramountdirectmarketing.com` — published for CCPA requests — bounced
  **Recipient Unknown**. It does not exist.
- `CCPARequests@pbinfo.com` — published for CCPA requests — auto-replies:
  *"Please note that this email address cannot accept consumer privacy rights
  requests."*

Both addresses are named after the exact function they cannot perform. Neither
failure is visible from the published page, and one of them is not visible from
the *bounce* either: an autoresponder returns a 250, so delivery succeeded, the
tracker records a sent letter, and the request is nonetheless nowhere.

> **An address's local part is a claim about what it does, not evidence.** The
> only proof is a substantive reply. `privacy@`, `ccpa@`, `dpo@` and
> `CCPARequests@` are the addresses most likely to be published without being
> wired to anything, precisely because they exist to be published.

This is the third distinct way a contact can be dead while looking healthy,
after §35 (null MX) and §30 (no MX at all). The taxonomy so far:

| Symptom | Detectable by | Verdict |
|---|---|---|
| No MX record | `dig MX` | Undeliverable |
| Null MX (`0 .`) | reading the MX *value* | Refused by policy |
| MX healthy, mailbox absent | hard bounce only | Recipient unknown |
| Delivers, autoresponder refuses | reading the auto-reply | **Accepted and discarded** |
| Delivers, template loop | reading the reply's *From* | Never reaches a human (§31) |

Only the last two look like success in a tracker.

## 40. Read the postmaster domain on every bounce

The Paramount bounce was more useful than the letter would have been. The
non-delivery report came from **`postmaster@paramountlists.com`** — a domain that
appears nowhere on `paramountdirectmarketing.com`, and which is the Office 365
tenant hosting their mail.

> **A non-delivery report names the sending infrastructure, and infrastructure is
> owned.** The tenant is on the envelope even when the website says nothing about
> who owns the brand.

This belongs in `_BROKER_FAMILIES.md`'s ranked signal list, roughly alongside "a
privacy address on another brand's domain" — it is the same evidence arriving
from the opposite direction, and it costs nothing because the bounce is already
in the inbox.

The habit to build: **when a letter bounces, read the whole report, not just the
status code.** The error tells you the request failed. The `From` and any
`Reporting-MTA` header tell you who they are.

## 41. The catch-all 200, and the opt-out sentence that stops

Probing a site for a removal page produced nine hits in a row:

    200  /optout.php        200  /opt-out.php      200  /optout
    200  /opt-out           200  /remove.php       200  /removal.php
    200  /do-not-sell.php   200  /contact.php      200  /ccpa.php

Every one of them was the homepage. The site serves a **catch-all 200** — any
path renders the index page rather than a 404. A probe loop that keys on status
code reports nine opt-out routes where there are none, and each one looks like a
find.

> **Compare titles or content, never status codes, when probing for a page you
> have not seen.** One extra field in the loop — `grep -oiE '<title>[^<]*'` —
> turns nine false positives into an obvious pattern.

### And the thing the probe was looking for does not exist either

The same site's privacy policy says, in full:

> *"phonenumberinfo.us also provides a quick and easy process to allow
> individuals to remove their information from our People Search results, whether
> or not they are a user of the Site. If you would like to opt out of our People
> Search results."*

The sentence ends there. No link, no address, no next step — the paragraph whose
entire job is to carry the removal route is a dangling conditional, the residue
of a template copied without the link pasted in.

Meanwhile the domain publishes **no MX record**, so the one address it does
publish — obfuscated behind Cloudflare's `data-cfemail` on two pages — cannot
receive mail either.

> **A promised process is not a process.** Directories of brokers routinely
> record "has an opt-out" from exactly this kind of sentence. The claim and the
> mechanism are separate things and only one of them can be tested. Test it.

### Decoding `data-cfemail` while you are there

Cloudflare's email obfuscation is a hex string XORed with its own first byte:

    b = bytes.fromhex(cfemail); key = b[0]
    addr = ''.join(chr(c ^ key) for c in b[1:])

Here it only confirmed a dead end, but scraping a page for `@` will never find an
address hidden this way — and on a site that *does* have working mail, this is the
difference between a contact and a `NO_EMAIL` verdict.

## 42. The apex and the www host are different records

Two agents checked the same broker minutes apart and reported different things.
One said the privacy page returned **503**; the other said the domain **failed to
resolve entirely**. Both were right.

    $ dig +short A matchandappend.com
    (nothing)

    $ dig +short A www.matchandappend.com
    34.106.169.43

The apex has no address record at all. The `www` host does. So a check against
`https://matchandappend.com/` gets a resolution failure, and a check against
`https://www.matchandappend.com/` reaches a server — which may then error, or
serve a page, or time out.

> **`example.com` and `www.example.com` are two independent DNS records.** Either
> can exist without the other. Checking one and reporting on "the domain" is a
> category error, and it produces exactly the disagreement above: two truthful
> observations that cannot both be about the same thing.

### Why this matters more than it sounds

The conclusion at stake was **"this broker has no website at all"** — which is
the kind of finding that ends an investigation. Recorded from an apex-only check,
it would have been wrong in a way nobody would revisit, because a documented dead
end does not get re-checked.

It is also the mirror of §35 and §30: a domain's DNS is not one fact. `A` on the
apex, `A` on `www`, `MX`, and the MX *value* are four separate questions, and a
broker can be alive on any subset of them.

### The check to run

    for h in example.com www.example.com; do
      echo "$h A: $(dig +short A $h | tr '\n' ' ')"
    done
    dig +short MX example.com

And when two sources disagree about whether something is reachable, **assume both
are honest and look for the asymmetry** — vantage point, host, protocol, or
timing — before deciding which one was wrong. Here neither was.

## 43. 5.7.1 is not 5.1.1, and the difference decides what to try next

Three addresses at one broker, all published on its own privacy policy, all
bounced:

    550 5.7.1 <info@rpmleader.com>: Recipient address rejected:
    User email address is marked as invalid.

Gmail's wrapper says "Address not found", which reads exactly like a missing
mailbox. It is not.

| Code | Means | What to do |
|---|---|---|
| `5.1.1` | **User unknown** — no such mailbox | Try another local part; `privacy@`, `legal@`, `dpo@` may exist |
| `5.7.1` | **Policy rejection** — the system knows the address and refuses it | Stop guessing local parts; the failure is not about which mailbox exists |
| `5.7.1` from a filtering gateway (Proofpoint, Mimecast, Barracuda) | Recipient not on the allowed-recipient list | The domain accepts mail only for addresses on a list the published ones are not on |

The practical difference is what you do next. On `5.1.1` it is worth trying two
or three other local parts. On `5.7.1` **every** address at that domain will fail
the same way, and probing is wasted effort — as it was here, where three
different published addresses produced three identical policy rejections.

> **Read the enhanced status code, not the mail client's summary.** "Address not
> found" is Gmail's paraphrase of at least two different failures that call for
> opposite responses.

The same message also carries the `Remote-MTA` line, which names the receiving
gateway — useful on its own (see §40 on reading the postmaster domain). Here it
was `mx1-us1.ppe-hosted.com`, i.e. Proofpoint Essentials, whose default posture
is exactly this: reject anything not on the customer's recipient list.

## 44. The "temporary" delay that is permanent

Gmail sent this about a letter to a broker:

> *"Delivery incomplete. There was a temporary problem delivering your message to
> privacy@example.com. Gmail will retry for 45 more hours."*

Everything about that is reassuring. It says *temporary*, it says *retry*, and it
implies the problem is at the far end and will pass. The tracker, meanwhile,
still says `submitted`.

One `dig` said otherwise:

    $ dig +short NS  keyopinionleaders.com     (nothing)
    $ dig +short SOA keyopinionleaders.com     (nothing)
    $ dig +short A   keyopinionleaders.com     (nothing)
    $ dig +short MX  keyopinionleaders.com     (nothing)

No nameservers, no SOA, no address, no mail exchanger — on the apex and on `www`
alike (§42). **The domain does not resolve at all.** The registration has lapsed
or been withdrawn, the retries cannot succeed, and the message will hard-bounce
in two days.

> **A soft bounce can mask a permanently dead domain.** Sending MTAs cannot
> distinguish "the far end is briefly down" from "there is no far end", so both
> produce a delay notice and a 48-hour retry window. For those two days a request
> that has nowhere to go looks exactly like one in flight.

### What to do

**Treat every delay notice as a prompt to check DNS, not as news that can wait.**
The check is one command and it is decisive:

    dig +short NS example.com

**No NS is the strongest possible negative.** It outranks everything in the
taxonomy at §39, because a domain without nameservers cannot have an MX, a null
MX, a mailbox, or an autoresponder — there is no zone at all. Compare:

| Symptom | Verdict |
|---|---|
| Delay notice, NS present, MX present | Genuinely transient — wait |
| Delay notice, **no NS / no SOA** | Domain gone. Downgrade now, do not wait |

**Downgrade the status immediately rather than waiting for the bounce.** Waiting
buys nothing: the outcome is already determined, and two days of a false
`submitted` is two days in which the entry looks handled and nobody re-checks it.

---

## §45 The registered contact the registrant has quietly retired

State data-broker registries exist so that a consumer can find a company they
have never heard of and write to it. The address in the entry is therefore the
only route that is both discoverable and authoritative.

A registered broker answered a letter to its registered address like this:

> "BDO has previously registered as a data broker under certain state laws using
> the email address privacy@bdo.com. **Please note that this email address is no
> longer used for that purpose.**"

The mailbox is not dead. It resolves, it accepts mail, a human reads it. Nothing
bounces. The route failed anyway — it just failed politely, and only for the
people who did not get forwarded.

> **A stale registered contact is invisible in a way a dead one is not.** A bounce
> is a signal you can act on. A courteous internal forward is a signal only if
> somebody chooses to send it, and you have no way of knowing whether they did.

**What to do.** Take the working address they gave you, use it, and *tell them the
registry entry is wrong* — separately from your request and without making it a
condition of anything. You are in a position to see the failure; the next consumer
using the same registry entry is not.

**What this means for the tracker.** A `submitted` against a registered address is
weaker evidence than it looks. It proves the letter was accepted, not that it
reached the function. Where a reply names a different address, record *both*, and
treat the new one as authoritative for follow-ups.

---

## §46 The reply that arrives from an address which cannot receive a reply

A broker answered a privacy request from `no-reply@<their domain>`. Replying
produced a hard "Address not found". No `Reply-To:` header, and no line in the
body saying where to write instead.

> **A `no-reply` From: on privacy correspondence is a one-way valve.** The
> consumer does the obvious thing — hits reply — and gets a bounce. From their
> side that is indistinguishable from a company that has refused to continue, and
> a fair number will stop there.

**The fix is free, and it is the habit that matters more than the instance.**

> **Reply to the address you wrote to, not to the `From:` of the answer.** The
> outbound template is broken; the inbound route you already proved is not.

More generally: when a broker answers from a *different* address than the one you
used, treat the new address as **additional**, never as a replacement. Two
candidate routes beat one, and the one with a delivery receipt behind it is the
one to fall back to when the new one fails.

This is the mirror image of §39 (the address named for the thing it refuses) and
§40 (read the postmaster domain on every bounce): in all three, the address a
message *appears* to come from is not the address that works.

---

## §47 Grey is not evidence — `.value` versus `.placeholder` is

The standard trap is a field that renders grey text and is actually empty, because
grey means placeholder. So the standard reflex is: grey → empty → retype it.

One opt-out form inverts the convention. The fields pre-filled from a verified
emailed link render **grey**; everything typed afterwards renders **black**. The
colour marks *provenance*, not emptiness. Every grey field held a real value and
an **empty** `placeholder`.

Checking costs one line, and it settles the question outright:

    Array.from(document.querySelectorAll('form input'))
         .map(i => ({n: i.name, v: i.value, ph: i.placeholder}))

> **Do not infer field state from colour.** Retyping a field that was already
> correct is harmless. Concluding "this form lost my data", abandoning a
> single-use link with a 24-hour expiry, and starting the whole route again is
> not.

The general rule this belongs to: **the rendered page and the DOM are two
different sources, and where they disagree the DOM is the one that gets
submitted.** The same principle recovers addresses split across `mailto:` tags,
reversed in CSS, or emitted from a `data-cfemail` attribute (§41).

### A related defect in the same form

Its inputs collide on `name`: three separate boxes were `name="firstName"` (first,
middle *and* last) and two were `name="address"` (street *and* date of birth). The
site's own submission works, presumably reading nodes positionally — but the form
cannot be reconstructed from its field names, and anything that serialises by name
loses data with no error.

---

## §48 A machine-read email can corrupt the link it is carrying

A broker mailed a single-use, personalised, 24-hour opt-out URL. Retrieved through
an API, the ticket parameter came back as `ticketid` + U+FFFD + a partial number.

It was not the sender's fault. The same corruption appears in the message's own
`<head>`: `content="width<?>vice-width"` for `width=device-width`, and
`content="IE<?>ge"` for `IE=edge`. The transport was eating `=` plus the two bytes
after it, everywhere in the message.

> **Calibrate against a string you can predict before trusting one you cannot.** A
> boilerplate meta tag is a free test: if `width=device-width` is mangled, every
> other `=` in that message is suspect — including the one carrying your ticket,
> your token, or your request ID.

**Practical recovery, in order:** try the URL with the damaged parameter dropped
(it worked here — the form loaded and accepted input); if that fails, open the
message in a normal client; if that fails, ask for a fresh link and start the
clock again.

And note the second, unrelated defect in the same URL: `mn=undefined` — not empty,
the literal seven-character string, leaked out of the site's own JavaScript into
the query string and pre-filled into the Middle Name box, where it would have been
submitted as a middle name if nobody looked.

---

## §49 The option grid that looks multi-select and behaves single-select

A rights portal presented seven request types as a grid of rounded buttons:
Access, Delete, Do Not Share or Sell, Correct, Limit Use of Sensitive Information,
Opt-Out of Targeted Advertising, Opt-Out of Profiling.

Buttons, not checkboxes and not radio pips. So the natural move — pick Delete, then
add the opt-outs to be thorough — reads as accumulating selections.

It is a radio group. Each click **replaced** the last. Four clicks later the form
was set to the narrowest right on the grid, and nothing on screen said so: the
previously-chosen button simply stopped being highlighted, which looks identical to
never having chosen it.

> **Buttons that look like checkboxes and act like radios are common in these
> portals, and the interface will not correct the belief that you selected
> everything you wanted.**

The DOM is unambiguous where the styling is not:

    Array.from(document.querySelectorAll('[role="option"]'))
         .map(b => ({t: b.textContent.trim(), sel: b.getAttribute('aria-selected')}))

Exactly one `true` in a group means radio. Check it **before** submitting, because
after submission the only artifact is a request ID, and the request ID does not say
which right it carries.

This is the same family as §47 (grey is not evidence): in both, the rendered page
and the submitted state are different sources, and only one of them is real.

**A note on why it matters more here than it looks.** These grids sit on deletion
forms. The failure is not cosmetic — it is the difference between a deletion and a
do-not-sell, and the confirmation email will cheerfully confirm whichever one
actually went.

---

## §50 The one-time code that expires faster than the handoff

A portal comment could only be read by signing in. Signing in required passing an
image CAPTCHA, which mails a one-time access code. Fine — stage the CAPTCHA, hand
off one human action.

Except the code said:

> "For security purposes, this code will expire in **15 minutes**."

The human cleared the CAPTCHA. The code arrived. By the time anything looked at the
mailbox again the code was thirty minutes dead, and the portal was no closer to
being open than before.

> **A handoff can only carry a step that is atomic.** If the human action produces
> a short-lived secret that a *second* step must consume, the two are one action,
> and splitting them across an automation boundary guarantees the timer wins.

**What to do instead.** Write the queue entry as a single sitting with the sequence
spelled out and the expiry stated in the first line — enter email, solve CAPTCHA,
Send, go to inbox, click "Already have an access code?", paste. And say plainly
that the gap cannot be bridged, because a browser tab does not survive between
passes and a fresh code will be needed otherwise.

The general shape, worth checking for whenever a route is queued for a human:

> **Ask what the human action *produces*, not just what it costs.** A CAPTCHA that
> unlocks a page is one action. A CAPTCHA that mints a fifteen-minute token is two,
> and the second one has a clock on it.

---

## §51 Your mail client rewrites the URLs in your own letters

A broker's reply contained a line that looked like ordinary friction:

> "I was unsuccessful in accessing the information from these links."

The links in question were two bare site names typed into the letter. What arrived
at the far end was neither:

    https://www.google.com/url?q=http://usatrace.com&source=gmail&ust=<mangled>&sa=E

The webmail client had silently rewritten every plain URL in the outgoing message
into its own click-tracking redirect, and a parameter in the wrapper did not
survive the round trip — so the recipient got an address that neither resolved nor
obviously corresponded to the site being discussed.

> **The letter you compose is not the letter that arrives.** Bare URLs are
> linkified and wrapped on send. The recipient sees the wrapper, not what you
> typed, and a broken wrapper reads as a malformed or evasive request rather than
> as a client-side artifact.

This matters more than it sounds, because URLs in these letters are load-bearing:
profile links a broker asks for, sibling-site names in a family request, a
registry entry cited as evidence. A support agent who cannot open the link
reasonably concludes there is nothing there.

**What to do.**

- **~~Do not put a bare URL in an outbound letter when the plain domain name will
  do.~~ THIS MITIGATION DOES NOT WORK — see the correction below.**
- **Where a real link is unavoidable** — a profile URL the broker asked for —
  say in the same sentence what it points at, so a mangled wrapper is still
  actionable: *"the results page for <name> in <city>, at <domain>/…"*.
- **Read your own sent copy**, not your draft, when a reply says a link failed.
  The evidence is in the sent message, and it will not match what you wrote.

**And when it has already happened, say so.** The broker above had spent real
effort on links that were never going to work. A short "that was my mail client,
not you, and here is what I actually meant" costs nothing, closes a false trail,
and is the difference between a cooperative correspondent and one who has quietly
written you off as a time-waster.

### Correction (2026-08-19): a bare domain name gets rewritten too

The advice above was tested and it failed. A later letter deliberately avoided
URLs and wrote the two sites as **plain domain names in running prose** —
`privaterecords.net` and `privatereports.com`, no scheme, no path, no anchor.

The broker's quoted copy of that letter shows both rewritten into
`google.com/url?q=…&source=gmail&ust=…` redirects anyway.

> **The client linkifies anything that *looks* like a hostname, then wraps the
> link it just created.** Removing the scheme does not help, because the
> linkifier is matching on the dotted label, not on `https://`.

So the same message that apologised for mangled links contained freshly mangled
links, in the sentence doing the apologising.

**Mitigations that actually survive**, in rough order of preference:

- **Break the dot.** `privaterecords [dot] net` is not a hostname to a linkifier
  and is unambiguous to a human. Ugly, and worth it.
- **Insert a zero-width or ordinary space** before the TLD — but check the sent
  copy, because some clients strip it and re-linkify.
- **Describe rather than name.** "the sibling site whose name is yours with
  *reports* in place of *records*" carries the question with no hostname at all.
- **For opaque tokens** — a request ID, a ServiceNow `sysparm_id`, an
  order number — there is no dot, so plain text is genuinely safe. Ask the broker
  to send those *unlinked*, and send yours the same way.

**And the general rule this belongs to:**

> **Verify a workaround against the sent copy before recommending it.** The draft
> is not the artifact. This entry confidently prescribed a fix for four days
> before anyone checked whether it worked, and it did not.

---

## §52 "We have no record of you" from a business you were never a customer of

A property marketplace answered a deletion request:

> "We attempted to process your Request to Delete. However, we do not have a record
> of you in our system. **If you previously interacted with us using a different
> email address**, please [tell us]."

That closing clause is the whole thing. It reveals what was searched: **interactions
keyed on email address**. A customer-account lookup.

For a people-search site, "do you have a record of me" and "have I interacted with
you" are the same question, so the answer is complete. For a marketplace,
aggregator, or any business that compiles data about non-customers, they are
different questions — and the compiled data is precisely the part a consumer
request is about.

> **Read a null result for the key it was searched on.** "No record of you" scoped
> to customer interactions says nothing about listing data, agent records,
> address-keyed records, or anything acquired from a third party about someone who
> never visited the site.

**The follow-up that resolves it** accepts the negative for what it covers and asks
the narrower question rather than re-asserting the original one:

> *Did you search only customer interactions, or also any listing, agent, or
> address-keyed records you hold about people who are not customers?*

That is answerable in one line, it does not accuse anyone of anything, and it
distinguishes a genuine `not_found` from a search that never looked in the right
place. Until it is answered, the negative is real but partial.

---

## §53 A bot-gated route is a snapshot, not a property

An entry here carried a flat verdict: *"no working self-service route — every route
fails"*, with `/opt-out` recorded as **"Cloudflare challenge on page load — never
reaches the form"**. That was accurate when written, and it had been true across
repeated attempts.

Re-tested six weeks later, the same URL loaded with no interstitial at all,
rendered the form, and accepted input.

> **Cloudflare posture is configuration, not architecture.** Bot-fight mode,
> challenge thresholds and path rules get turned up during an attack and quietly
> turned down afterwards. A route that blocked every attempt one month can be wide
> open the next, and nothing announces the change.

The failure mode this creates is a slow one: a `failed` or `manual_required` entry
looks settled, so nobody re-tries it, so it stays settled. The record outlives the
condition that produced it.

**What to do.**

- **Re-test bot-gated routes on a schedule**, not only when something prompts you.
  They are the cheapest re-checks available — one page load answers it.
- **Keep the old finding as history rather than deleting it.** The failures were
  real, and if the route re-gates you want the previously-discovered alternative
  door (here, a rights form on a different path that was never gated) still written
  down.
- **Date the verdict in the file.** "Every route fails" with no date reads as a
  permanent property. "Every route failed as of <date>" reads as what it is.

The same caution applies in reverse: a route that works today can gate tomorrow, so
a staged form left half-finished may not be resumable at the same URL.

---

## §54 The removal form hosted on a platform that revoked it

A broker's removal page is well written. It explains the process, carries an FAQ
promising completion *"between 24 to 48 hours"*, and says:

> "To remove your info, please submit your request by filling out this form."

The form is a **Google Form**. Following it returns:

> "We're sorry. You can't access this item because it is in violation of our Terms
> of Service."

Not a broken link. Not an expired document. Google assessed the form and took it
down — and the broker's page is unchanged, still instructing people to use it.

> **A rights route hosted on someone else's platform can be revoked without the
> broker noticing or caring.** The page keeps its confident wording, the link keeps
> its shape, and the failure lives one click away where the operator never looks
> and the consumer assumes they did something wrong.

**Check the destination, not the page that points at it.** This is the same lesson
as a published-but-dead mailbox (§39), one layer out: the difference is that a
third party can break this one unilaterally.

Two things follow.

**Test the outbound link as a separate step.** A playbook entry recording "removal
form at `/remove-my-info`" is recording the page, not the route. Record the
destination and re-test *that*.

**And it is the one failure that can silently repair itself.** A 404 stays a 404
until someone fixes it; a platform suspension can be lifted, or the broker can
create a new form and update the link. So this class of `failed` deserves a
shorter re-check interval than most — it costs one page load.

---

## §55 The required field the site will not issue

A sibling of the above has a form that genuinely works. It is unusable anyway,
because one required field cannot be filled:

    URL (Please paste the URL you request to remove) *

The site's own people search accepts a name and then **does not navigate** on
submit. Guessed profile paths in the obvious shape return a 404 — into a page
monetised with competitor advertising.

So the only removal route demands an artifact the site itself refuses to produce.

> **Distinguish this from the ordinary "send us the profile link" deflection.**
> That one is satisfiable with effort: search, find, copy. This one is a locked
> door with no key issued — and the broker never has to refuse anything, because
> the request simply never arrives.

It is worth recording as `manual_required` rather than `failed`, because the
blocker is specific and might be cleared by a human who can work the search UI
interactively, or by finding the profile through an external search engine rather
than the site's own box.

**And say so in writing to the operator.** A support desk being told "your form
requires a URL and your search does not return one" is being handed a fault report
they can act on. It is also the sentence that makes a later escalation coherent:
the route was not refused, it was impossible.

---

## §56 Two identical replies in one thread means you are talking to a machine

A support address answered a consumer request with a template asking for five
specific fields. The reply supplied **every one of them** — name, aliases, date of
birth, current and prior addresses, current and prior phone numbers, a dozen email
addresses.

The same template came back, quoting the reply it was answering.

> **A support address that re-sends the same text in response to a message
> containing everything it asked for is not a queue with a backlog — it is an
> autoresponder.** Replying again only re-triggers it, and the thread can run
> forever without a human ever reading it.

**The test is cheap: two byte-identical messages in one thread.** One is a template
sent by a person who has not read closely. Two is a machine. Three of four sites in
one family did it within the hour.

**What to do at the second one:**

- **Stop replying.** Every further message is free ticket volume for them and
  nothing for you.
- **Change channel.** Web opt-out form, a privacy address published elsewhere on
  the site, a registry contact, a postal address.
- **Record it as the finding it is.** "support@ is an autoresponder loop" is a fact
  about the route, and it belongs in the file next to the address so nobody spends
  another hour on it.

A useful corollary: because the loop fires on *every* inbound message, an
autoresponder tells you nothing about whether the original request was received or
read. Do not treat it as an acknowledgement.

---

## §57 The search box that is an affiliate funnel

A removal form required a profile URL. The obvious way to obtain one is the site's
own people-search box. Submitting it appeared to do nothing — the page stayed
where it was, no results, no navigation.

It had not done nothing. It had opened **two third-party brokers in background
tabs**, each carrying the query in the URL:

    truthfinder.com/search/?…utm_campaign=<this site>…firstName=…&lastName=…
    intelius.com/phone/search/?…utm_campaign=<this site>…phone=…

The name went to one, the **telephone number** to the other, both tagged with the
referring site's affiliate campaign and sub-ID.

> **A consumer searching for their own profile — in order to satisfy the same
> site's removal form — instead hands their identifiers to two further brokers as
> paid traffic.** The removal route and the leak are the same click.

**What this changes about how to work these entries:**

- **Never use a people-search site's own search box to locate your profile for an
  opt-out.** Use an external search engine with a `site:` restriction; the query
  then never reaches the broker or its partners.
- **"The search did nothing" is a conclusion to distrust.** Check the tab list, not
  the page. A search that navigates *away from the domain* is an affiliate handoff,
  and the original page sitting unchanged behind the new tabs is exactly what a
  broken form would also look like.
- **Treat anything that appears in an outbound affiliate URL as disclosed** to that
  partner, and add the partner to the removal list if it is not there already.
- Close those tabs rather than interacting with them. Continuing the flow on the
  partner site is a second disclosure, and the partner has no idea the visit
  originated in a privacy request.

A darker reading is available and is not necessary: whether or not the funnel is
deliberate, the effect on the requester is identical, and that is what the file
should record.

---

## §58 The percent-encoded value that a form reads back verbatim

A two-step opt-out mailed a personalised link with the requester's address encoded
into the **path**:

    /opt-out/removal-identification/<uuid>/jane%40example.com?fn=…&mn=…&ln=…

The form parsed the path and pre-filled its Email box — **without decoding**. The
field arrived containing the literal string `jane%40example.com`.

> **A `%40` in an email field is a valid-looking value that is not an email
> address.** It survives a glance. It may survive the form's own validation, since
> `%` and `40` are legal characters in a local part. And the request is then filed
> against an address nobody owns — so the confirmation goes nowhere, and the
> requester's evidence that they ever filed is a page they saw once.

Same family as §47 (grey is not evidence) and §38 (the field that looks committed
and is not): **a pre-filled field is a claim, not a fact.** Read the value, do not
read the fact that the box is non-empty.

**Where to look for this generally:** any flow that puts user data in a URL and
reflects it back. Encoded `@` (`%40`), spaces (`%20` or `+`) in a street address,
and apostrophes (`%27`) in a surname are the common ones. A surname arriving as
`O%27Brien` fails to match a record filed under `O'Brien`, and the removal then
returns "no record found" for a reason that has nothing to do with the data.

---

## §59 The invisible CAPTCHA that fails by doing nothing

An opt-out search form took a name, a city and a state, accepted them, and on
submit did **nothing**. No results. No error. No validation warning. The page sat
exactly as it was.

The form posted to its own URL and carried one hidden field:

    <input type="hidden" name="captchaId" value="">

Empty. The submission was being rejected for want of a token that was never issued
— and the rejection was silent.

> **A visible CAPTCHA announces itself and can be handed to a human. An invisible
> one has no challenge to see and no error to read, so its failure is
> indistinguishable from a form that is simply broken.**

What makes this worse than an ordinary dead form is what the silence *means* on a
people-search site. That operator's own reply had said:

> "If you are unable to locate your listing then it means your information was
> never collected, or has already been removed."

So an empty result is a **meaningful negative** — and a silently-rejected search
produces exactly the same screen. A requester following the instructions in good
faith would record a clean bill of health that was never issued.

**The check, before concluding a search found nothing:**

    Array.from(document.querySelectorAll('input[type=hidden]'))
         .map(i => ({n: i.name, v: i.value}))

A hidden field named `captcha*`, `token`, `nonce`, `csrf` or similar sitting
**empty** where a value belongs means the page on screen is not an answer.

**And check the form's own target while you are there** — `form.action` and
`form.method`. A form that posts to the URL it is already displaying, and returns
that same URL unchanged, is being rejected rather than answered.

> **Never record `not_found` off a search whose submit you did not see complete.**
> The evidence for a negative is a results page that says so, not the absence of a
> results page.

---

## §60 Do not accuse a broker of a fault in your own pipeline

Twice in one day I told a company something was wrong on their side, and twice it
was wrong on mine.

**Case one.** A broker's satisfaction survey arrived with no resolution message. I
had just documented that exact pattern as a silent close, matched on it, downgraded
a settled `not_found`, and emailed asking them to redo work. They had answered
fully the previous day; the survey was an ordinary auto-close *after* a resolution.
I had matched the pattern without reading the thread.

**Case two.** A broker's rights-portal links arrived with the query parameter
destroyed. I told them the links were "corrupted in transit" and offered proof: the
damage appears in **both** the plain-text and HTML parts, so it could not be my
client reading the wrong half. They replied: *"Both links are working links."*

They were right. Both MIME parts come through the same retrieval path, so a fault
in that path corrupts both identically.

> **"It's broken in both parts" cannot distinguish the sender's outbound mail from
> your inbound processing.** That is precisely the question at issue — and I
> offered it as the answer to it.

The disconfirming evidence was already in this file. Unrelated messages arrive with
boilerplate `<meta content="width=device-width">` reduced to `width` + `<?>` +
`vice-width`. Same signature, in text no broker wrote (§48).

### The rule

> **Before telling a broker their system is broken, ask what your own tooling would
> look like if it were the thing at fault — and check whether you can tell the
> difference.** If the evidence is identical under both hypotheses, you do not have
> evidence. You have a hypothesis you like.

**Cheap discriminators, all of which were available and unused:**

- **A control string.** Find something in the same message that the sender did not
  author — a boilerplate meta tag, a standard footer, a vendor's tracking
  parameter. If *that* is damaged too, the fault is downstream of the sender.
- **A second retrieval path.** Open the message in a normal client. One look
  settles it.
- **Read the thread before matching a pattern.** A survey with a resolution behind
  it and one without look identical; only the history distinguishes them.

### Why it matters more than being embarrassing

These exchanges depend on goodwill. A support desk that gets a confident, detailed,
wrong accusation learns that this correspondent is unreliable — and the next
message, the one that is right, gets read accordingly. Both companies here were
patient; one took the trouble to correct me in four words rather than ignoring it.

> **When you are wrong, withdraw the claim explicitly, name the reasoning error,
> and do it before asking for anything else.** "My argument was worthless and here
> is why" costs one paragraph and buys back the credibility the next request needs.

And record it in the file. A playbook that only contains the times the technique
worked is a playbook that will produce the same false positive again.

---

## §61 The link whose text and target disagree

A broker's site displays a contact address in its announcement bar. Rendered, it
reads correctly. The markup behind it does not:

    <a href="mailto:info@attritbits.com">
      <em>info@attribits.com</em>
    </a>

The **displayed text** is the real address, on a domain with working Google MX.
The **`mailto:` target** transposes two letters, and that domain has **no NS and no
MX at all** — it does not exist.

So the failure mode splits by how a person uses the page:

- **Read the address and type it** → the mail arrives.
- **Click the address** → the mail client composes to a domain with no zone, and
  the message hard-bounces.

> **A published contact can be simultaneously correct and broken.** Every automated
> scraper, every "copy the link address", and every ordinary click takes the
> `href`. Only a human reading with their eyes takes the text — and they are the
> minority.

This is the inverse of §41 (an address obfuscated in `data-cfemail` where the
*source* is right and the rendering is missing). Here the rendering is right and
the source is wrong, which is worse, because nothing looks amiss at any point.

**How to catch it.** Never harvest a contact address by reading the rendered page.
Pull the `href` and compare:

    Array.from(document.querySelectorAll('a[href^="mailto:"]'))
         .map(a => ({shown: a.textContent.trim(),
                     target: a.href.replace(/^mailto:/, '')}))
         .filter(x => x.shown !== x.target)

Any row that survives that filter is a bug — usually harmless (a display name), and
occasionally this.

**Then check both domains resolve**, because the disagreement alone does not tell
you which side is wrong. Here a `dig NS` on each settled it in one command: one had
nameservers and mail, the other had nothing.

**And report it.** A neighbouring field in the same CMS record held the *correct*
mailto URL, so this is a data-entry slip rather than anything deliberate. The
company almost certainly does not know that every consumer who clicks their privacy
contact is bouncing — and unlike most findings in this file, it costs them one
character to fix.

> **When a contact route is broken by a typo rather than by policy, say so
> plainly and separately from the request.** It is the one kind of fault report
> that is unambiguously good news for the recipient.

---

## §62 The contact form that is pure markup

A site's only surviving contact route was its Contact page form: a reason
dropdown, name, email, message, and a **Send Message** button. It accepted input
normally. Clicking Send did nothing — no navigation, no spinner, no success
banner, no validation error. The page simply sat there with the fields still
populated.

Three checks settled what was happening, and the third is conclusive:

    document.querySelector('form')            // → null
    button.outerHTML                          // → <button type="button">Send Message</button>
    String(button.onclick)                    // → "null"

**There is no form element on the page.** The button is not a submit button, and
nothing is bound to its click. No script on the page even references the field
ids. The whole thing is styled markup.

> **This is not a form that failed. It is a form that never existed.** A person
> fills it in, clicks Send, sees the page unchanged, and concludes either that it
> worked quietly or that they did something wrong. Nobody at the company ever
> learns they have a contact page that cannot be contacted.

### How it differs from the invisible-CAPTCHA case (§59)

Both look identical on screen — fill, click, nothing happens. But there a real
request was made and **rejected**; here **no request is made at all**. The
distinction matters because it changes what to try next: a CAPTCHA-gated form may
work for a human, so it is worth handing off. A form with no handler will not work
for anyone, so handing it off wastes someone's time.

**Tell them apart before queueing anything for a human:**

| check | gated form | decorative form |
|---|---|---|
| `document.querySelector('form')` | an element | `null` |
| button `type` | `submit` | `button` |
| `onclick` / listeners | present | `null`, none |
| network tab on click | a request appears | nothing |
| hidden `captcha*` field | present, empty | absent |

### What it means for the record

This site's other two published routes — both email addresses, one printed on the
Contact page itself — hard-bounced with 550. So every published route failed, and
the entry is `unreachable` rather than `failed`: there is nothing left to retry
except a telephone number.

> **Record "unreachable" only after checking whether each route is broken or
> merely gated.** The status is a claim about the company, and it should not rest
> on a form you did not inspect.

One mitigating note worth keeping alongside it: this particular operator's own
homepage states plainly that it is a directory of links to government sources and
holds nothing about individuals. So the likely exposure is nil — what is
unreachable is the ability to have that confirmed for a specific person.

---

## §63 The rights portal that renders no form

A company's autoresponder named its Privacy Choices Portal as *"the most efficient
way for you to submit your verified request"*, and refused the email route without
an extra identifier.

The portal loads. It shows a heading, and two lines of explanatory text — *"You can
use this form to submit a request regarding your personal information"* and
*"Please note that all requests for deletion are permanent."*

Then nothing. Below the text sits an embedded HubSpot frame, **680 × 1310 pixels,
with an entirely empty document body**: no fields, no labels, no submit control.
The host page has no input elements of its own either.

    document.querySelectorAll('input,select,textarea').length   // → 0
    iframe.contentDocument.body.innerHTML.length                // → 0

Reloaded, waited, re-checked. The frame stays empty.

> **The layout reserves 1310 pixels for a form that never arrives, so the page does
> not look broken — it looks like a form that has not scrolled into view yet.** A
> person who lands here scrolls, finds nothing, and is far more likely to conclude
> they are doing it wrong than that the company's rights portal is dead.

### Why this one is worse than a dead link

A 404 is honest. This page is confident, well-designed, and describes a form that
is not there — and it is the route the company's own autoresponder pushes you
toward, *while simultaneously refusing the alternative route* unless you hand over
an additional identifier.

> **When one route is broken and the other is conditional, check whether the
> condition is the only thing standing between the consumer and their right.** Here
> it was: the portal presented no form, and email was refused without an identifier
> the request did not require. Neither fact alone is remarkable; together they
> close the door.

**Say that plainly, and separate it from the argument.** The fault report lands
better when it is explicitly not leverage — *"I would have reported it regardless,
and I would rather it were fixed for everyone who reaches it than get an exception
for myself."* Then offer more than one way out, so fixing the embed is not the only
path to closing the request.

### Three form-failure modes, all identical on screen

This is the third distinct one in a single day, and they need different responses:

| mode | what happens | what to do |
|---|---|---|
| **gated** (§59) | request made, silently **rejected** — hidden empty `captcha*` | hand off to a human; it may work for them |
| **decorative** (§62) | **no request at all** — no `<form>`, button has no handler | do not hand off; it works for nobody |
| **absent** (§63) | form **never renders** — empty embed frame | report as a fault; ask for a second route |

The diagnostic order is cheap: count inputs on the page and in any frame, look for
a `<form>` element, check the submit control's `type` and handlers, then look for
an empty hidden token field. Four checks, and they separate "try again as a human"
from "stop and write to them instead".

## §64 The working address is the one your scraper cannot see

ROC Advertising's registry entry pointed at a compliance-service mailbox on a
third party's domain. It hard-bounced:

> `550 5.1.1 ... the address couldn't be found, or is unable to receive mail`

Their own privacy policy does publish a working address. But it is not in the
page text. It is written as HTML character entities:

```
&#112;&#x72;&#x69;&#118;&#x61;&#x63;y&#x40;&#x72;o&#99;&#x61;d&#118;&#x65;r&#116;&#x69;s&#105;&#x6e;g&#46;&#x63;&#x6f;&#109;
```

That is an ordinary anti-harvesting trick, and it works — it defeated it on the
first two passes of my own tooling, which greps the fetched HTML for something
shaped like an address. The browser renders it perfectly; the regex sees a wall
of `&#x` and moves on. The same page encodes the address a second time with a
*different* mix of decimal and hex escapes for the same characters, so even a
naive "unescape the one pattern I saw" fix would have missed the second one.

**The general shape.** A machine-readable address and a working address are
different properties, and they are anticorrelated in exactly the place it hurts:
a company that cares enough about harvesting to obfuscate its real contact often
leaves a plain-text address on some directory listing, and that plain-text one is
the stale one. So the address your pipeline finds most easily is disproportionately
likely to be the dead one.

**The fix is one line.** Unescape entities before extracting:

```
sed 's/<[^>]*>/ /g' page.html \
  | python3 -c "import sys,html; print(html.unescape(sys.stdin.read()))" \
  | grep -oiE '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}'
```

Do this on **every** privacy-page fetch, not only when the plain scrape comes
back empty — because the failure mode that costs you is not "no address found",
which is visible, it is "found a different, dead address", which is not.

**Two adjacent variants to check while you are there.** Addresses split across
elements (`privacy` `<span>@</span>` `example.com`) survive tag-stripping only
because the strip inserts a space — so also match `name ?@ ?domain`. And
addresses written `name [at] domain [dot] com`, which no email regex will ever
catch; grep for `\[at\]` and `\(at\)` separately.

**Related:** §45 (the registered contact quietly retired), §55 (the required
field the site will not issue), §61 (the link whose text and target disagree).

## §65 Both published addresses are dead and the domain is fine

Search Systems publishes `info@` on its own `/contact` page. It hard-bounces
550 5.1.1. So does `webmaster@`, the address listed for them elsewhere. The
domain itself is healthy — it has live Zoho MX records and answers on 443.

This is worth separating from §45 because the diagnosis is different. In §45 a
human told me the mailbox had been retired. Here nothing tells you: a live MX
with no live mailboxes behind it produces a bounce that looks exactly like a
typo on your side, and the natural next move — guess another local part — is
the wrong one. Two 5.1.1 rejections from a domain that is otherwise healthy is
not bad luck about local parts; it means **nobody is reading mail at that domain
at all**, and the published address is decoration left over from an earlier
staffing arrangement.

Stop guessing after the second bounce. The signal to distinguish:

| observation | reading |
|---|---|
| `5.1.1` on one guessed local part | try the published one |
| `5.1.1` on the **published** local part | the page is stale — look for a form |
| `5.1.1` on two or more, incl. published | the domain accepts no mail; email is not a route |
| `5.7.1` on any | policy rejection — stop immediately, they see you |
| no MX / null MX | the domain never accepted mail; do not try |

When you land in row three, the remaining route is whatever is not email: a
contact form, a rights portal, or a postal address. Record the domain as
email-dead in the registry with the evidence, so a later pass does not spend the
same three sends rediscovering it.

**Related:** §45, §46, §64.

## §66 The mailto: href and the link text are different mailboxes

SourceIT's privacy policy presents its contact address as an ordinary hyperlink.
Here is the whole anchor:

```html
<a href="mailto:dataprivacy@sourceitmarketing.com">dataprivacy2026@sourceitmarketing.com</a>
```

Those are two different mailboxes. The one you *see* is live. The one you
actually mail when you click is dead — rejected by their own Office 365 tenant:

> "Your message to dataprivacy@sourceitmarketing.com couldn't be delivered.
> dataprivacy wasn't found at sourceitmarketing.com... Recipient Unknown"

So the page works for anyone who retypes the visible address by hand, and fails
for anyone who does what the page invites them to do. The three plain-text
occurrences elsewhere in the same policy all carry the year stamp, which tells
you what happened: the mailbox was rotated, the prose was updated, and the href
was missed.

**Two things make this worse than an ordinary stale contact.**

*The year stamp is a rotation signal.* `dataprivacy2026@` implies a
`dataprivacy2025@` that is now gone and a `dataprivacy2027@` that does not exist
yet. Every address you cache from a site like this has an expiry date, and every
aggregator listing of it is guaranteed to go wrong on a schedule. When you see a
year in a privacy mailbox, record *when* you verified it, not just that you did.

*It defeats naive verification twice over.* My checker extracts addresses from
the fetched HTML and confirms the registry entry if it appears. Both addresses
appear — one in the href, one in the text — so the dead one verified as
`CONFIRMED` and stopped me looking. **A false CONFIRMED is worse than a
NO_EMAIL**, because NO_EMAIL sends you to look and CONFIRMED tells you to stop.

**Diagnosis.** Compare href against text explicitly; do not extract from the raw
HTML and treat the union as one pool:

```
grep -oiE '<a[^>]*mailto:[^"]*"[^>]*>[^<]*</a>' page.html
```

If they disagree, **both are candidates and neither is authoritative.** The
tie-break is the surrounding prose: whichever address the policy also states in
running text, unlinked, is the one a human wrote on purpose. Failing that, mail
the visible one — a person maintaining a page looks at what renders.

**This is §61 with the polarity reversed.** There (attribits) the displayed text
was correct and the href carried a typo'd domain that had no NS or MX at all,
which is easy to spot. Here the href is a perfectly well-formed address on a
live domain with live MX — it just has nobody behind it. The general rule that
covers both: **a link is two independent claims, and a page can be right about
one and wrong about the other.**

**Related:** §45, §61, §64, §65.

## §67 The source that is not a data broker, and that no name search will lead you to

A people-search page turned out to carry, alongside the usual addresses and
relatives, a block headed "websites and domain names" — thirty domains with the
registrant's name, contact postal address and telephone number, drawn from
**historical WHOIS registration records**.

That data has a specific and unusual history. For roughly two decades, the price
of registering a domain was publishing your name, postal address, telephone
number and email in a public directory. Redaction is now the registrar default,
so a WHOIS query today returns a privacy service — but **the archives outlived
the practice**. Snapshots taken while the records were open are held and resold
by domain-intelligence firms, and resurface inside people-search profiles years
later.

**Why this is a silent failure rather than just another broker.** A removal
project can be complete across a thousand people-search sites and this data will
still be standing, for three compounding reasons:

1. **It is keyed to whoever you were at registration time.** The address on a
   registration made fifteen years ago is an address that may appear in no other
   dataset you are working through — so it survives every removal keyed to your
   current details, and it is invisible to any verification that searches your
   current details.
2. **You cannot enumerate it.** WHOIS history is not searchable by person
   without a paid account at one of the intelligence firms. You cannot audit
   what exists about you; you can only ask them, which is why "tell me what you
   hold, in categories" matters more here than in an ordinary deletion letter.
3. **It is downstream-only where you find it.** Removing it from the
   people-search site that surfaced it does nothing to the archive it was
   licensed from. This is the one case in this project where the *discovery* and
   the *fix* are reliably at different companies.

**Where to write.** DomainTools was already tracked; ViewDNS, WhoisXML API,
SecurityTrails, Whoxy, DomainIQ and DomainBigData were not, and are now. Only
ViewDNS publishes a contact address in page text — three of the others return
403 or a Cloudflare 530 to scripted fetches, and two serve privacy and contact
pages with no address on them at all.

**The defence to expect, and the answer.** "That data was lawfully public when
it was published." Two responses, and the second is the stronger:

- The publication was **a condition of registering a domain**, not a decision
  about publicity. And the industry itself concluded the practice was wrong —
  which is why redaction is the default now. Pointing at their own sector's
  reversal is more persuasive than pointing at a statute.
- Whatever the position on the original publication, **the republication and
  commercial supply of it today is a separate act, done by them, now.** Being
  lawfully published in 2006 is not a licence to sell it in 2026. Keep the
  argument on the present act; it is the one they control and the one a statute
  actually reaches.

**Worth checking on yourself.** Search a people-search aggregate page for
"registered by", "Registrar:", or a registrar name (GoDaddy, Tucows, eNom,
Network Solutions). If a domain you registered appears with an old address next
to it, this category applies to you.

**Related:** §52 (no record of you from a business you were never a customer of),
and `_CATEGORY_VARIANTS.md` on identity graphs.

### §67 — correction, and the mistake worth keeping

Within thirty minutes of the first letter, a named person at ViewDNS replied:

> "I'd be interested to know where you saw historical WHOIS data on our site? We
> currently don't offer such a tool. Given this, I would also be interested to
> know where suggested we do?"

He was right. **ViewDNS does not offer a historical-WHOIS tool, and the section
above should not have implied that any specific firm on that list does.** The
list was assembled by reasoning from a category — "who sells this kind of data?"
— and then written to as though it were a finding about each company. I had
evidence that the *data* exists and is republished; I had no evidence about
*their* product line, and I did not check it before writing.

Note carefully what the error was, because it is subtler than a false accusation
and easier to repeat. The letter never claimed to have found the data on their
site; it said, accurately, that it was found on a third-party people-search
aggregate. The fault was **tone and aim, not a false statement**: a letter built
on a category inference was written in the register of a letter built on
evidence. The recipient cannot tell those apart from the outside, and is
entitled to read the more accusatory one.

**The rule.** A category letter must announce itself as one. "I found this data
republished elsewhere and I am writing to firms that may hold the underlying
records — do you?" costs one sentence, is completely honest, invites the same
answer, and cannot blow up in your face. Reserve the confident register for the
company you actually have evidence about.

**And the correction is where the request got better.** ViewDNS does run a
**Reverse Whois Lookup**, which their own page describes as: "Simply enter the
email address or name of the person or company to find other domains registered
using those same details." That is person-keyed by construction — a human's name
or email in, facts about that human out — which implies an index mapping
registrant identities to domains, and *that* is what the letter should have been
about from the start. The question that replaced the original four asks is one
their database can answer: does that index retain registrant details from
records now redacted at the registrar, or only reflect currently-published
WHOIS? An "only current" answer closes the matter.

**One asymmetry worth recording.** Their reverse lookup requires an account. So
the subject of a reverse-whois result is the one party who cannot see it without
registering, while anyone else can. That pattern — *the data subject is the only
person who has to identify themselves to learn what is published about them* —
is worth naming wherever it appears.

**Standing correction to the list above:** the six firms named are targets in a
category *hypothesis*, not confirmed historical-WHOIS providers. Their registry
entries record this. Verify each one's actual product line before writing to it.

**Related:** §60 — do not accuse a broker of a fault in your own pipeline. This
is its sibling: do not accuse a broker of a business you inferred.

## §68 The outsourced compliance route that outlived its vendor

Twice in one day, on unrelated brokers:

| broker | published privacy contact | result |
|---|---|---|
| ROC Advertising | `dataprivacy_rocadvertising@` **simpleoptoutcompliance.com** | `550 5.1.1` |
| Tymax Media | `privacyofficer@` **datacomplianceportal.com** | bounce; site returns Cloudflare **522**, origin down |

Both are third-party "compliance portal" vendors, hired to be the address a
consumer writes to. Both are gone. Neither broker updated the listing.

**Why this fails silently and specifically.** A vanity compliance domain is
built to look like an endpoint that will outlast staff turnover — which is
exactly what makes its failure invisible. The broker's *own* domain still
resolves, still has MX, still passes every registry health check you would
think to run, because the dead thing is somebody else's domain. Check the
broker's domain and you learn nothing about whether the request arrives.

**The tell in the address itself.** `dataprivacy_<brandname>@<vendor>.com` and
`privacyofficer@<vendor>.com` are both shaped like a shared mailbox partitioned
by client. When you see a privacy contact on a domain that is neither the
broker's nor a household-name platform (OneTrust, DataGrail, Ketch, Transcend),
treat it as **unverified until it delivers**, whatever the aggregator listing
says.

**Tymax is the fuller version of the failure** and worth reading as a diagnostic
sequence, because the first three checks all say "healthy":

```
dig A tymaxmedia.com      -> resolves
dig MX tymaxmedia.com     -> live Outlook MX
registry entry            -> looks complete
https://tymaxmedia.com/   -> TLS cert does not match the hostname
http://tymaxmedia.com/    -> 200, 62 bytes: "This website is for lease."
dig SOA                   -> serial 2017…
```

A resolving domain with live MX and a for-lease parking page is a company that
has stopped existing without telling its DNS. **A privacy contact is only as
alive as the least-alive hop in the chain**, and the chain here is broker →
vendor → mailbox, with the registry only ever showing you the first link.

**What to do.** When a compliance-vendor address bounces, do not go looking for
another local part at the vendor — go to the broker's own domain and start
again. If the broker's own site is a parking page too, record `unreachable`
with the evidence rather than leaving it `pending`, because a pending entry
invites a future pass to spend the same three sends rediscovering this.

**Related:** §45, §64, §65 (the four bounce cases), §67.
