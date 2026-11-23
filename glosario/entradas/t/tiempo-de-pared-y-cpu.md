# Tiempo de pared y cpu

[↑ Glosario](../../README.md) · [← Tiempo de ocurrencia / de procesamiento](./tiempo-de-ocurrencia-de-procesamiento.md) · [Tiempo de recuperación →](./tiempo-de-recuperacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

Wall time incluye espera; cpu time cuenta ejecución en procesador.

Definición de trabajo de [SE-099 — Profilers de CPU, memoria, I/O y red](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md).

## Por qué importa

En [SE-099 — Profilers de CPU, memoria, I/O y red](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md), el tema «Tiempo de pared y CPU» importa porque wall time incluye espera; CPU time cuenta ejecución en procesador.

## Cómo funciona

Según [SE-099 — Profilers de CPU, memoria, I/O y red](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md), en la sección «Tiempo de pared y CPU»:

Wall time incluye espera; CPU time cuenta ejecución en procesador. Una tarea I/O-bound puede tener pared alta y CPU baja. Perfilar solo funciones de CPU no atribuye latencia externa ni cola.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-099 — Profilers de CPU, memoria, I/O y red](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md):

En el entorno reproducible de diagnóstico, una investigación conserva síntoma, entorno, reproducción, hipótesis, observaciones, causa, corrección y regresión. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-099 — Profilers de CPU, memoria, I/O y red](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md)) son:

- **Se optimiza una función que no era el problema** — causa: perfil determinista inflado por llamadas. Corrección: confirmar con el tiempo total sin perfilador.
- **El perfil de memoria hace la prueba 62 veces más lenta** — causa: `tracemalloc` activo en la medición de tiempo. Corrección: perfilar memoria y tiempo en ejecuciones separadas.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-099 — Profilers de CPU, memoria, I/O y red](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md)) son: Las definiciones son operativas para el entorno reproducible de diagnóstico. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Un perfil dinámico observa entradas ejecutadas. La siguiente clase combina compilador, linter, formatter y análisis estático para detectar clases distintas de defectos.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Espera](../e/espera.md), [Asignaciones, retención y pico](../a/asignaciones-retencion-y-pico.md), [I/o y red](../i/i-o-y-red.md), [Perfil como hipótesis](../p/perfil-como-hipotesis.md), [Perfil determinista y muestreo](../p/perfil-determinista-y-muestreo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-099 — Profilers de CPU, memoria, I/O y red](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md).

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

[↑ Glosario](../../README.md) · [← Tiempo de ocurrencia / de procesamiento](./tiempo-de-ocurrencia-de-procesamiento.md) · [Tiempo de recuperación →](./tiempo-de-recuperacion.md)
