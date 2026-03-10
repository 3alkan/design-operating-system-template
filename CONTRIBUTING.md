# Contributing

Thanks for improving this template.

## How To Propose Changes
1. Open an issue using the templates in `.github/ISSUE_TEMPLATE/`.
2. Describe the affected artifact IDs, the design problem, and the intended impact on traceability.
3. Submit a PR using `.github/PULL_REQUEST_TEMPLATE.md`.

## Contribution Rules
- This repository is template-focused and DOS-owned.
- No product/application code is allowed before Gate 2.
- Product/application code is allowed after Gate 2.
- Contributions must preserve stack independence.
- Artifacts remain the source of truth, and structural code changes must update the relevant artifacts and traceability rules together.
- Placeholder tokens such as `[PROJECT_NAME]`, `[PROJECT_DESCRIPTION]`, `[PROJECT_CONTACT_EMAIL]`, `PROJECT_NAME_DESIGN_VERSION`, `[TBD]`, `[ASSUMPTION]`, and `[OPEN QUESTION]` may remain only where the authoring conventions allow them.

## Authoring Rules
- Follow `docs/10-authoring-conventions.md`.
- Use fixed section headings and front matter keys.
- Assign stable artifact IDs and maintain `related_ids`.
- Use Mermaid-only diagrams in fenced ` ```mermaid ` blocks.
- Keep prose concrete enough for downstream implementation without fixing a stack prematurely.

## Review Checklist
- [ ] Change respects the current gate model.
- [ ] Affected artifact IDs are declared in the issue or PR.
- [ ] Related artifacts and `docs/09-traceability.md` are updated.
- [ ] If product/application code changed after Gate 2, related structural artifacts were updated.
- [ ] Fixed structural decisions are captured in ADRs where needed.
- [ ] Placeholder policy remains valid for the DOS repo or the downstream project instance being reviewed.
- [ ] Review steps or other evidence are included in the PR.

## Templates
- Use issue templates for feature proposals, bugs, ADR proposals, and research spikes.
- Use the PR template and complete the `Plan`, artifact impact, and review sections.
