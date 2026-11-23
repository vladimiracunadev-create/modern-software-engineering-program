# Propiedad

[↑ Glosario](../../README.md) · [← Propagación de contexto](./propagacion-de-contexto.md) · [Propiedad de archivos →](./propiedad-de-archivos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Afirmación que debe cumplirse para toda entrada del dominio de una función.

Definición de trabajo de [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md): Afirmación que debe cumplirse para todas las entradas de un tipo y que se comprueba con entradas generadas.
- En [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md): Afirmación que debe cumplirse para toda entrada de una clase, comprobada con muchas entradas generadas.

## Por qué importa

En [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), el tema «Propiedades» importa porque dicen qué debe cumplirse sin enumerar casos.

## Cómo funciona

Según [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), en la sección «Propiedades»:

Una propiedad es una afirmación que debe cumplirse para toda entrada del dominio: la suma de las cantidades repartidas es `n`; normalizar dos veces da lo mismo que normalizar una; invertir una lista dos veces devuelve la original. Se escribe sin repetir la implementación (la propiedad «el resultado es lo que calcula la función» no comprueba nada). Hay familias útiles: invariantes que se conservan, idempotencia, relaciones entre entradas (si se añade un elemento, el resultado cambia así), comparación con un modelo más simple y propiedades metamórficas. Una propiedad débil se cumple casi siempre y casi no protege.

## Ejemplo

Ejemplo de [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md) (sección «Ejemplo mínimo»):

El fragmento comprueba tres propiedades de una función de reparto con 200 casos aleatorios. Antes de ejecutarlo, predice si pasa la versión que olvida el resto.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La propiedad pasa y la función tiene un defecto conocido** — causa: generador que no llega a la frontera. Corrección: sesgo hacia vacío, límites y combinaciones. ([SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md))
- **La propiedad repite la implementación** — causa: se calcula el resultado esperado con la misma fórmula. Corrección: usar invariantes o un modelo distinto. ([SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md))
- **El contraejemplo de una propiedad tiene 22 elementos y no se entiende** — causa: no hay reducción. Corrección: reducir el contraejemplo a su forma mínima antes de analizarlo. ([SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se escribe sin repetir la implementación (la propiedad «el resultado es lo que calcula la función» no comprueba nada). ([SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md))
- Los ejemplos documentan decisiones de negocio y fijan casos conocidos; las propiedades exploran lo que no se escribió. ([SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Afirmación](../a/afirmacion.md), [Dominio](../d/dominio.md), [Función](../f/funcion.md), [Tipo](../t/tipo.md), [Command](../c/command.md), [Contrato de consumidor](../c/contrato-de-consumidor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (274 clases más lo mencionan; las que más):

[SE-530](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md), [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md), [SE-343](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md), [SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md), [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md), [SE-551](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md), [SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Propiedades».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Claessen y Hughes, «QuickCheck: a lightweight tool for random testing of Haskell programs»](https://doi.org/10.1145/351240.351266) — pruebas por propiedades; autoridad: artículo original de ICFP 2000.
- [Documentación de Hypothesis](https://hypothesis.readthedocs.io/en/latest/) — biblioteca de propiedades para Python; autoridad: documentación oficial.
- [Hughes, «How to Specify It!»](https://doi.org/10.1007/978-3-030-47147-7_4) — estrategias para escribir propiedades; autoridad: capítulo del autor.
- [Hypothesis: pruebas con estado](https://hypothesis.readthedocs.io/en/latest/stateful.html) — comparación con modelos; autoridad: documentación oficial.
- [MacIver et al., «Hypothesis: A new approach to property-based testing»](https://joss.theoj.org/papers/10.21105/joss.01891) — diseño de la biblioteca; autoridad: artículo revisado de JOSS.

---

[↑ Glosario](../../README.md) · [← Propagación de contexto](./propagacion-de-contexto.md) · [Propiedad de archivos →](./propiedad-de-archivos.md)
