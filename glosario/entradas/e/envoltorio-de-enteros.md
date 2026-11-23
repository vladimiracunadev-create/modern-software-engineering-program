# Envoltorio de enteros

[↑ Glosario](../../README.md) · [← Envidia de características](./envidia-de-caracteristicas.md) · [Envoltura de un byte →](./envoltura-de-un-byte.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Resultado módulo 2ⁿ de una operación que excede el rango del tipo.

Definición de trabajo de [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md).

## Por qué importa

La clase donde se define, [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md), existe con este propósito: la clase existe para que entiendas qué hace un estándar de codificación segura, por qué sus reglas son restricciones sobre el lenguaje y no consejos de estilo, y cómo se integra una política así en un proyecto sin convertirla en un rito.

## Cómo funciona

Según [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md):

MISRA C define reglas obligatorias, requeridas y aconsejables para C, con una clasificación entre decidibles (una herramienta puede comprobarlas con certeza) y no decidibles (solo con aproximaciones), y un procedimiento de desviación; sus documentos se distribuyen por la organización que los mantiene. SEI CERT C es un estándar público con reglas (cuya violación suele ser un defecto) y recomendaciones, con ejemplos de código incumplidor y cumplidor y una clasificación de riesgo; incluye reglas sobre el envoltorio de enteros sin signo. La elección entre ellos suele venir impuesta por el cliente o la norma sectorial. Lo transferible es el funcionamiento: reglas escritas, comprobadas por herramienta, con desviaciones justificadas.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- SEI CERT C es un estándar público con reglas (cuya violación suele ser un defecto) y recomendaciones, con ejemplos de código incumplidor y cumplidor y una clasificación de riesgo; incluye reglas sobre el envoltorio de enteros sin signo. ([SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Módulo](../m/modulo.md), [Operación](../o/operacion.md), [Rango](../r/rango.md), [Resultado](../r/resultado.md), [Aserción](../a/asercion.md), [Cota de bucle](../c/cota-de-bucle.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Envidia de características](./envidia-de-caracteristicas.md) · [Envoltura de un byte →](./envoltura-de-un-byte.md)
