#!/usr/bin/env python3
"""Abre los artefactos de Windows y Android y comprueba que llevan el programa dentro.

Que el build termine y que la suma SHA-256 cuadre no demuestra nada: un APK o un instalador
puede compilar, firmarse y salir **vacío**. Este verificador abre cada artefacto de ``dist/``,
lo extrae (o lo instala o lo ejecuta) y lo compara con el portal ``site/`` del repositorio:

* cada fichero de ``site/`` está dentro, con el mismo SHA-256 (nada falta, nada cambió);
* las 612 clases ``SE-001``–``SE-612`` (una por ``content/part-NN/SE-NNN.md``), cada una con
  contenido real (no una página vacía), los 32 casos y los 2.743 conceptos del glosario;
* los ejecutables de Windows, abiertos con ``--self-check``, informan lo mismo y la misma huella;
* el APK trae ``AndroidManifest.xml``, ``classes.dex`` y el portal en ``assets/public/``;
* ``SHA256SUMS-<plataforma>.txt`` coincide con los ficheros y no deja ninguno fuera.

Uso::

    python scripts/verify_apps.py --dir dist --require windows android [--report informe.json]

El .msi (``msiexec /a``) y el instalador (instalación silenciosa y desinstalación) solo se
abren en Windows; en otro sistema salen **OMITIDO**, nunca aprobados. Termina con código 1 si
algo falla o si falta un artefacto requerido.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import platform
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import zipfile
from pathlib import Path


def safe_extract_zip(archive: "zipfile.ZipFile", destination: Path) -> None:
    """Extrae un zip rechazando rutas absolutas o que salgan de ``destination`` (zip slip)."""
    root = destination.resolve()
    for member in archive.infolist():
        target = (root / member.filename).resolve()
        if root != target and root not in target.parents:
            raise ValueError(f"ruta insegura dentro del zip: {member.filename}")
    for member in archive.infolist():
        archive.extract(member, root)


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
MIN_CLASS_BYTES = 5_000  # una clase publicada pesa decenas de kB; una vacía, unos cientos
EXPECTED_CASES = 32

PASS, FAIL, SKIP = "OK", "FALLA", "OMITIDO"
SUM_MARKERS = {"windows": "-windows-", "android": "-android", "linux": "-linux-", "macos": "-macos-"}
ARTIFACT_SUFFIXES = (".exe", ".zip", ".msi", ".apk", ".tar.gz", ".deb", ".dmg")


def load_main():
    spec = importlib.util.spec_from_file_location("apps_desktop_main", ROOT / "apps" / "desktop" / "main.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def expected_counts() -> dict:
    """Lo que el repositorio dice que debe haber, leído de fuentes distintas del portal."""
    classes = sorted(p.stem for p in (ROOT / "content").glob("part-*/SE-*.md"))
    inventory = (ROOT / "glosario" / "INVENTARIO.md").read_text(encoding="utf-8")
    match = re.search(r"\*\*(\d[\d.]*) conceptos\*\*", inventory)
    return {
        "classes": classes,
        "cases": EXPECTED_CASES,
        "glossary": int(match.group(1).replace(".", "")) if match else 0,
    }


def site_hashes(ignore_dotfiles: bool = False) -> dict[str, str]:
    """SHA-256 de cada fichero de site/. Android no empaqueta ficheros que empiezan por punto (``.nojekyll``)."""
    return {p.relative_to(SITE).as_posix(): sha256_file(p) for p in sorted(SITE.rglob("*"))
            if p.is_file() and not (ignore_dotfiles and p.name.startswith("."))}


def find_site(base: Path) -> Path | None:
    """Carpeta que contiene ``classes/SE-001.html`` y ``index.html`` (portal dentro del artefacto)."""
    for hit in sorted(base.rglob("SE-001.html")):
        candidate = hit.parent.parent
        if hit.parent.name == "classes" and (candidate / "index.html").is_file():
            return candidate
    return None


def check_tree(site: Path, expect: dict, repo_hashes: dict[str, str], exact: bool) -> list[str]:
    """Devuelve la lista de problemas del portal encontrado en ``site``."""
    problems: list[str] = []
    ids = [f"{n}.html" for n in expect["classes"]]
    missing_classes = [i for i in ids if not (site / "classes" / i).is_file()]
    if missing_classes:
        problems.append(f"faltan {len(missing_classes)} clases (p. ej. {missing_classes[:3]})")
    thin = [i for i in ids if (site / "classes" / i).is_file() and (site / "classes" / i).stat().st_size < MIN_CLASS_BYTES]
    if thin:
        problems.append(f"{len(thin)} clases vacías o casi vacías (p. ej. {thin[:3]})")
    cases = [p for kind in ("exito", "fallo") for p in (site / "casos" / kind).glob("*.html") if p.name != "index.html"] \
        if (site / "casos").is_dir() else []
    if len(cases) != expect["cases"]:
        problems.append(f"{len(cases)} casos, se esperaban {expect['cases']}")
    terms = [p for p in (site / "glosario").rglob("*.html") if p.name != "index.html"] if (site / "glosario").is_dir() else []
    if len(terms) != expect["glossary"]:
        problems.append(f"{len(terms)} conceptos de glosario, se esperaban {expect['glossary']}")
    absent = changed = 0
    first_bad = None
    for rel, digest in repo_hashes.items():
        target = site / rel
        if not target.is_file():
            absent += 1
            first_bad = first_bad or rel
        elif sha256_file(target) != digest:
            changed += 1
            first_bad = first_bad or rel
    if absent or changed:
        problems.append(f"{absent} ficheros de site/ ausentes y {changed} distintos (p. ej. {first_bad})")
    if exact:
        extra = sum(1 for p in site.rglob("*") if p.is_file()) - len(repo_hashes)
        if extra:
            problems.append(f"{extra} ficheros de más respecto de site/")
    return problems


def self_check(exe: Path, expect_digest: str, workdir: Path) -> list[str]:
    out = workdir / (exe.stem + "-selfcheck.json")
    try:
        subprocess.run([str(exe), "--self-check", "--out", str(out)], check=False, timeout=600)
    except (OSError, subprocess.TimeoutExpired) as error:
        return [f"no se pudo ejecutar {exe.name}: {error}"]
    if not out.is_file():
        return [f"{exe.name} no escribió el informe de --self-check"]
    report = json.loads(out.read_text(encoding="utf-8"))
    problems = []
    if not report.get("ok"):
        problems.append(f"{exe.name}: --self-check informa ok=false")
    inv = report.get("inventory", {})
    if inv.get("classes") != 612 or inv.get("case_total") != EXPECTED_CASES:
        problems.append(f"{exe.name}: inventario interno {inv}")
    if report.get("tree_sha256") != expect_digest:
        problems.append(f"{exe.name}: la huella del portal empaquetado no coincide con site/")
    return problems


class Report:
    def __init__(self) -> None:
        self.rows: list[dict] = []
        if hasattr(sys.stdout, "reconfigure"):  # la consola de Windows usa cp1252 y no imprime ✓/✗
            sys.stdout.reconfigure(encoding="utf-8")

    def add(self, artifact: str, check: str, status: str, detail: str = "") -> None:
        self.rows.append({"artifact": artifact, "check": check, "status": status, "detail": detail})
        mark = {PASS: "✓", FAIL: "✗", SKIP: "·"}[status]
        print(f"  {mark} {check}: {status}{(' — ' + detail) if detail else ''}")

    @property
    def failed(self) -> bool:
        return any(r["status"] == FAIL for r in self.rows)


def verify_zip(path: Path, ctx: dict, report: Report) -> None:
    with tempfile.TemporaryDirectory(prefix="verify-zip-") as tmp:
        base = Path(tmp)
        with zipfile.ZipFile(path) as archive:
            bad = archive.testzip()
            if bad:
                report.add(path.name, "integridad del zip", FAIL, bad)
                return
            safe_extract_zip(archive, base)
        report.add(path.name, "integridad del zip", PASS)
        site = find_site(base)
        if not site:
            report.add(path.name, "portal dentro del zip", FAIL, "no hay site/classes/SE-001.html")
            return
        problems = check_tree(site, ctx["expect"], ctx["hashes"], exact=True)
        report.add(path.name, "612 clases, 32 casos, glosario y huella de site/", FAIL if problems else PASS, "; ".join(problems))
        exes = sorted(base.rglob("*.exe"))
        if sys.platform == "win32" and exes:
            problems = self_check(exes[0], ctx["digest"], base)
            report.add(path.name, "ejecutable abierto con --self-check", FAIL if problems else PASS, "; ".join(problems))
        else:
            report.add(path.name, "ejecutable abierto con --self-check", SKIP, "solo en Windows")


def verify_single_exe(path: Path, ctx: dict, report: Report) -> None:
    if sys.platform != "win32":
        report.add(path.name, "ejecutable abierto con --self-check", SKIP, "solo en Windows")
        return
    with tempfile.TemporaryDirectory(prefix="verify-exe-") as tmp:
        problems = self_check(path, ctx["digest"], Path(tmp))
    report.add(path.name, "ejecutable abierto con --self-check", FAIL if problems else PASS, "; ".join(problems))


def verify_msi(path: Path, ctx: dict, report: Report) -> None:
    if sys.platform != "win32":
        report.add(path.name, "contenido del MSI (msiexec /a)", SKIP, "solo en Windows")
        return
    with tempfile.TemporaryDirectory(prefix="verify-msi-") as tmp:
        target = Path(tmp) / "extraido"
        result = subprocess.run(["msiexec", "/a", str(path), "/qn", f"TARGETDIR={target}"], timeout=900)
        if result.returncode != 0:
            report.add(path.name, "contenido del MSI (msiexec /a)", FAIL, f"msiexec devolvió {result.returncode}")
            return
        site = find_site(target)
        if not site:
            report.add(path.name, "contenido del MSI (msiexec /a)", FAIL, "no hay site/classes/SE-001.html")
            return
        problems = check_tree(site, ctx["expect"], ctx["hashes"], exact=True)
        report.add(path.name, "contenido del MSI (msiexec /a)", FAIL if problems else PASS, "; ".join(problems))


def verify_setup(path: Path, ctx: dict, report: Report) -> None:
    if sys.platform != "win32":
        report.add(path.name, "instalación silenciosa", SKIP, "solo en Windows")
        return
    with tempfile.TemporaryDirectory(prefix="verify-setup-") as tmp:
        target = Path(tmp) / "instalado"
        result = subprocess.run(
            [str(path), "/VERYSILENT", "/SUPPRESSMSGBOXES", "/NORESTART", "/CURRENTUSER", "/NOICONS",
             "/TASKS=", f"/DIR={target}"], timeout=900)
        try:
            if result.returncode != 0:
                report.add(path.name, "instalación silenciosa", FAIL, f"el instalador devolvió {result.returncode}")
                return
            site = find_site(target)
            if not site:
                report.add(path.name, "instalación silenciosa", FAIL, "no hay site/classes/SE-001.html")
                return
            problems = check_tree(site, ctx["expect"], ctx["hashes"], exact=True)
            exes = sorted(target.glob("*.exe"))
            exes = [e for e in exes if not e.name.lower().startswith("unins")]
            if exes:
                problems += self_check(exes[0], ctx["digest"], Path(tmp))
            report.add(path.name, "instalación silenciosa, contenido y --self-check", FAIL if problems else PASS, "; ".join(problems))
        finally:
            uninstallers = sorted(target.glob("unins*.exe"))
            if uninstallers:
                subprocess.run([str(uninstallers[0]), "/VERYSILENT", "/SUPPRESSMSGBOXES", "/NORESTART"], timeout=600)


def verify_apk(path: Path, ctx: dict, report: Report) -> None:
    with tempfile.TemporaryDirectory(prefix="verify-apk-") as tmp:
        base = Path(tmp)
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
            missing = [n for n in ("AndroidManifest.xml", "classes.dex") if n not in names]
            report.add(path.name, "estructura del APK (manifiesto y classes.dex)", FAIL if missing else PASS,
                       f"faltan {missing}" if missing else "")
            public = [n for n in names if n.startswith("assets/public/") and not n.endswith("/")]
            for name in public:
                archive.extract(name, base)
        site = base / "assets" / "public"
        if not (site / "classes" / "SE-001.html").is_file():
            report.add(path.name, "portal dentro del APK", FAIL, "assets/public/classes/SE-001.html no existe (APK vacío)")
            return
        problems = check_tree(site, ctx["expect"], ctx["hashes_android"], exact=False)
        report.add(path.name, "612 clases, 32 casos, glosario y huella de site/", FAIL if problems else PASS, "; ".join(problems))


def host_arch() -> str:
    machine = platform.machine().lower()
    return {"amd64": "x86_64", "x86_64": "x86_64", "arm64": "arm64", "aarch64": "aarch64"}.get(machine, machine)


def find_binary(base: Path) -> Path | None:
    """Ejecutable de PyInstaller dentro de un árbol extraído (Linux o macOS)."""
    for candidate in sorted(base.rglob("Ingenieria-Software-Moderna")):
        if candidate.is_file():
            candidate.chmod(candidate.stat().st_mode | 0o111)
            return candidate
    return None


def arch_of(name: str) -> str | None:
    for arch in ("x86_64", "aarch64", "arm64", "amd64"):
        if re.search(rf"[-_]{arch}\b", name):
            return {"amd64": "x86_64"}.get(arch, arch)
    return None


def run_if_native(binary: Path | None, label: str, path: Path, ctx: dict, report: Report, workdir: Path) -> None:
    """Ejecuta --self-check solo si el binario es de la arquitectura del equipo."""
    wanted = arch_of(path.name)
    unify = {"arm64": "aarch64"}  # Linux llama aarch64 a lo que el .deb llama arm64
    same = (unify.get(wanted, wanted) == unify.get(host_arch(), host_arch())) if sys.platform == "linux" \
        else wanted == host_arch()
    if binary is None or not same:
        report.add(path.name, label, SKIP, f"el equipo es {sys.platform}/{host_arch()}, el artefacto es {wanted}")
        return
    problems = self_check(binary, ctx["digest"], workdir)
    report.add(path.name, label, FAIL if problems else PASS, "; ".join(problems))


def verify_tar(path: Path, ctx: dict, report: Report) -> None:
    with tempfile.TemporaryDirectory(prefix="verify-tar-") as tmp:
        base = Path(tmp)
        with tarfile.open(path) as archive:
            archive.extractall(base, filter="data")
        site = find_site(base)
        if not site:
            report.add(path.name, "portal dentro del tar.gz", FAIL, "no hay site/classes/SE-001.html")
            return
        problems = check_tree(site, ctx["expect"], ctx["hashes"], exact=True)
        report.add(path.name, "612 clases, 32 casos, glosario y huella de site/", FAIL if problems else PASS, "; ".join(problems))
        if sys.platform == "linux":
            run_if_native(find_binary(base), "ejecutable abierto con --self-check", path, ctx, report, base)
        else:
            report.add(path.name, "ejecutable abierto con --self-check", SKIP, "solo en Linux")


def verify_deb(path: Path, ctx: dict, report: Report) -> None:
    if sys.platform != "linux" or not shutil.which("dpkg-deb"):
        report.add(path.name, "contenido del .deb (dpkg-deb -x)", SKIP, "requiere Linux con dpkg-deb")
        return
    with tempfile.TemporaryDirectory(prefix="verify-deb-") as tmp:
        base = Path(tmp) / "extraido"
        base.mkdir()
        subprocess.run(["dpkg-deb", "-x", str(path), str(base)], check=True, timeout=600)
        arch = subprocess.run(["dpkg-deb", "-f", str(path), "Architecture"], check=True, capture_output=True,
                              text=True).stdout.strip()
        problems = [] if arch in path.name else [f"Architecture {arch} no coincide con el nombre"]
        site = find_site(base)
        if not site:
            report.add(path.name, "contenido del .deb (dpkg-deb -x)", FAIL, "no hay site/classes/SE-001.html")
            return
        problems += check_tree(site, ctx["expect"], ctx["hashes"], exact=True)
        report.add(path.name, "612 clases, 32 casos, glosario y huella de site/", FAIL if problems else PASS, "; ".join(problems))
        run_if_native(find_binary(base), "ejecutable abierto con --self-check", path, ctx, report, Path(tmp))


def verify_mac_zip(path: Path, ctx: dict, report: Report) -> None:
    with tempfile.TemporaryDirectory(prefix="verify-maczip-") as tmp:
        base = Path(tmp)
        with zipfile.ZipFile(path) as archive:
            bad = archive.testzip()
            if bad:
                report.add(path.name, "integridad del zip", FAIL, bad)
                return
            safe_extract_zip(archive, base)
        site = find_site(base)
        if not site:
            report.add(path.name, "portal dentro del .app", FAIL, "no hay site/classes/SE-001.html")
            return
        problems = check_tree(site, ctx["expect"], ctx["hashes"], exact=False)
        report.add(path.name, "612 clases, 32 casos, glosario y huella de site/", FAIL if problems else PASS, "; ".join(problems))
        report.add(path.name, "ejecutable abierto con --self-check", SKIP,
                   "se abre en el .dmg del mismo runner (zipfile pierde los enlaces del .app)")


def verify_dmg(path: Path, ctx: dict, report: Report) -> None:
    if sys.platform != "darwin":
        report.add(path.name, "contenido del .dmg (hdiutil attach)", SKIP, "solo en macOS")
        return
    with tempfile.TemporaryDirectory(prefix="verify-dmg-") as tmp:
        mount = Path(tmp) / "montaje"
        mount.mkdir()
        subprocess.run(["hdiutil", "attach", str(path), "-nobrowse", "-readonly", "-mountpoint", str(mount)],
                       check=True, timeout=600, capture_output=True)
        try:
            site = find_site(mount)
            if not site:
                report.add(path.name, "contenido del .dmg (hdiutil attach)", FAIL, "no hay site/classes/SE-001.html")
                return
            problems = check_tree(site, ctx["expect"], ctx["hashes"], exact=False)
            report.add(path.name, "612 clases, 32 casos, glosario y huella de site/", FAIL if problems else PASS, "; ".join(problems))
            copy = Path(tmp) / "copia"
            shutil.copytree(mount, copy, symlinks=True, ignore=shutil.ignore_patterns("Applications"))
            run_if_native(find_binary(copy), "ejecutable abierto con --self-check", path, ctx, report, Path(tmp))
        finally:
            subprocess.run(["hdiutil", "detach", str(mount), "-force"], check=False, capture_output=True)


def verify_sums(sums: Path, dist: Path, platform: str, report: Report) -> None:
    marker = SUM_MARKERS[platform]
    listed: dict[str, str] = {}
    for line in sums.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (\S.*)", line)
        if not match:
            report.add(sums.name, "formato de línea", FAIL, line)
            return
        listed[match.group(2)] = match.group(1)
    problems = []
    for name, digest in listed.items():
        target = dist / name
        if not target.is_file():
            problems.append(f"{name} no existe")
        elif sha256_file(target) != digest:
            problems.append(f"{name}: la suma no coincide")
    present = {p.name for p in dist.iterdir() if marker in p.name and p.name.endswith(ARTIFACT_SUFFIXES)}
    problems += [f"{n} no está en {sums.name}" for n in sorted(present - set(listed))]
    report.add(sums.name, "sumas SHA-256 frente a los ficheros", FAIL if problems else PASS, "; ".join(problems))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Abre y cuenta el contenido de los artefactos de Windows y Android.")
    parser.add_argument("--dir", type=Path, default=ROOT / "dist")
    parser.add_argument("--require", nargs="*", choices=sorted(SUM_MARKERS), default=[],
                        help="plataformas cuyos artefactos deben existir")
    parser.add_argument("--report", type=Path, help="escribe el informe JSON aquí")
    args = parser.parse_args(argv)
    dist: Path = args.dir
    if not (SITE / "index.html").is_file():
        print("falta site/index.html")
        return 1
    main_module = load_main()
    digest, _ = main_module.tree_digest(SITE)
    ctx = {"expect": expected_counts(), "hashes": site_hashes(),
           "hashes_android": site_hashes(ignore_dotfiles=True), "digest": digest}
    report = Report()
    if len(ctx["expect"]["classes"]) != 612:
        report.add("repositorio", "clases en content/", FAIL, f"{len(ctx['expect']['classes'])}, se esperaban 612")
    print(f"Portal de referencia: {len(ctx['expect']['classes'])} clases, {ctx['expect']['cases']} casos, "
          f"{ctx['expect']['glossary']} conceptos, huella {digest[:16]}…")

    files = sorted(dist.iterdir()) if dist.is_dir() else []
    groups = {name: [f for f in files if marker in f.name and f.name.endswith(ARTIFACT_SUFFIXES)]
              for name, marker in SUM_MARKERS.items()}
    for platform in args.require:
        if not groups[platform]:
            report.add(platform, "artefactos requeridos", FAIL, f"no hay ninguno en {dist}")
    for platform, items in groups.items():
        if not items:
            continue
        print(f"\n[{platform}]")
        sums = dist / f"SHA256SUMS-{platform}.txt"
        if sums.is_file():
            verify_sums(sums, dist, platform, report)
        else:
            report.add(sums.name, "existe", FAIL, "falta el fichero de sumas")
        for item in items:
            print(f"\n{item.name}  ({item.stat().st_size / 1e6:.1f} MB)")
            if item.name.endswith(".tar.gz"):
                verify_tar(item, ctx, report)
            elif item.suffix == ".deb":
                verify_deb(item, ctx, report)
            elif item.suffix == ".dmg":
                verify_dmg(item, ctx, report)
            elif item.suffix == ".zip" and "-macos-" in item.name:
                verify_mac_zip(item, ctx, report)
            elif item.suffix == ".zip":
                verify_zip(item, ctx, report)
            elif item.suffix == ".msi":
                verify_msi(item, ctx, report)
            elif item.suffix == ".apk":
                verify_apk(item, ctx, report)
            elif "-setup-" in item.name:
                verify_setup(item, ctx, report)
            else:
                verify_single_exe(item, ctx, report)
    if args.report:
        args.report.write_text(json.dumps(report.rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    skipped = sum(r["status"] == SKIP for r in report.rows)
    print(f"\n{'VERIFICACIÓN FALLIDA' if report.failed else 'Verificación aprobada'}: "
          f"{sum(r['status'] == PASS for r in report.rows)} comprobaciones OK, "
          f"{sum(r['status'] == FAIL for r in report.rows)} fallan, {skipped} omitidas.")
    return 1 if report.failed else 0


if __name__ == "__main__":
    sys.exit(main())
