# Valor esperado

[↑ Glosario](../../README.md) · [← Valor del aprendizaje](./valor-del-aprendizaje.md) · [Valor esperado de la información perfecta →](./valor-esperado-de-la-informacion-perfecta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Dato (clave, constructor, repositorio, secuencia) que el verificador conoce por fuera del release.

Definición de trabajo de [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-534 — Gestión de riesgos y decisiones ejecutivas](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md): Suma de los resultados posibles ponderados por su probabilidad.

## Por qué importa

En [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), el tema «Valores esperados y raíz de confianza» importa porque sin valores fijados de antemano no se verifica nada.

## Cómo funciona

Según [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md):

Un release serio es una **cadena de huellas firmadas**. La firma cubre el manifiesto; el manifiesto contiene las huellas del artefacto, del SBOM y de la procedencia; la procedencia contiene la huella del sujeto (que debe ser el artefacto), el constructor, el repositorio, el commit y los materiales (entre ellos, la huella del archivo de bloqueo); el SBOM debe coincidir con el bloqueo; y el artefacto contiene, a su vez, el bloqueo. Cada eslabón se comprueba contra el siguiente, de modo que alterar uno obliga a alterar todos los que lo referencian y a firmar de nuevo.

Según [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md):

El equipo de seguridad de la universidad cliente define un procedimiento de aceptación. Los valores esperados (clave pública, nombre del producto, identificador del constructor, repositorio) se obtienen del contrato y de un canal independiente y se guardan en un archivo de configuración versionado; la secuencia más alta se registra en cada aceptación. El verificador recorre las doce comprobaciones y escribe un informe con los tres estados. Para cada release crítico, una segunda persona reconstruye el artefacto desde la fuente revisada en su propio entorno y compara la huella. Cuando la huella coincide, el informe lo registra como «procede de la fuente revisada»; cuando no, el release se rechaza y se abre una investigación.

## Ejemplo

Ejemplo de [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md) (sección «Ejemplo profesional»):

El equipo de seguridad de la universidad cliente define un procedimiento de aceptación. Los valores esperados (clave pública, nombre del producto, identificador del constructor, repositorio) se obtienen del contrato y de un canal independiente y se guardan en un archivo de configuración versionado; la secuencia más alta se registra en cada aceptación. El verificador recorre las doce comprobaciones y escribe un informe con los tres estados. Para cada release crítico, una segunda persona reconstruye el artefacto desde la fuente revisada en su propio entorno y compara la huella.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El verificador acepta un release de otro constructor** — causa: valores esperados tomados del documento. Corrección: configuración independiente y fijada de antemano. ([SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md))
- **Se mitigan riesgos que no pesan** — causa: matriz con celdas que agrupan valores muy distintos. Corrección: ordenar por valor esperado con rangos. ([SE-534](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Las dos manipulaciones que un atacante «con trabajo» intenta, cambiar el artefacto y volver a firmar el manifiesto con una clave que no es la esperada, fallan en la comprobación de la firma; cambiar el artefacto y re-firmar con la clave real exige además actualizar la procedencia, y cada actualización deja una discrepancia con los valores esperados. ([SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md))
- Genera carteras de treinta riesgos y cuenta en cuántas el riesgo de mayor valor esperado no está entre los cinco que elige la matriz. ([SE-534](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Secuencia](../s/secuencia.md).
- **Ver también:** [Resultado](../r/resultado.md), [Verificador](./verificador.md), [Caso coherente](../c/caso-coherente.md), [Decisión reversible](../d/decision-reversible.md), [No verificable](../n/no-verificable.md), [Petición de decisión](../p/peticion-de-decision.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-534 — Gestión de riesgos y decisiones ejecutivas](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

**También se usa en** (22 clases más lo mencionan; las que más):

[SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), [SE-141](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md), [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md), [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md).

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

[↑ Glosario](../../README.md) · [← Valor del aprendizaje](./valor-del-aprendizaje.md) · [Valor esperado de la información perfecta →](./valor-esperado-de-la-informacion-perfecta.md)
