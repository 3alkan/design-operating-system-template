# AGENTS.md

This repository is the canonical Design Operating System (DOS) repo. The frozen DOS package under `dos/` is the source of truth between architect, Codex, maintainers, and downstream LLMs.

- `dos/instance-template/docs/00-system-purpose.md` through `dos/instance-template/docs/10-authoring-conventions.md`: the downstream instance artifact contract.
- `dos/instance-template/docs/adr/`: ADR templates and ADR guidance that ship with downstream instances.
- `dos/patterns/`: frozen DOS reference patterns.
- `dos/reference/`: frozen DOS teaching material, including the example instance.
- `dos/dos-manifest.json`: canonical package version, inventory, and integrity metadata.

If repo shell docs and `dos/` conflict, `dos/` wins until updated. In a downstream instance created from this DOS, the materialized root artifacts become that project’s source of truth.

## DOS Package Gates
- Gate 1 (Package Coherent)
  - `dos/instance-template/`, `dos/patterns/`, and `dos/reference/` match the intended DOS release.
  - `dos/dos-manifest.json` matches the frozen package contents.
- Gate 2 (Downstream Instance Ready For Implementation)
  - A materialized downstream instance based on `dos/instance-template/` has project-specific artifacts `01` through `09`.
  - At least two ADRs are accepted in the downstream instance.
  - Contracts, runtime scenarios, quality expectations, and operational model are specified abstractly.
  - Traceability links goals, scenarios, capabilities, contracts, components, and checks.
  - Manual review confirms no critical placeholders remain in the downstream instance.
- Gate 3 (DOS Release Ready)
  - Repo shell docs and contributor surfaces reflect the current DOS package.
  - `VERSION`, `CHANGELOG.md`, and `dos/dos-manifest.json` are aligned.
  - Review evidence and any configured CI checks pass.

No product/application code is allowed inside downstream instances before Gate 2.

## Artifacts Are The Contract
- Any change to downstream design structure must update the relevant files under `dos/instance-template/`.
- Any change to DOS teaching/reference material must update the relevant files under `dos/patterns/` or `dos/reference/`.
- Fixed structural decisions that ship with downstream instances must be recorded in `dos/instance-template/docs/adr/`.
- PRs that change the DOS package without matching artifact updates are not review-ready.

## Codex Workflow In This Repo
Use this sequence for every substantial change:
1. Spec: align with the DOS package boundary, instance-template contract, manifest, and reference assets.
2. Plan: define scoped steps, risks, affected paths, and release impact.
3. Patch: apply minimal, traceable changes.
4. Verify: review DOS package integrity, downstream materialization impact, and path consistency.

## PR Plan Requirement
Every PR must contain a short `Plan` section with:
- affected files or artifact IDs,
- review or test approach,
- DOS impact (`Repo Shell`, `Instance Template`, `Patterns`, `Reference`, `Manifest`).

## Diagram Policy (Mermaid-Only)
- Diagrams must be embedded in Markdown fenced blocks using ` ```mermaid `.
- Keep diagrams small and readable.
- Split large diagrams by concern.
- Prefer simple styles and labels over visual effects.
- Allowed diagram types: `flowchart`, `sequenceDiagram`, `stateDiagram-v2`.
