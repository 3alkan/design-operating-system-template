---
artifact_type: capabilities
artifact_id: CAP-001
status: template
owner: "[PROJECT_CONTACT_EMAIL]"
related_ids:
  - SCN-001
  - CNT-001
  - CMP-001
  - CHK-001
assumptions:
  - "[ASSUMPTION] Capabilities can be expressed independently from UI, API, or deployment choices."
open_questions:
  - "[OPEN QUESTION] Which capability boundaries map to product tiers or release phases."
---

# 04 - Capabilities

## Purpose
- Define the system capabilities that satisfy goals and scenarios.

## Capability Catalog
| Capability ID | Capability | Value | Linked Goals | Priority |
|---|---|---|---|---|
| `CAP-001` | `[TBD]` | `[TBD]` | `GOAL-001` | Must |
| `CAP-002` | `[TBD]` | `[TBD]` | `GOAL-002` | Should |

## Acceptance Criteria
### Capability: `CAP-001` `[TBD]`
- Acceptance criteria:
  - [ ] `[TBD]`
  - [ ] `[TBD]`
- Done means:
  - [ ] Behavior satisfies linked scenarios.
  - [ ] Related contracts and components are defined.
  - [ ] Related checks in `docs/07-quality.md` are identified.

## Release Or Dependency Notes
- Dependencies: `[TBD]`
- Sequencing notes: `[TBD]`

## Inputs
- Goals from `docs/01-product-scope.md`.
- Scenarios from `docs/03-scenarios.md`.

## Outputs
- A capability inventory that can be mapped to contracts, components, and review or verification checks.

## Assumptions
- Capabilities are stable enough to serve as a primary traceability layer.

## Open Questions
- Which capabilities need explicit backward-compatibility guarantees.

## Related IDs
- `GOAL-001`
- `SCN-001`
- `CAP-001`
- `CNT-001`
- `CMP-001`
- `CHK-001`
