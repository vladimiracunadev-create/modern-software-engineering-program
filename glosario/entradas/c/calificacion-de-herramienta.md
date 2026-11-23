# Calificación de herramienta

[↑ Glosario](../../README.md) · [← Calidad interna](./calidad-interna.md) · [Calificador →](./calificador.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Demostración de que una herramienta es confiable para la verificación que sustituye.

Definición de trabajo de [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md).

## Por qué importa

En [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md), el tema «Calificación de herramientas» importa porque una herramienta que sustituye una verificación debe ser confiable.

## Cómo funciona

Según [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md):

Si una herramienta automatiza o reemplaza una verificación (el medidor de cobertura, el generador de código), su error puede pasar inadvertido; por eso existe un documento aparte sobre la calificación de herramientas y los suplementos para modelos, orientación a objetos y métodos formales. En el laboratorio, el medidor es el trazador de líneas de Python, no una herramienta calificada, y por eso los resultados sirven para entender el mecanismo y no como evidencia de certificación. La trazabilidad bidireccional (requisito a código a prueba y de vuelta) es el hilo que permite saber qué prueba cubre qué requisito y qué código no tiene requisito (`SE-450`).

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md)) son: La función del limitador es una pieza didáctica con defectos plantados, el medidor no es una herramienta calificada, las normas de pago no se reproducen y no se afirma conformidad con DO-178C ni DO-254. El siguiente paso, `SE-449`, pasa a los dispositivos médicos, donde el software se clasifica por su contribución al daño y por los controles externos que lo acotan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Herramientas](../h/herramientas.md), [Verificación](../v/verificacion.md), [Cobertura estructural](./cobertura-estructural.md), [Código muerto](./codigo-muerto.md), [Código no previsto](./codigo-no-previsto.md), [Condición de fallo](./condicion-de-fallo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Calificación de herramientas».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Calidad interna](./calidad-interna.md) · [Calificador →](./calificador.md)
