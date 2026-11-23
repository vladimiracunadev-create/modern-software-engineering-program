# Reducción

[↑ Glosario](../../README.md) · [← Redondeo](./redondeo.md) · [Reducción por dimensiones →](./reduccion-por-dimensiones.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Proceso que simplifica un contraejemplo mientras siga fallando.

Definición de trabajo de [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md): Simplificación de un contraejemplo hasta una forma mínima que sigue fallando.

## Por qué importa

En [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), el tema «Reducción de contraejemplos» importa porque un fallo de 150 caracteres no se diagnostica; uno de 20 sí.

## Cómo funciona

Según [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md):

Un fallo encontrado con una entrada grande y aleatoria no explica nada. La reducción (shrinking) toma el contraejemplo y prueba versiones más pequeñas (quitar elementos, acortar cadenas) mientras la propiedad siga fallando; termina en un caso en el que quitar cualquier parte lo hace pasar. El caso mínimo es lo que se discute en una revisión y lo que queda como prueba de regresión. Sin reducción, la prueba aleatoria encuentra defectos que nadie puede diagnosticar.

Según [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md):

Una prueba basada en propiedades afirma algo para todas las entradas de un tipo («la deduplicación no deja elementos repetidos») y la comprueba con muchas entradas generadas. Cuando falla, el contraejemplo original suele ser largo y ruidoso; la **reducción** lo simplifica probando entradas más pequeñas que siguen fallando hasta llegar a una forma mínima. La reducción convierte una lista de 22 números en tres, y esa forma mínima revela el defecto con una lectura.

## Ejemplo

Ejemplo de [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) (sección «Caso conductor»):

La plataforma de entregas es el caso conductor de la [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md). Esta clase deja cinco contratos de consumidor, una propiedad con reducción y una comprobación de dobles contra el proveedor real. `SE-167` los integrará en un taller que convierte una intención en un contrato comprobable de extremo a extremo, y `SE-168` los empaquetará con su trazabilidad. Cambia después una sola decisión, retirar el campo `links`, y revisa qué consumidores, ejemplos y pruebas se ven afectados.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El contraejemplo es largo e ininteligible** — causa: no hay reducción. Corrección: reducir antes de informar. ([SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md))
- **El contraejemplo de una propiedad tiene 22 elementos y no se entiende** — causa: no hay reducción. Corrección: reducir el contraejemplo a su forma mínima antes de analizarlo. ([SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Sin reducción, la prueba aleatoria encuentra defectos que nadie puede diagnosticar. ([SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contraejemplo](../c/contraejemplo.md), [Proceso](../p/proceso.md), [Contrato de consumidor](../c/contrato-de-consumidor.md), [Contrato dirigido por el consumidor](../c/contrato-dirigido-por-el-consumidor.md), [Doble de prueba](../d/doble-de-prueba.md), [Generador](../g/generador.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (70 clases más lo mencionan; las que más):

[SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md), [SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md), [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md), [SE-104](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md), [SE-106](../../../classes/part-08-entornos-herramientas-y-depuracion/se-106-ergonomia-accesibilidad-y-productividad-del-entorno/README.md), [SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), [SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md), [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md).

**Aparece en los casos de estudio:** [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md), [TSB Bank](../../../casos/fallo/tsb.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «shrinking».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Claessen y Hughes, «QuickCheck» (ICFP, 2000)](https://doi.org/10.1145/351240.351266) — pruebas basadas en propiedades y reducción; autoridad: ACM SIGPLAN ICFP.
- [Hypothesis documentation](https://hypothesis.readthedocs.io/en/latest/) — biblioteca de pruebas de propiedades para Python con reducción; autoridad: proyecto Hypothesis.
- [Hypothesis: pruebas con estado](https://hypothesis.readthedocs.io/en/latest/stateful.html) — comparación con modelos; autoridad: documentación oficial.
- [MacIver et al., «Hypothesis: A new approach to property-based testing»](https://joss.theoj.org/papers/10.21105/joss.01891) — diseño de la biblioteca; autoridad: artículo revisado de JOSS.
- [Hughes, «How to Specify It!»](https://doi.org/10.1007/978-3-030-47147-7_4) — estrategias para escribir propiedades; autoridad: capítulo del autor.

---

[↑ Glosario](../../README.md) · [← Redondeo](./redondeo.md) · [Reducción por dimensiones →](./reduccion-por-dimensiones.md)
