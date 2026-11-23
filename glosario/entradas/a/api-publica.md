# API pública

[↑ Glosario](../../README.md) · [← API gateway](./api-gateway.md) · [Api y cli coherentes →](./api-y-cli-coherentes.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

La api incluye nombres, tipos, errores, efectos, orden, formato y comportamiento documentado que consumidores pueden depender.

Definición de trabajo de [SE-110 — SemVer, compatibilidad y contratos públicos](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-474 — Versionado, compatibilidad y changelog](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md): Conjunto de interfaces y comportamientos que un proyecto promete mantener.

## Por qué importa

En [SE-110 — SemVer, compatibilidad y contratos públicos](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md), el tema «API pública» importa porque la API incluye nombres, tipos, errores, efectos, orden, formato y comportamiento documentado que consumidores pueden depender.

## Cómo funciona

Según [SE-110 — SemVer, compatibilidad y contratos públicos](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md), en la sección «API pública»:

La API incluye nombres, tipos, errores, efectos, orden, formato y comportamiento documentado que consumidores pueden depender. No se limita a funciones exportadas. CLI, archivos, variables y mensajes parseados también forman contratos si se presentan como estables.

## Ejemplo

Ejemplo de [SE-474 — Versionado, compatibilidad y changelog](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md) (sección «Ejemplo profesional»):

El equipo escribe una política de versionado de la API de entregas: la API pública son los puntos finales documentados, sus parámetros, sus campos de respuesta, sus códigos de error y el orden de los listados cuando está especificado; el comportamiento no documentado no se promete. Cada solicitud de integración ejecuta el comparador de firmas y las pruebas de contrato, y quien revisa elige el nivel; si hay discrepancia, gana el mayor. Una funcionalidad deprecada emite un aviso en tiempo de ejecución desde la versión que la marca hasta la que la retira, con un mínimo de dos versiones menores y seis meses.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El número de versión no dice nada** — causa: API pública no definida. Corrección: declarar la API pública y lo que no se promete. ([SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una versión puede ser válida y aun así no comunicar nada si el autor no define qué es su API pública. ([SE-110](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md))
- El **versionado semántico** asigna significado a los tres números de una versión: el **mayor** sube cuando hay cambios incompatibles de la API pública, el **menor** cuando se añade funcionalidad compatible y el **parche** cuando se corrige un error sin cambiar la API. ([SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Conjunto](../c/conjunto.md), [Efecto](../e/efecto.md), [Interfaz](../i/interfaz.md), [Tipo](../t/tipo.md), [Cambio incompatible](../c/cambio-incompatible.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-110 — SemVer, compatibilidad y contratos públicos](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.
- [SE-474 — Versionado, compatibilidad y changelog](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (21 clases más lo mencionan; las que más):

[SE-112](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-112-paquetes-modulos-y-publicacion/README.md), [SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md), [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), [SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md), [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md), [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md), [SE-111](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md).

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

[↑ Glosario](../../README.md) · [← API gateway](./api-gateway.md) · [Api y cli coherentes →](./api-y-cli-coherentes.md)
