# AGENTS.md

This repository is docs-first. Documentation is the source of truth between architect, Codex, and developers.

## Source of Truth (Doc Spine)
- `docs/00-idea.md`: idea, users, problem, constraints.
- `docs/01-prd-lite.md`: goals, MVP scope, acceptance criteria.
- `docs/02-architecture.md`: architecture intent, boundaries, contracts, runtime views.
- `docs/03-plan.md`: milestones, sequencing, risk log, spikes.
- `docs/04-quality.md`: DoD, test strategy, CI expectations, review checklist.
- `docs/05-runbook.md`: release, rollback, operations, troubleshooting.
- `docs/adr/`: architecture decision records (ADRs).
- `docs/diagrams/README.md`: diagram policy.

If docs and code conflict, docs win until updated.

## Phase Gates
- Gate 1 (Ready for Architecture):
  - `docs/01-prd-lite.md` has MVP acceptance criteria with explicit done conditions.
- Gate 2 (Ready for Implementation):
  - `docs/02-architecture.md` includes required views and 3 runtime scenarios.
  - At least 2 ADRs exist in `docs/adr/` (can include `[TBD]` where needed).
  - Interfaces/contracts are specified abstractly (implementation-agnostic).
- Gate 3 (Ready to Merge Features):
  - DoD in `docs/04-quality.md` is satisfied.
  - PR template is fully completed.
  - CI checks (when configured) pass.

No product/application code is allowed before Gate 2.

## Docs Are the Contract
- Any structural change (modules, boundaries, interfaces, runtime behavior, deployment shape, cross-cutting policy) must update:
  - `docs/02-architecture.md`, and/or
  - relevant ADRs in `docs/adr/`.
- PRs that change structure without doc updates are not review-ready.

## Codex Workflow In This Repo
Use this sequence for every substantial change:
1. Spec: align with PRD, architecture, runbook, and ADR context.
2. Plan: define scoped steps and risks.
3. Patch: apply minimal, traceable changes.
4. Verify: confirm acceptance criteria, checks, and doc impact.

## PR Plan Requirement
Every PR must contain a short `Plan` section with:
- files touched,
- test approach,
- documentation impact (`PRD`, `Architecture`, `ADR`, `Runbook`).

## Diagram Policy (Mermaid-Only)
- Diagrams must be embedded in Markdown fenced blocks using ` ```mermaid `.
- Keep diagrams small and readable.
- Split large diagrams by concern.
- Prefer simple styles and labels over visual effects.
- Allowed diagram types: `flowchart`, `sequenceDiagram`, `stateDiagram-v2`.

