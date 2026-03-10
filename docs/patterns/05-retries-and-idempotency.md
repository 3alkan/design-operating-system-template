---
artifact_type: pattern
artifact_id: PAT-005
status: active
owner: "[MAINTAINER_EMAIL]"
related_ids:
  - CNT-001
  - CNT-003
  - NFR-001
assumptions:
  - "[ASSUMPTION] Duplicate delivery or transient failure is possible in most real systems."
open_questions:
  - "[OPEN QUESTION] Which actions must be exactly-once in effect versus safely repeatable."
---

# PAT-005: Retries And Idempotency

## Purpose
- Prevent hidden ambiguity around duplicate execution, retriable failure, and consistency under replay.

## When To Use
- A contract may be retried by callers, infrastructure, or operators.
- A workflow crosses unreliable boundaries.

## Design Guidance
- Identify which commands or events must be idempotent.
- Define retryable vs non-retryable failures.
- State reconciliation expectations when repeated attempts disagree with current state.

## Tradeoffs
- Higher resilience under transient failure.
- More state tracking or deduplication complexity.

## Artifact Updates
- Contracts: state idempotency keys or equivalent semantics.
- Quality: define failure and replay checks.
- Operations: define replay handling and recovery guidance.
- ADRs: record any unusual consistency tradeoffs.

## Inputs
- Contract and failure-handling design.

## Outputs
- Explicit replay and retry semantics.

## Assumptions
- Reliability expectations should be designed, not deferred.

## Open Questions
- Whether downstream teams need separate strategies for user-triggered retries and background retries.

## Related IDs
- `PAT-005`
- `CNT-001`
- `CNT-003`
- `NFR-001`
