#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ALLOWED_STATUSES = {
    "template",
    "draft",
    "candidate",
    "accepted",
    "active",
    "deprecated",
    "superseded",
}

PLACEHOLDER_RE = re.compile(
    r"\[(PROJECT_NAME|PROJECT_DESCRIPTION|MAINTAINER_EMAIL|TBD|ASSUMPTION|OPEN QUESTION)\]"
)
ID_RE = re.compile(r"\b[A-Z]{2,4}-\d{3,4}\b")
TABLE_FIRST_CELL_RE = re.compile(r"^\|\s*`?([A-Z]{2,4}-\d{3,4})`?\s*\|")

CORE_REQUIRED_FILES = {
    "docs/00-system-purpose.md": [
        "Purpose",
        "Template Mission",
        "Usage Modes",
        "Design Principles",
        "Completion Standard",
        "Inputs",
        "Outputs",
        "Assumptions",
        "Open Questions",
        "Related IDs",
    ],
    "docs/01-product-scope.md": [
        "Purpose",
        "Problem Statement",
        "Actors",
        "Goals And Success Criteria",
        "Constraints",
        "Non-Goals",
        "Scope Notes",
        "Inputs",
        "Outputs",
        "Assumptions",
        "Open Questions",
        "Related IDs",
    ],
    "docs/02-domain-model.md": [
        "Purpose",
        "Domain Concepts",
        "Relationships",
        "Invariants",
        "Lifecycle Or State Notes",
        "Glossary",
        "Inputs",
        "Outputs",
        "Assumptions",
        "Open Questions",
        "Related IDs",
    ],
    "docs/03-scenarios.md": [
        "Purpose",
        "Scenario Catalog",
        "Scenario Template",
        "Runtime Notes",
        "Inputs",
        "Outputs",
        "Assumptions",
        "Open Questions",
        "Related IDs",
    ],
    "docs/04-capabilities.md": [
        "Purpose",
        "Capability Catalog",
        "Acceptance Criteria",
        "Release Or Dependency Notes",
        "Inputs",
        "Outputs",
        "Assumptions",
        "Open Questions",
        "Related IDs",
    ],
    "docs/05-contracts.md": [
        "Purpose",
        "Contract Catalog",
        "Contract Template",
        "Cross-Cutting Rules",
        "Inputs",
        "Outputs",
        "Assumptions",
        "Open Questions",
        "Related IDs",
    ],
    "docs/06-architecture.md": [
        "Purpose",
        "Architecture Goals",
        "Context And Boundaries",
        "Components",
        "Runtime Views",
        "Deployment Shape",
        "Cross-Cutting Concepts",
        "Risks",
        "Inputs",
        "Outputs",
        "Assumptions",
        "Open Questions",
        "Related IDs",
    ],
    "docs/07-quality.md": [
        "Purpose",
        "Definition Of Done",
        "Non-Functional Requirements",
        "Verification Strategy",
        "Review Checklist",
        "Inputs",
        "Outputs",
        "Assumptions",
        "Open Questions",
        "Related IDs",
    ],
    "docs/08-operations.md": [
        "Purpose",
        "Release Readiness",
        "Observability",
        "Rollback And Recovery",
        "Troubleshooting Skeleton",
        "Inputs",
        "Outputs",
        "Assumptions",
        "Open Questions",
        "Related IDs",
    ],
    "docs/09-traceability.md": [
        "Purpose",
        "Traceability Matrix",
        "Change Impact Notes",
        "Inputs",
        "Outputs",
        "Assumptions",
        "Open Questions",
        "Related IDs",
    ],
    "docs/10-authoring-conventions.md": [
        "Purpose",
        "Required Front Matter",
        "Required Section Names",
        "Artifact ID Scheme",
        "Status Values",
        "Placeholder Policy",
        "Traceability Rules",
        "Authoring Rules For Humans And LLMs",
        "Validation Contract",
        "Inputs",
        "Outputs",
        "Assumptions",
        "Open Questions",
        "Related IDs",
    ],
}

TEMPLATE_EXTRA_REQUIRED = [
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "docs/TEMPLATE_SETUP.md",
    "docs/MAINTAINER_PUBLISHING.md",
    "docs/adr/README.md",
    "docs/adr/0000-template.md",
    "docs/diagrams/README.md",
    "docs/patterns/README.md",
    "docs/patterns/01-sync-request-response.md",
    "docs/patterns/02-async-event-flow.md",
    "docs/patterns/03-external-integration-boundary.md",
    "docs/patterns/04-identity-and-authorization.md",
    "docs/patterns/05-retries-and-idempotency.md",
    "docs/patterns/06-observability-baseline.md",
    "docs/patterns/07-versioning-and-evolution.md",
    "docs/patterns/08-tenancy-and-isolation.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/feature.md",
    ".github/ISSUE_TEMPLATE/bug.md",
    ".github/ISSUE_TEMPLATE/adr-proposal.md",
    ".github/ISSUE_TEMPLATE/spike-research.md",
]

PATTERN_HEADINGS = [
    "Purpose",
    "When To Use",
    "Design Guidance",
    "Tradeoffs",
    "Artifact Updates",
    "Inputs",
    "Outputs",
    "Assumptions",
    "Open Questions",
    "Related IDs",
]

PATTERN_INDEX_HEADINGS = [
    "Purpose",
    "Pattern Set",
    "Inputs",
    "Outputs",
    "Assumptions",
    "Open Questions",
    "Related IDs",
]

ADR_GUIDE_HEADINGS = [
    "Purpose",
    "When ADRs Are Required",
    "Naming Scheme",
    "Lifecycle",
    "Authoring Rules",
    "Inputs",
    "Outputs",
    "Assumptions",
    "Open Questions",
    "Related IDs",
]

ADR_DOC_HEADINGS = [
    "Purpose",
    "Status",
    "Decision Summary",
    "Context",
    "Decision",
    "Alternatives Considered",
    "Rejected Options",
    "Consequences",
    "Follow-Ups",
    "Inputs",
    "Outputs",
    "Assumptions",
    "Open Questions",
    "Related IDs",
]

DIAGRAM_HEADINGS = [
    "Purpose",
    "Rules",
    "Recommended Usage",
    "Inputs",
    "Outputs",
    "Assumptions",
    "Open Questions",
    "Related IDs",
]

REQUIRED_FRONT_MATTER_KEYS = {
    "artifact_type",
    "artifact_id",
    "status",
    "owner",
    "related_ids",
    "assumptions",
    "open_questions",
}


def strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_front_matter(text: str, rel_path: str, errors: list[str]) -> tuple[dict[str, object], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        errors.append(f"{rel_path}: missing YAML front matter")
        return {}, text

    front_lines: list[str] = []
    closing_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing_index = index
            break
        front_lines.append(lines[index])

    if closing_index is None:
        errors.append(f"{rel_path}: unterminated YAML front matter")
        return {}, text

    data: dict[str, object] = {}
    current_list_key: str | None = None
    for line in front_lines:
        stripped = line.strip()
        if not stripped:
            continue
        if re.match(r"^[A-Za-z0-9_]+:\s*$", stripped):
            key = stripped[:-1]
            data[key] = []
            current_list_key = key
            continue
        if re.match(r"^[A-Za-z0-9_]+:\s+.+$", stripped):
            key, raw_value = stripped.split(":", 1)
            data[key] = strip_quotes(raw_value.strip())
            current_list_key = None
            continue
        if stripped.startswith("- ") and current_list_key:
            items = data.setdefault(current_list_key, [])
            if isinstance(items, list):
                items.append(strip_quotes(stripped[2:].strip()))
            continue
        errors.append(f"{rel_path}: unsupported front matter line `{line}`")

    body = "\n".join(lines[closing_index + 1 :])
    return data, body


def ensure_headings(text: str, rel_path: str, headings: list[str], errors: list[str]) -> None:
    for heading in headings:
        pattern = re.compile(rf"^##\s+{re.escape(heading)}\s*$", re.MULTILINE)
        if not pattern.search(text):
            errors.append(f"{rel_path}: missing heading `## {heading}`")


def collect_table_ids(body: str) -> set[str]:
    ids: set[str] = set()
    for line in body.splitlines():
        match = TABLE_FIRST_CELL_RE.match(line.strip())
        if match:
            ids.add(match.group(1))
    return ids


def validate_front_matter(
    rel_path: str,
    front_matter: dict[str, object],
    mode: str,
    errors: list[str],
) -> None:
    missing = REQUIRED_FRONT_MATTER_KEYS - set(front_matter)
    if missing:
        errors.append(f"{rel_path}: missing front matter keys {sorted(missing)}")

    status = front_matter.get("status")
    if isinstance(status, str) and status not in ALLOWED_STATUSES:
        errors.append(f"{rel_path}: invalid status `{status}`")
    if mode == "instance" and status == "template":
        errors.append(f"{rel_path}: instance content cannot keep status `template`")

    for list_key in ("related_ids", "assumptions", "open_questions"):
        value = front_matter.get(list_key)
        if not isinstance(value, list):
            errors.append(f"{rel_path}: `{list_key}` must be a list")


def validate_related_ids(
    docs: dict[str, dict[str, object]],
    declared_ids: set[str],
    errors: list[str],
) -> None:
    for rel_path, payload in docs.items():
        front_matter = payload["front_matter"]
        related_ids = front_matter.get("related_ids", [])
        if not isinstance(related_ids, list):
            continue
        for related_id in related_ids:
            if not isinstance(related_id, str):
                errors.append(f"{rel_path}: related id `{related_id}` is not a string")
                continue
            if related_id not in declared_ids:
                errors.append(f"{rel_path}: related id `{related_id}` does not resolve inside the instance")


def validate_traceability(root: Path, docs: dict[str, dict[str, object]], errors: list[str]) -> None:
    traceability_rel = "docs/09-traceability.md"
    traceability_payload = docs.get(traceability_rel)
    if not traceability_payload:
        return
    traceability_body = traceability_payload["body"]

    coverage_sources = {
        "docs/01-product-scope.md": {"GOAL"},
        "docs/03-scenarios.md": {"SCN"},
        "docs/04-capabilities.md": {"CAP"},
        "docs/05-contracts.md": {"CNT"},
        "docs/06-architecture.md": {"CMP"},
        "docs/07-quality.md": {"CHK", "NFR"},
    }
    for rel_path, prefixes in coverage_sources.items():
        payload = docs.get(rel_path)
        if not payload:
            continue
        for declared_id in payload["table_ids"]:
            prefix = declared_id.split("-", 1)[0]
            if prefix in prefixes and declared_id not in traceability_body:
                errors.append(
                    f"{traceability_rel}: missing traceability coverage for `{declared_id}`"
                )

    accepted_adrs = []
    adr_dir = root / "docs" / "adr"
    if adr_dir.exists():
        for path in sorted(adr_dir.glob("*.md")):
            if path.name in {"README.md", "0000-template.md"}:
                continue
            text = path.read_text(encoding="utf-8")
            local_errors: list[str] = []
            front_matter, _ = parse_front_matter(text, str(path), local_errors)
            if not local_errors and front_matter.get("status") == "accepted":
                accepted_adrs.append(str(front_matter.get("artifact_id")))
    for adr_id in accepted_adrs:
        if adr_id not in traceability_body:
            errors.append(f"{traceability_rel}: missing traceability coverage for `{adr_id}`")


def validate_adr_count(root: Path, errors: list[str]) -> None:
    adr_dir = root / "docs" / "adr"
    accepted = 0
    for path in sorted(adr_dir.glob("*.md")):
        if path.name in {"README.md", "0000-template.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        local_errors: list[str] = []
        front_matter, _ = parse_front_matter(text, str(path), local_errors)
        if not local_errors and front_matter.get("status") == "accepted":
            accepted += 1
    if accepted < 2:
        errors.append("docs/adr: instance mode requires at least two accepted ADRs")


def relative_string(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def get_validated_docs(root: Path, mode: str) -> tuple[dict[str, dict[str, object]], list[str]]:
    errors: list[str] = []
    docs: dict[str, dict[str, object]] = {}

    required_files = list(CORE_REQUIRED_FILES)
    if mode == "template":
        required_files.extend(TEMPLATE_EXTRA_REQUIRED)
    elif mode == "instance":
        required_files.append("README.md")

    for rel_path in required_files:
        if not (root / rel_path).exists():
            errors.append(f"{rel_path}: required file is missing")

    paths_to_validate: dict[str, list[str]] = dict(CORE_REQUIRED_FILES)
    if mode == "template":
        paths_to_validate["docs/adr/README.md"] = ADR_GUIDE_HEADINGS
        paths_to_validate["docs/adr/0000-template.md"] = ADR_DOC_HEADINGS
        paths_to_validate["docs/diagrams/README.md"] = DIAGRAM_HEADINGS
        paths_to_validate["docs/patterns/README.md"] = PATTERN_INDEX_HEADINGS
        for index in range(1, 9):
            paths_to_validate[f"docs/patterns/0{index}-{pattern_slug(index)}.md"] = PATTERN_HEADINGS

    for rel_path, headings in paths_to_validate.items():
        path = root / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        front_matter, body = parse_front_matter(text, rel_path, errors)
        validate_front_matter(rel_path, front_matter, mode, errors)
        ensure_headings(text, rel_path, headings, errors)
        docs[rel_path] = {
            "front_matter": front_matter,
            "body": body,
            "table_ids": collect_table_ids(body),
            "text": text,
        }

    if mode == "instance":
        adr_dir = root / "docs" / "adr"
        if adr_dir.exists():
            for path in sorted(adr_dir.glob("*.md")):
                rel_path = relative_string(path, root)
                text = path.read_text(encoding="utf-8")
                front_matter, body = parse_front_matter(text, rel_path, errors)
                validate_front_matter(rel_path, front_matter, mode, errors)
                ensure_headings(text, rel_path, ADR_DOC_HEADINGS, errors)
                docs[rel_path] = {
                    "front_matter": front_matter,
                    "body": body,
                    "table_ids": collect_table_ids(body),
                    "text": text,
                }

    return docs, errors


def pattern_slug(index: int) -> str:
    slugs = {
        1: "sync-request-response",
        2: "async-event-flow",
        3: "external-integration-boundary",
        4: "identity-and-authorization",
        5: "retries-and-idempotency",
        6: "observability-baseline",
        7: "versioning-and-evolution",
        8: "tenancy-and-isolation",
    }
    return slugs[index]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the design-system template or a completed instance.")
    parser.add_argument("--mode", choices=["template", "instance"], required=True)
    parser.add_argument("--root", required=True, help="Path to the repo root or completed instance root.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"error: root path does not exist: {root}", file=sys.stderr)
        return 1

    docs, errors = get_validated_docs(root, args.mode)

    artifact_ids: dict[str, str] = {}
    declared_ids: set[str] = set()
    for rel_path, payload in docs.items():
        front_matter = payload["front_matter"]
        artifact_id = front_matter.get("artifact_id")
        if isinstance(artifact_id, str):
            previous = artifact_ids.get(artifact_id)
            if previous and previous != rel_path:
                errors.append(f"{rel_path}: duplicate artifact_id `{artifact_id}` also used in {previous}")
            else:
                artifact_ids[artifact_id] = rel_path
            declared_ids.add(artifact_id)
        declared_ids.update(payload["table_ids"])

    if args.mode == "instance":
        validate_related_ids(docs, declared_ids, errors)
        validate_traceability(root, docs, errors)
        validate_adr_count(root, errors)

    for rel_path, payload in docs.items():
        if args.mode == "instance" and PLACEHOLDER_RE.search(payload["text"]):
            errors.append(f"{rel_path}: unresolved placeholder token found in instance mode")

    if errors:
        print("validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"validation passed for {args.mode} mode at {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
