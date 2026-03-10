# Maintainer Publishing Guide

## Mark Repository As GitHub Template
1. Open repository **Settings**.
2. In the general settings area, enable **Template repository**.
3. Save settings.

## Important Notes
- Template repositories cannot include Git LFS objects.
- Remove or migrate LFS-tracked files before enabling template use.

## Pre-Publish Checklist
- [ ] `README.md` reflects the design-system promise and validation commands.
- [ ] `AGENTS.md` and `docs/10-authoring-conventions.md` are aligned.
- [ ] The artifact spine and pattern library are internally consistent.
- [ ] The reference example is complete and passes instance validation.
- [ ] The root template passes template validation.
- [ ] `.github/` issue and PR templates reflect artifact IDs and traceability impact.
- [ ] Community files remain current.

## How "Use This Template" Should Feel
- A maintainer or downstream team should understand the repo purpose from `README.md`.
- A newcomer should be able to follow `docs/TEMPLATE_SETUP.md` without guessing artifact order.
- A developer or LLM should be able to inspect `examples/reference-product/` to see the expected completion bar.

## Release Discipline
- Update `CHANGELOG.md` when the template structure, validation rules, or collaboration workflow change materially.
- Publish only after both validator modes succeed from a clean checkout.
