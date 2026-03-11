---
artifact_type: authoring-spec
artifact_id: SPEC-001
status: active
owner: "[PROJECT_CONTACT_EMAIL]"
related_ids:
  - SYS-001
assumptions:
  - "[ASSUMPTION] The project may choose any implementation stack."
open_questions:
  - "[OPEN QUESTION] Whether the team will add extra artifact types beyond the core set."
---

# 10 - Authoring Conventions

## Purpose
- Define the required structure that makes this repository readable by humans and safe for LLM-assisted updates.
- Standardize IDs, statuses, placeholders, and cross-artifact references.

## Required Front Matter
Every artifact document in the instance spine and ADR set must declare:
- `artifact_type`
- `artifact_id`
- `status`
- `owner`
- `related_ids`
- `assumptions`
- `open_questions`

## Required Section Names
Core spine documents must preserve their titled sections exactly. Each document should include:
- `Purpose`
- `Inputs`
- `Outputs`
- `Assumptions`
- `Open Questions`
- `Related IDs`

Artifact-specific sections may add more detail, but the required sections must remain present.

## Artifact ID Scheme
- `SPEC-###`: project authoring conventions
- `SYS-###`: system-purpose statements
- `ACT-###`: actor definitions
- `GOAL-###`: goals and success criteria
- `CON-###`: constraints
- `DOM-###`: domain concepts
- `INV-###`: invariants
- `SCN-###`: scenarios
- `CAP-###`: capabilities
- `CNT-###`: contracts
- `CMP-###`: components
- `NFR-###`: non-functional requirements
- `OPS-###`: operational procedures or controls
- `RISK-###`: risks
- `ADR-####`: architecture decision records
- `PAT-###`: reusable patterns
- `CHK-###`: review or verification checks

IDs must be unique within a completed project instance.

## Status Values
Allowed statuses:
- `draft`
- `candidate`
- `accepted`
- `active`
- `deprecated`
- `superseded`

Use:
- `draft` or `candidate` for early work and in-progress artifacts.
- `accepted` for locked design decisions and completed artifacts.
- `active` for stable rules or operationally active items.

## Placeholder Policy
Allowed placeholder tokens:
- `[PROJECT_NAME]`
- `[PROJECT_DESCRIPTION]`
- `[PROJECT_CONTACT_EMAIL]`
- `INSTANCE_DESIGN_VERSION`
- `PRODUCT_VERSION`
- `[TBD]`
- `[ASSUMPTION]`
- `[OPEN QUESTION]`

Rules:
- A newly created instance may keep placeholders while the design is still incomplete.
- Active project instances should resolve project placeholders and critical design placeholders before Gate 2.
- Placeholders may remain only if they do not force an implementer to invent missing core design during handoff.
- Placeholder text must never replace an artifact ID.

## Traceability Rules
- Every `GOAL` must link to at least one `SCN` and one `CAP`.
- Every `SCN` must link to at least one `CAP`.
- Every `CAP` must link to at least one `CNT`, one `CMP`, and one `CHK`.
- Every `CNT` must link to at least one `CMP`.
- Every `CMP` used in architecture must appear in `design/09-traceability.md`.
- Accepted ADRs must link to impacted components, contracts, or cross-cutting rules.

## Authoring Rules For Humans And LLMs
- Keep headings stable; extend with new sections only when the conventions are updated.
- Prefer tables for inventories and mappings.
- Keep scenarios concrete, including preconditions, main flow, alternate flow, and failure behavior.
- Keep contracts abstract: define intent, inputs, outputs, errors, and guarantees without binding to a transport or stack unless an ADR fixes it.
- Record open design gaps explicitly rather than hiding them in prose.
- Write at the level of implementation-safe abstraction: leave stack choice open, but do not leave core behavior, boundaries, contracts, or operating expectations undefined.

## Review Contract
- Review this instance for artifact consistency before claiming Gate 2 readiness.
- Review covers file presence, headings, front matter keys, ID consistency, cross-reference integrity, ADR minimums, traceability coverage, placeholder policy, and whether the repo can be implemented without inventing missing core design.

## Inputs
- Instance artifact definitions.
- Repo contribution workflow.
- Manual review expectations.

## Outputs
- Stable authoring rules for all documents in this repository.
- A consistent review contract for this instance.

## Assumptions
- Implementers may choose different stacks while honoring the same abstract design.

## Open Questions
- Whether future versions should split traceability into multiple files for very large systems.

## Related IDs
- `SYS-001`
- `CHK-001`
