# Formatter

[↑ Glosario](../../README.md) · [← Formato columnar](./formato-columnar.md) · [Forward proxy →](./forward-proxy.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

Un **formatter** (formateador) es una herramienta que **transforma la presentación del código fuente bajo reglas deterministas**: sangrías, espacios, saltos de línea, orden de importaciones, comillas. Dada la misma entrada y la misma configuración produce siempre la misma salida. En [SE-100](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md) se presenta junto al compilador, el *linter* y el análisis estático, con un papel acotado: reducir las discusiones de estilo, sin juzgar el contenido. Que sea determinista es lo que lo distingue de una guía de estilo que se aplica a mano.

## Por qué importa

Sin un formateador común, los cambios de código arrastran ruido: sangrías distintas, líneas reflujadas, estilos que dependen de cada editor, y las revisiones se llenan de comentarios de estilo. Con uno, el formato deja de ser tema de conversación y los *diffs* muestran solo cambios de significado. La decisión que cambia es quién decide el estilo: la herramienta, con una configuración versionada, en lugar de cada persona o de cada revisión. También permite **reproducir el formato en integración continua**, de modo que un cambio mal formateado se detecte automáticamente.

## Cómo funciona

El formateador analiza el código a un árbol sintáctico (o a una representación que conserva el significado) y lo **vuelve a imprimir** con sus reglas, descartando el formato original. Por eso el resultado no depende de cómo estaba escrito, y por eso es idempotente: formatear lo ya formateado no cambia nada. Dos usos típicos:

- **Escribir:** se ejecuta al guardar o antes de confirmar un cambio.
- **Comprobar:** en integración continua se ejecuta en modo de verificación, que falla si algún archivo cambiaría.

Dos precauciones se desprenden de [SE-100](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md). Primero, un formateador **no mejora nombres, cohesión ni corrección**: ordena la apariencia, no el diseño. Segundo, hay que **versionarlo**: un cambio en las reglas de una versión nueva reformatea muchos archivos y produce *diffs* masivos sin cambio de comportamiento; fijar versión y configuración en el repositorio lo evita y permite que el editor y la integración continua den el mismo resultado.

## Ejemplo

Un proyecto fija la herramienta y su versión, y verifica en integración continua:

```bash
python -m black --check src tests     # falla si algún archivo cambiaría
python -m black src tests             # reformatea
```

Si dos personas escriben el mismo código con estilos diferentes, tras formatear ambas versiones son idénticas y la revisión se concentra en la lógica. Si la herramienta se actualiza sin fijar versión, un cambio de regla puede reescribir cientos de líneas en un solo cambio; fijar la versión convierte esa actualización en una decisión explícita, con su propio cambio dedicado.

## Errores y confusiones comunes

- **Creer que el formateador mejora el código.** Solo ordena la presentación.
- **No fijar versión.** Los cambios de regla producen diffs masivos y discrepancias entre editor e integración continua.
- **Confundirlo con el linter.** El linter detecta patrones sospechosos (variables sin uso, comparaciones erróneas); el formateador no juzga. A veces se solapan (orden de importaciones), pero son herramientas distintas.
- **Mezclar reformateos y cambios funcionales.** Dificulta la revisión; el reformateo masivo va en su propio cambio.

## Límites y cuándo no aplica

La señal estática no sustituye experimentación y puede ser ruidosa durante la exploración ([SE-100](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md)): formatear a cada paso un cuaderno de pruebas puede estorbar. El formateador impone un estilo único, que a veces resulta menos legible en un caso concreto (una tabla alineada a mano); la mayoría de las herramientas permiten desactivarlo por bloque. Y en equipos con una guía de estilo ya aplicada y poco cambio, el beneficio marginal es menor.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Regla](../r/regla.md), [Análisis estático y límites](../a/analisis-estatico-y-limites.md), [Compilación y front-end](../c/compilacion-y-front-end.md), [Linter](../l/linter.md), [Tipos y flujo](../t/tipos-y-flujo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-100 — Compiladores, linters, formatters y análisis estático](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-099](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md), [SE-101](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md), [SE-116](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Language Server Protocol 3.18](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/) — Mensajes, capacidades y sincronización entre editor y servidor; autoridad: Microsoft.
- [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/) — Breakpoints, frames, variables y negociación de capacidades; autoridad: Microsoft.
- [Python Debugging and Profiling](https://docs.python.org/3/library/debug.html) — Pdb, cprofile, timeit, tracemalloc y límites instrumentales; autoridad: Python Software Foundation.
- [Python venv](https://docs.python.org/3/library/venv.html) — Aislamiento de intérprete, scripts y entorno virtual; autoridad: Python Software Foundation.
- [Development Container Specification](https://containers.dev/implementors/spec/) — Configuración reproducible de herramientas y ciclo de vida del contenedor; autoridad: Dev Container Specification maintainers.

---

[↑ Glosario](../../README.md) · [← Formato columnar](./formato-columnar.md) · [Forward proxy →](./forward-proxy.md)
