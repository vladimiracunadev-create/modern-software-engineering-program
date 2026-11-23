# KS

[↑ Glosario](../../README.md) · [← Keyset](./keyset.md) · [KYC →](./kyc.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Distancia máxima entre dos funciones de distribución acumuladas.

Definición de trabajo de [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md).

## Por qué importa

En [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md), el tema «PSI y KS» importa porque detectan cambios de distribución con falsas alarmas y huecos.

## Cómo funciona

[SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Caso medido en la sección «PSI por característica y la prueba KS» de [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md):

Con una deriva de +1,0 en la carga y una ventana de 5 000, el PSI por característica fue 0,259 para la carga y entre 0,000 y 0,004 para las otras cinco: el índice localiza la característica que cambió. La prueba de Kolmogorov y Smirnov, que mide la mayor distancia entre las funciones de distribución acumuladas, dio 0,217 para la carga. Ambas señales localizan el cambio y ninguna dice si importa: eso lo dice la métrica con etiquetas y el peso de la característica en el modelo.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md)) son: La deriva, el generador, las políticas y los umbrales son construcciones del autor; la sensibilidad del PSI depende de la variable (un entero con pocos valores) y los umbrales de 0,1 y 0,2 son convenciones. La simulación de 44 semanas usa una deriva lineal y una semilla, y las diferencias entre políticas con reentrenamiento (del orden de 0,001) están dentro del ruido. No se evaluó ninguna herramienta de monitoreo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), [SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Función](../f/funcion.md), [Deriva de concepto](../d/deriva-de-concepto.md), [Deriva de covariables](../d/deriva-de-covariables.md), [Política de reentrenamiento](../p/politica-de-reentrenamiento.md), [PSI](../p/psi.md), [Referencia](../r/referencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Keyset](./keyset.md) · [KYC →](./kyc.md)
