# Guía para rediseñar figuras que repiten una tabla

Esta guía es el procedimiento para que una sesión por parte sustituya cada figura
generada con `tab()` (la que redibuja la tabla Markdown de la clase) por un gráfico que
aporte algo que la tabla no da. La regla y la tabla de primitivas están en
[`PEDAGOGICAL-STANDARD.md`](PEDAGOGICAL-STANDARD.md#figuras-regla-anti-duplicado); aquí
está el cómo.

## Qué falla y qué se busca

Una clase imprime una tabla en Markdown y, justo debajo, inserta una figura que es la
misma tabla dibujada con cajas. El párrafo que interpreta la figura sigue siendo
válido; la segunda tabla no. El objetivo es **cero** figuras `tab()` por parte, salvo
una lista explícita y justificada (`allowed_tables` del archivo de línea base).

Modelo de referencia, con los números medidos sin cambios (Parte 22):

| Figura | Antes | Ahora | Función |
| --- | --- | --- | --- |
| `se-265-latencia-segun-la-arquitectura.svg` | tabla de 3 columnas | barras horizontales en escala logarítmica | `grouped_bars(horizontal=True, log=True)` |
| `se-265-acumulador-de-16-bits.svg` | tabla de porcentajes | mapa de calor con la frontera de fallo | `heatmap` |
| `se-266-eficiencia-de-un-bus.svg` | tabla de ciclos y eficiencias | líneas I²C frente a SPI con eje logarítmico | `line_chart(log_x=True)` |

Lee `scripts/figures_part22_a.py` (`se265_latencia`, `se265_acumulador`, `se266_bus`) y
las secciones de `content/part-22/SE-265.md` y `SE-266.md` que las usan antes de empezar.

## Procedimiento por figura

1. **Localiza el duplicado.** En el generador de la parte (`scripts/figures_partNN_a.py`
   y `_b.py`) busca las funciones que llaman a `tab(` y abre la clase: la tabla
   Markdown anterior a la imagen y el párrafo «Cómo leer la figura» posterior.
2. **Decide qué conclusión pierde la clase si se borra la figura.** Si ninguna, la
   figura se elimina o se sustituye por otra evidencia que la clase ya tenga (una
   distribución, una secuencia, un antes y después). No conviertas por convertir.
3. **Elige la primitiva por el tipo de dato** (ver la tabla de abajo). Si los datos son
   un mecanismo (estados, flujo, arquitectura), usa `Fig.box` / `Fig.arrow` / `flow()`.
4. **Reescribe la función con los mismos números.** Copia las cifras de la tabla; no
   las recalcules ni cambies el redondeo. Conserva `SINT` / `MEDIDO` / `EJEC` como
   `foot` si lo tenía y deja en `note` la advertencia de alcance que ya existía.
5. **Mantén el nombre del archivo SVG** (la clave de `FIGURES`) para no tocar la
   referencia. Si el cambio de forma justifica otro nombre, cámbialo en `FIGURES` y en el
   enlace de la clase en el mismo commit; `build_figures.py` borra nada por sí solo, así
   que elimina el SVG antiguo (`git rm`).
6. **Reescribe el `desc` y el `alt`.** Describen el gráfico y su conclusión, no «Tabla
   con…»: «Barras horizontales en escala logarítmica con…; el sondeo llega a 166 ms y la
   interrupción se queda en 0,03 ms». El `alt` va en el texto alternativo de la imagen en la clase
   y el `desc` en el constructor de la figura; ninguno empieza por «Tabla».
7. **Reescribe «Cómo leer la figura. Dónde deja de valer».** Debe decir qué representa
   cada eje, marcador o color, qué mirar primero, qué conclusión sostiene y dónde deja de
   valer. No debe describir celdas ni columnas.
8. **Mira el resultado.** Genera el SVG y renderízalo a PNG antes de confirmar (ver
   «Revisión visual»). Comprueba que nada se corta, que la escala es honesta (empieza en
   cero salvo escala logarítmica declarada) y que los valores rotulados coinciden con la
   tabla.
9. **Baja el tope.** `python scripts/figure_tab_baseline.py --write` y revisa que solo
   bajen las cifras de tu parte (`tables`, `table_alts`).

## Elegir la primitiva

| Dato | Primitiva | Notas |
| --- | --- | --- |
| media / p99 / máximo | `grouped_bars` (`log=True` si el rango pasa de dos décadas) o `percentile_intervals` | `percentile_intervals` fusiona marcas iguales y alterna rótulos |
| un valor por categoría | `grouped_bars` con una serie | `horizontal=True` si los nombres son largos |
| composición de un total | `stacked_bars` | `percent=True` para proporciones; rotula segmentos y total |
| fracción por dos condiciones | `heatmap` | `scale="coral"` para fallos, `"teal"` para éxito; `highlight` marca la frontera |
| antes / después | `dumbbell` | `delta=` escribe el factor; `lower_is_better` decide el color |
| tendencia frente a un parámetro | `line_chart` | `log_x` / `log_y`, `hlines` para plazos, `annotations` para el punto clave |
| observaciones sueltas | `scatter` | `vlines` / `hlines` para umbrales |
| orden y plazos | `timeline` | segmentos, eventos y `ref_lines` |
| mecanismo, estados, flujo | `Fig.box`, `Fig.arrow`, `Fig.group`, `flow()` | ya existían |

Todas están en `scripts/figure_kit.py`, devuelven un `Fig` completo (título visible,
leyenda, ejes con unidades, valores rotulados, nota y pie) y lanzan `ValueError` si una
etiqueta no cabe: acorta el texto, usa `horizontal=True` o amplía `width`. El catálogo
con datos ilustrativos está en `scripts/figure_kit_gallery.py`.

Si una tabla trae **más de una idea**, divídela: la tabla Markdown conserva los valores
exactos y la figura muestra una sola conclusión. Una tabla con una columna de texto
(causa, solución) no se convierte en gráfico: esa columna ya está en la clase.

## Revisión visual

No hay dependencias de renderizado en el repositorio; usa el navegador del equipo. En
Windows con Edge:

```powershell
python scripts/figure_kit_gallery.py "$env:TEMP\galeria"
& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless --screenshot="$env:TEMP\galeria\heatmap.png" --window-size=940,420 "file:///$($env:TEMP -replace '\\','/')/galeria/heatmap.svg"
```

o abre el SVG directamente en el navegador. Para una figura de una parte, genera el SVG
con `python scripts/build_figures.py` y ábrelo desde `content/part-NN/figures/`. Revisa
cada gráfico a tamaño real y en un ancho de móvil (el SVG escala).

## Reconstruir y validar

Desde la raíz del repositorio, en este orden:

```bash
python scripts/build_figures.py
python scripts/build_phase2.py
python scripts/build_phase3.py
python scripts/build_phase4.py
python scripts/figure_tab_baseline.py --write
python scripts/build_figures.py --check
python scripts/build_phase2.py --check
python scripts/build_phase3.py --check
python scripts/build_phase4.py --check
python scripts/validate_class_contracts.py
python scripts/validate_phase3.py
python scripts/validate_phase4.py
python scripts/validate_encoding.py
python scripts/validate_site.py
python scripts/validate_repository.py --strict
python -m unittest discover -s tests -v
npx --yes markdownlint-cli2@0.23.0 "content/part-NN/**/*.md"
```

Una parte por commit. Tras el push, espera a que **Validate**, **Pages** y **Security**
estén en verde antes de registrar el hash en `docs/PART-EXECUTION-TRACKER.md`.

## Qué comprueba la prueba

`tests/test_figure_redesign.py` usa `scripts/figure_tab_baseline.json`:

- `tables`: figuras construidas con `tab()` (atributo `kind == "table"` del `Fig`) por parte;
- `table_alts`: imágenes de clase cuyo `alt` empieza por «Tabla»;
- `embedded_tables`: diagramas que dibujan una tabla con `Fig.table()`;
- cada cifra **no puede subir** y tampoco puede quedar por encima de la real: si bajas
  una, baja el tope en el mismo commit;
- una figura creada con las primitivas de gráfico (`kind == "chart"`) nunca puede tener un
  `alt` ni un `desc` que empiece por «Tabla»;
- `allowed_tables` es la lista de excepciones: nombre de archivo y una justificación de al
  menos 60 caracteres. Se admite, por ejemplo, una tabla cuya conclusión es justamente
  el contraste de texto entre dos columnas y no un valor numérico. Cualquier otra se rediseña.

Si añades un nuevo ayudante que dibuja tablas, márcalo con `fig.kind = "table"` para que
el trinquete lo cuente.

## Errores frecuentes

- cambiar una cifra al redibujar: la figura debe coincidir con la tabla y con el texto;
- escala truncada que exagera una diferencia: las barras empiezan en cero; si no se
  puede, usa escala logarítmica y dilo en el eje (las primitivas lo añaden solas);
- gráfico con una sola barra o dos puntos: no necesita figura, necesita una frase;
- dejar «Cómo leer la figura» hablando de filas y columnas;
- rotular solo con color: usa los marcadores, trazos y rótulos que ya dan las primitivas;
- olvidar `git rm` del SVG cuando se cambia el nombre de archivo.
