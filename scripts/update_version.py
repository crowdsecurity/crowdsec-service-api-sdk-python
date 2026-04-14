#!/usr/bin/env python3
"""Replace SDK version in pyproject.toml, OpenAPI JSON, and service files.

Usage: update_version.py <release_tag> <package_name> <openapi_file>

Normalizes the tag to PEP 440 (strips leading `v`, converts `-` to `.`) so
`v1.0.0-dev15` becomes `1.0.0.dev15`. Idempotent: re-running with the same
tag is a no-op.
"""
import json
import re
import sys
from pathlib import Path

PYPROJECT = Path("pyproject.toml")


def normalize(tag: str) -> str:
    return tag.lstrip("v").replace("-", ".")


def read_pyproject_version() -> str:
    m = re.search(r'(?m)^version\s*=\s*"([^"]+)"', PYPROJECT.read_text())
    if not m:
        raise SystemExit("Could not find version in pyproject.toml")
    return m.group(1)


def update_pyproject(new_version: str) -> None:
    text = PYPROJECT.read_text()
    text = re.sub(
        r'(?m)^version\s*=\s*"[^"]+"',
        f'version = "{new_version}"',
        text,
        count=1,
    )
    PYPROJECT.write_text(text)


def update_openapi(path: Path, new_version: str) -> None:
    text = path.read_text()
    spec = json.loads(text)
    spec.setdefault("info", {})["version"] = new_version
    pretty = "\n" in text.strip()
    result = json.dumps(spec, indent=2) if pretty else json.dumps(spec)
    path.write_text(result)


def update_service_files(package: str, old_version: str, new_version: str) -> None:
    services_dir = Path(package) / "services"
    if not services_dir.is_dir():
        return
    old = f'user_agent="{package}/{old_version}"'
    new = f'user_agent="{package}/{new_version}"'
    for py in services_dir.glob("*.py"):
        text = py.read_text()
        if old in text:
            py.write_text(text.replace(old, new))


def main() -> None:
    if len(sys.argv) != 4:
        raise SystemExit(
            "Usage: update_version.py <release_tag> <package_name> <openapi_file>"
        )
    release_tag, package, openapi_file = sys.argv[1:]
    new_version = normalize(release_tag)
    old_version = read_pyproject_version()
    print(f"Release tag: {release_tag}")
    print(f"Normalized version: {new_version}")
    print(f"Previous pyproject version: {old_version}")

    if old_version == new_version:
        print("Version already matches — nothing to do.")
        return

    update_pyproject(new_version)
    update_openapi(Path(openapi_file), new_version)
    update_service_files(package, old_version, new_version)

    print("---")
    print(f"pyproject.toml version: {read_pyproject_version()}")
    with open(openapi_file) as f:
        print(f"openapi version: {json.load(f)['info']['version']}")


if __name__ == "__main__":
    main()
