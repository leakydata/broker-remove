# Muraena

- **Email:** support@muraena.ai (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** muraena.ai
- **Priority: 1.**

## Status

- Current: `suppressed` (updated 2026-09-16)
- Note: Directory-sourced entry with no public information about what the business actually does beyond appearing in a removal-service directory. Sent the "unknown broker" categorisation letter (`_CATEGORY_VARIANTS.md`, "When you cannot tell what kind of broker it is") rather than guessing at a category.
- **Supplement (2026-09-01):** a follow-up added the one identifier the original letter had omitted — a public LinkedIn profile URL — explicitly as a suppression key rather than a search hint (see `SUPPRESS_BLOCK` in `make_optout_email.py`: a public profile is re-scraped continuously, so an exclusion keyed to nothing is undone at the next pass).
- **Reply (2026-09-15):** *"No, I wasn't able to find any of the provided emails in our DB. We have also applied suppression measures to that LI URL to prevent this information from being re-added."* A clean example of the `suppressed` status this project added specifically for this shape of outcome — nothing held, but a forward-looking suppression applied anyway on the one identifier that is itself the collection input.

## Steps

Email works. Include the public profile URL explicitly as a suppression key, not only as a search aid — that is what got the forward-looking suppression applied here even though no record existed to delete.

## Gotchas

Muraena confirmed the suppression is against the LI URL specifically, not against the person generally — if the profile URL ever changes, the new one would need to be supplied again.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
