# BeenVerified

- **Opt-out:** https://www.beenverified.com/app/optout/search
- **Email:** privacy@beenverified.com
- **Method:** web form (search → select record → email confirm); email also accepted
- **Priority: 5.**

## Status

- Current: `submitted` (updated 2026-10-10)
- Reference: `gmail:1a0063929652c5ef`
- Note: REAL REQUEST SENT 2026-10-10 to privacy@beenverified.com, replacing the unearned 'confirmed' regressed earlier this pass. USED THEIR OWN FAQ AGAINST THE WEB FORM'S LIMITS, which is why email was the right channel rather than the online opt-out: (1) the FAQ states the online process permits removal of ONE RECORD ONLY and directs anyone with more to email this address -- and a thirty-year, sixteen-address history is exactly the case their own FAQ says produces multiple unmatched records; (2) the FAQ states that opting out of People Search may leave a name appearing in their OTHER search services, and the opt-out page separately names Property Search and Contact Search; (3) the FAQ admits that when a data partner supplies a record they cannot match to an existing one, it MAY APPEAR AFTER AN OPT-OUT, and invites the consumer to write again each time. So the web flow removes one record from one product with no forward protection -- asked instead for all records, all products, and a STANDING DO-NOT-ADD LIST checked on ingestion, with an explicit offer to accept 'we cannot do that' as a complete architectural answer. ALSO ASKED WHETHER THE REQUEST REACHES OWNERLY AND NEIGHBORWHO, both Lifetime Value Co. brands, both of which carry adopted 'confirmed' with no correspondence in the mailbox at all. Better to ask once than discover in six months that an opt-out covered one brand of three. WARNED THEM OFF LOOSE MATCHING and gave the reason: the Seamless.AI disclosure (464) was a composite of four or five people sharing the name, so DOB 7 January [YEAR] is the discriminator and fewer-but-correct removals are preferred to more-but-careless. Standing limit restated -- key to the name-plus-DOB association, never a bare address or number, because other people live at those addresses now. DISCLAIMED DANIEL'S LAW EXPLICITLY: they offer a covered-person route for judges, prosecutors and law enforcement; the subject is a FORMER Pennsylvania State Constable and the letter says so rather than letting anyone later think the category was stretched. Also asked for the CATEGORIES of their data partners, to write upstream rather than keep catching the same record downstream.

## Family properties — check each

BeenVerified operates several sibling brands that carry the same underlying data:

- **Ownerly** (property / home value) — `brokers/o/ownerly.md`
- **NeighborWho** (property + neighbour reports) — `brokers/n/neighborwho.md`
- **PeopleLooker**
- **NumberGuru**
- **MoneyBot5000**
- **PeopleSmart**
- **ReversePhone**

A removal on one does **not** reliably clear the others *by default* — but as of
2026-09-22, an agent stated in writing that an opt-out on one brand is applied to
all eight: "When we process an opt-out request on one brand, it applies to all
of our brands. This applies to BeenVerified, MoneyBot5000, NeighborWho,
NumberGuru, Ownerly, PeopleLooker, PeopleSmart, and ReversePhone." Worth citing
back if a sibling brand later claims no record of a request filed elsewhere in
the family. File separately for the siblings only if that claim is contradicted.

**2026-09-30, independently confirmed via a third-party property.**
`freephonetracer.com` publishes BeenVerified's support address as its own
privacy contact and is "now powered by NumberGuru" (same Lifetime Value Co
family). A reverse-phone-number request (searched on 8 former numbers, not
name — the right key for a reverse-lookup site) got a concrete result:
"We have removed the requested phone numbers from our search results. This
change should be reflected within 24 hours," followed by the same
whole-family statement again, naming BeenVerified, PeopleLooker, PeopleSmart,
NeighborWho, Ownerly, and ReversePhone specifically (MoneyBot5000 and
NumberGuru not repeated this time, but covered by the 2026-09-22 list above).
This is a second, independent instance of the family-wide claim — reasonable
to rely on without re-filing to each sibling, but if any sibling later denies
having a record, cite both dates back to them.

## Gotchas
- Web opt-out requires an emailed confirmation link — unconfirmed requests are
  void. Point the confirmation at a mailbox you can actually read.
- The web flow surfaces multiple candidate records for a common name. Match on
  prior cities and relatives, not the name alone.

## Verification
Re-search beenverified.com, and separately check Ownerly and NeighborWho, after
~7–14 days.

## Email is answered by a named human, and partially actioned

A Zendesk ticket answered by a named agent within days. The reply pattern is worth
knowing because it looks like a refusal and is not:

> *"We are unable to locate a full record that directly corresponds with the
> combination of the first name, last name, age, and/or address information you
> provided."*

followed, further down, by:

> *"In the meantime, we have opted-out the other individual pieces of information
> that you provided to us"*

— listing the email addresses and telephone number, which **were** suppressed. So a
standard letter gets the identifiers actioned even when the person record is not
matched. Record it as partial, not failed.

## They match on name + age + city/state

That is the join key, and it is not what a standard opt-out letter contains. When
they ask for more, send:

- **age as a number**, not only a date of birth;
- a **bare list of cities and states**, separate from full postal addresses;
- the **complete address history** — with a long one, the record is most likely
  filed under a former address, which is usually why the match failed;
- every alias form of the name.

See `_DEFLECTIONS.md` §15.

## The profile-URL ask

They also offer *"provide a link to the page where you see your name"*. Reasonable,
but declining is fine: say you have not located the listing and would rather not
buy a report to exercise a privacy right, then give the identifier combination that
disambiguates you.

## Ask whether it is suppression

*"We have opted-out the other individual pieces of information"* does not say
whether those identifiers are blocked against future ingestion or merely removed
now. Ask explicitly, and ask how many records matched.

## Scope

Part of a group operating several people-search brands. Ask for the request to be
applied across all group properties — one ticket can cover several sites, and the
same reply template appeared from two of their brands on the same afternoon.

## Two searches, everything they asked for, still "unable to locate"

They asked for full name, age, and the cities and states the information is
listed under. All of it was supplied — plus name variants, date of birth, ten
addresses spanning about twenty-five years, twelve phone numbers and eight email
addresses. The second reply was the same as the first:

> *"It seems that we are still unable to locate a full record that directly
> corresponds with the combination..."*

At that point the exchange has to be forced to a conclusion, because an
unfulfilled request and an empty database are indistinguishable from outside.
There are only two honest positions and both are acceptable:

1. **They hold nothing** — then ask for that in those words, and record
   `not_found`. A written "we hold no record corresponding to this person" is a
   real artifact and is worth as much as a deletion.
2. **A record exists that these identifiers do not reach** — then ask which
   identifier would reach it.

## The profile-URL catch-22

Their fallback is to ask for *"a link to the page where you see your name"*.

Name the difficulty rather than complying: they are asking the consumer to find,
on their site, the listing they have just said they cannot find in their own
database. If it is there, the operator is better placed to locate it; if it is
not, the first answer applies. The same catch-22 turns up at Veripages — see
`veripages.md`.

**The partial success is real, though.** They opted out the individual email
addresses and the telephone number while failing the person match, which is more
than most do. Two follow-ups worth making every time this happens:

- Is the opt-out a **suppression against future re-listing** or a one-time
  removal? Only the first survives an upstream refresh.
- Does it cover **all** the addresses supplied, or only those echoed back?

**Both follow-ups got clean answers on the third round (2026-09-22).** "We hold
no person search result (i.e. person report) corresponding to you" (a genuine
nil, not another catch-22 profile-URL ask); the opt-outs already applied "are
suppression against future re-listing"; and "yes, the opt-out covers all of the
email addresses you supplied." Pushing past the first two "unable to locate"
replies to a direct third question — hold nothing, or tell me what would reach
it — is what got a plain answer instead of a third repetition of the template.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** BeenVerified, LLC, The Lifetime Value Co. LLC, its
  subsidiaries and affiliates
- **Trading as:** BeenVerified.com
- **Registered address:** 48 West 38th Street, 8th Floor, New York, NY
- **Filed contact email:** legal@ltvco.com
- **Filed phone:** 347-931-2725
- **Website:** https://www.beenverified.com

*Source: `data/registries/registry2024.csv`.*

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.beenverified.com/svc/optout/search/optouts
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `legal@ltvco.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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
