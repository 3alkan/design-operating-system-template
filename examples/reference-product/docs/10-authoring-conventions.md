---
artifact_type: template-spec
artifact_id: SPEC-101
status: accepted
owner: "template-maintainer@example.com"
related_ids:
  - SYS-101
assumptions:
  - "This example adopts the same authoring contract as the root template."
open_questions:
  - "None."
---

# 10 - Authoring Conventions

## Purpose
- Record how the reference product applies the template conventions.

## Required Front Matter
- Every artifact in this example declares `artifact_type`, `artifact_id`, `status`, `owner`, `related_ids`, `assumptions`, and `open_questions`.

## Required Section Names
- Each core artifact retains `Purpose`, `Inputs`, `Outputs`, `Assumptions`, `Open Questions`, and `Related IDs`.

## Artifact ID Scheme
- This example uses `SYS-1xx`, `ACT-1xx`, `GOAL-1xx`, `CON-1xx`, `DOM-1xx`, `INV-1xx`, `SCN-1xx`, `CAP-1xx`, `CNT-1xx`, `CMP-1xx`, `NFR-1xx`, `OPS-1xx`, `RISK-1xx`, `ADR-000x`, and `CHK-1xx`.

## Status Values
- Core artifacts and ADRs in this example are `accepted`.

## Placeholder Policy
- This completed instance contains no unresolved template placeholders.

## Traceability Rules
- Every goal links to a scenario and capability.
- Every capability links to contracts, components, and checks.
- Accepted ADRs are referenced in the architecture and traceability matrix.

## Authoring Rules For Humans And LLMs
- Keep contract and component names stable unless the design intentionally changes.
- Update traceability alongside any structural or behavior change.
- Preserve stack independence even when implementation planning begins.

## Validation Contract
- The reference product must pass `python scripts/validate_template.py --mode instance --root examples/reference-product`.

## Inputs
- The root template conventions and the completed example artifacts.

## Outputs
- A locally complete conventions note for the reference product.

## Assumptions
- The example is consumed as a finished design package rather than a starting skeleton.

## Open Questions
- None.

## Related IDs
- `SYS-101`
