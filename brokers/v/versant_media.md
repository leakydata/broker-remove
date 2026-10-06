# Versant Media

- **Email:** privacy@versantmedia.com (verified — named directly by NBCUniversal's own privacy team)
- **Method:** email — but only confirmed for CA/CO residents; see Gotchas.
- **Domain:** versantmedia.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-10-05)
- Reference: `gmail:1a0c897b24b8a5ed`
- Note: 9/22: emailed privacy@versantmedia.com per NBCUniversal's referral for the TeamUnify record (now a Versant brand). PA resident; invoked fallback clause since Versant's stated email route names only CA/CO.
- Note: 2026-10-05: answered the PA-residence disclosure directly rather than ignoring it — "As you have indicated that you reside in the United States, please visit our Individual Rights Request Portal... We process individual rights requests only through the portal." Separately offered a web FORM (not email) to add the address to an ad-sale suppression list, plus the standard device/cookie "Your Privacy Choices" footer link. No ungated email route exists for the deletion request itself; the fallback-clause ask did not move them off the portal. Both the portal and the suppression form need a browser — queued to `handoff.py` for completion.

## Steps

1. Write to `privacy@versantmedia.com` directly. Do not bother with a portal
   search first — this address only surfaced because NBCUniversal's privacy
   team named it in reply to a brand-scoped letter (see Gotchas).
2. If you are not a CA/CO resident, say so up front and invoke the fallback
   clause — see Gotchas for why this matters here specifically.

## Gotchas

**This is a spin-off, not a rebrand — old letters to the parent bounce logically
even when they don't bounce technically.** TeamUnify LLC was described on its
own site as an NBC Sports / NBCUniversal company. Writing to `privacy@nbcuni.com`
did not fail — it got a real, fast reply — but the reply was "that's not our
brand anymore." NBCUniversal spun off a group of media properties as Versant
Media, and TeamUnify went with it. **The lesson generalizes: a company
description on a broker's own site can be stale even when the site itself is
current.** If a parent company's privacy team redirects you to a successor
entity, that redirect is worth more than the original site copy — take it at
face value and write to the new entity, don't re-verify the old one.

**The email route is explicitly scoped to CA/CO residents, with everyone else
routed to a portal.** NBCUniversal's reply named `privacy@versantmedia.com` as
the route for "California and Colorado residents or their authorized agents"
and pointed all other countries to an "Individual Rights Request portal." This
project's subject is a Pennsylvania resident, so strictly the named channel
does not apply to him. Wrote anyway, disclosed the PA residency up front rather
than staying silent about it, and invoked the fallback clause (honor as
company policy if statute doesn't reach you) — that is the correct way to use
an out-of-scope email channel: transparently, not by omission. Watch for
whether Versant answers a Pennsylvania resident by email at all, or insists on
the portal once residency is disclosed.

## Verification

Watch for a reply from privacy@versantmedia.com. If it insists on the portal
route because of the disclosed PA residency, that's a data point for this
file — record whether the portal itself asks for a state, and whether
Pennsylvania is even an option in its dropdown.
