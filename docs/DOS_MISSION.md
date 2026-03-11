# DOS Mission

## What The DOS Is
- The Design Operating System (DOS) is a reusable system for producing product-design repositories.
- It is tech-stack-independent and implementation-agnostic at the technology level.
- It is implementation-ready at the design level: behavior, scope, contracts, boundaries, quality, and operations must be specified precisely enough that implementation is an execution task rather than invention of missing design.

## What This Repository Is
- This repository is the canonical source, packaging surface, and improvement space for the DOS itself.
- It is not the end product consumed by downstream builders.
- It owns the frozen DOS package under `dos/`, the publishing shell, the integrity manifest, the reference material, and the instantiation tooling.

## What The Product Is
- The actual product produced by the DOS is a project-specific instance repository.
- An instance repository is created from `dos/instance-seed/`.
- That instance becomes the working space where developers and LLMs collaborate to design and implement a specific product end to end.

## Product Standard For An Instance
- A completed instance must let a capable developer or LLM read the repository and understand:
  - what product is being built,
  - who it serves,
  - what is in scope and out of scope,
  - what the core scenarios and capabilities are,
  - what domain concepts and invariants must hold,
  - what contracts and architectural boundaries exist,
  - what quality and operational expectations must be met.
- A completed instance should be implementation-ready enough that a capable LLM can implement the product end to end in a chosen stack with minimal guessing.

## Default Lifecycle
- The default lifecycle stays in one repo.
- The instance starts in a design-first phase under `design/`.
- Product code begins after Gate 2 under `implementation/`.
- `design/` remains the source of truth while `implementation/` evolves.

## Collaboration Model
- Humans and LLMs use the same artifact spine as a shared working medium.
- Design artifacts are the contract.
- Structural changes must update the relevant artifacts and traceability.
- The DOS exists to make this collaboration predictable, inspectable, and repeatable.

## DOS Success Criteria
- The DOS succeeds when a team can use it to create an instance repository that is:
  - stack-independent,
  - design-complete enough for implementation,
  - understandable by humans,
  - and reliable enough for LLM continuation and end-to-end implementation.

## Boundary
- Root repo surfaces belong to the DOS.
- `dos/patterns/` and `dos/reference/` are DOS teaching assets.
- `dos/instance-seed/` is the packaged starting point for the actual product-design repository.
- After instantiation, the downstream instance root belongs to that project, not to the DOS repo.
