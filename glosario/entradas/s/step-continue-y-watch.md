# Step, continue y watch

[↑ Glosario](../../README.md) · [← Stdout, stderr y formatos](./stdout-stderr-y-formatos.md) · [Strategy →](./strategy.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

Step into sigue llamadas, over ejecuta la llamada y out termina el frame.

Definición de trabajo de [SE-098 — Depuradores, breakpoints y observación de estado](../../../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md).

## Por qué importa

En [SE-098 — Depuradores, breakpoints y observación de estado](../../../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md), el tema «Step, continue y watch» importa porque step into sigue llamadas, over ejecuta la llamada y out termina el frame.

## Cómo funciona

Según [SE-098 — Depuradores, breakpoints y observación de estado](../../../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md), en la sección «Step, continue y watch»:

Step into sigue llamadas, over ejecuta la llamada y out termina el frame. Watch reevalúa expresiones al pausar. Avanzar sin hipótesis produce una película larga; el entorno reproducible de diagnóstico marca el estado esperado y busca la primera transición que lo viola.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-098 — Depuradores, breakpoints y observación de estado](../../../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md):

En el entorno reproducible de diagnóstico, una investigación conserva síntoma, entorno, reproducción, hipótesis, observaciones, causa, corrección y regresión. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-098 — Depuradores, breakpoints y observación de estado](../../../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md)) son:

- **El fallo desaparece al depurar** — causa: el depurador altera los tiempos. Corrección: observar con registros o `sys.monitoring` y comparar.
- **Un proceso queda colgado en producción** — causa: `breakpoint()` olvidado. Corrección: regla de revisión y `PYTHONBREAKPOINT=0`.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-098 — Depuradores, breakpoints y observación de estado](../../../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md)) son: Las definiciones son operativas para el entorno reproducible de diagnóstico. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. El debugger explica una ejecución, no dónde se consume tiempo o memoria en una carga. La siguiente clase usa perfiles dirigidos por pregunta.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Frame](../f/frame.md), [Breakpoint y condición](../b/breakpoint-y-condicion.md), [Debugger, adapter y runtime](../d/debugger-adapter-y-runtime.md), [Heisenbug y costo de pausa](../h/heisenbug-y-costo-de-pausa.md), [Stack frame y alcance](./stack-frame-y-alcance.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-098 — Depuradores, breakpoints y observación de estado](../../../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

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

[↑ Glosario](../../README.md) · [← Stdout, stderr y formatos](./stdout-stderr-y-formatos.md) · [Strategy →](./strategy.md)
