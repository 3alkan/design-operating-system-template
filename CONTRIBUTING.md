# Contributing

Thanks for improving the DOS.

## How To Propose Changes
1. Open an issue using the forms in `.github/ISSUE_TEMPLATE/`.
2. Describe the affected DOS paths or artifact IDs, the design problem, and the intended DOS package impact.
3. Submit a PR using `.github/PULL_REQUEST_TEMPLATE.md`.

## Contribution Rules
- This repository owns the canonical DOS package.
- This repo is not a downstream product/application repo.
- Keep root-level changes focused on DOS package content, publishing guidance, reference material, and tooling.
- Contributions must preserve stack independence.
- The frozen package under `dos/` remains the source of truth, and structural changes must update the relevant package assets together.
- Changes to DOS goals, boundary, or success criteria must update `docs/DOS_MISSION.md` and any affected repo-shell files.
- Placeholder tokens inside `dos/instance-seed/` may remain only where the seed authoring conventions allow them.

## Authoring Rules
- Follow `dos/instance-seed/design/10-authoring-conventions.md` when changing the packaged downstream product repo.
- Use fixed section headings and front matter keys.
- Assign stable artifact IDs and maintain `related_ids`.
- Use Mermaid-only diagrams in fenced ` ```mermaid ` blocks.
- Keep DOS guidance concrete enough to support downstream implementation without fixing a stack prematurely.

## Review Checklist
- [ ] Change respects the current gate model.
- [ ] Affected DOS paths or artifact IDs are declared in the issue or PR.
- [ ] Related package artifacts are updated together.
- [ ] If the packaged instance seed changed, matching traceability or ADR starters were updated in `dos/instance-seed/`.
- [ ] Fixed structural decisions are captured where needed.
- [ ] Placeholder policy remains valid for the DOS package being released.
- [ ] Review steps or other evidence are included in the PR.

## Contribution Forms
- Use issue forms for feature proposals, bugs, ADR proposals, and research spikes.
- Use the PR form and complete the `Plan`, artifact impact, and review sections.
