# Característica

[↑ Glosario](../../README.md) · [← Captura de cambios](./captura-de-cambios.md) · [Característica autodeclarada →](./caracteristica-autodeclarada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Variable de entrada calculada a partir de eventos anteriores a la decisión.

Definición de trabajo de [SE-602 — Datos de entrenamiento, etiquetas y feature stores](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md).

## Por qué importa

En [SE-602 — Datos de entrenamiento, etiquetas y feature stores](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), el tema «Almacén de características» importa porque reutiliza definiciones y registra versiones.

## Cómo funciona

Según [SE-602 — Datos de entrenamiento, etiquetas y feature stores](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md):

Una fuga ocurre cuando una característica contiene información que no estará disponible en el momento de la decisión. La causa más frecuente no es un descuido grande sino una ventana mal cortada: un agregado que incluye el día de la decisión, una normalización calculada con todo el conjunto, un identificador que codifica el resultado. Se midió con una característica construida con la etiqueta más un poco de ruido, el equivalente a «entregas tardías de la semana» que incluye la entrega misma. Fuera de línea, el modelo con la fuga alcanzó un AUC de 0,987 frente a 0,851 del modelo sin ella: mejor en 0,136.

Según [SE-602 — Datos de entrenamiento, etiquetas y feature stores](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md):

El equipo de *Avisos* descubre que su AUC de 0,98 de la semana pasada era fuga. Define una regla de revisión: toda característica nueva se acompaña de una fila de la tabla de características con su fuente, su ventana y su «disponible desde», y una prueba automatizada que recalcula la característica sobre un historial truncado en el instante de decisión y exige que dé lo mismo que sobre el historial completo. Esa prueba habría fallado con «entregas tardías de siete días» porque el valor cambia al añadir el futuro. Además se acuerda guardar en cada predicción las seis entradas y la versión del modelo.

## Ejemplo

Ejemplo de [SE-602 — Datos de entrenamiento, etiquetas y feature stores](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* descubre que su AUC de 0,98 de la semana pasada era fuga. Define una regla de revisión: toda característica nueva se acompaña de una fila de la tabla de características con su fuente, su ventana y su «disponible desde», y una prueba automatizada que recalcula la característica sobre un historial truncado en el instante de decisión y exige que dé lo mismo que sobre el historial completo. Esa prueba habría fallado con «entregas tardías de siete días» porque el valor cambia al añadir el futuro. Además se acuerda guardar en cada predicción las seis entradas y la versión del modelo.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una fuga ocurre cuando una característica contiene información que no estará disponible en el momento de la decisión. ([SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md))
- Con pocas características y un solo modelo, una función compartida y una tabla versionada alcanzan. ([SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-343](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md), [SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md), [SE-601](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Almacén de características](../a/almacen-de-caracteristicas.md), [Etiqueta](../e/etiqueta.md), [Fuga de información](../f/fuga-de-informacion.md), [Paridad](../p/paridad.md), [Sesgo entre entrenamiento y servicio](../s/sesgo-entre-entrenamiento-y-servicio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-602 — Datos de entrenamiento, etiquetas y feature stores](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (87 clases más lo mencionan; las que más):

[SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md), [SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md), [SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-601](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md), [SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md), [SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Captura de cambios](./captura-de-cambios.md) · [Característica autodeclarada →](./caracteristica-autodeclarada.md)
