---
artifact_type: traceability
artifact_id: CHK-001
status: template
owner: "[MAINTAINER_EMAIL]"
related_ids:
  - GOAL-001
  - SCN-001
  - CAP-001
  - CNT-001
  - CMP-001
assumptions:
  - "[ASSUMPTION] A single matrix is sufficient for small and medium system designs."
open_questions:
  - "[OPEN QUESTION] When to split traceability by subsystem."
---

# 09 - Traceability

## Purpose
- Make design completeness and impact analysis explicit by linking all major artifact types.

## Traceability Matrix
| Goal ID | Scenario ID | Capability ID | Contract ID | Component ID | NFR/Check ID | ADR ID | Notes |
|---|---|---|---|---|---|---|---|
| `GOAL-001` | `SCN-001` | `CAP-001` | `CNT-001` | `CMP-001` | `CHK-001` | `ADR-0001` | `[TBD]` |
| `GOAL-002` | `SCN-002` | `CAP-002` | `CNT-002` | `CMP-002` | `CHK-002` | `ADR-0002` | `[TBD]` |

## Change Impact Notes
- Update this matrix whenever a goal, scenario, capability, contract, component, check, or ADR changes.
- A structural change is not review-ready until traceability is updated.

## Inputs
- All artifacts from `docs/01` through `docs/08`.
- Accepted ADRs from `docs/adr/`.

## Outputs
- A machine-checkable and review-friendly dependency map for the design.

## Assumptions
- Every in-scope goal should be represented by at least one row in the matrix.

## Open Questions
- Whether future versions need separate matrices for operational and compliance coverage.

## Related IDs
- `GOAL-001`
- `SCN-001`
- `CAP-001`
- `CNT-001`
- `CMP-001`
- `CHK-001`
