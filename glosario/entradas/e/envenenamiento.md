# Envenenamiento

[↑ Glosario](../../README.md) · [← Enumeración de identificadores](./enumeracion-de-identificadores.md) · [Envidia de características →](./envidia-de-caracteristicas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Manipulación de los datos de entrenamiento para alterar el modelo.

Definición de trabajo de [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md).

## Por qué importa

En [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), el tema «Envenenamiento y puerta trasera» importa porque con pocas filas se implanta un comportamiento sin dañar la métrica.

## Cómo funciona

Según [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md):

En un sistema de aprendizaje automático hay cinco activos: la entrada, el modelo, los datos de entrenamiento y sus etiquetas, el registro de modelos y la interfaz de consulta. Cada atacante tiene un acceso: quien envía entradas (cualquier usuario), quien consulta mucho (un cliente con interfaz abierta), quien aporta datos (un proveedor, un usuario que genera etiquetas), quien toca el registro (una persona interna o una cuenta comprometida). El modelo de amenazas de `SE-457` aplica: para cada activo y acceso se anota la amenaza, la medida y la defensa. La taxonomía del NIST organiza estas amenazas en evasión, envenenamiento y ataques de privacidad, entre otras, y da un vocabulario común.

Según [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md):

El equipo de *Avisos-ML* escribe su modelo de amenazas. Activos: el modelo, los datos de comportamiento de estudiantes, las etiquetas, el registro y la interfaz. Para cada uno, un atacante y una prueba. Evasión: se mide la fracción de marcados que evaden con las tres características autodeclaradas y se decide aceptar el riesgo, documentado, porque el costo es un recordatorio no enviado; se retira la tasa de lectura declarada del modelo y se reemplaza por una medida del sistema. Extracción: se limita a 1 000 consultas por cuenta y por día y se devuelve una clasificación en lugar de la probabilidad. Envenenamiento: los datos de proveedores externos pasan por una revisión de procedencia y una prueba de disparadores sobre un conjunto de combinaciones raras.

## Ejemplo

Ejemplo de [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos-ML* escribe su modelo de amenazas. Activos: el modelo, los datos de comportamiento de estudiantes, las etiquetas, el registro y la interfaz. Para cada uno, un atacante y una prueba. Evasión: se mide la fracción de marcados que evaden con las tres características autodeclaradas y se decide aceptar el riesgo, documentado, porque el costo es un recordatorio no enviado; se retira la tasa de lectura declarada del modelo y se reemplaza por una medida del sistema. Extracción: se limita a 1 000 consultas por cuenta y por día y se devuelve una clasificación en lugar de la probabilidad.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md)) son: Los ataques son implementaciones propias y simples sobre modelos y datos sintéticos; el disparador, el presupuesto de consultas y los atacantes son construcciones del autor. Las cifras muestran mecanismos (la fragilidad cerca de la frontera, la evasión con características controlables, la puerta trasera con pocas filas, la copia con pocas consultas y la brecha de pertenencia), no el riesgo de ningún sistema real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](../m/modelo.md), [Característica autodeclarada](../c/caracteristica-autodeclarada.md), [Evasión](./evasion.md), [Extracción](./extraccion.md), [Inferencia de pertenencia](../i/inferencia-de-pertenencia.md), [Presupuesto de consultas](../p/presupuesto-de-consultas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Enumeración de identificadores](./enumeracion-de-identificadores.md) · [Envidia de características →](./envidia-de-caracteristicas.md)
