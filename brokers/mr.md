# M+R (mrss.com)

- **Email:** privacy@mrss.com — live; replies come from a named individual at the firm
- **Method:** email — statutory request by email. No web form.
- **Domain:** mrss.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- A negative was received, but a narrow one. Not `not_found` yet.

## Steps

1. Email `privacy@mrss.com`. No form, no account, no ID document.
2. A reply arrived about a day later, sent from a person's own address with
   `privacy@mrss.com` copied — so the alias forwards to a human rather than
   feeding a ticketing system.

## Gotchas

**The negative is narrow on two independent axes.** Their reply:

> "We have received and processed your access request. After searching our
> records, we did not identify any information in our databases associated with
> your name and/or address."

| clause | what it leaves out |
|---|---|
| "your name and/or address" | the twelve email addresses and twelve phone numbers the request listed. In a fundraising or marketing file the email is usually the key the record sits under, and the postal address is often absent or stale. |
| "our records ... our databases" | anything held **for a client**. M+R is an agency. Its own controller records can be genuinely empty while a nonprofit client's supporter file, sitting in M+R's systems, contains the subject. |

The second is the one that matters here, and the original letter had specifically
asked for the processor-versus-controller split. The reply does not address it.
See `_SILENT_FAILURES.md` §52, "The second axis: whose records were searched".

**It also mislabels the request** as an *access* request; it was deletion and
opt-out. Harmless while the answer is "nothing found" — it decides which process
runs the moment a recheck turns something up. Worth flagging, not worth leading
with.

**The follow-up sent**, deliberately short and unformatted because it is going to
a named person rather than a compliance desk (`_DEFLECTIONS.md` §42):

- re-run the search against the emails and phones, which were supplied again
- does the answer cover data held for clients as well as data held in their own
  right? — with **"those are the client's records, go to them"** explicitly
  offered as a complete and acceptable answer

That exit is the point. It costs them nothing to take, it avoids an argument
about who controls what, and a named client is a better outcome than a win: it
converts one narrow negative into a new, correctly addressed request.

## Verification

No public search page. Verification is entirely the written answer. Flip to
`not_found` only if the recheck against email and phone comes back empty *and*
they confirm the answer covers client-held data — or name the client, in which
case open a new entry for that client and close this one.
