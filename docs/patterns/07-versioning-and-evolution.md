---
artifact_type: pattern
artifact_id: PAT-007
status: active
owner: "[MAINTAINER_EMAIL]"
related_ids:
  - CNT-001
  - ADR-0001
  - NFR-001
assumptions:
  - "[ASSUMPTION] Contracts and workflows will evolve after the first release."
open_questions:
  - "[OPEN QUESTION] Which changes qualify as backward-compatible for the downstream product."
---

# PAT-007: Versioning And Evolution

## Purpose
- Make compatibility and change-management expectations explicit before implementation.

## When To Use
- Contracts, workflows, or operational guarantees may change over time.

## Design Guidance
- State the unit of compatibility: contract, capability, workflow, or artifact.
- Define how breaking changes are introduced and communicated.
- Use ADRs when a versioning policy becomes fixed.

## Tradeoffs
- Clearer evolution path and safer collaboration.
- More process overhead and compatibility discipline.

## Artifact Updates
- Contracts: state versioning rules and compatibility expectations.
- ADRs: record fixed policy choices.
- Operations: define migration or rollout notes.

## Inputs
- Contract change expectations and release posture.

## Outputs
- A repeatable change policy for design and implementation.

## Assumptions
- Compatibility policy should be decided before interfaces proliferate.

## Open Questions
- Whether different contract classes need different versioning rules.

## Related IDs
- `PAT-007`
- `CNT-001`
- `ADR-0001`
- `NFR-001`
