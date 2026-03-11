---
artifact_type: contracts
artifact_id: CNT-101
status: accepted
owner: "reference-contact@example.invalid"
related_ids:
  - CAP-101
  - CMP-101
  - NFR-101
assumptions:
  - "Commands, queries, and events are sufficient to express the runtime interactions."
open_questions:
  - "None."
---

# 05 - Contracts

## Purpose
- Specify the abstract interfaces used by Flow Approval Hub components and actors.

## Contract Catalog
| Contract ID | Type | Intent | Producer | Consumer |
|---|---|---|---|---|
| `CNT-101` | Command | Submit a new work request | `CMP-101` | `CMP-102` |
| `CNT-102` | Command | Review a pending work request | `CMP-101` | `CMP-102` |
| `CNT-103` | Query | Fetch a request view with audit summary | `CMP-101` | `CMP-103` |
| `CNT-104` | Event | Announce request state changes | `CMP-102` | `CMP-104`, `CMP-105` |
| `CNT-105` | Event | Issue a fulfillment task for an approved request | `CMP-102` | `CMP-105` |

## Contract Seed
### Contract: `CNT-101` Submit a new work request
- Intent: `Create a request, validate required data, attach the applicable policy snapshot, and begin routing.`
- Trigger: `Requester submits the intake form.`
- Inputs: `requester identity, request type, structured request details, optional supporting notes`
- Outputs: `request identifier, accepted state, current approval step or immediate approval result`
- Error semantics: `validation errors are returned synchronously; policy resolution failure returns a retry-safe service error`
- Guarantees: `a successful submission creates exactly one request aggregate and one audit entry`
- Versioning notes: `new optional request attributes may be added without breaking existing callers; removal or semantic change requires a versioned contract evolution plan`

### Contract: `CNT-102` Review a pending work request
- Intent: `Accept an approver decision and advance or terminate the workflow.`
- Trigger: `Approver chooses approve or reject with a reason.`
- Inputs: `request identifier, approver identity, decision, reason`
- Outputs: `updated request state, next approval step if any, notification trigger summary`
- Error semantics: `stale or unauthorized decisions return a business error and generate an audit-visible warning`
- Guarantees: `the same decision request is idempotent by request identifier and decision token`
- Versioning notes: `decision vocabulary is stable; additional metadata may be added compatibly`

### Contract: `CNT-103` Fetch a request view with audit summary
- Intent: `Return the current request, policy snapshot, task summary, and recent audit entries.`
- Trigger: `Requester, approver, or operator opens a request detail view.`
- Inputs: `request identifier, actor identity`
- Outputs: `request state, approval trail, fulfillment summary, actor-appropriate actions`
- Error semantics: `unauthorized access returns access denied; missing request returns not found`
- Guarantees: `the view reflects the latest committed local state`
- Versioning notes: `additional view fields are backward-compatible`

### Contract: `CNT-104` Announce request state changes
- Intent: `Broadcast meaningful state transitions for notifications and integration reactions.`
- Trigger: `Workflow state changes or reconciliation updates request status.`
- Inputs: `request identifier, previous state, new state, correlation identifier, actor summary`
- Outputs: `downstream notification or integration work`
- Error semantics: `delivery failure triggers retry and operator alerting without rolling back committed request state`
- Guarantees: `state transition events are emitted exactly once in effect per transition`
- Versioning notes: `consumers must ignore unknown attributes`

### Contract: `CNT-105` Issue a fulfillment task for an approved request
- Intent: `Create downstream execution work once approval is complete.`
- Trigger: `Workflow engine marks a request approved.`
- Inputs: `request identifier, fulfillment payload, correlation identifier`
- Outputs: `task issue attempt and later task status updates`
- Error semantics: `temporary downstream failures trigger retriable processing; repeated issuance is deduplicated`
- Guarantees: `only approved requests can produce the event and one approved request yields one effective fulfillment task`
- Versioning notes: `payload mapping changes require compatibility review because downstream systems vary`

## Cross-Cutting Rules
- Authentication and authorization expectations: `All command and query contracts carry actor identity and role context sufficient for capability-level authorization decisions.`
- Idempotency and retry behavior: `Submit and review commands are idempotent by caller-provided or system-issued correlation tokens; events may be retried and consumers must deduplicate by correlation identifier.`
- Audit or observability requirements: `Every command outcome and every consumed status-changing event must produce audit and operational signals.`

## Inputs
- Capabilities from `docs/04-capabilities.md`.
- Quality and operational expectations from `docs/07-quality.md` and `docs/08-operations.md`.

## Outputs
- Abstract interfaces that implementations can realize through any suitable transport or persistence stack.

## Assumptions
- Contract boundaries map to business intent, not UI screens or storage tables.

## Open Questions
- None.

## Related IDs
- `CAP-101`
- `CNT-101`
- `CMP-101`
- `NFR-101`
