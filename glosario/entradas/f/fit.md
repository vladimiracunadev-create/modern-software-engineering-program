# FIT

[↑ Glosario](../../README.md) · [← Firmware](./firmware.md) · [Fixture →](./fixture.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Un fallo por 10⁹ horas de operación.

Definición de trabajo de [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md).

## Por qué importa

La clase donde se define, [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), existe con este propósito: la clase existe para que entiendas cómo el sector del automóvil convierte un análisis de peligros en un nivel de rigor de desarrollo y cómo se demuestra que los mecanismos de diagnóstico del producto cubren lo que dicen cubrir.

## Cómo funciona

Según [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md):

Para el hardware, la norma pide métricas que cuantifican qué fracción de las tasas de fallo peligrosas queda cubierta por diagnóstico: una de fallo único (cuánto de la tasa total no queda como fallo de un solo punto o residual), una de fallo latente y una probabilidad total de fallo de hardware peligroso. El cálculo de la primera es sencillo: un menos la tasa no cubierta dividida por la tasa total. En el laboratorio, con cuatro componentes de 200 FIT en total, el diseño A (diagnóstico mínimo) deja 78,5 FIT sin cubrir y su métrica es 60,7 %; el diseño B (diagnóstico por componente) deja 3,9 FIT y llega a 98,1 %.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En el laboratorio, con cuatro componentes de 200 FIT en total, el diseño A (diagnóstico mínimo) deja 78,5 FIT sin cubrir y su métrica es 60,7 %; el diseño B (diagnóstico por componente) deja 3,9 FIT y llega a 98,1 %. ([SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Operación](../o/operacion.md), [ASIL](../a/asil.md), [Cobertura de diagnóstico](../c/cobertura-de-diagnostico.md), [Descomposición](../d/descomposicion.md), [Fallo latente](./fallo-latente.md), [Objetivo de seguridad](../o/objetivo-de-seguridad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Firmware](./firmware.md) · [Fixture →](./fixture.md)
