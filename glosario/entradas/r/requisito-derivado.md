# Requisito derivado

[↑ Glosario](../../README.md) · [← Requisito comprobable](./requisito-comprobable.md) · [Requisito funcional →](./requisito-funcional.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Requisito que surge del diseño y no de los requisitos del sistema.

Definición de trabajo de [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md).

## Por qué importa

En [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md), el tema «Requisitos derivados» importa porque recogen lo que el diseño añade y nadie pidió.

## Cómo funciona

Según [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md):

El software parte de requisitos del sistema asignados a él (alto nivel) y los refina en requisitos de bajo nivel (de los que sale el código). Durante el diseño aparecen decisiones que no estaban en ningún requisito del sistema: usar una tabla, proteger una entrada, reintentar. Son **requisitos derivados** y deben reportarse a los procesos de seguridad porque pueden afectar la evaluación del sistema: el equipo de seguridad no sabía que el software haría eso. En el laboratorio, devolver el estado seguro si el sensor no tiene lectura es una conducta derivada que estaba en el código pero en ningún requisito.

Según [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md):

**Corrección.** Se escribe el requisito R5 con su resultado esperado, se reemplaza la prueba que solo ejecutaba por una que verifica el estado seguro y se añade a la revisión una regla: cada prueba que se añade por cobertura debe estar trazada a un requisito o a un requisito derivado. La lección es que la cobertura es una pregunta sobre las pruebas, no una prueba del código.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Son **requisitos derivados** y deben reportarse a los procesos de seguridad porque pueden afectar la evaluación del sistema: el equipo de seguridad no sabía que el software haría eso. ([SE-448](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Calificación de herramienta](../c/calificacion-de-herramienta.md), [Cobertura estructural](../c/cobertura-estructural.md), [Código muerto](../c/codigo-muerto.md), [Código no previsto](../c/codigo-no-previsto.md), [Condición de fallo](../c/condicion-de-fallo.md), [Prueba basada en requisitos](../p/prueba-basada-en-requisitos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Requisitos derivados».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Requisito comprobable](./requisito-comprobable.md) · [Requisito funcional →](./requisito-funcional.md)
