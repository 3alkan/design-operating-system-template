---
artifact_type: adr
artifact_id: ADR-0002
status: accepted
owner: "template-maintainer@example.com"
related_ids:
  - CMP-103
  - CNT-104
  - CNT-105
  - NFR-102
assumptions:
  - "Audit and compatibility mistakes are more expensive than additional storage or process overhead."
open_questions:
  - "None."
---

# ADR-0002: Use Append-Only Audit Entries And Additive Contract Evolution

## Purpose
- Record the policy for audit durability and contract change management.

## Status
- `accepted`

## Decision Summary
- `Audit history is append-only and contract evolution is additive by default, with breaking changes requiring explicit versioning review.`

## Context
- Problem: `The product must preserve trustworthy history and evolve contracts without surprising requesters, approvers, or operators.`
- Drivers: `Compliance retention, operator trust, replay safety, and long-lived integrations.`
- Impacted artifact IDs: `CMP-103`, `CMP-104`, `CNT-103`, `CNT-104`, `CNT-105`, `NFR-102`, `NFR-103`, `OPS-101`

## Decision
- `Persist audit entries immutably and project operator timelines from those entries rather than rewriting history.`
- `Treat contract additions as compatible by default; any semantic change or field removal requires an explicit compatibility review and likely a versioned path.`

## Alternatives Considered
1. `Mutable audit timeline records`
2. `Unversioned contract changes with consumer coordination`

## Rejected Options
- `Mutable audit timeline records` because `rewritten history weakens audit trust and complicates incident reconstruction.`
- `Unversioned contract changes with consumer coordination` because `it creates hidden coupling and fragile integrations.`

## Consequences
- Positive: `Audit trust is preserved and integrations can evolve more safely.`
- Negative: `Storage use grows over time and design changes require stronger review discipline.`
- Neutral or unknown: `Some implementations may project audit history into read models for user experience performance.`

## Follow-Ups
- `Ensure the request ledger and notification projection can rebuild from append-only history if needed.`

## Inputs
- Compliance requirements, operational needs, and integration change expectations.

## Outputs
- A fixed audit durability and compatibility policy for the reference product.

## Assumptions
- The system benefits from durable history and conservative interface evolution.

## Open Questions
- None.

## Related IDs
- `CMP-103`
- `NFR-102`
