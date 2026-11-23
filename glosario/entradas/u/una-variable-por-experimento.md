# Una variable por experimento

[↑ Glosario](../../README.md) · [← Umbral de adopción](./umbral-de-adopcion.md) · [Unidad entera →](./unidad-entera.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

Cada ejecución cambia una condición y conserva las demás.

Definición de trabajo de [SE-105 — Reproducción de errores y reducción de casos](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md).

## Por qué importa

En [SE-105 — Reproducción de errores y reducción de casos](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md), el tema «Una variable por experimento» importa porque cada ejecución cambia una condición y conserva las demás.

## Cómo funciona

Según [SE-105 — Reproducción de errores y reducción de casos](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md), en la sección «Una variable por experimento»:

Cada ejecución cambia una condición y conserva las demás. Comparar versiones necesita la misma entrada y configuración. Varias correcciones simultáneas pueden ocultar cuál causó la diferencia y dificultan regresión.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-105 — Reproducción de errores y reducción de casos](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md):

En el entorno reproducible de diagnóstico, una investigación conserva síntoma, entorno, reproducción, hipótesis, observaciones, causa, corrección y regresión. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-105 — Reproducción de errores y reducción de casos](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md)) son:

- **La reducción devuelve resultados distintos** — causa: prueba intermitente. Corrección: repetir cada decisión y fijar semillas.
- **La bisección señala un commit inocente** — causa: dos defectos o prueba inestable. Corrección: estabilizar la prueba y comprobar el commit señalado.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-105 — Reproducción de errores y reducción de casos](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md)) son: Las definiciones son operativas para el entorno reproducible de diagnóstico. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. El caso mínimo aún debe poder ejecutarlo otra persona con modalidades distintas. La siguiente clase incorpora ergonomía y accesibilidad al entorno, no como decoración.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Condición](../c/condicion.md), [Caso mínimo y representatividad](../c/caso-minimo-y-representatividad.md), [Primera divergencia](../p/primera-divergencia.md), [Reducción por dimensiones](../r/reduccion-por-dimensiones.md), [Reproducción determinista](../r/reproduccion-determinista.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-105 — Reproducción de errores y reducción de casos](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

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

[↑ Glosario](../../README.md) · [← Umbral de adopción](./umbral-de-adopcion.md) · [Unidad entera →](./unidad-entera.md)
