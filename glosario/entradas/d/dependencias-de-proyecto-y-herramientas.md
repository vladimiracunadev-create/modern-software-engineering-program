# Dependencias de proyecto y herramientas

[↑ Glosario](../../README.md) · [← Dependencia transitiva](./dependencia-transitiva.md) · [Dependencias y distribución →](./dependencias-y-distribucion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

Runtime, dependencias de ejecución, desarrollo y herramientas globales tienen ciclos distintos.

Definición de trabajo de [SE-103 — Entornos virtuales y aislamiento de dependencias](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md).

## Por qué importa

En [SE-103 — Entornos virtuales y aislamiento de dependencias](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md), el tema «Dependencias de proyecto y herramientas» importa porque runtime, dependencias de ejecución, desarrollo y herramientas globales tienen ciclos distintos.

## Cómo funciona

Según [SE-103 — Entornos virtuales y aislamiento de dependencias](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md), en la sección «Dependencias de proyecto y herramientas»:

Runtime, dependencias de ejecución, desarrollo y herramientas globales tienen ciclos distintos. Mezclarlas amplía superficie. El manifest declara intención y el lock o resolución registra selección; un freeze indiscriminado puede incluir paquetes ajenos.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-103 — Entornos virtuales y aislamiento de dependencias](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md):

En el entorno reproducible de diagnóstico, una investigación conserva síntoma, entorno, reproducción, hipótesis, observaciones, causa, corrección y regresión. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-103 — Entornos virtuales y aislamiento de dependencias](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md)) son:

- **Funciona aquí y no en otra máquina** — causa: dependencia no declarada presente en el sistema. Corrección: probar siempre en un entorno vacío.
- **El entorno deja de funcionar al moverlo** — causa: rutas absolutas. Corrección: recrearlo desde su definición.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-103 — Entornos virtuales y aislamiento de dependencias](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md)) son: Las definiciones son operativas para el entorno reproducible de diagnóstico. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. El venv comparte sistema operativo y toolchain nativa. La siguiente clase encapsula un entorno de desarrollo desechable sin afirmar reproducibilidad absoluta.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Ciclo](../c/ciclo.md), [Dependencia](./dependencia.md), [Herramientas](../h/herramientas.md), [Runtime](../r/runtime.md), [Activación y ejecutable explícito](../a/activacion-y-ejecutable-explicito.md), [Entorno virtual](../e/entorno-virtual.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-103 — Entornos virtuales y aislamiento de dependencias](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

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

[↑ Glosario](../../README.md) · [← Dependencia transitiva](./dependencia-transitiva.md) · [Dependencias y distribución →](./dependencias-y-distribucion.md)
