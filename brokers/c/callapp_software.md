# Callapp Software Ltd

- **Opt-out:** https://callapp.com/support/can-i-wipe-my-information-from-callapp-2
- **Email:** support@callapp.com (verified)
- **Method:** unknown — Route not yet established.
- **Priority: 1.**

## Status

- Current: `submitted` (updated 2026-09-12)
- Note: Letter to support@callapp.com 2026-09-12, opening with the fact that the subject is a NON-USER and framing that as the request rather than a reason to close it. Caller-ID services build their directory from the address books of people who install them, so the likeliest route in is someone else uploading their contacts -- a person who was not the subject and had no authority. Asked them not to check the user table but the CONTACT GRAPH. Four asks: delete, opt out, UNLIST the numbers from lookups, and suppress against re-upload, with the point made that in a contributed-directory model a deletion is temporary by construction. Also asked for a COUNT of how many address books he appears in, explicitly not the names. Offered SMS verification of the current number; refused ID, account and device identifiers up front.

## Steps

1. THERE IS A SELF-SERVICE PAGE and it is probably faster than the letter:
   https://callapp.com/support/can-i-wipe-my-information-from-callapp-2
   Not yet attempted -- browser automation was unavailable on 12 September. Try
   this before chasing the email.
2. Email `support@callapp.com` (sent 2026-09-12). The letter is written for a
   NON-USER, which is the case that matters here.

## Gotchas

- **The user table is the wrong place to look.** A caller-ID directory is
  assembled from the address books of people who install the app, so a non-user
  is in it because somebody ELSE uploaded their contacts. "We have no account
  for you" is a truthful answer to a question nobody asked.
- **A deletion here is temporary by construction.** The same contact syncs again
  next week and the entry returns, with no further act by anyone. The thing to
  ask for is a persistent unlisting or suppression keyed to the number, and to
  make them use that word rather than "deleted".
- Verification by SMS code to the current number is acceptable and was offered.
  ID upload, account creation and device identifiers were refused up front.

## Verification

Ask them to state which numbers matched. There is no public search page to
re-run from outside, so the only check available is their own answer -- which is
why the letter asks for a control query (an identifier they KNOW is in the table,
run the same way) rather than a bare nil.
