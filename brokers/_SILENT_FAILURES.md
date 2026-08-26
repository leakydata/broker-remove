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

### The second axis: whose records were searched

The key is one way a negative can be narrow. **Role** is the other, and it shows
up wherever the recipient is an agency, a bureau, or any firm that handles data
on behalf of clients.

A fundraising and marketing agency answered:

> "After searching our records, we did not identify any information in our
> databases associated with your name and/or address."

Both halves are narrow, and independently so:

| clause | what it silently excludes |
|---|---|
| "your name and/or address" | records keyed to email or phone — usually *the* key in a fundraising or marketing file, where the postal address is often absent or stale |
| "our records ... our databases" | client lists the agency **processes** rather than owns |

The second is the harder one, because the sentence can be completely true and
still leave the subject's data sitting in the agency's systems under a client's
name. An agency's own controller records are frequently empty; its clients' donor
and supporter files are the reason it was on a broker list in the first place.

**Ask it as a fork with an acceptable exit**, so the answer costs nothing:

> Does your answer cover data held for clients as well as data you hold in your
> own right? If those are your clients' records rather than yours, just say so
> and tell me it's their request to action — I'll take that as the answer and go
> to them instead.

Offering "it's the client's, go to them" as a complete answer is what makes it
answerable. It is also genuinely useful: a named client is a new, correctly
addressed request, which is a better outcome than an argument about who
controls what.

**Also worth flagging without making it the argument:** this reply described the
request as an *access* request when it was a deletion and opt-out request. That
mislabel is harmless while the answer is "we hold nothing" and stops being
harmless the moment a recheck finds something, because it determines which
process gets run. Note it, do not lead with it.

#### Correction: the wording was boilerplate, and the search was already broad

The agency answered the follow-up in six minutes, from a named analyst:

> "the response is a standard email reply, so I can understand the confusion. To
> clarify, we did check our records **and** client records we hold for all of
> those email addresses and phone numbers, and did not find any matches on any of
> those data points. We also treat all request as deletion requests, so if we had
> found any of your data, it would be deleted."

Every inference drawn above about *what they searched* was wrong. They had
searched their own records and client records, across every email address and
phone number, before the first reply went out. The "name and/or address" phrasing
was a template. So was "access request" — they treat every request as a deletion
request regardless of what the template calls it.

**Keep the follow-up. Drop the conclusion.** The asking was right and cost six
minutes to resolve. What was wrong was treating the wording as evidence about the
search rather than as evidence about the *template*. Those are different claims,
and only the second one is supported by a boilerplate reply:

> A canned negative under-describes the search that was run. It tells you what
> the template says, not what the analyst did. Ask which — do not record "they
> searched only X" as a finding.

This matters because the register of the ask changes with it. "Did you also
search email and phone?" is a fair question to a template. "You only searched
name and address" is an accusation, and it would have been false here.

The mirror-image risk is real too, and §11 covers it: a broad-sounding reply is
equally weak evidence that a broad search happened. **In both directions, the
wording of a canned reply is evidence about the canned reply.** The only thing
that resolves it is a person answering a specific question, which is exactly what
happened here — and what makes the one-line, everything-is-an-acceptable-answer
follow-up worth sending every time.

Recorded as a genuine `not_found`.

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
| NS delegated, but no A **and** no MX | the domain is a shell; there is no site and no mailbox |

When you land in row three, the remaining route is whatever is not email: a
contact form, a rights portal, or a postal address. Record the domain as
email-dead in the registry with the evidence, so a later pass does not spend the
same three sends rediscovering it.

**A note on row six, added after Trustoria.** `trustoria.com` returns four
`nsone.net` nameservers and nothing else — no A record, no MX. `curl` reports
exit code 0 bytes, which is the same thing it reports for a timeout, a TLS
failure and an aggressive bot block. Those four states look identical from the
fetch layer and only one of them means "give up", so **resolve before you
conclude**. A domain with NS and no A is registered and delegated but not
serving: somebody is still paying for the name and nothing is behind it. That is
`unreachable`, and unlike a bot block it will not come back with a better User-Agent.

The general rule: a failed fetch is a question, not an answer. `dig A`, `dig MX`
and `dig NS` cost nothing and turn four indistinguishable failures into four
distinguishable ones. §68's Tymax diagnosis needed the same three commands to
find a parking page behind live Outlook MX.

**Related:** §45, §46, §64, §68.

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
for anyone who does what the page invites them to do.

**What actually caused it — the company told me.** Having reported the broken
link in the letter, the operator replied the same morning:

> "Thanks for letting us know. We corrected the page, it was failed change in
> wordpress."

A botched WordPress edit. The visible text was updated and the link target was
not, which is the ordinary failure mode of editing a hyperlink's label without
editing its href.

### Correction: the year stamp was not a rotation signal

The original version of this section reasoned from the year in
`dataprivacy2026@` to a *policy* of annual rotation — a `dataprivacy2025@` now
retired, a `dataprivacy2027@` not yet created, and therefore an expiry date on
every address cached from a site like this. That was inference dressed as a
finding, and it was wrong. There is one mailbox, someone typed a year into it,
and a later edit broke the link around it.

The mechanism I invented was more interesting than the truth, which is exactly
why it should have been flagged as a guess. **A pattern that explains the
evidence is not thereby the cause of it.** The same visible symptom — href and
text disagreeing — is produced by a rotation, a botched edit, a stale cache, or
a copy-paste error, and nothing in the page distinguishes them. Reporting the
fault gets you the answer; theorising about it gets you a plausible story.

The practical advice survives the correction, for a duller reason: **record when
you verified an address, not just that you did**, because addresses go stale for
many reasons and none of them announce themselves.

**And report the fault in the letter.** This one was fixed within hours because
the request opened by describing the broken link plainly and without accusation.
That costs two sentences, it is useful to a small operator who cannot see their
own bounce log, and it visibly buys goodwill — the same reply answered every
substantive question asked.

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

---

## §69 The confirmation that names a record you do not recognise

Search Public Records answered a removal request with a clean, unambiguous
confirmation:

> "This email is to confirm that we have removed the public record information
> for [FIRST LAST] of [TOWN], ME, age [NN] from the search results of
> SearchPublicRecords.com."

(Name, town and age masked here; the repo is public. The shape is what matters:
they named a *specific* record, with a locality and an age.)

That is a broker-issued artifact. It names a person, a place, an age and a
site. By every rule in this repo it is the thing you have been asking brokers
for: not "we received your request", not "we are reviewing", but a past-tense
statement that a specific record is gone. It is the strongest class of evidence
a people-search site produces, and the temptation is to mark it `confirmed` and
move on.

**The age matched. The location did not.** The subject is 47. No address in the
request — sixteen of them, across three states and twenty-five years — is in
Maine, and the subject has never lived there.

So one of two things is true, and they have opposite consequences:

| | What happened | Consequence |
|---|---|---|
| **A** | They matched on name + age and hit a *different* person of the same name and age | A stranger's listing was suppressed. The subject's records are untouched and still live. |
| **B** | The record genuinely is the subject's, and their source data has the locality wrong | The removal worked, but the upstream source is feeding a wrong-locality record that will return on the next ingest. |

Under **A**, the confirmation is worse than no reply, because it closes the
ticket, closes the loop, and closes the file. The next verification sweep looks
for the subject's name on the site, and if the site's search is flaky or the
cache is warm it reads as removed. Under **B**, the removal is real but the
useful information is the source name, which the confirmation does not give.

Both readings share one instruction: **do not mark it confirmed.**

**The general rule.** A confirmation is evidence about the broker's *action*,
not about *whose record it acted on*. Those come apart whenever the subject has
a common name, and they come apart silently, because nothing in the workflow
compares the identifying details in the confirmation against the ones in the
request. Most confirmations do not name a record at all — "we have removed your
information from our database" identifies nobody — so the failure is invisible
by default. This one was catchable only because the broker was unusually
specific.

**Check to add.** When a confirmation names *any* identifying detail — a city,
an age, a middle initial, a former address, a relative — diff it against the
request. Treat a mismatch on locality as disqualifying and a match on age alone
as meaningless: age is a one-in-eighty coincidence, and for a common name in a
national database there are many people who match on name and age together.

**What to write back.** Ask for three things, and ask for the third one plainly
even though it works against the immediate goal:

1. Re-run the removal against the *addresses* supplied, not against a name-and-age
   match, and say how many records matched.
2. If the named record is not the subject's, **restore it.** Nobody asked for a
   stranger's listing to be taken down, and a privacy project that quietly
   accepts collateral suppression of third parties has stopped being a privacy
   project. This is the ask that costs nothing and is worth making every time.
3. If the record genuinely is the subject's with a wrong locality, name the
   source, so the error can be corrected upstream rather than hidden here.

**Why this is worth its own section.** Every other pattern in this file is a
broker doing less than it claimed. This is a broker doing *exactly* what it
claimed, competently and promptly, to the wrong person — and reporting success
to both of you. The tell is not in the language of the confirmation. It is in a
field the confirmation happened to include.

**Related:** §11, §40, §65, §70.

---

## §70 The ticket that closed without a reply, and the survey that proves it

Three sibling sites — publicinfoservices, publicdatacheck, publicrecordreports —
each acknowledged a request within minutes:

> "Your email has been received and is being reviewed by ... support staff."

Then, thirty hours later, from all three at once:

> "We'd love to hear what you think of our customer service. Please take a
> moment to answer one simple question ... How would you rate the support you
> received?"

Nothing in between. No outcome, no refusal, no request for more information.
The ticket went from Open to Solved and out the other side, and the only
evidence that anyone touched it is a satisfaction survey asking how the support
went.

**The survey is a real artifact, and it is the wrong one.** Zendesk fires CSAT
on transition to Solved, so its arrival is proof that a human (or a macro)
moved the ticket to Solved. It is proof of *closure*. It is not proof of
*removal*, and it does not distinguish between "we removed the records",
"we found nothing", and "we bulk-closed a queue". Those three outcomes produce
byte-identical mail to the requester.

This is the mirror image of §69. There, an artifact named a record and told you
something false. Here, an artifact confirms activity and tells you nothing at
all — while looking, in a status column, exactly like progress.

**The family tell, again.** The three ticket numbers were 3421272, 3421273 and
3421281, issued across three different Zendesk subdomains. Sequential IDs on
what are nominally three unrelated companies mean one shared queue, and one
queue means one bulk close (see §40 and the family-detection notes). It also
means the three follow-ups below are read by the same person, so send one
question, not three arguments.

**Update: a fourth survey arrived, and the counter turned into the answer.**
The next day quickpublicrecords closed its ticket the same way — #3421287, from
a fourth Zendesk subdomain. Four numbers, 3421272 / 3421273 / 3421281 / 3421287,
issued out of one sequence across four brands.

This is worth separating from the closure problem it arrived attached to,
because it is a *discovery* technique and it works on any Zendesk-hosted family.
Zendesk numbers tickets per account, not per brand or per help-centre subdomain.
So if two nominally unrelated companies hand you IDs a few apart on the same
day, they are one account. The evidence is unusually strong: not a shared host,
not a shared registrar, not a template — a shared monotonic counter, which
nothing but a common instance produces.

The useful part is that **the broker generates this evidence itself, in the
course of refusing to answer the question it settles.** I had asked all four
whether they shared an operator. None answered. All four then proved it by
sending automated mail. The nameserver evidence I opened with was suggestive;
this is close to conclusive.

**How to use it.** Put the four numbers in the reply, say plainly what they
imply, and then — this is the part that keeps it usable — ask only for the thing
that still isn't known. The operator question is settled; what remains is
whether one removal covered one index or four. Offering "they are four separate
indexes and you need four removals" as an equally acceptable answer keeps it a
question rather than an accusation. See the §52 correction for why that register
matters.

**Collect ticket IDs even when nothing is wrong.** They are cheap to record and
they cross-reference later. A number on its own means nothing; the fourth one is
what turned three into a sequence.

**Do not rate the survey.** Clicking a rating resolves the CSAT and gives the
desk a metric without giving you an answer. Rate nothing.

**What to do instead: reply into the ticket thread, not the survey.** Replying
to a Solved Zendesk ticket reopens it, which is the point. Reply to the
*acknowledgement* email — that is the ticket thread; the survey is a separate
notification and its reply path goes to a rating endpoint.

**What to say.** Make it cheaper to answer than to ignore, and make every
possible answer acceptable:

> I have just received a "how would you rate the support you received" survey
> for request #NNNN, which I take to mean the ticket has been closed. I never
> received a reply telling me what was done, so I have nothing to rate and
> nothing to record.
>
> I am not complaining about the closure. I would just like one line, and any of
> these is a complete answer as far as I am concerned:
> "Removed" / "We hold no record matching what you sent" / "We need something
> more from you".

Offering "we hold nothing" as a *complete and accepted* answer matters. A desk
that bulk-closes tickets does so because answering feels like work with a
downside; removing the downside is what makes the one-line reply happen.

**Status handling.** A CSAT survey does not move a broker to `confirmed`. It
does not move it to `failed` either — the ticket was worked, we simply do not
know how. Leave it `submitted`, record the survey and the ticket number in the
note, and let the reply or the next verification sweep decide.

**Related:** §11, §40, §69.

---

## §71 The rights page with no rights form on it

Terminus's privacy links redirect to demandscience.com, and
`terminus.com/privacy-rights/` returns 404. So the live route is
`demandscience.com/privacy-rights/`, a page whose `<title>` is
"California Consumer Privacy Act (CCPA)".

A scripted check of that page finds **three `<form>` elements**. By §62's test —
does a form exist and does it have handlers — the page passes. It is not
decorative, it is not an empty embed, the forms are real and they submit.

They are two copies of the site-search box and a newsletter signup.

```
form 0  .kb-search-form      action=demandscience.com/       [ s ]
form 1  .kb-search-form      action=demandscience.com/       [ s ]
form 2  #newsletter-subscribe action=b2bleadgen.demandscience.com/l/811663/...
```

**The rights mechanism is not a form on the page. It is one anchor:**

> Click here to submit a Data Subject Rights Request

pointing at a `portal.privacyengine.io` URL. One link, in body text, on a page
otherwise occupied by product marketing — the extracted page text runs through
"Ionic", "Labs", "VID", "Content-IQ", "AI Visibility Studio" twice before
reaching anything about privacy.

**Why this defeats the existing tests.** §62 asks whether a form exists. §63
asks whether a portal renders. Both are *presence* checks, and both are
satisfied here by forms that have nothing to do with rights. Counting forms is
not the same as finding the one that matters, and a page can be simultaneously
form-rich and rights-empty.

**The check to add.** After counting forms, classify them. A rights form has
some subset of: a request-type selector, a state-of-residence field, an
identity field beyond email, an attestation. A form whose only control is named
`s`, or whose action points at a marketing-automation host
(`b2bleadgen.`, `pardot`, `hs-sites`, `list-manage`), is not it. If no form
classifies, **then** sweep anchors and buttons for rights-shaped link text
before concluding anything:

```
[...document.querySelectorAll('a,button')]
  .filter(e => /click here|submit|request|exercise|rights|do not sell/i.test(e.innerText||''))
  .map(e => ({txt: e.innerText, href: e.getAttribute('href'), onclick: e.getAttribute('onclick')}))
```

Note this is the same sweep §62's companion test uses for the Ketch modal case,
run for the opposite reason. There the link had `href="javascript:void(0)"` and
opened a modal in place; here it is an ordinary `href` to a third-party host.
**Two failure modes, one probe** — which is the argument for running the anchor
sweep unconditionally rather than only after the form check fails.

**Also: an initial scrape for `trustarc` on this page hits.** It is the cookie
banner. The rights vendor is PrivacyEngine. Matching a vendor name anywhere in
the HTML tells you which consent tools the site loads, not which vendor handles
rights — resolve that from the link the rights text actually points at.

**Related:** §59, §62, §63, §68.

---

## §72 The privacy address that is a mailing list you are not a member of

`privacy@venpath.net` did not bounce 5.1.1. It bounced like this:

> "We're writing to let you know that the group you tried to contact (privacy)
> may not exist, or you may not have permission to post messages to the group."
>
> — signed `venpath.net admins`

That is Google Workspace rejecting a post to a **Group**, not a mail server
rejecting an unknown mailbox. The distinction matters because the two failures
have opposite meanings and identical consequences if you misread them:

| bounce | what it means | what to do |
|---|---|---|
| `550 5.1.1` unknown user | there is no such mailbox | find another address |
| Groups "may not exist, or you may not have permission to post" | there may well be a mailbox — but it is a distribution list closed to external senders | there is no address to find; the route is closed by policy |

The second one is a **configuration**, not an absence. Somebody set up a
`privacy` group, pointed the privacy policy at it, and left it restricted to
members of the domain. Every consumer who follows the published instructions is
rejected by design, and the rejection text blames the sender ("you might have
spelled the group name incorrectly").

Do not go hunting for `privacy1@`, `dataprivacy@` or `legal@` after this bounce.
Guessing local parts is the right move after a 5.1.1 on a *guessed* address
(§65, row one). It is the wrong move here, because the failure is not about
which name you used.

**The DNS makes the picture worse, and is worth checking every time:**

```
dig +short A  venpath.net   →  (nothing)
dig +short MX venpath.net   →  aspmx.l.google.com. and friends — live
```

**No website. Live mail.** The company's site is gone and its Workspace tenant
is still being paid for. This is the exact inverse of the Tymax case in §68,
where live MX sat in front of a "this website is for lease" parking page. Both
are the same underlying fact wearing different clothes: **infrastructure
outlives the business, and DNS keeps answering long after anyone is listening.**
A registry entry that records only "has a privacy address" cannot distinguish
either case from a healthy company.

**Recording it.** `unreachable`, with the bounce text and the DNS in the note.
Not `failed` — nothing was refused. Not `pending` — there is nothing left to
try. The evidence is what stops a later pass spending three sends rediscovering
a closed mailing list at a company with no website.

**Related:** §45, §65, §68, and `_DEFLECTIONS.md` §29 (when a privacy alias is a
distribution list — the same structure, seen from the inside).

---

## §73 The answer to the letter you superseded

Two messages went to the same mailbox, eleven hours apart, in one thread:

1. **18 Aug, 10:15** — the request. Four email addresses, name, DOB, current
   address, phone.
2. **18 Aug, 21:33** — a follow-up that widened it: cover both brands served by
   this mailbox, and search for records keyed to something *other* than a name —
   hashed email, mobile advertising identifier, cookie or CTV identifier,
   IP-derived household association — and delete the **edges**, not only the row
   carrying the name.

**Two days later the reply came back quoting message one.** Verbatim, in full,
with message two nowhere in it:

> "We have reviewed our systems, and the information you provided is not
> present. No further action is required at this time."

"The information you provided" is doing quiet, enormous work in that sentence.
It is true. It refers to four plaintext email addresses. It says nothing
whatsoever about hashed keys, device identifiers, or the sibling brand — because
the message that raised those was never the one being answered.

**Why this is a silent failure and not a brush-off.** Nobody ignored anything.
A support desk opens a ticket from the message that created it, works the fields
in that message, and replies. A follow-up arriving into the same thread lands as
a comment on an open ticket, and comments on open tickets are read far less
reliably than the ticket body — especially where the reply is composed in Outlook
from the original rather than from the thread tail. The requester sees a complete
answer in a thread containing both messages, and has no way to tell which one was
worked.

**The tell is in the quoted text.** Whatever a reply quotes underneath it is the
message that was actually answered. Check it every time. It costs a glance and it
is the only reliable signal available:

| what the reply quotes | what you learned |
|---|---|
| your most recent message | the full scope was in front of them |
| an earlier message in the thread | **the reply is scoped to that message only** |
| nothing | unknown — ask which identifiers were searched |

**Do not treat this as a refusal, and do not re-argue the finding.** The negative
they gave is honest for what they searched. If the original letter promised —
as it should have — that an unqualified "we hold nothing" would be accepted as a
complete answer, **honour that promise.** The technique of pre-accepting the
unflattering answer only works because it is kept; a project that pockets the
cheap answer and then argues anyway poisons the well for the next person.

**What to do instead: use the door they open.** Replies of this kind very often
end with an invitation, and this one did:

> "If you believe your data may exist under a different email address/company or
> spelling variation, please feel free to share it, and we will be happy to
> recheck."

Accepting an explicit invitation is not re-litigating a finding. Send the
identifiers the first letter omitted, and re-ask the scope questions **as
questions about how the check was run, not about whether it was right**:

> Does "not present in our systems" cover identifier-keyed records as well as
> contact records, or was the check a lookup on the addresses I gave? Either
> answer is fine and I will record it as given. I ask because the two produce the
> same sentence and mean different things.

That framing is the load-bearing part. It concedes the result, isolates the
mechanism, and offers both answers as acceptable — so answering costs the desk
nothing and refusing would be conspicuous.

**Status handling.** Not `not_found` yet. The negative is real but partial, and a
recheck is outstanding. Leave it `submitted`, record what the reply did and did
not cover, and flip when the recheck comes back.

**Prevention.** Do not send scope in a follow-up if it can go in the first
letter. A second message is not an amendment to the first — operationally it is
a lower-priority note attached to a ticket that has already been framed.

**Related:** §11, §40, §69, §70.

---

## §74 The privacy mailbox that the removal industry killed

SourceIT's privacy policy named `dataprivacy2026@` in its text and linked
`dataprivacy@` underneath it — §66, and the year-stamp turned out to be a
botched WordPress edit rather than the annual rotation I had inferred. But the
operator volunteered *why* the old address existed to be linked at all, and it
reframes a whole category of dead privacy mailboxes:

> "Hard part I built the portal for self service, probably was one of the
> earliest ones following CA CCPA, but some privacy removal sites would send
> tens of thousands of emails (sometimes with pdfs) to delist which would
> overload mail server, so retired the old email address which was originally
> just for CA Coppa."

Read that again from the consumer's side. A small broker set up a CCPA mailbox
early — earlier than it had to. Paid removal services then pointed automated
senders at it, tens of thousands of messages, some with PDF attachments, until
the mail server fell over. The broker retired the address and moved everything
to a self-service portal.

**So the dead mailbox was not neglect and not evasion. It was load-shedding.**

**Why this matters for diagnosis.** A hard bounce on a published privacy address
looks the same whoever caused it. Up to this point I had been reading dead
privacy mailboxes as one of three things: abandonment, a company that no longer
exists, or deliberate obstruction — a channel published for the look of it and
quietly unplugged. There is a fourth cause, and it is the opposite of the third:
*a channel that worked, was used at industrial volume by intermediaries acting
for consumers, and was closed under the weight of that*.

I cannot tell these apart from outside, and neither can anyone else. That is the
silent failure. But it changes what to do about it:

- **Do not open with an accusation about the dead address.** "Your published
  privacy contact bounces, which I assume is deliberate" is a bad opening and
  may well be false. Report it as a fault — see §66 — and let the reason come
  back on its own. It did here, unprompted, along with a same-morning fix.
- **Prefer the portal when one exists**, even though a portal is more work than
  an email. The operator's own reason for preferring it is legitimate: a form is
  authenticated-ish, structured, and rate-limitable, and it does not collapse
  under a vendor's send queue. A portal is not automatically a dark pattern.
- **Treat a "retired" address differently from an abandoned one.** If the policy
  text and the link disagree, one of them is usually the survivor of exactly
  this kind of migration. Try the one in the visible text, not the one in the
  href.

**The uncomfortable second-order point.** The bulk removal services doing this
are acting on behalf of consumers, and one of them may well be acting for the
person reading this. Their volume closed a working channel for everyone who
would rather write one careful letter. This is not an argument against those
services — most people have no other realistic route — but it is a reason for
individual requesters to behave unlike them: one message, addressed, specific,
no attachments, no retries on a timer. The channel you are using stays open
partly because few people use it the way a vendor would.

**What the operator actually wants.** Also unprompted:

> "I understand the burden for a user and would prefer a single site to
> unsubscribe from all."

Which is California's DELETE Act (SB 362) and its DROP platform — one consumer
submission, brokers registered in California pull the list on a cycle, and the
suppression is standing rather than point-in-time. Telling a cooperative broker
this is worth doing: it is the thing that ends the volume problem for them and
the letter-writing problem for everyone else, and a broker who does not know it
exists cannot opt into it early. Give something back to the ones who answer
properly. It costs a paragraph.

**Related:** §64, §65, §66, §68, §72.

---

## §75 Thirteen privacy addresses, none of them yours

LiveRamp's privacy pages publish, between them:

`privacy.ar@`, `privacy.be@`, `privacy.br@`, `privacy.de@`, `privacy.es@`,
`privacy.it@`, `privacy.nl@`, `privacy.no@`, `privacy.pl@`, `privacy.ro@`,
`privacy.se@`, `ukprivacy@`, and `cil@` (the French CNIL contact).

Thirteen addresses. Every one of them is a real, monitored privacy mailbox
staffed by people whose job is to answer exactly this kind of letter. Not one of
them is unqualified, and not one of them is the United States.

**Why this is a silent failure rather than an inconvenience.** A letter to
`privacy.ro@` is not bounced and is not refused. It arrives at a desk with no
authority over the requester's records, which forwards it, or closes it, or
answers about the wrong legal regime — and every one of those outcomes reads,
from the requester's inbox, as the same thing: nothing came back. The address
was published, the mail was delivered, the tracker says `submitted`. The failure
is invisible at both ends.

It also inverts the usual worry. The normal fear about a scraped address is that
it is stale or fake. Here every candidate is live and correct; the defect is
*jurisdictional scope*, which no reachability check can see. `dig`, an SMTP
probe and a delivery receipt all pass.

**How the tooling gets this wrong.** `verify_emails.py` ranks addresses by what
the local-part signals — `privacy` outranks `support` outranks `info`. Every one
of those thirteen contains `privacy` and ranks identically, so the pick fell to
set iteration order, and the first run proposed the Argentinian desk, the second
the German one, the third the UK one, on identical input. A ranking with a tie
it cannot break is a random choice wearing a justification.

**The fix, in two parts.**

1. *Break the tie toward the general address.* At equal rank, prefer the shorter
   local-part: `privacy@` beats `privacy.de@` beats `emea.privacy.dpo@`. The
   unqualified form is the general one almost by construction.
2. *Detect the case where there is no general address at all,* and say so rather
   than silently picking a country. Implemented as `region_of()`, which
   subtracts the intent tokens and asks whether what remains is a region:
   `ukprivacy` − `privacy` = `uk`; `americas.dpo` − `dpo` = `americas`; plain
   `privacy` leaves nothing. Subtracting beats pattern-matching here — a regex
   for a trailing country code reads `privacyadmin` as the Indian privacy desk.

When every rights-shaped address on a site carries a region and none matches the
requester's, the verdict is `DISCOVERED_REGIONAL`: the address is still recorded,
because a wrong desk beats no desk, but it is flagged rather than called
verified.

**What to do in the letter.** Name the problem in the first paragraph instead of
hoping. Being explicit converts a misroute into a routing request, which is
something a regional desk can actually action:

> I am writing to your [region] privacy contact because it is the only privacy
> address published on your site. I am a United States resident and my request
> is made under US state law, so I expect this is the wrong desk. If there is a
> US or global privacy contact, please forward this and tell me where it went —
> or reply with the address and I will write there directly.

**Do not read the absence as evasion.** A company with thirteen European privacy
contacts and no American one is far more likely to have built its privacy
function around GDPR, where naming a per-country contact is ordinary practice,
than to be hiding from CCPA. The correct inference is about org structure, not
motive. Ask for the routing.

**Status handling.** `submitted`, with the region recorded in the note. If the
regional desk forwards it, the reply comes from the right one and the note
becomes the audit trail for how it got there.

**Related:** §64, §65, §68, §72, §74.

---

## §76 A guessed domain, then an address scraped off it: two derivations, one confident wrong answer

`resolve_optery_domains.py` turns a broker slug into a domain by deriving
candidates and requiring each to resolve and to serve a page mentioning the
slug's distinctive words. `verify_emails.py` then reads an address off whatever
that domain serves. Each step is checked. Neither step can check the other, and
the second one launders the first one's mistake into something that looks
verified.

Two cases, both major background-screening companies:

**First Advantage.** Registry domain `firstadvantage.com`. It resolves, serves a
page, and passes every check — because it redirects to `erafirst.com`, **ERA
First Advantage Realty**, a real-estate brokerage with no connection to First
Advantage Corporation. The address sweep read that site and proposed
`support@moxiworks.com` — MoxiWorks, a real-estate software vendor — as First
Advantage's privacy contact. Two independent derivations, both internally valid,
producing a confident route to a company three steps removed from the target.
First Advantage Corporation is at `fadv.com`, which publishes nothing at all.

**HireRight.** Registry domain `hireright.io`. Live site, resolves, serves
pages, publishes `support@hireright.io`. The real HireRight LLC is
`hireright.com`, and it publishes eight addresses including
`hirerightprivacy@` and `dpo@`. The `.io` was never theirs.

**Why this is worse than a wasted send.** These letters carry a complete
identifier set: every prior address, every prior telephone number, a date of
birth, a dozen email addresses. Mailing that to a company that is not the broker
is a disclosure of personal data *caused by the removal effort*. It is the only
failure mode in this file that leaves the requester worse off than having done
nothing, and it arrives wearing an `email_verified: true` flag.

**The structural point.** A derived value used as the input to another
derivation needs a check that does not come from the same chain. Both scripts
verify their own step honestly; neither is positioned to notice that the thing
it was handed is wrong. Confidence multiplied along a chain does not survive the
first bad link, but the *appearance* of confidence does.

**The signal that catches most of it.** If a site publishes **no address on the
broker's own domain**, something is going on, and it is one of two things:

- an acquisition or rebrand, where the parent's privacy desk is the correct and
  frequently better route — CoreLogic → Cotality, Aberdeen → Spiceworks,
  FindLaw → Internet Brands, Intentgine → PharosIQ;
- a wrong domain, where the address belongs to a stranger — `datalead.io`
  serving `hello@fruits.co`, `firstadvantage.com` serving MoxiWorks.

These are indistinguishable from outside, so the verdict `DISCOVERED_OFFDOMAIN`
records the address (the acquisition case is common and the lead is worth
keeping) but never marks it verified, and `queue_batch.py` holds it out of the
send queue until a human confirms the corporate relationship. Nineteen addresses
from one sweep landed in that state.

**What must not be done here is quietly drop them.** A queue that silently
excludes work reads as "nothing left to do" — the same illusion that hid 304
routable brokers behind "0 brokers still to contact by email". The hold prints
the count and the ids every time it runs.

**A narrow exception, and only a narrow one.** Some off-domain addresses are
plainly the same company under a different legal or TLD form: `scribdinc.com`
publishing `privacy@scribd.com`, `salesintel.com` publishing
`support@salesintel.io`. `same_entity()` clears those by stripping corporate
noise words (`inc`, `group`, `holdings`, `media`) and comparing what is left.
It is deliberately unable to detect acquisitions — inferring a corporate
relationship from a name is exactly the kind of plausible reasoning §66 was
written about. A shared stem is evidence. A shared industry is not.

**Prevention.** Where a slug-derived domain and a curated domain disagree, the
curated one wins — that rule already exists. What was missing is the case where
there is no curated value at all and the derived one is simply wrong. The tell
is cheap to check by hand and expensive to miss: **follow the redirect and read
the company name.** `firstadvantage.com` announces itself as a realty firm in
the first line of its own homepage.

**Related:** §64, §65, §66, §75.

---

## §77 The identifier and the mailbox are the same field, so the record outlives the access to it

Growbots' opt-out form refuses public-domain addresses:

> *"we are not able to identify a person by public domain email addresses such as
> '@gmail.com' or '@yahoo.com'. For this reason please use your professional
> email here."*

Reasonable: a personal webmail address does not identify anyone in a B2B contact
database. Then, having been given the professional address, the form emails the
confirmation link **to that same address**. Also reasonable, taken alone.

Together they can only be satisfied by someone who still controls the mailbox
their record was built around. An institutional address that has since been
closed is simultaneously the only key that can find the record and the only
channel that can confirm the request. The opt-out submits, says something
reassuring, and is permanently unverifiable.

**The population this excludes is the population that most needs the form.** A
stale B2B record is stale *because* the role ended. The people with the strongest
reason to opt out — left the employer, left the university, changed careers — are
precisely the ones who can no longer receive mail at the address the broker
indexed them under. The form serves current employees, who are the least likely
to be looking for it.

Leadership Connect fails the same way from the other direction. Their opt-out
returned a negative scoped to a single personal address; the obvious next step
was to re-run it with the institutional one, since a leadership directory keys to
work identity. But their confirmation link also goes to whatever address is
typed, so a second address is only testable by someone who can read its mail.
The right key is unusable for the same reason it is the right key.

**The general shape.** Wherever a broker uses one field as *both* the record key
*and* the proof of reachability, everyone whose relationship to that identifier
has ended is locked out — and locked out silently, because the form's success
message is issued at submission, before the link is sent.

**Ask for them to be separated.** They do not have to be the same string, and
saying so is a one-line fix a support desk can act on:

> Key the suppression to the professional address, and send the confirmation to a
> separate contact address I nominate. The identifier and the proof of
> reachability do not have to be the same field.

**What to do meanwhile.** Take it to email and ask for manual completion. State
that the mailbox is closed and why, and ask them either to honour the submitted
request without the round trip or to re-issue the confirmation elsewhere. This is
one of the few situations where a support desk can straightforwardly help and has
no reason not to — nothing about it is adversarial, and the requester is not
asking for an exception to a rule, only for two rules to stop colliding.

**Operational rule that came out of this.** Before staging any form, establish
**where its confirmation goes**, not merely which address it searches. A dead
mailbox in the identifier list is harmless and useful — it is still a correct
identity assertion and the best join key for workforce and B2B datasets. A dead
mailbox in the *confirmation* field voids the request while every status
indicator on both sides reads `submitted`. Recorded in the profile notes so a
later pass cannot make the same substitution.

**Status handling.** Not `submitted`. The request does not exist until confirmed,
which is §1 of this file. Where a human could rescue it, it belongs in the
handoff queue; where no click can rescue it, take it off that queue entirely
rather than leaving a permanent no-op in a list of things a person is asked to
do.

**Related:** §1, §64, §75.

---

## §78 The corporate family is a sworn filing, and nobody reads it that way

Everything else in this project is inferred. Optery's list is a competitor's
research. Domains are derived from slugs. Contact addresses are scraped off
privacy pages. Sibling relationships are argued from shared nameservers and, in
§70, from a shared Zendesk counter.

California requires data brokers to register annually and to publish a primary
contact email address. That is not an inference — it is a legal filing with a
statutory contact, and it had never been imported here. Four files
(2020–2023 under the DOJ, then 2024, 2025 and 2026 under the CPPA) hold **942
distinct registrants**, of which **517 were entirely absent** from a registry
built from every other source combined. Every one of the new ones arrived with a
contact address already attached.

The provenance ranking that follows from this:

    ca_data_broker_registry  >  privacy_policy  >  derived_from_optery_slug

A scraped address is one somebody left on a page. A registry address is the one
the company nominated to receive exactly this kind of letter.

**But the list is the smaller half of what the registry is for.**

### Registrants grouped by contact address are corporate families

The sibling problem is hard from outside because nothing on four sites says they
share an index. Inside a filing, the family declares itself: the entities file
under **one contact address**.

> **BeenVerified, Inc.** registered with `privacy@moneybot5000.com`.

Nothing on either site connects them. I had been corresponding with MoneyBot5000
as an unrelated broker for days. The filing says otherwise, in a document signed
under penalty of perjury.

Grouping the 942 registrants by the domain of their contact address yields **99
families covering 226 filings**. Some are unsurprising once seen and impossible
to guess beforehand:

| Contact domain | Filings | What it turns out to be |
|---|---|---|
| `equifax.com` | 7 | Equifax, The Work Number, PayNet, Ansonia Credit Data, Austin Consolidated Holdings |
| `altrata.com` | 6 | Altrata, WealthEngine, Wealth-X, RelSci, BoardEx |
| `ignitevisibility.com` | 5 | EverConnect trading as 33 Mile Radius, Best Pick Reports, Keyword Connects, Remodeling.com, Five Star Rated |
| `alescodata.com` | 3 | Alesco Data, Response Solutions, Statlistics |

It also confirms, from the state's own records, the optOutLight family this
project worked out the hard way: `peoplesearcher.com`, `checksecrets.com`,
`weinform.org` and `privatereports.com` each file for several brands at once.

**This evidence is stronger than anything in §40 or §70.** A shared nameserver is
suggestive. A shared ticket counter is close to conclusive. A shared statutory
contact address in a sworn annual filing is the company saying so.

### The name field is a brand list

Registrants routinely put their whole portfolio in the name cell:

> *"Private Reports, Mugshot Look, Public Searcher"*
> *"Checksecrets, PeopleSearchUSA, inmate searcher, Sealed Records"*
> *"Alesco Data LLC; Response Solutions LLC; Statlistics"*

The website cell does it too — `weinform.org--www.truthrecord.org` is two sites
in one field. Splitting both surfaced **443 brand names that appear in no broker
list**.

**Those are leads, not brokers, and the distinction is load-bearing.** They are
written to `data/broker_leads.json` and go no further until each has a domain and
a contact address. Importing a name with no route would recreate exactly the
condition that left 304 registry entries unroutable while the queue reported
nothing left to do — see §76.

### Deregistration is a signal, not a deletion

A company that filed in 2024 and not in 2026 has been acquired, wound up, or
simply not filed — and the third case is the interesting one, because the
obligation did not lapse with the paperwork. So every year a registrant appears
in is recorded on the row, and nobody is dropped for being absent from the newest
file. A stale contact address is worth trying; an unexamined absence is worth
noticing.

### What is still unmined

California is the largest but not the only registry. **Vermont, Texas and Oregon**
also require registration and publish their lists, and the overlap is partial —
a broker with no California nexus can appear in Vermont and nowhere else. Same
importer, different column names.

**Related:** §40, §67, §70, §74, §76.

---

## §79 A verification link that works and tells you nothing

ROR Partners' OneTrust request needed an emailed confirmation click. Fetching the
link with a plain HTTP fetch returned a page whose entire readable content was
the words "Trust Center Portal" — no confirmation text, no error, no reference
number. Nothing to record and no way to tell whether the request had been
verified or not.

Opening the same link in a real browser showed a green tick and:

> *"Your request is confirmed! We will review your request and contact you
> shortly."*

**The portal is a JavaScript application.** The fetch retrieved the shell before
the app rendered anything into it. The verification very likely *did* fire on
that first fetch — the browser landed on `.../verify/verifySuccess/...` — but
that is an inference, and from the fetch result alone the two possibilities
(verified silently, or not verified at all) are indistinguishable.

**Why this is a silent failure and not merely an inconvenience.** §1 of this file
is that an unconfirmed request does not exist. The whole point of clicking the
link is to move a request from "does not exist" to "exists", and this is a class
of link where the tool used to click it **cannot report which state resulted**. A
pass that fetched the URL, saw no error, and marked the broker `submitted` would
be recording an outcome it never observed.

**Rule.** A verification link whose fetch returns no confirmation text is
**unverified**, not verified. Re-open it in a real browser and read the page
before recording anything. The cost is one browser tab; the cost of the
alternative is a request that silently never existed, discovered months later
when the listing is still there.

**Tell for this shape:** the fetched page has a title but effectively no body,
or the body is a bare product name. Any OneTrust, Ketch, DataGrail or similar
`my.<vendor>.com` portal path is a candidate.

**Related:** §1, §64.

---

## §80 One mailbox, several rows, and a second letter that undoes the first

Importing the state registrations added 517 brokers, and some of them are the
same company twice. "Alliant" and "Alliant Cooperative Data Solutions LLC" are
one business on one mailbox — `compliance@alliantdata.com` — which had **already
confirmed** a deletion under reference A6PP4DHC2W. The queue was about to write
to it again as a fresh first contact.

A sweep for rows sharing a contact address found **37 brokers queued behind an
address that already has an open thread**. Among them: `ansonia_credit_data` and
`austin_consolidated`, both behind `usprivacy@equifax.com`, which the Equifax
letter had *explicitly asked to treat as covering those entities*. Writing again
would have contradicted the letter already sent.

**Why a duplicate letter is worse than a wasted one.** It is not a free retry:

- To the desk it reads as either not having read their reply, or as pressure. The
  technique in `_DEFLECTIONS.md` — pre-accept the unflattering answer, make the
  honest one-line reply cheap — depends entirely on the sender appearing to read
  what comes back. A second identical request is the clearest possible signal
  that nobody did.
- It spends a slot from the daily cap on a broker already handled.
- Where the first thread produced a confirmation, the second reopens a settled
  matter and invites it to be re-decided.

**Fix.** `queue_batch.py` now skips any broker whose contact address already
belongs to a broker in a non-pending state, and prints what it held and why. The
earlier thread is the live one; a sibling discovered later should be raised
*inside* it — "your registration also lists X, does this cover them?" — rather
than opened as a new request.

### Two classes, and only one is a duplicate

The same sweep produced 77 name-stem matches, and most were not duplicates at
all:

| Pattern | Example | Treatment |
|---|---|---|
| One company, two rows | `alliant` / `alliant_cooperative_data_solutions` | **Duplicate.** One thread. |
| One operator, genuinely separate sites | 50+ `*courtrecords.us` state sites behind one contact | **Not duplicates.** Separate rows are correct; one letter, scoped to all. |
| Brand-list registration vs a tracked brand | `stirista` / the Stirista row naming 13 brands | **Not a duplicate.** The brand-list row is the *family* record — see `mississippi_tornado_alley.md`. |

**And a bug worth recording, because it is the kind that looks like a result.**
The stem matcher used raw substring containment, which made `kansas` a match for
`arkansas` and `virginia` a match for `westvirginia` — different states,
different sites, reported as the same company. A matcher whose false positives
are *plausible* is more dangerous than one that misses, because the output reads
as a finding. Compare §76: two honest derivations producing a confident wrong
answer.

**Related:** §40, §76, §78.


---

## §81 Six unrelated brokers, one redirect service, and a check that would have hidden them

§80 stopped the queue writing twice to one contact address. It did not stop the
other shape: **one company registered twice, under two domains and two contacts.**
`app_science` (appscience.inc, `privacy@appscience.inc`) and `appscience`
(appsci.io, `privacy@appsci.io`) share nothing matchable — and both redirect to
`www.appscience.ai`. A letter had already gone to the first when the second came
up in the queue.

So `find_duplicate_domains.py` resolves every registry domain and groups rows by
the host they actually land on after redirects. Across 1,369 domains it grouped
**96 rows**, and most were right: `alliant_cooperative_data_solutions` behind
`alliant`, `iqvia_digital` behind `iqvia`, four Deep Sync acquisitions behind
`deep_sync`, `terminus` behind `demandscience`.

**And it was wrong about ten of them, in the direction that costs the most.**

| Landing host | Rows grouped | What it actually was |
|---|---|---|
| `safebrowse.io` | 6 | A redirect service none of them owns |
| `accounts.google.com` | 2 | A sign-in wall |
| `audiense.com` | 2 | Unrelated landing |
| `gbg.com`, `kalibrate.com` | 2 | Parent-company sites |

Six unrelated brokers — forager.ai, malvern media, pickmedicare, reachdata,
ventiveiq and one more — were grouped because all six resolve to `safebrowse.io`.
Marked as duplicates, every one of them would have been **silently withheld from
the send queue**. That is the asymmetry to design around: **a duplicate letter is
embarrassing and visible; a suppressed one is invisible and permanent.** Nothing
in the tracker would ever have shown those six as skipped.

**The fix is a rule, not a blocklist.** Enumerating parking services and sign-in
walls only covers the ones already encountered. Instead the landing host must be
**claimed**: at least one member's own registry domain must be the host exactly,
or share its second-level label. `deepsync.com` groups four rows and is claimed
by `deep_sync`; `mtalley.zendesk.com` groups two and is one member's literal
domain; `safebrowse.io` is claimed by nobody, so the group is reported and
skipped rather than acted on.

**The rule deliberately errs toward sending.** It also rejected `gbg.com`
(GBG plc really did acquire both Acuant and IDology) and `kalibrate.com`. Those
are genuine relationships the guard now misses, and the consequence is at worst
two letters to one corporate group — which the recipient can say so about. That
trade is the right way round and was chosen deliberately, not conceded.

**83 rows now carry `duplicate_of`** and are held out of the queue, which fell
from 520 to 470. Nothing is deleted: a second registration is a real filing and
its contact may be the better route, so the row stays and points at the live
thread.

**General lesson.** A deduplication check is a suppression mechanism wearing a
tidiness costume. Before adding one, ask what happens when it fires wrongly — and
if the answer is "work silently disappears", it needs a positive test for
inclusion rather than a negative list of exclusions.

**Related:** §76, §78, §80.


---

## §82 The sample addresses on a marketing page

Scraping a broker's site for a contact address turns up whatever is on it, and on
a B2B vendor's site a lot of what is on it **is not a real address at all**.

Cloudlead's pages yielded five:

| Address | What it is |
|---|---|
| `support@cloudlead.co` | Published support address — **dead**, 550 5.1.1 |
| `support@cloudlead.io` | Published support address — **dead**, domain has no MX |
| `hello@cloudlead.co` | The only live candidate |
| `john@company.com` | A **placeholder** in a product screenshot |
| `r.richards@meridianops.com` | A **sample record** in a demo of their data |

The last two are the interesting ones. A company that sells contact data
demonstrates the product by showing contact data, so its marketing pages are
full of realistic-looking addresses at realistic-looking companies that belong
to nobody — or worse, to somebody uninvolved.

`verify_emails.py` already refuses to record a named individual's address as a
broker contact (`is_role_address`), and that rule caught both here: `john@` and
`r.richards@` are person-shaped, not role-shaped, so neither was ever proposed.
The rule was written to stop publishing a real person's work address in a public
registry. It turns out to catch demo data for the same reason — **both are cases
where the local-part is a human name rather than a function**, and neither is a
route to the company.

**Do not relax that rule to fill a gap.** When a broker publishes no role
address, the temptation is to take the person-shaped one that is there. That is
exactly when it is most likely to be a placeholder.

### The bounce is the more useful finding

`support@cloudlead.co` returned `550 5.1.1` in seconds, while the domain
publishes healthy Google MX records. Per §65 that pair means: **the domain is
fine, the mailbox is not there.** Not a dead company, not a policy rejection —
an address published on their own website that was never provisioned or has been
removed.

That is worth reporting to them as a fault, because unlike the requester they can
fix it, and every person who reads their site and writes to the address on it is
currently reaching nobody and never learning that.

**Operationally:** on a hard 5.1.1, do not mark the broker `unreachable`. Check
whether the *domain* has MX. If it does, there is a live mail system and the job
is to find the mailbox that exists — `hello@`, `info@`, `privacy@`, or a named
contact from a state registration filing. `unreachable` is only for a domain with
nowhere to deliver at all.

**Related:** §64, §65, §74.


---

## §83 The registered contact that is not a privacy contact

Altair Data Resources declined a request sent to the address **named in their own
California data broker registration**:

> *"This email address is intended solely for direct business communications and
> is not monitored for opt-out or privacy-related requests. As such, we are
> unable to process your submission because it was not submitted through one of
> our authorized request channels."*

They cited CCPA Regulations §999.312(e)(2) and directed the request to a Jira
Service Management portal, which turned out to be a proper one with separate
forms for individuals, authorised agents, corrections and access.

**The regulation citation is roughly fair.** That provision lets a business
either treat an off-channel request as validly submitted *or* direct the
requester to the correct method — it does not permit simply refusing. They took
the second option, which is what the rule contemplates. Do not argue this point;
it is a losing argument and it spends credibility.

**But the underlying fact is worth recording**, because it undermines an
assumption running through `_FAMILIES.md` and the whole registry import: **the
statutory contact address is not necessarily a privacy contact.**

The state registration exists so consumers can find where to send exactly this
kind of request. A registrant naming a business-development or sales mailbox —
one it will later say is "not monitored for privacy-related requests" — has
satisfied the form while defeating its purpose. Every consumer who does the
correct thing, looks up the registration, and writes to the address in it, gets
turned away.

### What this changes operationally

- **A registry-sourced address is a strong lead, not a guaranteed route.** It
  still outranks a scraped address, because a company nominated it under a legal
  obligation. But `email_verified_by: ca_data_broker_registry` should not be read
  as "this address accepts privacy mail".
- **Expect the redirect and do not treat it as a refusal.** Status is
  `manual_required` or `submitted` depending on what the redirect leads to —
  never `failed`. Altair's portal is better than their email would have been.
- **Say in the letter that you used the registered contact**, as these letters
  already do: *"I am writing to the contact nominated in your California data
  broker registration; if privacy requests are handled by someone else, I would
  be grateful if you would forward this rather than return it."* It costs a
  sentence, it makes the redirect polite rather than adversarial, and where a
  company *does* forward internally it saves a full round trip. Altair's reply
  came from a different person than the one addressed, so an internal forward did
  happen even though the outcome was a redirect.

### The related trap: pick the right form

Altair's portal offers five forms, and the second one in the list is
**Authorized Agent**. That is not the consumer's form. Submitting on your own
behalf through an agent form is a false statement about the capacity in which
you are acting, and the individual form contains an explicit affirmation that you
are *not* acting as an agent. Read the list before clicking; the ordering is not
a guide.

**Related:** §71, §78; `_DEFLECTIONS.md` §45, §46.


---

## §84 The per-record form that trips its own bot protection

Sync.me's removal form takes **one telephone number at a time**. This requester
has twelve, so a complete removal means twelve submissions of the same name and
email with a different number in one field.

Three went through. On the fourth, Cloudflare escalated from a passive check to
an interactive *"Verify you are human"* challenge.

**Nothing malfunctioned.** Three near-identical submissions in a few minutes look
automated to a bot detector — because structurally they *are* the same request
repeated, which is exactly what the form's design requires. The honest way to use
it is the thing that trips it.

**The people this excludes are the people who need it most.** A caller-ID
directory's stale entries cluster on numbers someone stopped using years ago. So
the requester with the most entries to remove is the one with the most numbers,
and therefore the one most likely to be stopped partway through and left with a
partial removal they cannot see the shape of.

### What to do

1. **Stop at the challenge.** Do not solve it — hard rule — and do not slow down
   and retry to sneak under the threshold. That is working around an anti-bot
   control, which is the same act however gently it is done.
2. **Count what landed.** Three submitted, nine not. A partial removal recorded
   as complete is worse than no removal, because it stops anyone looking again.
3. **Send the remainder by email, and say why.** The bounce back to email is not
   a failure — it reaches a human who can process all nine at once, and it
   carries the questions no per-number form can express.
4. **Report the design honestly, as a user rather than a complainant.** A single
   multi-number field, or an "add another number" control, fixes it completely
   and *reduces* their abuse-detection load. That framing gets read; an
   accusation does not.

### The general pattern

**A form scoped to one identifier plus rate-based bot protection equals a cap on
how much of yourself you can remove.** Neither component is objectionable alone.
The interaction is, and nobody designed it — which is why it is worth telling
them rather than routing around it.

Watch for this wherever a removal form takes a single email, phone number or
address and the subject has many: per-number opt-outs at caller-ID and
reverse-lookup sites, per-address forms at property data brokers, per-email forms
at list businesses.

### The same shape at a postal broker, and it is worse there

Altair's removal form has **one address field**. Their completion notice then
says, accurately:

> *"Data removed is specific to the name and mailing address provided... An
> additional request must be submitted if the name and/or address changes."*

So a form submission covers **one address out of sixteen** — and the fifteen
omitted are the ones that matter most. A consumer marketing file is built largely
from addresses a person no longer lives at, and a change-of-address append is
precisely the mechanism by which an old record follows someone to a new house.

This is more dangerous than the Sync.me case because **the confirmation is
correct**. Nothing in it is misleading; the scope limitation is stated outright.
A requester who skims it reads "Completed" and stops, having cleared a sixteenth
of the surface. §40's scoped-confirmation problem, arriving through a form field
rather than a hostname.

**Ask once in the ticket rather than submitting fifteen more forms.** Jira
Service Management tickets accept email replies, so the prior addresses can go
back on the same thread — one request instead of sixteen, and it avoids the
rate-based bot problem above entirely.

**Related:** §1, §40, §77; `_DEFLECTIONS.md` §45.


---

## §85 The registered contact that answers "this inbox is not monitored"

§83 covered a company declining a request sent to its own registered contact and
**directing the requester elsewhere**. This is the version with no elsewhere.

Experian's California data broker registrations nominate `ca_drop_fsd@` for
Experian Information Solutions and `ca_drop_audigent@` for Predictive Pop
(Audigent). A request to the second auto-replied:

> *"This inbox is not monitored and cannot process or respond to requests.
> Messages sent to this inbox will not be reviewed or fulfilled."*

No alternative address. No portal. Nothing.

The first had received a full request three days earlier and produced no reply of
any kind — almost certainly the same condition, silently.

### The likely innocent explanation, which should be stated first

The `ca_drop_` prefix suggests these mailboxes exist to receive **batch deletion
lists from California's DROP platform** under the DELETE Act, not individual
consumer mail. If so they are working exactly as designed for their actual
purpose, and nobody did anything wrong in operating them that way.

**Say that in the letter.** It is probably true, it costs nothing, and a fault
report that begins by conceding the benign reading is far likelier to be acted on
than one that begins by alleging obstruction.

### Why it is still a real failure

The registration field is the **published consumer contact**. A person who does
the diligent thing — looks the company up in the state's own registry rather than
guessing — is routed to an address that announces it will not act, and is given
nowhere else to go. The more correctly the consumer behaves, the worse the
outcome.

And the silent variant is worse than the auto-replying one. `ca_drop_audigent@`
at least *told* me. `ca_drop_fsd@` simply consumed a complete request and said
nothing, and the tracker read `submitted` for three days.

### What to do

1. **Find a live address on the company's own site** and resend there. Experian
   publishes `optout@experian.com`; that is where both requests went.
2. **Write one letter covering both entities**, quoting the auto-reply verbatim
   and asking for three things: route the stalled request, give the correct
   channel, and consider whether the registration or the auto-reply should be
   changed. The third is the one only they can do — *"a single added sentence,
   'for individual consumer requests please use X', would resolve it entirely."*
3. **Restate the substance briefly** so nothing is lost in the routing. A
   forwarded complaint about a mailbox is easy to close; a forwarded complaint
   that still contains the actual request is not.
4. **Do not mark the broker `unreachable`.** The company is plainly reachable —
   one specific mailbox is not a channel. Status stays `submitted` against the
   new address.

### The registry consequence

`email_verified_by: ca_data_broker_registry` has been the strongest provenance in
this project, on the reasoning that a company nominated the address under a legal
obligation. Between this and §83, that needs qualifying: **a registered contact is
a legally nominated address, not a demonstrated working consumer channel.** Both
affected rows now carry `registry_verified_unmonitored` and point at the live
address instead.

### What to do when the filed contact is a person, not a desk

A large share of registry filings publish an individual's work address — a named
employee, a `dev@`, an `admin@`. Writing to one of those is not wrong; it is the
only contact the company has published, and off-channel submission is
contemplated by CCPA Reg §999.312(e)(2). But the letter arrives in the inbox of
someone who did not expect it and may have no idea what to do with it, and the
cheapest thing for them to do is nothing.

Opening the letter by saying **where the address came from and what you want done
if it is the wrong desk** costs three sentences and removes that excuse:

> *"I have used this address because it is the contact your company published in
> its data broker registration filing; if it is not the right desk, I would be
> grateful if you would forward this internally rather than discard it, and tell
> me where to write in future. If the filing is out of date, correcting it would
> spare the next person this step."*

It does three things at once: it explains an otherwise baffling email, it names
forwarding as the expected action rather than leaving the recipient to invent
one, and it asks for a correction that benefits everyone who writes after you.
The last clause matters — a stale filing is a defect the company can fix once,
and the person reading your email is often exactly the person who filed it.

**Related:** §83, §85.

### The good version of the same thing

Blackbaud's registered contact also refuses requests, but the refusal is
everything Experian's was not:

> *"This email address is intended for the handling of questions and complaints
> regarding Blackbaud's privacy practices and is not a mechanism for the
> submission of privacy rights requests... Your email to this inbox will not be
> considered a valid submission of a privacy rights request, and the recipients
> of emails to this address do not have the ability to action any such
> requests."*

It **names the limitation precisely**, says plainly that the request has not been
received, and **gives a working destination**. Nobody is left believing a request
is in flight when it is not.

That is the whole difference. Both mailboxes decline; one tells you and points
onward, the other consumes the letter or says only that it will not be read. When
reporting this class of fault to a company, Blackbaud's autoreply is the model to
point at — a single added sentence naming the real route converts a dead end into
a redirect.

**Also read such a page for what it does *not* restrict.** Blackbaud's form page
says fulfilment of **correction and access** is limited to states with a
comprehensive privacy law. It says no such thing about **deletion or opt-out of
sale** — so those are the two to ask for from a state without one. The scope of a
stated limitation is itself information.

**Related:** §64, §65, §78, §83; `_DEFLECTIONS.md` §45, §46.


---

## §86 A registered address is only as good as the typing

B.I Science (2009) Ltd registered `dpo@bisceince.com` with California. Their
actual domain is `biscience.com` — the `e` and `i` are transposed. The registered
domain publishes **no MX and no A record**; the real one runs Microsoft 365.

Nothing in the existing tooling caught it, and it is worth being precise about
why. The address is well-formed. The local-part `dpo@` is a near-perfect privacy
contact. The provenance is `ca_data_broker_registry`, which this project ranks as
the strongest signal it has. **Every quality check passed except the only one that
mattered: can anything be delivered there?**

§83 and §85 already qualified registry provenance — a nominated contact may be
the wrong desk, or an unmonitored batch mailbox. This adds the dumbest failure of
the three and possibly the most common: **the filing has a typo in it.** These
forms are typed by hand once a year.

### What makes it invisible

A domain with no mail records does not bounce immediately. The sending MTA cannot
distinguish "this zone does not exist" from "the far end is briefly down", so it
reports a **temporary delay** and retries for roughly 48 hours before the final
failure. For two days the tracker reads `submitted` and the inbox shows a
reassuring "Gmail will retry" notice. Same mechanism as §65, arriving through a
typo rather than a lapsed registration.

### The check, and what it found

`check_email_domains.py` asks the crude question before the clever one: does the
contact domain have an MX, or failing that an A record? One DNS lookup per
broker, 959 distinct domains, and it surfaced **15 undeliverable contact
addresses**.

Five were repairable typos where the broker's own domain was live:

| Registered | Actual |
|---|---|
| `dpo@bisceince.com` | `biscience.com` |
| `hello@adttrbution.com` | `adttribution.com` |
| `chad@idengine.ai` | `idengine.com` |
| `contact@join5x5.com` | `5x5data.com` / `5x5coop.com` |

The other ten had a dead contact domain **and** a dead company domain — no route
by mail at all. Those were marked `unreachable` without ever being written to,
which is the point: the check runs before the send, not after two days of silent
retries.

### The third verdict: a website with no mail server

A domain with **no MX but a live A record** is a distinct case, and folding it
into either answer is wrong.

RFC 5321 says a sender falls back to the A record when no MX exists, so such a
domain is not *formally* undeliverable. But in practice a company that runs a
website and no mail server has nothing listening on port 25 — and the sender does
not learn that quickly. It reports a **delivery delay** and retries for two days
first.

Observed exactly that way:

| Domain | What happened |
|---|---|
| `structure.ac` | Three days of delay notices, then a hard failure |
| `4-eyes.ai` | Two days of "Gmail will retry", then failure |
| `calibrant.com` | Site serving normally, no MX, delay notice |

So the checker reports these as **weak** rather than resolving them either way,
and does not rewrite them. The two possible errors are asymmetric: calling such a
domain deliverable wastes a send and two days of a false `submitted`, while
calling it dead could write off a broker whose mail genuinely does arrive via the
A record. Neither is cheap enough to guess at, so the tool surfaces the list and
stops.

**Eight addresses in the registry are currently in this state.** Verify before
spending a send — a single SMTP probe, or simply watching whether the first
letter delays, settles it.

### The rules that fall out

- **Check deliverability before spending a send.** It costs one DNS lookup and it
  is the cheapest check in the project.
- **Only suggest the broker's own domain if that domain can take mail.** Rewriting
  onto a second dead domain achieves nothing and looks like progress.
- **Never condemn on a failed lookup.** The checker returns `None` when `dig`
  itself fails, and those rows are skipped rather than marked dead — guessing
  "dead" is the expensive direction of this error.
- **Report the typo to the broker.** They can amend the filing; a consumer
  cannot. And the sentence that lands is not the complaint but the consequence:
  *every person who looks you up in the state registry reaches nobody, and does
  not find out for two days.*

**Related:** §64, §65, §83, §85.


---

## §87 The addresses that matched were the ones nobody would think to send

BDEX ran a twelve-address list and reported back:

> *"4 of 12 emails have associated BDEX data. Found: [gateway.net address],
> [hotmail variant], [iwon.com address], [att.net address]."*

**All four are dead.** `gateway.net` and `iwon.com` are long-defunct consumer
ISPs; the other two are abandoned webmail accounts. **Not one currently-used
address matched.**

This project has argued from the start that a request should list every
identifier a person has ever had. That was reasoning from how the industry works.
This is the first case where a broker ran the full list and reported per-address
results, and the argument turns out to be not merely right but *the whole thing*:

**A consumer who submits only their current email address gets a truthful "no
record found", and every record stays exactly where it is.**

### Why the dead ones are the ones that match

A marketing or identity record is created at the moment data is acquired, and it
keeps whatever identifiers were current then. Nobody goes back and refreshes a
2009 record with a 2026 address. So the older and more abandoned an identifier
is, the more likely it is to be the key on a record that still exists — and the
less likely the person is to think of it as theirs.

Defunct-ISP addresses are the extreme case: `gateway.net`, `iwon.com`,
`webtv.net`, `aol.com`, `juno.com`, `netzero.net`, `earthlink.net`. The provider
is gone, the mailbox is unreachable, and the string is still a live join key in
somebody's database.

### What follows operationally

- **Never let a requester trim the identifier list for brevity.** The instinct is
  to send the two addresses currently in use. That is the one selection
  guaranteed to miss.
- **A dead mailbox is a search key, not a contact address**, and the letter must
  say which — see §77. "Please search this, do not reply to it" is the whole
  distinction and it takes one sentence.
- **A null result on a short list is not evidence of anything.** When a broker
  reports nothing found, check what they were given before recording
  `not_found`. Several early letters in this project carried only four addresses;
  those negatives are weaker than the ones that followed.
- **Ask for per-identifier results.** "4 of 12, here they are" is checkable.
  "No records found" is not, and the two can describe the same search.

### Worth telling the broker

BDEX prompts for a single email address on its opt-out. Saying so is free and
lands as help rather than criticism:

> If BDEX ever wants to make its opt-out more effective without doing more work,
> prompting for prior addresses would do it.

**Related:** §51, §53, §77.

## §88 — The filing names a person, and the person has left

`lzepeda@agrgroupinc.com` bounced: *address not found*. So did
`privacy@bvdinfo.com`: `550 5.1.1`.

Both domains are perfectly healthy. `agrgroupinc.com` has valid Microsoft 365 MX
records. `bvdinfo.com` has valid Proofpoint MX records and an A record and a
working website. Every domain-level deliverability check we run passes on both.
The **mailbox** is what is dead, and nothing short of sending a message reveals
that.

This is a different failure from §86 (a typo in the filing) and from §85 (a
mailbox that answers to say it is not monitored). Here the filing was correct
when it was made and has since rotted, quietly, in a way no one is responsible
for noticing:

- the company registered as a data broker and gave a real contact;
- the contact was an **individual's work address**, not a role mailbox;
- that individual left, or the acquisition closed, and the mailbox was deleted;
- the filing was never amended;
- the domain still resolves, so the address still *looks* fine.

**How much of the corpus is exposed to this.** Of 1,180 brokers for which we hold
a contact address, **195 (17%) have a person-shaped local-part** — a
`first.last@`, an `flast@`, a bare given name. **181 of those 195 came straight
from the California registry filings.** Every one of them is a letter that will
be delivered to a specific human being's inbox for as long as that person works
there, and will bounce, silently and without recourse, the day after they leave.

### What follows from it

1. **A green deliverability check is not evidence the address works.**
   `check_email_domains.py` verifies domains and cannot do better; mailbox
   existence is not observable without sending. Do not let a clean domain report
   create false confidence about a person-addressed contact.
2. **A bounce on a person-shaped address is a lead, not a dead end.** The company
   is usually still there. Look for a role mailbox, a privacy page, or — see §89
   — a parent that now runs the domain's mail.
3. **Say where you got the address.** The three-sentence opener recorded under
   §83 asks the recipient to correct a stale filing. The person who reads it is
   frequently the person who filed it.
4. **Registries should require a role address.** A filing regime that accepts an
   individual's mailbox as the sole public contact is guaranteed to decay. Worth
   saying to a regulator; nothing a consumer can do about it directly.

**Related:** §83, §85, §86, §89.

## §89 — The mailbox is dead because the company was bought

`privacy@bvdinfo.com` bounced. Bureau van Dijk is a registered data broker with a
live website and a live product, so the bounce was surprising rather than
explanatory — until the MX records answered it:

```
bvdinfo.com   MX -> mxa-00520701.gslb.pphosted.com
moodys.com    MX -> mxa-00520701.gslb.pphosted.com
reis.com      MX -> mxa-00520701.gslb.pphosted.com
```

`00520701` is a **Proofpoint tenant identifier**. It is issued to one customer.
Three brand domains resolving to it is not a coincidence of vendor choice the way
"they both use Google Workspace" would be — it means one organisation runs the
mail for all three. Bureau van Dijk and Reis are Moody's. The BvD privacy mailbox
was decommissioned after the acquisition and the registry filing was never
updated.

So the bounce was not a dead end. It relocated the request: one letter went to
`privacy@moodys.com` naming all five registered entities in the group, explaining
where the relationship came from, and asking them to fix the stale filing.

### Mail-tenant fingerprinting as a family detector

`family_scan.py` groups brokers whose contact addresses share a **domain**. That
catches the obvious cases and misses the interesting one: a company that was
acquired, kept its own brand domain, and had its mail quietly re-pointed at the
parent. Different domain, different branding, different registry filing —
identical mail tenant.

`mx_family_scan.py` is the new pass. Across all 960 contact domains it returns
**two confirmed groups**, and the second one is why the method is trustworthy:

| tenant | domains | brokers |
|---|---|---|
| `proofpoint:00520701` | bvdinfo.com, moodys.com, reis.com | Bureau van Dijk, Moody's, Moody's Analytics, Reis, Acquire Media |
| `proofpoint:00143702` | beeswax.com, freewheel.com | Beeswax, FreeWheel |

**The second row is a control.** We already knew Beeswax is FreeWheel — but only
because a letter to Beeswax produced an acknowledgement from FreeWheel's Zendesk,
a company we had never written to (`_FAMILIES.md`, appendix five). That took a
sent letter and a lucky reply. The MX scan rediscovers the same fact from public
DNS, before writing to anyone. A method that independently reproduces a
known-true finding is worth keeping.

### Precision cost this nearly had

The first run of the scanner reported **twenty-odd** groups, and most were
garbage: SendGrid inbound, MailChannels, Zendesk pods, Mimecast's shared inbound
pool, a Network Solutions reseller, Trellix's shared filtering cloud. It cheerfully
declared Altrata and GBG one company because both use Mimecast.

Every one of those false positives was *plausible*, which is exactly the failure
mode the duplicate-domain sweep already taught us — that sweep grouped six
unrelated brokers because their opt-out pages all redirected through one
interstitial. So the scanner now reports two tiers and will not merge them:

- **CONFIRMED** — a provider-issued tenant identifier that is unique to one
  customer.
- **WEAK** — two domains merely sharing a mail host. Reported, never acted on
  alone. Both remaining weak groups are Google Workspace and Amazon SES, i.e.
  half the internet.

Yield is low: 2 groups from 960 domains. But it costs one DNS lookup per domain,
asks no one for anything, and works precisely on the acquisition case that every
other method misses.

**Related:** §78, §80, §88; `_FAMILIES.md`.

## §90 — The LinkedIn URL is the suppression key you can actually supply

This is the most useful thing found so far for the re-scrape problem, and it
arrived unprompted, inside a refusal.

DemandScience declined the request on B2B grounds — and then offered this:

> *"If you believe we may hold a professional profile for you under a corporate
> email address, wish to suppress a specific business domain, or would like us to
> **suppress your public LinkedIn profile URL**, please reply with those business
> details so we can add them to our internal suppression list."*

Take that offer every time it appears, and ask for it where it does not.

### Why it solves a problem nothing else does

A public LinkedIn profile is re-scraped continuously by dozens of B2B brokers.
Every deletion won from one of them is undone at the next crawl, silently, and the
person has no way of knowing. Deletion without a durable key against the *source*
is a treadmill.

The LinkedIn URL is the only identifier in this whole exercise that has all four
of the properties you need:

| property | LinkedIn URL | MAID / device ID | internal record key | email address |
|---|---|---|---|---|
| the consumer can supply it | **yes** | no | no | yes |
| stable over time | **yes** | no (resettable) | unknown | changes with jobs |
| it is the actual collection input | **yes** | sometimes | n/a | usually derived *from* it |
| verifiable by both sides | **yes** | no | no | partly |

Compare it to the MAID demand (`_DEFLECTIONS.md` §54): that asks for an identifier
the subject structurally cannot produce. The LinkedIn URL is its exact opposite —
an identifier the subject can produce trivially, which sits *upstream* of the
derived data rather than downstream of it.

**And it reaches records you could never name.** Kaspr admitted its held address
was *"generated by our own internal tool based on your work experience"*. A
suppression keyed to the profile URL catches whatever was derived from that
profile, including `first.last@employer` constructions the person has never owned
and could not have guessed. You cannot list what you do not know exists. You can
hand over the input it was made from.

### How to ask for it

Two qualifications, both worth stating explicitly, because a suppression entry
can be implemented in ways that do nothing:

1. **Durable and forward-looking** — applied against future *ingestion*, not only
   against the current database. Otherwise a re-crawl re-creates the record and
   the suppression was cosmetic.
2. **Exclude-only, never a match key.** Same question as the hashed email: the
   URL held to keep you out is a protection, the URL held to recognise you in an
   incoming feed is inventory. Ask which list it sits on. Do not object to it
   being retained — object to not being told.

Then ask the diagnostic question the offer invites: **do you construct or infer
business email addresses from name and employer, or only ingest collected ones?**
A plain yes or no is a complete answer, and either one is useful.

### Generalise it

Do not wait to be offered this. **Add the LinkedIn URL and an explicit
suppress-on-this-URL request to every B2B, recruiting, sales-intelligence and
professional-data letter.** It costs one line, it is the identifier those
businesses are actually keyed to, and it is the only lever that acts on the
re-scrape rather than on one downstream copy.

**Related:** §87; `_DEFLECTIONS.md` §54; the B2B prospecting and
recruiting/talent entries in `_CATEGORY_VARIANTS.md`.

## §91 — The checkable denial

Circana's reply is the best-shaped denial received in this project, and the shape
is worth copying into any request for a *good* answer:

> *"Circana generally doesn't have personal data. These are the cases in which
> Circana could have your personal data: 1. You used one of Circana's mobile apps,
> ReceiptPal or CoinOut; 2. You participated in a Circana-run consumer panel;
> 3. You signed up for a Circana email newsletter; 4. You were a Circana employee;
> or 5. You applied for a job with Circana. If you fall into 1 or more of the
> above, then I'm happy to help. If you don't fall into any of the above cases,
> then your request is complete."*

Contrast with a bare "no records found". That is **unfalsifiable** — the consumer
cannot tell a genuine null from a search run against the wrong key, and
`_SILENT_FAILURES.md` §87 shows how often the search *was* run against the wrong
key. An enumerated denial is **checkable**: it hands the determination back to the
person who actually knows the answer, and it can be audited against memory rather
than taken on faith.

It is also cheap for the company. Five bullet points, written once, resolve most
requests without a database lookup at all.

**But check what the enumeration leaves out**, because a list of direct
relationships is not the same as a list of data holdings. All five of Circana's
cases involve the consumer dealing with Circana. The registered-data-broker
business is about purchase data obtained from *retailers*, resolved to households
— a category in which the consumer has no relationship with Circana at all and
would appear in none of the five. Similarly, "a Circana-run consumer panel" may or
may not include panels run by IRI or NPD before the merger.

So the follow-up is short and specific: accept the enumeration, confirm you fall
outside it, and ask the two questions the enumeration does not answer. **Naming
the gap precisely is what distinguishes a useful follow-up from an argumentative
one** — and a company that answered this well the first time will usually answer a
precise second question too.

## §92 — A null MX is an MX record that means the opposite

`privacy@crawlbee.com` bounced. The domain looked healthy — it served an A record
and a website — and our own checker had passed it as deliverable. The MX lookup
explained it:

```
crawlbee.com   MX -> 0 .
```

That is a **null MX** (RFC 7505): a single record, priority 0, pointing at the
root. It is the domain owner stating explicitly, in DNS, **"this domain accepts no
mail."**

`check_email_domains.py` returned `True` for it, because the logic was *"is there
an MX record? then mail can be delivered."* For every domain but this one that is
right. Here it is exactly backwards — the presence of the record is the refusal.

### Why this bug mattered more than a wasted send

A wasted letter is cheap. The real cost is that the broker gets marked
**`submitted`**, and a `submitted` row is a claim that a request is in flight.
Nobody ever learns the letter did not leave. That is the same class of harm as
§85 and §88: **a record that looks like progress and is not.** The tooling was
manufacturing exactly the failure this repository exists to document.

### The sweep

Fixed, then run across all 960 contact domains. **Two** null-MX domains:

| domain | broker | how found |
|---|---|---|
| `crawlbee.com` | crawlbee | bounced — the letter was already wasted |
| `idengine.com` | idengine | the sweep — no letter sent |

Two is a small number, and that is worth saying plainly rather than dressing the
finding up. The fix is still right: the failure is silent, so its rate is not what
determines whether it is worth catching.

### A correction to earlier work

`idengine.com` was one of the five "repairable typos" I fixed in the earlier
domain sweep, changing `idengine.ai` to `idengine.com` because the `.ai` domain
did not resolve. The correction looked obviously right — and it pointed the
address at a domain that refuses all mail.

Recorded rather than quietly amended, because **a correction that produces a dead
target is indistinguishable from one that worked** unless somebody checks. The
same instinct that made the typo fix feel safe is what would have kept it
unexamined.

### And the queue now checks at send time

`arrakis.ai` was NXDOMAIN — no MX, no A, no SOA — and our checker said so
correctly. It was queued and sent to anyway, because **nothing consulted the
checker at the moment of sending**. A domain that died after the last sweep is
indistinguishable from one that was never swept.

`queue_batch.py` now runs `deliverable()` over each batch on the way out and holds
anything that comes back `False`, printing what it held. Only the batch is
checked, so it stays a handful of DNS lookups. A lookup *failure* is still treated
as sendable, deliberately: condemning a broker on a transient resolver error is
the expensive direction of that mistake.

**Related:** §85, §86, §88, §89.

## §93 — The tracker was able to erase its own best results

While recording outcomes from the inbox, I set MyLife to `submitted` on the
strength of a newly acknowledged ticket. MyLife had been **`confirmed`** since 18
August — they had written that the account and its associated information were
deleted.

The new ticket was a *follow-up*, chasing residual identifiers re-supplied after
they searched only name and email. It was not a reversal. But `tracker.py set`
took the write without comment, and the confirmed total silently dropped by one.

### Why this is the worst shape of error in this project

Every other failure here is a broker doing something. This one was **the record
keeping losing a real result**, and it is nearly invisible: the totals are the
thing you check to see how you are doing, so an error that alters the totals
corrupts the instrument you would use to notice it. A confirmed removal is the
most expensive fact in the file — a letter, usually a follow-up, and a broker
willing to say plainly that the data is gone.

Worse, the pressure that produced it recurs constantly. **New activity on a
settled broker is normal**: a follow-up ticket, a duplicate confirmation re-sent,
an autoreply on an old thread. Every one of those tempts a status write, and every
one of them arrives long after the confirmation, when the confirmation is no
longer in front of you.

### The guard

`tracker.py set` now refuses to move a broker away from `confirmed` or
`not_found` unless `--regressed` is passed, and tells you what to do instead:

```
refusing to move mylife from 'confirmed' to 'submitted'.
  'confirmed' is a recorded outcome that cost real work. New activity on a
  settled broker is usually a follow-up, not a reversal -- record it with:
      tracker.py set mylife confirmed --note "..."
  If the broker really has re-added the data or withdrawn the confirmation,
  pass --regressed to say so deliberately.
```

**Downgrades are still possible, and must be.** A broker really can re-add
someone, and a tool that refused to record that would be lying in the other
direction. The point is only that it should never happen *by accident* — with
`--regressed` it happens deliberately and prints a note to stderr saying so.

**Note the shape of this fix.** The failure was not caught by care; I made the
mistake while being careful. It was caught because the summary count moved by one
in the wrong direction. **Watch the aggregates for movement you did not intend** —
they are frequently the only witness to this kind of error.

## §94 — Two agents on one queue

Partway through a run I found sends in the mailbox I had not made — four letters
and several replies, timestamped after my last batch. I checked for a cron entry,
a systemd timer, and other session files in the project directory. All three came
back empty, so I recorded the sends as *"most likely by the account owner working
the queue by hand."*

That was wrong. A `git push` was then rejected as non-fast-forward, and the
missing commit was **authored by Claude** — another session working the same
repository, fixing bounced addresses and sending its own outreach batch.

**The error was in the inference, not the evidence.** Every check I ran was
accurate. I just did not check the git remote, which is exactly where the answer
was, and then treated absence of evidence in the places I *had* looked as evidence
of absence. The same fault as §66: a mechanism that would explain the evidence is
not thereby the cause of it. I even wrote the wrong conclusion into five broker
notes before the push failure corrected me.

### What actually protects against collision here

Worth being precise, because the risk sounds worse than it is:

- **`data/removal_status.json` is gitignored and local.** Both sessions on the
  same machine read and write the same file, so `queue_batch.py`'s
  already-has-an-open-thread guard sees the other session's work. Duplicate
  letters to one broker are prevented by that, not by luck.
- **The daily cap is read from the same file**, so the two sessions share one
  budget rather than each spending a full one.
- **Git is where they actually collide**, and git says so loudly — a rejected push
  is a good failure. Rebase, resolve, continue.

### Resolving the overlap

Both sessions had written `brokers/datafy.md`. Theirs was the better file: they
made the send, and their note read more precisely than my scaffold. So I took
theirs wholesale rather than merging two descriptions of one event, and changed
only the status line, which said `email_pending` where nothing was actually
waiting on a confirmation link.

**Take the other agent's version when they did the work.** Merging two accounts of
the same action produces a record that reads as two actions.

### The rule

**When you find work you did not do, check the remote before theorising.** It is
one command, it is authoritative, and it beats an inference built from three
negative local checks.

## §95 — The registries exist so consumers can find brokers, and consumers cannot read them

Mining California's four registry files unlocked **517 brokers that appeared in no
other source we had**. It is far and away the highest-yield thing done in this
project. So the obvious next move is the other three states with a registration
regime: Vermont, Oregon and Texas.

All three are blocked, and each is blocked differently.

| state | registry | blocked by |
|---|---|---|
| California | four CSV files, downloadable | **nothing** — this is why it worked |
| Vermont | bulk database download | **login required** |
| Oregon | ASP.NET license lookup | **CAPTCHA** |
| Texas | Appian portal app | **client-rendered; no data without a browser** |

### What each one actually is

**Vermont** publishes the best artifact of any state — a genuine *bulk database
download*, no scraping needed, covering ~283 registrants (~177 active, ~101
expired). It sits behind an account login. We will not create an account with a
state filing system to read a public record, so this is a handoff.

**Oregon** has a public license-verification search and it very nearly worked. The
form is a standard ASP.NET postback; I fetched it, extracted `__VIEWSTATE`,
`__VIEWSTATEGENERATOR` and `__EVENTVALIDATION`, and posted
`t_web_lookup__profession_name=DFR-Data Broker` with
`t_web_lookup__license_type_name=Data Broker`. HTTP 200. The response said:

> *"There is an error with your input. * **Please solve the CAPTCHA.**"*

That is the end of the road. **We do not solve CAPTCHAs** — no exceptions, no
paid solving services, no local models. Handed off with the exact field values so
a person can reproduce it in about two minutes.

**Texas** requires registration under SB 2105 at \$300/year and publishes a
"searchable, central registry" — as an Appian portal application. `curl` returns
a **2.5 KB shell** containing the words "Data Broker" and nothing else; the list
is fetched client-side. It needs a real browser.

### Why this is worth recording rather than just working around

Each of these regimes was created so that consumers could find out who holds data
about them. The registry is not incidental to the law — in Texas the statute
*directs* the Secretary of State to maintain a searchable central registry.

And then:

- one requires an **account** to read a public record;
- one requires a **CAPTCHA**, i.e. it is designed to be readable one query at a
  time by a human and not otherwise;
- one requires **JavaScript**, which excludes any programmatic access and some
  assistive technology.

None of that is malice, and it should not be described as such. Each is an
ordinary implementation decision, made by a different agency, for reasons that
have nothing to do with data brokers. **The aggregate effect is still that the
lists exist and cannot be used at scale by the people they were written for.**

California is the control case. Its registry is four CSV files anyone can
download, and it is the reason 517 brokers are in this repository. The difference
between Californian coverage and everywhere-else coverage in this project is not
a difference in how many brokers operate in those states. **It is a difference in
file format.**

### The asymmetry that follows

A broker's obligation to register is satisfied by filing once a year. A
consumer's ability to act on that filing depends on being able to read the whole
list — one broker at a time behind a CAPTCHA is not a usable interface for
someone facing several hundred of them.

If any of this is ever worth raising with a regulator, the ask is small and
concrete: **publish the registry as a downloadable file.** California already
does. Nothing else about the regime needs to change.

### Status

Three handoffs staged — `_registry_oregon`, `_registry_vermont`,
`_registry_texas` — each self-contained, with the exact search values, the exact
menu path, and what to save where. Expected yield, extrapolating from California:
several hundred registrants, a meaningful share of them absent from every source
we currently hold.

**Related:** §78 (state filings as a family map), §83, §88.

## §96 — The enumerated confirmation caught the omission

§91 argued that an enumerated denial beats a bare one, because a bare "no records
found" is unfalsifiable. Sync.ME just demonstrated the same thing for a
**confirmation**, and it paid off immediately.

Their reply did not say "your data has been removed." It **listed every identifier
they had acted on** — eleven email addresses and eleven telephone numbers, pasted
out in full.

So the list could be checked against the one that was sent. **Two identifiers were
missing:**

- **one of the twelve email addresses** — twelve were supplied; eleven came back.
- **the current telephone number** — all eleven *disconnected* numbers were
  removed, and the one number actually in use was not.

Almost certainly an ordinary transcription slip while copying a long list. The
point is not that they erred. **The point is that it was detectable at all.** A
"your data has been removed" of the usual kind is compatible with any subset of
the work having been done, including this one, and the recipient has no way to
tell.

### The inversion is worth noting on its own

§87 recorded that the identifiers which match are frequently the stale ones —
BDEX found four matches and every one was a mailbox dead for years. Here the
opposite happened: every dead number was removed and **the live one was missed**.

For a caller-ID directory that is the worst single number to miss. It is the one
most likely to be live in the index, most likely to sit in other people's
uploaded contact books, and the only one where a wrong name or a spam label
affects a call the person actually receives.

**So check both ends of the list.** Stale identifiers are where matches hide;
current identifiers are where omissions hide. Neither habit substitutes for the
other.

### What made this reply good, and worth asking for by name

Sync.ME answered all three category-specific questions **separately** rather than
covering them with one word:

1. **Contact-book uploads** — the hardest question you can ask a crowdsourced
   directory, because entries contributed by other people's phones are filed
   under *those users'* accounts. Their answer: the block applies *"including if a
   user later uploads a contact book containing them."*
2. **Spam reports and labels** — *"these are removed along with everything
   else."* A number stripped of a name but still carrying commentary about its
   holder is not a completed removal.
3. **Suppression, not one-time deletion** — the opt-out list blocks future
   collection and display. In a directory that rebuilds from every new upload,
   that is the difference between a removal and a pause.

They also acknowledged the form defect (`_DEFLECTIONS.md` — one number at a time,
so the honest use of it trips the bot protection) rather than defending it.

**Ask for the three separately, in the first letter, and say why.** This reply is
the evidence that it works: a company given three distinct questions answered
three distinct questions.

### The confirmation wording worth quoting back at people

Speedeon's, in full:

> *"We have fulfilled your request to delete/opt-out. As you have asked to be
> deleted/opted-out please note that we are required by law to maintain a log of
> your request. Also, **we will retain your name and address on our Privacy
> Suppression file to ensure that we continue to delete your records from any new
> data files we receive from our vendors.**"*

Three sentences, and the last one does the work of a whole correspondence:

1. **The suppression is forward-looking** — applied against *incoming vendor
   files*, not a one-time clear of what they hold today. In a compiled-data
   business that is the difference between a removal and a pause.
2. **It says what is retained and why**, so the recipient does not have to ask
   which of the two lists it sits on. No guessing whether a retained identifier is
   protecting them or matching them.
3. **It explains the request log** as a legal requirement rather than leaving an
   unexplained retention to be discovered later.

Most confirmations say "your data has been removed" and stop, which is compatible
with almost any subset of the work having been done. **This one is checkable.**
Worth quoting to other companies as the model — it costs them one extra sentence
and removes three rounds of follow-up.

### But check the key it is suppressed on

Speedeon retains *"your name and address"* — singular. Sixteen addresses were
supplied.

A compiled consumer file is built on **address history**, and incoming vendor
records routinely carry a person under an address they left years ago. A
suppression matching only the current address lets precisely those records
through — the ones most likely to exist. So the scope question is worth asking
even of an excellent confirmation, and it is a question about **scope, not
sincerity** (§99): *is the entry keyed to the full history, or to current details
only?*

Same failure shape as §96, arrived at from the opposite direction: there, an
enumeration revealed an omission; here, a **singular noun** reveals a possible
one.


## §97 — The best tool in the country is available in one state

Datasys's General Counsel refused email by name — *"Sending a request to this
email address does not complete the privacy-request submission process"* — and
then, unusually, named **three** routes instead of one. The third was this:

> *"California residents: Datasys Group, Inc. is a registered California data
> broker. California residents may also submit a deletion request through
> California's Delete Request and Opt-Out Platform (**DROP**)."*

DROP is the mechanism created by California's DELETE Act (SB 362). Since 1
January 2026 a consumer submits **one request** and **every active registered
data broker** must honour it. Against a list of several hundred brokers, that is
not an incremental improvement over writing letters — it is a different category
of thing. It is, by a wide margin, the single highest-leverage action available to
a consumer anywhere in the United States.

**It is restricted to California residents.** The CPPA's own wording:

> *"As of January 1, 2026, **California residents** may use DROP to submit one
> request to all active data brokers."*

So it is unavailable here, and unavailable to residents of forty-nine states. It
must not be attempted by claiming a residency one does not have — that is a false
statement to a regulator's platform, and it would poison every legitimate request
in this project.

### What this means alongside §95

Two findings that belong together:

- **§95** — California is the only state whose data broker registry can be read
  in bulk. The other three require an account, a CAPTCHA, or JavaScript. That is
  why 517 of the brokers in this repository came from California filings.
- **§97** — California is also the only state where a consumer can act on that
  list with one submission instead of several hundred.

The same state has both the **readable list** and the **single lever**. Everyone
else gets neither, and has to do what this project does: enumerate brokers by
hand from whatever sources can be scraped, then write to each one individually,
then chase each reply.

The gap is not about how many brokers operate in each state — the brokers are
national and mostly identical. **It is entirely about what one state's
implementation makes possible.**

### The practical consequence for anyone using this repository

If you live in California: **use DROP first.** One submission does more than
everything in this repository combined, and the letters are then only for brokers
that are unregistered, out of scope, or that you want a substantive answer from
rather than just a deletion.

If you do not: this repository is the workaround, and the volume is the point.

### One thing worth taking from Datasys regardless

They also gave a **postal address** — 750 Park of Commerce Drive, Suite 150, Boca
Raton, FL 33487. Postal is the only channel in this entire project that **no
technical gate can close**. No account, no CAPTCHA, no JavaScript, no
autoresponder loop, no location gate. It is slow and it costs a stamp, and it
works when every other route has failed.

Worth asking for by default when a portal turns out to be unreachable: *"if the
form is not usable, what postal address may I write to?"*

**Related:** §95; `_DEFLECTIONS.md` §56, §57.

## §98 — Automation that routes, and automation that absorbs

Two automated first replies, four hours apart, doing opposite things.

**DemandScience** (`_DEFLECTIONS.md` §56) invited a reply — *"please reply with
those business details"* — and then answered that reply with a byte-identical copy
of itself, twelve seconds later, from an address sub-addressed `canned.response`.
The follow-up was **consumed**.

**DealMachine** replied:

> *"I'm AI Support Assistant, DealMachine's AI Agent and I'm well trained to
> answer your query but you can reply and ask for the team at any time. Your
> request involves legal compliance matters that require careful handling by our
> specialized team. A human agent will review your complete submission and respond
> directly to [your address] with next steps. **You won't need to repeat the
> details you've already provided.**"*

Both are automation. The difference is not sophistication — it is what happens to
the request.

### What DealMachine's agent got right

Four things, and each is worth naming because each is a decision somebody made:

1. **It identified itself as an AI.** No pretence of being a person.
2. **It recognised the limits of its competence.** A rights request is a legal
   compliance matter; it did not attempt an answer.
3. **It escalated, and said so specifically** — a named team, a stated next step,
   and a reply promised to the same address.
4. **It preserved the submission.** *"You won't need to repeat the details you've
   already provided."* That single sentence is the whole difference. A long,
   carefully assembled letter with twelve identifiers and prior addresses is
   exactly the thing an autoresponder loop destroys.

It also offered an override — *"you can reply and ask for the team at any time"* —
so the human route does not depend on the AI having judged correctly.

### The test to apply

An automated reply is fine. **Ask only what happened to the request:**

| | routes | absorbs |
|---|---|---|
| identifies itself | usually | sometimes |
| escalates to a human | yes, named | no |
| preserves what you sent | yes, says so | no |
| a reply to it reaches a person | yes | no — loops |

If the second automated message is identical to the first, it absorbs. If it names
a next step and says your details are retained, it routes.

**Do not treat "an AI answered" as a deflection in itself.** DealMachine's agent
handled a privacy request better than most human-staffed mailboxes in this
project: better than an unmonitored registered contact (§85), better than a dead
person-addressed filing (§88), and far better than an invitation that eats its own
acceptance (§56).

## §99 — Honouring the pre-commitment when the answer is inconvenient

Every letter in this project contains a version of this line:

> *"I would rather have an accurate answer than a flattering one. If you hold
> nothing about me, please say so — a clean 'no records found' is a useful and
> acceptable reply, and I will not treat it as evasion."*

True Blue Analytics replied, in full: **"We do not have your information on
file."**

That is a bare, unfalsifiable null — precisely the shape §91 argues is worse than
an enumerated one. Nothing about it can be checked. I could have asked which
identifiers they searched, whether prior addresses were included, whether the
search was keyed to name or to something else. Every one of those questions would
have been fair in the abstract.

**It was recorded as `not_found` and closed, with no follow-up.**

The pre-commitment exists to make honest answers cheap. A company that expects a
null to trigger an interrogation has every incentive to send something vaguer and
more defensible instead. **A pre-commitment honoured only when the answer is
convenient is not a pre-commitment** — it is a rhetorical device, and the second
time it is used on the same correspondent it will not work.

There is also a plain-facts reason to accept this one. True Blue Analytics
describes its work as serving progressive organisations and Democratic campaigns.
A null for someone with no donation, volunteer or membership history with them is
entirely plausible on its face. **Disbelief needs a reason, not just an
opportunity.**

### Where the line actually sits

The follow-ups sent elsewhere in this project were not to *nulls*. They were to
statements that **did not answer the question asked**:

- LoopMe and Connatix and Cint said *"we cannot identify you by name or email"* —
  which is not "we hold nothing", and my letters had asked about hashes, not
  names.
- BuiltWith said *"we do not hold data about social accounts"* — which is not
  "we hold nothing about you".
- Circana enumerated five cases and I asked about a sixth the list did not reach.

Those are gaps in scope. A flat "we do not have your information on file" has no
gap to point at — it answers exactly the question that was asked. **Press on
scope, never on sincerity.**

## §100 — The pass-through broker, and why writing to it is still worth doing

Blueprint Audiences is a **registered California data broker** that appears to
hold, about any given person, one thing: a pseudonymous identifier it did not
create, plus the audience segments that identifier belongs to.

Their Privacy Lead explained it plainly, and the explanation is worth quoting
because it resolves something this project kept running into:

> *"We don't hold email addresses in any form, hashed or otherwise. We never
> receive them... No email field, no phone field, no hashing function on our side.
> So there's no table to run your twelve addresses against.*
>
> *We are a registered data broker in the state of California because the law
> considers pseudonymous identifiers as personal data, and we hold pseudonymous
> identifiers. However, that is the only identifier we hold, and it is not created
> by us, but rather received from our partner.*
>
> *Hash to cookie to device to CTV to household is our identity partner's job, not
> ours. We don't build those mappings or receive them. No edges here to delete."*

### Why this matters beyond one company

A registry entry proves an obligation, **not a holding**. Some registered brokers
are genuinely the wrong target: the graph that resolves *you* to a pseudonymous ID
lives one step upstream, with an identity or onboarding partner who may not be
registered anywhere, or may be registered under a name that gives no hint of the
relationship.

So the letter can be perfectly aimed at a real registered broker and still be
aimed at the wrong company. That is not the broker being evasive. It is the
supply chain being longer than the registry.

### The useful output is a name, not a deletion

This is the key practical point. When a broker turns out to be a pass-through,
**what you want from them is the name of their upstream partner** — and they are
the only party who can give it to you.

A consumer can enumerate registered brokers from a state registry. A consumer
**cannot** discover which of them holds the mapping that resolves their own
identifiers. The broker can answer that in one line.

So the supplier question — already the highest-yield question in this project —
becomes the *entire* point of the correspondence once a pass-through is
identified. Ask it explicitly, ask it as a favour rather than a demand, and make
clear the request is closed either way so that answering costs them nothing.

### How to tell a pass-through from a qualified null

They look identical for one round. The difference shows on the follow-up:

| | qualified null (§58) | pass-through |
|---|---|---|
| answers "do you hold a hash of these?" | avoids it, or re-states architecture | **answers it directly** |
| explains *why* there is nothing | no | **yes — no field, no function, no table** |
| says where the data does live | no | **yes, names the layer** |
| survives a precise follow-up | no | **yes** |

Blueprint's *first* reply was a qualified null and is recorded as one. Its
**second** reply was a pass-through explanation. The same company produced both,
which is the useful lesson: **a qualified null is often a template, and a precise
follow-up is what gets you past it to whoever actually knows.**

### And the thing worth copying

Asked which list a retained suppression hash sits on — the question a dozen
companies have now been asked — the answer was:

> *"It can't work as a match key because there's nothing here to match it
> against."*

Not a denial. A demonstration that the question dissolves under their
architecture. **That is what a good answer looks like: it makes itself checkable
rather than asking to be believed.**

**Related:** §91, §96, §99; `_DEFLECTIONS.md` §54, §58.

## §101 — The mailbox that sends but does not receive

`optout@accurateappend.com`, **14:58**, a personalised confirmation naming exactly
which of my details had been opted out:

> *"Information opted-out: [name] / [current address] / [current phone] /
> [current email]"*

The same address, **15:20**, replying to my follow-up:

> *"Please note that **this email address is not monitored.**"*

Twenty-two minutes apart. The mailbox **sends** and does not **receive**.

### This is worse than §85, and looks better

§85 was Experian's mailbox announcing it was unmonitored — annoying, but honest,
and immediately legible as a dead end. Here the first message is a **personalised
confirmation containing my own data**, which is about as strong a signal as exists
that a person is on the other end. Every instinct says *someone read my letter and
acted on it*.

They did not. A machine did, and nothing will read the reply.

**So a confirmation that names your specific data is not evidence the mailbox is
monitored.** That inference feels safe and is wrong.

### The shape of the partial tells you which mechanism produced it

This is the useful diagnostic, and it generalises.

Accurate Append processed **four** identifiers out of roughly **forty**: one name,
one address, one phone number, one email address. **Exactly one of each field
type, all of them the current value.**

That is not what careless human transcription looks like. A person skimming a long
list and giving up drops a *ragged* subset — six of twelve emails, a few
addresses, whatever they got through. **One-of-each-type is the signature of an
automated single-value field parser**: it recognises `Name:`, `Phone:`, `Mailing
address:`, `Email:`, takes the first value it finds for each, and ignores every
subsequent line.

| what the partial looks like | what produced it | what to do |
|---|---|---|
| exactly one of each field type | automated field extraction | email is useless — find the form; expect one value per submission |
| ragged subset across categories | a human working through a list | reply with the remainder; a person will read it |
| every stale value, current one missed | human working from the list as given | reply, flag the omission (§96) |
| only stale values matched | genuine search result, not an error | that is a real finding (§87) |

Sync.me's omission (§96) was the *ragged* kind — eleven of twelve emails, all
eleven old numbers but not the current one. A human copying a long list. And a
human read the follow-up and could act on it.

Accurate Append's is the *parser* kind. The follow-up asking for the remaining
thirty-six identifiers will not be read by anyone, ever.

### What follows practically

1. **Read the shape of a partial before writing a follow-up.** If it is
   one-of-each-type, a follow-up is wasted effort; go straight to the form.
2. **A form that takes one identifier per submission is the same limitation
   surfacing in a different place.** Accurate Append's does, and so does
   Speedeon's (*"Only one name and address may be included on this form"*). The
   system holds one value per field, so every route it offers holds one value per
   field. That is not obstruction, it is the data model showing through.
3. **Correct a handoff when the facts change.** Mine told the reader to wait for
   the email reply before touching the form. That instruction became wrong
   twenty-two minutes after I wrote it, and a handoff that is confidently wrong is
   worse than one that is vague.

**Related:** §85, §87, §96; and the Speedeon note above on suppression scope.

## §102 — The cold approach is a free sample of the pipeline

An unsolicited recruiter email arrived mid-project:

> *"Hi [name], We came across your profile and think you could be an excellent fit
> for a role we're looking to fill..."*

Ordinary recruiting spam. Not a registered data broker, not in our registry, and
in the normal course you would delete it.

**Do not delete it. Reply and ask where they got your details.**

### Why this is the highest-signal discovery event available

The hardest problem in this entire project is not persuading brokers to delete
things. It is **finding out which companies hold your data in the first place.**
State registries list companies that have *registered*; they do not say which of
them holds a record on **you**, and a large number of the businesses in this chain
never register at all.

Every other discovery method is inference:

- registries → who is *obliged to register*, not who holds you;
- MX tenant fingerprinting (`_FAMILIES.md` appendix six) → corporate structure;
- asking brokers to name suppliers → good, but only reaches brokers you already
  found.

A cold approach is different in kind. **The sender was looking at a screen with
your name and email address on it.** They know the answer as a matter of direct
observation, and it costs them one line.

### How to ask

Politely, and as a favour rather than a demand. This person sent a normal
recruiting email; turning it into a compliance confrontation makes them defensive
and forward it to a legal team who will say nothing.

What worked in the letter sent:

- **Disclaim hostility explicitly.** *"I am not accusing you of anything, and I
  know that sourcing candidate contact details is a normal part of recruiting."*
- **Say what you actually want:** the name of the tool, platform, list or
  enrichment service. Not a policy discussion — a product name.
- **Explain why it is worth so much to you**, briefly. People help when they
  understand the problem, and this one is easy to explain: registries say who is
  obliged to register, not who holds me; you know because you were looking at it.
- **Ask for deletion *and* suppression**, with the reason stated — deletion alone
  is undone by their next refresh from the same source, and neither party would
  know.
- **Offer the profile URL as a suppression key** (§90).
- **Mention the statutory right last, and defuse it:** *"I would much rather this
  were a favour between people than a formal request."* Keep it available without
  leading with it.

### It also confirms something in the other direction

This arrival is itself evidence that the LinkedIn → sourcing-tool →
recruiter-inbox pipeline is **live right now**, and that the profile is still
being ingested despite every suppression request sent. That is not a reason to
stop asking for suppression. It is the measurement showing why the suppression has
to be *forward-looking against the source* rather than a deletion of one
downstream copy.

**Treat every unsolicited approach — recruiter, insurance, home services, "we
noticed you own a property" — as a discovery lead.** It is the only signal in this
whole exercise that arrives without being sought.

**Related:** §90, §100; `_FAMILIES.md` appendix six.

## §103 — 464 requests were searched against the wrong keys, and I caused it

The largest defect found in this project so far is mine, not a broker's.

**The identifier list grew during the campaign.** Early letters carried 8 email
addresses, 10 prior addresses and 8 prior telephone numbers. Current letters carry
12, 16 and 11. The additions were made partway through, as older accounts and
addresses were recovered.

**464 brokers were contacted before that expansion.** Every one of them was
searched against a list missing four email addresses, six prior addresses and
three telephone numbers.

### Why that is much worse than "some keys were missing"

BDEX searched all twelve email addresses and reported back that **four matched —
and every one of the four was a mailbox out of service for years. Not one current
address matched** (§87).

Those four are:

| identifier | in the early letters? |
|---|---|
| the four addresses BDEX matched | **none of them** |

All four were among the late additions. So the identifiers **demonstrated to be
the ones that actually match** were absent from 464 requests. This is not a
theoretical gap — it is the specific gap that the one broker who checked carefully
told us was the productive one.

Worse, the early wave was the **high-value wave**: Acxiom, Epsilon, Data Axle,
Intelius, BeenVerified, InstantCheckmate were all contacted on 15–18 August. The
largest compilers got the shortest list.

### Every null from that period is weaker evidence than it looked

This is the part that changes how the record should be read. A "no records found"
from a broker contacted on 16 August means *"nothing matched 8 email addresses, 10
addresses and 8 numbers"* — **not** *"nothing matched the full set."* Those are
different claims, and the first was being recorded as though it were the second.

The brokers did nothing wrong. They answered accurately for what they were given.

### The remediation

`scripts/supplement_identifiers.py` generates a letter that:

- **states plainly that it is not a new request** — *"please treat it as completing
  the one already on file rather than restarting the clock."* Framing matters: a
  new request resets a statutory response period and invites a fresh verification
  round, which is exactly what should not happen;
- lists the additions separately, and **marks them inline** in the full list so
  the recipient can see at a glance what is new;
- gives the BDEX evidence as the reason, without disputing the earlier answer:
  *"that answer was accurate for the identifiers it was given — and may still be
  incomplete. I am not disputing it."*;
- asks the recipient to **enumerate what they searched** (§96, §101);
- pre-commits to accepting a repeated null.

**426 brokers qualify** (the balance of the 464 are unreachable, form-only, or
otherwise past helping by email). It tracks a `supplemented` flag per broker so the
campaign is resumable and nobody is written to twice.

### The lesson worth generalising

**When the identifier list changes, every prior request becomes partially stale —
and nothing in the system notices.** The tracker records that a request was sent;
it does not record *what was in it*. A null answer keeps looking like a null answer
long after the question that produced it has changed.

Two habits follow:

1. **Freeze the identifier list before a campaign, or version it.** Recording which
   identifier-set version each request used would have made this visible
   immediately instead of five hundred letters later.
2. **Treat a recovered identifier as a trigger, not just an addition.** Finding an
   old mailbox is not merely one more thing to search — it retroactively weakens
   every answer already received.

**Related:** §87, §96, §101.

## §104 — Proving you control a mailbox that no longer exists

Proxima's verification notice, which is otherwise one of the better ones received:

> *"We reserve the right, where allowed by law, to take steps to confirm that you
> are the owner/controller of all email addresses you provide in connection with a
> request."*

The purpose is sound and should be conceded immediately: a company should not
delete a stranger's records because someone typed their address into a form.

But applied strictly, the rule is **unmeetable for exactly the identifiers that
matter.**

### The two directions run opposite

Of the twelve email addresses in this project, several are mailboxes that cannot
be accessed by anyone:

- a university account closed on leaving the institution;
- addresses at `webtv.net`, `iwon.com`, `gateway.net` — **providers that no longer
  exist.** Nobody can demonstrate control of a mailbox at a company gone for
  twenty years.

And those are the ones that match. BDEX searched all twelve and found **four — every
one a dead mailbox, none of the current addresses** (§87).

So:

| | can prove control | likely to match |
|---|---|---|
| current addresses | **yes** | rarely |
| dead mailboxes | **no** | **frequently** |

A verification rule of *prove you control each address* therefore admits the
identifiers least likely to be in the data and excludes the ones most likely to
be. It is the same shape as the MAID demand (`_DEFLECTIONS.md` §54): a requirement
that is unmeetable **by construction** rather than by reluctance, and unmeetable
for everyone equally.

### Do not just object — offer three substitutes

Objecting alone gets you nowhere, because the company's concern is legitimate.
Offer alternatives that preserve the protective purpose:

1. **Confirm the live ones individually** — reply from each address you still
   control. Cheap, and it settles that subset completely.
2. **Corroborating identifiers for the dead ones** — date of birth, prior postal
   addresses, prior telephone numbers. Not proof of mailbox control, but a set a
   stranger would not hold together.
3. **Confirm-before-delete** — the strongest, and the one to lead with:

   > *"If a dead address matches something in your data, tell me what you found —
   > the approximate record date, the associated postal address or telephone
   > number — and I will confirm it is mine before you delete anything."*

   This **protects any third party completely**, because nothing is removed until
   the requester verifies the match, and it uses only information the company
   already holds. It is the email-address analogue of the geographic query offered
   to location brokers.

### Then close the gap explicitly

> *"If none of those is acceptable and you can only act on addresses whose control
> I can demonstrate today, please say so plainly. I will accept it and record it
> as the scope of what was done — but I would like it stated, rather than have the
> dead addresses quietly fall out of the request."*

That last clause is the point. Without it, the likely outcome is not a refusal but
a **silent narrowing**: the request is honoured for the addresses that verified,
the others are never mentioned again, and the confirmation reads exactly as it
would have if everything had been searched.

**Related:** §87, §96, §103; `_DEFLECTIONS.md` §54.

### A company that solved this in one sentence

Disqus, unprompted, in a routine support reply:

> *"If the account you are looking to remove is registered with an email address
> that you no longer have access to, **please mention that in your request**."*

That is the whole fix. It costs one sentence, it requires no new process, and it
tells the person with the twenty-year-old mailbox that their case is anticipated
rather than disqualifying. Worth quoting to any company that raises the control
requirement.

## §105 — Thirty-five thousand requests, six matches

Scraping Robot (Sprious) replied to a deletion request with something almost
nobody provides: **a number.**

> *"In response to previous requests from authorized agents, we searched our
> records for **over 35,000 data subjects** for whom authorized agents requested
> that we delete their data. We found **six email addresses** (and no other data
> elements) that were responsive to the data subjects' requests. Those matches
> constituted **less than 0.0002%** of the records we were asked to review, and
> that low response rate corroborates the fact we are not a data processor or data
> broker."*

### Take the argument seriously, because it is a good one

This is the strongest form of null answer in this entire project, and it should be
accepted rather than argued with. A bare *"we hold no records about you"* is
unfalsifiable — the recipient cannot distinguish a genuine null from a search run
against the wrong key (§91). A rate measured across 35,000 subjects is a claim
that can be **weighed**. 0.0002% is not consistent with holding consumer data at
scale.

The request was closed on that basis. **A company that answers with evidence has
earned the answer being accepted.**

### The scope gap that survives it

One question the reply does not reach, and it is narrow. Their position is that
they do not store what customers collect using their software. But Scraping Robot
is an **API service**, not software installed on a customer's own machines — so
scraped content is retrieved by *their* infrastructure before being handed to the
customer.

*"We do not store what customers collect"* and *"no copy ever exists on our
systems"* are different statements, and only the second answers the question. So
the follow-up asks, factually: does content pass through, get cached, or get
logged on infrastructure they control — even transiently, even in error logs — and
if so, for how long, and is it searchable by content rather than only by customer
account?

With, as always, the pre-commitment: **if nothing is retained beyond transit, say
so and that is complete.**

### The second finding, which is not about this company at all

Thirty-five thousand deletion requests were fired at a company holding **six email
addresses in total.**

Those came through **authorized agents** — the paid removal services. Which means
those services appear to be blasting every entity that shows up on a data-broker
list, with no regard to whether the entity plausibly holds anything about their
client.

Two consequences, and both matter to anyone using this repository:

1. **It imposes a real cost on the recipient.** Reviewing 35,000 subject requests
   is a substantial amount of work for an outcome of six.
2. **It devalues the well-founded requests.** A privacy team that has learned to
   expect a 0.0002% hit rate will reasonably start treating the entire category as
   noise. That makes life harder for an individual writing about a specific record
   they have reason to believe exists — which is precisely what this project does.

This inverts §100. There, the lesson was that *a registry entry proves an
obligation, not a holding.* Here the same fact runs the other way: **appearing on
a list attracts requests regardless of whether you hold anything** — and the volume
is generated by automated agents rather than by people.

### What follows for how we write

It is an argument for the approach already taken here and against the obvious
alternative of blasting everything:

- **Say you are not an agent.** Every letter in this project opens by stating the
  writer is the consumer, writing about their own data. Against a background of
  35,000 agent-driven requests, that sentence is doing more work than it appears
  to.
- **Give a reason to look**, not just a demand — the category-specific paragraph,
  the named identifiers, the specific product.
- **Mean the pre-commitment to accept a null** (§99). It is the cheapest way to
  distinguish yourself from a bulk filing, and the only reason a company that has
  been burned 35,000 times would spend attention on you.

**Related:** §91, §99, §100.

## §106 — Five answers, two of them uncomfortable, and then a closed door

Revelio Labs answered a five-part follow-up in five lines:

> *1. Fully suppressed unless someone changes their professional profile URL and
> we can't connect it to the old one*
> *2. We had modeled fields, but we have deleted all of them*
> *3. Underlying records came from professional profile sites*
> *4. **No, we cannot enforce downstream deletion.***
> *5. We fully deleted the individual record; it is no longer contained in
> aggregates*
>
> *"We now consider this case fully closed and will not be engaging in further
> correspondence on the matter."*

### Two of those cost them something to say

**Answer 4 is the one to notice.** Companies are not obliged to volunteer that a
deletion does not reach copies already licensed to customers. Most simply do not
mention downstream copies at all, and the omission is invisible. Revelio said it
flatly.

My letter had asked for exactly that: *"I would rather have an uncomfortable
accurate answer than a comfortable vague one."* **When a company takes you up on
that, the answer is to accept it — not to treat the admission as an opening.**

**Answer 2 is the second.** *"We had modeled fields"* concedes that inferred
attributes existed, in reply to a question that named estimated compensation,
inferred seniority, inferred gender or ethnicity, and departure-likelihood
scores. Nothing forced that concession either.

### Answer 1 confirms the suppression key

*"Fully suppressed unless someone changes their professional profile URL and we
can't connect it to the old one."*

That is §90 stated from the inside. A standing do-not-source entry **is**
possible at a crawl-driven workforce broker, and it **is** keyed to the profile
URL. The caveat is honest and technically real: change the URL and the link to the
old suppression may break.

So the guidance sharpens. When asking for profile-URL suppression, it is worth
knowing that **changing your profile URL afterwards can silently undo it.** That
is not a reason to avoid the request; it is a reason not to change the URL later
without re-notifying.

### Answer 3 fell short, and I let it

I asked which platform, posting site or licensed feed supplied the records. The
answer — *"professional profile sites"* — is a category, not a name.

**I did not press.** Not because the answer was adequate, but because they had
answered four other questions squarely, conceded two things against interest, and
said they were closing the matter.

Pressing there teaches a company that **candour buys more work.** The next person
who asks Revelio a five-part question gets a shorter reply, or a form. A single
generic answer among five good ones is a price worth paying to keep candour cheap.

Recorded as unresolved rather than pursued: **the sources are still unnamed.**

### On "we will not be engaging in further correspondence"

Honour it. This is not the Outlogic case (`_DEFLECTIONS.md`) where two refusals
came without substance — here the door closed *after* the questions were answered.

**The test is not whether they refused to keep talking. It is whether they
answered before they stopped.**

**Related:** §90, §99; `_CATEGORY_VARIANTS.md` on workforce and talent
intelligence.

## §107 — The company does not know what its own filing says

Datonics' accounting department replied to a request that had reached them because
their registered contact address is an accounts mailbox:

> *"We believe you have mistakenly reached the Datonics accounting department.
> **This email address is not made publicly available by Datonics.**"*

It is. By Datonics. In its own California data broker registration filings — which
is the only place I found it.

| filing year | contact email listed |
|---|---|
| 2020–2023 (DOJ) | `privacy [at] datonics.com` |
| **2024 (CPPA)** | **`accounting@…`** |
| **2025 (CPPA)** | **`accounting@…`** |
| **2026 (CPPA)** | **`accounting@…`** |

The address was right in the earliest filing, changed before the 2024
registration, and has been **re-filed the same way for three consecutive years.**

### This is a distinct failure from §83 and §86

- **§83** — the filed contact is a *person*, not a desk. Wrong desk, but the
  company chose it.
- **§86** — the filed address contains a *typo*. Wrong address, and nobody
  noticed.
- **§107** — the address is correct, deliverable, and monitored. **The company
  simply does not know it is the one they published**, and says so in writing when
  a request arrives.

That last one is the most invisible of the three, because **everything works**.
The mail is delivered. A human reads it. They reply. And the reply says the
sender must have made a mistake — so the sender, if less stubborn than this
project, concludes they got the address from somewhere unreliable and goes away.

### Why it compounds silently

Every consumer who does the correct thing — look up the registered contact and
write to it — lands in Accounting. Some of those requests will be deleted as
misdirected. **Neither the sender nor the privacy team ever learns it happened.**
The privacy team's view is that email requests are rare; the accounting team's
view is that they occasionally get odd mail. Both are consistent with the
evidence each of them sees.

### What to do

**Tell them, with the citation.** Not tactfully — plainly, with the filing years
and the exact values, because a vague "I think your filing might be wrong" is easy
to set aside and a table is not. The correction costs them one form and closes the
gap permanently for everyone who writes after you.

And say why it matters *to them*, not to you: misdirected rights requests that
get quietly deleted are a compliance exposure they cannot see from inside.

**This is the forward-this-internally opener (§83) paying off twice.** It got the
letter routed to the right desk *and* surfaced the reason it had gone to the wrong
one. Asking a recipient to correct a stale filing sounds like boilerplate
politeness; here it produced a documented three-year error the company did not
know it had.

**Related:** §83, §86, §88.

## §108 — We have been over-supplying identifiers, and a broker told us so

Datonics' automated reply contains a sentence no other company in this project has
sent:

> *"Please do not send us the personal information of people that we would not
> otherwise possess, such as a physical address, telephone number or date of
> birth."*

They are right, and the standard letter here was wrong for their category.

Datonics holds **MAIDs, cookies and hashed email addresses** — they say so plainly
in the same reply. The letter sent to them supplied **sixteen postal addresses,
twelve telephone numbers and a date of birth.** That is handing a company
identifiers it does not have, does not want, and cannot use — and they now sit in
its inbox and ticketing system whether or not the privacy team retains them.

### The instinct was right and the application was wrong

"List every identifier so they can search properly" is **correct for an
address-keyed business** — a people-search index, a compiled consumer file, a
property-records product. §103 exists precisely because too *few* identifiers
produced 464 under-scoped requests.

But it is **wrong for a pseudonymous ad-tech business**, where the only useful
input is an email address to hash. There, extra identifiers are not thoroughness;
they are disclosure.

**Match the identifiers supplied to the identifier types the recipient actually
holds:**

| broker type | supply | withhold |
|---|---|---|
| people-search, compiled files, property, skip trace | everything — the address history *is* the record | — |
| identity graph / ad-tech / MAID-and-hash | **email addresses only** | postal addresses, phone numbers, DOB |
| B2B / professional data | emails, employer, **profile URL** | home addresses, DOB |
| credit/FCRA-adjacent | as required for file disclosure | nothing extra |

### Why this is worth recording rather than quietly fixing

Every letter in this project argues that companies should collect less than they
can. **Sending a pseudonymous ad-tech firm a date of birth it never had is the
same error, made by me.** The asymmetry is not lost: I have spent weeks asking
brokers to justify holding data about people who never gave it to them, while
posting new identifiers to a company that had explicitly not collected them.

The reply to Datonics says so directly, asks them to delete the excess, and
supplies email addresses only.

### It also produced the §54 admission unprompted

The same autoreply volunteered what four other companies had to be asked for:

> *"We generally only collect and process mobile device advertising IDs, cookies
> and **hashed email addresses**... **We may have such data about you.**"*

That is the honest form of *"we cannot identify you by name or email"*. The others
stopped at the first clause. **A company that tells you it holds hashed emails is
easier to deal with than one that tells you it holds no email addresses**, and both
sentences can describe the same database.

**Related:** §103; `_DEFLECTIONS.md` §54, §58.


---

## §109
### A compliance portal's navigation menu is a client list

`privacycompliance.biz` runs the opt-out flow for DatabaseUSA and Infofree. We knew
that much: Infofree's privacy policy links to it, and we completed the flow through
it twice on 2026-08-18.

What we had not done was read the menu.

The portal's navigation enumerates **fourteen brands**, each with its own privacy
pages: AtoZdatabases, AtoZacademics, DatabaseUSA, DatabaseUSA Gov, EmailUSA,
FreeSalesLeads, HDML, Infofree, ListProGuru, NewBusinessListsUSA,
NewHomeownerListsUSA, ReferenceGuru, ResearchUSA, Salesflower, SalesLeads101.

Two of those fourteen were in a broker registry assembled from every state
data-broker registry plus a commercial removal service's catalogue. **Twelve were
not in it anywhere.**

The technique generalises, and it is better than the MX fingerprinting in §89 for
this purpose. Mail-tenant fingerprinting infers a family from shared
infrastructure, which is circumstantial — two companies can share a mail host and
be unrelated, which is why that scan reports CONFIRMED and WEAK separately. A
compliance portal's menu is not circumstantial. The operator built a page for each
brand because each brand needs one, and the menu that lists them is the operator's
own statement of which brands it answers for.

And the enumeration is a **byproduct of the law**. The pages exist because
state privacy statutes require a disclosed consumer route. The more thoroughly an
operator complies, the more completely it publishes the shape of the group.

**How to use it:** when a broker's opt-out route lands on a third-party compliance
domain rather than the broker's own site, do not just complete the form. Pull every
link on the page and group them by brand token. The ones you do not recognise are
brokers you have not written to.

**Related:** §89 (family discovery by mail tenant), §110, §100.

---

## §110
### The matrix has rows for states, and you may not be one of them

The same portal is organised as a grid: one page per brand, per state. California,
Colorado, Connecticut, Delaware, Indiana, Iowa, Maryland, Montana, Utah, Virginia —
the states with comprehensive privacy statutes. Six of the fourteen brands also
have a catch-all page for everybody else, named `/other-<brand>/`.

Eight of them do not.

So for eight brands in this family, a resident of a state without a comprehensive
privacy law has **no page at all**. Not a page that refuses them. Not a page that
explains why they are ineligible. Nothing — the URL 404s, because the row was never
built.

This is worth separating from an ordinary residency deflection. A residency
deflection is an answer: *we only honour requests from covered states.* It can be
argued with, escalated, or pre-empted (ask them to honour it as company policy and
to say in writing which basis they used). It is a position someone holds.

A missing row is not a position. Nobody decided that a Pennsylvanian may not opt
out of NewHomeownerListsUSA. Someone built pages for the states that generate legal
exposure and stopped. The absence is invisible from the operator's side — no form
arrives, no complaint arrives, no bounce arrives — and it is invisible from the
consumer's side too, because a 404 looks like a broken link rather than a decision.

The consequence is that **which rights you have depends on which brand name your
data was sold under**, and that is a fact about the vendor's page matrix rather
than about you, the data, or the statute.

**What to do:** write to the operator, not the brand, and ask the question plainly
— *what is a resident of a non-covered state supposed to do for these brands?*
Frame it as a routing question rather than an accusation, because it probably is
one. Then ask them to honour the request as company policy if the honest answer is
that no route exists. We sent exactly that letter on 2026-08-26 to
`OptOut@privacycompliance.biz`, naming all fourteen brands and the eight gaps.

**Related:** §109, §97 (DROP is California-only), `_DEFLECTIONS.md` §61 (the
deflection that is a schema rather than a decision).

---

## §111
### Both addresses this company filed with the state are dead

ResearchUSA's California data-broker registration lists
`privacy@researchusallc.com` as its consumer contact. It returns
550 "address couldn't be found." DatabaseUSA's filing lists
`privacy@databaseusa.com`. Same 550.

In both cases the domain is healthy and the MX records resolve — Intermedia
Exchange, the same tenant for both — so **every domain-level deliverability check
passes.** `check_email_domains.deliverable()` returns True for both. The mailbox is
what does not exist, and nothing short of sending a message finds that out.

That is the §88 pattern, but the detail that matters here is *where the address came
from.* This was not scraped off a footer or guessed from a pattern. It is the
address the company itself typed into a regulator's form as the place consumers
should write. Our registry even records `email_verified: true`,
`email_verified_by: ca_data_broker_registry` — and the verification was real. The
filing does say that. The filing is just wrong.

ResearchUSA's older 2020 filing lists a web route too, `ccpa-optout.com/rsusa/`.
That 404s. The 2024 filing's route, `privacycompliance.biz/researchusallc-ccpa/`,
is the only one of the three that works.

**So of the three consumer routes this company has filed with a state regulator
across its registration history, two are dead, and nothing in the registry marks
which is current.** Filings accumulate. Nobody revalidates them. A consumer working
from the published registry — or a tool doing it at scale — fails two times in
three and has no way to tell a dead route from a route that is ignoring them.

This is checkable by anyone, cheaply, at scale: resolve every address in every
state registry, send nothing, and count the 550s. It is the kind of sweep a
regulator could run in an afternoon.

**Related:** §88, §92 (null MX), §107, §109.

---

## §112
### Seven brands, one refusal, word for word

Writing to a people-search site's support address gets this back:

> "This email address is dedicated to customer service inquiries and is not
> intended for privacy-related requests. We do not process privacy requests
> received via email."

We have now had that text back **character-for-character identical** from seven
brands: PeopleSearchNow, Phonebooks, AdvancedBackgroundChecks, FastPeopleSearch,
SpyDialer, TruePeopleSearch and FamilyTreeNow.

Four of those seven are named on Mississippi Tornado Alley LLC's California
registration. **Three are not.**

So this is a third family-fingerprinting technique, and it has a different reach
from the other two:

| Signal | Strength | Finds |
|---|---|---|
| Shared mail tenant (§89) | circumstantial — shared hosts exist | who runs the mailboxes |
| Compliance-portal menu (§109) | the operator's own client list | who the vendor answers for |
| Identical support boilerplate | strong, but ambiguous in one specific way | who shares a *support desk* |

The ambiguity is real and worth stating rather than papering over: identical
boilerplate can mean one operator, or it can mean two operators using the same
support vendor's canned reply. The reason to act on it anyway is that the two
possibilities have the same next step — **ask the estate you already know about
whether the unattributed brands are theirs**, and offer them the vendor explanation
as an out. Either answer moves you forward, and only silence does not.

We sent exactly that on 2026-08-26 to `privacy@mtalley.zendesk.com`, quoting the
boilerplate and naming the three outsiders.

**The second thing this catches.** A brand that sends this reply has stated in
writing that email does not reach its privacy function. That retroactively weakens
every `submitted` status resting on an email to it. Check each one before
downgrading, though — five of our six looked wrong and turned out to be fine:

- three were separately covered by the consolidated letter to the estate's
  *privacy* address, which is a different channel and does work;
- two had on-screen confirmed self-service submissions.

Only **SpyDialer** had nothing underneath — its `submitted` had been adopted from a
shared ledger with the note *"another agent recorded submitted, no detail is
carried across"*, and the sole reply we have ever had from it is the refusal.
Downgraded to `manual_required` and staged against the real form.

The lesson is not "downgrade on sight." It is that **a refusal template is a reason
to re-check every status that rests on that channel**, and the check has to look at
what each status actually rests on, one at a time.

**Related:** §89, §109, §103, `_DEFLECTIONS.md` §63, `_FAMILIES.md`.
