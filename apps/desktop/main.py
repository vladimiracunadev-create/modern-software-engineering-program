#!/usr/bin/env python3
"""Aplicación de escritorio: el portal del programa, sin conexión.

Sirve la carpeta ``site/`` (empaquetada dentro del ejecutable o, en un checkout, la del
repositorio) desde un servidor **solo de loopback** (127.0.0.1) y abre el navegador
predeterminado. No usa ningún servicio externo: el portal necesita HTTP porque su índice
carga ``assets/catalog.json`` con ``fetch``, y eso no funciona desde ``file://``.

Uso::

    python apps/desktop/main.py                    # ventana + navegador
    python apps/desktop/main.py --no-gui           # solo servidor, en la consola
    python apps/desktop/main.py --self-check --out resultado.json

``--self-check`` abre el contenido empaquetado, cuenta clases, casos y glosario, calcula la
huella de todo el árbol y comprueba que el servidor responde. Lo usa
``scripts/verify_apps.py`` para abrir el binario compilado en vez de fiarse del build.
"""
from __future__ import annotations

import argparse
import hashlib
import http.server
import json
import re
import socketserver
import sys
import threading
import urllib.request
import webbrowser
from pathlib import Path

APP_NAME = "Programa de Ingeniería de Software Moderna"
HOST = "127.0.0.1"
PREFERRED_PORT = 8765

CLASS_RE = re.compile(r"^SE-\d{3}\.html$")


def site_root() -> Path:
    """Carpeta ``site/``: dentro del paquete PyInstaller o, en un checkout, la del repo."""
    bundled = getattr(sys, "_MEIPASS", None)
    if bundled:
        return Path(bundled) / "site"
    return Path(__file__).resolve().parents[2] / "site"


def read_version() -> str:
    for candidate in (
        Path(getattr(sys, "_MEIPASS", "")) / "VERSION",
        Path(__file__).resolve().parents[1] / "VERSION",
    ):
        if candidate.is_file():
            return candidate.read_text(encoding="utf-8").strip()
    return "desconocida"


def tree_digest(root: Path) -> tuple[str, int]:
    """Huella SHA-256 del árbol: ``ruta\\0sha256\\n`` ordenado. Devuelve (huella, nº de ficheros)."""
    outer = hashlib.sha256()
    count = 0
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = path.relative_to(root).as_posix()
        inner = hashlib.sha256(path.read_bytes()).hexdigest()
        outer.update(f"{rel}\0{inner}\n".encode("utf-8"))
        count += 1
    return outer.hexdigest(), count


def inventory(root: Path) -> dict:
    """Cuenta lo que hay dentro del portal empaquetado."""
    classes = sorted(p.name for p in (root / "classes").glob("SE-*.html") if CLASS_RE.match(p.name))
    cases = {kind: sorted(p.stem for p in (root / "casos" / kind).glob("*.html") if p.name != "index.html")
             for kind in ("exito", "fallo")}
    glossary = [p for p in (root / "glosario").rglob("*.html") if p.name != "index.html"]
    return {
        "classes": len(classes),
        "first_class": classes[0] if classes else None,
        "last_class": classes[-1] if classes else None,
        "cases": {kind: len(slugs) for kind, slugs in cases.items()},
        "case_total": sum(len(slugs) for slugs in cases.values()),
        "glossary_terms": len(glossary),
        "has_index": (root / "index.html").is_file(),
        "has_catalog": (root / "assets" / "catalog.json").is_file(),
    }


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    """Solo GET/HEAD sobre ``site/``; sin registro por petición."""

    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        # el registro de Windows a veces asocia .js o .svg a tipos que el navegador rechaza
        ".html": "text/html; charset=utf-8",
        ".css": "text/css; charset=utf-8",
        ".js": "text/javascript; charset=utf-8",
        ".json": "application/json; charset=utf-8",
        ".svg": "image/svg+xml",
        "": "application/octet-stream",
    }

    def log_message(self, format: str, *args) -> None:  # noqa: A002 - firma de la clase base
        return


def start_server(root: Path, port: int = PREFERRED_PORT) -> socketserver.TCPServer:
    def handler(*args, **kwargs):
        return QuietHandler(*args, directory=str(root), **kwargs)

    class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
        daemon_threads = True

    for candidate in (port, 0):  # si el puerto preferido está ocupado, pide uno libre al sistema
        try:
            server = Server((HOST, candidate), handler)
            break
        except OSError:
            continue
    else:  # pragma: no cover - sin puertos libres no hay nada que hacer
        raise SystemExit("No se pudo abrir ningún puerto de loopback.")
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def base_url(server: socketserver.TCPServer) -> str:
    return f"http://{HOST}:{server.server_address[1]}/"


def self_check(root: Path, out: Path | None) -> int:
    """Abre el contenido empaquetado y lo cuenta; sale con 1 si el portal está vacío o no responde."""
    report: dict = {"app": APP_NAME, "version": read_version(), "site_root_exists": root.is_dir()}
    ok = root.is_dir()
    if ok:
        report["inventory"] = inventory(root)
        digest, files = tree_digest(root)
        report.update(tree_sha256=digest, files=files)
        server = start_server(root, 0)
        try:
            with urllib.request.urlopen(base_url(server) + "classes/SE-001.html", timeout=10) as reply:
                body = reply.read()
                report["http"] = {"status": reply.status, "bytes": len(body),
                                  "content_type": reply.headers.get("Content-Type")}
            with urllib.request.urlopen(base_url(server) + "assets/catalog.json", timeout=10) as reply:
                catalog = json.loads(reply.read().decode("utf-8"))
                report["catalog_classes"] = len(catalog.get("classes", []))
            ok = report["http"]["status"] == 200 and report["http"]["bytes"] > 1000
        except (OSError, ValueError) as error:  # 404 de un portal vacío, catálogo ilegible, etc.
            report["error"] = f"{type(error).__name__}: {error}"
            ok = False
        finally:
            server.shutdown()
    report["ok"] = bool(ok)
    text = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True)
    if out:
        out.write_text(text + "\n", encoding="utf-8")
    elif sys.stdout:
        print(text)
    return 0 if ok else 1


def run_window(url: str, server: socketserver.TCPServer) -> None:
    import tkinter as tk
    from tkinter import ttk

    window = tk.Tk()
    window.title(APP_NAME)
    window.geometry("560x260")
    window.resizable(False, False)
    frame = ttk.Frame(window, padding=18)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text=APP_NAME, font=("Segoe UI", 14, "bold"), wraplength=520).pack(anchor="w")
    ttk.Label(frame, text=f"Versión {read_version()} · 612 clases, 32 casos y glosario, sin conexión",
              wraplength=520).pack(anchor="w", pady=(4, 12))
    ttk.Label(frame, wraplength=520, text=(
        "El portal se sirve solo en tu equipo (127.0.0.1) y se abre en tu navegador. "
        "Cierra esta ventana para detener el servidor.")).pack(anchor="w")
    ttk.Label(frame, text=url, font=("Consolas", 11)).pack(anchor="w", pady=10)
    buttons = ttk.Frame(frame)
    buttons.pack(anchor="w", pady=(8, 0))

    def copy_url() -> None:
        window.clipboard_clear()
        window.clipboard_append(url)

    ttk.Button(buttons, text="Abrir en el navegador", command=lambda: webbrowser.open(url)).pack(side="left")
    ttk.Button(buttons, text="Copiar dirección", command=copy_url).pack(side="left", padx=8)
    ttk.Button(buttons, text="Salir", command=window.destroy).pack(side="left")
    window.after(400, lambda: webbrowser.open(url))
    window.mainloop()
    server.shutdown()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=APP_NAME)
    parser.add_argument("--no-gui", action="store_true", help="solo servidor, sin ventana")
    parser.add_argument("--no-browser", action="store_true", help="no abrir el navegador")
    parser.add_argument("--port", type=int, default=PREFERRED_PORT)
    parser.add_argument("--self-check", action="store_true", help="contar el contenido empaquetado y salir")
    parser.add_argument("--out", type=Path, help="con --self-check: escribir el informe JSON aquí")
    args = parser.parse_args(argv)

    root = site_root()
    if args.self_check:
        return self_check(root, args.out)
    if not (root / "index.html").is_file():
        message = f"El portal no está empaquetado: falta {root / 'index.html'}"
        if sys.stderr:
            print(message, file=sys.stderr)
        return 1

    server = start_server(root, args.port)
    url = base_url(server)
    if args.no_gui:
        print(f"{APP_NAME} en {url} (Ctrl+C para salir)")
        if not args.no_browser:
            webbrowser.open(url)
        try:
            threading.Event().wait()
        except KeyboardInterrupt:
            server.shutdown()
        return 0
    try:
        run_window(url, server)
    except ImportError:  # sin tkinter: la consola basta
        webbrowser.open(url)
        threading.Event().wait()
    return 0


if __name__ == "__main__":
    sys.exit(main())
