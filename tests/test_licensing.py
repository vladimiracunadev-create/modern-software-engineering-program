from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_licensing", ROOT / "scripts" / "validate_licensing.py"
)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class LicensingContractTests(unittest.TestCase):
    def test_complete_licensing_contract(self) -> None:
        VALIDATOR.validate_files()
        VALIDATOR.validate_software_license()
        VALIDATOR.validate_content_scope()
        VALIDATOR.validate_public_contract()
        VALIDATOR.validate_history()
        VALIDATOR.validate_inventories()
        VALIDATOR.validate_workflow_contract()

    def test_notice_maps_both_original_material_licenses(self) -> None:
        notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
        self.assertIn("Apache License 2.0", notice)
        self.assertIn("CC BY-NC-SA 4.0", notice)
        self.assertIn("THIRD_PARTY_NOTICES.md", notice)


if __name__ == "__main__":
    unittest.main()

