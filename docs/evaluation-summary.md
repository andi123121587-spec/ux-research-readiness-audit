# Evaluation Summary

The benchmark compared a generic prompt, V1, V2.1.1, and V2.2 across three synthetic cases. Earlier runs showed that V1 and V2.1.1 could over-audit mature projects and over-block conflicting evidence. The V2.2 regression added conflict-layer classification, root-cause deduplication, a counterfactual BLOCKER gate, and separate solution/problem-direction states.

V2.2 results:

| Case | Result |
|---|---|
| Mature research | 3/3 PASS; 0 BLOCKER |
| Evidence missing | 3/3 PASS; required BLOCKER and `NOT_READY` |
| Conflicting evidence | 3/3 PASS; 0 BLOCKER and solution-level pause |

The primary logical set was 9/9. Output size decreased 56.8% relative to the frozen V2.1.1 baseline. Runtime did not meet the reduction target because one run experienced repeated network reconnects and lasted 12,629 seconds. This is a performance/infrastructure warning, not a logical pass fabricated from a failed run.
