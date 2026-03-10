---
artifact_type: pattern
artifact_id: PAT-001
status: active
owner: "[MAINTAINER_EMAIL]"
related_ids:
  - CNT-001
  - SCN-001
  - CMP-001
assumptions:
  - "[ASSUMPTION] The caller needs an immediate outcome or confirmation."
open_questions:
  - "[OPEN QUESTION] Which latency budget should a completed instance declare."
---

# PAT-001: Sync Request-Response

## Purpose
- Model work where the caller needs an immediate answer or acceptance result.

## When To Use
- A user-facing action needs synchronous confirmation.
- The response must include computed data or validation outcome.

## Design Guidance
- Define one command or query contract per clear intent.
- Document timeout, validation failure, and partial failure semantics.
- Keep responsibilities separated between request orchestration and domain decision logic.

## Tradeoffs
- Simpler caller behavior and user feedback.
- Tighter runtime coupling and stricter latency expectations.

## Artifact Updates
- Scenarios: add user-visible success and failure paths.
- Contracts: define request, response, and error semantics.
- Quality: define latency and correctness checks.
- Operations: define timeout and error monitoring.

## Inputs
- Scenario and capability requirements.

## Outputs
- A synchronous interaction pattern that can be traced through contracts and checks.

## Assumptions
- Immediate response matters more than eventual decoupling.

## Open Questions
- Whether the action should degrade gracefully when dependencies are unavailable.

## Related IDs
- `PAT-001`
- `CNT-001`
- `SCN-001`
- `CMP-001`
