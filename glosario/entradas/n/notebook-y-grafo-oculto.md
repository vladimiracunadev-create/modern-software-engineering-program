# Notebook y grafo oculto

[↑ Glosario](../../README.md) · [← Normativo](./normativo.md) · [Nube híbrida →](./nube-hibrida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

Visualmente las celdas tienen orden, pero pueden ejecutarse en otra secuencia.

Definición de trabajo de [SE-101 — REPL, notebooks y desarrollo exploratorio](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md).

## Por qué importa

En [SE-101 — REPL, notebooks y desarrollo exploratorio](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md), el tema «Notebook y grafo oculto» importa porque visualmente las celdas tienen orden, pero pueden ejecutarse en otra secuencia.

## Cómo funciona

Según [SE-101 — REPL, notebooks y desarrollo exploratorio](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md), en la sección «Notebook y grafo oculto»:

Visualmente las celdas tienen orden, pero pueden ejecutarse en otra secuencia. Salidas persistidas tampoco prueban qué código las produjo. Reiniciar kernel y ejecutar todo revela dependencias; parametrizar separa entrada de estado interactivo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-101 — REPL, notebooks y desarrollo exploratorio](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md):

En el entorno reproducible de diagnóstico, una investigación conserva síntoma, entorno, reproducción, hipótesis, observaciones, causa, corrección y regresión. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-101 — REPL, notebooks y desarrollo exploratorio](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md)) son:

- **El cuaderno da otro resultado en otra máquina** — causa: estado oculto por orden de ejecución. Corrección: reiniciar y ejecutar todo antes de compartir.
- **El diff es enorme con cambios mínimos** — causa: salidas y metadatos en el archivo. Corrección: limpiar las salidas antes de confirmar.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-101 — REPL, notebooks y desarrollo exploratorio](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md)) son: Las definiciones son operativas para el entorno reproducible de diagnóstico. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Un proceso limpio aún puede usar otra versión de runtime. La siguiente clase fija instalación y selección del intérprete sin esconder el mecanismo.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Celda](../c/celda.md), [Secuencia](../s/secuencia.md), [Exploración frente a producto](../e/exploracion-frente-a-producto.md), [Narrativa y verificación](./narrativa-y-verificacion.md), [Proveniencia de datos](../p/proveniencia-de-datos.md), [Repl y ciclo de realimentación](../r/repl-y-ciclo-de-realimentacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-101 — REPL, notebooks y desarrollo exploratorio](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

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

[↑ Glosario](../../README.md) · [← Normativo](./normativo.md) · [Nube híbrida →](./nube-hibrida.md)
