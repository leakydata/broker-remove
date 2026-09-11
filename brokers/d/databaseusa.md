# DatabaseUSA

- **Opt-out:** https://privacycompliance.biz/other-dbusa/
- **Method:** web_form — Web form.
- **Domain:** databaseusa.com
- **Priority: 4.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Discovered via infofree.com, which links its privacy route to this portal. Completed privacycompliance.biz end to end with all three rights enabled: opt-out of sale (15 days), deletion (45 days), and disclosure of categories collected. Their disclosure page is unusually candid - see the playbook.
- **Correction (2026-08-29):** a separately CA-registered `databaseusa` entry (this same company, registered under its own name rather than found via infofree.com) had never actually been emailed and its registered address, privacy@databaseusa.com, hard-bounced (550) when tried. No dedicated privacy mailbox is published anywhere on their site — only a general inbox (info@databaseusa.com) and this same privacycompliance.biz portal. Sent a short secondary email to info@databaseusa.com naming the portal and this already-completed submission, so the two threads read as the same request rather than a fresh one. Status stays `submitted` on the strength of the portal completion; this was a duplicate-effort near-miss from the registry carrying the company under two unconnected entries.

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
