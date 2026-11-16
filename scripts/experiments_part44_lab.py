"""Utilidades compartidas de los experimentos de la Parte 44 (estilos arquitectónicos).

Todo es biblioteca estándar. Incluye un servidor HTTP local, un proxy TCP de un salto y
estadísticos simples. Nada sale de la máquina: los servidores escuchan solo en 127.0.0.1 y en
un puerto que asigna el sistema operativo.
"""
from __future__ import annotations

import http.client
import json
import socket
import statistics
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def pct(values, q):
    """Percentil por rango más cercano (sin interpolar), estable entre plataformas."""
    ordered = sorted(values)
    idx = max(0, min(len(ordered) - 1, int(round(q * (len(ordered) - 1)))))
    return ordered[idx]


def fmt(x, d=2):
    return f"{x:.{d}f}".replace(".", ",")


def table(rows):
    for r in rows:
        print("  " + " | ".join(str(c) for c in r))


# ---------------------------------------------------------------- servidor HTTP local
PAYLOAD = {"id": "e1", "student": "s1", "course": "c1", "due": 72, "submitted": False}


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_GET(self):  # noqa: N802 (nombre impuesto por la biblioteca)
        body = json.dumps(PAYLOAD).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):  # silencio
        pass


def start_server():
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    server.daemon_threads = True
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def start_proxy(target_port):
    """Proxy TCP de un salto: copia bytes en ambos sentidos, como haría un sidecar mínimo."""
    listener = socket.socket()
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(("127.0.0.1", 0))
    listener.listen(64)

    def pump(src, dst):
        try:
            while True:
                data = src.recv(65536)
                if not data:
                    break
                dst.sendall(data)
        except OSError:
            pass
        finally:
            for s in (src, dst):
                try:
                    s.shutdown(socket.SHUT_RDWR)
                except OSError:
                    pass

    def accept_loop():
        while True:
            try:
                client, _ = listener.accept()
            except OSError:
                return
            upstream = socket.create_connection(("127.0.0.1", target_port))
            for a, b in ((client, upstream), (upstream, client)):
                threading.Thread(target=pump, args=(a, b), daemon=True).start()

    threading.Thread(target=accept_loop, daemon=True).start()
    return listener


def time_calls(fn, n):
    out = []
    for _ in range(n):
        t = time.perf_counter()
        fn()
        out.append((time.perf_counter() - t) * 1000)
    return out


def keepalive_caller(port):
    conn = http.client.HTTPConnection("127.0.0.1", port)

    def call():
        conn.request("GET", "/")
        r = conn.getresponse()
        r.read()

    return call, conn


def fresh_caller(port):
    def call():
        conn = http.client.HTTPConnection("127.0.0.1", port)
        conn.request("GET", "/")
        r = conn.getresponse()
        r.read()
        conn.close()

    return call


def median(values):
    return statistics.median(values)
