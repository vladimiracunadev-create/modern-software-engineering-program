from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "LICENSE",
    "LICENSE-CONTENT.md",
    "NOTICE",
    "THIRD_PARTY_NOTICES.md",
    "ASSET_LICENSES.md",
    "DATA_LICENSES.md",
    "LICENSING_AUDIT.md",
    "TRADEMARKS.md",
    "docs/LICENSING_HISTORY.md",
)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def validate_files() -> None:
    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        raise AssertionError(f"Missing licensing documents: {missing}")


def validate_software_license() -> None:
    license_text = read("LICENSE")
    required = (
        "Apache License",
        "Version 2.0, January 2004",
        "TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION",
        "Copyright 2026 Vladimir Acuña",
    )
    missing = [token for token in required if token not in license_text]
    if missing:
        raise AssertionError(f"Apache-2.0 license text is incomplete: {missing}")


def validate_content_scope() -> None:
    content = read("LICENSE-CONTENT.md")
    required = (
        "CC BY-NC-SA 4.0",
        "código fuente, scripts, workflows",
        "datos sintéticos",
        "Atribución recomendada",
        "Contribuciones",
        "LICENSING_HISTORY.md",
    )
    missing = [token for token in required if token not in content]
    if missing:
        raise AssertionError(f"Content-license scope is incomplete: {missing}")


def validate_public_contract() -> None:
    readme = read("README.md")
    required = (
        "licencia-Apache--2.0",
        "contenido-CC_BY--NC--SA_4.0",
        "LICENSE-CONTENT.md",
        "THIRD_PARTY_NOTICES.md",
        "ASSET_LICENSES.md",
        "DATA_LICENSES.md",
        "LICENSING_AUDIT.md",
        "TRADEMARKS.md",
        "docs/LICENSING_HISTORY.md",
    )
    missing = [token for token in required if token not in readme]
    if missing:
        raise AssertionError(f"README licensing contract is incomplete: {missing}")
    if "Código, scripts, workflows, configuración y contenido original:" in readme:
        raise AssertionError("README still merges software and educational content under one license")


def validate_history() -> None:
    history = read("docs/LICENSING_HISTORY.md")
    required = (
        "b24578d03c4014148bf3e76948379383f0ffaae6",
        "No retroactividad",
        "git show <revision>:LICENSE",
        "MIT",
        "Apache-2.0",
        "CC BY-NC-SA 4.0",
    )
    missing = [token for token in required if token not in history]
    if missing:
        raise AssertionError(f"Licensing history is not reproducible: {missing}")


def validate_inventories() -> None:
    third_party = read("THIRD_PARTY_NOTICES.md")
    for token in ("actions/checkout", "Gitleaks 8.18.4", "Bandit 1.9.4", "SBOM"):
        if token not in third_party:
            raise AssertionError(f"Third-party inventory is missing: {token}")
    if "no existen PNG" not in read("ASSET_LICENSES.md"):
        raise AssertionError("Asset inventory must record the verified absence of binary assets")
    data = read("DATA_LICENSES.md")
    for token in ("curriculum.yaml", "lesson.json", "activity.yaml", "schemas/*.json"):
        if token not in data:
            raise AssertionError(f"Data inventory is missing: {token}")


def validate_workflow_contract() -> None:
    security = read(".github/workflows/security.yml")
    for token in (
        'cron: "0 11 * * 1"',
        "GITLEAKS_VERSION: \"8.18.4\"",
        "bandit==1.9.4",
        "python scripts/validate_licensing.py",
    ):
        if token not in security:
            raise AssertionError(f"Security workflow is missing: {token}")


def main() -> int:
    try:
        validate_files()
        validate_software_license()
        validate_content_scope()
        validate_public_contract()
        validate_history()
        validate_inventories()
        validate_workflow_contract()
    except (AssertionError, UnicodeDecodeError) as error:
        print(f"LICENSING_VALIDATION_FAILED: {error}", file=sys.stderr)
        return 1
    print("LICENSING_OK: Apache-2.0 software · CC BY-NC-SA 4.0 educational content")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

