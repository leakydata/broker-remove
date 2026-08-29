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
R=$(python3 scripts/redact.py 2>&1 | grep 'personal-data occurrence')
V=$(python3 scripts/validate.py 2>&1 | grep 'curated brokers')
echo "$R"
echo "$V"
case "$R" in "0 personal-data"*) ;; *) echo "GATE FAILED: personal data in publishable files" >&2; exit 1;; esac
case "$V" in *"| 0 errors"*) ;; *) echo "GATE FAILED: validate errors" >&2; exit 1;; esac
echo "GATE PASSED"
