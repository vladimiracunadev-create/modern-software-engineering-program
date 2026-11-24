#!/usr/bin/env python3
"""Construye las aplicaciones de Windows y Android a partir del portal ``site/`` (docs/APPS.md).

Los binarios no entran en git: se generan en ``dist/`` (ignorado) y se publican como activos de
un GitHub Release. La versión canónica es ``apps/VERSION``.

Uso::

    python scripts/build_apps.py windows              # exe único + portable .zip
    python scripts/build_apps.py windows --installers # además Inno Setup (setup.exe) y WiX (.msi)
    python scripts/build_apps.py android-prepare      # copia site/ a apps/android/www
    python scripts/build_apps.py android-collect      # renombra el APK compilado con Gradle
    python scripts/build_apps.py sums windows|android # SHA256SUMS-<plataforma>.txt
    python scripts/build_apps.py manifest --dir D --commit C --date YYYY-MM-DD  # apps/manifest.json

``windows`` necesita Python con ``pyinstaller`` y ``pillow``; los instaladores, Inno Setup 6 y
``wix``. Cada paso termina con código distinto de 0 si no produce el fichero esperado. Abrir el
resultado y contar su contenido es trabajo de ``scripts/verify_apps.py``.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
DIST = ROOT / "dist"
WORK = ROOT / "build" / "apps"
APP_DIR = ROOT / "apps"
ANDROID = APP_DIR / "android"
PREFIX = "Ingenieria-Software-Moderna"
EXE_NAME = "Ingenieria-Software-Moderna"
PORTABLE_NAME = EXE_NAME + "-portable"
ICON_SOURCE = ANDROID / "resources" / "icon.png"
ISCC_CANDIDATES = (
    r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe",
    r"C:\Program Files\Inno Setup 6\ISCC.exe",
)


def version() -> str:
    return (APP_DIR / "VERSION").read_text(encoding="utf-8").strip()


def run(cmd: list[str], **kwargs) -> None:
    print("+", " ".join(str(c) for c in cmd), flush=True)
    subprocess.run(cmd, check=True, **kwargs)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def make_icon() -> Path:
    from PIL import Image

    WORK.mkdir(parents=True, exist_ok=True)
    target = WORK / "app.ico"
    Image.open(ICON_SOURCE).convert("RGBA").save(
        target, sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    )
    return target


def render(template: Path, target: Path, values: dict[str, str]) -> None:
    text = template.read_text(encoding="utf-8")
    for key, value in values.items():
        text = text.replace(f"@{key}@", value)
    target.write_text(text, encoding="utf-8-sig")  # Inno y WiX leen UTF-8 con BOM sin ambigüedad


def pyinstaller(name: str, mode: str, icon: Path, distpath: Path) -> None:
    run([
        sys.executable, "-m", "PyInstaller", "--noconfirm", mode, "--windowed",
        "--icon", str(icon), "--name", name,
        "--distpath", str(distpath), "--workpath", str(WORK / ("pyi-" + name)),
        "--specpath", str(WORK),
        "--add-data", f"{SITE}{os.pathsep}site",
        "--add-data", f"{APP_DIR / 'VERSION'}{os.pathsep}.",
        str(APP_DIR / "desktop" / "main.py"),
    ])


def build_windows(installers: bool) -> list[Path]:
    if not (SITE / "index.html").is_file():
        raise SystemExit("falta site/index.html: no hay portal que empaquetar")
    v = version()
    DIST.mkdir(exist_ok=True)
    icon = make_icon()
    produced: list[Path] = []

    # 1) ejecutable único: un solo fichero, arranque más lento (se descomprime en %TEMP%)
    pyinstaller(EXE_NAME, "--onefile", icon, WORK / "onefile")
    single = DIST / f"{PREFIX}-{v}-windows-x64.exe"
    shutil.copyfile(WORK / "onefile" / f"{EXE_NAME}.exe", single)
    produced.append(single)

    # 2) carpeta portable: arranque rápido; también es la base del setup y del MSI
    portable_dist = WORK / "portable"
    pyinstaller(PORTABLE_NAME, "--onedir", icon, portable_dist)
    app_dir = portable_dist / PORTABLE_NAME
    for extra in ("LICENSE", "LICENSE-CONTENT.md", "NOTICE", "README.md"):
        if (ROOT / extra).is_file():
            shutil.copy2(ROOT / extra, app_dir / extra)
    zip_path = DIST / f"{PREFIX}-{v}-portable-windows-x64.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path in sorted(p for p in app_dir.rglob("*") if p.is_file()):
            archive.write(path, f"{PORTABLE_NAME}/{path.relative_to(app_dir).as_posix()}")
    produced.append(zip_path)

    if installers:
        values = {"VERSION": v, "ICON": str(icon), "APPDIR": str(app_dir), "EXE": f"{PORTABLE_NAME}.exe"}
        iscc = next((c for c in ISCC_CANDIDATES if Path(c).is_file()), shutil.which("ISCC"))
        if not iscc:
            raise SystemExit("falta Inno Setup 6 (ISCC.exe)")
        iss = WORK / "installer.iss"
        render(APP_DIR / "desktop" / "installer.iss.in", iss, {
            **values, "OUTDIR": str(DIST), "OUTNAME": f"{PREFIX}-{v}-setup-windows-x64"})
        run([iscc, str(iss)])
        produced.append(DIST / f"{PREFIX}-{v}-setup-windows-x64.exe")

        wxs = WORK / "package.wxs"
        render(APP_DIR / "desktop" / "package.wxs.in", wxs, values)
        msi = DIST / f"{PREFIX}-{v}-windows-x64.msi"
        run(["wix", "build", str(wxs), "-arch", "x64", "-out", str(msi)])
        produced.append(msi)

    for path in produced:
        if not path.is_file() or path.stat().st_size < 5_000_000:
            raise SystemExit(f"{path.name}: falta o es sospechosamente pequeño")
    return produced


def android_prepare() -> int:
    if not (SITE / "index.html").is_file():
        raise SystemExit("falta site/index.html: no hay portal que empaquetar")
    www = ANDROID / "www"
    if www.exists():
        shutil.rmtree(www)
    # .nojekyll solo sirve a GitHub Pages, y Android descarta de todos modos los ficheros que empiezan por punto
    shutil.copytree(SITE, www, ignore=shutil.ignore_patterns(".*"))
    count = sum(1 for p in www.rglob("*") if p.is_file())
    print(f"apps/android/www: {count} ficheros")
    return count


def android_collect() -> Path:
    built = ANDROID / "android" / "app" / "build" / "outputs" / "apk" / "debug" / "app-debug.apk"
    if not built.is_file():
        raise SystemExit(f"no existe {built}: ejecuta Gradle primero")
    DIST.mkdir(exist_ok=True)
    target = DIST / f"{PREFIX}-{version()}-android.apk"
    shutil.copyfile(built, target)
    return target


def write_sums(platform: str) -> Path:
    patterns = {"windows": ("*.exe", "*.zip", "*.msi"), "android": ("*.apk",)}[platform]
    files = sorted({p for pattern in patterns for p in DIST.glob(pattern)}, key=lambda p: p.name)
    if not files:
        raise SystemExit(f"no hay artefactos de {platform} en {DIST}")
    target = DIST / f"SHA256SUMS-{platform}.txt"
    target.write_text("".join(f"{sha256(p)}  {p.name}\n" for p in files), encoding="utf-8", newline="\n")
    print(target.read_text(encoding="utf-8"), end="")
    return target


def write_manifest(directory: Path, commit: str, date: str) -> Path:
    """Registra en git (sin binarios) qué activos tiene el release: nombre, tamaño y SHA-256."""
    v = version()
    assets = []
    for path in sorted(directory.iterdir(), key=lambda p: p.name):
        if path.suffix in (".exe", ".zip", ".msi", ".apk") or path.name.startswith("SHA256SUMS-"):
            assets.append({"name": path.name, "bytes": path.stat().st_size, "sha256": sha256(path)})
    if not assets:
        raise SystemExit(f"no hay activos en {directory}")
    manifest = {"version": v, "tag": f"v{v}", "date": date, "commit": commit, "assets": assets}
    target = APP_DIR / "manifest.json"
    target.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "
", encoding="utf-8", newline="
")
    return target


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = parser.add_subparsers(dest="command", required=True)
    win = sub.add_parser("windows")
    win.add_argument("--installers", action="store_true", help="también setup.exe (Inno Setup) y .msi (WiX)")
    sub.add_parser("android-prepare")
    sub.add_parser("android-collect")
    sums = sub.add_parser("sums")
    sums.add_argument("platform", choices=["windows", "android"])
    man = sub.add_parser("manifest")
    man.add_argument("--dir", type=Path, default=DIST)
    man.add_argument("--commit", required=True)
    man.add_argument("--date", required=True)
    args = parser.parse_args(argv)
    if args.command == "manifest":
        print(write_manifest(args.dir, args.commit, args.date))
    elif args.command == "windows":
        for path in build_windows(args.installers):
            print(f"{path.name}  {path.stat().st_size} bytes")
    elif args.command == "android-prepare":
        android_prepare()
    elif args.command == "android-collect":
        print(android_collect())
    else:
        write_sums(args.platform)
    return 0


if __name__ == "__main__":
    sys.exit(main())
