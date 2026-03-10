---
artifact_type: scenarios
artifact_id: SCN-101
status: accepted
owner: "template-maintainer@example.com"
related_ids:
  - ACT-101
  - CAP-101
  - CNT-101
assumptions:
  - "The first release centers on intake, approval, and fulfillment visibility."
open_questions:
  - "None."
---

# 03 - Scenarios

## Purpose
- Describe the primary user and system journeys for Flow Approval Hub.

## Scenario Catalog
| Scenario ID | Scenario | Primary Actor | Linked Capability |
|---|---|---|---|
| `SCN-101` | Submit a new work request | `ACT-101` | `CAP-101` |
| `SCN-102` | Approver reviews and decides a request | `ACT-102` | `CAP-102` |
| `SCN-103` | Operator reconciles a delayed fulfillment update | `ACT-103` | `CAP-103` |

## Scenario Template
### Scenario: `SCN-101` Submit a new work request
- Goal: `Capture a valid request and route it into the approval workflow.`
- Preconditions: `The requester is authenticated and has access to the chosen request type.`
- Main flow:
  1. `ACT-101` submits request details through the experience surface.
  2. `CMP-101` validates the payload and forwards `CNT-101`.
  3. `CMP-102` creates the request, snapshots the applicable policy, records an audit entry, and places the request in `awaiting_approval`.
  4. `CMP-104` emits notifications to the first approver set.
- Alternate flow: `If no approval is required for the request type, the workflow marks the request approved immediately and issues a fulfillment task.`
- Failure behavior: `Validation failure returns field-specific errors; policy lookup failure leaves the request uncreated and emits an operational signal.`
- Success outcome: `The requester receives a request identifier and initial status.`

### Scenario: `SCN-102` Approver reviews and decides a request
- Goal: `Record an approval or rejection decision with durable audit history.`
- Preconditions: `The request is awaiting approval and the actor is authorized for the current approval step.`
- Main flow:
  1. `ACT-102` loads the request view through `CNT-103`.
  2. `ACT-102` submits `CNT-102` with decision and reason.
  3. `CMP-102` validates authorization, updates workflow state, and records an audit entry.
  4. `CMP-102` either advances to the next approver or marks the request approved and publishes `CNT-105`.
- Alternate flow: `A rejection ends the workflow and notifies the requester.`
- Failure behavior: `A stale or unauthorized decision is rejected and logged for operator review.`
- Success outcome: `The request state reflects the decision and downstream actions are triggered if approval is complete.`

### Scenario: `SCN-103` Operator reconciles a delayed fulfillment update
- Goal: `Resolve divergence between local request state and downstream fulfillment state.`
- Preconditions: `A fulfillment task exists and the external system has not reported status within the expected window.`
- Main flow:
  1. `ACT-103` reviews the delayed task queue and opens the affected request.
  2. `CMP-105` queries the downstream system using the task reference.
  3. `CMP-102` updates local request and task state if the external status changed.
  4. `CMP-104` records the reconciliation event and notifies affected actors if state changes.
- Alternate flow: `If the external system has no record, the task is marked for manual investigation.`
- Failure behavior: Integration failure keeps the request in `approved` or `fulfillment_failed` and raises an operator alert.
- Success outcome: `The local request state matches the best known fulfillment truth.`

## Runtime Notes
- `SCN-101` and `SCN-102` are primarily synchronous from the actor perspective, with asynchronous notifications and fulfillment triggers.
- `SCN-103` is operator-driven and may call the integration boundary repeatedly until state converges.

## Inputs
- Actors and goals from `docs/01-product-scope.md`.
- Domain concepts and invariants from `docs/02-domain-model.md`.

## Outputs
- The core runtime journeys used to define capabilities, contracts, architecture views, and verification checks.

## Assumptions
- Three scenarios are sufficient to demonstrate the reference design.

## Open Questions
- None.

## Related IDs
- `ACT-101`
- `SCN-101`
- `CAP-101`
- `CNT-101`
