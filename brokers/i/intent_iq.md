# Intent IQ LLC

- **Email:** privacy@intentiq.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** intentiq.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-09-25)
- Note: 2026-09-25, privacy@intentiq.com replied to the same thread: "The
  processing of your email address for opt out purposes has been completed."
  No mention of the broken button from the September reply, and no way to
  independently verify the servlet defect below no longer applies -- but a
  plain-text completion statement from the privacy team supersedes an
  inference from a broken link, so this is recorded `confirmed` rather than
  left on the `failed` finding. Worth noting for the next person: **the
  written confirmation is the thing to ask for and rely on, not the button.**
  If you only click the link, you cannot tell success from failure (see
  below); if you get a written "completed" reply, that answers it regardless
  of what the button does.
- Prior: OPT-OUT LINK IS BROKEN AT BOTH ENDS, 2026-09-05. Intent IQ replied from privacy@intentiq.com with a button, 'Click to opt-out of this email address being shared, sold or used for targeted advertising'. Two defects. (1) THE HREF CONTAINS A RAW CONTROL CHARACTER: the URL in the HTML source is ...ProfilesEngineServlet?at=7&mi<0x10>&email=...&emailVoucher=..., with a literal DLE byte where the mi parameter's value should be. That is in the message as they sent it, not an artefact of reading it. (2) THE SERVLET ANSWERS 200 WITH A REDIRECT HEADER: every request to it returns HTTP 200 carrying 'Location: https://www.intentiq.com/opt-out-failed'. A 200 is a success status and browsers only follow Location on a 3xx, so the two audiences see opposite things -- a person clicking the button lands on a BLANK PAGE with no message at all, while anything that follows the header (curl -L, a scanner, a link checker) is told the opt-out FAILED. Verified in the real browser as well as with curl: the tab stays on the servlet URL with an empty body. Tried the parameter three ways (mi=, mi, and mi%10 preserving the control byte); identical result each time, so the control character is not the discriminator. WHETHER THE OPT-OUT WAS RECORDED CANNOT BE DETERMINED FROM OUTSIDE, which is why this is failed and not submitted -- and note that a consumer who clicks once and sees a blank page has no way to tell either. Writing to them. This is the third distinct success/failure disagreement found today, after AddressSearch's HTTP 500 behind a success page and Juicebox gating an opt-out on a verification email.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@intentiq.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

**Don't rely on their opt-out button to tell you anything.** As documented
above, the button in their email is broken two different ways depending on
who or what follows it — a human sees a blank page, an automated checker sees
a failure redirect. Ask for a written confirmation in the same thread instead
of clicking through, and treat that written statement as the record of what
happened, not the button.

## Verification

No independently checkable URL — the servlet in their opt-out email answers
every request the same way regardless of outcome (see Status), so it can't be
used to verify anything. Rely on a written reply in the email thread instead.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Intent IQ LLC
- **Registered address:** 250 Broadway Floor 24, New York, NY, 10007
- **Filed contact email:** privacy@intentiq.com
- **Filed phone:** (888) 701-1811
- **Website:** www.intentiq.com

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
