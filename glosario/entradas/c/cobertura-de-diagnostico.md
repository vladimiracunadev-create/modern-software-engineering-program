# Cobertura de diagnóstico

[↑ Glosario](../../README.md) · [← Cobertura de decisión](./cobertura-de-decision.md) · [Cobertura de documentación →](./cobertura-de-documentacion.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Fracción de fallos peligrosos que un mecanismo detecta.

Definición de trabajo de [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md).

## Por qué importa

En [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), el tema «Cobertura de diagnóstico» importa porque es lo que vuelve «detectable» un fallo.

## Cómo funciona

[SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Caso medido en la sección «Cobertura de diagnóstico: medida, no declarada» de [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md):

La métrica de arquitectura depende de la cobertura de cada diagnóstico, y esa cobertura se mide inyectando fallos y observando cuáles se detectan. En el laboratorio se inyectan 20 000 fallos de un bit al azar (semilla 47) en tres puntos: la entrada, un valor intermedio y la salida del canal A; con el canal B sano. De ellos, 15 422 producen una desviación mayor que la tolerancia.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md)) son: Las tasas, las coberturas por componente y el cálculo de par son del autor; el modelo de fallos es de un bit; los valores de referencia de las métricas no se verificaron contra la norma de pago; no se reproduce ninguna tabla ni se afirma conformidad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Mecanismo](../m/mecanismo.md), [ASIL](../a/asil.md), [Descomposición](../d/descomposicion.md), [Fallo latente](../f/fallo-latente.md), [FIT](../f/fit.md), [Objetivo de seguridad](../o/objetivo-de-seguridad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Cobertura de decisión](./cobertura-de-decision.md) · [Cobertura de documentación →](./cobertura-de-documentacion.md)
