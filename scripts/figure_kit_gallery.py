"""Gallery of the chart primitives of ``figure_kit`` with illustrative data.

Run ``python scripts/figure_kit_gallery.py <output-dir>`` to write one SVG per primitive and look at
them (or render them to PNG) when you design a figure. The numbers are invented for the gallery and
are never used by a lesson. ``tests/test_figure_redesign.py`` builds every entry so that a change to
the kit that makes a label overflow fails the build.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from figure_kit import (Fig, dumbbell, grouped_bars, heatmap, line_chart, percentile_intervals,  # noqa: E402
                        scatter, stacked_bars, timeline)

NOTE = "Datos ilustrativos de la galería: no proceden de ninguna medición."


def gallery_grouped_vertical() -> Fig:
    return grouped_bars(
        "Barras agrupadas verticales: tiempo de respuesta por versión y percentil",
        "Barras agrupadas verticales con el tiempo de respuesta en milisegundos de tres versiones en el percentil 50 y el 99.",
        ["Versión 1", "Versión 2", "Versión 3"],
        [("p50", [120, 95, 60], "teal"), ("p99", [900, 640, 210], "coral")],
        unit="Tiempo de respuesta (ms)", ref_lines=[(500, "Objetivo: 500 ms")], note=NOTE)


def gallery_grouped_horizontal_log() -> Fig:
    return grouped_bars(
        "Barras agrupadas horizontales en escala logarítmica",
        "Barras horizontales en escala logarítmica con la media, el percentil 99 y el máximo de dos configuraciones.",
        ["Configuración con una cola muy larga", "Configuración acotada"],
        [("Media", [14.19, 0.025], "teal"), ("p99", [78.2, 0.03], "gold"), ("Máx", [166, 0.03], "coral")],
        unit="Latencia (ms)", horizontal=True, log=True, ticks=[0.01, 0.1, 1, 10, 100, 1000], note=NOTE)


def gallery_stacked_vertical() -> Fig:
    return stacked_bars(
        "Barras apiladas: de qué se compone el tiempo de una petición",
        "Barras apiladas verticales con el tiempo de tres peticiones repartido en red, servidor y base de datos.",
        ["Búsqueda", "Pago", "Informe"],
        [("Red", [30, 45, 20], "teal"), ("Servidor", [50, 80, 40], "gold"), ("Base de datos", [20, 120, 300], "coral")],
        unit="Tiempo (ms)", note=NOTE)


def gallery_stacked_percent_horizontal() -> Fig:
    return stacked_bars(
        "Barras apiladas al 100 %: reparto del esfuerzo por tipo de tarea",
        "Barras horizontales apiladas al cien por cien con el reparto del esfuerzo de tres equipos.",
        ["Equipo A", "Equipo B", "Equipo C"],
        [("Construir", [60, 40, 25], "teal"), ("Probar", [25, 35, 25], "gold"), ("Operar", [15, 25, 50], "coral")],
        unit="Esfuerzo", horizontal=True, percent=True, note=NOTE)


def gallery_line_log() -> Fig:
    return line_chart(
        "Líneas con marcadores, escala logarítmica y anotación",
        "Dos curvas de tiempo según el tamaño de la entrada en escala logarítmica en ambos ejes, una lineal y otra cuadrática.",
        [("Lineal", [(10, 0.4), (100, 4), (1000, 41), (10000, 420)], "teal"),
         ("Cuadrática", [(10, 0.2), (100, 18), (1000, 1900), (10000, 190000)], "coral")],
        x_label="Tamaño de la entrada (n)", y_label="Tiempo (ms)", log_x=True, log_y=True,
        x_ticks=[(10, "10"), (100, "100"), (1000, "1 000"), (10000, "10 000")],
        point_labels="last", hlines=[(1000, "Límite: 1 s")],
        annotations=[(1000, 1900, "con n = 1 000 la cuadrática ya pasó el límite", -250, -30)],
        note=NOTE)


def gallery_scatter() -> Fig:
    return scatter(
        "Dispersión: tamaño de un cambio y días hasta fusionarlo",
        "Dispersión con cada punto un cambio de código: los cambios de más de 400 líneas tardan más de seis días en fusionarse.",
        [("Cambios del equipo", [(20, 0.5), (45, 0.8), (90, 1.4), (150, 2.2), (260, 3.8), (420, 6.1), (700, 9.5), (60, 1.0)], "teal"),
         ("Cambios con revisión doble", [(80, 2.9), (310, 7.3), (520, 8.8)], "coral")],
        x_label="Líneas cambiadas", y_label="Días hasta fusionar", vlines=[(400, "400 líneas")],
        x_ticks=[(0, "0"), (200, "200"), (400, "400"), (600, "600"), (800, "800")], note=NOTE)


def gallery_heatmap() -> Fig:
    return heatmap(
        "Mapa de calor: fracción de fallos por condición",
        "Mapa de calor con el porcentaje de peticiones fallidas según la carga y el tiempo de espera.",
        ["Carga baja", "Carga media", "Carga alta"], ["Espera 50 ms", "Espera 200 ms", "Espera 1 s"],
        [[0.2, 0.0, 0.0], [4.5, 0.8, 0.1], [38.0, 12.5, 2.3]], unit="% de peticiones fallidas",
        row_title="Condición", col_title="Tiempo de espera del cliente", scale="coral", decimals=1, suffix=" %",
        note=NOTE)


def gallery_dumbbell() -> Fig:
    return dumbbell(
        "Antes y después: duración de cada etapa de la integración continua",
        "Mancuernas con la duración en minutos de tres etapas antes y después de cachear dependencias; todas mejoran.",
        [("Instalar dependencias", 6.2, 0.9), ("Compilar", 4.1, 3.8), ("Ejecutar pruebas", 12.0, 5.5)],
        unit="Duración (min)", names=("Antes de la caché", "Con caché"),
        delta=lambda a, b: f"×{a / b:.1f}".replace(".", ","), note=NOTE)


def gallery_percentiles() -> Fig:
    return percentile_intervals(
        "Intervalos: p50, p99 y máximo de cada configuración",
        "Intervalos de latencia con la mediana, el percentil 99 y el máximo de tres configuraciones en escala logarítmica.",
        [("Sin caché", [120, 480, 2300]), ("Con caché local", [8, 95, 410]), ("Con caché y precarga", [6, 6.4, 6.4])],
        unit="Latencia (ms)", log=True, ref_lines=[(500, "Objetivo")], note=NOTE)


def gallery_timeline() -> Fig:
    return timeline(
        "Secuencia: quién hace qué durante un despliegue",
        "Línea de tiempo con tres carriles, integración continua, entorno y observabilidad, durante diez minutos de un despliegue.",
        [("Integración continua", [(0, 3, "Construir", "teal"), (3, 4, "Firmar", "navy")]),
         ("Entorno", [(4, 6, "Migrar", "gold"), (6, 8, "Reiniciar", "coral")]),
         ("Observabilidad", [(6, 10, "Vigilar errores", "grey")])],
        unit="Minutos desde el inicio", events=[(4, "Aprobación"), (8, "Tráfico completo")],
        ref_lines=[(9, "Plazo")], note=NOTE)


GALLERY = {
    "grouped-vertical": gallery_grouped_vertical,
    "grouped-horizontal-log": gallery_grouped_horizontal_log,
    "stacked-vertical": gallery_stacked_vertical,
    "stacked-percent-horizontal": gallery_stacked_percent_horizontal,
    "line-log": gallery_line_log,
    "scatter": gallery_scatter,
    "heatmap": gallery_heatmap,
    "dumbbell": gallery_dumbbell,
    "percentiles": gallery_percentiles,
    "timeline": gallery_timeline,
}


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python scripts/figure_kit_gallery.py <output-dir>", file=sys.stderr)
        return 2
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for name, builder in GALLERY.items():
        (out / f"{name}.svg").write_text(builder().svg(), encoding="utf-8", newline="\n")
    print(f"GALLERY_OK: {len(GALLERY)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
