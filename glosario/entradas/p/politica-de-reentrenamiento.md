# Política de reentrenamiento

[↑ Glosario](../../README.md) · [← Política de presupuesto](./politica-de-presupuesto.md) · [Política de seguridad de contenido →](./politica-de-seguridad-de-contenido.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Regla que decide cuándo reentrenar.

Definición de trabajo de [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md).

## Por qué importa

En [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md), el tema «Política de reentrenamiento» importa porque cuesta y no siempre mejora.

## Cómo funciona

[SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Caso medido en la sección «Cuatro políticas de reentrenamiento» de [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md):

Se simularon 44 semanas de monitoreo (de la 9 a la 52) con una deriva lineal que combina más carga, menor tasa de lectura y un peso del historial que cae de 1,0 a 0,15; cada semana llegan 3 000 observaciones. El modelo inicial se entrenó con las ocho primeras semanas, con un AUC de referencia de 0,843. Cuatro políticas, con reentrenamiento sobre las siete últimas semanas disponibles:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md)) son: La deriva, el generador, las políticas y los umbrales son construcciones del autor; la sensibilidad del PSI depende de la variable (un entero con pocos valores) y los umbrales de 0,1 y 0,2 son convenciones. La simulación de 44 semanas usa una deriva lineal y una semilla, y las diferencias entre políticas con reentrenamiento (del orden de 0,001) están dentro del ruido. No se evaluó ninguna herramienta de monitoreo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), [SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla](../r/regla.md), [Deriva de concepto](../d/deriva-de-concepto.md), [Deriva de covariables](../d/deriva-de-covariables.md), [KS](../k/ks.md), [PSI](./psi.md), [Referencia](../r/referencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Política de presupuesto](./politica-de-presupuesto.md) · [Política de seguridad de contenido →](./politica-de-seguridad-de-contenido.md)
