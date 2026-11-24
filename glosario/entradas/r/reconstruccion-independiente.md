# Reconstrucción independiente

[↑ Glosario](../../README.md) · [← Reconstrucción de la solución](./reconstruccion-de-la-solucion.md) · [Recorrido crítico →](./recorrido-critico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

La **reconstrucción independiente** es la construcción de un artefacto desde la fuente por una parte distinta del constructor original, para comparar el resultado con el artefacto publicado. [SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md) la usa en la cadena de suministro: se toma la fuente revisada, se construye con las entradas declaradas en un entorno que no es el del constructor y se compara la huella con la del release.

## Por qué importa

Un release firmado prueba *quién* lo publicó, no que corresponda al código que se revisó. Si el entorno de construcción se compromete, el binario puede incluir algo que la fuente no tiene. La reconstrucción independiente cambia la confianza: de «creo en el constructor» a «alguien más puede obtener el mismo artefacto desde la fuente que revisé». Detecta, por ejemplo, un release manipulado después de la revisión.

## Cómo funciona

[SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md) compara tres reconstrucciones contra dos releases (uno legítimo y uno malicioso):

1. Reconstruir desde la **fuente revisada** y comparar con el release legítimo: coincide.
2. Reconstruir desde la fuente revisada y comparar con el release malicioso: **no coincide**; es la detección.
3. Reconstruir desde la **fuente maliciosa** y comparar con el release malicioso: coincide.

La tercera comparación es la advertencia de la clase: **reproducible no equivale a legítimo**. Que un build se reproduzca solo prueba que es determinista; si la fuente de partida es la comprometida, el resultado coincide igual. De ahí la condición de independencia: la fuente de comparación tiene que ser la *revisada*, obtenida por un camino distinto del de quien publicó el release.

Esto presupone un **build reproducible** ([SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md)): mismas entradas y mismo proceso dan la misma huella. La comparación se hace sobre la huella del artefacto.

## Ejemplo

Se publica una versión 2.4.0 de una biblioteca. Una segunda parte clona la etiqueta revisada, usa las dependencias fijadas por su bloqueo, construye en su entorno y calcula la huella. Si coincide con la del release, la fuente revisada es la que se empaquetó. Si no coincide, hay una diferencia que explicar: o hay una entrada no declarada (la fecha de compilación, una ruta absoluta) o hay manipulación. La cifra de coincidencias de la clase viene de un modelo sintético con releases legítimo y malicioso, no de un compilador real.

## Errores y confusiones comunes

- **El verificador acepta un release de otro constructor.** Causa ([SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md)): valores esperados tomados del documento que se verifica. Corrección: configuración independiente, fijada de antemano.
- **Un release antiguo pasa como el último.** No se comprobó la secuencia; hay que recordar la mayor secuencia vista y rechazar las menores.
- **Confiar en una reconstrucción desde la fuente equivocada.** Coincide, pero no valida nada.
- **No declarar todas las entradas.** Con entradas ocultas la coincidencia falla incluso en el caso legítimo.

## Límites y cuándo no aplica

Exige tres cosas ([SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md)): que exista una «fuente revisada» independiente de la usada para el release, que el build sea reproducible y que las entradas estén declaradas. Un compilador real con entradas no declaradas haría que la coincidencia no ocurriera ni siquiera en el caso legítimo. Aun cuando funcione, solo prueba que el artefacto corresponde a la fuente; no que la fuente sea segura ni que las dependencias lo sean. Y exige a alguien con la capacidad de reconstruir: para proyectos sin esa tercera parte, la garantía no existe.

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
