# Mugshotlook

- **Opt-out:** https://www.mugshotlook.com/api/helper/optOutLight/search
- **Email:** support@mugshotlook.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** mugshotlook.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Arrest/mugshot publisher. Used the split ask from _CATEGORY_VARIANTS: conceded the public record at source is not theirs to alter, then separated hosting a page from making it findable by name, and asked for de-indexing as a distinct fallback if deletion is refused. Also asked the Local Crime News question explicitly - is the opt-out a STANDING suppression applied to future feeds, or a removal of what matches today - and supplied the age as well as the DOB, since booking records are hand-transcribed.

## Steps

1. Email `support@mugshotlook.com`. You get a template reply within minutes — the
   SAME template InmatesSearcher sends. It will not answer your questions.
2. Opt-out is at `/api/helper/optOutLight/search` — first name, last name, city
   (required) and state. A text-image CAPTCHA blocks the SEARCH itself.
3. Submit an email address against the listing, then **REPLY** to the
   acknowledgement email. Clicking is not enough and there is nothing to click.
4. Fallback if the web route fails: they offer a phone line, 8am–11pm EST.

## Gotchas

Same operator as InmatesSearcher, same flow, same reply-not-click confirmation — and
the template answers none of the questions actually asked. Below.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Same operator as InmatesSearcher

The reply is **word for word** the one InmatesSearcher sends: *"It's my pleasure to help
you out today"*, the reply-to-confirm instruction with **NOT** capitalised, the
browser-cache advice, and the closing line that *"all information contained in our
database is public information, so you may need to perform a similar action with other
non-affiliated data providers also"*. Only the signature name, the street address
(Woodland Hills rather than Glendale) and the telephone number differ.

The decisive tell is not the template but the URL: both brands run their opt-out at
`/api/helper/optOutLight/search`. Nobody white-labels an internal API helper route. See
`_BROKER_FAMILIES.md`.

## The template does not answer the letter

The request asked two specific things — is the opt-out a **standing suppression** applied
to future booking feeds, and is **de-indexing** available if deletion is refused. The
reply addresses neither. It is dispatched on receipt, not written in response.

**Read that as a property of the desk, not a refusal.** There is no point re-arguing the
same points into the same template; the useful moves are the self-service flow, and the
telephone line they volunteer for when it fails.

## The flow's own hazards, inherited from the sibling

  - the **CAPTCHA is on the search**, so you cannot even learn whether a listing exists
    without a human clearing it;
  - **city is required** despite the instructions implying name and state suffice;
  - the confirmation is a **REPLY**, not a click — *"If you do not respond to the email,
    your listing will NOT be removed"*;
  - their cache advice is real: verify with a fresh search in a clean session, never a
    saved link. See `_SILENT_FAILURES.md` §31.

Their stated definition of a negative is also worth keeping: *"If you are unable to
locate your listing then it means your information was never collected, or has already
been removed."*

