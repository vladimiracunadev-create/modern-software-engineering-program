# Artefacto e instalación

[↑ Glosario](../../README.md) · [← Artefacto de verificación](./artefacto-de-verificacion.md) · [Artefacto inmutable →](./artefacto-inmutable.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

Se construyen sdist y wheel, inspeccionan contenidos y se instalan en venv limpio.

Definición de trabajo de [SE-119 — Taller: empaquetar una capacidad reusable](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md).

## Por qué importa

En [SE-119 — Taller: empaquetar una capacidad reusable](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md), el tema «Artefacto e instalación» importa porque se construyen sdist y wheel, inspeccionan contenidos y se instalan en venv limpio.

## Cómo funciona

Según [SE-119 — Taller: empaquetar una capacidad reusable](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md), en la sección «Artefacto e instalación»:

Se construyen sdist y wheel, inspeccionan contenidos y se instalan en venv limpio. Ejecutar desde checkout no cuenta. Los hashes del artefacto se conservan para comparar lo probado con lo entregado.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-119 — Taller: empaquetar una capacidad reusable](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md):

En el producto reutilizable con SDK y CLI, un release contiene contrato público, artefactos inmutables, dependencias, procedencia, ejemplos, errores y ruta de migración. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-119 — Taller: empaquetar una capacidad reusable](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md)) son:

- **El paquete instalado no encuentra su archivo de datos** — causa: falta `package-data`. Corrección: declararlo y comparar `namelist()` con una lista esperada.
- **`ModuleNotFoundError` solo en un entorno limpio** — causa: dependencia usada pero no declarada. Corrección: declararla en `dependencies` y ejecutar la prueba de humo en un entorno vacío.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-119 — Taller: empaquetar una capacidad reusable](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md)) son: Las definiciones son operativas para el producto reutilizable con SDK y CLI. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. El taller verifica una versión y un entorno principal. El proyecto siguiente construye una matriz de compatibilidad, plugin, automatización y procedencia para SDK+CLI.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Sdist y wheel](../s/sdist-y-wheel.md), [Api y cli coherentes](./api-y-cli-coherentes.md), [Cambio compatible](../c/cambio-compatible.md), [Diseño desde consumidor](../d/diseno-desde-consumidor.md), [Slice reusable](../s/slice-reusable.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-119 — Taller: empaquetar una capacidad reusable](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.

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

[↑ Glosario](../../README.md) · [← Artefacto de verificación](./artefacto-de-verificacion.md) · [Artefacto inmutable →](./artefacto-inmutable.md)
