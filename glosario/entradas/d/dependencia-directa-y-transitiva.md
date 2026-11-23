# Dependencia directa y transitiva

[↑ Glosario](../../README.md) · [← Dependencia directa](./dependencia-directa.md) · [Dependencia externa →](./dependencia-externa.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

El manifest declara relaciones directas; cada paquete añade transitivas.

Definición de trabajo de [SE-111 — Resolución de dependencias y lockfiles](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md).

## Por qué importa

En [SE-111 — Resolución de dependencias y lockfiles](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md), el tema «Dependencia directa y transitiva» importa porque el manifest declara relaciones directas; cada paquete añade transitivas.

## Cómo funciona

Según [SE-111 — Resolución de dependencias y lockfiles](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md), en la sección «Dependencia directa y transitiva»:

El manifest declara relaciones directas; cada paquete añade transitivas. El grafo final, no la lista superior, determina superficie. Importar algo disponible solo transitivamente crea dependencia implícita que puede desaparecer cuando el padre cambia.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-111 — Resolución de dependencias y lockfiles](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md):

En el producto reutilizable con SDK y CLI, un release contiene contrato público, artefactos inmutables, dependencias, procedencia, ejemplos, errores y ruta de migración. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-111 — Resolución de dependencias y lockfiles](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md)) son:

- **La instalación de ayer y la de hoy dan versiones distintas** — causa: dependencia sin fijar y un lanzamiento nuevo en el índice. Corrección: fijar con `==` y archivo generado; actualizar de forma deliberada.
- **`ResolutionImpossible` al añadir una librería nueva** — causa: dos restricciones incompatibles sobre la misma transitiva. Corrección: leer el mensaje, ceder una restricción o elegir otra versión de la librería.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-111 — Resolución de dependencias y lockfiles](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md)) son: Las definiciones son operativas para el producto reutilizable con SDK y CLI. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Resolver dependencias no produce un artefacto publicable ni garantiza que contenga lo esperado. La siguiente clase construye paquete, distribuciones y publicación verificable.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Paquete](../p/paquete.md), [Relación](../r/relacion.md), [Integridad y dependency confusion](../i/integridad-y-dependency-confusion.md), [Lockfile](../l/lockfile.md), [Resolución](../r/resolucion.md), [Restricciones y marcadores](../r/restricciones-y-marcadores.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-111 — Resolución de dependencias y lockfiles](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), [SE-201](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md), [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md).

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

[↑ Glosario](../../README.md) · [← Dependencia directa](./dependencia-directa.md) · [Dependencia externa →](./dependencia-externa.md)
