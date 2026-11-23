# Package URL

[↑ Glosario](../../README.md) · [← PaaS](./paas.md) · [Pagador, usuario y decisor →](./pagador-usuario-y-decisor.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Identificador uniforme de un paquete que codifica ecosistema, nombre y versión.

Definición de trabajo de [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md).

## Por qué importa

La clase donde se define, [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), existe con este propósito: la clase existe para que puedas entregar, junto con un artefacto, dos documentos que otra persona pueda leer sin confiar en ti:

## Cómo funciona

Según [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md):

Un **SBOM** (*software bill of materials*) es una lista estructurada de los componentes de un artefacto con los datos suficientes para identificarlos: nombre, versión, un identificador uniforme (como el *Package URL*, que codifica ecosistema, nombre y versión), la huella de su contenido, la licencia, y las relaciones de dependencia entre ellos. Los formatos más usados son CycloneDX y SPDX; ambos son JSON o similares legibles por máquina. Los elementos mínimos que fijó la NTIA en 2021 incluyen quién lo produjo y cuándo, porque un SBOM sin autor ni fecha no puede evaluarse. Su utilidad inmediata es responder a un aviso: dado el identificador de una pieza vulnerable, buscar en los SBOM de todos los productos cuáles la contienen.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md):

El CI de la API de entregas genera el SBOM a partir del bloqueo y del contenido del artefacto final (escaneo de los archivos copiados en `third_party/`), y escribe una procedencia con el commit, el identificador del trabajo de construcción, el hash del bloqueo y la huella del artefacto. Ambos documentos tienen como sujeto la huella del artefacto y se almacenan junto a él como metadatos (`SE-470`).

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Nadie puede usar el SBOM** — causa: faltan autor, fecha o identificadores. Corrección: cumplir los elementos mínimos y usar purl. ([SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **SBOM** (*software bill of materials*) es una lista estructurada de los componentes de un artefacto con los datos suficientes para identificarlos: nombre, versión, un identificador uniforme (como el *Package URL*, que codifica ecosistema, nombre y versión), la huella de su contenido, la licencia, y las relaciones de dependencia entre ellos. ([SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Paquete](./paquete.md), [Versión](../v/version.md), [Atestación](../a/atestacion.md), [Procedencia](./procedencia.md), [SBOM](../s/sbom.md), [Sujeto](../s/sujeto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «purl».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Package URL](https://github.com/package-url/purl-spec) — identificador uniforme de paquetes; autoridad: proyecto purl-spec.
- [CycloneDX: visión general de la especificación](https://cyclonedx.org/specification/overview/) — formato de lista de materiales; autoridad: proyecto CycloneDX, OWASP.
- [SPDX 2.3](https://spdx.github.io/spdx-spec/v2.3/) — formato alternativo normalizado; autoridad: proyecto SPDX, Linux Foundation.
- [NTIA: elementos mínimos de un SBOM](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom) — datos mínimos; autoridad: Administración Nacional de Telecomunicaciones e Información de EE. UU.
- [SLSA v1.0: procedencia](https://slsa.dev/spec/v1.0/provenance) — contenido de una procedencia; autoridad: proyecto SLSA, OpenSSF.

---

[↑ Glosario](../../README.md) · [← PaaS](./paas.md) · [Pagador, usuario y decisor →](./pagador-usuario-y-decisor.md)
