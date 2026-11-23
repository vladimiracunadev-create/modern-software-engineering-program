# Relación

[↑ Glosario](../../README.md) · [← Reintentos](./reintentos.md) · [Relación de contraste →](./relacion-de-contraste.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Conjunto de pares entre dominios.

Definición de trabajo de [SE-051 — Conjuntos, relaciones, funciones y grafos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md).

## Por qué importa

En [SE-051 — Conjuntos, relaciones, funciones y grafos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md), el tema «estructura» importa porque ¿qué relaciones se conservan?

## Cómo funciona

Según [SE-051 — Conjuntos, relaciones, funciones y grafos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md), en la sección «Relaciones»:

Una relación es un subconjunto del producto cartesiano. `prueba_refuta ⊆ Pruebas × Hipótesis` permite muchos a muchos. Propiedades como reflexividad, simetría y transitividad no se presumen: «correlacionado con» puede ser simétrico, «depende de» no.

## Ejemplo

Ejemplo de [SE-051 — Conjuntos, relaciones, funciones y grafos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md) (sección «Ejemplo mínimo»):

Define H={DNS,TCP,TLS}, P={p1,p2,p3} y una relación `refuta`. Calcula qué hipótesis no tiene prueba y qué pruebas son redundantes. Después dibuja dependencias como grafo.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-051 — Conjuntos, relaciones, funciones y grafos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md)) son:

- **El recorrido no termina** — causa: no hay conjunto de visitados o medida decreciente. Corrección: registrar los nodos visitados y acotar los pasos.
- **El orden de construcción cambia entre ejecuciones** — causa: se fijó una prueba al orden de vecinos. Corrección: comprobar solo las propiedades exigidas por el contrato.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un conjunto de componentes con relaciones «A depende de B» es un grafo dirigido. ([SE-051](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Conjunto](../c/conjunto.md), [Dominio](../d/dominio.md), [Alcanzabilidad](../a/alcanzabilidad.md), [Estrategia](../e/estrategia.md), [Función](../f/funcion.md), [Grafo](../g/grafo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-051 — Conjuntos, relaciones, funciones y grafos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.

**También se usa en** (158 clases más lo mencionan; las que más):

[SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md), [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md), [SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), [SE-258](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md), [SE-050](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md), [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Stripe](../../../casos/exito/stripe.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase.

---

[↑ Glosario](../../README.md) · [← Reintentos](./reintentos.md) · [Relación de contraste →](./relacion-de-contraste.md)
