# Instantánea

[↑ Glosario](../../README.md) · [← Instancia por petición](./instancia-por-peticion.md) · [Instante →](./instante.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Copia de una salida contra la que se compara exactamente en cada ejecución.

Definición de trabajo de [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md): Copia del estado en un punto de la historia que evita reaplicar todos los eventos anteriores.
- En [SE-547 — Diseño por contrato y pruebas de contrato como oráculo](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md): Copia guardada de una respuesta completa que se compara con la actual.
- En [SE-582 — Sandboxes, reversibilidad y control de daño](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md): Copia o commit que permite restaurar un estado.
- En [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md): Copia consistente del estado en un momento dado, punto de partida de un flujo de cambios.

## Por qué importa

En [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md), el tema «Instantánea frente a aserción semántica» importa porque una comparación exacta genera ruido que se aprueba sin leer.

## Cómo funciona

Según [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md):

Una instantánea guarda la salida (por ejemplo el HTML) y falla ante cualquier diferencia. Detecta todo cambio y no distingue uno que importa de uno que no: un espacio, el orden de los atributos o una fecha nueva rompen la prueba igual que un botón que desaparece. Cuando la mayoría de las diferencias son ruido, el equipo aprende a aprobarlas sin leerlas, y la instantánea deja de proteger. Una aserción semántica afirma lo que el usuario percibe (el título, la nota de la entrega, la presencia del botón) y es insensible al resto; su costo es que solo ve lo que se le pidió mirar.

Según [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md):

Traslada el análisis a otra aplicación (por ejemplo, una tienda de entradas): construye un registro de uso, elige recorridos con dos métricas, calcula la inestabilidad de cada uno y compara una instantánea con una aserción semántica. La transferencia está lograda cuando puedes explicar por qué un recorrido se acortó o se bajó de nivel, no cuando la lista se parece.

## Ejemplo

Ejemplo de [SE-582 — Sandboxes, reversibilidad y control de daño](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md) (sección «Preguntas frecuentes»):

Son el riesgo principal. O se copian explícitamente en la instantánea, o se montan en solo lectura, o se mantienen fuera del alcance del agente.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Las instantáneas se aprueban sin leerlas** — causa: casi todas las diferencias son ruido. Corrección: aserciones semánticas y una instantánea solo para salidas pequeñas. ([SE-424](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md))
- **Reconstruir un agregado tarda cada vez más** — causa: historia creciente sin instantáneas. Corrección: instantáneas periódicas o un agregado más pequeño. ([SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cuando la mayoría de las diferencias son ruido, el equipo aprende a aprobarlas sin leerlas, y la instantánea deja de proteger. ([SE-424](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md))
- Traslada el análisis a otra aplicación (por ejemplo, una tienda de entradas): construye un registro de uso, elige recorridos con dos métricas, calcula la inestabilidad de cada uno y compara una instantánea con una aserción semántica. ([SE-424](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Copia consistente](../c/copia-consistente.md), [Estado](../e/estado.md), [Evento](../e/evento.md), [Flujo](../f/flujo.md), [Captura de cambios](../c/captura-de-cambios.md), [Consistencia eventual](../c/consistencia-eventual.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-547 — Diseño por contrato y pruebas de contrato como oráculo](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.
- [SE-582 — Sandboxes, reversibilidad y control de daño](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (24 clases más lo mencionan; las que más):

[SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), [SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md), [SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), [SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md), [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md), [SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md), [SE-099](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md).

**Aparece en los casos de estudio:** [Stripe](../../../casos/exito/stripe.md), [Slack](../../../casos/exito/slack.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «snapshot».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Jest: pruebas de instantáneas](https://jestjs.io/docs/snapshot-testing) — instantáneas; autoridad: documentación oficial.
- [Martin Fowler, «BroadStackTest»](https://martinfowler.com/bliki/BroadStackTest.html) — pruebas de banda ancha; autoridad: autor del texto.
- [Google Testing Blog: Just Say No to More End-to-End Tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html) — costo de las pruebas de extremo a extremo; autoridad: equipo de pruebas de Google.
- [Martin Fowler, «TestPyramid»](https://martinfowler.com/bliki/TestPyramid.html) — reparto por nivel; autoridad: autor del texto.
- [Playwright: buenas prácticas](https://playwright.dev/docs/best-practices) — pruebas centradas en el usuario; autoridad: documentación oficial.

---

[↑ Glosario](../../README.md) · [← Instancia por petición](./instancia-por-peticion.md) · [Instante →](./instante.md)
