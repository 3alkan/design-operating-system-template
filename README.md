# [PROJECT_NAME]

Tech-stack-independent design-system template for defining a product end to end in a form that is abstractly implementation-ready.

Current DOS version: `0.2.0`

## What This Template Is
- A design operating system, not a loose docs repository.
- A shared medium for architects, developers, and LLMs to define product intent, domain, behavior, contracts, architecture, quality, and operations.
- A template whose completed instance should be sufficient for a capable developer or LLM to implement the product end to end in a chosen stack with minimal guessing.

## Design Contract
- Design artifacts are the source of truth.
- Technology choices are intentionally left open unless an ADR fixes them.
- The template must stay implementation-independent while being concrete about behavior, boundaries, contracts, runtime scenarios, and quality expectations.
- Structural changes require matching artifact and traceability updates before review.

## What The Template Contains
- A numbered artifact spine in `docs/00` to `docs/09`.
- Authoring and review rules in `docs/10-authoring-conventions.md`.
- Architecture decision records in `docs/adr/`.
- Reusable design patterns in `docs/patterns/` as DOS reference material for humans and LLMs.
- A completed reference example in `examples/reference-product/` as DOS teaching material for humans and LLMs.
- GitHub issue and PR templates for design-driven collaboration.

Patterns and the bundled reference example exist to explain the DOS itself. They do not define downstream product scope by default.

## Who It Is For
- Product-minded engineers and technical leads who want a stack-independent design package before implementation.
- Teams that want design traceability across goals, scenarios, capabilities, contracts, architecture, and operations.
- LLM-assisted workflows that need stable structure and explicit update rules.

## How To Use It
1. Click **Use this template** on GitHub.
2. Replace repository placeholders such as `[PROJECT_NAME]`, `[PROJECT_DESCRIPTION]`, `[PROJECT_CONTACT_EMAIL]`, and `PROJECT_NAME_DESIGN_VERSION`.
3. Read `docs/00-system-purpose.md` through `docs/10-authoring-conventions.md` in order.
4. Define or update ADRs in `docs/adr/` for fixed structural decisions.
5. Use `docs/patterns/` and `examples/reference-product/` as DOS reference material for the level of clarity and traceability expected.
6. Treat those bundled materials as teaching aids, not as downstream product scope by default.
7. Review artifacts manually for consistency before claiming a downstream project instance is ready for implementation.

## Artifact Spine
1. `docs/00-system-purpose.md`
2. `docs/01-product-scope.md`
3. `docs/02-domain-model.md`
4. `docs/03-scenarios.md`
5. `docs/04-capabilities.md`
6. `docs/05-contracts.md`
7. `docs/06-architecture.md`
8. `docs/07-quality.md`
9. `docs/08-operations.md`
10. `docs/09-traceability.md`
11. `docs/10-authoring-conventions.md`

## Version Semantics
- `VERSION` contains `DOS_VERSION`, which is the release version of this DOS/template repo.
- `VERSION` also contains `PROJECT_NAME_DESIGN_VERSION`, which is a generic placeholder pattern for downstream project instances.
- Downstream project repos should replace `PROJECT_NAME_DESIGN_VERSION` with their own design version value.

## Review Model
- Use manual artifact-consistency review instead of automated enforcement tooling.
- Review the root template when changing DOS structure, rules, or contributor workflow.
- Review the reference example when changing teaching material or the expected quality bar.
- Review both surfaces when a DOS change affects how humans or LLMs should understand the template.

## Mermaid-Only Diagrams
- Diagrams must be embedded in Markdown fenced blocks using ` ```mermaid `.
- Keep diagrams small and split by concern.
- Allowed diagram types: `flowchart`, `sequenceDiagram`, `stateDiagram-v2`.

## License (Default)
- Default license: **GNU GPL v3.0** (`LICENSE`).
- Replace `LICENSE` if your downstream project needs a different license.

## Community Profile Checklist Hint
This template includes common community health files used by GitHub community profile checks:
- `LICENSE`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- issue and PR templates in `.github/`
