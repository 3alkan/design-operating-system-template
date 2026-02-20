# Maintainer Publishing Guide

## Mark Repository As GitHub Template
1. Open repository **Settings**.
2. In the general settings area, enable **Template repository**.
3. Save settings.

## Important Notes
- Template repositories cannot include Git LFS objects.
- Remove or migrate LFS-tracked files before enabling template use.

## How "Use this template" Works
- Users click **Use this template** to create a new repository from this structure.
- The new repository starts with unrelated history (not a fork of the template).
- This makes it suitable for clean project starts while reusing docs/process scaffolding.

## Pre-Publish Checklist
- [ ] `README.md` reflects template purpose and quick start.
- [ ] Community files exist (`LICENSE`, `CONTRIBUTING`, `CODE_OF_CONDUCT`, `SECURITY`).
- [ ] `.github/` issue and PR templates are current.
- [ ] Docs spine and ADR templates are consistent.
- [ ] Mermaid-only policy is clearly documented.
