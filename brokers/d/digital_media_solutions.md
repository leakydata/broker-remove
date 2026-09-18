# Digital Media Solutions

- **Opt-out:** https://dms-privacy.my.onetrust.com/webform/506f8b15-11ff-4f18-95fa-48ff903e623f/4268d0f0-bd98-4afb-b33a-a7a922ae182a
- **Email:** autodelete@dmsgroup.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** dmsgroup.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-17)
- Note: Sent to [named individual]@dmsgroup.com. The mailbox name suggests automated processing, so the letter asks explicitly what format their parser needs and warns that acting only on the sending address would leave seven of eight addresses untouched with no way to tell from the confirmation. Lead-gen variant otherwise.

## Steps

1. Email `[named individual]@dmsgroup.com`.
2. Ask, in the letter itself, **what format the parser expects** and whether it
   handles more than one identifier per message.
3. Use the lead-gen asks: acquisition source, downstream recipients, permanent
   suppression rather than one-time deletion.

## Gotchas

The mailbox is called **autodelete**, which is a useful piece of information
before you have any reply at all: the request is likely being parsed by a machine
rather than read by a person.

That matters because of how an automated processor typically fails. It does not
error — it succeeds on the part it understood. The plausible failure here is that
it acts on the **sending address** and ignores the seven other addresses in the
body, then returns a confirmation that says the request was completed. Which it
was, for one eighth of it.

**This is the silent-failure shape that is hardest to catch** (`_SILENT_FAILURES.md`
§4): the confirmation is genuine, the work was really done, and the scope was
quietly reduced to whatever the parser could see. Nothing in the reply tells you
which happened.

So ask up front, in the request: what format do you need, and does one message
cover multiple identifiers? A processor that only handles one identifier per
message is a fine constraint to work within — but only if you know about it.

## Verification

Ask for the **list of identifiers acted upon**, echoed back. Not "your request has
been completed" — the actual list. That is the only way to distinguish a full
deletion from a parser that saw one address.

If the reply names fewer identifiers than were sent, resubmit one message per
identifier and keep each confirmation separately.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Digital Media Solutions
- **Registered address:** 4800 140th Ave N Ste 101, Clearwater, FL
- **Filed contact email:** legal@dmsgroup.com
- **Website:** https://www.digitalmediasolutions.com

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
