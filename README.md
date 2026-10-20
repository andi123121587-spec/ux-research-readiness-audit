# UX Research Readiness Audit

Audit whether UX research is sufficient to support prototype exploration without allowing AI to replace designer judgment.

This repository contains the stable V2.2 Codex Agent Skill. It helps a UX designer inspect whether research and analysis support low-cost prototype exploration and appropriately bounded research claims.

## What it does

- Audits evidence, analysis outputs, assumptions, and decisions.
- Checks a nine-dimension minimum analysis package without mechanically creating one Issue per dimension.
- Builds root causes before generating Issues.
- Classifies where evidence conflicts occur.
- Separates prototype exploration, proposed-solution convergence, research-claim readiness, and aggregate readiness.
- Applies a counterfactual threshold before assigning `BLOCKER`.
- Produces a compact, evidence-grounded action plan with designer decision points.

## What it does not do

- It does not replace user research.
- It does not invent personas, interviews, quotes, or validation results.
- It does not turn a feature list into verified user needs.
- It does not choose a single final design for the designer.
- It does not treat a prototype plan as a research result.

## Install and invoke

From this repository's root, copy the Skill directory into a project:

```bash
mkdir -p your-project/.agents/skills
cp -R skill/ux-research-readiness-audit-v2-2 \
  your-project/.agents/skills/
```

Then explicitly invoke it in Codex:

```text
$ux-research-readiness-audit-v2-2
```

Provide a brief, research evidence, analysis notes, decisions, and source notes when available. The Skill works best when each input's provenance and confidence are clear.

## Decision model

| State | Question |
|---|---|
| Prototype exploration | Can the team continue low-cost, reversible learning? |
| Proposed solution | Should the current solution converge, pause, or remain a hypothesis? |
| Research claim | Which claims are supported, bounded, or not ready? |
| Aggregate rating | What is the overall readiness state for the current decision? |

Pausing a proposed solution does not automatically pause the problem direction. A `BLOCKER` requires that a low-cost, reversible, explicitly hypothetical prototype cannot produce useful learning, or that exploration creates unacceptable irreversible risk.

## Evaluation

The public evaluation set contains three synthetic cases: mature research, missing evidence, and conflicting evidence. The V2.2 primary regression set passed 9/9 logical outputs:

| Case | V2.2 |
|---|---|
| Mature research | 3/3 PASS |
| Evidence missing | 3/3 PASS |
| Conflicting evidence | 3/3 PASS |

The result is `V2.2_LOGIC_PASSED_WITH_PERFORMANCE_WARNING`: output size fell 56.8% versus the V2.1.1 baseline, while runtime was distorted by a network reconnect outlier.

Run the local structural validator with the Python environment available on your machine:

```bash
python3 skill/ux-research-readiness-audit-v2-2/scripts/validate_audit_report.py <audit-report.md>
```

## Repository map

- `skill/`: installable V2.2 Skill.
- `examples/`: small fictional input and report example.
- `evals/`: synthetic cases, Gold Standards, and rubric.
- `docs/`: method, decision model, human/AI boundary, evaluation summary, and version history.

## Limitations

The public set contains only three compressed synthetic cases. It demonstrates failure prevention and structure, not universal superiority over a generic prompt. Runtime depends on the model, Codex version, network, and local environment. Future evaluations should include hidden gaps, noisy sources, contradictory files, duplicate participants, and AI-generated false evidence.

## License

MIT. See [LICENSE](LICENSE).
