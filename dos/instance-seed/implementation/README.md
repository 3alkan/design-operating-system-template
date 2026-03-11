# Implementation

This directory is the default home for product code after Gate 2.

## Purpose
- Keep implementation in the same repo as the design artifacts.
- Make the design-to-implementation lifecycle explicit from the start.
- Preserve `design/` as the source of truth while code evolves here.

## Default Conventions
- Application code: `implementation/src/`
- Tests: `implementation/tests/`
- Infrastructure or deployment code: `implementation/infra/`

## Guardrails
- Do not introduce product/application code here before Gate 2.
- Structural code changes here must update the relevant files in `design/`.
