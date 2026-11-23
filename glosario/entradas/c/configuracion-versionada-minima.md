# Configuración versionada mínima

[↑ Glosario](../../README.md) · [← Configuración por capas](./configuracion-por-capas.md) · [Configuración y precedencia →](./configuracion-y-precedencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

Se versionan manifest, lock cuando aplica, contenedor y configuración compartible del editor.

Definición de trabajo de [SE-108 — Proyecto: entorno de desarrollo autocontenido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md).

## Por qué importa

En [SE-108 — Proyecto: entorno de desarrollo autocontenido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md), el tema «Configuración versionada mínima» importa porque se versionan manifest, lock cuando aplica, contenedor y configuración compartible del editor.

## Cómo funciona

Según [SE-108 — Proyecto: entorno de desarrollo autocontenido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md), en la sección «Configuración versionada mínima»:

Se versionan manifest, lock cuando aplica, contenedor y configuración compartible del editor. Se excluyen tokens, rutas locales y preferencias no necesarias. Un default ayuda, pero existe ruta CLI independiente del IDE.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-108 — Proyecto: entorno de desarrollo autocontenido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md):

En el entorno reproducible de diagnóstico, una investigación conserva síntoma, entorno, reproducción, hipótesis, observaciones, causa, corrección y regresión. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-108 — Proyecto: entorno de desarrollo autocontenido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md)) son:

- **El entorno no se reconstruye en otra máquina** — causa: pasos manuales no documentados. Corrección: un comando que recree todo, probado desde cero.
- **Los hashes de la rueda cambian entre construcciones** — causa: marcas de tiempo en el archivo. Corrección: fijar el archivo instalado, no reconstruirlo.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-108 — Proyecto: entorno de desarrollo autocontenido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md)) son: Las definiciones son operativas para el entorno reproducible de diagnóstico. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. El entorno reduce variabilidad conocida, no congela hardware, red o servicios externos. La [Parte 9](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md) convertirá la capacidad de la biblioteca de estructuras y algoritmos en una biblioteca, paquete, SDK y CLI con contratos públicos y compatibilidad verificable.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Bloqueo](../b/bloqueo.md), [Contenedor](./contenedor.md), [Contrato de bootstrap](./contrato-de-bootstrap.md), [Criterio de aceptación](./criterio-de-aceptacion.md), [Diagnóstico incorporado](../d/diagnostico-incorporado.md), [Limpieza y recuperación](../l/limpieza-y-recuperacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-108 — Proyecto: entorno de desarrollo autocontenido](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

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

[↑ Glosario](../../README.md) · [← Configuración por capas](./configuracion-por-capas.md) · [Configuración y precedencia →](./configuracion-y-precedencia.md)
