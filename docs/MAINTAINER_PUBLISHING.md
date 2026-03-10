# Maintainer Publishing Guide

## Mark Repository As GitHub Template
1. Open repository **Settings**.
2. In the general settings area, enable **Template repository**.
3. Save settings.

## Important Notes
- Template repositories cannot include Git LFS objects.
- Remove or migrate LFS-tracked files before enabling template use.

## Pre-Publish Checklist
- [ ] `VERSION` has the correct `DOS_VERSION` for the release.
- [ ] `VERSION` keeps `PROJECT_NAME_DESIGN_VERSION` as a downstream-project placeholder pattern.
- [ ] `CHANGELOG.md` has a dated DOS release section for that version.
- [ ] `README.md` reflects the design-system promise and manual review model.
- [ ] `AGENTS.md` and `docs/10-authoring-conventions.md` are aligned.
- [ ] The artifact spine and pattern library are internally consistent.
- [ ] The reference example is complete and still serves as DOS teaching material.
- [ ] The root template still reads coherently as the canonical DOS repo.
- [ ] `.github/` issue and PR templates reflect artifact IDs and traceability impact.
- [ ] Community files remain current.

## How "Use This Template" Should Feel
- A maintainer or downstream team should understand the repo purpose from `README.md`.
- A newcomer should be able to follow `docs/TEMPLATE_SETUP.md` without guessing artifact order.
- A developer or LLM should be able to inspect `docs/patterns/` and `examples/reference-product/` to understand the DOS and the expected completion bar without mistaking them for default downstream product scope.

## Release Discipline
- Update `CHANGELOG.md` when the DOS structure, review model, or collaboration workflow change materially.
- Create an annotated Git tag in the format `vX.Y.Z` after the release commit is finalized.
- Publish only after manual artifact-consistency review is complete.
