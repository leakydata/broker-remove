# 33across

- **Opt-out:** https://udp.33across.com/udp_opt_out
- **Email:** privacy@33across.com (verified)
- **Method:** web_form — Web form.
- **Domain:** 33across.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-26)
- Reference: `gmail:1a03dfc22c483e9e`
- Note: 2026-08-26: replied with adtech boilerplate from Privacy+noreply@33across.com pointing at their cookie opt-out page. That is an ad-PREFERENCE signal for one browser, not a deletion - after setting it they still hold the hashed emails, device/CTV ids, segments and the edges between them. Answered with the distinction stated plainly and three line-answerable asks: hash the four new addresses themselves rather than concluding no-match from plaintext, delete the EDGES not only the nodes, and say whether it is deletion or suppression.

## Steps

1. Email `privacy@33across.com` with the **adtech variant** of the letter, not the
   people-search one. The difference matters — see below.
2. Demand deletion of the identifier types they actually hold: cookie IDs, mobile
   advertising IDs, hashed email identifiers, and inferred audience segments.
3. Ask them to search **hashed forms** of each address. An adtech platform that
   "has no record of your email" may hold its MD5 and SHA-256 digests, which is
   the same record by another name.
4. Ask them to propagate the deletion to DSP and SSP partners the identifiers were
   syndicated to, and to say which.
5. Their opt-out page at `https://udp.33across.com/udp_opt_out` is a separate,
   weaker action — take it as well, but do not let it stand in for the request.

## Gotchas

They auto-acknowledged, and the acknowledgement framed the request as **interest-
based advertising choice**. That framing is the thing to push back on.

An adtech opt-out and a deletion request are different in a way that is easy to
lose: opting out of targeting stops them *acting* on the profile while leaving the
profile intact, and it is usually implemented as a cookie — which dies with the
cookie jar, the browser or the device. Deletion removes the record. A reply that
says "you have been opted out" has answered a question you did not ask.

**Identity-keyed, not name-keyed.** This is the category distinction that governs
everything here (`_CATEGORY_VARIANTS.md`): a people-search site indexes a person
by name and address, and an adtech platform indexes a device or a hashed email.
Sending the people-search letter gets a truthful "we hold no record under that
name" that is completely uninformative.

Follow-up needed: press them to state, in writing, whether identifiers were
deleted or merely suppressed from targeting, and whether the deletion reached
downstream partners. An opt-out that only binds 33Across leaves copies wherever
the segments were sold.

## Verification

There is nothing to search — you cannot look yourself up in an adtech platform,
which is exactly why the written answer carries the whole weight here.

Ask for confirmation naming the identifier types deleted, and the downstream
partners notified. Re-check the opt-out cookie after any browser or device change;
if the opt-out was cookie-based, that change silently undid it.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** 33Across, Inc.
- **Registered address:** 228 Park Avenue South PMB 74008, New York, NY,
  10003
- **Filed contact email:** privacy@33across.com
- **Filed phone:** 18882974094
- **Website:** www.33across.com

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
