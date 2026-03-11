---
artifact_type: adr-guide
artifact_id: SPEC-002
status: active
owner: "[PROJECT_CONTACT_EMAIL]"
related_ids:
  - ADR-0001
  - CMP-001
assumptions:
  - "[ASSUMPTION] Structural decisions worth preserving will exist even in stack-independent designs."
open_questions:
  - "[OPEN QUESTION] Whether future versions need ADR starters for reversible experiments."
---

# ADRs

## Purpose
- Capture design decisions that materially shape boundaries, contracts, cross-cutting rules, or operational posture.

## When ADRs Are Required
- A structural boundary or deployment shape is fixed.
- A contract, consistency model, or versioning rule is fixed.
- A security, observability, or error-handling policy is fixed.
- A tradeoff has long-term consequences or closes meaningful alternatives.

## Naming Scheme
- Files: `NNNN-short-title.md`
- IDs inside the file: `ADR-NNNN`

## Lifecycle
1. `draft`
2. `candidate`
3. `accepted`
4. `superseded`
5. `deprecated`

## Authoring Rules
- Use `0000-record.md`.
- Include impacted artifact IDs.
- Include at least two alternatives.
- Record rejected options and consequences.
- Link the ADR in `design/09-traceability.md`.

## Inputs
- Architecture, contracts, quality, and operations artifacts.

## Outputs
- Durable design decisions that remove ambiguity during implementation.

## Assumptions
- Most completed instances should have at least two accepted ADRs.

## Open Questions
- Whether ADR supersession should automatically update traceability notes.

## Related IDs
- `ADR-0001`
- `CMP-001`
