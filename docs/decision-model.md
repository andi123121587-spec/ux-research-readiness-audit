# Decision Model

V2.2 keeps four states separate:

| State | Meaning |
|---|---|
| `EXPLORE` / `EXPLORE_WITH_GUARDRAILS` | Low-cost, reversible prototype learning may continue. |
| `PAUSE_PROPOSED_SOLUTION` / `PROCEED_AS_HYPOTHESIS` | The current solution should not converge as if verified. |
| `CLAIM_READY_AFTER_FIXES` / `CLAIM_NOT_READY` | Research claims are bounded by the available evidence. |
| `READY_AFTER_FIXES` / `NOT_READY` | Aggregate decision for the current prototype or implementation path. |

`PAUSE_CORE_PROTOTYPING` is reserved for cases where the core problem, user, or learning goal is too uncertain for a safe, useful low-cost prototype. It must not be used merely because a default solution is unsupported.
