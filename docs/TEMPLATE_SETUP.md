# Template Setup Guide

Use this guide right after clicking **Use this template**.

## 1) Initial Repository Setup
1. Rename the repository and set its description.
2. Replace `[PROJECT_NAME]`, `[PROJECT_DESCRIPTION]`, `[PROJECT_CONTACT_EMAIL]`, and `PROJECT_NAME_DESIGN_VERSION`.
3. Read `README.md`, `AGENTS.md`, and `docs/10-authoring-conventions.md`.
4. Keep `DOS_VERSION` as the DOS/template release marker in this repo.

## 2) Fill The Artifact Spine In Order
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

## 3) Use The Reference Example
- Read `examples/reference-product/` end to end before filling project-specific artifacts.
- Copy the level of specificity, not the business domain.
- Reuse the pattern library in `docs/patterns/` when similar concerns appear.
- Treat both `docs/patterns/` and `examples/reference-product/` as DOS reference material for humans and LLMs.
- They help explain the DOS and do not define downstream product scope by default.

## 4) Replace Placeholders Safely
- Replace project placeholders globally.
- Keep `[TBD]`, `[ASSUMPTION]`, and `[OPEN QUESTION]` only while the repo remains a reusable DOS template or the downstream design is still incomplete.
- Remove all unresolved placeholders before claiming Gate 2 readiness.

## 5) Create ADRs Early
1. Copy `docs/adr/0000-template.md` into `docs/adr/0001-[short-title].md`.
2. Add at least two ADRs before implementation begins.
3. Link accepted ADRs from `docs/06-architecture.md` and `docs/09-traceability.md`.

## 6) Review Continuously
- Review the root DOS surfaces when changing template rules, patterns, examples, or contributor workflow.
- Review downstream project artifacts for consistency before claiming Gate 2 readiness.
- Confirm that artifacts, ADRs, and traceability stay aligned whenever structure changes.

## Ready For Implementation Gate
- [ ] Core artifacts `01` through `09` contain project-specific content.
- [ ] Traceability links goals, scenarios, capabilities, contracts, components, checks, and ADRs.
- [ ] At least two ADRs are accepted.
- [ ] No critical placeholders remain.
- [ ] Manual artifact-consistency review passes.
