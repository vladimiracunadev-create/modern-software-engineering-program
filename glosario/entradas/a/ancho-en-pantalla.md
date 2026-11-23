# Ancho en pantalla

[↑ Glosario](../../README.md) · [← Ancho de banda](./ancho-de-banda.md) · [Anchura →](./anchura.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Número de celdas de terminal que ocupa un texto, distinto de su longitud en caracteres.

Definición de trabajo de [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md).

## Por qué importa

En [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md), el tema «Texto Unicode» importa porque `len()` no mide el ancho en pantalla; dos formas pueden ser el mismo texto.

## Cómo funciona

Según [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md):

Un acento puede ser un carácter (`é`, NFC) o dos (`e` más un diacrítico combinante, NFD): `len` da 1 o 2 para lo mismo que se ve. Un ideograma ocupa dos celdas; un emoji compuesto con un unión de ancho cero ocupa dos y varias posiciones de código. Alinear con `ljust()` y `len()` produce columnas torcidas. La alineación correcta usa el **ancho en pantalla** (propiedad `East Asian Width`, ignorando los combinantes y los de ancho cero) y, antes de comparar o agrupar, normaliza a una forma (NFC) para que «José» sea siempre la misma cadena.

Según [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md):

`notas validar` decide su presentación así: color solo si `isatty()` y no existe `NO_COLOR`, con `--color` como interruptor; prefijos textuales (`ERROR`, `AVISO`, `OK`) que repiten lo que dice el color; ancho tomado de `shutil.get_terminal_size()` y respetado por una función de tabla que alinea por ancho en pantalla; identificadores truncados por el medio con una opción `--ancho-completo`; texto normalizado a NFC al leer; y un modo `--sin-animacion` (por defecto cuando no hay terminal) que escribe una línea por evento. Una prueba ejecuta el informe en tubería y falla si encuentra una secuencia de escape; otra compara la tabla con nombres NFC y NFD y exige igual alineación.

## Ejemplo

Ejemplo de [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md) (sección «Ejemplo profesional»):

`notas validar` decide su presentación así: color solo si `isatty()` y no existe `NO_COLOR`, con `--color` como interruptor; prefijos textuales (`ERROR`, `AVISO`, `OK`) que repiten lo que dice el color; ancho tomado de `shutil.get_terminal_size()` y respetado por una función de tabla que alinea por ancho en pantalla; identificadores truncados por el medio con una opción `--ancho-completo`; texto normalizado a NFC al leer; y un modo `--sin-animacion` (por defecto cuando no hay terminal) que escribe una línea por evento. Una prueba ejecuta el informe en tubería y falla si encuentra una secuencia de escape; otra compara la tabla con nombres NFC y NFD y exige igual alineación.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La tabla sale torcida con acentos o ideogramas** — causa: se alineó con `len()`. Corrección: alinear por ancho en pantalla y normalizar. ([SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md)) son: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos salvo el tamaño en bytes. No se probó ningún terminal interactivo, ninguna biblioteca de interfaz de texto ni ningún lector de pantalla; el ancho se estimó con una propiedad Unicode. La siguiente clase pasa de la interfaz de un proceso corto a la de uno que vive mucho tiempo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-220](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Celda](../c/celda.md), [Terminal](../t/terminal.md), [Normalización Unicode](../n/normalizacion-unicode.md), [Secuencia de escape](../s/secuencia-de-escape.md), [TUI](../t/tui.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ECMA-48: Control Functions for Coded Character Sets](https://ecma-international.org/publications-and-standards/standards/ecma-48/) — secuencias de control de los terminales; autoridad: Ecma International.
- [NO_COLOR](https://no-color.org/) — convención para desactivar el color; autoridad: proyecto comunitario.
- [Unicode UAX #11: East Asian Width](https://www.unicode.org/reports/tr11/) — clasificación de anchos de carácter; autoridad: Consorcio Unicode.
- [Unicode UAX #15: Normalization Forms](https://www.unicode.org/reports/tr15/) — NFC y NFD; autoridad: Consorcio Unicode.
- [W3C: WCAG 2.2](https://www.w3.org/TR/WCAG22/) — pautas de accesibilidad; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Ancho de banda](./ancho-de-banda.md) · [Anchura →](./anchura.md)
