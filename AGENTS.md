# AGENTS.md

This repository is a design-system template. Design artifacts are the source of truth between architect, Codex, developers, and downstream LLMs.

## Source of Truth (Artifact Spine)
- `docs/00-system-purpose.md`: template mission, usage modes, completion standard.
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
- `docs/adr/`: architecture decision records.
- `docs/patterns/`: reusable design patterns.

If artifacts and implementation conflict, artifacts win until updated.

## Design Readiness Gates
- Gate 1 (Ready To Shape The Design)
  - The artifact spine exists with required headings and front matter.
  - A manual artifact-consistency review confirms the DOS template surfaces align.
- Gate 2 (Ready For Implementation)
  - Core artifacts `01` through `09` are project-specific and internally consistent.
  - At least two ADRs are accepted in `docs/adr/`.
  - Contracts, runtime scenarios, quality expectations, and operational model are specified abstractly.
  - Traceability links goals, scenarios, capabilities, contracts, components, and checks.
  - Manual review confirms no critical placeholders remain in the downstream project instance.
- Gate 3 (Ready To Merge Structural Changes)
  - Definition of Done in `docs/07-quality.md` is satisfied.
  - PR template is fully completed.
  - Review evidence and any configured CI checks pass.

No product/application code is allowed before Gate 2.

## Artifacts Are The Contract
- Any change to product scope, behavior, domain, interfaces, components, runtime behavior, deployment shape, or cross-cutting policy must update the relevant artifacts and `docs/09-traceability.md`.
- Fixed structural decisions must be recorded in `docs/adr/`.
- PRs that change the design without matching artifact updates are not review-ready.

## Codex Workflow In This Repo
Use this sequence for every substantial change:
1. Spec: align with the artifact spine, ADRs, and patterns.
2. Plan: define scoped steps, risks, and affected artifact IDs.
3. Patch: apply minimal, traceable changes.
4. Verify: run manual artifact-consistency review, confirm traceability, and document artifact impact.

## PR Plan Requirement
Every PR must contain a short `Plan` section with:
- affected files or artifact IDs,
- review or test approach,
- documentation impact (`Scope`, `Domain`, `Scenario`, `Capability`, `Contract`, `Architecture`, `Quality`, `Operations`, `Traceability`, `ADR`).

## Diagram Policy (Mermaid-Only)
- Diagrams must be embedded in Markdown fenced blocks using ` ```mermaid `.
- Keep diagrams small and readable.
- Split large diagrams by concern.
- Prefer simple styles and labels over visual effects.
- Allowed diagram types: `flowchart`, `sequenceDiagram`, `stateDiagram-v2`.
