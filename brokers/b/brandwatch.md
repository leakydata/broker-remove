# Brandwatch

- **Email:** privacy@brandwatch.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** brandwatch.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-28)
- Note: REPLY 2026-08-28 from PrivacyTeam@cision.com to a letter sent 17 Aug to privacy@brandwatch.com -- CISION NOW RUNS BRANDWATCH'S PRIVACY FUNCTION (see _FAMILIES.md). They answered the architectural question straight, which most do not: 'Our data is generally indexed by social media account identifiers rather than by name, address, phone number, or email address.' Then asked for the social handles plus proof of account ownership before searching. HANDLES DECLINED, and the reasoning matters: if their index is keyed to handles and not to names or emails, they cannot presently connect any record to this person -- so supplying handles would not help them find an existing record, it would CREATE the missing linkage, in writing, dated, tied to a name and email, inside a company whose business is selling profiles derived from social content. That is §144 at its sharpest. Offered them the sentence that would close it instead: 'indexed by social account identifiers and unable to locate any record from the name, emails, addresses and phone numbers supplied'. THE FIND: their own signature footer offers a one-word unverified opt-out -- 'reply with OPT OUT as a subject line and we'll get this done for you' -- sitting four inches below a demand for handles and ownership verification. §146 in its purest form: the right that costs them nothing is free, the right that touches the data is gated. Took the free one; the reply was sent with the literal subject line OPT OUT so their process triggers, with the reasoning in the body. Also asked whether one search covers Brandwatch and Cision or whether they are separate systems.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.brandwatch.com/your-privacy-choices/
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `dpo@cision.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## The auto-reply is a gate — you must reply to it

`privacy@brandwatch.com` answers within minutes from `PrivacyAutoreplyBW@`. It
opens with *"We confirm receipt of your message"* and then, further down:

> *"If you believe we have collected data on you as a Content Author, please reply
> to this email indicating your desire for us to proceed with your request."*

**Nothing is processed until you send that reply.** The receipt looks like the
artifact you were waiting for. See `_SILENT_FAILURES.md` §5.

## Two categories, two different answers

The same reply splits requests in a way that matters:

**Users (customers/prospects)**

> *"Our products are not meant for use by private individuals and therefore we
> only accept and index upon business email addresses. If your email address is a
> personal email address, we can confirm that we would not have collected any data
> related to you as part of our services, sales, or marketing efforts."*

So for a private individual with personal addresses, this category is genuinely
empty. Worth accepting rather than arguing.

**Online content authors** — the category that actually applies:

> *"The Brandwatch product collects only publicly available online content and
> stores it based on the social handle/username associated with the content. We
> only index on your social handles. We do not have any content indexed by your
> proper name, email address, or phone number."*

**This is why a standard opt-out letter achieves nothing here.** Name, email and
phone — the entire contents of the usual request — are not searchable fields.
Without social handles there is nothing for them to match on, and a truthful "no
records" reply is the likely outcome.

## What to send

1. Reply confirming you want the request processed (the gate above).
2. **Ask which platforms they hold author content from before volunteering
   handles.** Sending a speculative list adds identifiers to a broker's systems
   that may not correspond to anything they hold — the opposite of the goal.
3. Ask for the archived content, the author profile, and derived attributes
   (sentiment, demographic, interest, influence, segment membership) — not just
   the posts.
4. Ask for written confirmation if nothing matches. There is no public listing to
   re-check, so their letter is the only available evidence.

## On "it was already public"

Their note that the data *"is available publicly for anyone to find via any search
engine"* is accurate about the source posts and irrelevant to the request. The
archive, the author-level aggregation, and the inferences drawn from it are their
processing of personal information about an identifiable person. Framing it that
way — agreeing about the posts, distinguishing the derived record — keeps the
exchange cooperative, which matters with a team that is clearly willing to engage.

## Every inbound message gets the same auto-reply

Both `privacy@brandwatch.com` and the `PrivacyAutoreplyBW@` address it replies
from return the identical canned message — including a reply that is itself the
confirmation their auto-reply asked for.

**This does not prove nobody read it.** The auto-responder almost certainly fires
on every inbound message regardless of what a human does behind it. But it does
mean **you cannot tell from the mailbox whether the gate was satisfied**, which is
the practically important part: there is no artifact distinguishing "confirmed and
queued" from "sitting unread".

What to do: send the confirmation to the **monitored** address (`privacy@`) rather
than the auto-reply address, say plainly that you are re-sending because the first
attempt was auto-answered, and then wait for a human reply rather than treating any
auto-reply as progress. Record the request as submitted-pending-human-response, and
chase it if nothing personal arrives within the statutory window.

> **Correction (2026-08-25):** A duplicate-detection error in that day's run sent an unnecessary second request to `dpo@cision.com`, on top of the already-open thread documented above. The exclusion check matched only exact addresses seen in a partial Sent-folder scan, and this broker's registry `email_to` had drifted from the address actually used historically — so it looked unsent when it wasn't. No new information was requested; treat the status above as authoritative. **Lesson: check this playbook's own `Current:` status before treating a registry email_to as evidence a broker is unsent — it is not reliable on its own.**

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Crimson Hexagon
- **Trading as:** Brandwatch
- **Registered address:** 200 Vesey Street, New York, New York, 10281
- **Filed contact email:** dpo@cision.com
- **Filed phone:** 2122292240
- **Website:** www.brandwatch.com

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
