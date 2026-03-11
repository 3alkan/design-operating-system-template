---
artifact_type: scenarios
artifact_id: SCN-001
status: draft
owner: "[PROJECT_CONTACT_EMAIL]"
related_ids:
  - ACT-001
  - CAP-001
  - CNT-001
assumptions:
  - "[ASSUMPTION] Each core capability can be demonstrated through one or more scenarios."
open_questions:
  - "[OPEN QUESTION] Which failure paths need the strongest operational visibility."
---

# 03 - Scenarios

## Purpose
- Describe the highest-value user and system journeys, including alternate and failure flows.

## Scenario Catalog
| Scenario ID | Scenario | Primary Actor | Linked Capability |
|---|---|---|---|
| `SCN-001` | `[TBD]` | `ACT-001` | `CAP-001` |
| `SCN-002` | `[TBD]` | `ACT-002` | `CAP-002` |
| `SCN-003` | `[TBD]` | `ACT-001` | `CAP-003` |

## Scenario Structure
### Scenario: `SCN-001` `[TBD]`
- Goal: `[TBD]`
- Preconditions: `[TBD]`
- Main flow:
  1. `[TBD]`
  2. `[TBD]`
  3. `[TBD]`
- Alternate flow: `[TBD]`
- Failure behavior: `[TBD]`
- Success outcome: `[TBD]`

## Runtime Notes
- Indicate which contracts or components participate in each scenario.
- Note user-visible latency or consistency expectations when relevant.

## Inputs
- Actors and goals from `design/01-product-scope.md`.
- Concepts and invariants from `design/02-domain-model.md`.

## Outputs
- Concrete runtime journeys used to derive capabilities, contracts, and tests.
- A scenario list for traceability and architecture runtime views.

## Assumptions
- A completed instance should capture at least three core scenarios.

## Open Questions
- Which scenarios require dedicated state diagrams or sequence diagrams.

## Related IDs
- `ACT-001`
- `SCN-001`
- `CAP-001`
- `CNT-001`
