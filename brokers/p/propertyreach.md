# Propertyreach

- **Opt-out:** https://www.propertyreach.com/privacy-rights
- **Email:** compliance@propertyreach.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** propertyreach.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-19)
- Note: Email refused: 'In order to process your privacy request, please fill out the appropriate form at the link below. We do not accept privacy requests via email.' The form is a cascade of custom dropdowns and it is better designed than most: the rights list is explicit (Do Not Sell/Opt-out, Delete, Know/Access, Correct) and the capacity list includes MEMBER OF THE PUBLIC alongside PropertyReach Customer - the option Nielsen's form lacked entirely. Two structural notes: the rights selector is SINGLE-SELECT so deletion and opt-out need separate runs, and Cloudflare gates the page for about ten seconds before it paints. Could not drive it to completion under automation - the widgets are not real selects, and clicking an option's text label navigated to their Property API marketing page rather than choosing the option. Mapped the full path and handed off. Company is Property Reach, LP, 1915 21st St, Sacramento CA.

## Steps

1. **Do not email.** `compliance@propertyreach.com` replies:
   *"In order to process your privacy request, please fill out the appropriate
   form at the link below. We do not accept privacy requests via email."*
2. `/privacy-rights`. Cloudflare gates it for about ten seconds before it paints.
3. **Select The Right You Want To Exercise** → *Do Not Sell/Right to Opt-out*,
   *Right to Delete*, *Right to Know/Access*, *Right to Correct*.
4. A second dropdown appears — **Exercise my rights as a** → *PropertyReach
   Customer* or **Member of the public**. Choose the latter.
5. The remaining fields appear after that.

## Gotchas

**The rights selector is single-select**, so *Right to Delete* and *Do Not
Sell/Right to Opt-out* cannot be asked for in one submission. Run the form twice.
Same trap as Data Axle and Path2Response: one run looks complete and asks for
half of what was intended.

**Clicking an option's text label navigates away.** Clicking the label element
for *Member of the public* loaded their Property API marketing page instead of
selecting the option. The controls are custom widgets rather than real `<select>`
elements, and the option rows appear to sit over other clickable content. Click
the row, or drive it with the keyboard.

**Credit where it is due: the capacity list has the right option.** *Member of the
public* is exactly what Nielsen's rights form lacked, where every choice presumed
a prior relationship with the company (see `nielsen.md`). It costs nothing and it
is the difference between a form a data subject can answer honestly and one they
cannot. Phonebooks does the same thing with *"I have no direct relationship with
the company"*. Worth noting which operators get this right — it is a reasonable
proxy for whether the rest of the process was designed for real requests.

Company of record: Property Reach, LP, 1915 21st St, Sacramento, CA.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Property Reach, LP
- **Registered address:** 750 N Saint Paul St Ste 250 PMB 75659, Dallas,
  TX
- **Filed contact email:** compliance@propertyreach.com
- **Website:** https://www.propertyreach.com

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
