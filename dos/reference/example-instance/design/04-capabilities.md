---
artifact_type: capabilities
artifact_id: CAP-101
status: accepted
owner: "reference-contact@example.invalid"
related_ids:
  - SCN-101
  - CNT-101
  - CMP-101
  - CHK-101
assumptions:
  - "Capabilities map cleanly to workflow boundaries."
open_questions:
  - "None."
---

# 04 - Capabilities

## Purpose
- Define the system capabilities that satisfy the product goals for Flow Approval Hub.

## Capability Catalog
| Capability ID | Capability | Value | Linked Goals | Priority |
|---|---|---|---|---|
| `CAP-101` | Capture and validate requests | Ensures all requests enter the workflow with complete data and policy context | `GOAL-101` | Must |
| `CAP-102` | Route and record approvals | Makes approval decisions explicit, durable, and policy-driven | `GOAL-102` | Must |
| `CAP-103` | Issue and reconcile fulfillment tasks | Connects approved work to downstream systems and keeps local status accurate | `GOAL-103` | Must |
| `CAP-104` | Notify actors and preserve audit history | Reduces manual follow-up and provides trustworthy history | `GOAL-102`, `GOAL-104` | Should |

## Acceptance Criteria
### Capability: `CAP-101` Capture and validate requests
- Acceptance criteria:
  - [x] A requester can submit a request only when required fields and request type rules are satisfied.
  - [x] The system snapshots the applicable approval policy when the request enters the workflow.
- Done means:
  - [x] Behavior satisfies `SCN-101`.
  - [x] Related contracts and components are defined.
  - [x] Related checks in `design/07-quality.md` are identified.

### Capability: `CAP-102` Route and record approvals
- Acceptance criteria:
  - [x] Authorized approvers can approve or reject with a required reason.
  - [x] Every decision creates an immutable audit entry and advances workflow state deterministically.
- Done means:
  - [x] Behavior satisfies `SCN-102`.
  - [x] Related contracts and components are defined.
  - [x] Related checks in `design/07-quality.md` are identified.

### Capability: `CAP-103` Issue and reconcile fulfillment tasks
- Acceptance criteria:
  - [x] An approved request emits a fulfillment task exactly once in effect.
  - [x] Operators can reconcile local and external fulfillment state when updates lag or fail.
- Done means:
  - [x] Behavior satisfies `SCN-103`.
  - [x] Related contracts and components are defined.
  - [x] Related checks in `design/07-quality.md` are identified.

### Capability: `CAP-104` Notify actors and preserve audit history
- Acceptance criteria:
  - [x] Requesters, approvers, and operators receive event-driven notifications for meaningful status changes.
  - [x] Operators can view a durable timeline of request and fulfillment actions.
- Done means:
  - [x] Supporting contracts, signals, and operational checks are defined.
  - [x] The capability is traceable to goals and runtime paths.
  - [x] Audit and notification behavior is covered in architecture and operations artifacts.

## Release Or Dependency Notes
- Dependencies: `CAP-103` depends on the external fulfillment boundary; `CAP-104` depends on event publication from the workflow engine.
- Sequencing notes: `CAP-101` and `CAP-102` must exist before `CAP-103`; `CAP-104` can be implemented incrementally but must preserve audit history from day one.

## Inputs
- Product goals from `design/01-product-scope.md`.
- Runtime journeys from `design/03-scenarios.md`.

## Outputs
- The capability set that drives contracts, components, traceability, and verification.

## Assumptions
- Approval routing and fulfillment integration are the dominant system boundaries.

## Open Questions
- None.

## Related IDs
- `GOAL-101`
- `SCN-101`
- `CAP-101`
- `CNT-101`
- `CMP-101`
- `CHK-101`
