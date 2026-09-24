# HubSpot, Inc.

- **Email:** privacy@hubspot.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** hubspot.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-09-23)
- Note: 2026-09-23, `privacyrequest@privacy.hubspot.com` sent two separate automated confirmations four minutes apart — one for an "Object to Processing" request, one for a "Deletion" request — each saying only "We have taken action per your request." This is the OneTrust-portal route referenced below (`preferences.hubspot.com/privacy`), not a reply to the original `privacy@hubspot.com` email thread that had been looping on autoresponders; whoever ran the portal route this time got through where the email route did not. No specifics on what was found or which of the two ("Clearbit" vs. "HubSpot" data) it covered. Recorded `confirmed` on the strength of "action taken," but the lack of detail means it's worth a follow-up asking what was actually deleted/objected-to.
- Prior: Recovered from the committed playbook brokers/h/hubspot.md, because the ledger carries no notes and this row's status had no evidence behind it: Recovered from Gmail Sent folder -- letter sent 2026-08-23 to privacy@hubspot.com re: Clearbit data. Got stuck: an autoresponder keeps replying with the same 3-working-day/portal-links template regardless of content; a real reply once said the request 'must be submitted directly by the data subject' despite the letter already stating that in its first line -- replied clarifying, got the same autoresponder template again. Web form (preferences.hubspot.com/privacy) is the only route that will get past the loop; queued for a human.

## Steps

Email loops rather than resolves. Use `https://preferences.hubspot.com/privacy`
directly for a request about Clearbit-sourced data.

## Gotchas

**The auto-reply and the human reply say different things, and the human
reply is wrong.** `privacy+noreply@hubspot.com` sends a fixed 3-working-day
template with three links no matter what's asked. A real person replied once
saying the request "must be submitted directly by the data subject" — despite
the original letter stating exactly that in its first line. A clarifying
follow-up got the autoresponder template again, not a human answer. Don't
keep pushing by email past that point; the portal is the only way through.

**The portal route works where the email route loops.** Submitting via
`https://preferences.hubspot.com/privacy` produced two clean "action taken"
confirmations (an Object-to-Processing and a Deletion) within minutes of each
other, in contrast to the `privacy@hubspot.com` email thread that repeatedly
returned the fixed 3-day autoresponder template. If you're stuck in the email
loop described below, stop pushing there and use the portal instead.

**Addressed to "Clearbit (HubSpot)"** — Clearbit is the registered CA data
broker; HubSpot acquired it. Naming the acquired brand may be what triggered
the "not the data subject" misreading, if it wasn't just the mismatched
sending address (see the b2b/enrichment variant note in
`_CATEGORY_VARIANTS.md`).

## Verification

No confirmation yet. Nothing public to re-search (B2B enrichment data, not
a listing site); a written confirmation from the portal route would be the
artifact.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** HubSpot, Inc.
- **Registered address:** 2 Canal Park, Cambridge, MA, 02141
- **Filed contact email:** Privacy@hubspot.com
- **Filed phone:** 8884827768
- **Website:** https://www.hubspot.com; https://clearbit.com

*Source: `data/registries/registry.csv`.*

## If they ignore you

Work down this list. Each rung costs them more than the one above it.

1. **Reply in the existing thread** after the statutory deadline. California
   allows 45 days for a deletion request (Cal. Civ. Code 1798.130), extendable
   once by a further 45 with notice. Quote the date you first wrote.
2. **Write to the legal entity at the registered address above**, by post, if
   email has failed. A letter to the address of record is harder to lose than a
   support ticket, and it establishes a paper trail.
3. **Complain to the California Attorney General**, who administers the data
   broker registry: <https://oag.ca.gov/contact/consumer-complaint-against-business-or-company>.
   A broker's registration is what obliges it to answer; a complaint referencing
   the registry entry is the pressure point.
4. **Complain to the FTC**: <https://reportfraud.ftc.gov>. Useful for a pattern
   of non-response rather than a single case.
5. **Your own state Attorney General.** Many states with no comprehensive
   privacy statute still have consumer-protection powers and will take a
   complaint about a business that ignores its own published policy.

**What not to bother with:** phoning a support line to argue. The person who
answers cannot change the policy and did not write it. The registry entry, the
statutory deadline and the regulator are what actually move a company.
