# DatabaseUSA

- **Opt-out:** https://privacycompliance.biz/other-dbusa/
- **Method:** web_form — Web form.
- **Domain:** databaseusa.com
- **Priority: 4.**

## Status

- Current: `submitted` (updated 2026-08-26)
- Note: 2026-08-26 BOUNCE: the supplementary letter failed - privacy@databaseusa.com returned 550 5.1.1 'User unknown in relay recipient table'. Domain and MX are healthy (Intermedia Exchange, shared with researchusallc.com); the MAILBOX does not exist. This is the SILENT_FAILURES 88 pattern, invisible to any domain-level check. IMPORTANT - NO FALSE RECORD HERE: the original 2026-08-18 'submitted' was NOT an email. It was a completed end-to-end submission through the privacycompliance.biz portal with all three rights enabled, so that request stands and this bounce is the first ever attempt at the email address. Registry row updated: email_to cleared, email_verified_by set to 'bounced', and the reason written into notes so nobody re-adds it. Supplement re-staged as a portal handoff. CONSEQUENCE: my letter had asked DatabaseUSA to extend the request to ResearchUSA, and since it never arrived, ResearchUSA needs its own - its filed address is privacy@researchusallc.com on the same mail tenant, so it may be dead too.

## Steps

Three stages, all automatable except reading the verification email.

1. **Start at** `https://privacycompliance.biz/other-dbusa/` — email, full name,
   state, Send. An invisible reCAPTCHA sits on it and does not challenge.
2. **Open the emailed link** from `OptOut@privacycompliance.biz`. It expires in
   **24 hours** and is single-use.
3. **Fill the verification form.** Choose *For Myself* and *Residential Address*,
   then name, date of birth, address, email (must match what you submitted) and
   telephone. Gender is offered but was left blank without objection.
4. **Enable all three toggles**, each of which pops its own confirm dialog:
   - Opt-Out of the sale of my data
   - Delete my personal information
   - I want to know what categories of information have been collected about me
5. Submit. Stated timelines: **opt-out within 15 days, deletion within 45 days.**

`Add Additional Addresses` accepts up to **3 addresses** for the same person — use
it for address history, or run the flow again for the rest.

## Gotchas

**How this broker was found is the reusable part.** It is not in any of the source
lists this project started from. `privacy@infofree.com` bounced, so the next step
was reading Infofree's site for another route — and their privacy link points at
`privacycompliance.biz/other-dbusa/`, a DatabaseUSA portal. A bounce sent us
looking, and looking found a broker nobody had listed.

**Three separate toggles, not a single-select.** Opt-out, deletion and disclosure
are independent switches and all three can be enabled in one submission. Compare
`dataaxle.md`, where the same rights are a dropdown and each costs its own
submission. Same rights, same industry, opposite defaults — and only one of them
lets a consumer get what they actually asked for in one pass.

**The verification email's plaintext part contains no link.** Its text reads *"You
can complete the opt out by going to the following link"* — and then stops. The
link exists only in the HTML part. A plaintext mail client shows an instruction to
click something that is not there, which is a complete dead end for anyone reading
mail that way. Take the href from the HTML part; see `_SILENT_FAILURES.md`.

**The link expires in 24 hours.** Not a problem for an attended run; fatal for a
queued hand-off left overnight.

## What they say they collect

Their disclosure page is unusually candid, and worth keeping as evidence of what
this category of business actually holds:

| Category | Examples they list |
|---|---|
| Contact | Name, Title, Address, Phone, Email, **Geo-Spatial Information** |
| Individual | Month & Year of Birth, Age, Education, Gender, Occupation, **Ethnicity, Religion, Political Party**, Veteran Present in Household |
| Household | Dwelling Type, Homeowner/Renter, Length of Residence, Marital Status, Pets, **Presence of Children, Children's Age**, Household Size |
| Income / Financial | Estimated Income, **Estimated Net Worth**, Investment Properties, Discretionary Income |
| Property | Home Value, Square Footage, Presence of Swimming Pool, Utilities |
| Mortgage | Purchase Date and Amount, Loan Date, Amount, Type, **Interest Rate** |
| Donor | **Religious Donors, Political Donors**, Charitable Donors |
| Credit Card | Presence of Major, Gasoline, Department Store, Premium cards |
| Interests, Buying Activities | Hobbies, purchasing behaviour, mail-order buyer |

And the purposes, which include — stated plainly — **"Resale to Data Brokers"**.
Sources include "Public Records", "Self-Reported Information", "Warranty
Registrations" and "Data Brokers".

**Keep this page.** A broker listing ethnicity, religion, political party and
children's ages among its collected categories, and resale to other brokers among
its purposes, has documented the thing this project keeps having to argue for. It
is far better evidence than any inference drawn from outside, and it is published
by them.

## Verification

Two clocks, and they differ: **opt-out at 15 days, deletion at 45**. Diarise the
longer one, and treat a confirmation arriving before then as a receipt rather than
a completion.

The category disclosure is returned immediately on the confirmation page. If the
"specific information" report was requested instead, they state it is emailed
within 45 days of receiving the signed form.

Nothing public to search here, so the written answer is the artifact. Where a
report arrives, read it against the category table above — the gap between what
they say they collect and what they say they hold about you is itself worth
knowing.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** DatabaseUSA
- **Registered address:** 11211 John Galt Blvd, Omaha, NE
- **Filed contact email:** Privacy@databaseusa.com
- **Website:** https://www.databaseusa.com

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
