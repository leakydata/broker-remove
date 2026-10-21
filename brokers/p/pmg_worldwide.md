# PMG Worldwide, LLC

- **Email:** dataprivacy@pmg.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** pmg.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-10-21)
- 2026-10-21: The same `FM6XRMKND5` "Needs Attention" notice has now fired
  on every single day from 2026-10-11 through 2026-10-21 (several days more
  than once), eleven-plus notices total, every one unreadable without a
  browser. This is not a backlog of distinct comments -- the portal appears
  to be re-sending the same notification on a loop regardless of whether
  the underlying comment has changed. Confirms this is a broken notifier
  on PMG's OneTrust instance rather than an active conversation; still
  routed through `/dsr-form` per the 10-18 note, still queued for a human.
  Nothing new to act on by email.
- Prior (2026-10-18): Request `FM6XRMKND5` has sent six near-identical "Needs Attention"
  notices since 2026-10-11 (initial confirm, then comments on 13th, 14th, 15th,
  16th, 17th x2, 18th). Every "View request" link lands on OneTrust's access-code
  screen, which demands a distorted-image CAPTCHA before it will even email a
  code — this project does not solve CAPTCHAs, so the comment itself has never
  been read. On 2026-10-17 wrote to `dataprivacy@pmg.com` directly explaining
  this and pre-answering the four things a privacy desk usually asks (identity,
  state of residence, identifiers, scope). The reply, from
  `dataprivacy+noreply@pmg.com`, was the same canned template as Koddi/Kargo
  (see Gotchas) and named a **different, ungated route**: `https://www.pmg.com/dsr-form`.
  That is not the same URL as `optout_url` above (`/your-privacy-choices`) —
  worth checking both exist and lead somewhere real. Queued for a human via
  `handoff.py` since it needs a browser; not yet attempted.
- 2026-08-27: first contact. PMG is a media/marketing agency, so used the ad-tech variant: hashed email, advertising/cookie IDs, modelled audience segments, and asked them to confirm client campaign data and DSP/SSP partners were directed to do the same.

## Steps

1. Do not expect an email reply to answer anything — `dataprivacy+noreply@pmg.com`
   is a canned autoresponder (see Gotchas). Use whatever web form/portal it names.
2. The OneTrust portal link in "Needs Attention" emails is a dead end without a
   browser: it requires solving an image CAPTCHA just to get an access code
   emailed, before you can even read the comment. Don't burn an email round
   asking PMG to repeat the comment by email — the canned reply (if any comes)
   just repeats the form link. Go straight to the form.
3. Use `https://www.pmg.com/dsr-form`, named explicitly in the 2026-10-17
   autoresponder, rather than guessing at `/your-privacy-choices`.

## Gotchas

**`dataprivacy+noreply@pmg.com` sent the identical canned template used by
Koddi and Kargo** ("On behalf of [Company], I am writing to address your
recent inquiries concerning 'Do Not Sell or Share' requests..."). Same
boilerplate, different company name substituted — almost certainly a shared
privacy-ops vendor or template across these three. Treat any `+noreply`
sender the same way: don't spend an email round asking it a question, look
for the web form it names instead.

**The OneTrust "Needs Attention" portal is CAPTCHA-gated before you can even
read what it says.** The emailed link does not open the request directly — it
opens a "request an access code" screen behind a distorted-image CAPTCHA, and
the code it would eventually email expires in 15 minutes. Six notices arrived
over a week without the comment ever being readable. The working fallback is
PMG's own `dataprivacy@pmg.com` mailbox (filed with the CA registry) and the
`/dsr-form` link that its autoresponder names — not the OneTrust portal.

## Verification

No confirmation yet — the only reply so far is the canned autoresponder.
Nothing public to re-search (ad agency, not a listing site).

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** PMG Worldwide, LLC
- **Registered address:** 2601 Olive Street, Floor 19, Dallas, TX, 75201
- **Filed contact email:** dataprivacy@pmg.com
- **Filed phone:** 8174209970
- **Website:** https://www.pmg.com

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
