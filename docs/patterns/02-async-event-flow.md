---
artifact_type: pattern
artifact_id: PAT-002
status: active
owner: "[MAINTAINER_EMAIL]"
related_ids:
  - CNT-003
  - SCN-002
  - CMP-002
assumptions:
  - "[ASSUMPTION] The initiator does not require the final result inline."
open_questions:
  - "[OPEN QUESTION] What delivery guarantees the completed instance requires."
---

# PAT-002: Async Event Flow

## Purpose
- Model workflows where work continues after the initiating interaction finishes.

## When To Use
- Processing is long-running, fan-out, or integration-heavy.
- The system can tolerate eventual completion and asynchronous notifications.

## Design Guidance
- Define trigger, event publication, consumer responsibilities, and compensation paths.
- Document deduplication, ordering assumptions, and reprocessing behavior.
- Make observability explicit because failures are less visible to users.

## Tradeoffs
- Better decoupling and scalability.
- More complex retries, visibility, and consistency reasoning.

## Artifact Updates
- Scenarios: include eventual outcome and timeout paths.
- Contracts: define event semantics and consumer obligations.
- Architecture: define publishers, consumers, and boundaries.
- Operations: define queue depth, lag, and dead-letter handling signals.

## Inputs
- Long-running or decoupled capability requirements.

## Outputs
- A reusable async interaction model and its supporting traceability.

## Assumptions
- Eventual completion is acceptable to primary actors.

## Open Questions
- Whether downstream projects need explicit reconciliation procedures.

## Related IDs
- `PAT-002`
- `CNT-003`
- `SCN-002`
- `CMP-002`
