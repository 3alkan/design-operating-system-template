# Changelog

All notable DOS/template changes are documented in this file.

The format follows Keep a Changelog and this DOS repo uses Semantic Versioning for `DOS_VERSION`.

## Downstream Project Changelog Placeholder
- This repository is the canonical DOS/template repo, so it does not track downstream project change history.
- Downstream project repos should replace `PROJECT_NAME_DESIGN_VERSION` in their own `VERSION` file and maintain their own changelog.

## DOS Template Release History

### [Unreleased]
#### Added
- [TBD]

#### Changed
- [TBD]

#### Fixed
- [TBD]

### [0.3.0] - 2026-03-10
#### Changed
- Replaced validator-driven workflow language with manual artifact-consistency review across the DOS repo.
- Clarified that bundled patterns and the reference example are DOS teaching material, not downstream product scope by default.
- Updated contribution and PR guidance to follow the gate model, including allowing product/application code after Gate 2.
- Switched template-owned public contact placeholders to `[PROJECT_CONTACT_EMAIL]`.
- Changed `VERSION` semantics to use `DOS_VERSION` plus the downstream placeholder `PROJECT_NAME_DESIGN_VERSION`.

#### Removed
- Automated validator script and validator-specific GitHub workflow automation.

### [0.2.0] - 2026-03-10
#### Added
- Artifact-based design spine (`docs/00` to `docs/10`) with authoring conventions and pattern library.
- Completed reference example product in `examples/reference-product/`.
- Review-oriented collaboration surfaces for issues, PRs, and maintainer setup.

#### Changed
- Repository positioning from docs-first architecture template to design-system template.
- ADR and diagram guidance to align with traceable design artifacts.

### [0.1.0] - 2026-02-20
#### Added
- Initial docs-first template release.
- Docs spine (`docs/00` to `docs/05`), ADR system, and Mermaid diagram policy.
- GitHub issue and PR templates for docs-driven workflow.
- Community health files (`LICENSE`, `CONTRIBUTING`, `CODE_OF_CONDUCT`, `SECURITY`).
