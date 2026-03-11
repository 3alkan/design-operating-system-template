---
artifact_type: architecture
artifact_id: CMP-101
status: accepted
owner: "reference-contact@example.invalid"
related_ids:
  - CNT-101
  - SCN-101
  - NFR-101
  - ADR-0001
assumptions:
  - "The product can be implemented as a set of clear responsibilities even if it is deployed as a single unit."
open_questions:
  - "None."
---

# 06 - Architecture

## Purpose
- Define the system structure, runtime views, deployment shape, and cross-cutting concepts for Flow Approval Hub.

## Architecture Goals
- Preserve deterministic workflow and audit history.
- Isolate external fulfillment dependencies from core request state.
- Keep the experience-facing boundary simple for requesters and approvers.

## Context And Boundaries
- In scope: `request intake, approval routing, request view retrieval, notification triggers, fulfillment task issuance, reconciliation`
- Out of scope: `downstream work execution, enterprise identity provider implementation, analytics warehousing`
- External systems: `identity provider, fulfillment platform, notification delivery channels`

```mermaid
flowchart LR
    Requester["ACT-101 Requester"] --> Gateway["CMP-101 Experience Gateway"]
    Approver["ACT-102 Approver"] --> Gateway
    Operator["ACT-103 Operations Admin"] --> Gateway
    Gateway --> Workflow["CMP-102 Workflow Engine"]
    Workflow --> Ledger["CMP-103 Request Ledger"]
    Workflow --> Notifications["CMP-104 Notification and Audit Projection"]
    Workflow --> Integration["CMP-105 Fulfillment Integration Boundary"]
    Integration --> Fulfillment["External Fulfillment Platform"]
```

## Components
| Component ID | Component | Responsibility | Notes |
|---|---|---|---|
| `CMP-101` | Experience Gateway | Accepts actor requests, performs edge validation, and exposes request views | Can be delivered through UI plus API, but the design treats it as one boundary |
| `CMP-102` | Workflow Engine | Owns request lifecycle, approval policy evaluation, decisions, and event emission | Implements the state machine from `ADR-0001` |
| `CMP-103` | Request Ledger | Stores current request view, policy snapshot, fulfillment summary, and immutable audit entries | Logical persistence boundary, not a prescribed datastore |
| `CMP-104` | Notification and Audit Projection | Builds actor-facing notifications and operator-facing timelines from state changes | May consume events asynchronously |
| `CMP-105` | Fulfillment Integration Boundary | Translates approved requests into downstream tasks and reconciles external status | Shields core components from external system semantics |

```mermaid
flowchart TB
    C1["CMP-101 Experience Gateway"] --> C2["CMP-102 Workflow Engine"]
    C2 --> C3["CMP-103 Request Ledger"]
    C2 --> C4["CMP-104 Notification and Audit Projection"]
    C2 --> C5["CMP-105 Fulfillment Integration Boundary"]
    C5 --> EXT["External Fulfillment Platform"]
```

## Runtime Views
### Scenario `SCN-101`
```mermaid
sequenceDiagram
    participant R as ACT-101
    participant G as CMP-101
    participant W as CMP-102
    participant L as CMP-103
    participant N as CMP-104
    R->>G: Submit request
    G->>W: CNT-101
    W->>L: Persist request, policy snapshot, audit entry
    W->>N: CNT-104 state change
    W-->>G: Accepted request state
    G-->>R: Request id and status
```

### Scenario `SCN-102`
```mermaid
sequenceDiagram
    participant A as ACT-102
    participant G as CMP-101
    participant W as CMP-102
    participant L as CMP-103
    participant I as CMP-105
    A->>G: Review request
    G->>W: CNT-102
    W->>L: Persist decision and audit
    W->>I: CNT-105 if approved
    W-->>G: Updated request state
    G-->>A: Decision outcome
```

### Scenario `SCN-103`
```mermaid
sequenceDiagram
    participant O as ACT-103
    participant G as CMP-101
    participant I as CMP-105
    participant W as CMP-102
    participant L as CMP-103
    O->>G: Open delayed task
    G->>I: Request reconciliation
    I->>W: External status result
    W->>L: Persist reconciled state and audit
    W-->>G: Updated request view
    G-->>O: Reconciliation result
```

## Deployment Shape
- Runtime units: `At minimum, the experience boundary, workflow engine, logical ledger, and integration boundary must exist even if some are co-deployed.`
- Data boundaries: `Request and audit data remain inside the ledger boundary; downstream task state may be cached locally but the external system remains source of truth for execution details.`
- Scaling posture: `Read-heavy request viewing can scale separately from workflow processing if needed.`
- Environment model: `One production environment plus at least one lower environment with fulfillment integration simulation.`

## Cross-Cutting Concepts
- Security: `Actor identity is verified before commands or queries execute; authorization is enforced in the workflow engine using capability and policy context.`
- Observability: `Core commands and events emit success, failure, and lag signals tied to request and correlation identifiers.`
- Configuration and secrets: `Policy definitions, integration credentials, and notification routing are managed as configuration, not embedded in request data.`
- Error handling: `Validation and business rule failures are synchronous; downstream failures are retried and escalated operationally without losing committed local state.`
- Versioning and compatibility: Contract evolution follows the policy in `ADR-0002` and uses additive change by default.

## Risks
| Risk ID | Risk | Impact | Mitigation |
|---|---|---|---|
| `RISK-101` | External fulfillment updates arrive late or not at all | Requesters and operators may see stale status | Reconciliation workflow, lag alerts, idempotent task issuance |
| `RISK-102` | Approval policy changes after a request enters routing | Decisions become inconsistent or disputed | Snapshot policy at submission and retain it in the ledger |

## Inputs
- Contracts from `docs/05-contracts.md`.
- Scenarios from `docs/03-scenarios.md`.
- Accepted ADRs from `docs/adr/`.

## Outputs
- A complete stack-independent architecture and runtime view for implementation.

## Assumptions
- The core workflow and ledger responsibilities should remain distinct even if physically co-located.

## Open Questions
- None.

## Related IDs
- `CMP-101`
- `CNT-101`
- `SCN-101`
- `NFR-101`
- `ADR-0001`
