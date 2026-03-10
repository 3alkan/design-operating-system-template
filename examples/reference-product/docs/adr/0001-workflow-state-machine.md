---
artifact_type: adr
artifact_id: ADR-0001
status: accepted
owner: "template-maintainer@example.com"
related_ids:
  - CMP-102
  - SCN-101
  - SCN-102
  - INV-101
assumptions:
  - "Approval routing must remain deterministic as request volume grows."
open_questions:
  - "None."
---

# ADR-0001: Use A Deterministic Workflow State Machine

## Purpose
- Record the decision to model request lifecycle transitions explicitly.

## Status
- `accepted`

## Decision Summary
- `The workflow engine will treat request progression as an explicit state machine with guarded transitions and audit emission on every state change.`

## Context
- Problem: `Approval routing, rejection, cancellation, and fulfillment handoff must remain predictable and auditable across implementations.`
- Drivers: `Deterministic behavior, operator reasoning, auditability, and easier invariant enforcement.`
- Impacted artifact IDs: `CMP-102`, `DOM-101`, `INV-101`, `SCN-101`, `SCN-102`, `CNT-102`, `CNT-104`, `CNT-105`

## Decision
- `Represent request lifecycle transitions as named states with explicit allowed transitions and side effects.`
- `Route every approval, rejection, cancellation, reconciliation, and fulfillment update through the workflow engine so invariants are enforced centrally.`

## Alternatives Considered
1. `Implicit status updates spread across multiple components`
2. `Ad hoc workflow scripts owned by request type`

## Rejected Options
- `Implicit status updates spread across multiple components` because `it makes invariants and operator debugging harder to preserve consistently.`
- `Ad hoc workflow scripts owned by request type` because `it would fragment decision logic and increase drift between request types.`

## Consequences
- Positive: `State transitions, retries, and audit generation become easier to reason about and test.`
- Negative: `Workflow changes require deliberate updates and compatibility review.`
- Neutral or unknown: `Some implementations may still deploy the workflow engine and ledger together physically.`

## Follow-Ups
- `Ensure traceability and quality checks cover invalid transition rejection and replay behavior.`

## Inputs
- Product requirements for approval routing and auditability.

## Outputs
- A fixed lifecycle modeling approach for the reference product.

## Assumptions
- Centralized transition control is worth the added design discipline.

## Open Questions
- None.

## Related IDs
- `CMP-102`
- `INV-101`
