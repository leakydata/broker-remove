# AcademixDirect

- **Email:** tp-compliance@academixdirect.com
- **Status: CONFIRMED REMOVED** — *"Your data has been removed from our system and
  your opt-out has been completed."*
- **Priority: 2.** Education lead generation.

## Why this entry matters more than the removal itself

**No request was ever sent to AcademixDirect.** The confirmation arrived unprompted.

The only plausible route is downstream propagation: the standard letter asks
brokers to *"DIRECT any service providers and third parties to whom you have sold,
shared, or otherwise disclosed my personal information to do the same."* One of the
lead-network recipients passed the request along, and it reached a company we did
not know held the data.

Two things follow:

1. **Keep the downstream-propagation clause in every letter.** It reaches brokers
   that are not in any registry, which is the part of the long tail no list covers.
2. **Watch the inbox for confirmations from companies you never contacted.** They
   are evidence the clause is working, and each one identifies a broker worth
   adding to the registry — as this one was.

> **Correction (2026-08-25):** A duplicate-detection error in that day's run sent an unnecessary second request to `tp-compliance@academixdirect.com`, on top of the already-open thread documented above. The exclusion check matched only exact addresses seen in a partial Sent-folder scan, and this broker's registry `email_to` had drifted from the address actually used historically — so it looked unsent when it wasn't. No new information was requested; treat the status above as authoritative. **Lesson: check this playbook's own `Current:` status before treating a registry email_to as evidence a broker is unsent — it is not reliable on its own.**
