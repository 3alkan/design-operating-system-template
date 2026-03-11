---
artifact_type: pattern
artifact_id: PAT-003
status: active
owner: "[PROJECT_CONTACT_EMAIL]"
related_ids:
  - CMP-003
  - CNT-001
  - RISK-001
assumptions:
  - "[ASSUMPTION] External systems will have different availability and change cadence than the designed system."
open_questions:
  - "[OPEN QUESTION] Which integration failure modes are acceptable to surface directly."
---

# PAT-003: External Integration Boundary

## Purpose
- Isolate dependencies on third-party or legacy systems behind explicit contracts and risk controls.

## When To Use
- The product depends on a vendor API, legacy database, partner feed, or internal shared service.

## Design Guidance
- Introduce a boundary component with clearly owned contracts.
- Normalize external errors into internal error semantics.
- Document fallback, caching, or manual recovery expectations.

## Tradeoffs
- Clearer boundaries and easier replacement.
- Additional translation logic and operational complexity.

## Artifact Updates
- Architecture: add boundary component and dependency notes.
- Contracts: define inbound and outbound abstractions.
- Risks: record dependency-specific availability and versioning risks.
- Operations: define integration health checks and escalation steps.

## Inputs
- Architecture and dependency constraints.

## Outputs
- A safer, more replaceable external system boundary.

## Assumptions
- External dependencies should not leak their raw semantics through the design unchecked.

## Open Questions
- Whether downstream projects need explicit sandbox or certification environments for integrations.

## Related IDs
- `PAT-003`
- `CMP-003`
- `CNT-001`
- `RISK-001`
