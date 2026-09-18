# Real Performance Marketing

- **Email:** ConsumerInquiries@RPMleader.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** rpmleader.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-19)
- Note: COMPLETE DEAD END, and an unusually well-documented one. All THREE addresses their own privacy policy publishes are rejected by their own Proofpoint mail server with the same code: 550 5.7.1 'Recipient address rejected: User email address is marked as invalid' - ConsumerInquiries@, connect@ and info@rpmleader.com. Note the code. That is 5.7.1, a POLICY rejection, not 5.1.1 user-unknown: the mail server has these addresses on file and is configured to refuse them. Then the web route: the only form on the site is a SALES enquiry form, and its required 'I am' dropdown offers Agency, Affiliate, Affiliate Network and Brand Platform - THERE IS NO CONSUMER OPTION. Filled the form with the full request in its free-text box and submitted; it errored on the missing required dropdowns. I will not select 'Agency' or 'Affiliate' to get past it, because that is a false statement about who is asking and it would taint the request. So: no working address, and no form a member of the public can honestly complete. The remaining lever is their own admission - 'Company acts as a data broker, as that term is defined in California Civil Code section 1798.99.80 et seq.' - which puts them on the California data-broker register with its own statutory contact obligations. Also captured: their header links to an Inc. profile for BEST CASE LEADS, a trading name the privacy policy never mentions.

## Steps

**There is no route a member of the public can use.** Recorded so nobody
re-derives it.

1. **All three addresses on their own privacy policy are rejected by their own
   mail server** — `ConsumerInquiries@`, `connect@` and `info@rpmleader.com`, each
   with `550 5.7.1 Recipient address rejected: User email address is marked as
   invalid` from `mx1-us1.ppe-hosted.com`.
2. The only form on the site is a **sales enquiry form** at `/contact-us-1`, and
   its required `I am` dropdown offers *Agency, Affiliate, Affiliate Network,
   Brand Platform* — **no consumer option**.
3. What is left is their own admission that they are a registered California data
   broker.

## Gotchas

**Note the SMTP code: 5.7.1, not 5.1.1.** That distinction matters and it
is easy to skim past. `5.1.1` is *user unknown* — the mailbox does not exist.
`5.7.1 ... address is marked as invalid` is a **policy rejection**: the mail
system knows about the address and is configured to refuse it. All three
published addresses fail the same way, which points at a recipient-validation
list that simply does not include the addresses the company publishes.

Practical consequence: **there is no address worth guessing at this domain.** A
`privacy@`, `legal@` or `dpo@` probe will fail identically, because the failure is
not about which mailbox exists.

**The sales form cannot be completed truthfully.** Its required capacity dropdown
has four business categories and nothing for a member of the public — the same
shape as Nielsen's rights form, but here it blocks submission outright rather
than merely misfiling the request. The full request was written into its
free-text box and the form was submitted; it errored on the missing dropdowns.

> **Do not tick "Agency" to get past it.** It is a false statement about who is
> asking, it is exactly the misrepresentation these forms exist to prevent, and a
> request obtained that way is worth less than no request — it hands them a clean
> reason to disregard it.

**The lever that remains is their own privacy policy**, which states:

> *"Company acts as a data broker, as that term is defined in California Civil
> Code section 1798.99.80 et seq."*

That is a self-declaration of registration with the California Privacy Protection
Agency, and registration carries statutory obligations about being contactable.
A broker that publishes three addresses and refuses all three is a straightforward
complaint — see the handoff note. Whether it is worth filing is the subject's
call, not an agent's.

**Trading name worth recording:** the site header links to an Inc. profile for
**Best Case Leads**, a name the privacy policy never mentions. Company badges and
award links in a header are a cheap source of alternate trading names.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** FADILAW MARKETING, LLC
- **Trading as:** Best Case Leads, RPM: Real Performance Marketing
- **Registered address:** 12243 Queenston Blvd. Suite I, Houston, TX
- **Filed contact email:** [named individual]@rpmleader.com
- **Website:** https://www.rpmleader.com

*Source: `data/registries/registry2024.csv`.*

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
