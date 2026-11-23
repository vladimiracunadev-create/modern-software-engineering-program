# Caso coherente

[↑ Glosario](../../README.md) · [← Caso base](./caso-base.md) · [Caso de abuso →](./caso-de-abuso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Release maliciosa o dudosa que supera todas las comprobaciones porque su evidencia es consistente.

Definición de trabajo de [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md).

## Por qué importa

La clase donde se define, [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), existe con este propósito: el taller existe para que ejecutes, de principio a fin y con tus manos, la pregunta que justifica toda la [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md):

## Cómo funciona

Según [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md):

La **reconstrucción independiente** toma la fuente revisada, la construye con las entradas declaradas en un entorno que no es el del constructor y compara la huella con la del release. Si coincide, el artefacto procede de esa fuente; si difiere, hay una manipulación del proceso o una entrada no declarada (y se vuelve a `SE-469` para localizarla). Es la única comprobación que ata el artefacto a la fuente sin confiar en el constructor, y por eso convierte en discrepancia visible el primer caso coherente: si el código malicioso no está en la fuente revisada, la reconstrucción desde esa fuente no coincide con el release. Tiene un límite que el taller exhibe: si la fuente es la maliciosa, la reconstrucción coincide y confirma con exactitud el daño.

Según [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md):

Traslada el taller a otro release (una imagen de contenedor firmada, un paquete de un índice, un firmware): cambia el formato de los documentos y las herramientas de verificación y conserva el procedimiento de fijar valores esperados, recorrer la cadena de huellas, ejecutar una reconstrucción independiente y emitir un informe con tres estados. La transferencia está lograda cuando puedes decir qué caso coherente seguiría pasando en el nuevo formato y qué control lo vería.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md):

El equipo de seguridad de la universidad cliente define un procedimiento de aceptación. Los valores esperados (clave pública, nombre del producto, identificador del constructor, repositorio) se obtienen del contrato y de un canal independiente y se guardan en un archivo de configuración versionado; la secuencia más alta se registra en cada aceptación. El verificador recorre las doce comprobaciones y escribe un informe con los tres estados. Para cada release crítico, una segunda persona reconstruye el artefacto desde la fuente revisada en su propio entorno y compara la huella.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Las pruebas pasan siempre** — causa: el catálogo solo tiene casos que el verificador conoce. Corrección: añadir casos coherentes y pedir a otra persona que construya los suyos. ([SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Es la única comprobación que ata el artefacto a la fuente sin confiar en el constructor, y por eso convierte en discrepancia visible el primer caso coherente: si el código malicioso no está en la fuente revisada, la reconstrucción desde esa fuente no coincide con el release. ([SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia](../e/evidencia.md), [No verificable](../n/no-verificable.md), [Reconstrucción independiente](../r/reconstruccion-independiente.md), [Valor esperado](../v/valor-esperado.md), [Verificación](../v/verificacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), [SE-058](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SLSA v1.0: niveles](https://slsa.dev/spec/v1.0/levels) — garantías de la construcción y verificación de procedencia; autoridad: proyecto SLSA, OpenSSF.
- [in-toto: declaración (Statement)](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md) — atestaciones ligadas a un sujeto; autoridad: proyecto in-toto.
- [Reproducible Builds: definición](https://reproducible-builds.org/docs/definition/) — reconstrucción independiente; autoridad: proyecto Reproducible Builds.
- [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de desarrollo seguro de software; autoridad: NIST.
- [Lamb y Zacchiroli, «Reproducible Builds»](https://doi.org/10.1109/MS.2021.3073045) — reconstrucción independiente como defensa; autoridad: IEEE Software.

---

[↑ Glosario](../../README.md) · [← Caso base](./caso-base.md) · [Caso de abuso →](./caso-de-abuso.md)
