# Supply chain mínima

[↑ Glosario](../../README.md) · [← Suposición](./suposicion.md) · [Supresión →](./supresion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

La **supply chain mínima** (cadena de suministro de software, en su versión mínima) es, en el proyecto de [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md), el conjunto básico de prácticas para que un *release* sea inspeccionable: **las dependencias y las licencias se inventarían, las fuentes se fijan según una política y se genera metadata de procedencia y SBOM** cuando está disponible. El adjetivo «mínima» es explícito: no equivale a una cadena de suministro completa y segura, pero **hace visibles los componentes y las decisiones** que de otro modo quedan implícitas. Es un término propio del programa para delimitar lo exigible en un proyecto de este alcance.

## Por qué importa

Un paquete publicado incorpora código de terceros: sus dependencias directas, las transitivas, las herramientas de construcción. Si nadie sabe cuáles son, tampoco se puede responder a preguntas básicas: ¿incluimos la biblioteca afectada por esa vulnerabilidad?, ¿las licencias son compatibles con la nuestra?, ¿de dónde vino cada componente? La decisión que cambia es qué se entrega con el artefacto: no solo el código, también el inventario de lo que contiene. Sin él, la respuesta a un incidente empieza por averiguar qué hay dentro.

## Cómo funciona

Tres elementos, cada uno con su causa:

- **Inventario de dependencias y licencias:** la lista de todo lo que el producto incluye (directas y transitivas), con su versión y licencia. Permite revisar licencias y buscar vulnerabilidades conocidas.
- **Fuentes fijadas según política:** de dónde se obtienen las dependencias (qué índice o repositorio) y con qué versión exacta (un archivo de bloqueo con versiones y, idealmente, hashes). Evita que una instalación posterior traiga algo distinto o que un nombre de paquete se resuelva desde una fuente no prevista.
- **Metadata de procedencia y SBOM:** el **SBOM** (*Software Bill of Materials*) es la lista estructurada de componentes en un formato estándar; la **procedencia** (*provenance*) registra cómo y dónde se construyó el artefacto. Se generan **cuando están disponibles** en el ecosistema y la herramienta.

Esta disciplina es *mínima*: no incluye, por ejemplo, firma de artefactos con verificación por parte del consumidor, construcciones reproducibles verificadas ni auditoría del código de terceros. Lo que sí hace es que la superficie de dependencia sea **visible y versionada**, el primer paso para gestionarla.

## Ejemplo

Para el release del SDK del programa, el repositorio incluye (ilustración):

```text
requirements.lock        versiones exactas con hashes (fuente: índice oficial según política)
THIRD_PARTY_LICENSES.md  dependencia, versión, licencia
dist/sbom.cdx.json       SBOM del artefacto (formato estándar)
dist/provenance.json     cómo y desde qué commit se construyó
```

Un script de integración continua falla si aparece una dependencia sin licencia declarada o fuera de la lista permitida, y si el archivo de bloqueo difiere del instalado. Con esto, cuando se anuncia una vulnerabilidad en una biblioteca, la consulta «¿la tenemos?» se resuelve buscando en el SBOM en lugar de revisar el repositorio a mano.

## Errores y confusiones comunes

- **Confundir «mínima» con «segura».** Visibilidad no es protección.
- **Fijar solo las dependencias directas.** Las transitivas también entran al artefacto.
- **No fijar la fuente.** El mismo nombre puede resolverse en otro índice.
- **Generar el SBOM una vez y no actualizarlo.** Deja de reflejar el artefacto.

## Límites y cuándo no aplica

El proyecto acredita un release candidato dentro de su matriz, no disponibilidad, seguridad ni soporte productivo ([SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md)). Un SBOM dice qué hay, no si es seguro ni si se usa. Para un script personal sin dependencias externas, el inventario es trivial. Y las exigencias reales de un producto con requisitos regulatorios o de alto riesgo van mucho más allá de este mínimo.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Dependencia](../d/dependencia.md), [Procedencia](../p/procedencia.md), [SBOM](./sbom.md), [Aceptación desde el consumidor](../a/aceptacion-desde-el-consumidor.md), [Contrato multicapa](../c/contrato-multicapa.md), [Matriz de compatibilidad](../m/matriz-de-compatibilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-120 — Proyecto: SDK y CLI con compatibilidad verificada](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.

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

[↑ Glosario](../../README.md) · [← Suposición](./suposicion.md) · [Supresión →](./supresion.md)
