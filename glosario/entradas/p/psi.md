# PSI

[↑ Glosario](../../README.md) · [← Pseudolocalización](./pseudolocalizacion.md) · [Publicación y repositorio →](./publicacion-y-repositorio.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Índice de estabilidad de la población, comparación de dos distribuciones por tramos.

Definición de trabajo de [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md).

## Por qué importa

En [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md), el tema «PSI y KS» importa porque detectan cambios de distribución con falsas alarmas y huecos.

## Cómo funciona

Según [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md):

El PSI compara dos distribuciones por tramos: suma, sobre los tramos, la diferencia entre las proporciones multiplicada por el logaritmo de su cociente. Se calcula con los tramos de la referencia (por cuantiles) y se suele leer con las convenciones de que por debajo de 0,1 el cambio es pequeño y por encima de 0,2 es grande. Son convenciones, no leyes: dependen del número de tramos, del tamaño de la ventana y de la naturaleza de la variable. Con la carga de tareas, que toma pocos valores enteros, el cuantil de la referencia deja tramos muy desiguales y el PSI es un instrumento torpe, un recordatorio de que cada característica necesita su propia calibración.

Según [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md):

El equipo de *Avisos-ML* redefine su monitoreo en tres capas. Calidad de entrada: comprobaciones de rango y nulos por característica con un umbral del 1 %, que bloquean el lote y degradan a la regla (`SE-601`), con dueño operaciones. Distribución: PSI por característica sobre ventanas diarias de 5 000 observaciones, con umbral de 0,2 como ticket de baja urgencia con dueño datos, y tasa de marcados por segmento con una guarda de 10 puntos. Etiquetas: AUC semanal por segmento con las etiquetas de hace siete días, y una muestra de 200 casos revisados cada semana para detectar caídas grandes antes.

## Ejemplo

Ejemplo de [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos-ML* redefine su monitoreo en tres capas. Calidad de entrada: comprobaciones de rango y nulos por característica con un umbral del 1 %, que bloquean el lote y degradan a la regla (`SE-601`), con dueño operaciones. Distribución: PSI por característica sobre ventanas diarias de 5 000 observaciones, con umbral de 0,2 como ticket de baja urgencia con dueño datos, y tasa de marcados por segmento con una guarda de 10 puntos. Etiquetas: AUC semanal por segmento con las etiquetas de hace siete días, y una muestra de 200 casos revisados cada semana para detectar caídas grandes antes.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se midió el PSI de la carga con 300 ventanas sin deriva y 300 con una deriva de media de la carga de +0,5, +1,0 y +2,0 tareas, para ventanas de 100, 500, 2 000 y 10 000 observaciones. ([SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), [SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estabilidad](../e/estabilidad.md), [Índice](../i/indice.md), [Deriva de concepto](../d/deriva-de-concepto.md), [Deriva de covariables](../d/deriva-de-covariables.md), [KS](../k/ks.md), [Política de reentrenamiento](./politica-de-reentrenamiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Pseudolocalización](./pseudolocalizacion.md) · [Publicación y repositorio →](./publicacion-y-repositorio.md)
