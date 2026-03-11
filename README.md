# Design Operating System

Tech-stack-independent Design Operating System (DOS) for defining products end to end in a form that is abstractly implementation-ready.

Current DOS version: `0.6.0`

## What This Repository Is
- The canonical DOS repository, not a downstream product-design repo.
- A publishing shell for a frozen DOS package under `dos/`.
- A shared medium for architects, developers, and LLMs to maintain the canonical package and materialize downstream design instances.

## DOS Model
- `dos/instance-seed/` is the copyable downstream design package.
- `dos/patterns/` contains frozen DOS pattern assets for humans and LLMs.
- `dos/reference/` contains frozen DOS teaching material, including the bundled example instance and walkthroughs.
- `dos/dos-manifest.json` is the machine-readable package manifest for versioning, file inventory, and integrity data.

The repo root belongs to the DOS itself. A downstream instance is created from `dos/instance-seed/` and owns its own root from the first moment of materialization.

## How To Use The DOS
1. Read `docs/INSTANCE_CREATION.md` to understand canonical DOS repo vs downstream instance.
2. Review `dos/README.md` to understand the frozen package boundary.
3. Inspect `dos/patterns/` and `dos/reference/` as teaching material, not as downstream product scope by default.
4. Regenerate `dos/dos-manifest.json` with `python scripts/build_dos_manifest.py` whenever the frozen package changes.
5. Materialize a downstream repo with `python scripts/instantiate_dos.py --target <path> --instance-name <name> --instance-version <x.y.z>`.
6. Fill the materialized instance root and reach Gate 2 before implementation begins.

## Repository Structure
- `dos/`
  - Canonical frozen DOS package.
- `docs/`
  - DOS repo shell guides for instance creation and DOS publishing.
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
- Review the repo shell when changing DOS publishing, onboarding, or contributor workflow.
- Review `dos/instance-seed/` when changing the downstream instance contract.
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
