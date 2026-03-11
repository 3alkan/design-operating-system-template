# [PROJECT_NAME]

This repository is a product-design instance.

A completed instance should let developers and LLMs collaborate to design a product end to end in a stack-independent but implementation-ready form.

## What This Instance Owns
- The root of this repo belongs to the product design instance.
- `INSTANCE_METADATA.json` records origin metadata for this instance.
- `VERSION` records the instance design version.
- `docs/` contains the instance artifact spine and is the design source of truth.

## First Steps
1. Replace `[PROJECT_NAME]`, `[PROJECT_DESCRIPTION]`, and `[PROJECT_CONTACT_EMAIL]`.
2. Set `INSTANCE_DESIGN_VERSION` in `VERSION`.
3. Fill `docs/00-system-purpose.md` through `docs/10-authoring-conventions.md`.
4. Add and accept at least two ADRs before implementation begins.
5. Reach Gate 2 before introducing product/application code.

## Completion Standard
- The completed repository should answer product, scope, scenarios, domain, capabilities, contracts, architecture, quality, and operations questions from the repo alone.
- The completed repository should be implementation-ready enough that a capable LLM can implement the product end to end in a chosen stack with minimal guessing.

## Repository Boundary
- This repo contains only instance-owned design artifacts and collaboration surfaces.
- External provenance details stay in `INSTANCE_METADATA.json`.
