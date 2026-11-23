# Prueba basada en requisitos

[↑ Glosario](../../README.md) · [← Prueba A/A](./prueba-a-a.md) · [Prueba contractual →](./prueba-contractual.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Prueba diseñada a partir de un requisito, no del código.

Definición de trabajo de [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md).

## Por qué importa

En [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md), el tema «Pruebas basadas en requisitos» importa porque verifican la intención.

## Cómo funciona

Según [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md):

Tras las pruebas basadas en requisitos se mide qué partes del código se ejecutaron. Los criterios crecen en exigencia: sentencias, decisiones (cada resultado de cada condicional), y condición/decisión modificada (cada condición muestra su influencia independiente en el resultado; `SE-454`). Los niveles de rigor más altos exigen los criterios más estrictos; esa asociación aparece en material público de la autoridad y en tutoriales de la NASA. La cobertura no se usa para escribir más pruebas hasta llegar a un número, sino para **encontrar lo que las pruebas basadas en requisitos no ejercitaron**: una prueba que «solo sube la cobertura» sin verificar un requisito es una trampa.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La cobertura no se usa para escribir más pruebas hasta llegar a un número, sino para **encontrar lo que las pruebas basadas en requisitos no ejercitaron**: una prueba que «solo sube la cobertura» sin verificar un requisito es una trampa. ([SE-448](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Calificación de herramienta](../c/calificacion-de-herramienta.md), [Cobertura estructural](../c/cobertura-estructural.md), [Código muerto](../c/codigo-muerto.md), [Código no previsto](../c/codigo-no-previsto.md), [Condición de fallo](../c/condicion-de-fallo.md), [Requisito derivado](../r/requisito-derivado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-454](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Pruebas basadas en requisitos».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Prueba A/A](./prueba-a-a.md) · [Prueba contractual →](./prueba-contractual.md)
