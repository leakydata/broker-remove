# Broker families — one letter can cover dozens of sites

Many "different" data brokers are one company running a template across every US
state. They share a single privacy contact, so **one well-scoped letter naming
every property covers all of them** — and is far more likely to be actioned than
fifty near-identical emails landing in the same inbox on the same morning.

## Families found so far

| Contact | Sites | What they are |
|---|---|---|
| `privacy@courtrecords.us` | **51** | `<state>courtrecords.us` for every state |
| `privacy@infotracer.com` | **48** | InfoTracer + `<state>arrests` for every state |
| `contact@licensedata.org` | **10** | California professional-licence sites (nursing, contractors, firearms, notaries…) |
| `support@mailer.intelius.com` | 5 | PeopleConnect: criminalrecords.com, publicrecords.com, reversephonelookup, snoopstation, peoplefinder |
| `support@verifyrecords.com` | 4 | verifyrecords, verifypublicrecords, arrestwarrant.org, texaswarrantroundup.org |
| `privacy@eab.com` | 2 | EAB, Appily |
| `notice@tunnldata.com` | 2 | Tunnl, Deep Root |

**120 brokers reachable through 7 addresses.**

## Finding them

Group pending brokers by `email_to` in `data/brokers.json` — any address with more
than one broker attached is a family. Worth re-running as the registry grows.

## Writing the letter

- **Name every property explicitly.** "All properties you operate" invites a
  narrow reading; an enumerated list does not.
- **Ask which properties held a record.** The answer maps the family for you and
  surfaces sites the registry may have missed.
- For arrest, warrant and court-record families, also ask them to **disclose any
  entry attributed to you and its source** — not only to remove it. A common name
  attracts misattribution, and you cannot correct a record you have never seen.
- Send **one** letter per family. Fifty separate emails to one privacy team reads
  as a mail flood and gets triaged accordingly.
