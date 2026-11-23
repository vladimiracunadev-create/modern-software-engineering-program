# SIL

[↑ Glosario](../../README.md) · [← Siguiente paso](./siguiente-paso.md) · [Silo y pool →](./silo-y-pool.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Simulación del controlador contra un modelo de planta en software.

Definición de trabajo de [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md).

## Por qué importa

En [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md), el tema «SIL» importa porque da volumen y repetibilidad.

## Cómo funciona

Según [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md):

En la **simulación en software (SIL)** el código del controlador se ejecuta contra un modelo de la planta en un computador: es repetible, barata y permite miles de escenarios, pero el modelo no tiene el retardo, el ruido ni los fallos reales del hardware. En el **banco con hardware (HIL)**, el controlador real (o su procesador) corre conectado a una simulación en tiempo real de la planta por sus entradas y salidas reales: añade tiempo real, convertidores, interrupciones y electricidad. En el **sistema real**, se añade el entorno físico. En el laboratorio, 300 escenarios de calentamiento con el limitador en 245 °C no violan el límite de 250 °C con retardos del sensor de 0, 2 y 5 muestras; con 10 muestras, 30 escenarios lo violan; con 15, 52.

Según [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md):

Ejercita el hardware real: convertidores, tiempos, interrupciones, el ruido eléctrico. El SIL es más barato y repetible. La práctica habitual es descubrir con SIL, confirmar con HIL y validar con el sistema.

## Ejemplo

Ejemplo de [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md) (sección «Preguntas frecuentes»):

Ejercita el hardware real: convertidores, tiempos, interrupciones, el ruido eléctrico. El SIL es más barato y repetible. La práctica habitual es descubrir con SIL, confirmar con HIL y validar con el sistema.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En la **simulación en software (SIL)** el código del controlador se ejecuta contra un modelo de la planta en un computador: es repetible, barata y permite miles de escenarios, pero el modelo no tiene el retardo, el ruido ni los fallos reales del hardware. ([SE-454](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Controlador](../c/controlador.md), [Modelo](../m/modelo.md), [Cobertura de condiciones](../c/cobertura-de-condiciones.md), [Cobertura de decisión](../c/cobertura-de-decision.md), [HIL](../h/hil.md), [MC/DC](../m/mc-dc.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Siguiente paso](./siguiente-paso.md) · [Silo y pool →](./silo-y-pool.md)
