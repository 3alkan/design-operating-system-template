# Contributing

Thanks for improving the DOS.

## How To Propose Changes
1. Open an issue using the forms in `.github/ISSUE_TEMPLATE/`.
2. Describe the affected DOS paths or artifact IDs, the design problem, and the intended impact on downstream instances.
3. Submit a PR using `.github/PULL_REQUEST_TEMPLATE.md`.

## Contribution Rules
- This repository owns the canonical DOS package.
- No product/application code is allowed before Gate 2.
- Product/application code is allowed after Gate 2.
- Contributions must preserve stack independence.
- The frozen package under `dos/` remains the source of truth, and structural changes must update the relevant package assets together.
- Placeholder tokens such as `[PROJECT_NAME]`, `[PROJECT_DESCRIPTION]`, `[PROJECT_CONTACT_EMAIL]`, `INSTANCE_DESIGN_VERSION`, `[TBD]`, `[ASSUMPTION]`, and `[OPEN QUESTION]` may remain only where the instance-seed authoring conventions allow them.

## Authoring Rules
- Follow `dos/instance-seed/docs/10-authoring-conventions.md` when changing the downstream instance contract.
- Use fixed section headings and front matter keys.
- Assign stable artifact IDs and maintain `related_ids`.
- Use Mermaid-only diagrams in fenced ` ```mermaid ` blocks.
- Keep prose concrete enough for downstream implementation without fixing a stack prematurely.

## Review Checklist
- [ ] Change respects the current gate model.
- [ ] Affected DOS paths or artifact IDs are declared in the issue or PR.
- [ ] Related package artifacts are updated together.
- [ ] If the downstream instance contract changed, matching traceability or ADR starters were updated in `dos/instance-seed/`.
- [ ] Fixed structural decisions are captured where needed.
- [ ] Placeholder policy remains valid for the DOS package being released.
- [ ] Review steps or other evidence are included in the PR.

## Contribution Forms
- Use issue forms for feature proposals, bugs, ADR proposals, and research spikes.
- Use the PR form and complete the `Plan`, artifact impact, and review sections.
