# [PROJECT_NAME]

This repository is a downstream product-design instance materialized from the canonical Design Operating System package.

## What This Instance Owns
- The root of this repo belongs to the product design instance.
- `INSTANCE_METADATA.json` records which DOS release and package hash this instance came from.
- `VERSION` records the instance design version.
- `docs/` contains the instance artifact spine and is the design source of truth.

## First Steps
1. Replace `[PROJECT_NAME]`, `[PROJECT_DESCRIPTION]`, and `[PROJECT_CONTACT_EMAIL]`.
2. Set `INSTANCE_DESIGN_VERSION` in `VERSION`.
3. Fill `docs/00-system-purpose.md` through `docs/10-authoring-conventions.md`.
4. Add and accept at least two ADRs before implementation begins.
5. Reach Gate 2 before introducing product/application code.

## DOS Reference Boundary
- DOS teaching material is not copied into this repo by default.
- If you need patterns or the bundled example, consult the source DOS release recorded in `INSTANCE_METADATA.json`.
