---
artifact_type: pattern
artifact_id: PAT-004
status: active
owner: "[PROJECT_CONTACT_EMAIL]"
related_ids:
  - ACT-001
  - CAP-001
  - CNT-001
assumptions:
  - "[ASSUMPTION] Actor identity and access scope affect behavior."
open_questions:
  - "[OPEN QUESTION] Whether the completed instance needs attribute-based, role-based, or policy-based access control."
---

# PAT-004: Identity And Authorization

## Purpose
- Make authentication context and authorization decisions explicit in design artifacts.

## When To Use
- Different actors have different permissions, visibility, or workflow powers.

## Design Guidance
- Name the actor identity source and trust boundary abstractly.
- Define authorization rules at capability and contract level.
- Document audit expectations for privileged actions.

## Tradeoffs
- Clearer security posture and fewer hidden assumptions.
- More up-front design detail and access-rule maintenance.

## Artifact Updates
- Product scope: define actors and trust assumptions.
- Capabilities: state who can invoke each capability.
- Contracts: define required identity context and failure responses.
- Operations: define audit and incident expectations.

## Inputs
- Actor model and security expectations.

## Outputs
- A consistent access-control model that survives stack changes.

## Assumptions
- Authorization behavior is part of product design, not just implementation detail.

## Open Questions
- Whether downstream projects need delegated administration or impersonation rules.

## Related IDs
- `PAT-004`
- `ACT-001`
- `CAP-001`
- `CNT-001`
