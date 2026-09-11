# Resonate

- **Email:** privacy@resonate.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** resonate.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-22)
- Note: Their reply came FROM no-reply@resonate.com which hard-bounces on reply. Resent the challenge to privacy@resonate.com (the original, working address) and flagged the unroutable From: as a defect (2026-08-19). A follow-up run (2026-08-22) sent essentially the same follow-up content to privacy@resonate.com again, not realizing the 2026-08-19 resend had already gone through cleanly — redundant, but harmless, and no reply had arrived yet either time to answer the open questions (inference-layer deletion, sources, downstream licensees, standing do-not-model). Still awaiting a substantive reply as of 2026-08-22.

## Steps

1. Write to `privacy@resonate.com`.
2. Aim the request at the **inferences**, which are the product.

## Gotchas

**Name the sensitive inferred attributes individually.** A general deletion
request reliably fails to reach them, for three reasons that apply squarely to a
psychographic modelling business:

1. they are held as **scores and segment memberships**, not as fields in a
   contact record;
2. they are **inferred rather than collected**, so nobody — including the subject
   — thinks of them as "my data";
3. they are exactly the attributes that do lasting harm when they circulate, and
   **an inaccurate one is worse than an accurate one**.

The list worth naming: political affiliation, ideology and issue positions;
voting likelihood; religiosity; ethnicity; sexual orientation; health conditions
and treatment propensities; disability; pregnancy and children's ages; income,
net worth and financial-distress indicators; firearms and gambling interest;
charitable giving; and psychographic value and motivation scores.

**Ask for a standing do-not-model entry, not just deletion.** If the inputs remain
available, the same inferences are regenerated at the next refresh. Deleting
today's scores without blocking re-modelling is the clearest case in this project
of a removal that undoes itself by design.

Many of these categories are **sensitive personal information** under the state
statutes; if the operator considers any of them out of scope, make them identify
which and on what basis.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## The reply that comes from an address which cannot receive a reply (updated 2026-08-19)

The letter went to `privacy@resonate.com`. The answer came back from
**`no-reply@resonate.com`**. Hitting reply produced:

> "Address not found. Your message wasn't delivered to no-reply@resonate.com
> because the address couldn't be found, or is unable to receive mail."

There is no `Reply-To:` header pointing anywhere useful, and nothing in the body
says where to write instead.

> **A `no-reply` From: on privacy correspondence is a one-way valve.** The
> consumer does the obvious thing, gets a bounce, and a fair number will read that
> bounce as the end of the road — which is indistinguishable, from their side,
> from a company that simply refuses to continue.

The fix is trivial once you see it: **reply to the address you originally wrote
to, not to the `From:` header of the answer.** `privacy@` accepted mail before and
accepts it now; only the outbound template is broken.

> **Keep the address you sent to.** When a broker answers from a different
> address, treat the new one as *additional* information, not as a replacement.
> Two candidate routes are better than one, and the one you already proved works
> is the one to fall back on.

Recorded as a defect in the reply itself, because Resonate can fix it in one line
by setting `Reply-To: privacy@resonate.com` on that template.

## "An encrypted version of your email that cannot be reversed"

The substantive reply narrowed the request to identity fields and then declined
them:

> "Resonate uses digital identifiers like browser cookies and hashed email
> addresses (an encrypted version of your email that cannot be reversed). We do
> not maintain other personal details such as your name, address, phone number, or
> government ID."

Both halves need answering, and they need answering differently.

**On the characterisation.** A hashed email is not encryption and it is not
anonymity. It is a **stable pseudonymous identifier**: the same address always
produces the same digest, which is exactly the property that makes cross-company
matching work. Data linkable to an identifiable person is personal information
under the CCPA as amended by the CPRA and under the comparable state statutes —
and for an address an attacker can guess or already holds, the hash is reversible
in practice by simply hashing candidates until one matches.

> **The phrasing is not necessarily bad faith — it is industry boilerplate — but
> ask whether it is doing work.** If that sentence is what decides which records
> fall inside the deletion process, then a legal error has become an operational
> one, and the question to put is precisely: *is it?*

**On the scope.** The reply is a careful description of what Resonate does *not*
hold. It says nothing about what it does. Resonate's product is the **inference
layer** — the values, motivations, attitudes, political and social positions,
health and financial propensities and audience segments modelled about a person
and attached to exactly the identifiers they do admit holding.

> **Deleting the key while keeping the profile keyed to it is not a deletion.** In
> this business the profile *is* the product. Ask explicitly whether the modelled
> attributes and segment memberships go, or only the identifier row.

Three further questions kept open: which **sources** supplied the underlying
inputs (panels, purchase data, browsing, voter files, licensed third-party data);
whether **clients who already licensed segments containing the subject** retain
them after deletion; and whether there is a **standing do-not-model entry** or
whether the same inferences are simply regenerated at the next refresh from the
same inputs. The last one decides whether any of this survives a quarter.

Also worth pre-empting, as the original letter did: the self-service tools they
recommend (the site footer controls and the DAA opt-out page) set a **preference**
in one browser. They die with the cookie jar, do nothing on another device, and
leave the underlying record intact. Use them — they are not worthless — but do not
accept them as the answer to a deletion request.

See [[_DEFLECTIONS]] and [[_CATEGORY_VARIANTS]].
