# Plan y dry-run

[↑ Glosario](../../README.md) · [← Plan de salida](./plan-de-salida.md) · [Plan-and-execute →](./plan-and-execute.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

Mostrar cambios antes de aplicarlos mejora revisión, siempre que use la misma lógica de decisión.

Definición de trabajo de [SE-114 — Scripting repetible y tareas idempotentes](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md).

## Por qué importa

En [SE-114 — Scripting repetible y tareas idempotentes](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), el tema «Plan y dry-run» importa porque mostrar cambios antes de aplicarlos mejora revisión, siempre que use la misma lógica de decisión.

## Cómo funciona

Según [SE-114 — Scripting repetible y tareas idempotentes](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), en la sección «Plan y dry-run»:

Mostrar cambios antes de aplicarlos mejora revisión, siempre que use la misma lógica de decisión. Un dry-run que omite permisos o resolución externa no garantiza éxito. Se etiqueta qué no puede simular.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-114 — Scripting repetible y tareas idempotentes](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md):

En el producto reutilizable con SDK y CLI, un release contiene contrato público, artefactos inmutables, dependencias, procedencia, ejemplos, errores y ruta de migración. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-114 — Scripting repetible y tareas idempotentes](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md)) son:

- **Al repetir el script el archivo de configuración crece** — causa: se añade en vez de asegurar. Corrección: leer el estado, comparar y escribir solo si difiere.
- **`FileExistsError` al reintentar tras un fallo** — causa: `mkdir` o creación sin tolerar existencia. Corrección: `exist_ok=True` y una comprobación del estado deseado.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-114 — Scripting repetible y tareas idempotentes](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md)) son: Las definiciones son operativas para el producto reutilizable con SDK y CLI. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. La automatización administra capacidades conocidas. La siguiente clase permite extensiones de terceros sin entregarles accidentalmente toda la autoridad del proceso.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Revisión](../r/revision.md), [Idempotencia](../i/idempotencia.md), [Journal y rollback](../j/journal-y-rollback.md), [Precondición y postcondición](./precondicion-y-postcondicion.md), [Retry y operaciones inciertas](../r/retry-y-operaciones-inciertas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-114 — Scripting repetible y tareas idempotentes](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) — Api pública, versiones, prereleases y compatibilidad declarada; autoridad: Semantic Versioning project.
- [Python Packaging User Guide: Specifications](https://packaging.python.org/en/latest/specifications/) — Metadata, nombres, versiones, dependencias y artefactos de distribución; autoridad: Python Packaging Authority.
- [pylock.toml Specification](https://packaging.python.org/en/latest/specifications/pylock-toml/) — Lock files para instalaciones reproducibles y selección por entorno; autoridad: Python Packaging Authority.
- [Python Standard Library](https://docs.python.org/3/library/index.html) — Argparse, importlib.metadata, subprocess y apis de automatización; autoridad: Python Software Foundation.
- [SPDX Specification 3.0](https://spdx.dev/use/specifications/) — Identificadores, sbom y procedencia legible por máquinas; autoridad: Linux Foundation.

---

[↑ Glosario](../../README.md) · [← Plan de salida](./plan-de-salida.md) · [Plan-and-execute →](./plan-and-execute.md)
