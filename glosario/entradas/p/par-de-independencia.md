# Par de independencia

[↑ Glosario](../../README.md) · [← Paquete trazable](./paquete-trazable.md) · [Paralelismo →](./paralelismo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Dos vectores que difieren solo en una condición y dan resultados distintos.

Definición de trabajo de [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md).

## Por qué importa

La clase donde se define, [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md), existe con este propósito: la clase existe para que sepas qué mide cada criterio de cobertura, por qué la **cobertura de condición/decisión modificada** (MC/DC) es la que se exige en el nivel más alto de la aviación, y cómo se combinan la simulación en software (SIL), el banco de pruebas con hardware (HIL) y las pruebas en el sistema real para verificar un controlador crítico.

## Cómo funciona

[SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md)) son: La decisión, los 17 mutantes, la planta y el retardo son del autor; no hay banco con hardware real; la cobertura se calcula con código propio y no con una herramienta calificada; las normas de pago no se reproducen. El siguiente paso, `SE-455`, junta todas las miradas en un taller: analizar un fallo real, el del Therac-25, frente a las ideas de las normas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Resultado](../r/resultado.md), [Cobertura de condiciones](../c/cobertura-de-condiciones.md), [Cobertura de decisión](../c/cobertura-de-decision.md), [HIL](../h/hil.md), [MC/DC](../m/mc-dc.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Paquete trazable](./paquete-trazable.md) · [Paralelismo →](./paralelismo.md)
