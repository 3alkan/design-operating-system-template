# Maintainer Publishing Guide

## Repository Settings
- Keep the repo positioned as the canonical DOS source, not as a GitHub template.
- If the repository was previously marked as a template, disable that setting before publishing the next release.
- Keep any repo description or About text aligned with the DOS package model.

## Pre-Publish Checklist
- [ ] `VERSION` has the correct `DOS_VERSION` for the release.
- [ ] `CHANGELOG.md` has a dated DOS release section for that version.
- [ ] `README.md` reflects the DOS package boundary and instantiation model.
- [ ] `AGENTS.md` and `dos/instance-seed/docs/10-authoring-conventions.md` are aligned.
- [ ] The frozen package under `dos/` is internally consistent.
- [ ] `dos/dos-manifest.json` matches the current `dos/` package and hash.
- [ ] The reference example is complete and still serves as DOS teaching material.
- [ ] The repo shell still reads coherently as the canonical DOS repo.
- [ ] `.github/` issue and PR forms reflect artifact IDs and traceability impact.
- [ ] Community files remain current.

## How DOS Publishing Should Feel
- A maintainer or downstream team should understand from `README.md` that this repo publishes a canonical DOS package.
- A newcomer should be able to follow `docs/INSTANCE_CREATION.md` without guessing what becomes a downstream instance.
- A developer or LLM should be able to inspect `dos/patterns/` and `dos/reference/` to understand the DOS and the expected completion bar without mistaking them for default downstream product scope.

## Release Discipline
- Update `CHANGELOG.md` when the DOS structure, review model, or collaboration workflow change materially.
- Regenerate `dos/dos-manifest.json` with `python scripts/build_dos_manifest.py` whenever the frozen `dos/` package changes.
- Create an annotated Git tag in the format `vX.Y.Z` after the release commit is finalized.
- Publish only after manual artifact-consistency review is complete.
