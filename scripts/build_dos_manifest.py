#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DOS_ROOT = REPO_ROOT / "dos"
MANIFEST_PATH = DOS_ROOT / "dos-manifest.json"
HASHLIB_NAME = "sha3_256"
HASH_LABEL = "sha3-256"
FILE_HASH_FIELD = "sha3_256"


def read_dos_version() -> str:
    version_path = REPO_ROOT / "VERSION"
    for line in version_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("DOS_VERSION="):
            return line.split("=", 1)[1].strip()
    raise ValueError("DOS_VERSION not found in VERSION")


def iter_package_files() -> list[Path]:
    files: list[Path] = []
    for path in DOS_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path == MANIFEST_PATH:
            continue
        files.append(path)
    return sorted(files)


def hash_bytes(data: bytes) -> str:
    return hashlib.new(HASHLIB_NAME, data).hexdigest()


def build_inventory(files: list[Path]) -> list[dict[str, object]]:
    inventory: list[dict[str, object]] = []
    for path in files:
        content = path.read_bytes()
        inventory.append(
            {
                "path": path.relative_to(REPO_ROOT).as_posix(),
                FILE_HASH_FIELD: hash_bytes(content),
                "bytes": len(content),
            }
        )
    return inventory


def package_hash(inventory: list[dict[str, object]]) -> str:
    hasher = hashlib.new(HASHLIB_NAME)
    for item in inventory:
        hasher.update(str(item["path"]).encode("utf-8"))
        hasher.update(b"\0")
        hasher.update(str(item[FILE_HASH_FIELD]).encode("utf-8"))
        hasher.update(b"\0")
        hasher.update(str(item["bytes"]).encode("utf-8"))
        hasher.update(b"\0")
    return f"{HASH_LABEL}:{hasher.hexdigest()}"


def build_manifest(released_at: str | None, release_tag: str | None) -> dict[str, object]:
    dos_version = read_dos_version()
    files = iter_package_files()
    inventory = build_inventory(files)
    return {
        "manifest_version": 1,
        "dos_version": dos_version,
        "dos_release_tag": release_tag or f"v{dos_version}",
        "released_at": released_at or date.today().isoformat(),
        "hash_algorithm": HASH_LABEL,
        "instance_seed_root": "dos/instance-seed",
        "reference_root": "dos/reference",
        "copy_paths": ["dos/instance-seed"],
        "exclude_paths": [
            "dos/README.md",
            "dos/dos-manifest.json",
            "dos/patterns",
            "dos/reference",
        ],
        "file_inventory": inventory,
        "dos_package_hash": package_hash(inventory),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the canonical DOS manifest.")
    parser.add_argument("--released-at", help="Release date override in YYYY-MM-DD format.")
    parser.add_argument("--release-tag", help="Release tag override, defaults to v<DOS_VERSION>.")
    args = parser.parse_args()

    manifest = build_manifest(args.released_at, args.release_tag)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {MANIFEST_PATH.relative_to(REPO_ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
