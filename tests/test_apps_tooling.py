"""Pruebas de la cadena de aplicaciones (docs/APPS.md) que no necesitan compilar nada."""
from __future__ import annotations

import importlib.util
import json
import re
import sys
import tempfile
import unittest
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_apps as ba  # noqa: E402
import verify_apps as va  # noqa: E402

SPEC = importlib.util.spec_from_file_location("apps_desktop_main_test", ROOT / "apps" / "desktop" / "main.py")
DESKTOP = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DESKTOP)


def make_site(base: Path, classes: int = 3, cases: int = 2, terms: int = 2, body: int = 6000) -> Path:
    """Portal mínimo con la misma forma que site/."""
    site = base / "site"
    (site / "classes").mkdir(parents=True)
    (site / "assets").mkdir()
    (site / "index.html").write_text("<html></html>", encoding="utf-8")
    (site / "assets" / "catalog.json").write_text(json.dumps({"classes": []}), encoding="utf-8")
    for i in range(1, classes + 1):
        (site / "classes" / f"SE-{i:03d}.html").write_text("x" * body, encoding="utf-8")
    for kind in ("exito", "fallo"):
        (site / "casos" / kind).mkdir(parents=True)
    for i in range(cases):
        (site / "casos" / ("exito" if i % 2 else "fallo") / f"c{i}.html").write_text("x", encoding="utf-8")
    (site / "glosario" / "a").mkdir(parents=True)
    for i in range(terms):
        (site / "glosario" / "a" / f"t{i}.html").write_text("x", encoding="utf-8")
    return site


def expectation(classes: int = 3, cases: int = 2, terms: int = 2) -> dict:
    return {"classes": [f"SE-{i:03d}" for i in range(1, classes + 1)], "cases": cases, "glossary": terms}


def hashes_of(site: Path) -> dict[str, str]:
    return {p.relative_to(site).as_posix(): va.sha256_file(p) for p in sorted(site.rglob("*")) if p.is_file()}


class DesktopAppTests(unittest.TestCase):
    def test_inventory_and_digest_of_the_real_portal(self) -> None:
        counts = DESKTOP.inventory(ROOT / "site")
        self.assertEqual(612, counts["classes"])
        self.assertEqual("SE-001.html", counts["first_class"])
        self.assertEqual("SE-612.html", counts["last_class"])
        self.assertEqual(32, counts["case_total"])
        self.assertEqual(va.expected_counts()["glossary"], counts["glossary_terms"])

    def test_server_listens_only_on_loopback_and_serves_the_catalog(self) -> None:
        server = DESKTOP.start_server(ROOT / "site", 0)
        try:
            self.assertEqual("127.0.0.1", server.server_address[0])
            with urllib.request.urlopen(DESKTOP.base_url(server) + "assets/catalog.json", timeout=10) as reply:
                self.assertEqual(200, reply.status)
                self.assertIn("application/json", reply.headers["Content-Type"])
                self.assertEqual(612, len(json.loads(reply.read())["classes"]))
        finally:
            server.shutdown()

    def test_self_check_fails_on_an_empty_portal(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            empty = Path(tmp) / "site"
            empty.mkdir()
            out = Path(tmp) / "out.json"
            self.assertEqual(1, DESKTOP.self_check(empty, out))
            self.assertFalse(json.loads(out.read_text(encoding="utf-8"))["ok"])


class VerifierTests(unittest.TestCase):
    def test_complete_portal_passes_and_empty_or_partial_ones_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            site = make_site(Path(tmp))
            expect, hashes = expectation(), hashes_of(site)
            self.assertEqual([], va.check_tree(site, expect, hashes, exact=True))
            (site / "classes" / "SE-002.html").unlink()
            self.assertTrue(any("faltan 1 clases" in p for p in va.check_tree(site, expect, hashes, exact=True)))

    def test_hollow_classes_are_detected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            site = make_site(Path(tmp), body=40)
            problems = va.check_tree(site, expectation(), hashes_of(site), exact=True)
            self.assertTrue(any("vacías" in p for p in problems), problems)

    def test_modified_file_and_extra_file_are_detected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            site = make_site(Path(tmp))
            hashes = hashes_of(site)
            (site / "index.html").write_text("otro", encoding="utf-8")
            (site / "sobra.txt").write_text("x", encoding="utf-8")
            problems = " | ".join(va.check_tree(site, expectation(), hashes, exact=True))
            self.assertIn("distintos", problems)
            self.assertIn("de más", problems)

    def test_empty_apk_is_reported_as_empty(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            apk = Path(tmp) / "vacio.apk"
            with zipfile.ZipFile(apk, "w") as archive:
                archive.writestr("AndroidManifest.xml", "<manifest/>")
                archive.writestr("classes.dex", "dex")
            report = va.Report()
            va.verify_apk(apk, {"expect": expectation(), "hashes": {}, "digest": ""}, report)
            self.assertTrue(report.failed)
            self.assertTrue(any("APK vacío" in r["detail"] for r in report.rows))

    def test_checksum_file_must_list_every_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            dist = Path(tmp)
            (dist / "a.apk").write_bytes(b"a")
            (dist / "b.apk").write_bytes(b"b")
            sums = dist / "SHA256SUMS-android.txt"
            sums.write_text(f"{va.sha256_file(dist / 'a.apk')}  a.apk\n", encoding="utf-8")
            report = va.Report()
            va.verify_sums(sums, dist, "android", report)
            self.assertTrue(report.failed)
            self.assertIn("b.apk no está", report.rows[-1]["detail"])


class BuildConfigTests(unittest.TestCase):
    def test_version_is_semver_and_matches_the_android_project(self) -> None:
        version = ba.version()
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        package = json.loads((ROOT / "apps" / "android" / "package.json").read_text(encoding="utf-8"))
        self.assertEqual(version, package["version"])

    def test_asset_names_carry_platform_and_version(self) -> None:
        text = (ROOT / "scripts" / "build_apps.py").read_text(encoding="utf-8")
        for suffix in ("windows-x64.exe", "portable-windows-x64.zip", "setup-windows-x64", "windows-x64.msi", "android.apk"):
            self.assertIn(suffix, text)

    def test_workflow_pins_actions_to_a_commit_and_avoids_literal_tmp(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "apps.yml").read_text(encoding="utf-8")
        uses = re.findall(r"uses:\s*(\S+)", workflow)
        self.assertTrue(uses)
        for ref in uses:
            self.assertRegex(ref, r"@[0-9a-f]{40}$", ref)
        for path in (ROOT / "scripts" / "build_apps.py", ROOT / "scripts" / "verify_apps.py", ROOT / "apps" / "desktop" / "main.py"):
            self.assertNotIn("/tmp", path.read_text(encoding="utf-8"), path.name)

    def test_capacitor_app_is_offline_and_pinned(self) -> None:
        config = json.loads((ROOT / "apps" / "android" / "capacitor.config.json").read_text(encoding="utf-8"))
        self.assertEqual("www", config["webDir"])
        self.assertNotIn("url", config.get("server", {}))  # sin servidor remoto: el contenido va dentro del APK
        package = json.loads((ROOT / "apps" / "android" / "package.json").read_text(encoding="utf-8"))
        for versions in (package["dependencies"], package["devDependencies"]):
            for name, spec in versions.items():
                self.assertRegex(spec, r"^\d+\.\d+\.\d+$", name)
        self.assertTrue((ROOT / "apps" / "android" / "package-lock.json").is_file())


if __name__ == "__main__":
    unittest.main()
