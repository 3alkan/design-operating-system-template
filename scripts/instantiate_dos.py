#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DOS_ROOT = REPO_ROOT / "dos"
MANIFEST_PATH = DOS_ROOT / "dos-manifest.json"


TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".json",
    ".yml",
    ".yaml",
    ".gitignore",
}


def load_manifest() -> dict[str, object]:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def compute_package_hash() -> str:
    from build_dos_manifest import build_inventory, iter_package_files, package_hash

    return package_hash(build_inventory(iter_package_files()))


def target_is_non_empty(path: Path) -> bool:
    return path.exists() and any(path.iterdir())


def copy_instance_template(target: Path, force: bool) -> None:
    source = DOS_ROOT / "instance-template"
    target.mkdir(parents=True, exist_ok=True)
    for item in source.iterdir():
        destination = target / item.name
        if item.is_dir():
            shutil.copytree(item, destination, dirs_exist_ok=force)
        else:
            if destination.exists() and not force:
                raise FileExistsError(f"Target file already exists: {destination}")
            shutil.copy2(item, destination)


def should_replace(path: Path) -> bool:
    return path.suffix in TEXT_EXTENSIONS or path.name in {"AGENTS.md", "VERSION"}


def replace_placeholders(target: Path, replacements: dict[str, str]) -> None:
    for path in target.rglob("*"):
        if not path.is_file() or not should_replace(path):
            continue
        content = path.read_text(encoding="utf-8")
        updated = content
        for key, value in replacements.items():
            if value:
                updated = updated.replace(key, value)
        if updated != content:
            path.write_text(updated, encoding="utf-8")


def write_instance_metadata(
    target: Path,
    manifest: dict[str, object],
    instance_version: str,
    source_repo: str,
) -> None:
    metadata = {
        "instance_design_version": instance_version,
        "source_dos_version": manifest["dos_version"],
        "source_dos_release_tag": manifest["dos_release_tag"],
        "source_dos_package_hash": manifest["dos_package_hash"],
        "instantiated_at": datetime.now(timezone.utc).isoformat(),
        "source_dos_repo": source_repo,
        "notes": "",
    }
    (target / "INSTANCE_METADATA.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Materialize a downstream instance from the canonical DOS package.")
    parser.add_argument("--target", required=True, help="Path to the downstream instance root.")
    parser.add_argument("--instance-name", required=True, help="Value for [PROJECT_NAME].")
    parser.add_argument("--instance-version", required=True, help="Value for INSTANCE_DESIGN_VERSION.")
    parser.add_argument("--contact-email", default="", help="Value for [PROJECT_CONTACT_EMAIL].")
    parser.add_argument("--project-description", default="", help="Value for [PROJECT_DESCRIPTION].")
    parser.add_argument("--source-repo", default="", help="Source DOS repository identifier.")
    parser.add_argument("--force", action="store_true", help="Allow materialization into a non-empty target.")
    args = parser.parse_args()

    manifest = load_manifest()
    current_hash = compute_package_hash()
    if current_hash != manifest["dos_package_hash"]:
        raise SystemExit(
            f"Manifest hash mismatch. Expected {manifest['dos_package_hash']}, got {current_hash}. "
            "Rebuild dos/dos-manifest.json before instantiating."
        )

    target = Path(args.target).resolve()
    if target_is_non_empty(target) and not args.force:
        raise SystemExit("Target directory is not empty. Use --force to allow overwrite/merge.")

    copy_instance_template(target, args.force)
    replace_placeholders(
        target,
        {
            "[PROJECT_NAME]": args.instance_name,
            "[PROJECT_DESCRIPTION]": args.project_description,
            "[PROJECT_CONTACT_EMAIL]": args.contact_email,
            "INSTANCE_DESIGN_VERSION=X.X.X": f"INSTANCE_DESIGN_VERSION={args.instance_version}",
        },
    )
    write_instance_metadata(
        target,
        manifest,
        args.instance_version,
        args.source_repo or REPO_ROOT.as_posix(),
    )
    print(f"materialized downstream instance at {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
