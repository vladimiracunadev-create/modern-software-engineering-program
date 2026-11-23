# Desechabilidad y persistencia

[↑ Glosario](../../README.md) · [← Desechabilidad](./desechabilidad.md) · [Desfase de reloj →](./desfase-de-reloj.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

El contenedor debe poder borrarse sin perder código; volúmenes persistentes se enumeran y limpian con cuidado.

Definición de trabajo de [SE-104 — Dev Containers y entornos desechables](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md).

## Por qué importa

En [SE-104 — Dev Containers y entornos desechables](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md), el tema «Desechabilidad y persistencia» importa porque el contenedor debe poder borrarse sin perder código; volúmenes persistentes se enumeran y limpian con cuidado.

## Cómo funciona

Según [SE-104 — Dev Containers y entornos desechables](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md), en la sección «Desechabilidad y persistencia»:

El contenedor debe poder borrarse sin perder código; volúmenes persistentes se enumeran y limpian con cuidado. Datos importantes viven en repositorio o backup explícito. `funciona en mi contenedor` sigue siendo local si nadie puede reconstruirlo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-104 — Dev Containers y entornos desechables](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md):

En el entorno reproducible de diagnóstico, una investigación conserva síntoma, entorno, reproducción, hipótesis, observaciones, causa, corrección y regresión. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-104 — Dev Containers y entornos desechables](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md)) son:

- **`docker` responde pero no se puede ejecutar nada** — causa: el motor no está en marcha. Corrección: verificar el servidor con `docker info`.
- **La imagen cambia sin que el repositorio cambie** — causa: etiqueta mutable. Corrección: fijar el digest.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-104 — Dev Containers y entornos desechables](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md)) son: Las definiciones son operativas para el entorno reproducible de diagnóstico. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Un contenedor estable no reduce automáticamente un fallo. La siguiente clase aplica delta debugging manual y control de variables para obtener un caso mínimo.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Contenedor](../c/contenedor.md), [Contenedor de desarrollo](../c/contenedor-de-desarrollo.md), [Imagen, tag y digest](../i/imagen-tag-y-digest.md), [Lifecycle y caché](../l/lifecycle-y-cache.md), [Workspace, mounts y permisos](../w/workspace-mounts-y-permisos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-104 — Dev Containers y entornos desechables](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

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

[↑ Glosario](../../README.md) · [← Desechabilidad](./desechabilidad.md) · [Desfase de reloj →](./desfase-de-reloj.md)
