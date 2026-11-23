# Característica autodeclarada

[↑ Glosario](../../README.md) · [← Característica](./caracteristica.md) · [Característica de calidad →](./caracteristica-de-calidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Entrada que el usuario controla.

Definición de trabajo de [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md).

## Por qué importa

En [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), el tema «Características autodeclaradas» importa porque el atacante las controla y las puede optimizar.

## Cómo funciona

Según [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md):

El equipo de *Avisos-ML* escribe su modelo de amenazas. Activos: el modelo, los datos de comportamiento de estudiantes, las etiquetas, el registro y la interfaz. Para cada uno, un atacante y una prueba. Evasión: se mide la fracción de marcados que evaden con las tres características autodeclaradas y se decide aceptar el riesgo, documentado, porque el costo es un recordatorio no enviado; se retira la tasa de lectura declarada del modelo y se reemplaza por una medida del sistema. Extracción: se limita a 1 000 consultas por cuenta y por día y se devuelve una clasificación en lugar de la probabilidad. Envenenamiento: los datos de proveedores externos pasan por una revisión de procedencia y una prueba de disparadores sobre un conjunto de combinaciones raras.

Según [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md):

**Corrección.** Se sustituye la característica autodeclarada por una medida del sistema, se añade la evasión con características controlables a la batería de pruebas y se agrega a las guardas la tasa de marcados por segmento, que ya existía en la sombra de `SE-607`. La lección es que el ataque no fue técnico sino de uso, y que un control sobre lo que el usuario puede manipular valía más que un modelo más robusto.

## Ejemplo

Ejemplo de [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos-ML* escribe su modelo de amenazas. Activos: el modelo, los datos de comportamiento de estudiantes, las etiquetas, el registro y la interfaz. Para cada uno, un atacante y una prueba. Evasión: se mide la fracción de marcados que evaden con las tres características autodeclaradas y se decide aceptar el riesgo, documentado, porque el costo es un recordatorio no enviado; se retira la tasa de lectura declarada del modelo y se reemplaza por una medida del sistema. Extracción: se limita a 1 000 consultas por cuenta y por día y se devuelve una clasificación en lugar de la probabilidad.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md)) son: Los ataques son implementaciones propias y simples sobre modelos y datos sintéticos; el disparador, el presupuesto de consultas y los atacantes son construcciones del autor. Las cifras muestran mecanismos (la fragilidad cerca de la frontera, la evasión con características controlables, la puerta trasera con pocas filas, la copia con pocas consultas y la brecha de pertenencia), no el riesgo de ningún sistema real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Envenenamiento](../e/envenenamiento.md), [Evasión](../e/evasion.md), [Extracción](../e/extraccion.md), [Inferencia de pertenencia](../i/inferencia-de-pertenencia.md), [Presupuesto de consultas](../p/presupuesto-de-consultas.md), [Puerta trasera](../p/puerta-trasera.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Características autodeclaradas».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Característica](./caracteristica.md) · [Característica de calidad →](./caracteristica-de-calidad.md)
