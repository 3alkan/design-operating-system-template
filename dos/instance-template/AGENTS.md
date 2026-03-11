# AGENTS.md

This repository is a downstream product-design instance created from the canonical Design Operating System package. Materialized root artifacts are the source of truth between architect, Codex, developers, and downstream LLMs.

## Source of Truth (Instance Artifact Spine)
- `docs/00-system-purpose.md`: product mission, usage modes, completion standard.
- `docs/01-product-scope.md`: actors, problems, goals, constraints, non-goals.
- `docs/02-domain-model.md`: domain concepts, invariants, lifecycle rules, glossary.
- `docs/03-scenarios.md`: user and system scenarios with outcomes and failure paths.
- `docs/04-capabilities.md`: capability catalog with acceptance criteria.
- `docs/05-contracts.md`: abstract commands, queries, events, payload semantics, error rules.
- `docs/06-architecture.md`: components, boundaries, runtime views, deployment shape, cross-cutting concepts.
- `docs/07-quality.md`: definition of done, verification strategy, review checklist.
- `docs/08-operations.md`: release, rollback, observability, troubleshooting, operating model.
- `docs/09-traceability.md`: mappings across goals, scenarios, capabilities, contracts, components, ADRs, and checks.
- `docs/10-authoring-conventions.md`: required schema, statuses, IDs, placeholder policy, and update rules.
- `docs/adr/`: project-specific architecture decision records.
- `INSTANCE_METADATA.json`: lineage data for the source DOS release and package hash.

If code and artifacts conflict, artifacts win until updated.

## Design Readiness Gates
- Gate 1 (Ready To Shape The Design)
  - The artifact spine exists with required headings and front matter.
  - A manual artifact-consistency review confirms the instance surfaces align.
- Gate 2 (Ready For Implementation)
  - Core artifacts `01` through `09` are project-specific and internally consistent.
  - At least two ADRs are accepted in `docs/adr/`.
  - Contracts, runtime scenarios, quality expectations, and operational model are specified abstractly.
  - Traceability links goals, scenarios, capabilities, contracts, components, and checks.
  - Manual review confirms no critical placeholders remain in the instance.
- Gate 3 (Ready To Merge Structural Changes)
  - Definition of Done in `docs/07-quality.md` is satisfied.
  - PR template is fully completed.
  - Review evidence and any configured CI checks pass.

No product/application code is allowed before Gate 2.

## Artifacts Are The Contract
- Any change to product scope, behavior, domain, interfaces, components, runtime behavior, deployment shape, or cross-cutting policy must update the relevant artifacts and `docs/09-traceability.md`.
- Fixed structural decisions must be recorded in `docs/adr/`.
- PRs that change structure without matching artifact updates are not review-ready.
