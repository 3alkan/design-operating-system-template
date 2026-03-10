---
artifact_type: pattern
artifact_id: PAT-006
status: active
owner: "[MAINTAINER_EMAIL]"
related_ids:
  - OPS-001
  - NFR-001
  - CHK-001
assumptions:
  - "[ASSUMPTION] Core capabilities need diagnosable signals from the first release."
open_questions:
  - "[OPEN QUESTION] Which signals are mandatory across all downstream products."
---

# PAT-006: Observability Baseline

## Purpose
- Ensure the design specifies the minimum signals needed to operate and debug the system.

## When To Use
- Always, for any capability that matters to users or operators.

## Design Guidance
- Define success, error, and saturation signals for core scenarios.
- Tie each signal to a question an operator may need to answer.
- Keep signal names abstract so they can map to logs, metrics, traces, or events later.

## Tradeoffs
- Better supportability and faster incident diagnosis.
- More design effort and implementation obligations.

## Artifact Updates
- Quality: define checks and measurable expectations.
- Operations: list signals, alerts, and escalation paths.
- Traceability: map checks to capabilities and NFRs.

## Inputs
- Capabilities, scenarios, and operations needs.

## Outputs
- A minimal but explicit observability contract.

## Assumptions
- Unobservable behavior is not implementation-ready.

## Open Questions
- Whether downstream projects should classify signals by business impact.

## Related IDs
- `PAT-006`
- `OPS-001`
- `NFR-001`
- `CHK-001`
