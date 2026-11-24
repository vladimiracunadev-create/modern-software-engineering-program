#!/usr/bin/env python3
"""Construye las aplicaciones de Windows y Android a partir del portal ``site/`` (docs/APPS.md).

Los binarios no entran en git: se generan en ``dist/`` (ignorado) y se publican como activos de
un GitHub Release. La versión canónica es ``apps/VERSION``.

Uso::

    python scripts/build_apps.py windows              # exe único + portable .zip
    python scripts/build_apps.py windows --installers # además Inno Setup (setup.exe) y WiX (.msi)
    python scripts/build_apps.py android-prepare      # copia site/ a apps/android/www
    python scripts/build_apps.py android-collect      # renombra el APK compilado con Gradle
    python scripts/build_apps.py linux | macos        # tar.gz y .deb / .zip y .dmg de la arquitectura del equipo
    python scripts/build_apps.py sums windows|android|linux|macos # SHA256SUMS-<plataforma>.txt
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
import platform
import shutil
import subprocess
import sys
import tarfile
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
        *(["--osx-bundle-identifier", "dev.vladimiracuna.ingenieriasoftware"] if sys.platform == "darwin" else []),
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


ABIS = ("arm64-v8a", "armeabi-v7a", "x86_64")
SPLITS_MARK = "// apks por ABI (scripts/build_apps.py)"


def android_configure() -> None:
    """Añade los ABI splits de Gradle al proyecto que genera ``npx cap add android``."""
    gradle = ANDROID / "android" / "app" / "build.gradle"
    text = gradle.read_text(encoding="utf-8")
    if SPLITS_MARK in text:
        return
    include = ", ".join(f'"{abi}"' for abi in ABIS)
    block = (f"    {SPLITS_MARK}\n    splits {{\n        abi {{\n            enable true\n            reset()\n"
             f"            include {include}\n            universalApk true\n        }}\n    }}\n")
    marker = "android {\n"
    if marker not in text:
        raise SystemExit("build.gradle no tiene un bloque android { ... }")
    gradle.write_text(text.replace(marker, marker + block, 1), encoding="utf-8", newline="\n")


def android_collect() -> list[Path]:
    """Copia el APK universal y, si Gradle los generó, los APK por ABI, con nombre versionado."""
    outputs = ANDROID / "android" / "app" / "build" / "outputs" / "apk" / "debug"
    DIST.mkdir(exist_ok=True)
    universal = next((p for p in (outputs / "app-universal-debug.apk", outputs / "app-debug.apk") if p.is_file()), None)
    if universal is None:
        raise SystemExit(f"no hay APK universal en {outputs}: ejecuta Gradle primero")
    produced = [DIST / f"{PREFIX}-{version()}-android.apk"]
    shutil.copyfile(universal, produced[0])
    for abi in ABIS:
        built = outputs / f"app-{abi}-debug.apk"
        if built.is_file():
            target = DIST / f"{PREFIX}-{version()}-android-{abi}.apk"
            shutil.copyfile(built, target)
            produced.append(target)
        else:
            print(f"aviso: Gradle no generó el APK de {abi}")
    return produced


def host_arch() -> str:
    machine = platform.machine().lower()
    return {"amd64": "x86_64", "x86_64": "x86_64", "arm64": "arm64", "aarch64": "aarch64"}.get(machine, machine)


def build_linux() -> list[Path]:
    """tar.gz y .deb del ejecutable de PyInstaller para la arquitectura del equipo (x86_64 o aarch64)."""
    if not (SITE / "index.html").is_file():
        raise SystemExit("falta site/index.html: no hay portal que empaquetar")
    v, arch = version(), host_arch()
    deb_arch = {"x86_64": "amd64", "aarch64": "arm64"}[arch]
    DIST.mkdir(exist_ok=True)
    icon = ICON_SOURCE
    pyinstaller(EXE_NAME, "--onedir", icon, WORK / "linux")
    app_dir = WORK / "linux" / EXE_NAME
    for extra in ("LICENSE", "LICENSE-CONTENT.md", "NOTICE"):
        if (ROOT / extra).is_file():
            shutil.copy2(ROOT / extra, app_dir / extra)
    tar_path = DIST / f"{PREFIX}-{v}-linux-{arch}.tar.gz"
    with tarfile.open(tar_path, "w:gz") as archive:
        archive.add(app_dir, arcname=EXE_NAME)

    stage = WORK / "deb"
    if stage.exists():
        shutil.rmtree(stage)
    opt = stage / "opt" / "ingenieria-software-moderna"
    shutil.copytree(app_dir, opt, symlinks=True)
    (stage / "usr" / "bin").mkdir(parents=True)
    (stage / "usr" / "bin" / "ingenieria-software-moderna").symlink_to("/opt/ingenieria-software-moderna/" + EXE_NAME)
    for rel in ("usr/share/applications", "usr/share/icons/hicolor/512x512/apps", "DEBIAN"):
        (stage / rel).mkdir(parents=True)
    from PIL import Image
    Image.open(ICON_SOURCE).convert("RGBA").resize((512, 512)).save(
        stage / "usr/share/icons/hicolor/512x512/apps/ingenieria-software-moderna.png")
    (stage / "usr/share/applications/ingenieria-software-moderna.desktop").write_text(
        "[Desktop Entry]\nType=Application\nName=Ingeniería de Software Moderna\n"
        "Comment=Programa de ingeniería de software, sin conexión\nExec=/usr/bin/ingenieria-software-moderna\n"
        "Icon=ingenieria-software-moderna\nCategories=Education;Development;\nTerminal=false\n", encoding="utf-8")
    size_kb = sum(p.stat().st_size for p in stage.rglob("*") if p.is_file()) // 1024
    (stage / "DEBIAN" / "control").write_text(
        f"Package: ingenieria-software-moderna\nVersion: {v}\nSection: education\nPriority: optional\n"
        f"Architecture: {deb_arch}\nInstalled-Size: {size_kb}\nMaintainer: Vladimir Acuña <noreply@users.noreply.github.com>\n"
        "Depends: libc6, zlib1g\nRecommends: python3-tk\n"
        "Homepage: https://github.com/vladimiracunadev-create/modern-software-engineering-program\n"
        "Description: Programa de Ingeniería de Software Moderna, sin conexión\n"
        " Sirve el portal (612 clases, 32 casos y glosario) en 127.0.0.1 y abre el navegador.\n", encoding="utf-8")
    deb_path = DIST / f"{PREFIX}-{v}-linux-{deb_arch}.deb"
    run(["dpkg-deb", "--root-owner-group", "--build", str(stage), str(deb_path)])
    produced = [tar_path, deb_path]
    for path in produced:
        if not path.is_file() or path.stat().st_size < 5_000_000:
            raise SystemExit(f"{path.name}: falta o es sospechosamente pequeño")
    return produced


def build_macos() -> list[Path]:
    """.app de PyInstaller empaquetado en .zip y .dmg para la arquitectura del equipo (arm64 o x86_64). Sin firma."""
    if not (SITE / "index.html").is_file():
        raise SystemExit("falta site/index.html: no hay portal que empaquetar")
    from PIL import Image

    v, arch = version(), host_arch()
    DIST.mkdir(exist_ok=True)
    WORK.mkdir(parents=True, exist_ok=True)
    icns = WORK / "app.icns"
    Image.open(ICON_SOURCE).convert("RGBA").save(icns)
    pyinstaller(EXE_NAME, "--onedir", icns, WORK / "macos")
    app = WORK / "macos" / f"{EXE_NAME}.app"
    if not app.is_dir():
        raise SystemExit(f"PyInstaller no generó {app}")
    zip_path = DIST / f"{PREFIX}-{v}-macos-{arch}.zip"
    run(["ditto", "-c", "-k", "--keepParent", str(app), str(zip_path)])
    stage = WORK / "dmg"
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True)
    run(["ditto", str(app), str(stage / app.name)])
    (stage / "Applications").symlink_to("/Applications")
    dmg_path = DIST / f"{PREFIX}-{v}-macos-{arch}.dmg"
    run(["hdiutil", "create", "-volname", "Ingenieria de Software Moderna", "-srcfolder", str(stage),
         "-ov", "-format", "UDZO", str(dmg_path)])
    produced = [zip_path, dmg_path]
    for path in produced:
        if not path.is_file() or path.stat().st_size < 5_000_000:
            raise SystemExit(f"{path.name}: falta o es sospechosamente pequeño")
    return produced


SUM_MARKERS = {"windows": "-windows-", "android": "-android", "linux": "-linux-", "macos": "-macos-"}
ARTIFACT_SUFFIXES = (".exe", ".zip", ".msi", ".apk", ".tar.gz", ".deb", ".dmg")


def write_sums(platform: str) -> Path:
    marker = SUM_MARKERS[platform]
    files = sorted((p for p in DIST.iterdir() if p.is_file() and marker in p.name and p.name.endswith(ARTIFACT_SUFFIXES)),
                   key=lambda p: p.name)
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
        if path.name.endswith(ARTIFACT_SUFFIXES) or path.name.startswith("SHA256SUMS-"):
            assets.append({"name": path.name, "bytes": path.stat().st_size, "sha256": sha256(path)})
    if not assets:
        raise SystemExit(f"no hay activos en {directory}")
    manifest = {"version": v, "tag": f"v{v}", "date": date, "commit": commit, "assets": assets}
    target = APP_DIR / "manifest.json"
    target.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return target


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = parser.add_subparsers(dest="command", required=True)
    win = sub.add_parser("windows")
    win.add_argument("--installers", action="store_true", help="también setup.exe (Inno Setup) y .msi (WiX)")
    sub.add_parser("android-prepare")
    sub.add_parser("android-configure")
    sub.add_parser("linux")
    sub.add_parser("macos")
    sub.add_parser("android-collect")
    sums = sub.add_parser("sums")
    sums.add_argument("platform", choices=sorted(SUM_MARKERS))
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
    elif args.command == "android-configure":
        android_configure()
    elif args.command == "android-collect":
        for path in android_collect():
            print(path)
    elif args.command in ("linux", "macos"):
        for path in (build_linux if args.command == "linux" else build_macos)():
            print(f"{path.name}  {path.stat().st_size} bytes")
    else:
        write_sums(args.platform)
    return 0


if __name__ == "__main__":
    sys.exit(main())
