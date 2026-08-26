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

## 34. "Here are the steps to use our form" — when email would have done it

A large people-search operator answered a detailed request with polite,
step-by-step instructions for its self-service opt-out: find your profile, copy
the URL, paste it here, confirm by email. Nothing about it was obstructive. It
also answered none of the questions asked.

Pressed once — the same questions restated, plus one drawn from the operator's
own FAQ — the second reply said:

> *"Based on the information you provided, we located matching records and have
> removed them."*

**The form was never necessary.** They could search the identifiers in the letter
all along, and doing so was strictly better than the route they had recommended:

| Self-service form | Email with identifiers |
|---|---|
| One profile per submitted URL | All matching records in one pass |
| Subject must identify their own record among strangers sharing the name | Broker matches on identifiers they hold |
| Wrong URL removes someone else's listing | No such risk |
| No opportunity to ask anything | Questions can travel with the request |

### Why this is a deflection and not merely unhelpful

It moves the work — and the *risk* — from the party with the data to the party
without it. The broker knows which records match; the consumer is guessing from a
list. And it silently narrows the request: a form that takes one URL cannot carry
a suppression request, a sources question, or a scope question, so everything
except "remove this one page" is dropped without anyone saying no.

### What to do

- **Ask explicitly whether they can action the request from the identifiers
  supplied**, rather than assuming the recommended route is the only one. The
  phrasing that worked: *"please treat this email as a request covering all of
  them, and use the identifiers in my previous message rather than making me
  submit a link for each."*
- **Restate the unanswered questions rather than dropping them.** A first reply
  that ignores every question is not a refusal; it is frequently a support agent
  sending the standard article. The second pass often reaches someone who reads.
- **Do work the form as well if it is cheap** — but do not let its existence
  retire the letter, and never guess at a profile URL.
- **Say thank you when the second reply is good.** This one named the predecessor
  company unprompted. Operators who engage are worth engaging with; the tone of
  the follow-up is part of why the third reply arrives at all.

---

## §35 "We are a B2B tool, so this is not personal information"

From a lead-generation vendor, in a personal reply from the founder:

> "We don't aggregate any data, buy lists, and are not a data broker. This is a
> B2B tool to capture businesses publicly available information and is not allowed
> to capture private information on consumers."

Nothing there is implausible, and arguing about the label "data broker" is a waste
of everyone's afternoon. The move to answer is the quiet slide in the middle:
**"business information" is treated as equivalent to "not personal
information."** They are different categories.

> **A B2B contact record is nearly always a named human being** — a person's name,
> work email, direct line, title, employer. Each is personal information *about
> that person*. "It is business data" describes the context of collection, not the
> legal category.

And the fact most of the industry has not absorbed: **California's
business-to-business carve-out sunset on 1 January 2023 and was not renewed.**
Since then a work address in a prospecting database sits in the same category as a
home address in a people-search database.

### How to reply so that you get a search instead of an argument

Do not contest the label. Collapse the whole thing to one question a lookup can
settle:

> Do you hold a record — in the product, in a CRM, in an enrichment cache, or in a
> suppression list — keyed to my name, to any of these email addresses, or to any
> of these telephone numbers?

Then hand them the cheap exit explicitly: *an unqualified "we searched those
identifiers and hold nothing" is a complete answer and closes this.*

> **Offer the null result as a win.** A company that genuinely holds nothing will
> put it in writing gladly, because writing it ends the correspondence. A company
> that will not put it in writing has told you something without meaning to.

Pair this with the standing ask: if the answer is yes, delete *and suppress*,
regardless of whether the source was public or the record commercial. A
professional record is still a record about a person.

---

## §36 The self-service tool that searches a different index than the product

Customer care answers a detailed privacy letter with a link and a friendly
instruction to search for yourself and click **Proceed to Opt Out**. The tool
works. You search. It says **"no exact match"**. Case closed?

Not necessarily — and this is subtler than the usual form deflection, because
nobody is being evasive.

> **Check what the opt-out tool searches against what the product sells.** One
> reverse-*phone* service offers an opt-out that searches by **first and last
> name**. Those are not the same index. A number-keyed record — including
> disconnected and reassigned numbers, which may sit attached to a stale name
> string, a carrier record, or no name at all — is simply not reachable from a
> name box.

So a person searches, reads "no exact match", concludes they are absent, and stays
in the phone index under a number they gave up twenty years ago.

**Record the negative, but do not record it as absence.** Keep the entry at
`submitted` with the clean search noted, not `not_found`. The negative is real and
worth having; it just answers a narrower question than the one asked.

**What to put back to them:**

1. Does a name opt-out clear the number-keyed records, or only the profile?
2. Search the identifiers the form cannot take — supply them in the reply and ask
   for a **count** of matches. Zero, stated unqualified, closes it.
3. Remove the association in **both directions**; clearing one leaves the fact
   retrievable from the other side, and no confirmation says which was done.
4. Remove the **enrichment** too, and any appearance as a "related person" on
   somebody else's page — a relative-graph entry is a record about you living on a
   page that is not yours, and searching your own name will never surface it.

### Two things to do before replying at all

**Read the opt-out page's own footer.** It published `privacy@<domain>` twice, on
the very page support sent as the answer. That is a different queue from the one
that wrote to you.

**Do not click the button next to a stranger.** The results page offered ~100
same-name records, each with a live one-click opt-out beside somebody's date of
birth, relatives and address history, and asked for no proof of identity at all.
Suppressing a record you have not positively identified is acting on a third
party's data without their knowledge.

### And check whether you are being answered twice by one company

Two brands sent the *identical* support template on the same day — same greeting,
same "If you are having trouble with the online process" paragraph. That is
[[_BROKER_FAMILIES]] signal 7. Put the questions to the family once rather than
per brand, and ask them to confirm the scope covers every property they operate.

---

## §37 Replacing the argument with a query

Not a deflection so much as the technique that dissolves a whole class of them —
the category refusals in §35, "we are not a data broker", "we are not a CRA", "that
is business data", "we are a processor not a controller".

Every one of those invites a legal argument. The argument is winnable and it is
almost always the wrong move: you are asking a person to concede a position their
company has taken publicly, in writing, to a stranger. Even when they privately
agree, saying so costs them something. So they restate the position, and the thread
dies at exchange two.

> **Give them a question a database can answer instead of a position to defend.**
> "Are you a data broker?" is a claim about identity. "Does a row exist keyed to
> any of these identifiers, in the product, a CRM, an enrichment cache or a
> suppression list?" is a lookup. The second costs one query and concedes nothing.

Then make saying no cheap, explicitly:

> *If the answer is no, say so plainly and we are done. An unqualified "we searched
> those identifiers and hold nothing" is a complete answer, I will record it as
> such, and I will not write to you again.*

That sentence is doing the real work. It converts the reply from a commitment into
an exit. A company that holds nothing will take an exit gladly; a company that will
not put "no" in writing has told you something it did not mean to.

**Then keep the promise.** Close out with a short thank-you and stop. It costs
nothing, and it is the only reason the next person who writes to that company gets a
straight answer rather than a form letter.

Worked verbatim this week on a lead-generation vendor whose first reply was the full
category refusal. The second reply, same day, was three words: *"Simple Answer: No."*

**Two things to keep in mind.**

- **Ask about every store, not just the product.** "In the product, in a CRM, in an
  enrichment cache, or in a suppression list" is deliberate — the first "no" people
  give is usually about the customer-facing product only.
- **A null result is a result.** Record it as `not_found`, not as an unanswered
  request, and keep the thread: if the name surfaces there later, that one line is
  what a follow-up cites.

---

## §38 "We require your LinkedIn URL"

Two workforce/talent-intelligence datasets asked for exactly this, a day apart, in
almost identical words:

> "To ensure we identify the correct record in our database, we require your
> LinkedIn URL."

Once is a request. Twice, from two unrelated companies in the same category, is a
**category pattern** — and worth having a settled answer to.

### The need is real; the token is wrong

Do not treat it as a stalling tactic. A common surname against an
employment-keyed dataset genuinely is ambiguous, and the CPRA does contemplate
requesting further information where identity is in doubt. Conceding that up front
is what makes the rest of the reply land.

But refuse the specific artifact, for three reasons worth stating:

> **1. A LinkedIn URL is an enrichment key, not a verification token.** It is
> live, third-party and continuously updated. Handing it to a talent-intelligence
> company *in order to have data deleted* supplies exactly the linkage being
> objected to — and unlike a verification factor, it stays useful to them after
> the request closes. A verification factor should prove who you are and then be
> discarded; this one improves the record.

**2. The statute is qualified.** Additional information may be requested where
*necessary* to verify, and a business should not collect more personal information
than that purpose requires, preferring a less intrusive route where one exists.

**3. They already hold a better identifier.** For a workforce dataset the join key
is email — and specifically an old one:

> **A `.edu` address in an institutional format is the strongest disambiguator you
> already own.** It ties one person to one institution, it is what an
> academic or early-career profile was sourced against, and unlike a name it does
> not collide.

### The reply that keeps it moving

Ask them to run the email addresses first. Then offer a fallback that achieves the
same disambiguation without a live identifier — **the names of the last three
employers** — conditional on three written terms:

  a. used **solely** to locate and delete, never to enrich, including if nothing is
     found;
  b. **deleted** if the search finds nothing — not retained as a suppression key or
     a "requested but not found" log row; and
  c. the request still processed as a **deletion and opt-out**, not silently
     converted into an access-only request by the verification step.

> **(b) is the one that matters. The standard failure mode is that a company
> holding no record about a person ends up holding one *because they asked for
> identification* — the request itself becomes the data.**

### And keep the jurisdiction-independent questions alive

Verification detours quietly reset a thread: the substantive questions stop being
answered while everyone argues about identity. None of these depend on it, so
re-ask them in the same message:

- **Inferred demographics** — gender, ethnicity, veteran or disability status.
  Diversity filtering is a *marketed feature* of this category, which makes this a
  concrete question rather than a hypothetical, and an inferred protected
  characteristic attached to a name is sensitive data generated without the
  subject's knowledge.
- **Sources** of the underlying records.
- Whether **customers who already exported a profile** must delete it.
- Whether a **standing do-not-source entry** is possible — sourcing here is
  continuous, so without one a deletion is a pause.

### Outcome: it worked, and it worked without surrendering anything

A day later Revelio Labs replied:

> "Please find the raw data we hold attached."

Four CSV files. **No LinkedIn URL was supplied. No employment history was
supplied.** They ran the twelve email addresses, found the record, and sent it.

The whole of the argument was two moves, and it is worth being precise about
which did the work:

1. **The statutory point, stated narrowly.** The CPRA does let a business request
   additional information where identity is genuinely in doubt — the demand was
   not unreasonable, and the reply said so out loud. But the provision is
   qualified: the information must be *necessary* to verify, and the business is
   meant not to collect more personal information than the purpose requires.
   Where a less intrusive route would identify the record, that is the route the
   statute prefers.
2. **Supplying the less intrusive route, concretely.** Not "you should try
   harder" but *here is the join key*: twelve addresses already in their
   possession, with a specific argument for one of them — a `.edu` address in a
   university's standard format. For a workforce dataset built partly from
   academic and early-career profiles, that address is both far more likely to be
   the key and far less likely to collide with a different person of the same
   name than current webmail is.

The second move is the one that mattered. A proportionality objection with
nothing behind it is just a refusal to verify, and a company is right to hold
firm against it. A proportionality objection **that hands over a better
identifier than the one being demanded** leaves nothing to argue about — it is
cheaper for them to run the search than to reply.

**Concede the reasonable part first, and mean it.** The reply opened by saying
the demand was reasonable in kind and would not be treated as a stalling tactic.
That is not politeness for its own sake; it is what makes the narrow objection
land as a narrow objection rather than as the usual noise.

**Say why the LinkedIn URL specifically is different**, and separate it from the
employer question rather than refusing both as one:

> A LinkedIn profile URL is not a verification token. It is a live, third-party,
> continuously-updated identifier that would let you join my request to a public
> profile and enrich from it — which is, with respect, adjacent to what your
> product does. Handing it over in order to have data deleted risks supplying
> exactly the linkage I am asking you to remove.

**Offer the fallback genuinely, with conditions.** The reply agreed to supply
employer names if the email search came back empty, subject to (a), (b) and (c)
above. Offering it made the refusal credible — this was not someone looking for a
reason not to verify — and in the event it never had to be honoured.

**One thing to do differently.** Ask for the schema with the data. The export
arrived as `data_1.csv` through `data_4.csv` with no column dictionary. For a
workforce record the entire question is which fields are *sourced* and which are
*modelled* — estimated compensation, inferred seniority, inferred demographics —
and a raw table does not distinguish them. Request the description of what each
column represents in the same message that requests the disclosure.

**And disclosure is not deletion.** The original letter asked for disclosure
*then* deletion; a company that sends the data has answered the first half. Reply
promptly asking them to proceed with the deletion, the opt-out, and the standing
do-not-source entry, and re-ask the questions above — they are still unanswered,
and the export does not answer them.

---

## §39 The voluntary opt-out that beats the statutory one

A broker's autoreply refused an emailed request — *"your request was not submitted
in the manner required by our Product & Services Privacy Policy"* — and then
offered **two** routes:

> "Consumers, **regardless of their state of residence**, may opt-out of our
> database at any time and at no cost via our website… Exercising this opt-out
> right will prevent [us] from selling your personal information, processing your
> personal information for targeted advertising or profiling, and will result in
> the **removal of your personal information from [our] database**."

> "Residents of **certain other states** may also submit deletion/correction
> requests via our website at /deletion-form and a right to know/access request at
> /access-form."

The instinct is to reach for the second one: it says *deletion*, it cites statutory
rights, it looks like the real thing. For a resident of a state without a
comprehensive privacy law, that instinct is exactly wrong.

> **A statutory form is gated on residency and scoped to the statute. A voluntary
> company-wide opt-out can be broader, and is often open to people the statute does
> not cover.** Read the voluntary route before assuming it is the weaker one.

Here the voluntary route delivers sale, targeted advertising, profiling *and*
database removal, to anyone. The statutory route delivers deletion to residents of
covered states — which, for Pennsylvania, is nobody.

**Two practical consequences:**

- **When both exist, use the voluntary one first**, then file the statutory one as
  well if you qualify. They are not alternatives.
- **Keep the autoreply.** The commitment lives in that message, not on the form.
  "Regardless of their state of residence… removal of your personal information
  from our database" is a quotable promise, and the form itself says none of it.

**And the wider lesson about routing refusals.** This one was technically a
rejection — the request was refused for arriving in the wrong channel. But it was
the most useful rejection of the day, because it described the business ("data-
driven marketing… existing and prospective donors and customers"), named three
routes, and stated what each one does.

> **Read a "wrong channel" refusal for what it discloses, not just for what it
> declines.** An autoresponder written to deflect still has to explain where to go,
> and that explanation is frequently the clearest account of the company's data
> practices you will get.

## §40 The confirmation scoped to one hostname when you asked about sixteen

Four sites on the `optOutLight` platform answered a single letter — one letter,
addressed to nine mailboxes, arguing that they are one operator and asking to be
treated as covering all sixteen — within eight minutes of each other. Each reply
was byte-identical to the others apart from two substitutions:

> "From the information you provided, we have removed your information from our
> database at https://www.**\<this brand\>**"

Read that carefully, because it is a good outcome and an incomplete one at the
same time. It **is** a removal, and it is unqualified, and it needed no form and
no account. It is also **scoped, silently, back down to one hostname** — the
request to treat the letter as covering all sixteen went unacknowledged, not
refused. The reply does not say "we only handle this brand." It says nothing.

The template's second half is the part to notice:

> "If your name still appears in our listings, it is possible we were unable to
> distinguish your listing across multiple similar listings... or your browser
> cache contains stale data... you may clear your cache, or try your search in a
> few days when your cache has recycled stale data."

Both explanations put the residual listing on your side of the line — an
ambiguity you failed to resolve for them, or your own browser lying to you. Both
are sometimes true. Neither is checkable by the person receiving the email, and
between them they pre-absorb every complaint you could make about an incomplete
removal.

**How to answer.** Not by arguing about scope, which invites a "we are separate
companies" answer nobody can disprove. Do two things instead:

1. **Verify from outside the browser they blamed.** Re-run the search with a
   cold fetch, not a reload — no cookies, no cache — so that the cache
   explanation is off the table before you write again. If it is gone, the
   removal was real and you owe them nothing further.
2. **Convert the unanswered scope question into a per-brand fact.** Do not ask
   "are you the same company?" Ask, of each brand that has not replied: *"Was
   this site actioned by the removal you confirmed on \<brand that did reply\>,
   yes or no?"* A database can answer that. Corporate structure cannot be
   answered by a support agent, and asking for it gives them a reason to escalate
   to somebody who will say less.

**And keep the confirmations.** Each one is a precedent to quote at the next
sibling — the single most effective lever found so far. A sibling's granted
request is not an argument they can rebut; it is something their own colleague
already did, for the same person, on the same platform.

**Related:** §36 (the self-service tool that searches a different index),
§37 (replacing the argument with a query), and `_BROKER_FAMILIES.md` on citing
one sibling's granted request to the rest.

## §41 "We do not hold clear text email" — said by a portal whose lookup key is your email

Tapad's autoresponse states plainly:

> "we do not collect or hold any of the following information: name, clear text
> email, phone number, address, any government-issued number or ID, or precise
> location information."

Read alone, that sounds like "we have nothing of yours." Then their own request
portal asks for an email address as the lookup key, and explains why that is
consistent:

> "we only collect encrypted emails and do not retain any emails in clear text
> form. The email address you provide will only be used for the purpose of
> processing your request"

Both statements are true. Together they *concede the point*, and the useful move
is to say so rather than to accuse anyone of contradicting themselves.

**The argument, in one sentence.** If a clear-text address typed into a box
deterministically finds your record, the stored hash is functioning as a stable
identifier for you — hashing changes the storage format, not what the key
resolves to, because the input space of email addresses is small, known and
enumerable. A company that builds its own rights portal on "type your address
and we will find you" has already assumed this; you are only asking them to
apply the same assumption to the definition of personal information.

Say it *with* them, not at them. "I am not treating that as a contradiction — I
think it is an accurate description of a hashed-email keyspace, and I am glad it
is stated plainly. But it settles the point my letter was making." A concession
offered generously is much harder to walk back than one extracted.

**The second half is where the real answer lives.** The same portal disclosed
something the autoresponse did not:

> "whenever an ID... is opted out it will be opted out in perpetuity and we will
> automatically remove any other IDs that Tapad determines to be associated or
> related to that ID for sixty (60) days. If those related IDs have not been
> opted out during the sixty (60) day period, those IDs will follow our standard
> data ingress rules."

The node is permanent; **the cluster is temporary**. In an identity business the
cluster is the product, so a removal with a sixty-day cascade window deletes one
node from a graph that reassembles around it. Turn that into the §37 shape — a
question a database can answer, with a stated exit:

> "After day sixty, does the linkage between the remaining members of that
> cluster still exist — yes or no? If yes, tell me which request type dissolves
> it. If no, I will record this as complete and not write again."

**The general lesson.** Read the *portal*, not only the autoresponse. The
autoresponse is written by the privacy team to close a ticket; the portal is
written by the engineers to describe what the system does, and it routinely
discloses the limitation the autoresponse omits. The material for the strongest
follow-up is usually sitting on the page they just directed you to.

**Related:** §35 (B2B tool, so not personal information), §37 (replacing the
argument with a query), and `_SILENT_FAILURES.md` on point-in-time vs standing
suppression.

## §42 "Thanks for the AI response. Binned."

The most efficient rejection received so far, and it had nothing to do with the
law, the scope, or the facts. ViewDNS answered a carefully-argued follow-up with
one line:

> "Thanks for the AI response. Binned. Have a nice day."

He was not wrong. The letter was ~700 words, opened with a bolded section
header, ran a quoted block, a numbered structure and a blockquoted question, and
closed with a bolded "one observation, offered as feedback rather than an
accusation." Every one of those choices was deliberate and each is defensible on
its own. Together they produce a document that looks like a template, and a
template is what a mass mailing looks like.

**This is a distinct failure mode and it deserves its own section**, because
nothing in the *content* was wrong. The first reply from the same person had
been substantive and correct. What ended the exchange was the register.

**Match the letter to the reader.** This is the actual lesson, and it cuts
against a habit that has otherwise worked well:

| reader | what works |
|---|---|
| a compliance desk at a large firm | structure helps — numbered asks, headers, statutory citations. It gets routed, logged and answered by process. Length is not a cost. |
| a one-person operation reading their own mail | structure is the cost. Bold text, headers and numbered asks read as bulk. One question in plain sentences gets an answer; a well-organised page gets binned. |

Before writing, ask which one you are writing to. A `privacy@` address behind a
ticketing system is the first. A named individual replying personally within
half an hour from a small technical site is emphatically the second, and the
second letter should have been three sentences.

**Concrete markers to strip when writing to a person rather than a desk:**
bold; section headings; blockquotes; numbered or lettered ask-lists; the
"I would like each confirmed separately" construction; em dashes; any sentence
that announces what the next paragraph will do. Keep: what you want, why you are
asking them specifically, and an explicit way to end the exchange.

**How to answer the accusation itself.** Do not argue about whether it was
machine-written. Concede the criticism, say plainly what you are doing and why
the tone came out that way, compress the request to one line, and offer to
accept silence as an answer. Then keep that promise. The reply that follows this
section did that in about 130 words with no formatting at all.

**And do not send a second one.** "Binned" is a termination. One short,
plain-language note that owns the criticism is defensible; a third message is
the behaviour he was objecting to.

**Related:** §37 (replacing the argument with a query — still right, but the
query has to arrive in a form a human will read), §40.

---

## §43 The rights form only an employee of some company can complete

DemandScience's rights portal is a real form, hosted by PrivacyEngine, reachable,
functional, and it submits. It asks a consumer exercising a consumer right for:

- **Business Email Address** (required)
- **What is the name of the company you work for?** (required)
- **Requester Business Phone** (required)
- **Data Subject Business Phone** (required)
- **Category of Data Subject** (required), whose complete option list is:
  Current Employees · Former Employees · Job Candidates · Shift Workers ·
  Customers · Suppliers · Students · USA

Read that last list again. It enumerates every category of person a company has a
*relationship* with. The one category it omits is the one that describes almost
everyone a data broker holds records about: **a member of the public, whose
information was compiled without any relationship existing at all.** ("USA" is
not a category of data subject; it is a stray row someone left in the config.)

**This is not a refusal, and it is important not to treat it as one.** Nobody
decided to exclude consumers. The form is a generic GDPR data-subject-request
template, built for an organisation fielding requests from its own staff,
applicants and customers, deployed unchanged at a company whose entire product is
records about strangers. The mismatch is structural, not hostile — and it is
worse than hostile, because there is no one to argue with.

**What it does to the requester.** Every mandatory field is answerable only by
someone acting in a corporate capacity. A private individual has no business
email in this context, no employer relevant to the request, and no honest choice
in the dropdown. The form will not submit until they misrepresent themselves.
That is a rights mechanism that works for everyone except the people the statute
was written for.

**How to fill it without lying.** Complete it, and put the disclaimer *inside the
submission* so the record carries it:

- Business email → the personal address. It is the address they must reply to.
- Employer → `Not applicable - I am a consumer, not a business contact`
- Category → pick the least-wrong option, then say so explicitly in the free text:

> This field is mandatory and its only options are Current Employees, Former
> Employees, Job Candidates, Shift Workers, Customers, Suppliers, Students, and
> "USA". None of those describes me. I have never been an employee, candidate,
> customer, supplier or student of yours. I am a member of the public whose
> personal information was compiled without any relationship between us, which is
> the ordinary situation for a data broker's records and is not offered as a
> choice. I have selected "Customers" only because the form will not submit
> without a selection, and I am stating here explicitly that it is not accurate so
> that it is not later read as an admission of a commercial relationship.

The last clause is the one that matters. A dropdown selection is an assertion,
and it persists in their ticketing system long after the free text is skimmed.
Disclaim it in the same submission or it stands unopposed.

**On the business-email demand specifically**, one sentence is enough and it is
worth including because it is both true and load-bearing:

> California's business-to-business carve-out sunset on 1 January 2023, so a
> business contact record is personal information on the same footing as a
> consumer one, and a rights form that can only be completed by someone with a
> corporate email excludes exactly the people the statute covers.

**The related, milder version: no route at all.** Windfall's privacy policy
publishes no privacy contact address and offers, as its only opt-out mechanism,
links to the DAA, NAI and Google Analytics industry tools. Those govern
advertising cookies in a browser. They do not touch a compiled consumer record,
and they are not a mechanism for deletion, access, or opt-out of sale. Pointing
at them is not a rights route; it is a rights-shaped object in the place where
the route should be. Say that plainly, write to a guessed `privacy@` anyway, and
note the absence — a bounce and a silence are different findings, and both are
worth recording.

**The general shape.** Both cases are the same failure wearing different clothes:
**a compliance artifact built for a population that does not include you.** The
portal, the dropdown, the industry opt-out link — each is genuine, each was
adopted in good faith, and each answers a question nobody in your position asked.
Do not argue with it. Complete it, disclaim what is inaccurate, and put the
structural problem in writing where a human will read it.

**Related:** §17, §24, §41, and §71 in `_SILENT_FAILURES.md`.

---

## §44 "Can you verify if it would be under a different email address or format?"

LeadIQ, a B2B prospecting database, searched the eight personal email addresses
in the request and came back with:

> "We're unable to locate any data connected to this email/s. Can you verify if
> it would be under a different email address or format? We can also search
> under your LinkedIn profile URL."

Both halves of that sentence look cooperative. Both are unanswerable, and for
different reasons.

**Part one: they are asking you to guess an identifier their system generated.**

A prospecting database's index key is a *work* email address, and a large share
of those are not addresses the person ever chose. They are constructed from a
pattern — `first.last@`, `flast@`, `f.last@` — inferred from other employees at
the same domain, or captured from a signature block by a customer's browser
extension. So "which format is it under" is asking the consumer to reproduce an
identifier the broker manufactured. There is no way to know whether they hold
`first.last@`, `flast@`, `f.last@`, or nothing.

This is the same structural shape as the MAID problem (see the identity-graph
notes): the requester cannot look up an identifier that was never disclosed to
them. It is not evasion — the agent asking is being genuinely helpful within a
workflow that assumes you know your own record — but it converts an obligation
into a puzzle only the broker has the pieces to.

**Do not guess formats.** Listing plausible permutations invites a search on
addresses that may belong to a different person entirely with the same name, and
a hit on one of those is worse than a miss.

**Part two: do not hand a prospecting database your LinkedIn URL.** §38 covers
this as a verification demand. Here it is offered as a *search convenience*,
which is softer and more dangerous, because there is no adversarial framing to
put you on guard.

A profile URL is a stable, globally unique, employer-linked key. Supplying one to
a contact database supplies an identifier it may not currently hold, together
with a link between it and every email address, phone number and postal address
in the request. If there is genuinely no record, that search does not test for a
match — it assembles one. The enrichment risk is not hypothetical: the join is
the product.

Under the CPRA, information used to verify or locate a record must be necessary
and proportionate to the request. A profile URL is not the least intrusive way to
find a contact record; it is the most productive way to build one.

**What to offer instead.** Redirect to keys that are already in their possession
or already in your letter, and that are keyed to the person rather than the
employer:

- **Telephone numbers first.** For a B2B contact database this is the highest-
  value field and the most person-shaped one. A direct dial or personal mobile
  follows someone between jobs, and it is the field that actually produces the
  calls. Ask them to search the numbers specifically.
- **Name variants**, which are what their matching engine uses anyway.
- The `.edu` or other institutional address, if you have one — see §38, where
  handing over a *better* identifier than the one demanded is what dislodged the
  request.

**The ask that survives a null result.** This is the part worth keeping whatever
the search returns:

> If you hold nothing today, please still add my name, telephone numbers and
> email addresses to a permanent do-not-add suppression entry, so a future ingest
> from an upstream supplier cannot create a record I would have to find all over
> again.

A prospecting database is continuously rebuilt from suppliers. "No record today"
has a short shelf life; a suppression entry does not. Cite a broker that already
does this — SourceIT holds SHA-1/SHA-256 hashes of addresses purely to prevent
re-adding, holding suppression while holding no record. Naming another company's
practice moves the conversation from "will you do me a favour" to "this is
normal", which is the most reliable lever in this whole file.

**And ask who supplies them.** If the record is going to arrive eventually, the
supplier is the better target. See the SourceIT exchange in §74 of
`_SILENT_FAILURES.md` — asking a reseller to name its sources surfaced a
250-million-record broker that appeared in no list.

#### Confirmed from the inside (2026-08-24)

The structural claim in this section — that a B2B database's work email addresses
are frequently *manufactured* rather than observed, so the consumer cannot supply
one — no longer has to be argued. **Kaspr said it outright**, unprompted, when
disclosing what they held:

> *"Kaspr Research refers to the fact that the email was generated by our own
> internal tool based on your work experience."*

They listed a business email address alongside a source label of "Kaspr
Research", and then explained that the label means the address was generated
from employment history rather than collected.

**Quote this when a prospecting database asks which email format to search.** It
is a competitor of theirs describing the practice in its own words, which is far
harder to wave away than a consumer's inference. The follow-up that lands:

> One of your competitors told me plainly that the work addresses in their
> database are generated by an internal tool from employment history rather than
> observed. If that is also true of yours, then asking me which address you hold
> is asking me to reproduce something your system invented. Please search the
> telephone numbers and name variants instead.

#### Correction (2026-08-22): part one of this was my misreading

LeadIQ replied to the argument above and pushed back, and they were right:

> *"To clarify our previous request, we are not asking you to guess the specific
> email format that may exist in our database. We are asking whether you have any
> other professional/work email addresses associated with you that we can use to
> conduct an additional search."*

That is a reasonable question, not a puzzle with no answer. I read "a different
email address **or format**" as the format half and built the section on it. The
address half was the actual ask.

**The structural point survives; the accusation does not.** It remains true that a
consumer cannot enumerate pattern-constructed work addresses, and that a null
result on personal webmail is uninformative in a B2B index. It is *not* true that
this broker was asking me to guess one. Those are different claims and only the
first is supported.

This is the same error as `_SILENT_FAILURES.md` §66 and the §52 correction: a
mechanism that would explain the evidence is not thereby the cause of it. The
tell, again, is that the invented version was more interesting than the plain
one. Register matters — "which of my addresses did you search?" is fair;
"you are asking me to guess" was an accusation, and it was wrong.

LeadIQ also confirmed they searched the telephone numbers and hold no dates of
birth, home addresses or consumer webmail at all — so the whole consumer-shaped
identifier block was genuinely unusable to them, exactly as the section says.

**What to do instead.** Ask the narrow, checkable question. Their negative swept
a `.edu` address of mine in with the Gmail addresses under "personal email addresses from
domains such as Gmail, Hotmail, or similar consumer providers" — but a `.edu`
address is institutional, is precisely what a B2B index keys on, and may simply
not have been searched. One identifier, one question, and a commitment to accept
the answer if it comes back empty.

**On reversing yourself under pressure.** Having argued in writing that a profile
URL is disproportionate, handing it over the moment the search returned nothing
would mean the argument was never sincere — and these letters only work because
the reasoning in them is meant. The position to take is conditional: if a
candidate record turns up that genuinely needs disambiguating, that is a
different situation and worth reconsidering on its own terms. Say so explicitly
rather than just holding the line.

**Related:** §38, §41, §43; `_SILENT_FAILURES.md` §52, §66, §73.

---

## §45 The rights form that refuses to render because of where you live

AdeptID answered an emailed request by routing it to a form:

> *"In order to help you with your data rights request with AdeptID, you must fill
> out the following form."*

Opening the prefilled link produced a page that detected the requester's
jurisdiction as "Pennsylvania, US" and then displayed one sentence and nothing
else:

> *"We have detected that you are attempting to submit a request from a
> jurisdiction that does not currently support privacy rights."*

**No fields. No submit control. No route onward.** The form does not decline the
request on the merits; it declines to exist.

This is not the broker's doing. The form is **Osano** (`my.datasubject.com`), so
this is vendor-default behaviour and every Osano customer will do the same thing
to a requester in any state without a comprehensive privacy law. Expect it
wherever a rights link lands on that host — and by extension, check for the same
pattern on other platform vendors.

### Why it is worse than a refusal

A refusal is an answer. This is a working request being redirected into a channel
that cannot accept it, from a channel that already worked — the email arrived,
was read, and was routed. From the requester's side the result is
indistinguishable from a refusal nobody actually made, and there is nothing to
appeal because nothing was decided.

### The dropdown is the trap

The detected jurisdiction is a **selector**. Setting it to California would
presumably open the form.

**Do not.** It is a false statement of residency, it would be made in the course
of asserting a legal right, and a deletion obtained that way is worth nothing —
it is voidable the moment anyone looks, and it hands the broker a reason to
distrust every other identifier in the letter. It also poisons the technique for
the next person.

Say so in the reply rather than silently declining, because naming it is what
turns a design flaw into something the company can fix:

> The detected jurisdiction is a dropdown. I could set it to California and the
> form would presumably open. I am not doing that — I am a Pennsylvania resident,
> saying otherwise would be a lie, and a request obtained that way would be
> worthless to both of us.

### What to actually do

1. **Go back to the email thread.** It works; the form does not. Ask them to
   treat the original message as the request.
2. **Invoke the published-policy fallback**, which should already be in every
   letter: *honour this as a matter of your published privacy policy, and tell me
   in writing which basis you applied.* Offer "we extend rights only to residents
   of states that mandate them" as a complete and acceptable answer — it is a
   legitimate position, and pre-accepting it is what makes a plain answer cheap
   to give.
3. **Tell them it is the vendor's gate**, not theirs. They are far better placed
   to raise it with Osano than a consumer is, and it costs them nothing.
4. **Restate the substance**, briefly. The form was never load-bearing; the
   request does not depend on it.

### Two points of accuracy worth getting right

- **Geolocation is not residency.** The gate keys off where the browser connects
  from. Someone travelling, on a VPN, or on mobile carrier routing can be
  misplaced entirely — including *into* a rights state, which is the same error
  in the opposite direction.
- **Residency is not the whole test.** What binds a company is also what its own
  privacy policy promises. Plenty extend rights to all US residents and then
  deploy a vendor gate that contradicts the promise. Ask what the policy says
  rather than conceding the point.

**Status handling.** Not `failed` and not `manual_required` — the email channel is
live and a reply is outstanding. Leave it `submitted` and record that the web
route is closed to this requester, so nobody retries the form later.

**Related:** §43 (a form only an employee can complete), §71 in
`_SILENT_FAILURES.md` (a rights page with no rights form on it).

---

## §46 The instruction that points at a page which excludes you

Distinct from §45, and worth separating because the fix is different.

§45 is a **machine** gate: an Osano form geolocates the browser and renders no
fields at all. Nothing decided it and nobody at the company knows it happened.

This one is a **wording** gate, and it is self-contradictory. Aristotle
International's autoreply says:

> *"If you are a US resident writing about your rights under California Consumer
> Protection Act (CCPA) **or other state privacy laws**, you must make your
> request using the links on our website at
> …/privacy/addendum-for-california-residents/"*

Every mechanism on that page is scoped to one state — *"California residents may
exercise their California privacy rights by submitting deletion request"*,
*"California residents may opt out of the 'sale' of their personal
information"*, and the same for access, correction and sensitive-information
limits.

So the autoreply routes residents of *other* states to a page that offers rights
to Californians only. Both statements cannot be true, and between them there is
no route.

**The likely cause is mundane and worth saying out loud in the reply:** an
addendum written for one statute, later pressed into service as the general
privacy channel, with the autoreply updated and the page not. Naming the probable
cause rather than the probable motive is what keeps the exchange answerable.

### Why this one is more tractable than §45

A geo-gate has nobody behind it. A wording gate is a sentence somebody wrote, so
there is a person who can say "use the forms anyway" — and that is usually the
true position, because the narrow wording reflects the statute the page was
drafted for rather than the company's actual practice.

So **ask the cheapest possible question first**:

> Tell me which route a non-California US resident should use. If the answer is
> the same forms and the wording is simply narrower than your practice, say so
> and I will use them today. One sentence resolves it.

Then the published-policy fallback, then a request that they fix whichever of the
two is wrong — framed as something only they can see, since every non-California
requester hits the identical wall and most will conclude there is no route and
stop.

### Do not solve it by misdescribing your state

The forms are open; nothing stops a Pennsylvania resident typing a California
address. Do not. It is a false statement made while asserting a legal right, and
it makes the resulting deletion worthless — see §45.

**But note the narrower move that is legitimate:** submitting a form whose stated
audience is narrower than you, *while stating your actual state truthfully*, is
not a misrepresentation. It uses a channel and lets the company decide
eligibility. That is materially different from selecting "California" in a
residency field. Where a form has a free-text state field and no attestation,
that route is available; where it requires attesting to California residency, it
is not.

### Keep the phone number, do not lead with it

Aristotle publishes 888-217-9600. A voice call leaves no record either side, so
it is a fallback rather than an opening — queued as a handoff with a one-week
trigger, and with the instruction not to state a California address.

**Status handling.** `submitted`, not `failed`. The email channel is live, a
reply is outstanding, and the deflection is a routing problem rather than a
refusal.

**Related:** §43, §45; `_SILENT_FAILURES.md` §71.

---

## §47 "Your state has no privacy law" — and what to do when it is true

Pennsylvania has no comprehensive consumer privacy statute. So this refusal is
not a dodge, and treating it as one is both wrong and counterproductive:

> *"At this time, while many states do have consumer privacy laws, the state of
> Pennsylvania does not yet have consumer privacy legislation in place... We
> invite you to reach back out to us once the legislation has been officially
> enacted."*
> — N-Focus, The Data Agency

Roughly half the US population lives in a state with no such law. For those
requesters this is the single most common substantive refusal there is, and the
answer to it is not an argument about the statute.

### Three things that work, in order

**1. The published-policy fallback, which every letter should already carry.**

> If you believe you are not subject to these statutes, or that I do not reside
> in a covered state, I ask that you honour this request as a matter of your
> published privacy policy, and tell me in writing which basis you applied.

This costs nothing and converts a legal question into a policy one, where the
company has discretion and often exercises it. Many brokers run one suppression
list rather than fifty, because maintaining per-state carve-outs is more work
than honouring everyone.

**2. List every prior address, including out-of-state ones.** N-Focus refused
the Pennsylvania request and, in the next paragraph, honoured it as a Maryland
one — because a former Maryland address in the identifier list gave them a state
they recognised, and they suppressed on that basis.

**Do not assert this as an entitlement.** Coverage turns on residency, not
address history, and "I have rights in Maryland because I used to live there"
would be an overreach that collapses the moment anyone pushes. The reusable
lesson is narrower and purely practical: **never trim the address list for
brevity.** A broker looking for a basis to act may find one in it. Most will
not. This one did.

**3. Ask for suppression rather than deletion.** A deletion right is what the
statute confers; a suppression entry is something a company can simply choose to
add, and refusing it looks worse than granting it. N-Focus found no record and
added a suppression entry anyway, unprompted. That is quotable at any broker
claiming suppression is impossible absent a record.

### What not to do

- **Do not claim to live somewhere you do not.** Covered at length in §45 and
  §46. It is a false statement made while asserting a legal right, and it makes
  anything obtained worthless.
- **Do not argue that the CCPA applies to a non-Californian.** It does not, and
  saying so costs the credibility the rest of the letter needs.
- **Do not treat the refusal as bad faith.** N-Focus's reply was courteous, gave
  a reference number, invited a return once the law changes, disclosed its
  processor limits, and granted more than it had to. A combative follow-up to
  that is how a cooperative desk stops being cooperative.

### Status handling

Depends on what the second paragraph says, not the first. Where the refusal is
total, `manual_required` with a note to revisit if the state legislates. Where —
as here — something was granted on another basis, record that outcome:
`not_found` plus a suppression entry is a real result.

**Related:** §45, §46; `_SILENT_FAILURES.md` §64.


---

## §48 The ID demand that arrives *after* the deletion was already done

US Marketing Group processed a deletion and an opt-out automatically, with no
identity document, on the strength of the identifiers in the letter. Then, for
the **access** half of the same request, they asked for:

> *"a copy of a valid driver's license or other government-issued photo
> identification... Alternatively, a recent copy of 2 utility bills or bank
> statements reflecting both your name and your current address."*

**Never send any of these.** A government ID, and equally a bank statement, hands
a marketing data company a sensitive document it did not previously hold, in
order to discover what it holds about you. If the answer is "nothing", the
disclosure is pure loss. This is a hard rule in this project and it does not bend
because the broker is otherwise cooperative.

### The argument that actually lands

Not the statute — the **asymmetry inside their own reply**:

> The deletion and opt-out were processed without any identity document at all.
> You accepted my identifiers as sufficient to act on my behalf — to change your
> records — but not sufficient to tell me what those records contain. If the
> identifiers are good enough to delete on, I would ask you to consider whether
> they are good enough to describe.

That is hard to answer, and it is their own conduct rather than an outside
demand. Pair it with the CPRA point that verification must be *necessary and
proportionate*, and that the regulations direct businesses away from collecting
new categories of sensitive information where a less intrusive route exists.

### Offer three ways out, all acceptable

1. **A category-level answer** — "postal record with appended demographic
   attributes", not the values. Discloses nothing to a third party even if the
   identifiers were wrong, and usually answers the real question.
2. **The questions that need no verification at all**, because they are about
   practices rather than one record: which supplier provided it, whether it was
   rented onward and whether those clients were directed to delete, and whether
   deletion covers appended and modelled attributes or only the name row.
3. **A clean refusal** — "the access request cannot proceed without
   documentation" — recorded as given and not argued with.

Offering the third is what stops the request sitting open forever against a
condition that will never be met. Say so explicitly: *"what I would like to avoid
is the request sitting open indefinitely against a condition I have told you I
will not meet."*

### Do not lose the win in the argument

Their opt-out was **standing and survived a null result** — recorded against
identifiers they may not even hold, so a future acquisition cannot rebuild the
record. That is the thing most brokers refuse. Acknowledge it first, plainly, and
say you are not asking them to revisit it. The remaining dispute is narrower than
the reply makes it look.

**Related:** §43, §45, §46, §47.


---

## §49 Verification that IS the record key, versus verification that is a new disclosure

Two ID demands arrived on the same day and they are not the same thing. The
distinction decides whether to refuse or to hand the decision to the requester.

**US Marketing Group** (marketing lists) asked for a driver's licence, passport,
or two utility bills or bank statements. **Refuse.** None of those is in their
record. Producing one hands a marketing data company a sensitive document it did
not previously hold, in order to learn what it holds — and if the answer is
"nothing", the disclosure is pure loss. See §48.

**Airlines Reporting Corporation** (airline ticket settlement) asked for full
name, address, and:

> *"the last four digits of any and all credit card number(s) that you used to
> purchase air travel."*

That is materially different, and it is worth being honest about why rather than
reflexively treating every ID demand as obstruction:

- **It is not a new document.** Form of payment is already a field in a ticket
  settlement record. They are asking the requester to match against data they
  already hold, which is the textbook shape of proportionate verification.
- **It is the actual record key.** ARC's records are transactions, not people.
  A name alone cannot identify a ticket; the card that bought it can.
- **Last four digits alone cannot transact.**

**But it is still card data, and this project does not handle card numbers.** So
the correct move is neither to refuse on the requester's behalf nor to supply it:
**queue it as a decision, with the reasoning attached**, so the person can weigh
a genuinely defensible request themselves. Recording it as "another obstructive
ID demand" would be inaccurate and would teach the wrong lesson to anyone reusing
this file.

### The test

Ask: **is the requested field already in the record being asked about?**

| Requested | In the record? | Verdict |
|---|---|---|
| Driver's licence, at a list broker | No | Refuse |
| Bank statement, anywhere | No | Refuse |
| Card last-4, at a ticket settlement company | **Yes** | User's call |
| Prior addresses, anywhere | Usually | Supply — already in every letter |
| Account number for a service you used | Yes | User's call |

**And whatever the answer, ask for the parts that need no verification at all.**
ARC's reply ignored the substantive questions entirely — which agencies received
data, whether they act as processor for the carriers, and the government-
disclosure questions. None of those depends on verifying a specific record, and
letting an ID demand quietly close the whole request is how a verification step
becomes a refusal without anyone having to write one.

**Related:** §43, §45, §46, §47, §48.


## §50 "We are a processor — ask your employer" applied to an FCRA access right

Equifax, asked for a Work Number Employment Data Report and a freeze:

> *"Equifax Workforce Solutions (The Work Number provider) serves as a processor
> for Businesses who utilize our service. As such, any request (depending on your
> State of Residence) for access, correction, or deletion of this data, must be
> made to your Employer(s) to process the request."*

**Half right, and the wrong half is the half that matters.**

The processor framing works for *deletion*: employment and income data reported
by an employer is not something the consumer can order destroyed, and pointing at
the employer for a correction is reasonable — the employer is the furnisher and
owns the underlying facts.

**It does not work for access.** The Work Number assembles employment and income
information on consumers and furnishes it to third parties for employment, credit
and benefit decisions. That is what a consumer reporting agency *is* under the
FCRA — which is precisely why Work Number data is FCRA-regulated, a point worth
conceding early since it is also the reason deletion is off the table.

And under the FCRA, **file disclosure comes from the CRA, not the furnisher**. An
employer holds its own payroll records; it does not hold and cannot produce a
Work Number file. So the referral sends the consumer to a party that structurally
cannot help.

**The closing move is not the statute, it is the company's own product.** Equifax
Workforce Solutions already operates a consumer-facing route for obtaining an
Employment Data Report and placing a freeze. Asking to be pointed at a service
they already run is far harder to refuse than asking them to do something new:

> I am not asking you to build anything or make an exception — I am asking to be
> pointed at a service Equifax already runs, rather than to my employer.

### Why this is worth pushing on rather than filing

Employment and income history is among the most consequential records anyone
holds about a person: it is queried for jobs, loans, apartments and benefits, and
the consumer never sees it. A referral that reads as helpful and lands nowhere is
the most expensive kind of dead end, because it looks like an answer.

### The general shape

**"We are a processor, go to the controller" is often true and is sometimes a
category error.** Test it: *can the party you are being sent to actually produce
the thing you asked for?* Where the referral target is a furnisher and the ask is
file disclosure, the answer is no, and the referral is wrong regardless of how
the relationship is characterised elsewhere.

Related but distinct from §48, where the same company's identifiers were good
enough to delete on but not to describe. Both are asymmetries between what a
company will *do* to a record and what it will *say* about one.

**Related:** §47, §48, §49.


## §51 Grading a confirmation: what a good one actually contains

Two completions arrived within a minute of each other and the contrast is the
most useful teaching example in this file.

**Altair (excellent), quoted in full because each clause does work:**

> *"any personal data found relating to this consumer's name and mailing address
> has been removed... the data may exist on offline backups for up to 45 days...
> unless you instruct us otherwise, we will retain this request and use it to
> filter out and eliminate personal data if it is received by us from a data
> supplier in the future... we cannot remove the personal data from files on our
> suppliers' computer systems."*

**Giant Partners (typical):**

> *"Any required actions related to the consumer's personal information,
> including deletion, have been completed."*

Both say the request is done. Only one tells you what was done.

### The four things a confirmation should answer

1. **Deletion or suppression?** The single most important distinction and the one
   most often left ambiguous. A deletion is undone by the next supplier file; a
   suppression entry persists and filters future ingests. Altair applied
   suppression *by default* and said so. From Giant Partners' wording it is
   impossible to tell which happened — and the two produce identical text.
2. **Which identifiers were covered?** "Your information" is unfalsifiable.
   Compare IDM, which itemised eight email addresses and eleven postal addresses
   so the requester could check coverage against what they sent.
3. **What is the retention tail?** Altair names 45 days of offline backups.
   Silence here does not mean zero; it means unstated.
4. **What is out of reach?** Altair says plainly they cannot touch suppliers'
   systems and that the consumer must go upstream. That is not an evasion — it is
   the map for the next request.

### What to do with a vague one

Do not treat it as a refusal, and do not re-argue the whole request. Ask the two
or three questions that convert it into a gradeable answer, and **pre-accept the
unflattering option** so the reply is cheap:

> If it is deletion only, that is a real answer and I will record it as given — it
> simply means the removal has a shelf life and I should re-check rather than
> assume.

Offer the one-line format explicitly: *"all identifiers supplied"*, or *"current
name and address only"*, or whichever is accurate. A desk that would not write
three paragraphs will often write four words.

### The suppression-on-null-result ask is winning

Worth recording that this is no longer a long shot. In a single day, **three
separate registered brokers** found no record and added a permanent suppression
entry anyway, unprompted or on one line of asking:

| Broker | What they did |
|---|---|
| **IDM** | Itemised 8 email addresses and 11 postal addresses, then added all 9 phone numbers on request |
| **Prospeo** | Suppressed the phone number and every email supplied; named exactly what they had searched |
| **01Advertising** | *"Even though we found no records, we still exercise your right to opt out... by including you in our suppression list"* — plus a reference code and an appeal address, neither asked for |

So the ask has moved from favour to norm, and **naming the precedent is what
moves it**. The sentence that does the work:

> Another registered broker replied to me this week having found no record at all
> and added a permanent suppression entry regardless, itemising every identifier —
> so I know it is something a company in this business can do.

That converts "will you do something unusual for me" into "will you do what your
peers do", which is a much easier yes. Use the most recent and most comparable
example, not the most impressive one.

### Status handling

A vague confirmation is still `confirmed` — the broker affirmatively said the
data is gone, and disbelieving that without evidence is not honest record-keeping.
Record the vagueness in the note instead, so the next verification sweep knows the
claim was never specific enough to check.

**Related:** §48, §50; `_SILENT_FAILURES.md` §40, §84.


## §52 The ticket solved before you could act, and the link that isn't there

automotiveMastermind opened ticket 325845 and marked it **solved three minutes
later**, with this instruction:

> *"please complete the form on our California Do Not Share My Personal
> Information page... If you would like to make a request regarding your personal
> information not related to the CCPA, please complete the form found on our
> Privacy Request Page."*

**Neither URL is in the message.** Both are plain text with nothing behind them —
link text that lost its hyperlink somewhere between the template and the outbound
mail. So the requester is told to go somewhere and not told where, and the ticket
is already closed.

This is §66 (the mailto whose href and text disagree) in a new shape, and the
same rule applies: **report it as a fault rather than treating it as evasion.** It
is almost certainly a broken template, it affects everyone who receives that
reply, and only the company can see it. Ask for the two URLs and say you will use
them.

**The close-before-action pattern is separate and worth noting.** A ticket solved
in three minutes has not been worked; it has been routed. Do not rate the CSAT
survey that follows, and reply into the ticket thread to reopen it — see
`_SILENT_FAILURES.md` §70.

### The service-provider assertion in the same message

> *"automotiveMastermind is compliant with the CCPA provisions for a service
> provider... aM does not publish or otherwise disseminate this information to
> the general public."*

Both true, and neither ends the matter. Two responses that work:

**"Not published publicly" answers a question nobody asked.** Nobody fears that a
dealer-intelligence platform posts data on a website. The concern is that records
are supplied to dealerships and acted on there — calls, mail, offers. That is
dissemination to the parties who actually make contact, and it is entirely
consistent with never being public.

**A service provider is required to assist, so the answer is "route it", not
"no".** Under the CCPA a service provider must cooperate with the business in
responding to consumer requests and must delete on instruction. So convert the
deflection into a routing request:

> Please tell me which dealerships or clients hold data about me, so I can direct
> requests to them as controllers. If naming them individually is commercially
> impossible, the categories, or the count, would each be genuinely useful.

**And separate out what is unambiguously theirs.** Whatever the processor
analysis says about client-sourced records, **an inference the company generated
is its own processing** — a likelihood-to-buy or equity-position score is not
data a dealer supplied. Asking about the scores specifically sidesteps the entire
controller/processor argument, because there is no third party to point at.

Same move for suppression: *does your suppression survive a client uploading its
own customer file?* That is about their systems, not the client's data.

**Related:** §50 (processor referral to a party that cannot help), §51;
`_SILENT_FAILURES.md` §66, §70.


## §53 The conditional confirmation

BDEX answered a twelve-address request with:

> *"if an email address was provided then the opt-out has been processed."*

The condition is satisfied — twelve were provided — so on its face this says the
opt-out ran. But **"an email address" is singular**, and the sentence is
identical whether the opt-out covered one address, some, or all twelve. It is a
template written for the common case of a one-address request, reused against a
list.

**This is the cheapest kind of unfalsifiable confirmation** and it is worth
distinguishing from the vague sort in §51. A vague confirmation says nothing
specific. A *conditional* one appears to say something specific while the
condition does all the work — it is true regardless of what happened, so it
carries no information at all.

### How to answer it

Ask for the list, and make producing it look like the labour-saving option:

> A broker who answered me this week itemised eight email addresses and eleven
> postal addresses individually, which let me check coverage against what I sent.
> A list is more work to produce once and saves both of us a follow-up.

Then restate the addresses so the reply can be a copy-paste rather than a
lookup.

### Do not lose the disclosure buried in it

The same message contained something genuinely useful:

> *"our platform tracks consumers based on their email address, not name and
> postal address"*

That is a direct answer to *what is your index keyed to*, which is the question
worth asking of any identifier-based broker. Lead the reply by acknowledging it —
it tells you the sixteen postal addresses and twelve phone numbers in the letter
are not usable keys there, which shapes every follow-up and is worth knowing
rather than assuming.

**And the follow-on question it creates:** a platform that keys on email address
almost certainly keys on a **hash** of one for matching. So ask whether the
opt-out covers hashed forms or only plaintext. A truthful "we hold no record of
that address" is entirely compatible with holding its digest, and that is the
difference between an opt-out that works and one that looks like it did.

**Related:** §51 (grading a confirmation), §50.

## §54 — "We don't collect personal data like name or email"

LoopMe's autoreply, in full on the relevant point:

> *"LoopMe is an advertising technology company that provides interest-based
> advertising. We don't collect traditional forms of personal data such as
> name/email address and therefore we are unable to action a request based on
> this information alone. You can opt-out of interest-based advertising by
> providing your Device ID on our opt-out page."*

Read that sentence carefully, because it is almost certainly **true**, and it is
almost certainly **not the whole picture**. In the advertising industry all of
the following routinely hold at the same time:

- the company receives **hashed** email addresses — MD5, SHA-1, SHA-256 — in bid
  requests or from data partners;
- it stores them as **match keys** against device, cookie and CTV identifiers;
- it never sees or stores the plaintext, and can therefore say with a straight
  face that it does not collect email addresses.

Every clause of "we don't collect name or email" survives. And a hashed email is
still personal information about the person it identifies — identifying them is
its *only* function.

### Why this is the most efficient deflection in the industry

It does two jobs in one sentence. It sounds like a **privacy virtue** ("we never
even see your email"), and it functions as a **jurisdictional exit** ("so we
cannot act on what you sent us"). A consumer who accepts it at face value goes
away satisfied and deleted, and nothing has been deleted.

### The reply that gets past it

Do not argue about whether they collect email addresses. Concede the sentence and
ask the question it does not answer:

> *"I accept that as stated. Please answer this directly rather than by reference
> to the collection statement: does LoopMe hold, or receive from partners, hashed
> forms of any of the email addresses or phone numbers listed in my first letter?
> **You can determine this without my help — hash each of the twelve and check.**"*

That last clause is the load-bearing one. It removes the only practical excuse
for not answering. The company has the hashing function; the consumer supplied
the inputs; no additional information is required from anyone.

Then ask the two follow-ups that decide whether a deletion is real:

- are the hashes **linked** to device, cookie or CTV identifiers, and will the
  **links** be deleted rather than only the attribute rows? In an identity
  business the graph is the product, and a record deleted while the linkage
  survives is reassembled from the next bid stream;
- if a hash is retained **for suppression**, say so and confirm it is used only to
  keep me out and never to match me in. Do not object to a suppression hash —
  object to not being told which list it sits in. The same string does opposite
  work depending on the answer.

### It arrived paired with the Device ID demand

The same autoreply asks for a Device ID, which is the §MAID impossibility in
`_CATEGORY_VARIANTS.md`: an identifier the person it describes cannot reliably
read, and which may have been reset many times over the period the records cover.
Any ID readable off a phone today will not match the historical rows; the ones
that would match are exactly the ones the consumer has no way of knowing.

The two deflections work as a pair, and it is worth naming that in the reply: one
sentence says the identifiers you *can* supply are not held, the next says the
only acceptable identifier is one you *cannot* supply. Between them there is no
route in — **not because the consumer is being difficult, but by construction**,
and equally for every consumer.

So do not merely complain about it. Offer a concrete substitute and put the
burden where the knowledge is:

> *"I am not asking you to delete on an unverified guess... If that particular
> method does not fit your systems, please tell me what would. I am asking you to
> name a route that exists, not to waive the check."*

### One genuinely useful thing in the autoreply

It ended: *"If your email does not relate to the above, we will review and
respond as necessary."* That sentence is a hook, and it is worth pulling on
explicitly — open the reply by quoting it. It converts a canned response into a
standing commitment to review, made by them, in writing.

**Related:** §MAID material in `_CATEGORY_VARIANTS.md`; `_SILENT_FAILURES.md` §87
(the identifiers that matched were the ones nobody would think to send).

## §55 — The referral that requires the answer you are asking for

ClearCompany, a talent-management SaaS platform, replied:

> *"To access, correct, delete, or export any data that you as a data subject have
> submitted through our system while applying for a job to one of our customers,
> simply go back to that company's career site... If you wish to have your data
> removed from the ClearCompany system, you'll need to reach out to the company
> that you've applied to in order to do so. ClearCompany, as a Data Processor in
> this context, cannot delete any data on behalf of our customers who are the
> Data Controllers."*

The controller/processor distinction is correct and worth conceding immediately.
The **instruction built on it is a loop**:

- to exercise the right, contact the controller;
- to identify the controller, ask the processor;
- the processor says contact the controller.

The consumer does not know which of the vendor's customers holds a record.
Applications may be years old, made to companies since renamed or acquired, and
there is no published list of which employers use a given platform. **There is no
route from "somewhere in your system there may be a record of me" to "this
specific career site" that does not pass through the processor.**

This is sharper than §50 (a referral to a party that cannot help). Here the
referral is to a party the consumer **cannot even identify** — the instruction
presupposes exactly the fact being requested.

### What to ask for instead

Do not argue the processor point; concede it and ask for the one thing that
breaks the loop and that only the processor can do:

> *"Please tell me which of your customers hold records associated with the
> identifiers in my original message, so that I can approach those controllers
> directly."*

That is a **disclosure about where the data sits**, not a deletion of anyone's
record, and it sits squarely within what a processor can do. If they decline,
make them decline explicitly and name the alternative route — a recorded refusal
is worth more than an instruction that cannot be carried out.

### Also check what the processor answer does not describe

A processor reply describes the data customers put in. It is silent on anything
the vendor does **in its own right**, and in this sector that is usually the part
worth asking about: sourced or passive-candidate profiles assembled from outside
any application, enriched or **derived** contact details, and fit/match/ranking
scores generated by the system. None of that was submitted through a career site,
so no customer's job portal will ever show it, and the processor framing quietly
excludes it without saying so.

Ask whether the vendor sources, enriches, derives or scores independently. **If
the answer is genuinely no, that is a complete reply and should be accepted as
one** — the point of the question is to make the silence explicit, not to insist
something must be there.

### Two riders worth attaching

1. **Retention after the controller is gone.** What is the default retention for
   applicant records after a requisition closes, and do records persist after a
   customer stops being a customer? Where the controller has disappeared, the
   consumer has no one left to ask, and the referral fails absolutely rather than
   merely inconveniently.
2. **Suppress the LinkedIn URL** (`_SILENT_FAILURES.md` §90). It is the
   collection input for derived records, it is stable, and it is one of the few
   identifiers the consumer can actually supply.

### The hook, again

This autoreply ended: *"If your request is for something else, we will get back to
you as soon as possible."* LoopMe's ended the same way (§54). **Open the reply by
quoting that sentence.** It converts a canned response into a standing commitment
to review, made by them, in writing — and it is nearly always literally true that
the request *was* for something else, because the canned answer addresses the
common case and the letter was written for the uncommon one.

## §56 — The offer that cannot be accepted

DemandScience's reply made a genuinely good offer, better than most in its sector
(`_SILENT_FAILURES.md` §90):

> *"If you believe we may hold a professional profile for you under a corporate
> email address, wish to suppress a specific business domain, or would like us to
> suppress your public LinkedIn profile URL, **please reply with those business
> details** so we can add them to our internal suppression list."*

I replied and did exactly that. **Twelve seconds later a byte-identical copy of
the same message arrived**, from `dataprivacy+canned.response@demandscience.com`.

The invitation asks you to reply. Replying triggers the autoresponder that issued
the invitation.

### State only what is observable

I cannot see inside their mail routing, and I am not claiming no human ever reads
the thread. What is observable is: identical text, twelve seconds, and a
sub-address whose local part is literally `canned.response` — consistent with a
rule that fires on every inbound message including replies to itself. Whether a
person also triages the thread later is unknown, and the follow-up should say so
rather than accuse. (Compare `_SILENT_FAILURES.md` §66: a mechanism that would
explain the evidence is not thereby the cause of it.)

### Why this is worse than a plain refusal

A refusal tells you where you stand and you move on. This shape:

- **looks cooperative**, so a consumer records it as progress;
- **consumes the follow-up**, so the substantive reply is absorbed;
- **is self-concealing** — the loop is only visible if you notice the second
  message is identical to the first. Skim it and it reads as "they responded
  again", which sounds like engagement.

A consumer working through a long list will very reasonably file this as handled.

### What to do

1. **Diff the two messages.** If a reply produces an identical body, treat the
   address as an autoresponder rather than a mailbox, whatever the signature says.
2. **Change channel, do not re-send.** Re-replying feeds the same rule. Look for
   another published address — theirs named `legal@` for HR and applicant
   requests, which is at least a different mailbox — or a web form or portal.
3. **Lead with the loop, briefly and without accusation.** Set it out as numbered
   steps with the timing, say plainly that you cannot tell whether a human also
   reviews the thread, and ask them to route the message. A company that made a
   good offer will usually want to know its acceptance path is broken.
4. **Grant the point that the offer was good.** It costs nothing and it is true.
   *"That is precisely why the loop is worth fixing — it makes a genuine
   concession look like a brush-off, which cannot be what you intended."* You are
   reporting a defect in their process, not litigating their good faith.
5. **Restate the ask in full in the new message.** Do not refer back to "my
   previous email"; assume whoever reads this has none of the history.

### The general lesson

**A published contact address is not a channel until something other than a
machine has answered on it.** Registry filings (`_SILENT_FAILURES.md` §83, §85,
§88) already fail in three ways — wrong desk, unmonitored mailbox, mailbox
decommissioned. This is a fourth: **a mailbox that answers every time and receives
nothing.** It looks healthiest of the four and is no better than the rest.

## §57 — The form redirect that keeps a door open

Converge Marketing's autoreply is the best-shaped redirect received so far:

> *"To submit your request, please use our secure online form: » Submit Your
> Privacy Request [my.datasubject.com link]. The form takes just a few minutes to
> complete and will route your request to the right team based on your location.
> **If you are unable to use the form, please reply with your name, the state you
> reside in, and a description of your request, and we will assist you
> directly.**"*

Two sentences separate this from every other form redirect in this file:
Blackbaud, Buxton, Catalist and Crexi all name a destination and stop there. This
one names a destination **and keeps email open for anyone the destination does not
work for.**

### Why that last sentence matters more than it looks

A form is not a neutral channel. It can fail in ways the person on the other end
never sees:

- §45 — an Osano `my.datasubject.com` request that **rendered with no fields at
  all** once a location gate applied. Same platform Converge links to.
- A CAPTCHA the requester will not solve, or cannot.
- An attestation they are not willing to make.
- Assistive technology the form does not work with.
- A required field the person genuinely cannot fill.

In every one of those cases a form-only policy converts a valid request into
silence, and the company never learns it happened. **The fallback is what makes
the redirect honest**, because it means a broken form costs the requester a reply
rather than the request.

### Take the fallback rather than the form

When offered, use it. It needs no browser, faces no CAPTCHA, and produces a
threaded written record, which a form submission usually does not. Give exactly
the three things asked for, then attach the full request underneath — supplying
the requested minimum is what makes the reply easy to action, and the detail
underneath is what makes it complete.

### While you are there: volunteer the weak fact

Their fallback asks for **state of residence**, and the honest answer is often
unhelpful — Pennsylvania has no comprehensive consumer privacy statute.

Say so first, plainly, rather than letting it surface later as a reason to
decline:

> *"Pennsylvania has no comprehensive consumer privacy statute. I am therefore not
> claiming a Pennsylvania statutory right, and I will not pretend otherwise. I am
> asking you to honour this under the CCPA as amended to the extent it applies to
> records you hold about me; and failing that, as a matter of your own published
> privacy policy, which is not conditioned on my state of residence."*

Then close the escape hatch:

> *"If your position is that you will only act for residents of states with a
> comprehensive privacy law, please say so directly rather than declining
> silently. A clear refusal is something I can record and respect; an unanswered
> request is not."*

The published policy is the load-bearing part. Most privacy policies commit to
handling requests without limiting the promise by state, and a company that
declines anyway has to decline **against its own published words** rather than
against a statute you cannot invoke. See §47 — "your state has no privacy law" is
sometimes true, and the answer is not to argue it but to move the request onto
ground that does not depend on it.

## §58 — The qualified null

Blueprint Audiences' Privacy Lead replied — carefully, in full sentences, from a
named human address. It is the most sophisticated non-answer received in this
project, and it is worth taking apart slowly, because at a glance it reads as a
completed search.

> *"Blueprint Audiences has reviewed its records and completed a search of the
> **direct identifiable records** it maintains. We did not locate any **direct
> identifiable records** for this individual in our systems.*
>
> *Blueprint Audiences does not maintain directly identifiable records in its
> pseudonymous audience activation environment and does not reidentify
> pseudonymous identifiers to a known individual. We have already forwarded this
> request to applicable partners through our partner suppression workflow.*
>
> *Based on our review of the records maintained directly by Blueprint Audiences,
> there is no further direct deletion action for Blueprint Audiences to take at
> this time."*

### Three distinct moves, each individually true

**1. The qualifier carries everything.** "We did not locate any *direct
identifiable* records" is not "we hold nothing about you." My letter had opened by
predicting precisely this: *"A name-and-address search is likely to return nothing
even when you do hold data about me, because the record is keyed to a pseudonymous
identifier."* The search performed was the one I said in advance would come back
empty.

**2. A tautology presented as a finding.** *"Does not maintain directly
identifiable records in its **pseudonymous** audience activation environment"* is
true **by definition** — a pseudonymous environment holds pseudonymous records.
It describes the architecture. It says nothing about whether anything in that
environment corresponds to the person asking.

**3. A statement about process, answering a question about data.** *"Does not
reidentify pseudonymous identifiers to a known individual"* describes something
they **do not do**. The question was what they **hold**. A company can hold a
hashed email that identifies someone perfectly well as a match key while never
once reidentifying it to a name. **Both facts are simultaneously true, and the
second does not answer the first.**

### Why this is harder to answer than §54

§54 ("we don't collect name or email") is visibly a statement about collection.
This one **has the shape of a completed search** — records reviewed, search
completed, no results, no further action. Every structural cue says *resolved*.
Only the adjective says otherwise.

### The lever: suppression implies a key

The strongest thing in the reply is also the loose thread, and it should be pulled
**as a question, not an accusation**:

> *"You forwarded the request to partners through your partner suppression
> workflow. Suppression normally operates against an identifier — a partner has to
> be told what to suppress. So: what identifier was forwarded? If a hash or key of
> mine was passed to partners, then such a key existed here, and I would like it
> deleted as well as suppressed."*

A null and a forwarded suppression are hard to hold together without a key
somewhere. Say that you are not alleging untruthfulness and would rather ask than
assume — because there *are* innocent answers (a generic workflow, a
partner-side-only match), and the point is to find out which.

### Also: correct a mischaracterisation of who is asking

This reply described the request as *"submitted on behalf of the individual
identified in your correspondence"* — i.e. recast a first-party consumer as an
**authorized agent**, despite the letter's opening line saying the opposite.

Correct it, briefly and factually, and say why it matters: **agent-submitted
requests carry additional authorisation requirements and are sometimes declined
for want of them.** Left uncorrected, it sits in the file as a ready-made reason
to refuse later. Do not treat it as bad faith — long letters get skimmed — but do
not let it stand.

### The reply that fits

1. **Credit what was actually done.** They forwarded to partners unprompted and
   said so. That is item 3 of the standard request, delivered without chasing.
   Lead with it.
2. **Accept the finding as stated** — the direct-identifiable search really did
   come back empty, and saying so costs nothing.
3. **Name the qualifier** and show it answers a predicted false negative.
4. **Re-ask the hash question with the hash-it-yourself clause**, which reduces it
   to a lookup requiring nothing from the consumer.
5. **Pull the suppression thread as a question.**
6. **Re-commit to accepting a clean answer**, and mean it — see
   `_SILENT_FAILURES.md` §99.

**Related:** §54, §55; `_SILENT_FAILURES.md` §91, §99.

## §59 — The notification that withholds the notification

Eight emails from PwC's OneTrust in thirty-two minutes, one per open request:

> *"Dear [name], A comment has been added to your request (Request ID:
> 82M3JY825A). Please click the button below to access your request in the
> portal."*

**It tells you a comment exists. It does not tell you what the comment says.**

That is a small design decision with a large effect. The content — very often a
verification question or a scope clarification, the sort of thing answerable in
one line — sits behind a signed portal link. So a message that could have resolved
the request in a single reply instead becomes a task: open a browser, follow a
per-request token, read, log in to the reply box, type there.

For a consumer with **one** request that is a minor annoyance. For anyone with
several it multiplies, and it multiplies precisely when the requests are otherwise
identical.

### Why there were eight

Almost certainly the §101 data model again: **intake forms commonly accept one
identifier per submission.** Someone with twelve email addresses, twelve telephone
numbers and sixteen prior addresses cannot make one complete request — they are
structurally forced to make many near-identical ones, and then receive many
near-identical notifications about them.

Same root cause as Accurate Append processing exactly one value per field, and as
Speedeon's *"Only one name and address may be included on this form."* The system
holds one value per field, so every interface it offers holds one value per field.

### What to do

1. **Use the fallback address the notification itself names.** This one said: *"If
   you have issues accessing your request, please contact a member of the PwC US
   privacy team at us_privacy_office@pwc.com."* That sentence is an escape hatch
   from the portal, exactly like the Converge fallback in §57 — and "I cannot read
   a comment I have not been shown" is a genuine access issue.
2. **Ask them to paste the comment text into a reply** and say you will answer it
   there. Almost nothing in a DSAR comment actually requires a portal.
3. **Ask them to merge the parallel requests into one**, and to say which reference
   survives. Put it as good for both sides, because it is: it is *n* queues for
   their team and *n* portals for you, and every one needs the same answer to the
   same question.
4. **Explain why there are n**, briefly, without blame. A privacy team may not know
   its intake form is generating duplicate work for itself. This is the rare case
   where the consumer can see the defect and the company cannot.
5. **Restate the request in the email** so that nothing depends on retrieving it —
   and say explicitly that this is a restatement, **not a new request**, so no
   statutory clock restarts.

### The general shape

A notification that says *something happened, go elsewhere to find out what* is a
channel that costs the recipient more than it needed to. It is not obstruction —
nobody designed it to frustrate anyone — but it converts an answerable question
into an errand, and it does so most severely for the people with the most
identifiers, who are the people most likely to have records worth deleting.

### It was not eight. It was twenty-seven.

I recorded this as eight parallel requests. That was wrong — I read one page of
search results and did not paginate. The true figure is **at least twenty-seven**,
still arriving, one notification roughly every three and a half minutes, each with
a different request ID.

The count was available and I did not ask for it. Worth recording because the
handoff I wrote on the strength of it told the reader to work through eight
portals when there were twenty-seven — **a handoff that understates the work
threefold is worse than one that admits it does not know the size**, because the
reader budgets for it and stops when the number they were given runs out.

The correction also changes the advice. At eight portals, opening them one by one
is tedious but reasonable. At twenty-seven it is the wrong first move entirely, so
the rewritten handoff leads with *do not start by opening twenty-seven portals* and
sends the reader to the consolidation email thread first.

**And it sharpens the underlying point.** One notification per request is a
reasonable design when a person has one request. The number of requests here is
not a choice anyone made — it is the one-value-per-field intake form multiplied by
someone with a long identifier history. **The notification volume is the intake
design, compounding.** Whoever set the per-request email rule never saw a case
like this, and would probably not defend it if shown one.

### Correction: we did not create these requests. PwC did.

I twice assumed the parallel requests came from **our** side — that a form taking
one identifier per submission had forced many near-identical submissions. That is
the pattern recorded at `_SILENT_FAILURES.md` §101 and it fitted, so I reached for
it.

The mailbox says otherwise. **We sent PwC exactly one email**, on 19 August, and
one follow-up today. There are **no submission confirmations at all** — nothing
saying "we have received your request", which is what a portal sends when a
consumer files one. Every message is *"a comment has been added to your request"*,
about a request we never knowingly opened.

And the arithmetic is hard to ignore. That single letter carried:

| | count |
|---|---|
| email addresses | 12 |
| prior postal addresses | 16 |
| prior telephone numbers | 11 |
| current address | 1 |
| current telephone number | 1 |
| **total identifiers** | **41** |

Request IDs observed: **~35 and still arriving**, at a machine-steady 3.5-minute
cadence.

**The most likely explanation is that their intake decomposed one letter into one
request per identifier.** I hold that as the best available reading rather than a
finding — §66 applies, and a mechanism that would explain the evidence is not
thereby the cause of it. But it fits the count, the absence of confirmations, the
cadence, and the fact that only one letter was ever sent.

### Why this inverts the lesson

§101 and the earlier part of this section describe **the consumer** being forced
into many requests by a one-value-per-field form. This is the same data model
**on the receiving side**, and it is worse in an interesting way:

- the consumer did exactly the right thing — one letter, every identifier listed,
  explicitly asking that each be searched;
- the recipient's system could not hold that shape, so it fanned it out;
- the fan-out then generated ~41 notifications, ~41 portals, and ~41 comment
  threads, **for one person making one request**.

Nobody chose this. No individual at PwC decided to send forty emails. The intake
design multiplied a single well-formed request by the requester's identifier
count, and the requester's identifier count is high precisely because they have a
long history — which is precisely why they have records worth deleting.

**The practical consequence is reassuring rather than alarming.** This is not our
volume and cannot be read as abusive on our part: we sent one letter. It also
means the consolidation ask is exactly right, and better founded than when I sent
it — I asked PwC to merge requests that *their own system* created.

### The salutation gave it away

Partway through the stream the greeting changed. Earlier messages opened with the
subject's **full name**. Later ones open with an **initialised short form** —
`[initial] [surname]`.

That short form is not a mistake. It is one of the **name variants** our letter
listed under "Also known as", where five spellings of the same name were supplied
so that each could be searched.

So each request carries whichever item from the letter it was built from, and the
salutation is rendered from that request's own record. **A system that had simply
received many requests from one person would not change how it addresses them
mid-stream.** One that built a request per line item would.

That moves the decomposition from a plausible reading to a well-evidenced one, and
it lets the total be predicted rather than guessed:

| item type in the 19 Aug letter | count |
|---|---|
| email addresses | 12 |
| prior postal addresses | 16 |
| prior telephone numbers | 11 |
| current address | 1 |
| current telephone number | 1 |
| **name variants** | **5** |
| **total** | **46** |

Observed at the time of writing: **45, still arriving.**

### Final count: 58. It stopped. And every prediction I made was wrong.

Counted from timestamps rather than estimated:

| | |
|---|---|
| distinct request IDs | **58** |
| first / last notification | 17:46:54 – 21:26:38 UTC |
| span | 220 minutes |
| median gap | 3.6 minutes |
| since then | **nothing** |

My successive predictions were **41**, then **46**, then **205**. The actual figure
is 58. **None of them was close, and I am not going to propose a fourth theory to
fit the number** — what is established is that one letter fanned out into 58
requests, and that the salutation cycled through at least three of the supplied
name variants. The rule that produced exactly 58 is unknown.

The 205 came from a specific, avoidable mistake. Gmail's `resultCountEstimate`
returned **201**, and I read it as a count. It is a placeholder for *"many"* — the
same field had returned an **exact 45** an hour earlier, and I did not notice that
one of those numbers was a different kind of thing from the other. **A tool that
sometimes returns exact counts and sometimes returns a saturation value will
mislead anyone who does not check which they got.**

I also pushed that figure to the user, with an estimate of eight hours remaining.
It stopped twelve minutes later.

### On whether the escalation stopped it — it probably did not

I emailed PwC asking them to halt the notifications at roughly 21:14 UTC. The
stream ended at 21:26. The temptation to record that as cause and effect is
obvious, and the evidence does not support it: **the deceleration had already
begun before the email landed.** The final gaps ran

    3.6 → 4.0 → 4.0 → 4.6 → 6.1 minutes

with the slowdown starting around 21:07, several minutes *before* the escalation.
A queue winding down looks exactly like this. An intervention would more likely
have cut it off sharply.

So: it stopped, the escalation was still worth sending — the requests remain open
and unconsolidated — and **it should not be recorded as having worked.** A
coincidence of timing that flatters the action you happened to take is precisely
the kind of thing this file exists to catch (§66).

### Four counts, and why that is worth admitting

I reported this as **eight**, then **twenty-seven**, then **forty-five**, then
**about two hundred**. The first two were simply wrong — I read one page of
results and did not paginate. The third was correct at the time. The fourth
corrects a *reasoning* error rather than a counting one: I had the right data and
drew the wrong structure from it, because "5 names" looked like five things.

The cost was never embarrassment. Each number went into a handoff, and a handoff
is instructions someone else acts on. These are not the same task:

| stated scale | reasonable response |
|---|---|
| 8 portals | work through them |
| 27 portals | ask for consolidation first, then work through |
| 46 portals | do not start; make them consolidate |
| **~205 portals, still growing** | **do not start; consolidate, telephone, and filter the inbox** |

They are not even the same *kind* of task. So the handoff has been rewritten four
times, and its final form adds two things none of the earlier versions had:

- **telephone them.** This is now a volume problem their own system is generating,
  and a call resolves it faster than email ever will;
- **filter the inbox.** A rule on the sender stops ~200 identical notifications
  drowning every other broker reply. None of them needs individual attention.

**When a number is load-bearing for someone else's work, count it properly or say
you have not** — and when a structure is load-bearing, check whether the thing you
counted is a list or a dimension. Five names in a list is five. Five names crossed
with forty-one identifiers is two hundred and five.



I reported this as **eight**, then **twenty-seven**, then **forty-five**. The first
two were not cautious estimates that grew — they were **wrong numbers stated
plainly**, because I read one page of results and did not paginate, and then did
not re-check before writing the second.

The cost was not embarrassment. It was that each number went into a handoff, and a
handoff is a set of instructions someone else acts on. *Work through eight
portals* and *work through forty-six portals* are not the same task; they are not
even the same **kind** of task. At eight, grinding through is reasonable. At
forty-six, grinding through is the wrong move and the right move is to make the
sender consolidate.

So the handoff has been rewritten a third time and **changed from a click task to a
decision task**, because that is what it now is:

> Do not open forty-six portals. Wait on the consolidation email. If no reply,
> open **two**, compare the comment text, and if identical answer once by email
> citing every ID.

**When a number is load-bearing for someone else's work, count it properly or say
you have not.** An estimate labelled as an estimate would have caused no harm here.
A confident wrong number caused two bad handoffs.

### If the comments turn out to be identical

Check two or three before answering any. If a queue of requests from one person
received the same templated comment, it can be answered **once by email citing
every request ID**, rather than typed into twenty-seven separate reply boxes. Ask
for that explicitly rather than assuming it is allowed.

**Related:** §57; `_SILENT_FAILURES.md` §101.

## §60 — The ID demand that was never the policy

Arity's automated message said identity could not be verified and pointed at an
appeals form. The implication — and it is the implication almost every such
message carries — was that a government-issued ID would be needed.

I replied refusing to upload one, and asked **two specific questions**:

> *"Could you tell me specifically what about my submission failed verification
> (e.g. a mismatch between the name/phone/email I gave and what's on file), and
> whether there is a less intrusive way to resolve it — confirming the last four
> digits of the phone number on the account, or confirming the ZIP code on file,
> for example?"*

The answer:

> *"**Arity does not require consumers to provide government identification** to
> submit a 'Delete My Data' request... Our review found the **phone verification
> step was not completed.**"*

The blocker was a one-time passcode that had to be entered from *both* email and
phone. That is all it ever was.

### The lesson

**An automated verification-failure message may not describe the company's actual
policy.** It is a generic template fired by a rule, and the rule does not know why
the check failed. Reading it as "they demand ID" and either complying or giving up
would both have been wrong.

Two things made the difference, and both are cheap:

1. **Refuse the intrusive step and say why**, without treating it as final —
   *"I would rather not submit a government ID, and I don't believe one should be
   necessary."*
2. **Ask what specifically failed, and offer to answer something narrower.**
   Naming plausible alternatives — last four digits, ZIP on file — does the work
   for them and shows you are trying to be verified, not to avoid verification.

The reply that came back was more useful than a successful appeal would have been:
it named the actual step, gave a second channel (a telephone number as well as the
form), and put the no-ID position **in writing**, which is worth having on the
record for any later exchange.

### Do not stop at the refusal

The instinct on seeing an ID demand is to object and wait. Objecting alone gets a
restatement. **Objecting plus a specific question gets a specific answer** — and
here that answer dissolved the problem entirely, because there had never been an
ID requirement to argue about.

**Related:** §48 (ID demanded after deletion was already done); `_SILENT_FAILURES.md`
§104 (verification that cannot be met by construction).

## §61 — The form has no box for you

Deloitte's intake redirect asks the requester to state **their relationship with
Deloitte**, and offers: current or former job applicant, Tax client, subscriber or
marketing recipient, MyDeloitte accountholder, event registrant, Business
Chemistry participant, alumnus or retiree, and *Other*.

Every option describes **a customer, an employee, or a counterparty.**

But Deloitte Consulting LLP appears in a state **data broker registry** — and
registration applies to an entity that sells or shares personal information about
consumers **with whom it has no direct relationship.** The one category that
describes the person most likely to be exercising a broker-related right is the
only one the form does not offer.

### This is not a refusal, and that is what makes it interesting

Nobody wrote a rule saying "reject people with no relationship to us." The form
was almost certainly designed by mapping the ways a person's data *normally*
arrives at a professional services firm — and that map is complete, for the
population it was drawn from.

Then a registration obligation attached, aimed at a completely different
population, and no one revisited the taxonomy. **The deflection is a schema, not a
decision.** It cannot be appealed, because there is nobody who chose it.

That makes it invisible from the inside, too: a privacy team reviewing its intake
sees categories that account for every request it has ever received.

### What to do

1. **Select "Other" and name the missing category explicitly** — *"no
   relationship; writing in response to a data broker registration."* Do not pick
   the nearest-fitting real relationship. Saying you are a former job applicant
   when you are not routes the request to HR and answers a different question.
2. **Say the category is missing, once, without heat.** It is genuinely useful
   information: *"a request taxonomy built entirely from customer relationships
   cannot receive requests from the population that data-broker registration
   exists to protect."*
3. **Separate the question that needs no form.** Here that was: *what activity
   caused the registration?* That is not a data subject request — it needs no
   verification and no identity check, because it is not about the requester at
   all. **Asking it in the email thread, explicitly flagged as not-a-DSR, routes
   around the form entirely.**

### The companion instruction: one request per email address

The same reply said: *"Please submit one request for each unique email address that
is associated with you."*

Twelve addresses, twelve separate Data Subject Requests, for one person. This is
`_SILENT_FAILURES.md` §101 — the one-value-per-field data model — but stated as
**policy, in advance**, and placed on the consumer rather than executed silently
inside the company.

Ask whether one request listing all of them is acceptable, and **give the reason
in terms of their cost, not yours**: it is twelve queues, twelve reference numbers
and twelve verification exercises on their side. Cite the case where an intake
system did this multiplication by itself and generated dozens of parallel requests
from one letter — it makes the point concrete and it is not hypothetical.

**Related:** `_SILENT_FAILURES.md` §101, §107; §57.


---

## §62
### The row that was never built

**Shape:** you follow a broker's published opt-out link, land on a compliance
portal, and find pages for California, Colorado, Connecticut, Delaware, Indiana,
Iowa, Maryland, Montana, Utah and Virginia. You live somewhere else. The URL for
somewhere else 404s.

**Why it is not the residency deflection.** The residency deflection is a claim:
*we honour requests only from covered states.* You can answer a claim — point at
the company's own registry filing, ask them to honour it as policy and to state in
writing which basis they used, note that their form already accepts non-covered
states. Someone wrote that sentence and someone can unwrite it.

A missing page is not a claim. It is the absence of one. There is no text to quote
back, no author to appeal to, and no one on the operator's side who will ever learn
it happened — no form arrives, no complaint arrives, nothing bounces. From where
you stand it looks like a broken link.

**What it costs.** In the family we found this in, six of fourteen brands have a
catch-all page and eight do not. Same operator, same Omaha address, plausibly the
same underlying file. So whether you can opt out turns on **which brand name your
record was sold under** — a fact about the vendor's page matrix, not about you or
the statute.

**The response.** Go up a level. Write to the operator of the portal rather than
the brand, and ask it as a routing question, because that is almost certainly what
it is: *what is a resident of a non-covered state supposed to do for these brands?*
Name the brands and name the gaps, so the question cannot be answered generically.
Then ask them to honour the request as company policy if the honest answer is that
no route exists — which gives them something easy to say yes to.

**Related:** §61 (the deflection that is a schema rather than a decision — this is
its geographic twin), `_SILENT_FAILURES.md` §110, §109.

---

## §63
### The address that answers is not the address that acts

**Shape:** you write to the contact address a broker published — often the very one
in its state registry filing — and get a courteous reply saying that this mailbox
handles customer service and *"we do not process privacy requests received via
email,"* followed by a link to a form.

**Is it legitimate?** Under CCPA Reg §999.312(e)(2) a business that receives a
request through a non-designated channel must either treat it as validly submitted
or tell the consumer how to submit it properly. These replies do the second thing,
so on the regulation's own terms they are compliant. Do not argue that point; it is
not winnable and it is not the interesting part.

**What is worth noticing** is what the reply does to your records. Every request you
sent to that address before the reply arrived was, by the company's own account,
never processed. If a status in your tracker says `submitted` on the strength of an
email to a mailbox that refuses email, that status is describing something that did
not happen.

**And check before you downgrade.** When we swept the six brokers in this position,
five turned out to be properly backed — three by a consolidated letter to the
corporate estate's *privacy* address, which is a different channel and does work,
and two by self-service submissions confirmed on screen. Only one rested on nothing.
Downgrading all six would have thrown away four real submissions and one confirmed
one.

**The useful move:** find the address that *does* act. It is rarely the one on the
website. For a family of brands it is often the parent's registry-filed privacy
address, which answers precisely because it was filed for this purpose — while the
consumer-facing support desks are staffed to sell subscriptions and are told to
deflect.

**Related:** §61 (the deflection with no author), `_SILENT_FAILURES.md` §112, §103.

---

## §64
### Closed, and how would you rate us?

**Shape:** you ask a specific question. The reply answers something adjacent. You
follow up, shorter, with the one question isolated. The next thing you receive is
**a customer-satisfaction survey** — the ticket is closed and the question was
never touched.

Nuwber did this on 2026-08-26. Three asks, none answered:

1. A five-question letter came back with *"your information has already been
   deleted"* plus a paragraph on Google's cache — the one thing they explicitly
   cannot control.
2. A deliberately short follow-up isolated the single question: deletion or
   suppression?
3. The ticket was closed and a survey sent.

**Why it is worth a name.** There is no refusal anywhere in this. Nobody declined
to answer, so there is nothing to escalate and nothing to quote. A support system
measured on ticket closure and satisfaction treats a closed ticket as a success,
and a question that does not map to a macro is friction on the way there. The
survey is not cynicism; it is the workflow reaching its end state.

It is also, quietly, the most effective deflection in this file — because it leaves
the consumer holding a **real** outcome. The Nuwber profile genuinely is down. It
is easy to accept that as the answer and stop, and only notice months later that
nobody ever said whether it stays down.

**The response.** Reply once more, and make three things explicit:

- **Decline the survey, and say why** — "I would rather not rate the exchange
  before the question in it has been answered." This is not point-scoring; on
  Zendesk-style systems a reply reopens the ticket, and it names the thing that
  just happened without accusing anyone.
- **Offer the easy answer.** *"If nobody there can answer it, or if the answer is
  'deletion only, we do not hold suppression entries,' say so in a line — I will
  record it and will not write again."* A support agent who cannot answer a
  technical question can very often forward one that has been reduced to a
  sentence.
- **State the default.** *"If I do not hear back, I will record it as
  deletion-only."* That converts silence into an answer with a cost, and it is
  honest — it is what you are going to do anyway.

**Do not click the rating.** A rating closes the loop on their side and gives the
thread a terminal state.

**It is systemic, not one company.** Three satisfaction surveys arrived from three
different people-search desks on a single day — Nuwber, Ownerly and NeighborWho.
Only Nuwber's is confirmed to have closed over an unanswered question; the point is
that the survey is a standard stage in the workflow these desks run, so expect it
after any exchange that does not end in a macro. Its arrival is not a signal that
anything was resolved. It is a signal that the ticket state changed.

**Related:** §58 (the qualified null), `_SILENT_FAILURES.md` §112.

---

## §65
### One request per identifier

**Shape:** the portal works. The request types are all there. Nothing is refused.
And then, in Epsilon's case highlighted in yellow so you cannot miss it:

> "A separate request must be made for each address and email address."

Do the arithmetic for one ordinary person. Twelve email addresses accumulated over
thirty years, sixteen postal addresses, and five applicable request types —
delete, do not sell, do not share, opt out of profiling, right to know. That is
**up to 140 portal submissions**, each with its own identity verification email to
click, to exercise one set of rights at one company.

**Why this is the sharpest version of the pattern.** PwC's fan-out (§59) was
accidental — an intake system decomposed one letter into ~58 parallel requests and
nobody chose that. This one is *policy*. Someone wrote the sentence, someone
highlighted it, and it is delivered alongside "we do not action privacy requests
received via email" and "responses to this message will not be answered." Every
door except the multiplying one is closed in the same message.

**And it inverts the incentive.** The more identifiers a company holds on you — the
more thoroughly it has tracked you across three decades of addresses and dead
mailboxes — the more submissions it takes to get free of it. The rule scales the
burden with the harm.

**What it costs even if you comply.** Each submission is independently verified and
independently answered, so you get 140 confirmations, none of which tells you
whether the others succeeded, and no way to ask a question that spans them. It also
guarantees the identifier-linkage question can never be asked: the whole point of
an identity graph is the edges between identifiers, and a process that admits one
identifier at a time cannot be asked about the join.

**The response.** Do not file 140 requests. File **one more**, through the portal
since that is the only channel that is actioned, and use its free-text field to:

- reference the request IDs already issued, so it reads as completing existing
  requests rather than opening new ones;
- list every identifier and ask them to treat the request as covering all of them;
- state the arithmetic plainly and ask whether that is genuinely the intended
  process — *"if it is, please say so in writing."*

That last part is the point. A company will often quietly do the sensible thing
rather than put "yes, 140 submissions" in writing. And if they do put it in
writing, that sentence is worth more than the 140 submissions would have been:
it is the clearest possible evidence that the process, not the answer, is what
defeats the right.

**Related:** §59 (the notification that withholds the notification), §61 (the
deflection that is a schema), §63 (the address that answers is not the address that
acts), `_SILENT_FAILURES.md` §103.

---

## §66
### Send us the URL of the profile we already deleted

**Shape:** you write a supplementary letter to a people-search site — new
identifiers, added to a request they have already honoured. The reply is polite and
sounds reasonable:

> "We apologize for any inconvenience. Please provide the URL/web address of your
> profile details page so we can identify your profile."

There is no profile details page. **They removed it**, eight days earlier, and
confirmed it on screen with the record named back. The only way to produce the URL
they are asking for would be for the removal to have failed.

**The removal you were granted is what makes the follow-up unanswerable.** Nobody
designed that; it falls out of a support script written for the first contact being
used on the second. But its effect is a request that cannot be satisfied and a
ticket that closes for want of information the consumer structurally cannot have.

**The deeper error is the key, not the timing.** Even before the removal, a URL
would have been the wrong thing to ask for. A supplementary letter exists precisely
because of identifiers that *do not surface in a name search* — four dead email
addresses, six addresses left decades ago, three old phone numbers. Records keyed
to those were never going to appear on the page the consumer could find. A URL is a
front-end artifact; the request is about the index behind it. **A back-end search
takes identifiers, not links.**

**The response.** Do not treat it as obstruction — say plainly why it cannot be
answered, and give them the thing that works:

- Name the circularity in one sentence: *the only way I could give you that URL is
  if your removal had failed.*
- Distinguish the artifact from the data: *a page URL is the front end; my request
  is about what is in the index.*
- Redirect to the usable key: *please search the identifiers themselves.*
- Invert the ask: *if any of them produce a live record, that URL is something you
  can see and I cannot — I would rather be told about it than asked for it.*

That last line is the useful one. It converts an impossible demand into a question
they are uniquely able to answer, and it costs them nothing to answer honestly.

**A tell worth noticing.** Both TruePeopleSearch and FamilyTreeNow sent this text —
identical, word for word — **two seconds apart**. Same script, same desk, same
moment. That is stronger corroboration of a shared operator than the boilerplate in
`_SILENT_FAILURES.md` §112, and it arrived for free.

**Related:** §61, §63, `_SILENT_FAILURES.md` §112, §103.

---

## §67
### The sending address is not the address in the record

**Shape:** you write, in the first line, *"I am the consumer, writing about my own
data. I am not an authorized agent acting for anyone else."* The reply says:

> "To proceed with this request, it must be submitted directly by the data
> subject."

Nobody read past the identifier list. But the interesting question is not *why did
they not read it* — it is **what made an agent request the more natural reading**,
because that is fixable and the rest is not.

**The likely cause, and it is structural.** A letter is sent from one address and
lists twelve. If a broker holds a record at all, it is far more likely keyed to one
of the older ones — the dead university mailbox, the ISP address abandoned in 2003
— than to the address you write from today. So the sending address does not match
the record, and a verification step built on "does the requester's email match the
subject's email" fails on exactly the population with the longest data trail.

The same shape appeared at BDEX: of twelve addresses searched, **four matched and
every one had been out of service for years**, while none of the current addresses
matched at all. The addresses most likely to be *in* the file are the least likely
to be the one you can send from.

**A second trigger** is naming the brand rather than the parent. Writing to Clearbit
about Clearbit, when HubSpot now owns it, reads to a HubSpot agent as a request
about somebody else's product.

**The response.** Do not simply re-assert that you are the data subject; that is
what the ignored first line already said. Instead:

- Quote your own first line back, so the correction is checkable rather than
  asserted.
- **Offer them the cause.** *"If something made it look otherwise I would like to
  know what"* — then name the sending-address mismatch and the brand-versus-parent
  point. This converts a contradiction into a diagnosis, which is much easier for a
  support agent to accept.
- Ask them to treat the existing request as validly submitted **rather than
  restarting the clock**. A re-file resets the statutory deadline, which is the real
  cost of the misclassification.
- Offer the fallback without conceding: *"if your process genuinely cannot accept it
  on that basis, say so plainly and I will use the portal."*

**Related:** §61, §63, §65, `_SILENT_FAILURES.md` §103.

---

## §68
### The redirect that carries the request with it

Almost every entry in this file is a way of handing work back to the consumer.
This one is the opposite, and it is worth recording as the shape to hope for.

LexisNexis Legal & Professional replied:

> "You have reached LexisNexis Legal & Professional which handles case law and news
> information. We are a separate business from LexisNexis Risk Solutions which
> handles requests such as yours. We have reviewed the details that you provided,
> and we have forwarded this request to LexisNexis Risk Solutions."

Four things happened there, and only the first is common:

1. They identified that they were the wrong division.
2. They **forwarded the request** rather than telling the consumer to resend it.
3. They **said they had done so**, with a reference number.
4. They gave the correct route anyway, and closed their own ticket cleanly.

Compare that with the usual version — *"we do not action privacy requests received
via email, please use the portal"* (§63) — where the work of getting the request to
the right place lands back on the person who already did it once, and the statutory
clock quietly restarts.

**The trap inside the good outcome.** A forwarded request is invisible to the person
who sent it. You cannot tell whether it arrived, whether it kept its date, or
whether it landed in a queue nobody reads. So the right move is not to relax — it is
to **write directly to the receiving division as well**, referencing the forward and
saying plainly *"treat this as the same request, not a second one."* That costs one
letter and removes the single point of failure without accusing anyone of anything.

**And check who they pointed at.** `lexisnexis_risk_solutions_fl` sat in our
registry with **no status at all** — one of the largest consumer data businesses in
the United States, never written to. It surfaced only because the reply named it.
A redirect is a fact about corporate structure, and corporate structure is where the
untracked entities live (`_SILENT_FAILURES.md` §118).

**Related:** §57, §63, `_SILENT_FAILURES.md` §118, §117.

---

## §69
### The deflection that was just broken

automotivemastermind replied to a deletion request:

> "To help us respond to your request as quickly as possible please complete the
> form on our California Do Not Share My Personal Information page"

**There was no link in the message.** The anchor text had been sent without its
href, so the sentence named a page and gave no way to reach it. Their ticket was
then marked "solved" — twice.

From outside, this is indistinguishable from a hostile deflection. Being told to use
a form that cannot be found, and having the ticket closed, reads as a brush-off, and
the natural response is to treat it as one.

It was a template bug. We replied saying so plainly — *"neither link is in the
message"* — as a fault report rather than an accusation, and the next message
contained the URL written out in full.

**The lesson is about the reply you choose.** The same facts support two responses:

- *"You closed my request and pointed me at a page you did not link to"* — true, and
  it puts a support agent on the defensive about something they did not decide.
- *"Neither link is in the message; I think your template has lost its hrefs"* —
  also true, costs nothing, and gives them something they can actually fix.

The second one got a working URL in a day. Assume a broken system before a hostile
one, because the broken kind is far more common and is the only kind that responds
to being told.

**A related tell:** a ticket marked "solved" whose resolution text is the same
deflection, repeated. Resolution is a workflow state, not a claim that anything
happened — the same point as §64.

**Related:** §64, §66, `_SILENT_FAILURES.md` §115.

---

## §70
### Confirm your residency — when residency was never the question

CinqDI replied to a deletion request:

> "under current U.S. state data privacy laws, only residents of certain states are
> eligible to submit consumer requests. Based on the information provided, it
> appears you are not a resident of one of those states. If you believe this may be
> an error, please provide us with additional information confirming your state of
> residency."

The letter had given the current address in full, **Pennsylvania** included. Nothing
about residency was unclear, and Pennsylvania genuinely has no comprehensive
consumer privacy statute — **their conclusion is correct**.

So do not argue the law. Arguing it is the trap: it is a fight you lose on the
merits, it uses up the goodwill you need, and it lets the exchange end on the one
question where they are right.

**What is actually wrong with the reply is that it answers a question the letter had
already conceded.** Our template ends:

> *"If you believe you are not subject to these statutes, I ask that you honor this
> request as a matter of your published privacy policy."*

That sentence exists for exactly this reply, and the reply did not engage with it.
Not refused — **not seen**. A residency check is a workflow step with two outcomes,
and "honour it anyway as policy" is not one of them, so the sentence had nowhere to
go (the §61 shape: a schema, not a decision).

**The response, in three moves:**

1. **Concede the law immediately and explicitly.** *"Your conclusion is correct on
   the facts as stated and I am not going to argue that a law covers me when it does
   not."* This costs nothing, and it makes the rest readable as something other than
   a complaint.
2. **Re-ask the policy question as a separate question**, in one sentence, so it
   cannot be absorbed back into the residency workflow: *will you delete and
   suppress as a matter of company policy, notwithstanding that no state law obliges
   you to?*
3. **Price it honestly and give them the out.** The cost is one suppression entry;
   the alternative is continuing to sell data about someone who asked in writing not
   to, in a state that happens not to have legislated yet. And: *if the answer is no,
   say so and tell me which basis you applied — I will record it and will not write
   again.*

That last part matters most. The failure mode to avoid is not refusal, it is the
request that is **neither honoured nor refused and simply stops**. A stated refusal
is a usable outcome; silence is not.

**An aside worth noticing.** The reply was signed by a Principal Digital Project
Manager at *mv digital group* — CinqDI's privacy desk is run by an outside agency.
That is a vendor relationship you only learn from a signature block, and it is the
same class of fact as §63: the address that answers is not always the company.

**Related:** §61, §63, §68, `_SILENT_FAILURES.md` §110.
