# Ejecución en sombra

[↑ Glosario](../../README.md) · [← Ejecución durable](./ejecucion-durable.md) · [Ejecución gestionada →](./ejecucion-gestionada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

El candidato calcula con tráfico real sin que sus decisiones se usen.

Definición de trabajo de [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md).

## Por qué importa

La clase donde se define, [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md), existe con este propósito: la clase existe para que pongas un modelo nuevo en producción sin apostar a todos los usuarios a la vez.

## Cómo funciona

Según [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md):

En la ejecución en sombra el candidato recibe una copia de cada petición, calcula su puntuación y nadie la usa. No necesita etiquetas, que llegan siete días después: compara las decisiones de ambos modelos. En el laboratorio, el desacuerdo global fue del 21,4 % y la tasa de marcados global pasó de 47,3 % a 26,4 %. Por segmento fue distinto: en el 83 % restante, el vigente marcaba al 45,0 % y el candidato al 31,1 % (desacuerdo del 14,6 %, correlación de puntajes 0,947); en el segmento móvil y nocturno, el vigente marcaba al 58,7 % y el candidato al 3,6 % (desacuerdo del 55,1 %).

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md)) son: El candidato, la anomalía de etiquetado, el tráfico y la simulación de potencia son construcciones del autor; los números muestran que el promedio puede aprobar lo que daña a un segmento, que la sombra ve sin etiquetas y que la potencia de un canary pequeño es baja. No se evaluó ninguna plataforma de despliegue y el tiempo de rollback es de archivos locales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Candidato](../c/candidato.md), [Escalón de tráfico](./escalon-de-trafico.md), [Guarda](../g/guarda.md), [Potencia](../p/potencia.md), [Registro de modelos](../r/registro-de-modelos.md), [Retroceso](../r/retroceso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Ejecución durable](./ejecucion-durable.md) · [Ejecución gestionada →](./ejecucion-gestionada.md)
