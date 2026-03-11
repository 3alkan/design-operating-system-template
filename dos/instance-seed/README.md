# [PROJECT_NAME]

This repository is the product repository for one system. It starts in a design-first phase and continues into implementation in the same repo by default.

A completed instance should let developers and LLMs collaborate to design and then implement a product end to end in a stack-independent but implementation-ready form.

## What This Instance Owns
- The root of this repo belongs to the product design instance.
- `INSTANCE_METADATA.json` records origin metadata for this instance.
- `VERSION` records both the instance design version and the product version.
- `design/` contains the artifact spine and remains the design source of truth.
- `implementation/` is the default location for product code after Gate 2.
- `design/07-quality.md` is the governing implementation-readiness contract for this repo.

## First Steps
1. Replace `[PROJECT_NAME]`, `[PROJECT_DESCRIPTION]`, and `[PROJECT_CONTACT_EMAIL]`.
2. Set `INSTANCE_DESIGN_VERSION` in `VERSION`.
3. Set `PRODUCT_VERSION` if implementation planning or release tracking already exists.
4. Fill `design/00-system-purpose.md` through `design/10-authoring-conventions.md`.
5. Use `design/07-quality.md` to define and review the implementation-readiness bar.
6. Add and accept at least two ADRs before implementation begins.
7. Reach Gate 2 before introducing product/application code.

## Completion Standard
- The completed repository should answer product, scope, scenarios, domain, capabilities, contracts, architecture, quality, and operations questions from the repo alone.
- The completed repository should be implementation-ready enough that a capable LLM can implement the product end to end in a chosen stack with minimal guessing.
- Gate 2 means this repo is ready to begin implementation in `implementation/`, not only that design work is mostly done.

## Repository Boundary
- This repo contains only instance-owned design artifacts and collaboration surfaces.
- `design/` is the design-first phase of the repo.
- `implementation/` is where code begins after Gate 2 in the same repo.
- After Gate 2, `design/` remains authoritative for structure, behavior, contracts, and quality expectations while code evolves in `implementation/`.
- External provenance details stay in `INSTANCE_METADATA.json`.
