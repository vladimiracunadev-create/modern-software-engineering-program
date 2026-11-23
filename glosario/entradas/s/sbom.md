# SBOM

[↑ Glosario](../../README.md) · [← Saturación](./saturacion.md) · [SDD →](./sdd.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Un **SBOM** (*software bill of materials*, lista de materiales de software) es una lista estructurada de los componentes de un artefacto, con identificador, versión y huella. Es la definición de [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), que trabaja con un esquema simplificado inspirado en CycloneDX.

## Por qué importa

Responde «¿qué hay dentro de este artefacto?» sin abrirlo y permite saber si una vulnerabilidad en un componente afecta a un artefacto publicado. Es una pieza de la cadena de suministro: junto con la procedencia, dice qué se entregó y cómo se construyó.

## Cómo funciona

Cada componente se identifica con un identificador y una versión ([SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) recomienda usar *purl*) y con una huella. El SBOM debe cumplir los elementos mínimos (autor, fecha, identificadores) para ser utilizable. Lo que lo hace confiable es su vínculo con el artefacto real: se identifica el sujeto por la huella del artefacto, y se genera desde el bloqueo de dependencias y se contrasta escaneando el artefacto final, no desde el manifiesto.

## Ejemplo

[SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) trabaja con 100 proyectos sintéticos cuyos componentes se reparten, por supuesto del autor, en 62 % declarados, 24 % transitivos, 7 % copiados, 4 % enlazados y 3 % descargados en ejecución. Las categorías copiada, enlazada y descargada no aparecen en un manifiesto, por lo que un SBOM generado solo desde el manifiesto queda incompleto.

## Errores y confusiones comunes

- **El SBOM no contiene una pieza que está en el artefacto.** Se generó desde el manifiesto; hay que generarlo desde el bloqueo y escanear el artefacto final.
- **Un SBOM válido describe otro artefacto.** Falta el vínculo por huella.
- **Un SBOM bien formado con un componente falso.** Solo se validó la forma; hay que comparar con el contenido real.
- **Nadie puede usarlo.** Faltan autor, fecha o identificadores; cumplir los elementos mínimos y usar purl.

## Límites y cuándo no aplica

[SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) declara que su SBOM sigue un esquema simplificado inspirado en CycloneDX y que las procedencias son documentos propios con campos cercanos a SLSA e in-toto, no los formatos completos; los 100 proyectos y su composición son supuestos del autor, y no se usó ninguna herramienta generadora de SBOM ni base de vulnerabilidades. Un SBOM describe composición, no seguridad: no dice si un componente es vulnerable ni si fue construido con garantías.

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
