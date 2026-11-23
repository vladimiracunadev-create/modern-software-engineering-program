# Patrón

[↑ Glosario](../../README.md) · [← Pass@k y pass^k](./pass-k-y-pass-k.md) · [Patrón de acceso →](./patron-de-acceso.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Solución con nombre a un problema recurrente en un contexto, con sus consecuencias.

Definición de trabajo de [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md): Estructura repetida con consecuencias conocidas.

## Por qué importa

En [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), el tema «Qué es un patrón» importa porque sin contexto y consecuencias, un patrón es solo una forma

## Cómo funciona

Según [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md):

El formato del catálogo de la Gang of Four fija lo que debe llevar un patrón: un **nombre** que permita conversar, el **problema** y su contexto, la **solución** como estructura de clases y colaboraciones, y las **consecuencias** con sus ventajas y costos. Cuando se aplica un patrón sin contexto ni consecuencias, queda solo la forma: una jerarquía de clases cuyo propósito nadie recuerda. Por eso el criterio de esta clase obliga a escribir las cinco partes aunque la solución sea conocida. El esfuerzo no es burocrático: la segunda y la cuarta suelen revelar que el contexto no es el del catálogo.

Según [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md):

El equipo de *Avisos* revisa el cálculo de tarifas antes de añadir el canal de mensajería instantánea. Escribe en el `criterio-de-patron.md`: fuerza («cada canal nuevo ha obligado a editar `precio_aviso` y a repasar las pruebas de los otros»), evidencia («tres canales nuevos en seis meses y dos más en el backlog con responsable»), costo («el Strategy usa un 44 % más de nodos y añade un salto de indirección; la complejidad por función baja»), alternativa («un diccionario de funciones haría lo mismo con menos piezas, pero las tarifas de voz necesitan estado») y salida («si en un año no entra un canal nuevo, se vuelve a la función simple»). Con eso la discusión pasa de gusto a evidencia, y la decisión queda registrada para quien la revise.

## Ejemplo

Ejemplo de [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md) (sección «Ejemplo mínimo»):

La segunda no es un patrón con nombre y resuelve la fuerza «añadir un canal sin tocar la función» con una línea de datos. Es el diseño más barato que da la propiedad buscada, y por eso el patrón completo con clases solo se justifica si cada canal necesita **comportamiento** propio y no solo un número.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cuando se aplica un patrón sin contexto ni consecuencias, queda solo la forma: una jerarquía de clases cuyo propósito nadie recuerda. ([SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Consecuencia](../c/consecuencia.md), [Contextos](../c/contextos.md), [Estructura](../e/estructura.md), [Evidencia](../e/evidencia.md), [Abstracción](../a/abstraccion.md), [Condición de salida](../c/condicion-de-salida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (169 clases más lo mencionan; las que más):

[SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md), [SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), [SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md), [SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md), [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md), [SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), [SE-599](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md), [SE-280](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Stripe](../../../casos/exito/stripe.md), [Slack](../../../casos/exito/slack.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [TSB Bank](../../../casos/fallo/tsb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.
- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.

---

[↑ Glosario](../../README.md) · [← Pass@k y pass^k](./pass-k-y-pass-k.md) · [Patrón de acceso →](./patron-de-acceso.md)
