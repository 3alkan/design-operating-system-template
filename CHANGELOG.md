# Changelog

All notable DOS changes are documented in this file.

The format follows Keep a Changelog and this DOS repo uses Semantic Versioning for `DOS_VERSION`.

## Downstream Project Changelog Placeholder
- This repository is the canonical DOS repo, so it does not track downstream project change history.
- Downstream project repos should set `INSTANCE_DESIGN_VERSION` and `PRODUCT_VERSION` in their own `VERSION` file and maintain their own changelog.

## DOS Release History

### [Unreleased]
#### Added
- [TBD]

#### Changed
- [TBD]

#### Fixed
- [TBD]

### [0.9.0] - 2026-03-11
#### Changed
- Hardened the packaged instance so Gate 2 now reads as the point where implementation can credibly begin in the same repo, not just where coding becomes allowed.
- Strengthened `dos/instance-seed/design/07-quality.md` into the primary implementation-readiness and LLM-handoff contract for downstream instances.
- Updated the packaged instance entry docs, contribution guidance, and issue/PR forms to point at the stronger readiness bar and same-repo lifecycle.
- Aligned the DOS mission, onboarding guidance, and reference example with the stronger instance product standard.

### [0.8.0] - 2026-03-11
#### Changed
- Restructured the packaged instance around `design/` plus `implementation/` to make same-repo implementation the default lifecycle after Gate 2.
- Updated instance versioning to include both `INSTANCE_DESIGN_VERSION` and `PRODUCT_VERSION`.
- Updated instantiation tooling to prefer `--design-version` and support optional `--product-version`.

### [0.7.0] - 2026-03-11
#### Added
- Canonical DOS mission document in `docs/DOS_MISSION.md`.

#### Changed
- Rewrote the root README and shell guidance around the explicit DOS mission and boundary.
- Strengthened the packaged instance entry surfaces so they read as a real product-design repository rather than package scaffolding.

### [0.6.0] - 2026-03-11
#### Changed
- Switched DOS package integrity hashing from `SHA-256` to `SHA3-256`.
- Updated `dos/dos-manifest.json` to record `hash_algorithm` and `sha3_256` file hashes.

### [0.5.0] - 2026-03-11
#### Changed
- Removed GitHub-template positioning from the canonical DOS repo and aligned publishing guidance with the DOS package flow.
- Renamed the downstream copy surface from `dos/instance-template/` to `dos/instance-seed/`.
- Replaced remaining human-facing template wording with DOS, seed, starter, or form language across the repo shell and packaged instance artifacts.

### [0.4.0] - 2026-03-11
#### Added
- Canonical frozen DOS package under `dos/`, including `dos/instance-template/`, `dos/patterns/`, `dos/reference/`, and `dos/dos-manifest.json`.
- Instance materialization tooling in `scripts/instantiate_dos.py`.
- DOS manifest generation tooling in `scripts/build_dos_manifest.py`.
- Downstream instance lineage contract via `INSTANCE_METADATA.json`.

#### Changed
- Repo root now acts as a DOS publishing and governance shell rather than the downstream instance root.
- DOS onboarding now distinguishes the canonical DOS repo, frozen DOS package, and materialized downstream instance.
- Downstream instance versioning now lives in the materialized instance `VERSION` file rather than the DOS repo `VERSION`.

### [0.3.0] - 2026-03-10
#### Changed
- Replaced validator-driven workflow language with manual artifact-consistency review across the DOS repo.
- Clarified that bundled patterns and the reference example are DOS teaching material, not downstream product scope by default.
- Updated contribution and PR guidance to follow the gate model, including allowing product/application code after Gate 2.
- Switched DOS-owned public contact placeholders to `[PROJECT_CONTACT_EMAIL]`.
- Changed `VERSION` semantics to use `DOS_VERSION` plus the downstream placeholder `PROJECT_NAME_DESIGN_VERSION`.

#### Removed
- Automated validator script and validator-specific GitHub workflow automation.

### [0.2.0] - 2026-03-10
#### Added
- Artifact-based design spine (`docs/00` to `docs/10`) with authoring conventions and pattern library.
- Completed reference example product in `examples/reference-product/`.
- Review-oriented collaboration surfaces for issues, PRs, and maintainer setup.

#### Changed
- Repository positioning from docs-first architecture repo to design-system repo.
- ADR and diagram guidance to align with traceable design artifacts.

### [0.1.0] - 2026-02-20
#### Added
- Initial docs-first release.
- Docs spine (`docs/00` to `docs/05`), ADR system, and Mermaid diagram policy.
- GitHub issue and PR forms for docs-driven workflow.
- Community health files (`LICENSE`, `CONTRIBUTING`, `CODE_OF_CONDUCT`, `SECURITY`).
