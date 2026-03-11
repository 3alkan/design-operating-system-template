# Instance Creation Guide

Use this guide to create a downstream product-design repo from the canonical DOS package.

The DOS repo is the source and packaging surface for the system. The actual working product for users, developers, and LLMs is the instance repository created from it.

## Lifecycle Model
- Canonical DOS repo: this repository, which owns the frozen package under `dos/`.
- Frozen DOS package: the versioned package boundary defined by `dos/` and `dos/dos-manifest.json`.
- Downstream instance: a separate repo whose root is materialized from `dos/instance-seed/`.
- Implementation-ready instance: a downstream instance that satisfies Gate 2.

## What Gets Copied
- The contents of `dos/instance-seed/` are copied into the downstream repo root.
- `dos/reference/`, `dos/patterns/`, DOS publishing guides, and `dos/dos-manifest.json` are not copied by default.
- Downstream lineage is written into `INSTANCE_METADATA.json`.

## Lineage Metadata
- `INSTANCE_METADATA.json` records `source_dos_version`, `source_dos_release_tag`, and `source_dos_package_hash`.
- The same file records instance-owned values such as `instance_design_version` and `instantiated_at`.
- Treat this file as the downstream instance's provenance record, not as a replacement for the instance artifact spine.

## How To Materialize An Instance
1. Choose the DOS release you want to use.
2. Review `dos/dos-manifest.json`, `dos/patterns/`, and `dos/reference/` to understand the package quality bar.
3. Run `python scripts/instantiate_dos.py --target <path> --instance-name <name> --instance-version <x.y.z>`.
4. Open the generated downstream repo and replace remaining placeholders such as `[PROJECT_DESCRIPTION]` and `[PROJECT_CONTACT_EMAIL]`.
5. Fill the artifact spine in the materialized `docs/` directory.

Optional instantiation inputs:
- `--project-description` to prefill `[PROJECT_DESCRIPTION]`.
- `--contact-email` to prefill `[PROJECT_CONTACT_EMAIL]`.
- `--source-repo` to override the default source repository identifier in `INSTANCE_METADATA.json`.

## Downstream Instance Ownership
- After materialization, the downstream repo root belongs to the instance.
- The instance keeps its own `VERSION`, `INSTANCE_METADATA.json`, `README.md`, `AGENTS.md`, `.github/`, and `docs/`.
- The instance should not carry DOS publishing guides or DOS teaching material unless explicitly copied later.
- The instance is the actual product-design repository that should enable human and LLM collaboration toward implementation.

## Ready For Implementation Gate
- [ ] Core artifacts `01` through `09` contain project-specific content.
- [ ] Traceability links goals, scenarios, capabilities, contracts, components, checks, and ADRs.
- [ ] At least two ADRs are accepted.
- [ ] No critical placeholders remain.
- [ ] Manual artifact-consistency review passes.
