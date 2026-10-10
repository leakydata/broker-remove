# HubSpot, Inc.

- **Email:** privacy@hubspot.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** hubspot.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-10-10)
- Note: VERIFIED (468 audit) -- EARNED, TWO SEPARATE ACTIONS CONFIRMED. HubSpot's privacy system sent two results emails on 2026-09-23, four minutes apart: an OBJECT TO PROCESSING request ('We have taken action per your request') and a DELETION request ('We have taken action per your request'). Separating the two is the practice 443 asks for. THE ROUTE WAS NOT CLEAN AND THE DETOUR IS WORTH RECORDING. The request concerned CLEARBIT, which HubSpot acquired, and went to privacy@hubspot.com. On 2026-08-25 they refused it as an agent request: 'To proceed with this request, it must be submitted directly by the data subject.' It had been submitted directly by the data subject -- the misreading appears to come from the letter naming Clearbit in the subject line, which their triage read as acting on behalf of a third party. One correction on 2026-08-26 fixed it, and the results followed four weeks later. SAME FAMILY OF ERROR AS ALLANT GROUP AT 473, whose completions described the request as submitted 'on behalf of' the subject. A letter that names a company other than the recipient invites an agent-request misclassification; worth a line in the opening paragraph saying plainly that the sender IS the data subject and the named brand is the recipient's subsidiary.

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
