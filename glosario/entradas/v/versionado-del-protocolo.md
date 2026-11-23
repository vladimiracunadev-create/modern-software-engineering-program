# Versionado del protocolo

[↑ Glosario](../../README.md) · [← Versionado](./versionado.md) · [Versionado semántico →](./versionado-semantico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

Host y plugin negocian versión/capacidades antes de ejecutar.

Definición de trabajo de [SE-115 — Plugins, extensiones y puntos de integración](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md).

## Por qué importa

En [SE-115 — Plugins, extensiones y puntos de integración](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md), el tema «Versionado del protocolo» importa porque host y plugin negocian versión/capacidades antes de ejecutar.

## Cómo funciona

Según [SE-115 — Plugins, extensiones y puntos de integración](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md), en la sección «Versionado del protocolo»:

Host y plugin negocian versión/capacidades antes de ejecutar. Una versión del paquete no basta si existen contratos independientes. Incompatibilidad produce error accionable y no corrupción silenciosa.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-115 — Plugins, extensiones y puntos de integración](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md):

En el producto reutilizable con SDK y CLI, un release contiene contrato público, artefactos inmutables, dependencias, procedencia, ejemplos, errores y ruta de migración. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-115 — Plugins, extensiones y puntos de integración](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md)) son:

- **La aplicación no arranca porque un plugin no se importa** — causa: carga ansiosa sin aislamiento. Corrección: cargar por plugin con `try/except`, registrar y continuar.
- **El arranque tarda más cuanto más plugins hay instalados** — causa: se cargan todos aunque se use uno. Corrección: descubrir los nombres y cargar solo el solicitado.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-115 — Plugins, extensiones y puntos de integración](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md)) son: Las definiciones son operativas para el producto reutilizable con SDK y CLI. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Un protocolo reduce acoplamiento, no hace seguro código arbitrario. La siguiente clase estudia generación y metaprogramación como transformaciones que requieren fuente de verdad y diff.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Capacidad](../c/capacidad.md), [Complemento](../c/complemento.md), [Versión](./version.md), [Capacidades y aislamiento](../c/capacidades-y-aislamiento.md), [Descubrimiento](../d/descubrimiento.md), [Fallo y desactivación](../f/fallo-y-desactivacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-115 — Plugins, extensiones y puntos de integración](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.

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

[↑ Glosario](../../README.md) · [← Versionado](./versionado.md) · [Versionado semántico →](./versionado-semantico.md)
