# Formatter

[↑ Glosario](../../README.md) · [← Formato columnar](./formato-columnar.md) · [Forward proxy →](./forward-proxy.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

Un formatter transforma presentación bajo reglas deterministas y reduce discusiones de estilo.

Definición de trabajo de [SE-100 — Compiladores, linters, formatters y análisis estático](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md).

## Por qué importa

En [SE-100 — Compiladores, linters, formatters y análisis estático](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md), el tema «Formatter» importa porque un formatter transforma presentación bajo reglas deterministas y reduce discusiones de estilo.

## Cómo funciona

Según [SE-100 — Compiladores, linters, formatters y análisis estático](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md), en la sección «Formatter»:

Un formatter transforma presentación bajo reglas deterministas y reduce discusiones de estilo. No mejora nombres, cohesión ni corrección. Versionarlo evita diffs masivos por cambios de regla y permite reproducir formato en CI.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-100 — Compiladores, linters, formatters y análisis estático](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md):

En el entorno reproducible de diagnóstico, una investigación conserva síntoma, entorno, reproducción, hipótesis, observaciones, causa, corrección y regresión. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-100 — Compiladores, linters, formatters y análisis estático](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md)) son:

- **El código pasa mypy y falla al ejecutar** — causa: `Any` o falta de anotaciones. Corrección: reducir `Any` en las fronteras y probar con datos reales.
- **El linter pasa pero hay un defecto conocido** — causa: la regla no está activa. Corrección: revisar el conjunto de reglas y activar la relevante.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-100 — Compiladores, linters, formatters y análisis estático](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md)) son: Las definiciones son operativas para el entorno reproducible de diagnóstico. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. La señal estática no sustituye experimentación y puede ser ruidosa durante exploración. La siguiente clase diseña REPL y notebooks con una ruta explícita hacia artefactos reproducibles.

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
