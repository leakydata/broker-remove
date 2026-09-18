# Affinity Solutions

- **Email: refused.** *"For privacy and security reasons, Affinity Solutions does
  not accept privacy requests via email."*
- **Working route:** OneTrust web form, linked from
  <https://www.affinity.solutions/data-privacy-notice/>
- **Method:** web form + **text CAPTCHA** at submit, then email verification
- **Priority: 2.** Consumer purchase / card transaction data via bank partners.

## Route
1. Their auto-reply supplies a OneTrust webform URL. It is **not** gated on load.
2. Choose: *on behalf of* → **Myself**; then the right you want.
   **Only ONE right is selectable per submission** — pick Delete, and state in
   Request Details that it also constitutes Do Not Sell, or file twice.
3. Fields: address, city, country, state, zip, first/last, email, phone, **DOB**,
   Request Details (5000 chars), acknowledgement, **text CAPTCHA**, submit.
4. An email verification link follows. **The request is not processed until it is
   clicked** — point the email at a mailbox you can actually read.
5. Success page: `/trust-center-portal/#/verify/success`. Keep the **Request ID**.

## What to ask for
Bank-sourced transaction data. Use Request Details to widen scope beyond the
name-and-address record:

- transaction records, merchant-level purchase history, spend categories
- segments, scores and inferences derived from them
- **ask them to search hashed forms** of your email — identifier matching here is
  routinely done on hashed email, so a plaintext-only search can return nothing
  while they hold plenty
- ask **which financial institution or data partner supplied** your information;
  that names an upstream relationship you probably don't know exists

## Gotchas
- Request Details says "please refrain from entering any personal information" —
  odd on a privacy form. Use it for scope and instructions, not identifiers.
- Two valid domains for their mail: `affinitysolutions.com` and `affinity.solutions`.

## Email is refused; the web form is the only route

Auto-reply, verbatim:

> *"Please note that for privacy and security reasons, Affinity Solutions does not
> accept privacy requests via email. You can submit a privacy request via our
> interactive web form."*

No human appears to read the mailbox, so unlike some refusals this one is not
worth arguing — go to the form.

## The request is not filed until you click the emailed link

The form is OneTrust-hosted. On submission it issues a Request ID by email and
then requires a second step: an emailed **"Confirm email"** button. Only after
clicking does the portal say *"Your request is confirmed!"*

A request submitted here sat unverified for roughly a day and was indistinguishable
from a completed one. Do not close the loop until you have seen the confirmation
page. See `_SILENT_FAILURES.md` §2.

## Status

- Current: `submitted` (updated 2026-09-03)
- **2026-09-03 (§294):** SECOND RIGHT PRESSED BY EMAIL 2026-09-03 (SILENT_FAILURES 293/290). The OneTrust deletion is filed and email-verified (X4SPXJY2DR, right selected: Delete My Information) but THE FORM ALLOWS ONE RIGHT PER SUBMISSION, so the do-not-sell request went into the free-text details field -- and a note in a text box is not a filed request. Asked them to record the 1798.120 opt-out from the email, on the ground that it requires no verification: there is nothing to verify, a wrongly-honoured opt-out discloses nothing and harms no one, which is why it is treated differently from deletion where a mistaken match destroys the wrong person's record. Their form has already verified the address for the deletion; the opt-out needs less than that. TWO COMPANY-SPECIFIC POINTS: Affinity works with CARD-TRANSACTION DATA SOURCED FROM FINANCIAL INSTITUTIONS, so (a) the derived layer IS the product -- spend categories, merchant affinities, income and lifestyle inferences, audience segments -- and a deletion clearing an identity row while keeping the segments is a half-deletion; and (b) I never had a relationship with them, so if a record exists it arrived from a bank or card issuer I DID deal with, which ma

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Affinity Solutions
- **Registered address:** 112 West 34th Street, 18th Floor, New York, NY
- **Filed contact email:** privacy@affinitysolutions.com
- **Website:** https://www.affinity.solutions

*Source: `data/registries/registry2024.csv`.*

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://affinitysolutions-privacy.my.onetrust.com/webform/a564cfa1-53bf-4c10-bf95-cd907432d7e8/7e4e6bf3-6562-454e-8c73-6a7bd1f4b336
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `privacy@affinitysolutions.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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
