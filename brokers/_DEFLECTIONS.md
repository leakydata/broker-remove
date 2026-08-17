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
