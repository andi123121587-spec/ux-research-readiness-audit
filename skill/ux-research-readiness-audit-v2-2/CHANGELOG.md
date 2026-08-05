# Changelog

## 2.2.0

- Added conflict-level classification before severity assignment.
- Added root-cause registry and affected-dimension mapping to prevent duplicate Issues.
- Added BLOCKER counterfactual gate.
- Added proposed-solution convergence status, including `PAUSE_PROPOSED_SOLUTION`.
- Prevented solution-level conflicts from pausing the entire problem direction.
- Added maturity/stage calibration for Discovery, Alpha and later-stage projects.
- Added compact default output and full audit mode.
- Added regression criteria for mature, evidence-missing and conflicting-evidence cases.
- Updated examples, evaluation prompts, report templates, metadata and validator.

## 2.1.1

- Made the Issue registry the single source of truth for all severity counts.
- Added cross-section consistency checks.

## 2.1.0

- Split `MAJOR_GAP` and `BLOCKING_GAP`.
- Added separate validation plan, execution and evidence statuses.

## 2.0.0

- Added two-axis readiness decisions and designer-decision boundaries.
