# SBOM

[↑ Glosario](../../README.md) · [← Saturación](./saturacion.md) · [SDD →](./sdd.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Lista estructurada de los componentes de un artefacto, con identificador, versión y huella.

Definición de trabajo de [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md).

## Por qué importa

En [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), el tema «SBOM y sus campos» importa porque es el vocabulario común para responder «¿estamos afectados?».

## Cómo funciona

Según [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md):

Un **SBOM** (*software bill of materials*) es una lista estructurada de los componentes de un artefacto con los datos suficientes para identificarlos: nombre, versión, un identificador uniforme (como el *Package URL*, que codifica ecosistema, nombre y versión), la huella de su contenido, la licencia, y las relaciones de dependencia entre ellos. Los formatos más usados son CycloneDX y SPDX; ambos son JSON o similares legibles por máquina. Los elementos mínimos que fijó la NTIA en 2021 incluyen quién lo produjo y cuándo, porque un SBOM sin autor ni fecha no puede evaluarse. Su utilidad inmediata es responder a un aviso: dado el identificador de una pieza vulnerable, buscar en los SBOM de todos los productos cuáles la contienen.

Según [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md):

El CI de la API de entregas genera el SBOM a partir del bloqueo y del contenido del artefacto final (escaneo de los archivos copiados en `third_party/`), y escribe una procedencia con el commit, el identificador del trabajo de construcción, el hash del bloqueo y la huella del artefacto. Ambos documentos tienen como sujeto la huella del artefacto y se almacenan junto a él como metadatos (`SE-470`). El verificador del despliegue calcula la huella, busca las atestaciones, comprueba que el constructor y el repositorio coinciden con los valores esperados que la política fija de antemano, que el SBOM no contiene componentes de una lista de prohibidos y que la procedencia corresponde a la rama protegida.

## Ejemplo

Ejemplo de [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) (sección «Ejemplo mínimo»):

El fragmento genera un SBOM mínimo desde dos líneas de un archivo de bloqueo y lo liga a una huella. Antes de ejecutarlo, predice qué cambia si se modifica un byte del artefacto.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El SBOM no contiene una pieza que está en el artefacto** — causa: generado desde el manifiesto. Corrección: generar desde el bloqueo y escanear el artefacto final. ([SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md))
- **Un SBOM válido describe otro artefacto** — causa: sin vínculo por huella. Corrección: sujeto identificado por la huella del artefacto. ([SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md))
- **Un SBOM bien formado contiene un componente falso** — causa: solo se valida la forma. Corrección: comparar con el contenido real del artefacto. ([SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **SBOM** (*software bill of materials*) es una lista estructurada de los componentes de un artefacto con los datos suficientes para identificarlos: nombre, versión, un identificador uniforme (como el *Package URL*, que codifica ecosistema, nombre y versión), la huella de su contenido, la licencia, y las relaciones de dependencia entre ellos. ([SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md))
- **un SBOM generado desde el manifiesto que no contiene la pieza vulnerable**. ([SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Artefacto](../a/artefacto.md), [Componente](../c/componente.md), [Huella](../h/huella.md), [Versión](../v/version.md), [Atestación](../a/atestacion.md), [Package URL](../p/package-url.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (19 clases más lo mencionan; las que más):

[SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), [SE-117](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md), [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md), [SE-108](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md), [SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NTIA: elementos mínimos de un SBOM](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom) — datos mínimos; autoridad: Administración Nacional de Telecomunicaciones e Información de EE. UU.
- [CycloneDX: visión general de la especificación](https://cyclonedx.org/specification/overview/) — formato de lista de materiales; autoridad: proyecto CycloneDX, OWASP.
- [SPDX 2.3](https://spdx.github.io/spdx-spec/v2.3/) — formato alternativo normalizado; autoridad: proyecto SPDX, Linux Foundation.
- [SLSA v1.0: procedencia](https://slsa.dev/spec/v1.0/provenance) — contenido de una procedencia; autoridad: proyecto SLSA, OpenSSF.
- [in-toto: declaración (Statement)](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md) — atestaciones ligadas a un sujeto; autoridad: proyecto in-toto.

---

[↑ Glosario](../../README.md) · [← Saturación](./saturacion.md) · [SDD →](./sdd.md)
