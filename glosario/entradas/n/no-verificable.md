# No verificable

[↑ Glosario](../../README.md) · [← No determinismo](./no-determinismo.md) · [No-code →](./no-code.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Afirmación sobre la cual ninguna comprobación disponible puede decidir.

Definición de trabajo de [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md).

## Por qué importa

La clase donde se define, [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), existe con este propósito: el taller existe para que ejecutes, de principio a fin y con tus manos, la pregunta que justifica toda la [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md):

## Cómo funciona

Según [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md):

El resultado de una verificación no es un booleano sino un **informe con tres estados**. *Verificado*: se comprobó, con estos valores esperados, y coincide. *No verificado*: se comprobó y no coincide (con la comprobación que falló). *No verificable con esta evidencia*: ninguna de las comprobaciones puede decidirlo (la bondad del contenido de la fuente, la honestidad del constructor, la existencia de una clave robada). El informe indica la fecha, las versiones de las herramientas, los valores esperados y su origen, las comprobaciones ejecutadas, las no ejecutadas y el estado de cada afirmación. Esa honestidad es el producto del taller: la frase «el release está verificado» se sustituye por «estas afirmaciones se verificaron, estas no, y estas no son verificables con lo que tengo».

Según [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md):

El equipo de seguridad de la universidad cliente define un procedimiento de aceptación. Los valores esperados (clave pública, nombre del producto, identificador del constructor, repositorio) se obtienen del contrato y de un canal independiente y se guardan en un archivo de configuración versionado; la secuencia más alta se registra en cada aceptación. El verificador recorre las doce comprobaciones y escribe un informe con los tres estados. Para cada release crítico, una segunda persona reconstruye el artefacto desde la fuente revisada en su propio entorno y compara la huella. Cuando la huella coincide, el informe lo registra como «procede de la fuente revisada»; cuando no, el release se rechaza y se abre una investigación.

## Ejemplo

Ejemplo de [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md) (sección «Ejemplo profesional»):

El equipo de seguridad de la universidad cliente define un procedimiento de aceptación. Los valores esperados (clave pública, nombre del producto, identificador del constructor, repositorio) se obtienen del contrato y de un canal independiente y se guardan en un archivo de configuración versionado; la secuencia más alta se registra en cada aceptación. El verificador recorre las doce comprobaciones y escribe un informe con los tres estados. Para cada release crítico, una segunda persona reconstruye el artefacto desde la fuente revisada en su propio entorno y compara la huella.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md)) son:

- **El verificador acepta un release de otro constructor** — causa: valores esperados tomados del documento. Corrección: configuración independiente y fijada de antemano.
- **Un release antiguo pasa como el último** — causa: sin comprobar la secuencia. Corrección: recordar la mayor secuencia vista y rechazar menores.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- *No verificable con esta evidencia*: ninguna de las comprobaciones puede decidirlo (la bondad del contenido de la fuente, la honestidad del constructor, la existencia de una clave robada). ([SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Afirmación](../a/afirmacion.md), [Sobre](../s/sobre.md), [Caso coherente](../c/caso-coherente.md), [Reconstrucción independiente](../r/reconstruccion-independiente.md), [Valor esperado](../v/valor-esperado.md), [Verificación](../v/verificacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md), [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md), [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md).

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

[↑ Glosario](../../README.md) · [← No determinismo](./no-determinismo.md) · [No-code →](./no-code.md)
