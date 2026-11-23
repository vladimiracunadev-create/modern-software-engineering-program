# Resolución por path

[↑ Glosario](../../README.md) · [← Resolución de un oráculo](./resolucion-de-un-oraculo.md) · [Resolución y backtracking →](./resolucion-y-backtracking.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

El shell busca ejecutables según path, alias, launcher o shim.

Definición de trabajo de [SE-102 — Gestores de versiones de runtimes](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md).

## Por qué importa

En [SE-102 — Gestores de versiones de runtimes](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md), el tema «Resolución por PATH» importa porque el shell busca ejecutables según PATH, alias, launcher o shim.

## Cómo funciona

Según [SE-102 — Gestores de versiones de runtimes](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md), en la sección «Resolución por PATH»:

El shell busca ejecutables según PATH, alias, launcher o shim. `python` puede cambiar por terminal y directorio. Registrar ruta absoluta observada ayuda a diagnosticar; hardcodearla en el proyecto reduce portabilidad.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-102 — Gestores de versiones de runtimes](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md):

En el entorno reproducible de diagnóstico, una investigación conserva síntoma, entorno, reproducción, hipótesis, observaciones, causa, corrección y regresión. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-102 — Gestores de versiones de runtimes](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md)) son:

- **El script usa otro Python en otra máquina** — causa: se invoca `python` a secas. Corrección: declarar la versión y verificarla al inicio.
- **La medición no se repite en otro equipo** — causa: compilación o sistema distintos. Corrección: registrar versión y sistema con cada medición.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-102 — Gestores de versiones de runtimes](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md)) son: Las definiciones son operativas para el entorno reproducible de diagnóstico. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Fijar runtime no aísla paquetes instalados. La siguiente clase explica entornos virtuales, resolución y frontera con herramientas globales.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Alias](../a/alias.md), [Shell](../s/shell.md), [Actualización y rollback](../a/actualizacion-y-rollback.md), [Compatibilidad y sintaxis](../c/compatibilidad-y-sintaxis.md), [Gestor de versiones](../g/gestor-de-versiones.md), [Runtime e implementación](./runtime-e-implementacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-102 — Gestores de versiones de runtimes](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

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

[↑ Glosario](../../README.md) · [← Resolución de un oráculo](./resolucion-de-un-oraculo.md) · [Resolución y backtracking →](./resolucion-y-backtracking.md)
