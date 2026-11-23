# Nivel de integridad

[↑ Glosario](../../README.md) · [← Nivel de abstracción](./nivel-de-abstraccion.md) · [Nivel de prueba →](./nivel-de-prueba.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Escala de 1 a 4 que fija el rigor y la banda de probabilidad de fallo de una función de seguridad.

Definición de trabajo de [SE-446 — IEC 61508 y niveles de integridad de seguridad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md).

## Por qué importa

La clase donde se define, [SE-446 — IEC 61508 y niveles de integridad de seguridad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md), existe con este propósito: la clase existe para que entiendas qué significa, en números y en proceso, que una función de seguridad tenga un **nivel de integridad**, y qué hay que hacer para sostener esa afirmación.

## Cómo funciona

Según [SE-446 — IEC 61508 y niveles de integridad de seguridad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md):

Una función de seguridad es una acción que se realiza para llevar el sistema a un estado seguro o mantenerlo en él cuando ocurre una condición peligrosa. En el horno es «si la temperatura medida supera 250 °C o la puerta se abre, desconectar el calentador en menos de dos segundos». La función incluye el sensor que mide, la lógica que decide y el actuador que corta, y a veces también a la persona que actúa. Su nivel de integridad es el de la cadena completa: el eslabón más débil y las causas comunes entre eslabones deciden. Escribir la función con su tiempo de respuesta es parte de la especificación: una protección que actúa tarde (`SE-451`) puede ser correcta y no servir.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-446 — IEC 61508 y niveles de integridad de seguridad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-446 — IEC 61508 y niveles de integridad de seguridad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md)) son: Las fórmulas son simplificadas, las tasas y el valor de β son del autor y el texto de la norma no se reproduce; las bandas se describen desde material público y no se verificaron contra la norma. El siguiente paso, `SE-447`, especializa esta lógica para vehículos de carretera, con otro vocabulario y otra forma de asignar el rigor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Función de seguridad](../f/funcion-de-seguridad.md), [Banda](../b/banda.md), [Función](../f/funcion.md), [Seguridad](../s/seguridad.md), [Β](../c/concepto.md), [Arquitectura MooN](../a/arquitectura-moon.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-446 — IEC 61508 y niveles de integridad de seguridad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Nivel de abstracción](./nivel-de-abstraccion.md) · [Nivel de prueba →](./nivel-de-prueba.md)
