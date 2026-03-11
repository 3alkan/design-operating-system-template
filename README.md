# Design Operating System

Tech-stack-independent Design Operating System (DOS) for producing product-design repositories that are abstractly implementation-ready.

Current DOS version: `0.7.0`

## What This Repo Owns
- The canonical DOS source.
- The frozen DOS package under `dos/`.
- DOS reference and teaching assets.
- DOS integrity and instantiation tooling.

This repository improves, documents, and packages the DOS. It is not the actual product-design repository that downstream builders work in.

## What The DOS Produces
- The actual product produced by the DOS is a project-specific instance repository.
- That instance is materialized from `dos/instance-seed/`.
- The instance is where developers and LLMs collaborate to design a product end to end.
- The target state is a stack-independent but implementation-ready design repo that a capable LLM can use to implement the product end to end with minimal guessing.

## DOS Model
- `dos/instance-seed/` is the copyable downstream design package.
- `dos/patterns/` contains frozen DOS pattern assets for humans and LLMs.
- `dos/reference/` contains frozen DOS teaching material, including the bundled example instance and walkthroughs.
- `dos/dos-manifest.json` is the machine-readable package manifest for versioning, file inventory, and integrity data.

The repo root belongs to the DOS itself. A downstream instance is created from `dos/instance-seed/` and owns its own root from the first moment of materialization.

## Mission
- The canonical DOS mission is defined in `docs/DOS_MISSION.md`.
- That mission governs how the DOS package, repo shell, instance seed, and reference material should evolve.

## How To Use The DOS
1. Read `docs/DOS_MISSION.md`.
2. Read `docs/INSTANCE_CREATION.md` to understand DOS repo vs instance.
3. Review `dos/README.md` to understand the frozen package boundary.
4. Inspect `dos/patterns/` and `dos/reference/` as teaching material, not as downstream product scope by default.
5. Regenerate `dos/dos-manifest.json` with `python scripts/build_dos_manifest.py` whenever the frozen package changes.
6. Materialize a downstream repo with `python scripts/instantiate_dos.py --target <path> --instance-name <name> --instance-version <x.y.z>`.
7. Fill the materialized instance root and reach Gate 2 before implementation begins.

## Repository Structure
- `dos/`
  - Canonical frozen DOS package.
- `docs/`
  - DOS repo shell guides for mission, instance creation, and DOS publishing.
- `scripts/`
  - DOS tooling for instantiation and manifest generation.
- `.github/`
  - Contribution surfaces for the canonical DOS repo.

## Version And Integrity
- Root `VERSION` contains only `DOS_VERSION`.
- `dos/dos-manifest.json` repeats DOS version metadata and records the `SHA3-256` package hash and file inventory for the frozen `dos/` package.
- `python scripts/build_dos_manifest.py` is the canonical way to refresh the manifest before release or instantiation.
- Downstream instances own their own `VERSION` and `INSTANCE_METADATA.json`.

## Review Model
- Review the repo shell when changing mission, DOS publishing, onboarding, or contributor workflow.
- Review `dos/instance-seed/` when changing the packaged downstream seed.
- Review `dos/patterns/` and `dos/reference/` when changing teaching/reference material.
- Review `dos/dos-manifest.json` whenever the frozen DOS package changes.

## Mermaid-Only Diagrams
- Diagrams must be embedded in Markdown fenced blocks using ` ```mermaid `.
- Keep diagrams small and split by concern.
- Allowed diagram types: `flowchart`, `sequenceDiagram`, `stateDiagram-v2`.

## License (Default)
- Default license: **GNU GPL v3.0** (`LICENSE`).
- Replace `LICENSE` if your downstream project needs a different license.

## Community Profile Checklist Hint
This repo includes common community health files used by GitHub community profile checks:
- `LICENSE`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- issue and PR forms in `.github/`
