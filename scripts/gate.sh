#!/usr/bin/env bash
# Pre-commit gate. EXITS NON-ZERO on failure -- that is the entire point.
#
# Written 2026-08-29 after a name reached a public commit. The check had been
# inlined at every call site as:
#
#     case "$R $V" in "0 personal-data"*"| 0 errors"*) echo "GATE PASSED";;
#                     *) echo "GATE FAILED";; esac
#     git add -A && git commit ... && git push
#
# which prints a verdict and then commits anyway. It looked like a guard for
# weeks because it had never yet reported FAILED at a moment that mattered. A
# check whose failure branch is `echo` is not a check.
#
# Usage:  scripts/gate.sh && git commit ... && git push
set -uo pipefail
cd "$(dirname "$0")/.."

# PUBLISH THE SHARED LEDGER FIRST.
#
# Added 2026-08-31 after discovering that 139 brokers -- two full days of work by
# both agents -- had never been shared. The ledger is the only way the local and
# cloud sessions can see each other, and I had been reading the merge warning
# "the other agent is not publishing a ledger yet" while not publishing mine.
#
# Doing it here rather than by remembering is the 179 rule applied to
# coordination: a step that depends on someone remembering it is not a step. The
# publish is deterministic and strips notes, quotes and identifiers, and redact.py
# runs immediately after on the result -- so if it ever emitted personal data the
# very next line would block the commit.
python3 scripts/sync_status.py >/dev/null 2>&1 || {
    echo "GATE FAILED: could not publish the shared ledger" >&2; exit 1; }

R=$(python3 scripts/redact.py 2>&1 | grep 'personal-data occurrence')
V=$(python3 scripts/validate.py 2>&1 | grep 'curated brokers')
echo "$R"
echo "$V"
case "$R" in "0 personal-data"*) ;; *) echo "GATE FAILED: personal data in publishable files" >&2; exit 1;; esac
case "$V" in *"| 0 errors"*) ;; *) echo "GATE FAILED: validate errors" >&2; exit 1;; esac
echo "GATE PASSED"
