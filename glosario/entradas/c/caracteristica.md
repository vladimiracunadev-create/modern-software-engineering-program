# Característica

[↑ Glosario](../../README.md) · [← Captura de cambios](./captura-de-cambios.md) · [Característica autodeclarada →](./caracteristica-autodeclarada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

En aprendizaje automático, una **característica** (*feature*) es una variable de entrada calculada a partir de eventos anteriores a la decisión ([SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md)). Las características son lo que el modelo ve; el valor que debe predecir es la etiqueta.

## Por qué importa

La condición «anteriores a la decisión» es el punto de la definición. Una característica que contiene información que no estará disponible en el momento de decidir produce una **fuga**: el modelo parece excelente fuera de línea y falla en producción.

## Cómo funciona

[SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md) explica que la causa más frecuente de fuga no es un descuido grande sino una **ventana mal cortada**: un agregado que incluye el día de la decisión, una normalización calculada con todo el conjunto, un identificador que codifica el resultado. En su medición, un modelo con una característica contaminada («entregas tardías de la semana» que incluye la entrega misma) alcanzó un AUC de 0,987 frente a 0,851 sin ella: 0,136 de mejora ficticia.

## Ejemplo

El equipo de *Avisos* descubre que su AUC de 0,98 era fuga. Define una regla: toda característica nueva se documenta con su fuente, su ventana y su «disponible desde», y una prueba recalcula la característica sobre un historial truncado en el instante de decisión; si el valor cambia al añadir el futuro, la prueba falla.

## Errores y confusiones comunes

Medir calidad con la característica contaminada; calcular normalizaciones con todo el conjunto; olvidar guardar con cada predicción las entradas y la versión del modelo.

## Límites y cuándo no aplica

La prueba de truncamiento detecta fugas temporales, no sesgos de otra naturaleza. Los números de la clase son de un laboratorio con datos sintéticos.

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
