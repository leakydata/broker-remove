# Deflection scripts, and how to answer them

Brokers reuse a small number of arguments for not honoring a request. None of them
are unanswerable. Collected from actual replies — quotes are verbatim.

---

## 1. "Your state has no privacy law"

> *"Only residents of states with Consumer Privacy laws are able to make official
> Consumer Privacy requests."* — Whitepages, listing 18 states

**Answer:** read the rest of their own message. The same reply continued:

> *"It currently is company policy to remove and not sell all information from our
> site, including public information, upon request."*

That policy is **not conditioned on residence**. Invoke it explicitly and ask them
to confirm they are processing on that basis.

Also check their **own form's state dropdown**. TruePeopleSearch, FamilyTreeNow and
PeopleFinders all list every state including ones absent from their "covered"
list — the gatekeeping is softer than the copy implies. And note that Whitepages'
list of 18 states **omitted California**, whose CCPA is the oldest such law in the
country; treat these lists as marketing, not law.

**Pre-empt it.** Every outgoing letter should already say: *if you believe you are
not subject to these statutes, or that I do not reside in a covered state, honor
this as a matter of your published privacy policy, and tell me in writing which
basis you applied.* That closes the door before they reach for it.

---

## 2. "We don't accept privacy requests via email"

> *"This email address is dedicated to customer service inquiries and is not
> intended for privacy-related requests."* — TruePeopleSearch, FamilyTreeNow

**Answer:** they almost always name the route they *do* accept. Take it. This
single move unblocked three brokers here:

- TruePeopleSearch / FamilyTreeNow → `/privacy-rights`
- Affinity Solutions → a OneTrust webform
- PeopleFinders → `/request-my-info`

Then check whether that route is *itself* gated (see `_CLOUDFLARE_GATED.md`), and
whether **request type changes whether a form even renders** — on both
TruePeopleSearch and FamilyTreeNow, "Right to Delete" produced no form at all while
"Right to Know" produced a working one.

---

## 3. "Publicly available information isn't covered"

> *"Federal law does not require data brokers to delete publicly available
> information as it is deemed public. However… we offer the option to remove it as
> a courtesy."* — Radaris

> *"Peoplefinders uses publicly available information, which is not covered by U.S.
> state privacy laws."* — PeopleFinders

**Answer:** note that both sentences end by offering removal anyway. This is
positioning, not a refusal. Accept the "courtesy" framing and proceed — the goal is
the removal, not winning the argument. Ask them to confirm in writing which basis
they applied, so the answer is on record either way.

---

## 4. "We don't store data — we fetch it from third parties"

> *"The information you find is not stored by us. Instead, it is retrieved from
> third-party data providers at the time you perform the search."*
> — TruePeopleSearch

**Answer:** the listing still displays, and displaying is the harm. Ask for
suppression of the **display**, which is within their control regardless of where
the data is fetched from. Then pursue the upstream provider separately — and ask
them to name it.

---

## 5. "Send us more information first"

> *"We need to gather a few extra details to locate the record… First and Last
> Name / City and State / Street Address / Link to the profile. Please include only
> one profile per email request."* — CheckPeople

**Answer:** legitimate, usually. Supply it — but supply *more* than asked: prior
addresses, old phone numbers, aliases, every email. And **check their listed data
for errors before replying**. CheckPeople's record carried a birth year off by one;
flagging that proactively removes a later excuse that the record "could not be
matched".

---

## 6. Silence

No reply is the most common response of all. Statutory clocks (45 days under CCPA,
extendable) run from the request date, so keep the timestamp and the ticket
reference. A follow-up on an existing thread is more effective than a fresh
request, which starts at the back of the queue.

---

## 7. The broken flow that isn't advertised as broken

Radaris illustrates a pattern worth naming: **the documented route and the working
route are different pages.**

`/control-privacy` is the removal wizard linked from their support replies. It
*does* complete, but it terminates on a third-party upsell page while the
verification email is still in flight — which reads as failure if you check the
inbox immediately. (An earlier version of these notes recorded it as broken. It
was not; the check was simply too early.)

`/data_privacy_center` is a separate page that documents email routes the wizard
never mentions: a covered-persons address for former law enforcement, a
customer-service address for the multiple-record case, a phone line, and appeal
rights by state.

**Before accepting that a broker's opt-out is broken, look for their privacy
*policy* page rather than their opt-out *tool*.** The policy page is written for
regulators and lists obligations; the tool is written for deflection. They often
disagree, and the policy page usually wins.

Terms worth trying: `/data_privacy_center`, `/privacy-rights`, `/privacy-center`,
`/your-privacy-choices`, `/dsr`, `/legal/privacy`.

---

## 8. The form that structurally excludes you

Aged Lead Store refuses email and directs consumers to six web forms. Their Data
Deletion form has a **required** State field with a fixed 20-state dropdown.
Pennsylvania is absent — so a PA resident **cannot submit it at all**.

Combined with the email refusal, a resident of roughly thirty states has no working
self-service route. Their own page also contradicts itself: the prose lists 24
states, the dropdown offers 20, and the two sets do not match.

**Answer:** check whether the broker publishes *any* other channel — postal and
telephone are common, and both were offered here. Then put the exclusion in writing
and ask them to process by the available route. Quote any commitment in their own
reply: this one promised compliance *"within twenty-four (24) hours"* and said they
retain opt-outs to suppress future collection.

**Check the dropdown before assuming a form is usable.** A required field whose
options exclude you is a wall, not a nuisance — and it is invisible until you try to
submit. Worth recording in the playbook so the next person does not discover it the
hard way.

---

## 9. "Deleted" without saying how much, or for how long

A confirmation of deletion is not the same as an answer to *what* was deleted or
*whether it stays deleted*. Nuwber confirmed removal promptly and did not address
either follow-up:

- **How many records matched?** Someone with address history across several towns
  frequently has multiple records. Brokers create separate profiles when new source
  data cannot be matched to an existing one — Radaris says so explicitly in its FAQ.
  A single deletion may cover one of four.
- **Is it suppressed against future ingest, or merely deleted from the index?**
  This is the difference between settled and temporarily quiet. Deletion without
  suppression means the record returns with the next data feed.

**Ask both, every time.** They cost one sentence each and determine whether a
broker needs a recurring sweep. Expect the second to go unanswered more often than
not — which is itself informative, and a reason to re-verify rather than trust.

## Search-engine caches are not a failed removal

Several brokers warn that a delisted profile stays visible in Google or Bing for
days to **8 weeks**. Nuwber puts it plainly: *"we have no control or influence over
this process."*

So when verifying, **check the broker's own site, not a search engine**. A cached
result weeks later proves nothing. To clear it faster, use the search engines' own
removal tools rather than re-filing with the broker:

- Google: <https://support.google.com/websearch/answer/6349986>
- Bing: <https://www.bing.com/webmasters/tools/contentremoval>

---

## 10. "We don't accept requests by email" — sometimes answerable by email anyway

The most common refusal in this project, and it is worth one polite push rather
than immediate surrender. It is a *policy*, not a capability: the mailbox works,
a human is reading it, and the statutory duty attaches to the request, not to the
channel it arrived on.

A worked example. A lead broker replied:

> *"We don't accept deletion or opt-out requests sent to us by email. Please use
> one of the following methods..."*

listing six online forms. The forms had a required State dropdown that **did not
include the requester's state** — the prescribed route was structurally impossible
for them. The reply back said exactly that: the forms were attempted, here is the
field that excludes me, and the request stands. The next message was:

> *"Your info was not in our database. We added you to suppression file so your
> info will Not be able to enter our db in future either"*

Processed by email, by the same person who had said email was not accepted — and
the outcome was better than a deletion, because forward suppression stops the
record ever arriving.

**How to push back, in one short reply:**

1. Confirm you tried their route, and name the specific thing that blocked you.
   Vague complaints get form letters; a named broken field gets a human.
2. Note that the obligation follows the request, not the channel.
3. Restate the request compactly so it can be actioned without re-reading the
   thread.
4. Ask for **suppression**, not just deletion.

**When to stop pushing:** if their route genuinely works and merely inconveniences
you, use it. This is for routes that are broken, exclude you, or demand more
personal data than the request requires. Some brokers really do route email to an
unmonitored mailbox and mean it — a second refusal with no human on the other end
is your answer.

---

## 11. "We were acquired — file with the new owner" (and the cut-off date trap)

An auto-reply that redirects you to a parent or acquirer. Verbatim example:

> *"Andrews Wharton, Inc. is now a Stirista company. As such, privacy preferences
> and Data Subject Access Requests are now to be completed through stirista.com.
> Stirista holds the privacy preferences of our consumers in the highest regard
> and will honor any requests received by Andrews Wharton, Inc. prior to
> January 1, 2025"*

Read the last clause carefully. They undertake to honor requests received by the
old entity **before a cut-off date** — which means a request sent after it is
being declined, politely, in the same breath as the redirect. Treat the reply as a
**refusal plus a forwarding address**, not as a hand-off that has been actioned.

**What to do:**

1. **Re-file with the acquirer** — the original request is not carried over.
2. **Name both entities explicitly** and ask them to search records acquired from
   or previously operated by the old company. Merged data often keeps different
   record keys, so a search of the acquirer's own database may genuinely miss it.
3. **Quote the redirect back to them.** It is their own statement of
   responsibility and forecloses a second hand-off.
4. Mark the old entry as failed-with-a-successor rather than done, and add the
   successor to your list if it isn't there. One acquisition can silently strand a
   request that looks filed.

This is worth checking for proactively across any list built from public
registries: broker lists date quickly, and acquisitions are frequent.

---

## 12. "Send us the profile URL" — when the URL is unobtainable

A people-search site answers your request by asking you to identify the profile
yourself, in a strict format. Veripages, verbatim:

> *"NOTE: Please make sure that the URL you are copying and pasting into the form
> has the unique ending."*
>
> *CORRECT FORMAT: `https://veripages.com/profile/Tom-Lee/HTHQAoBB`*
> *wrong format: `https://veripages.com/name/Tom/Lee/`*
> *wrong format: `https://veripages.com/inner/profile/search?fname=Tom&lname=Lee`*

Reasonable-sounding, and often it is — a URL disambiguates you from everyone else
with your name. Three things can make it a wall:

1. **The required format is not exposed anywhere public.** On the site above, the
   search results contain only `/name/First/Last/` links — the format the email
   calls wrong. The "view all details" control does not resolve to a
   `/profile/<Name>/<ID>` address at all.
2. **Reaching the full profile raises a paywall.** A *"$1 – 7 day trial access"*
   modal appears before any detail is shown. The removal then depends on buying a
   subscription to the service you are trying to leave.
3. **A common name makes the search itself impractical.** One search for an
   ordinary first-and-last-name combination returned **214 individuals in a single
   state**, across 20 pages of results, with no age or date of birth on the cards
   to tell them apart.

Together these invert the burden: the broker holds the record and the index, and
asks the person with neither to perform the lookup.

**How to answer.** Don't refuse the format — show you tried, then hand the lookup
back with the reason it failed:

- State which cities/filters you searched and that no matching profile was found.
- Say plainly that the required URL format does not appear in their public search
  results, naming the format that *is* present.
- Note that the full-profile route raises a payment prompt, and that a statutory
  right should not be conditioned on a purchase. Keep this factual, not accusatory
  — it is usually an unconsidered side effect of the paywall, not a deliberate
  barrier.
- Offer three ways out, so the easiest one is still a win: process against the
  identifiers supplied; **send you** the profile URLs so you can submit them as
  asked; or confirm in writing that no matching records exist.

That third option matters — "we hold nothing about you" in writing is a complete
answer for a broker with no public listing to re-check.

**Verify before you submit a URL.** If you do find a candidate profile, confirm it
is actually you (DOB, prior cities, old phone numbers) before asking for removal.
Submitting a stranger's profile is a real risk with a common name, and it wastes
the one identifier the broker will act on.

---

## 13. Every route blocked — email refused, form broken, link expired

Occasionally a broker leaves no working path at all. Not by design, usually — just
neglect, each channel failing for a different reason:

- email refused as a matter of policy;
- the opt-out page behind a bot gate, with an emailed link that expires in 24
  hours;
- the alternative form accepting input and then failing server-side;
- the "delete" link deleting an *account* rather than the public record.

Each failure is individually plausible. Together they mean a statutory right has no
working channel.

**What to do.**

1. **Stop after two attempts at a failing form.** Every retry burns a solved
   CAPTCHA and tells you nothing new. Two failures establishes the endpoint is
   broken.
2. **Find the phone number in the legal notice, not the support email.** Opt-out
   telephone numbers are often published only in the body of a "Notice of Right to
   Opt-Out" and differ from the customer-service number. A call bypasses bot gates,
   broken forms and expiring links in one step. It is the most reliable route in
   this situation and the most overlooked.
3. **Write to the refused email address anyway, and document the failures.** Quote
   their own instruction, list each route with what it did, and ask them to process
   directly, escalate to whoever maintains the form, or name a working alternative.
   Offering three outs makes the easy one attractive. A refusal to accept email
   cannot reasonably stand when the prescribed alternative is broken — and the
   message is also your evidence that you tried, which matters if this ever
   escalates to a regulator.
4. **Record it as blocked, not submitted.** Nothing was filed.

**Do not** treat a broken form as a reason to give up on the broker. The failure is
evidence, and evidence is leverage.

---

## 14. The form that excludes your state

A request form gated on residency, listing only the states with comprehensive
consumer privacy statutes. One example restricts to sixteen: California, Colorado,
Connecticut, Delaware, Indiana, Iowa, Kentucky, Maryland, Montana, New Hampshire,
New Jersey, Oregon, Rhode Island, Tennessee, Utah, Virginia — plus "non-U.S.
resident" and "None of the above". **Choosing "None of the above" does not advance
past page one.** Combined with *"We cannot process your request until we have
received the completed form"*, a resident of any other state has no route at all.

Distinguish this from §6 (a required dropdown that simply omits your state, which
is usually carelessness). This version is **legally coherent**: those states grant
the right, others do not. That makes it harder to argue and changes the approach.

**Do not misstate your residency to get past the gate.** It is a false statement
on a request, it is often certified, and it hands the broker a clean reason to
void the request later — after you have stopped watching.

**What actually works instead:**

1. **Ask them to honor it as a matter of published policy.** Most privacy policies
   describe practices company-wide rather than per-state. A request framed as
   "your policy says you do X; I am asking you to do X" does not depend on a
   statute at all. Build this into the standard letter so it is already on record
   before the form turns you away.
2. **Check for a state data-broker registration.** Texas, California, Vermont and
   Oregon require brokers to register, and those regimes carry their own
   obligations regardless of where the consumer lives. If the company's own policy
   says *"The entity maintaining this website is a data broker under Texas law"*,
   cite it.
3. **Use the phone route if one exists.** Phone lines are frequently offered "for
   California consumers" but answered by a human who processes what they are given.
4. **Keep the paper trail.** A form that structurally excludes you, plus a refusal
   to accept email, is exactly the evidence a regulator complaint needs — and it is
   worth saying so, politely, in the request itself.

---

## 15. "We cannot locate a record matching what you provided"

The most common substantive reply from people-search sites, and the one most
likely to be mistaken for a clean "you are not listed". Verbatim, from two brands
in the same group on the same afternoon:

> *"We are unable to locate a full record that directly corresponds with the
> combination of the first name, last name, age, and/or address information you
> provided. If you have seen your name and information on [site], please provide a
> link to the page where you see your name and information, or provide the full
> name, age, cities and states under which your information is listed."*

**Read the rest of the message before concluding anything.** The same reply
continued:

> *"In the meantime, we have opted-out the other individual pieces of information
> that you provided to us: Email: ... Phone Number: ..."*

So the email addresses and the phone number **were** suppressed. The failure was
only on matching the *person* record. A reply like this is a partial success, not
a refusal, and the tracker entry should say which parts were actioned.

**Why the match fails.** These sites key person records on
`name + age + city/state`. A standard opt-out letter supplies name, current
address and email — which is not what the index is built on. Nothing is wrong with
the request; it simply does not contain the join key.

**What to send back:**

1. **Age, stated as a number.** Not just a date of birth — their operators search
   an age field. Do the arithmetic for them.
2. **A bare list of cities and states**, separate from the full postal addresses.
   That is the shape their search takes. Give both, formatted separately.
3. **Every prior address.** With a long address history, the record is very likely
   attached to a former one — the single likeliest reason the match failed.
4. **Every alias form of the name**, including middle name and initial.
5. **Ask how many records matched**, so a partial removal cannot pass as complete.

**On the profile-URL request:** you can decline without being obstructive. Say you
have not located the listing yourself and would rather not purchase a report to
exercise a privacy right, then point at the identifier combination that
distinguishes you — date of birth plus an unusual address in the history does most
of the work. See §12 for when the URL demand is a genuine wall rather than a
preference.

**Always ask whether the applied opt-out is a suppression**, not a one-time
removal. "We have opted-out these pieces of information" does not say which.

---

## 16. "Provide a signed authorization proving you may act on the consumer's behalf"

A first-party request answered as though it came from an **authorized agent**:

> *"With regard to your Right-to-Know request, we have not received sufficient
> written information to verify that you are duly authorized to act on the
> consumer's behalf. To proceed, please provide a viewable copy (e.g. PDF) of the
> consumer's signed authorization... A valid power of attorney may be submitted in
> lieu of a signed authorization."*

The demand is impossible to satisfy, because the document does not exist: you
cannot authorize yourself to act on your own behalf, and there is no principal for
a power of attorney to name. Left unanswered, the ticket closes for
non-compliance and the request quietly dies.

**Likely cause, worth heading off.** A letter that lists several email addresses
and then asks for correspondence at one of them can read like a third party
writing about somebody else — especially to an agent reading quickly. Anything
that separates "the person writing" from "the person the records concern"
invites this misreading.

**How to answer:** briefly and without irritation.

- State plainly: *I am not an authorized agent; I am the consumer.* Name yourself,
  and say the request concerns you.
- Explain the multiple addresses: **they are all mine**, listed so each can be
  searched, because records are often held against an address no longer in use.
- Ask them to **reclassify the ticket** as a consumer request submitted directly
  by the consumer, rather than simply resubmitting.
- Offer proportionate verification — confirming details they already hold, or
  replying from any listed address — while declining a government ID, which
  discloses more than the request itself warrants.

**Prevention:** say "I am the consumer, writing about my own personal information"
in the opening line of the original letter, and label the address list explicitly
as *my* addresses. One clause removes the ambiguity.

## 17. "Prove you are authorized to act on the consumer's behalf"

The request is first-party. The reply demands a signed authorization or a power
of attorney proving you may act for the consumer — that is, proving you are
yourself.

> *"we have not received sufficient written information to verify that you are
> duly authorized to act on the consumer's behalf... A valid power of attorney
> may be submitted in lieu of a signed authorization."*

**Do not comply.** The document being requested cannot exist: there is no
principal, so there is nobody to sign it. Supplying a notarised anything to prove
your own identity concedes the misclassification and adds a legal document to a
data broker's file — which is the opposite of the object of the exercise.

**It folds when answered.** At one broker the demand was withdrawn the same day
after a single reply, the ticket reclassified, and the request processed, with no
document supplied. Treat it as a triage default rather than a position: some
proportion of inbound privacy mail genuinely is from agents, and a template fires.

The reply that works has three parts:

1. State it plainly — *"I am not an authorized agent. I am the consumer."* Say it
   in the first line, not the fourth paragraph.
2. Explain the likely trigger. Listing several email addresses and nominating one
   for correspondence reads, to a clerk working from a template, like an agent
   writing for a client. Say why they are all listed: records are frequently held
   against details a person no longer uses, and having several email accounts is
   not agency.
3. Ask for a specific action — *"please reclassify the ticket as a consumer
   request submitted directly by the consumer"* — rather than arguing in general.

**Better still, pre-empt it.** Opening every letter with a first-party
declaration costs three lines and appears to prevent the misclassification
outright; it is now the first paragraph of the template in
`scripts/make_optout_email.py`.

## 18. The FCRA exemption, and the disclaimer that forecloses it

*We are a consumer reporting agency, this data is regulated under the FCRA, and
state deletion rights do not reach it.*

Before arguing the law, **read their own boilerplate.** Public-records and
background-check sites very often disclaim consumer-reporting-agency status in
their footers and terms, because that disclaimer serves a different commercial
purpose — it is how they avoid FCRA compliance obligations while selling
background information. One arrest-records operator volunteers it unprompted in
the signature block of every support email:

> *"[Company] and it's subsidiaries are not a consumer reporting agency as based
> on the Fair Credit Reporting Act..."*

A company cannot disclaim the status in order to escape the obligations and then
claim the status in order to escape a deletion request. Nobody inside the company
reconciles the two documents, so quote them back.

**Keep the artifact.** Boilerplate changes quietly, and a screenshot or raw
message dated before the refusal is worth considerably more than a link to a page
that has since been edited.

## 19. "Suppressed" is not "deleted" — and the difference has a clock on it

A large people-search operator answered a deletion request like this:

> *"This suppression request prevents those records from being displayed as
> required by applicable law on those sites, but does not delete or alter the
> underlying public record from its original source."*

This is not a deflection in the usual sense — it is candid, and more informative
than most replies. Treat it as a **partial success that needs one more question**,
not as a refusal and not as a completion.

The mechanism is straightforward once stated. The broker holds a copy of a public
record. Suppression hides their copy. The source is untouched, and the source will
be ingested again. So the only thing that determines whether this result is
permanent is whether the suppression **persists across refresh cycles** — whether
they keep a do-not-display list that is checked at every ingest, or whether they
simply removed a row that will come back.

**Ask, in these terms:** *does the suppression survive the next refresh of the
source data, or will the record re-display when that source is next ingested?*

A broker that keeps a persistent suppression list will say so, because it is a
better answer for them. A broker that cannot say so has told you to diarise a
re-check.

Two adjacent questions worth asking in the same message, because a "we have
processed your request" answers none of them:

- **Which policy basis was applied?** Where a request was submitted under a
  special policy (protected persons, minors) with an ordinary consumer request in
  the alternative, the two may differ in scope and durability.
- **Was an opt-out of sale or sharing applied separately?** Not displaying a
  record on a website and not selling it are different actions, and only the
  first is "suppression".

## 20. The jurisdictional reply that answers a question you did not ask

A UK or EU company holding US consumer data replies that you are not a UK or EU
data subject, so the GDPR does not apply to you.

That may well be correct. It is also **not an answer**. "You do not have the right
you did not claim" says nothing about whether your data still exists, and a thread
that ends there ends with the data intact and the request looking answered.

**Concede the point you were never making, then restate the real one.** In the
original letter, before they raise it:

> *"I am not claiming to be a UK or EU data subject, and I am not asserting rights
> under the UK GDPR on the basis of residence. However, if you process the personal
> data of US individuals — as any holder of the addresses above necessarily does —
> then the question is simply whether you will action a deletion request from the
> person concerned. I am asking you to do so, whether as a matter of law or of
> company policy, and to tell me in writing which basis you applied."*

One paragraph, and it removes the easiest exit. It also makes a refusal legible: a
company that declines *after* that framing has declined to delete, which is a
materially different thing to hold in writing than a disagreement about
jurisdiction — and a much better piece of evidence if it ever goes to a regulator.

The same shape works for the domestic version — *"your state has no comprehensive
privacy law"* — which is true of Pennsylvania and equally beside the point. Ask
them to honour it as company policy and to state which basis they applied. See §3.

## 21. "We only process this on behalf of our clients"

The processor-not-controller reply: we hold your data for our customers, so please
take it up with them.

Often technically true, and practically a dead end — **you do not know who the
customers are**, which is precisely why the exit works. This is standard at
visitor-identification, identity-resolution and data-enrichment businesses, where
the whole product is operated for somebody else's account.

**Ask for the client list in the same breath as the deletion**, so the answer is
useful whichever way it goes:

> *"If you hold this data on behalf of clients rather than for your own account,
> please tell me which clients, so that I can make the same request of them
> directly."*

A company that will not delete should at minimum name who can. Refusing both — we
cannot delete it and we will not say who holds it — is a much weaker position for
them to be in, and it is worth making them occupy it explicitly rather than
letting the first half stand alone.

Note also that a processor is generally obliged to **pass the request on** to the
controller. Asking them to do that, and to confirm they have, is a reasonable
request that costs them very little to grant.

## 22. "That is business data, not consumer data"

Offered by small-business data providers, B2B compilers and firmographic services.
It is half an answer, and the half it omits is the one that matters.

For a **sole proprietorship, a single-member LLC or a home-based business**, the
business record *is* a personal record. The contact name is a person's name, the
business address is a home address, the business telephone is a personal mobile.
And the modelled attributes hung off it — estimated revenue, transaction volume,
card activity, creditworthiness, stability and risk scores — are inferences about
one identifiable individual, whatever the schema calls the table.

**Do not argue the general point.** Ask the specific questions it implies, which
are answerable and awkward to dodge:

- *Do any of my personal identifiers appear in your business records as contact,
  owner, officer or principal details?*
- *Do you hold a record associating my name with a business? What does it
  contain?*
- *What modelled or estimated attributes are attached to that record?*

Then, if they still decline, **ask for the refusal in writing**. A dated "we
consider this business data and will not action your request" is worth having: it
is evidence, it fixes their position, and it is the thing a regulator complaint is
built from. An unanswered request is worth nothing, and from outside the two look
identical.

## A note on inviting the negative

Not a deflection, but it belongs beside them, because it converts the most common
non-outcome into a real one.

For any broker who may genuinely hold nothing — a diversified company, a B2B
service, a front site — say explicitly in the letter that a written negative is
welcome:

> *"If you hold nothing about me, I would welcome that in writing. A statement
> that no record exists is a real and useful answer and I will treat it as closing
> the matter. What I cannot use is silence, since an unanswered request and an
> empty database look identical from outside."*

This makes the cheapest possible reply the one you actually want. Without it,
"we have nothing" feels to the recipient like a non-answer not worth sending, and
silence becomes the path of least resistance — which is indistinguishable from
being ignored. With it, a two-line email closes the broker as `not_found`.

## 23. The mailbox name that does the deflecting for them

Not a reply at all — a deterrent placed before the request is ever sent.

One large advertising company's **only** published privacy contact is:

    FW_California_Consumers_CCPA_Data_Requests@...

A consumer in Pennsylvania reading that address has been told, without anyone
having to say it or defend it, that this channel is not for them. Most will not
write. No refusal was issued, no position was taken, and nothing exists to
complain about — which makes it more effective than an actual refusal and
completely invisible in any tally of requests received.

The same trick appears as a form that asks for your state before it will proceed,
a policy section headed "California residents", and a privacy page that describes
rights only under one statute.

**Write anyway, and address it in the first paragraph:**

> *"I am writing to this address because it is the channel you have provided, and
> I would ask you not to treat the name of the mailbox as the scope of your
> obligations or of your policy. If your position is that you will only action
> requests from residents of particular states, I ask you to tell me that in
> writing, and to state which basis you applied. I would also ask you to honour
> this request as a matter of company policy in any event."*

One paragraph, and it converts a silent deterrent into one of two useful things:
an actioned request, or a documented refusal that fixes their position and is
worth having.

**The principle, which recurs:** never let a scope *claim* do the work of a scope
*decision*. A mailbox name, a form's state dropdown and a policy heading are all
claims about who may ask. None of them is a decision about your particular
request, and only a decision can be appealed, quoted or complained about.

## 24. "That information is already public"

Offered by people-search sites, public-records aggregators, voter-file companies
and profile aggregators — the largest single category in this project.

It is usually **true**, and answering it as though it were false loses the
argument. Court filings, voter registrations, parcel records and social media
profiles are public. A private company cannot be asked to alter a county
assessor's database, and a request that appears to ask for that invites a refusal
which sounds entirely reasonable and then colours the rest of the reply.

**Concede the source; contest the compilation.** The reply that works:

> *"I am not asking you to alter a public record, which you could not do. I am
> asking you to delete **your** compiled record, your derived scores, and your
> association of that public data with the rest of my identifying information —
> which is within your control."*

The distinction is not rhetorical. A public filing and a commercial compilation are
different objects:

| The public source | What the broker made |
|---|---|
| A filing in a government database | A record joined to eight email addresses, twelve phone numbers, a date of birth and twenty-five years of address history |
| A voter registration | The same, plus modelled partisanship, turnout propensity and purchasing behaviour |
| Several public social profiles | One page keyed to a legal name, joining accounts, usernames, photographs, employer and location |
| A parcel record | A name-searchable page asserting who lives there |

In every row the second column is theirs, was created by them, and is the only
thing that was ever in question. **The harm is rarely that a record exists; it is
that typing a name into a search box returns it, joined to everything else.**

Two things that follow:

- **Ask for the association to be deleted**, in those words. It is grantable, and
  a broker who agrees has given you the thing that mattered.
- **Where the compilation includes derived data — scores, models, segments — name
  those separately.** Nothing about them is public, and they are the part least
  likely to be covered by a request the broker reads as being about public records.

## 25. The removal that requires you to become a customer

Some people-search sites route removals through a flow that requires an account, a
purchase, or a subscription — so exercising a deletion right means first entering
into a relationship with the company you are asking to forget you.

Sometimes this is deliberate. More often it is the site having only one identity
system, and removal being bolted onto it. Either way the effect is the same: a
proportion of people give up, and the ones who do not have handed over a payment
method and a verified account to a data broker in exchange for being deleted from
it.

**Refuse it in the first letter, before it is asked for.** One sentence:

> *"Please do not ask me to create an account, and please do not require a purchase
> or subscription in order to exercise a deletion right — I am asking you to stop
> holding my information, not to enter into a relationship with you."*

It costs nothing, it is usually unnecessary because most desks will simply process
the request, and where it *is* necessary the refusal is worth having in writing. A
company that will only delete your data if you buy something has said something
useful about itself, and it is the kind of statement a regulator complaint is built
on.

**The same applies to identity documents**, with an extra edge where the broker's
business is compiling exposed personal data: sending a passport or driving licence
to such a company is a poor trade, and saying so plainly makes the refusal a
position rather than an obstruction. Offer a proportionate alternative — replying
from a listed address, or confirming details they already hold — so the refusal
cannot be read as an unwillingness to verify at all.

## 26. The document demand that guards only the deletion

An automotive marketing company processed an **opt-out** straight from an email,
with no verification of any kind. The **deletion** was routed to a webform whose
*"Provide a copy of your utility bill"* field is **required** — the form cannot be
submitted without it.

**The asymmetry is the argument.** Both requests concern the same person and the
same records. If identity is established well enough to stop the company selling
your data, it is hard to say it is not established well enough to delete it. The
gap only makes sense if the document requirement is doing something other than
verification.

Three points to put back, in this order:

1. **It discloses more than the request removes.** A utility bill carries a full
   name, home address, account number, billing history and supplier. Asking a
   company to hold *less* of your information, by uploading a document containing
   *more* of it into a ticketing system, is a poor trade — and if that upload is
   ever breached, the harm exceeds anything the original record could cause.
2. **Their own handling proves it unnecessary.** Name the thing they already did
   without it.
3. **It is weak verification anyway.** A utility bill is not issued as an identity
   credential, is trivially forged, and proves an *address* rather than a *person*.
   Anyone able to obtain someone's post can produce one.

### Postscript: the document was not required after all

The company that produced this section sent an **email verification link** an hour
after the objection was sent — *"By clicking the link below you confirm the
verification of your identity"* — and the request was accepted with no document at
all.

So the required upload gated the **form** path only. The email path had its own,
weaker-on-paper and stronger-in-practice check: clicking a link proves control of
the mailbox, where a utility bill proves possession of a piece of paper.

**Two lessons.** A required field is the end of *that* route, not of every route —
look for the path you are already on. And stating the objection cost one message
and the document was never sent, which is a better outcome than either complying or
giving up.

**Then offer better verification rather than refusing outright**, so the refusal
cannot be read as unwillingness to be identified:

> *"I am happy to verify by any proportionate means: reply from or receive a code
> at any of the addresses I listed; confirm details you already hold — the
> addresses, telephone numbers or dates on whatever record you have; answer
> specific questions about that record."*

Each of those verifies you against **their** data rather than against a document,
which is the stronger test — a forged bill beats a document check, and nothing
forged beats being asked what is already in the file.

**Close by naming the three acceptable outcomes**: process it from the thread, name
an alternative step, or state in writing that no deletion happens without the
document. The third is a usable answer; an unresolved request is not.

## 27. "Your state has no privacy law" — take the other door

Three sibling brands refused the same statutory request within the same minute, in
near-identical words:

> *"it appears that the person identified in your request lives in a state that does
> not have a comprehensive consumer privacy law that applies to our data. Because of
> this, we are not able to process the request at this time."*

They offer an appeal, and then close it off again:

> *"Please note that replying directly to this email will not start an appeal and
> may not receive a response."*

**This is the hardest deflection in the project to argue with, because it is very
probably correct.** Pennsylvania has no comprehensive consumer privacy statute. An
appeal asking you to *"identify the specific law you believe applies"* is an
invitation to lose on the merits, and losing formally is worse than not filing --
it converts an open question into a documented refusal.

**So do not argue about jurisdiction. Go round it.**

Every one of these people-search sites runs a **self-service opt-out** that is
entirely separate from the statutory rights process, and that never asks what state
you live in:

  - a "Do Not Sell / Right to Opt-out" page,
  - or a "Privacy Request" / "Opt-Out Form" page,

reached from the site footer rather than from the privacy notice. Submit name and
email, click a link that arrives by email, complete a fuller form, and the record
comes off the site. No statute is cited anywhere in that flow, because it is offered
as a matter of policy rather than compliance.

**The general principle: a statutory refusal is a refusal of a statutory route, not
of the outcome.** When a company tells you the law does not reach them, stop asking
whether the law reaches them and start asking what they offer voluntarily. Those two
questions have different answers surprisingly often, and only one of them requires
you to win an argument.

**Keep the refusal, though.** It is a written admission that they hold data about a
named individual and have chosen not to act on a rights request -- useful context if
the state law changes, and useful evidence that the request was made and dated.

## 28. "Send us the URL" — and what happens when you refuse politely

Two companies on the same day answered a deletion request with a request of their
own: *"Please send us a link where your information appears."*

It reads as cooperative rather than obstructive, which is what makes it effective.
But it reverses who can see what, and the reply that works says so without accusing
anyone:

  1. **Name the asymmetry.** A consumer cannot enumerate what a company holds; the
     company can. That is why deletion is a right rather than a request.
  2. **Explain why the negative would be worthless.** If the consumer searches and
     finds nothing, that settles neither question -- the record may be unindexed,
     filed under a former address or disconnected number, or inside a licensed or
     syndicated product with no page of its own.
  3. **Resend every identifier**, so the request cannot be recharacterised as too
     vague to action.
  4. **Offer the benign reading.** If their removal tool genuinely takes a URL as
     input, that is a real constraint -- ask them to say so and point at the tool.

**It works.** One of the two came back having actually run the search, with
screenshots of the result and a written negative naming all four name variants. The
company went from asking the consumer to do the work to doing it themselves, in one
exchange, with no escalation and no legal threat.

**Tailor point 2 to the business.** The generic version is fine; the specific version
is much stronger:

  - *occupational licence data* -- records are keyed to a **licence number, issuing
    board or business address**, not to a person, so a name search misses them;
  - *business directories* -- listings are keyed to a **telephone number** and filed
    under a **trading name**, so the listing most likely to exist is precisely the one
    a self-search under a personal name cannot find;
  - *identity-resolution platforms* -- the record is a hashed email or device
    identifier and has no public page at all.

**And read the negative for its scope when it arrives.** "The search on our website
by your name and state does not reflect any records" is a real answer, but it is
bounded three ways -- their website, that name, that state. Record it with the
scope attached rather than as a blanket "no record", and ask the two follow-up
questions that close the gap: is the website the whole of what you hold, and is
anything indexed by something other than a name.

## 29. "Contact those sites directly" — the redirect that relocates the problem

Attached to an otherwise clean removal confirmation:

> *"If you continue to see your information online, please review the specific
> URLs of the profiles in question and contact those sites directly about their
> privacy policies and compliance."*

Nothing about this is dishonest, and for a genuinely unrelated site it is exactly
the right advice. It is worth noticing anyway, for two reasons.

**It answers a question nobody asked.** The request was about *their* index. The
reply is about everyone else's. That substitution is easy to miss because the
sentence is helpful in tone and arrives after a real confirmation — the reader is
already satisfied by the time they get to it.

**It cannot distinguish a stranger from a sibling.** "Those sites" covers three
very different things:

- a genuinely unrelated competitor — where the advice is correct;
- another property the same operator runs under a different name;
- a site that licenses or is supplied by the very index just cleaned.

From outside, all three look identical: a page with the same details on it. And
the removal just confirmed does not necessarily touch the second or third.

### What to do with it

Do not argue with the sentence — it is not wrong. Instead **ask the sibling
question directly and by name**, and treat silence on it as an open item rather
than a settled one:

> *"I asked whether [named site] is related to your operation, and the reply does
> not address it. I am not assuming a connection — a plain 'no relationship' is a
> complete answer and I will take it at face value."*

Naming a specific site matters. A general question about "any related properties"
invites a general answer. A specific one either gets a specific denial worth
recording, or gets no answer at all — and a conspicuous non-answer to a named
question is itself informative in a way that silence on a vague one is not.

The general principle, which recurs: **a confirmation that arrives bundled with
advice about somebody else has quietly changed the subject.** Take the
confirmation. Then put the subject back.

## 30. "You may remove one record" — the cap that bites hardest on the exposed

From a reverse-lookup site's opt-out FAQ:

> *"Currently, in order to prevent fraud and protect the integrity of our Do Not
> Sell My Info/Opt-Out process, we only permit you to remove one record from our
> People Search Results through our online Do Not Sell My Info/Opt-Out process."*

Taken alone this reads as a reasonable anti-abuse measure. It is placed several
screens below the opt-out itself, and the opt-out never mentions it.

What makes it a deflection rather than a limit is the paragraph immediately
above, in which the same FAQ explains how multiple records come to exist:

> *"there may be times when we receive a new record about you that is different
> enough from your existing record — for example, containing different spellings,
> initials, combinations of information, and/or addresses — that we cannot match
> this new record to your existing record. In these instances, a separate record
> may be created in our database."*

Put the two together and the cap is inverted from what it appears to be. The
people who generate several unmatched records are the people with long address
histories, several spellings of a name, initials on some records and a full
middle name on others — which is to say **the people with the most exposure and
the least ability to see it.** A person with one address and one spelling is
fully served by the online flow. A person with sixteen addresses removes one
record out of several and is told, accurately, that it succeeded.

### What to do

The FAQ that discloses the cap almost always names the way around it, because it
has to — here, *"please contact us and we will be happy to help you."* Take that
route in writing and make it do the work the form cannot:

- **Ask for every record matching any identifier**, and list them all. Do not ask
  them to "check for other records"; give them the list to match against.
- **Quote their own explanation of why several records exist.** It is the whole
  argument, and it is theirs.
- **Ask which services were searched**, by name. A cap on records often sits
  beside a scope limited to one product — see the sibling admission that a name
  "might appear in search results for the other search services... even after you
  opt-out of People Search."
- **Ask for suppression separately.** A site that invites you to contact them
  again each time a new record appears has told you there is no do-not-add list.
  Ask for one anyway, and record the answer either way.

The general rule: **when a self-service route announces a limit, the limit is the
route's answer to volume, not to abuse.** Read the FAQ before using the form; the
form will not tell you what it does not do.

## 31. The exception route that is the same queue

A reverse-lookup site's FAQ caps its online opt-out at one record and then names
the way around it:

> *"If you find more than one record about you in our People Search Results and
> would like to remove them all, please contact us at privacy@[broker].com and we
> will be happy to help you."*

That is a clear, published exception, and it was taken exactly as written: a
letter to the privacy address, quoting the FAQ, explaining that sixteen addresses
and five spellings of a name produce precisely the multiple records the FAQ had
just described.

**The reply came back from `support@`, under a new ticket number, byte-identical
to the general template — directing me to the one-record online process the FAQ
had told me to bypass.**

So the loop closes on itself: the automated route says *contact us for more*, and
contacting them says *use the automated route.* Anyone with more than one record
on the site is inside that loop, and nothing about it looks like a refusal. No one
has said no. The request simply never reaches anyone who can act on it.

### How to tell it is happening

- **The reply arrives from a different address than the one you wrote to.** That
  is the tell. If `privacy@` answers from `support@`, they are one queue with two
  labels, and the queue is answering on keyword rather than on content.
- **The template does not engage with any specific thing you said** — not the
  quoted FAQ, not the named exception, not the question that only a person can
  answer.
- **A new ticket number is issued** rather than the existing one continuing.

### What to do

Reply once, short, and make three moves:

1. **Name the loop and quote both halves** — their FAQ sending you to the address,
   and their reply sending you back. Written out plainly, it is obviously a
   defect, and it is the kind of defect a human reviewer will recognise.
2. **Point out the address mismatch** and ask directly whether the two are the
   same desk. If they are, say that the published exception does not exist in
   practice; if they are not, ask for the message to be passed to the other one.
3. **Ask one question the template cannot answer** — ideally a yes/no a system
   cannot fake, such as *can you place my identifiers on a do-not-add list so a
   matching record is never published?* Offer to accept "no" as a final answer.
   A template has no way to produce either answer, so a reply that engages at all
   proves a person is now reading.

Keep it short. The first letter was long and thorough and got a template; length
was not the problem, and repeating it will not help.

### A related own-goal worth avoiding

**Do not cc a support alias on a privacy letter.** It reliably opens a *second*
ticket, and the second ticket is the one that answers with a template — twice in
one night, at two unrelated companies. One letter to Outreach produced tickets
#657692 and #657693. Write to the privacy address alone, and follow up separately
if it goes quiet.

## 32. The form that cannot be submitted

A people-search site's support desk refuses privacy requests by email — *"We do
not process privacy requests received via email"* — and points at a **Privacy
Rights Form**. The form is three cascading dropdowns:

1. *I want to access, delete, or correct my personal information.*
2. Request type: *Right to Know / **Right to Delete** / Right to Correct*
3. My interactions with the company: *I have no direct relationship with the
   company / As a job applicant or employee / As a vendor...*

Answer all three and nothing appears. **No name field, no email field, no submit
button.** What appears instead is prose:

> *"Please note that state privacy laws... do not apply to all types of
> information. For instance, publicly available data is not included... Regarding
> your deletion request, while we cannot delete data held by third parties, you do
> have the option to prevent your information from appearing on our website."*

The funnel exists to deliver a refusal, dressed as a request process. Every
element of it — the title, the request-type selector, the careful relationship
taxonomy — implies that a request is being composed. None of it is.

### Why this is worth naming separately

It is not a refusal, and it will not be recorded as one. No ticket is opened, no
reference number is issued, nothing enters any queue. A person who works through
it has been *answered* without ever having *asked*, and there is nothing to
follow up, escalate, or point to later. Compare §31, the template loop: there at
least a ticket exists.

It also defeats the usual test for whether a route is real. The page loads, the
controls work, the selections register, the content is responsive to what you
chose. Everything behaves correctly. The only thing missing is the button, and a
missing button looks like a page that has not finished rendering.

### What to do

- **Take the answer as the substantive position and reply to it**, in writing, by
  whatever channel does exist. It is a stated refusal even if nothing recorded it
  as one — quote it back.
- **Use the route that does work**, however narrow. Here the opt-out achieves
  display suppression, which is less than deletion but is not nothing.
- **Press the claim the refusal rests on.** This one rests on
  *"retrieved from third-party data providers at the time you perform the
  search"* — so ask **who the providers are**. If the answer is real, the request
  belongs with them; if it is not, it contradicts their own opt-out page, which
  promises to *"remove all your information from our site"*.
- **Record it as a route that does not exist**, not as a request awaiting reply.
  Otherwise it sits in a tracker looking pending forever.

## 33. "Submit a separate request for each" — the arithmetic deflection

A consent-and-preference-management company's autoresponder, otherwise polite and
helpful:

> *"If you have multiple addresses or email addresses, please submit a separate
> request for each."*

Read on its own it sounds like ordinary hygiene — one identifier, one clean
record. Multiply it out and it is a wall.

A person with sixteen addresses and twelve email addresses is being asked for
**twenty-eight submissions**. And on this site a CAPTCHA gates the form *before
the fields are displayed* — the button reads "Verify & Continue to Form" — so it
is twenty-eight CAPTCHAs as well.

Nobody has refused anything. There is no exemption claimed, no jurisdiction
argument, no carve-out. The request is simply priced out of reach, and priced in
the one currency a data subject cannot delegate or automate: their own attention,
one CAPTCHA at a time. **And the cost scales with exposure** — the person with the
longest address history, who most needs the removal, pays the most to get it.

This is the same shape as §30 (the one-record cap), arriving from the other
direction. There the form did less than you needed; here it does exactly what you
need, N times.

### What to do

- **Keep the emailed request as the request of record.** A letter naming all
  twenty-eight identifiers at once is one request; it has already been received;
  and an autoresponder saying "we will respond in a timely manner" is not a
  refusal to handle it. Do not let the form's existence retire the letter.
- **Say the arithmetic out loud in the reply.** Twenty-eight submissions is a
  fact about their process, and stating it plainly — without complaint — is
  usually the first time anyone has.
- **Ask whether the form can accept multiple identifiers**, or whether a single
  written request can be processed as one. Both are cheap for them to say yes to.
- **If you use the form anyway, triage.** Current address plus the two or three
  live email addresses covers most real exposure. Do not grind through the
  historical list at one CAPTCHA each; the marginal value drops fast and the
  letter already carries them all.
- **Watch for a broken link in the same message.** This one's autoresponder
  pointed at a `site.` subdomain that 404'd onto a hosted knowledge base; the
  working page was the same path on `www`. An automated reply is written once and
  then sent for years, so it is exactly where a stale URL survives longest —
  **always load the link before following its instructions.**
