# Presupuesto de consultas

[↑ Glosario](../../README.md) · [← Presupuesto de complejidad](./presupuesto-de-complejidad.md) · [Presupuesto de contexto →](./presupuesto-de-contexto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Número de consultas que un atacante puede hacer.

Definición de trabajo de [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md).

## Por qué importa

La clase donde se define, [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), existe con este propósito: la clase existe para que incorpores a la superficie de ataque de un sistema las debilidades propias del aprendizaje automático, que ni un análisis de código ni un escáner de vulnerabilidades revelan, porque no están en el código sino en el comportamiento aprendido.

## Cómo funciona

Según [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md):

Con un modelo que solo se puede consultar (el boosting de *Avisos-ML*), el atacante prueba valores de las características que controla y mira la respuesta. Se probaron, para 150 estudiantes marcados, candidatos aleatorios de las tres características controlables: con 10 consultas, 95 de 150 (63,3 %) lograron dejar de ser marcados; con 50, 118 (78,7 %); con 200, 120 (80,0 %). Con diez consultas y sin ninguna información del interior del modelo, casi dos tercios evaden. El presupuesto de consultas importa y se limita con tasas por cuenta, detección de patrones de sondeo y, cuando se puede, devolviendo menos información (una clasificación en lugar de una probabilidad).

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md)) son: Los ataques son implementaciones propias y simples sobre modelos y datos sintéticos; el disparador, el presupuesto de consultas y los atacantes son construcciones del autor. Las cifras muestran mecanismos (la fragilidad cerca de la frontera, la evasión con características controlables, la puerta trasera con pocas filas, la copia con pocas consultas y la brecha de pertenencia), no el riesgo de ningún sistema real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Característica autodeclarada](../c/caracteristica-autodeclarada.md), [Envenenamiento](../e/envenenamiento.md), [Evasión](../e/evasion.md), [Extracción](../e/extraccion.md), [Inferencia de pertenencia](../i/inferencia-de-pertenencia.md), [Puerta trasera](./puerta-trasera.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Presupuesto de complejidad](./presupuesto-de-complejidad.md) · [Presupuesto de contexto →](./presupuesto-de-contexto.md)
