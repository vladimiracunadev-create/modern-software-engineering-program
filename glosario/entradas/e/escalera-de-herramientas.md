# Escalera de herramientas

[↑ Glosario](../../README.md) · [← Escalera de degradación](./escalera-de-degradacion.md) · [Escalón de tráfico →](./escalon-de-trafico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

Se empieza por versión, logs y reproducción; luego debugger, profiler o análisis según la pregunta.

Definición de trabajo de [SE-107 — Taller: diagnosticar un fallo desconocido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md).

## Por qué importa

En [SE-107 — Taller: diagnosticar un fallo desconocido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md), el tema «Escalera de herramientas» importa porque se empieza por versión, logs y reproducción; luego debugger, profiler o análisis según la pregunta.

## Cómo funciona

Según [SE-107 — Taller: diagnosticar un fallo desconocido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md), en la sección «Escalera de herramientas»:

Se empieza por versión, logs y reproducción; luego debugger, profiler o análisis según la pregunta. Herramienta más sofisticada no implica mejor evidencia. Cada paso registra qué descartó y qué incertidumbre queda.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-107 — Taller: diagnosticar un fallo desconocido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md):

En el entorno reproducible de diagnóstico, una investigación conserva síntoma, entorno, reproducción, hipótesis, observaciones, causa, corrección y regresión. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-107 — Taller: diagnosticar un fallo desconocido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md)) son:

- **Se cambia código antes de reproducir** — causa: se actúa sobre una impresión. Corrección: escribir la prueba determinista primero.
- **El diagnóstico se repite entre personas** — causa: no hay registro. Corrección: escribir hipótesis, pruebas y descartes.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-107 — Taller: diagnosticar un fallo desconocido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md)) son: Las definiciones son operativas para el entorno reproducible de diagnóstico. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. El taller produce diagnóstico del caso dado; no demuestra que todo el equipo pueda recrearlo. El proyecto siguiente convierte el proceso en entorno autocontenido con ruta de recuperación.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Análisis](../a/analisis.md), [Reproducción](../r/reproduccion.md), [Versión](../v/version.md), [Causa, corrección y seguimiento](../c/causa-correccion-y-seguimiento.md), [Cronología y hechos](../c/cronologia-y-hechos.md), [Hipótesis rivales](../h/hipotesis-rivales.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-107 — Taller: diagnosticar un fallo desconocido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

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

[↑ Glosario](../../README.md) · [← Escalera de degradación](./escalera-de-degradacion.md) · [Escalón de tráfico →](./escalon-de-trafico.md)
