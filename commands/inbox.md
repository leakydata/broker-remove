---
description: Triage broker replies — bounces, deflections, confirmations, verification links
---

Triage the broker replies waiting in the inbox. Work in this order, because the
order is what stops work being wasted:

1. **Verification links.** Time-critical; some expire in 30 minutes. An
   unconfirmed request does not exist no matter what the form said.
2. **Bounces.** A hard bounce means the route is dead and every future letter to
   it is wasted. Distinguish: `5.1.1` no such user, `5.7.1` policy rejection,
   a null MX, a domain with nameservers but no A and no MX, a Google Group you
   are not a member of. These mean different things and only some mean "nobody
   is there". Find the live route before marking anything `unreachable`.
3. **Confirmations.** Check the *scope*. Does it name one hostname when the
   company runs four? Does it name a record that is not the user's? A
   confirmation is evidence about the broker's action, not about whose record it
   acted on.
4. **Deflections.** `${CLAUDE_PLUGIN_ROOT}/brokers/_DEFLECTIONS.md`.
5. **Closure surveys with no reply.** A satisfaction survey proves the ticket was
   closed, not that anything was done. Do not rate it — reply into the
   acknowledgement thread, which reopens it.

Record every ticket number you are given, even when nothing is wrong. Ticket IDs
across different brands are the strongest cheap evidence of a shared operator.

Update statuses as you go, then write what you learned into the playbooks.
