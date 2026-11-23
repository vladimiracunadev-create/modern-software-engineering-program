# Cobertura de decisión

[↑ Glosario](../../README.md) · [← Cobertura de controles](./cobertura-de-controles.md) · [Cobertura de diagnóstico →](./cobertura-de-diagnostico.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Cada decisión toma ambos resultados en alguna prueba.

Definición de trabajo de [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md).

## Por qué importa

En [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md), el tema «Cobertura de decisión» importa porque ejerce los dos resultados de cada decisión.

## Cómo funciona

Según [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md):

La cobertura de decisión se satisface con 2 pruebas (una que dé verdadero y otra falso) y la de condiciones con 2 pruebas (todas las condiciones verdaderas y todas falsas), pero sus conjuntos mínimos no son iguales en capacidad. En el laboratorio, para la cobertura de condiciones hay 8 conjuntos de 2 pruebas y 5 de ellos nunca cambian el resultado de la decisión (todos dan falso, por ejemplo), de modo que no cumplen ni la cobertura de decisión. Un criterio cumplido por un conjunto degenerado es un criterio cumplido sin valor. Por eso la cobertura se exige junto con pruebas derivadas de requisitos: un conjunto que sale de requisitos tiene un propósito detrás de cada caso.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La cobertura de decisión se satisface con 2 pruebas (una que dé verdadero y otra falso) y la de condiciones con 2 pruebas (todas las condiciones verdaderas y todas falsas), pero sus conjuntos mínimos no son iguales en capacidad. ([SE-454](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](../r/resultado.md), [Cobertura de condiciones](./cobertura-de-condiciones.md), [HIL](../h/hil.md), [MC/DC](../m/mc-dc.md), [Par de independencia](../p/par-de-independencia.md), [SIL](../s/sil.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-448](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Cobertura de controles](./cobertura-de-controles.md) · [Cobertura de diagnóstico →](./cobertura-de-diagnostico.md)
