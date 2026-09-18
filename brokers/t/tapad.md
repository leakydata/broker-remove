# Tapad

- **Email:** privacy@tapad.com — verified against their own published page
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** tapad.com
- **Priority: 2.**

## Status

- Current: `replied` (updated 2026-09-07)
- Reference: `gmail:1a07b10551f356bb`
- Note: DEVICE-RESET QUESTION SENT 2026-09-07, second of the MAID-keyed cohort after Madhive, on the 20 August thread that produced ticket PRIV-106240 and an autoresponse but no substantive answer. Not a chase; a question that asks them to look nothing up. WHY TAPAD IS THE CASE THAT DECIDES WHETHER THE RESET REMEDY GENERALISES: a reset works by removing the identifier a record is keyed to, which is a complete remedy against a store holding observations against one device id and nothing else. A CROSS-DEVICE GRAPH IS BUILT TO SURVIVE EXACTLY THAT LOSS -- keeping a person's cluster intact when any single identifier changes is what makes it a graph rather than a list. So the question put to them is not whether a reset severs one edge but whether the cluster is RE-ASSOCIATED through the remaining ones: other devices, a hashed email, an IP or household signal, a probabilistic match. If yes, the general advice to reset an advertising id is materially weakest exactly where it is most needed, and consumers relying on it would have no way to discover that. See SILENT_FAILURES 397. Four questions asked: does a reset sever the linkage; is the cluster re-associated through the graph's other edges; is it a severance or a deletion; does it reach downstream to a cluster already delivered to a client. A no to the first or a yes to the second was stated to be just as useful and will be recorded without pressing. THE REFUSAL RESTATED IN THE FORM THAT FITS THIS COMPANY: supplying one identifier to a business whose product is joining identifiers does not merely disclose one device -- it offers a fresh, dated, SELF-ATTESTED SEED, a confirmed link between a named person and a device, which is the single most valuable input a cross-device graph can receive. Of every company in this project Tapad is the one where handing over the key would do the most work against the request. ALSO ASKED, unresolved since August: the letter went to privacy@tapad.com and the ticket came back on an EXPERIAN MARKETING SERVICES Atlassian instance. If Experian is now the controller, the request belongs with whoever answers for that -- asked which entity owns it rather than assuming a group request covers it. Same question Throtle/IQVIA, MediaMath/Infillion and LiveIntent/Zeta each turned out to need.

## Steps

Email gets you a ticket; it does not get you a removal. `privacy@tapad.com`
raises a Jira issue on an **Experian Marketing Services** Atlassian instance
(`PRIV-` prefix) and returns an autoresponse redirecting all Access and Deletion
requests to the portal at `crportal.tapad.com`.

1. Open `https://crportal.tapad.com/#/` and scroll to the bottom — the three
   entry buttons (**EMAIL**, **COOKIE or MOBILE ADVERTISING ID**, **IP Address**)
   are below several screens of instructions.
2. Choose **EMAIL**. It is the only path that needs nothing from the device.
3. Set Request Type. Choosing **Deletion** or **Data Access** makes a
   **Signature** canvas appear that was not there a moment before; **Opt Out**
   does not — their page says opt-out requests do not require a Certification
   Form.
4. Set Country, then the email address.
5. Remaining: draw a signature with the mouse, tick the reCAPTCHA, Submit.

The signature certifies **under penalty of law** that you own the address. Stage
it and hand off — that attestation belongs to the person, not to the tooling.

## Gotchas

- **One identifier per submission.** Twelve addresses means twelve runs, each
  with its own signature and CAPTCHA.
- **The certification text changes with the path.** On the Cookie/MAID path you
  certify ownership of the *devices*; on the Email path, ownership of the
  *email*. Read which one you are signing.
- **They say they hold no name.** "Tapad does not know your name or known
  identity details, we rely on device identifiers." So do not lead with a name —
  it is not a key here, and a name-shaped request invites a true "no record".
- **"No clear text email" is not "no email".** The portal states they hold
  encrypted emails and use the address you type to find them. That concedes the
  hashed-email point rather than refuting it — see `_DEFLECTIONS.md` §41.
- **The sixty-day cascade is the real limit, and only the portal discloses it.**
  An opted-out ID is out "in perpetuity", but related IDs are removed for
  **sixty days only**, after which they "follow our standard data ingress
  rules". The node is permanent; the cluster is not. In a cross-device graph
  that is the difference between a deletion and a pause.
- **IP-address opt-outs expire at twelve months** and public IPv4 addresses
  rotate between households, so that path is worth little.
- **UK/EEA is out of scope entirely** — they state they ceased UK/EEA data use
  on 1 August 2021 and deleted what they held.

## Verification

No public profile to search. The observable is their written answer to the
sixty-day question: after day sixty, does the linkage between the remaining
members of the cluster still exist? A yes converts this from a completed request
into an open one, and tells you which request type to file instead.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Tapad
- **Registered address:** 475 Anton Blvd, Costa Mesa, IL, 60067
- **Filed contact email:** [named individual]@experian.com
- **Filed phone:** 714-830-7000
- **Website:** www.experian.com

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
