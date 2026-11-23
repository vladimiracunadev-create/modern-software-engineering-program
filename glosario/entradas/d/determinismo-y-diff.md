# Determinismo y diff

[↑ Glosario](../../README.md) · [← Determinismo de una prueba](./determinismo-de-una-prueba.md) · [Deuda →](./deuda.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

Misma entrada, versión y entorno deben producir salida equivalente.

Definición de trabajo de [SE-116 — Generación de código y metaprogramación](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md).

## Por qué importa

En [SE-116 — Generación de código y metaprogramación](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md), el tema «Determinismo y diff» importa porque misma entrada, versión y entorno deben producir salida equivalente.

## Cómo funciona

Según [SE-116 — Generación de código y metaprogramación](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md), en la sección «Determinismo y diff»:

Misma entrada, versión y entorno deben producir salida equivalente. Orden estable, timestamps controlados y formatter fijado reducen ruido. CI regenera y falla si hay diff, revelando fuentes o derivados desactualizados.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-116 — Generación de código y metaprogramación](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md):

En el producto reutilizable con SDK y CLI, un release contiene contrato público, artefactos inmutables, dependencias, procedencia, ejemplos, errores y ruta de migración. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-116 — Generación de código y metaprogramación](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md)) son:

- **El CI marca diferencias en archivos generados que nadie tocó** — causa: el generador depende de reloj, orden o ruta. Corrección: ordenar entradas, quitar marcas de tiempo y usar rutas relativas.
- **Alguien editó el archivo generado y se perdió al regenerar** — causa: no hay encabezado ni verificación. Corrección: encabezado «no editar», regeneración en CI y `git diff --exit-code`.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-116 — Generación de código y metaprogramación](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md)) son: Las definiciones son operativas para el producto reutilizable con SDK y CLI. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. La generación legalmente reutilizable depende de licencias y procedencia de entradas y plantillas. La siguiente clase hace esas obligaciones visibles y verificables.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Entorno](../e/entorno.md), [Versión](../v/version.md), [Escape hatch y ownership](../e/escape-hatch-y-ownership.md), [Fuente de verdad y transformación](../f/fuente-de-verdad-y-transformacion.md), [Metaprogramación](../m/metaprogramacion.md), [Plantillas y ast](../p/plantillas-y-ast.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-116 — Generación de código y metaprogramación](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.

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

[↑ Glosario](../../README.md) · [← Determinismo de una prueba](./determinismo-de-una-prueba.md) · [Deuda →](./deuda.md)
