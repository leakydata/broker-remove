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

