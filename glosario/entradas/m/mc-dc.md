# MC/DC

[↑ Glosario](../../README.md) · [← Mayoría absoluta](./mayoria-absoluta.md) · [MCP →](./mcp.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Además, cada condición muestra su influencia independiente en el resultado.

Definición de trabajo de [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md).

## Por qué importa

En [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md), el tema «MC/DC» importa porque muestra la influencia independiente de cada condición.

## Cómo funciona

Según [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md):

La cobertura de **sentencias** exige que cada sentencia se ejecute; la de **decisión**, que cada decisión (cada `if`) tome ambos resultados; la de **condiciones**, que cada condición simple tome ambos valores; la de **condición/decisión**, las dos juntas; y la de **condición/decisión modificada** (MC/DC) añade que cada condición muestre su influencia independiente en el resultado: existen dos pruebas que difieren solo en esa condición y producen resultados distintos. Los criterios más estrictos se exigen en los niveles de rigor más altos del software aeronáutico, según circulares de la autoridad y tutoriales de la NASA. El tutorial de la NASA lo expresa con el principio del «peso suficiente» de cada condición: sin esa prueba, no se demuestra que la condición importe.

Según [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md):

Un equipo entrega un informe con MC/DC al 100 % para la lógica de un limitador. El revisor repasa los pares de independencia y descubre que en la condición «puerta abierta», el par presentado usa un vector en el que la temperatura ya está sobre el límite: el resultado es «cortar» con o sin la puerta. El par solo parecía independiente porque la herramienta contó mal una condición acoplada. Se rehace el análisis con el tratamiento de acoplamiento y aparece un par válido que ninguna prueba cubría. El equipo agrega la prueba y descubre un defecto real: con la puerta abierta y la temperatura baja, el código no cortaba. No lo había notado ninguna otra prueba porque ninguna ponía la puerta abierta con temperatura baja.

## Ejemplo

Ejemplo de [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md) (sección «Ejemplo profesional»):

Un equipo entrega un informe con MC/DC al 100 % para la lógica de un limitador. El revisor repasa los pares de independencia y descubre que en la condición «puerta abierta», el par presentado usa un vector en el que la temperatura ya está sobre el límite: el resultado es «cortar» con o sin la puerta. El par solo parecía independiente porque la herramienta contó mal una condición acoplada. Se rehace el análisis con el tratamiento de acoplamiento y aparece un par válido que ninguna prueba cubría. El equipo agrega la prueba y descubre un defecto real: con la puerta abierta y la temperatura baja, el código no cortaba.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un conjunto de pruebas satisface MC/DC si contiene, para cada condición, uno de sus pares. ([SE-454](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Influencia](../i/influencia.md), [Resultado](../r/resultado.md), [Cobertura de condiciones](../c/cobertura-de-condiciones.md), [Cobertura de decisión](../c/cobertura-de-decision.md), [HIL](../h/hil.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md).

**Aparece en los casos de estudio:** [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md), [Boeing 737 MAX y MCAS](../../../casos/fallo/boeing-737-max-mcas.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Mayoría absoluta](./mayoria-absoluta.md) · [MCP →](./mcp.md)
