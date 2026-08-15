# ClustrMaps

- **Opt-out:** https://clustrmaps.com/bl/opt-out
- **Method:** web form
- **Priority: 4.**

## Status
**Blocked on tooling, not on the broker.** The Claude in Chrome extension has no
site permission for `clustrmaps.com`, so the page cannot be read or acted on:
*"Permission denied for reading page content on this domain."*

Fix: grant the domain in the extension, or complete this one by hand.

## What it exposes
ClustrMaps is **address-centric** — it publishes who lives (or lived) at a given
street address, alongside neighbours and prior residents. That means:

- Removing your name may still leave the **address page** intact and linking to you
- Ask for removal of the *address association*, not just a name listing
- Prior addresses matter as much as the current one

## Gotchas
- No verified privacy email recorded yet — find the real one before mailing rather
  than guessing `privacy@clustrmaps.com`. See CONTRIBUTING.md on why a guessed
  address is worse than no address.

## Verification
Re-check the address page itself, not only a name search.
