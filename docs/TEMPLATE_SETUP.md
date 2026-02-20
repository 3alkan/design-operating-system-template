# Template Setup Guide

Use this guide right after clicking **Use this template**.

## 1) Initial Repository Setup
1. Rename repository and set description.
2. Replace placeholders such as `[PROJECT_NAME]`, `[PROJECT_DESCRIPTION]`, `[MAINTAINER_EMAIL]`.
3. Confirm `AGENTS.md` phase gates match your intended process.

## 2) Fill Docs Spine In Order
1. `docs/00-idea.md`
2. `docs/01-prd-lite.md`
3. `docs/02-architecture.md`
4. `docs/03-plan.md`
5. `docs/04-quality.md`
6. `docs/05-runbook.md`

## 3) Replace Placeholders Safely
- Replace only project-specific placeholders.
- Keep structural placeholders when decisions are still open (`[TBD]`, `[ASSUMPTION]`, `[OPEN QUESTION]`).
- Make replacements consistently across files.

## 4) Rename Docs (Optional)
- Keep numeric prefixes (`00`, `01`, `02`, ...) to preserve reading order.
- If renaming, update references in `AGENTS.md`, README, and templates.

## 5) Create First ADRs
- Copy `docs/adr/0000-template.md` to `docs/adr/0001-[short-title].md` and `docs/adr/0002-[short-title].md`.
- Capture context, decision, alternatives, rejected options, and consequences.
- Link ADRs from architecture sections when relevant.

## 6) Keep Docs As Source of Truth
- Any structural change must update `docs/02-architecture.md` and/or ADRs.
- Keep Mermaid diagrams embedded in Markdown (` ```mermaid `) and small by concern.

## Ready to Implement Gate
- [ ] Docs `00` to `05` are filled with project-specific content.
- [ ] Architecture includes required context/container/runtime views.
- [ ] Mermaid diagrams are present and readable in GitHub Markdown.
- [ ] At least two initial ADRs are written.
- [ ] Definition of Done is agreed in `docs/04-quality.md`.
- [ ] Gate 2 conditions in `AGENTS.md` are satisfied.
