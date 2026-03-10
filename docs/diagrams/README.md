---
artifact_type: diagram-policy
artifact_id: PAT-900
status: active
owner: "[MAINTAINER_EMAIL]"
related_ids:
  - CMP-001
  - SCN-001
assumptions:
  - "[ASSUMPTION] GitHub Markdown is the primary rendering environment."
open_questions:
  - "[OPEN QUESTION] Whether future versions should allow architecture context images generated from source."
---

# Diagram Policy

## Purpose
- Keep architecture and behavior visuals lightweight, portable, and easy for humans and LLMs to parse.

## Rules
- Mermaid-only diagrams.
- Diagrams must be embedded in Markdown fenced blocks using ` ```mermaid `.
- No committed PNG or SVG artifacts are required.
- Keep diagrams small and split by concern.
- Avoid decorative styling; optimize for readability and maintenance.

## Recommended Usage
- Use `flowchart` for context, boundaries, and component views.
- Use `sequenceDiagram` for scenarios and contract interactions.
- Use `stateDiagram-v2` for domain lifecycle or workflow state only when text is insufficient.

## Inputs
- Architecture, scenario, and domain artifacts.

## Outputs
- Portable diagrams that remain reviewable in GitHub and diff-friendly in version control.

## Assumptions
- Mermaid is sufficient for the intended level of design detail.

## Open Questions
- Whether future pattern docs should include diagram snippets by default.

## Related IDs
- `PAT-900`
- `CMP-001`
- `SCN-001`
