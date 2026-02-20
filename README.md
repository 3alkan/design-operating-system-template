# [PROJECT_NAME]

Docs-first architecture and delivery template for developer teams.

## What This Template Is
- A docs-as-medium starter kit where documentation is the contract.
- Includes a docs spine (`docs/00` to `docs/05`), ADR system (`docs/adr/`), and GitHub issue/PR templates.
- Mermaid-only diagram workflow in Markdown for architecture and runtime views.

## Who It Is For
- Developers and technical leads who want implementation-agnostic design before coding.

## Quick Start
1. Click **Use this template** on GitHub to create a new repository.
2. Update placeholders like `[PROJECT_NAME]`, `[PROJECT_DESCRIPTION]`, and `[MAINTAINER_EMAIL]`.
3. Fill `docs/00-idea.md` to `docs/05-runbook.md` in order.
4. Write ADRs in `docs/adr/` for major structural decisions.
5. Start implementation only after the repo gates are satisfied (see `AGENTS.md`).
6. Keep docs updated as the source of truth as work evolves.

## What To Edit First
- `docs/00-idea.md`
- `docs/01-prd-lite.md`
- `docs/02-architecture.md`
- `docs/adr/0000-template.md` (copy to create first ADRs)

## Mermaid-Only Diagrams
- Diagrams must be embedded in Markdown fenced blocks using ` ```mermaid `.
- GitHub renders Mermaid diagrams directly in Markdown.
- Policy reference: `docs/diagrams/README.md`.

## License (Default)
- Default license: **GNU GPL v3.0** (`LICENSE`).
- Why GPLv3 by default: ensures derivatives remain open under the same license (strong copyleft).
- How to change license:
  - Replace `LICENSE` with your preferred license text.
  - Update this section and any license badges/mentions.

## Community Profile Checklist Hint
This template includes common community health files used by GitHub community profile checks:
- `LICENSE`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- issue and PR templates in `.github/`

