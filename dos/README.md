# DOS Package

This directory is the frozen canonical DOS package.

## Package Structure
- `instance-template/`: the only subtree that is materialized into a downstream repo root.
- `patterns/`: frozen DOS reference patterns for humans and LLMs.
- `reference/`: frozen DOS teaching material, including the bundled example instance and walkthroughs.
- `dos-manifest.json`: machine-readable DOS version, file inventory, and package hash.

## Package Rules
- Changes under `dos/` change the DOS package and must be reflected in `dos/dos-manifest.json`.
- Downstream repos should not copy `patterns/`, `reference/`, or DOS publishing docs by default.
- Instance lineage is recorded after materialization in the downstream `INSTANCE_METADATA.json`.
