# Public Evaluation Set

This directory contains three synthetic, compressed cases and their Gold Standards. It is intended to make the core regression behavior inspectable without publishing raw Codex sessions, SQLite state, or private research material.

Each case contains five input files. The expected-results directory contains the target findings and state expectations. The rubric defines evidence recall, boundary accuracy, gap precision, decision control, stability, and cost.

The V2.2 regression expectations are:

- mature research: zero BLOCKERs and `READY_AFTER_FIXES`;
- missing evidence: at least one BLOCKER and `NOT_READY`;
- conflicting evidence: zero BLOCKERs, `EXPLORE_WITH_GUARDRAILS`, and a pause of the proposed solution rather than the problem direction.
