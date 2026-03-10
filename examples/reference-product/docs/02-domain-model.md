---
artifact_type: domain-model
artifact_id: DOM-101
status: accepted
owner: "template-maintainer@example.com"
related_ids:
  - INV-101
  - SCN-101
  - CAP-101
assumptions:
  - "Request lifecycle and approval policy are the core business concepts."
open_questions:
  - "None."
---

# 02 - Domain Model

## Purpose
- Define the core business concepts and invariants that any Flow Approval Hub implementation must preserve.

## Domain Concepts
| Concept ID | Concept | Description | Key Attributes |
|---|---|---|---|
| `DOM-101` | Work Request | A request created by a requester for shared-service work | request type, requester, policy snapshot, current state, timestamps |
| `DOM-102` | Approval Policy | Rules that determine which approvers and thresholds apply | request type, thresholds, approver groups, escalation rules |
| `DOM-103` | Fulfillment Task | A task issued to an external fulfillment system once a request is approved | target system, task reference, issue time, external status |
| `DOM-104` | Audit Entry | An immutable record of a business or operational action | actor, action, reason, correlation identifier, timestamp |

## Relationships
| Source | Relationship | Target | Notes |
|---|---|---|---|
| `DOM-101` | is evaluated by | `DOM-102` | The policy snapshot is captured when routing begins |
| `DOM-101` | may issue | `DOM-103` | Only after approval is complete |
| `DOM-101` | emits | `DOM-104` | Every state transition and decision creates an audit entry |

## Invariants
| Invariant ID | Rule | Impacted Concepts |
|---|---|---|
| `INV-101` | A work request must move through lifecycle states monotonically and cannot return to a prior approved state without a new audit entry | `DOM-101`, `DOM-104` |
| `INV-102` | A fulfillment task cannot exist until the linked request is fully approved | `DOM-101`, `DOM-103` |
| `INV-103` | Every approval or rejection decision must reference the deciding actor and reason | `DOM-101`, `DOM-104` |

## Lifecycle Or State Notes
- `DOM-101`: `draft -> submitted -> awaiting_approval -> approved -> fulfilled` with side branches `rejected`, `cancelled`, and `fulfillment_failed`.
- `DOM-103`: `issued -> acknowledged -> completed` with side branch `failed`.

## Glossary
- `Policy snapshot`: the immutable copy of approval rules attached to a request when routing starts.
- `Reconciliation`: operator-driven comparison of local request state against downstream fulfillment state.

## Inputs
- Product goals and constraints from `docs/01-product-scope.md`.
- The need for auditability and fulfillment tracking.

## Outputs
- The shared domain vocabulary and invariants used by scenarios, capabilities, contracts, and architecture.

## Assumptions
- A request can be modeled as one aggregate even when multiple approvers participate.

## Open Questions
- None.

## Related IDs
- `DOM-101`
- `INV-101`
- `SCN-101`
- `CAP-101`
