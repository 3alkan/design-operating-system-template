# Contributing

Thanks for improving this product-design instance.

## How To Propose Changes
1. Open an issue using the templates in `.github/ISSUE_TEMPLATE/`.
2. Describe the affected artifact IDs, the design problem, and the intended impact on traceability.
3. Submit a PR using `.github/PULL_REQUEST_TEMPLATE.md`.

## Contribution Rules
- No product/application code is allowed before Gate 2.
- Product/application code is allowed after Gate 2.
- Artifacts remain the source of truth, and structural code changes must update the relevant artifacts and traceability rules together.
- Placeholder tokens such as `[PROJECT_NAME]`, `[PROJECT_DESCRIPTION]`, `[PROJECT_CONTACT_EMAIL]`, `INSTANCE_DESIGN_VERSION`, `[TBD]`, `[ASSUMPTION]`, and `[OPEN QUESTION]` may remain only where the authoring conventions allow them.

## Authoring Rules
- Follow `docs/10-authoring-conventions.md`.
- Use fixed section headings and front matter keys.
- Assign stable artifact IDs and maintain `related_ids`.
- Use Mermaid-only diagrams in fenced ` ```mermaid ` blocks.
- Keep prose concrete enough for implementation without fixing a stack prematurely.
