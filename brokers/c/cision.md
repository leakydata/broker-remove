# Cision

- **Email:** privacy@cision.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** cision.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-17)
- Note: Auto-reply gate (same template as sister company Brandwatch): nothing proceeds without an explicit confirmation reply. Sent to the monitored privacy@ address. KEY DIFFERENCE from Brandwatch: Cision indexes journalist/influencer records by NAME, EMAIL and social handle, not handles alone, so the standard letter is directly actionable here.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `dpo@cision.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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

## Same auto-reply gate as Brandwatch — and the same trap

Cision owns Brandwatch, and both use an identical auto-responder template. It
opens *"We confirm receipt of your message"* and then, further down:

> *"If you believe we have collected data on you as a Journalist or Influencer,
> please reply to this email indicating your desire for us to proceed with your
> request."*

**Nothing is processed until you send that reply.** See `_SILENT_FAILURES.md` §5.
Send the confirmation to `privacy@cision.com`, not to the `PrivacyAutoreply`
address it arrives from — replying to the auto-responder just triggers it again.

## Crucial difference from Brandwatch: they index on name and email

This is the sentence that matters, and it is the opposite of its sister company's:

> *"We index your information by your name, email address, and social handle."*

Brandwatch indexes **social handles only** and says so explicitly, which makes a
standard opt-out letter unanswerable there. Cision indexes **name and email as
well**, so the ordinary request — name, addresses, every email address — is
directly actionable. No handles required.

Do not assume sister companies share a data model. The two auto-replies are
word-for-word identical in structure and differ on exactly the point that decides
whether your letter can be answered.

## The two categories

**Users (customers/prospects)** — *"we only process and index upon business email
addresses. If your email address is a personal email address, we can confirm that
we would not have collected any data related to you."* Genuinely empty for a
private individual; accept it.

**Journalists and Influencers** — the category that applies to anyone whose byline,
public profile or published content has been scraped. *"The Cision product collects
only publicly available contact details and articles and content you have
published."*

Answer both explicitly, or a truthful "no records" may address only the category
you did not mean.

## What to ask for

Beyond the contact record: **beat and topic classifications, outlet affiliations,
and influence/reach/engagement scores.** These are Cision's own inferences, they
are what subscribers pay for, and they outlive a deleted contact row.

Also ask for platform-level **do-not-contact suppression** — subscribers run
outreach campaigns through the platform, so suppression stops the email even where
a record legitimately remains.

## On "it was already public"

> *"The data that we collect is available publicly for anyone to find via any
> search engine."*

True of the source articles, irrelevant to the request. Concede the point about
the originals — they are not Cision's to remove — and distinguish the compiled
profile, the contact details as held, and the derived scores, which are.

> **Correction (2026-08-25):** A duplicate-detection error in that day's run sent an unnecessary second request to `dpo@cision.com`, on top of the already-open thread documented above. The exclusion check matched only exact addresses seen in a partial Sent-folder scan, and this broker's registry `email_to` had drifted from the address actually used historically — so it looked unsent when it wasn't. No new information was requested; treat the status above as authoritative. **Lesson: check this playbook's own `Current:` status before treating a registry email_to as evidence a broker is unsent — it is not reliable on its own.**

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Cision
- **Registered address:** 300 S Riverside Plaza, Suite 300, Chicago,
  Illinois, 60606
- **Filed contact email:** dpo@cision.com
- **Filed phone:** 866-639-5087
- **Website:** https://www.cision.com

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
