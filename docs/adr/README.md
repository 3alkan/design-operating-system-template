# ADRs

Architecture Decision Records (ADRs) capture significant technical and structural decisions.

## When ADRs Are Required
- New architectural pattern or major boundary change.
- Interface/contract changes across components.
- Cross-cutting policy changes (security, observability, versioning, error handling).
- Decisions with long-term consequences or notable tradeoffs.

## Naming Scheme
- Files: `NNNN-short-title.md` (zero-padded).
- Example: `0001-interface-versioning-policy.md`.

## Lifecycle
1. Proposed
2. Accepted
3. Superseded (link replacement ADR)
4. Rejected

## Authoring Rules
- Use `0000-template.md`.
- Include at least two alternatives.
- Record rejected options and reasoning.
- Add follow-ups/open questions when decision is partial.

