---
artifact_type: pattern-index
artifact_id: PAT-000
status: active
owner: "[PROJECT_CONTACT_EMAIL]"
related_ids:
  - PAT-001
  - PAT-002
assumptions:
  - "[ASSUMPTION] A small pattern library reduces repeated design ambiguity."
open_questions:
  - "[OPEN QUESTION] Which additional patterns recur most often in downstream projects."
---

# Patterns

## Purpose
- Provide reusable design guidance for recurring system concerns without forcing a specific stack.

## Pattern Set
| Pattern ID | Pattern | Use When |
|---|---|---|
| `PAT-001` | Sync request-response | Immediate acknowledgment or data retrieval is required |
| `PAT-002` | Async event flow | Work can complete after the initiating interaction returns |
| `PAT-003` | External integration boundary | The system depends on a third-party or legacy system |
| `PAT-004` | Identity and authorization | Access decisions shape capabilities or contracts |
| `PAT-005` | Retries and idempotency | Failures or replays can occur |
| `PAT-006` | Observability baseline | Core behaviors require diagnosable signals |
| `PAT-007` | Versioning and evolution | Contracts or behaviors will change over time |
| `PAT-008` | Tenancy and isolation | Multiple tenants or strict data boundaries matter |

## Inputs
- Product, scenario, capability, and architecture artifacts.

## Outputs
- Reusable guidance that can be referenced from contracts, architecture, quality, and operations.

## Assumptions
- Patterns should stay concise and map back to artifact updates.

## Open Questions
- Whether future versions need anti-pattern examples.

## Related IDs
- `PAT-001`
- `PAT-002`
