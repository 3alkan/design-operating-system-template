---
artifact_type: traceability
artifact_id: CHK-101
status: accepted
owner: "reference-contact@example.invalid"
related_ids:
  - GOAL-101
  - SCN-101
  - CAP-101
  - CNT-101
  - CMP-101
assumptions:
  - "A single matrix is enough for this reference product."
open_questions:
  - "None."
---

# 09 - Traceability

## Purpose
- Provide the dependency map that links product intent to runtime behavior, structure, and verification.

## Traceability Matrix
| Goal ID | Scenario ID | Capability ID | Contract ID | Component ID | NFR/Check ID | ADR ID | Notes |
|---|---|---|---|---|---|---|---|
| `GOAL-101` | `SCN-101` | `CAP-101` | `CNT-101` | `CMP-101`, `CMP-102`, `CMP-103` | `CHK-101`, `NFR-101` | `ADR-0001` | Request submission validates input and snapshots policy |
| `GOAL-102` | `SCN-102` | `CAP-102` | `CNT-102`, `CNT-104` | `CMP-101`, `CMP-102`, `CMP-103`, `CMP-104` | `CHK-101`, `CHK-102`, `NFR-102` | `ADR-0001`, `ADR-0002` | Approval decisions are deterministic and auditable |
| `GOAL-103` | `SCN-103` | `CAP-103` | `CNT-105`, `CNT-104` | `CMP-102`, `CMP-103`, `CMP-105` | `CHK-102`, `CHK-103`, `NFR-103` | `ADR-0002` | Fulfillment issuance is idempotent and reconciliation handles lag |
| `GOAL-104` | `SCN-102`, `SCN-103` | `CAP-104` | `CNT-103`, `CNT-104` | `CMP-103`, `CMP-104` | `CHK-103`, `NFR-102` | `ADR-0002` | Notifications and timeline views reduce manual follow-up |

## Change Impact Notes
- Any change to workflow state rules must update `SCN-101` through `SCN-103`, `CNT-102`, `CNT-104`, `CNT-105`, `CMP-102`, and `ADR-0001`.
- Any change to audit durability or notification projection must update `CAP-104`, `CMP-103`, `CMP-104`, `NFR-102`, and `ADR-0002`.

## Inputs
- All product artifacts from `design/01` through `design/08`.
- Accepted ADRs from `design/adr/`.

## Outputs
- A complete traceability map for the reference implementation.

## Assumptions
- Every in-scope goal should remain covered by at least one scenario-capability-check path.

## Open Questions
- None.

## Related IDs
- `GOAL-101`
- `SCN-101`
- `CAP-101`
- `CNT-101`
- `CMP-101`
- `CHK-101`
