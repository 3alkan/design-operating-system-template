# AGENTS.md

This repository is a product-design instance. Root artifacts are the source of truth between architect, Codex, developers, and collaborating LLMs.

The purpose of this repository is to define one product end to end in a stack-independent but implementation-ready form.

## Source of Truth (Instance Artifact Spine)
- `design/00-system-purpose.md`: product mission, usage modes, completion standard.
- `design/01-product-scope.md`: actors, problems, goals, constraints, non-goals.
- `design/02-domain-model.md`: domain concepts, invariants, lifecycle rules, glossary.
- `design/03-scenarios.md`: user and system scenarios with outcomes and failure paths.
- `design/04-capabilities.md`: capability catalog with acceptance criteria.
- `design/05-contracts.md`: abstract commands, queries, events, payload semantics, error rules.
- `design/06-architecture.md`: components, boundaries, runtime views, deployment shape, cross-cutting concepts.
- `design/07-quality.md`: definition of done, verification strategy, review checklist.
- `design/08-operations.md`: release, rollback, observability, troubleshooting, operating model.
- `design/09-traceability.md`: mappings across goals, scenarios, capabilities, contracts, components, ADRs, and checks.
- `design/10-authoring-conventions.md`: required schema, statuses, IDs, placeholder policy, and update rules.
- `design/adr/`: project-specific architecture decision records.
- `INSTANCE_METADATA.json`: origin metadata for this instance.
- `implementation/`: default location for product code after Gate 2.

If code and artifacts conflict, artifacts win until updated.

## Design Readiness Gates
- Gate 1 (Ready To Shape The Design)
  - The artifact spine exists with required headings and front matter.
  - A manual artifact-consistency review confirms the instance surfaces align.
- Gate 2 (Ready For Implementation)
  - Core artifacts `01` through `09` are project-specific and internally consistent.
  - At least two ADRs are accepted in `design/adr/`.
  - Contracts, runtime scenarios, quality expectations, and operational model are specified abstractly.
  - Traceability links goals, scenarios, capabilities, contracts, components, and checks.
  - Manual review confirms no critical placeholders remain in the instance.
- Gate 3 (Ready To Merge Structural Changes)
  - Definition of Done in `design/07-quality.md` is satisfied.
  - PR form is fully completed.
  - Review evidence and any configured CI checks pass.

No product/application code is allowed before Gate 2. After Gate 2, product code belongs in `implementation/` by default.

## Artifacts Are The Contract
- Any change to product scope, behavior, domain, interfaces, components, runtime behavior, deployment shape, or cross-cutting policy must update the relevant artifacts and `design/09-traceability.md`.
- Fixed structural decisions must be recorded in `design/adr/`.
- Structural code changes after Gate 2 must keep `design/` aligned with `implementation/`.
- PRs that change structure without matching artifact updates are not review-ready.
