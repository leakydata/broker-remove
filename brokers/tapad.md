# Tapad

- **Email:** privacy@tapad.com — verified against their own published page
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** tapad.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: Sent 2026-08-20 05:35 UTC to privacy@tapad.com. Cross-device identity graph (Experian). Letter argues the graph EDGES are the personal information, not just the identifiers: deleting named seed identifiers while leaving the probabilistic cluster (device IDs, cookie IDs, CTV IDs, IP-derived household associations, inferred household members) intact is not a deletion, because the cluster is a record the system generated about me and any surviving member re-attaches it on the next observation. Three asks: delete identifiers including MD5/SHA-1/SHA-256 of each address (hashing is not de-identification when the input space is a known email); dissolve the cluster rather than remove from it; standing do-not-re-onboard. Quoted their own tagline 'Connecting brands to consumers across devices'.

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
