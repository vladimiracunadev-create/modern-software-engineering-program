# Fallo latente

[↑ Glosario](../../README.md) · [← Fallo inyectado](./fallo-inyectado.md) · [Fallo metaestable →](./fallo-metaestable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Fallo de un mecanismo de seguridad que no se manifiesta hasta que se necesita.

Definición de trabajo de [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md).

## Por qué importa

La clase donde se define, [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), existe con este propósito: la clase existe para que entiendas cómo el sector del automóvil convierte un análisis de peligros en un nivel de rigor de desarrollo y cómo se demuestra que los mecanismos de diagnóstico del producto cubren lo que dicen cubrir.

## Cómo funciona

Según [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md):

Para el hardware, la norma pide métricas que cuantifican qué fracción de las tasas de fallo peligrosas queda cubierta por diagnóstico: una de fallo único (cuánto de la tasa total no queda como fallo de un solo punto o residual), una de fallo latente y una probabilidad total de fallo de hardware peligroso. El cálculo de la primera es sencillo: un menos la tasa no cubierta dividida por la tasa total. En el laboratorio, con cuatro componentes de 200 FIT en total, el diseño A (diagnóstico mínimo) deja 78,5 FIT sin cubrir y su métrica es 60,7 %; el diseño B (diagnóstico por componente) deja 3,9 FIT y llega a 98,1 %.

## Ejemplo

Caso medido en la sección «Dónde termina el diagnóstico: causa común y fallos latentes» de [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md):

El 100 % vale para el modelo de fallos usado: un bit, un fallo a la vez, canal B sano. Un fallo de causa común (el mismo error de especificación en ambos canales) o un fallo en el propio comparador (un fallo latente de diagnóstico) quedan fuera. El análisis de dependientes pide buscar causas comunes (misma alimentación, mismo reloj, mismo compilador, mismo equipo) y cubrir los fallos de los mecanismos de seguridad con sus propias comprobaciones.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Para el hardware, la norma pide métricas que cuantifican qué fracción de las tasas de fallo peligrosas queda cubierta por diagnóstico: una de fallo único (cuánto de la tasa total no queda como fallo de un solo punto o residual), una de fallo latente y una probabilidad total de fallo de hardware peligroso. ([SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Seguridad](../s/seguridad.md).
- **Ver también:** [Mecanismo](../m/mecanismo.md), [ASIL](../a/asil.md), [Cobertura de diagnóstico](../c/cobertura-de-diagnostico.md), [Descomposición](../d/descomposicion.md), [FIT](./fit.md), [Objetivo de seguridad](../o/objetivo-de-seguridad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Fallo inyectado](./fallo-inyectado.md) · [Fallo metaestable →](./fallo-metaestable.md)
