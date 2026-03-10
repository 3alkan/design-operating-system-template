# Template Setup Guide

Use this guide right after clicking **Use this template**.

## 1) Initial Repository Setup
1. Rename the repository and set its description.
2. Replace `[PROJECT_NAME]`, `[PROJECT_DESCRIPTION]`, and `[MAINTAINER_EMAIL]`.
3. Read `README.md`, `AGENTS.md`, and `docs/10-authoring-conventions.md`.

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
- Read `examples/reference-product/` end to end before filling the project-specific artifacts.
- Copy the level of specificity, not the business domain.
- Reuse the pattern library in `docs/patterns/` when similar concerns appear.

## 4) Replace Placeholders Safely
- Replace project placeholders globally.
- Keep `[TBD]`, `[ASSUMPTION]`, and `[OPEN QUESTION]` only while the repo remains in template mode.
- Remove all unresolved placeholders before claiming Gate 2 readiness.

## 5) Create ADRs Early
1. Copy `docs/adr/0000-template.md` into `docs/adr/0001-[short-title].md`.
2. Add at least two ADRs before implementation begins.
3. Link accepted ADRs from `docs/06-architecture.md` and `docs/09-traceability.md`.

## 6) Validate Continuously
- While still shaping the template instance:
  - `python scripts/validate_template.py --mode template --root .`
- When the project-specific design is complete:
  - `python scripts/validate_template.py --mode instance --root .`

## Ready For Implementation Gate
- [ ] Core artifacts `01` through `09` contain project-specific content.
- [ ] Traceability links goals, scenarios, capabilities, contracts, components, checks, and ADRs.
- [ ] At least two ADRs are accepted.
- [ ] No critical placeholders remain.
- [ ] Instance validation passes.
