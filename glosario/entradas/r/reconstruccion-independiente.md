# Reconstrucción independiente

[↑ Glosario](../../README.md) · [← Reconstrucción de la solución](./reconstruccion-de-la-solucion.md) · [Recorrido crítico →](./recorrido-critico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Construcción del artefacto desde la fuente por una parte distinta del constructor original.

Definición de trabajo de [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md).

## Por qué importa

En [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), el tema «Reconstrucción independiente» importa porque es la única comprobación que ata el artefacto a la fuente.

## Cómo funciona

Según [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), en la sección «Reconstrucción independiente»:

Se reconstruye el artefacto desde la fuente revisada y se compara con el release legítimo, con el release malicioso, y se reconstruye desde la fuente maliciosa y se compara con el release malicioso.

**Cómo leer la figura.** A la izquierda está la reconstrucción y a la derecha tres comparaciones. Las turquesa muestran que reconstruir desde la fuente revisada detecta la manipulación; la coral recuerda que reconstruir desde una fuente maliciosa también coincide: reproducible no equivale a legítimo. **Dónde deja de valer:** exige que exista una «fuente revisada» independiente de la que se usó para el release, que el build sea reproducible (`SE-469`) y que las entradas estén declaradas; un compilador real con entradas no declaradas haría que la coincidencia no ocurriera ni siquiera en el caso legítimo.

## Ejemplo

Caso medido en la sección «Reconstrucción independiente» de [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md):

**Cómo leer la figura.** A la izquierda está la reconstrucción y a la derecha tres comparaciones. Las turquesa muestran que reconstruir desde la fuente revisada detecta la manipulación; la coral recuerda que reconstruir desde una fuente maliciosa también coincide: reproducible no equivale a legítimo. **Dónde deja de valer:** exige que exista una «fuente revisada» independiente de la que se usó para el release, que el build sea reproducible (`SE-469`) y que las entradas estén declaradas; un compilador real con entradas no declaradas haría que la coincidencia no ocurriera ni siquiera en el caso legítimo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md)) son:

- **El verificador acepta un release de otro constructor** — causa: valores esperados tomados del documento. Corrección: configuración independiente y fijada de antemano.
- **Un release antiguo pasa como el último** — causa: sin comprobar la secuencia. Corrección: recordar la mayor secuencia vista y rechazar menores.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **reconstrucción independiente** toma la fuente revisada, la construye con las entradas declaradas en un entorno que no es el del constructor y compara la huella con la del release. ([SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Artefacto](../a/artefacto.md), [Caso coherente](../c/caso-coherente.md), [No verificable](../n/no-verificable.md), [Valor esperado](../v/valor-esperado.md), [Verificación](../v/verificacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reproducible Builds: definición](https://reproducible-builds.org/docs/definition/) — reconstrucción independiente; autoridad: proyecto Reproducible Builds.
- [Lamb y Zacchiroli, «Reproducible Builds»](https://doi.org/10.1109/MS.2021.3073045) — reconstrucción independiente como defensa; autoridad: IEEE Software.
- [SLSA v1.0: niveles](https://slsa.dev/spec/v1.0/levels) — garantías de la construcción y verificación de procedencia; autoridad: proyecto SLSA, OpenSSF.
- [in-toto: declaración (Statement)](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md) — atestaciones ligadas a un sujeto; autoridad: proyecto in-toto.
- [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de desarrollo seguro de software; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Reconstrucción de la solución](./reconstruccion-de-la-solucion.md) · [Recorrido crítico →](./recorrido-critico.md)
