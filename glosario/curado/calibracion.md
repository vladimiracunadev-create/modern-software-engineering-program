# Calibración

## Definición

**Calibración** es la correspondencia entre la confianza que anuncia un pronóstico y la frecuencia con que se cumple. El sentido principal es el de `SE-191`: un pronóstico está calibrado si el resultado real cae por debajo de su percentil 85 el 85 % de las veces. El programa lo reutiliza con el mismo núcleo en `SE-604` (probabilidad predicha frente a frecuencia observada en un modelo), en `SE-553` (confianza declarada de una respuesta generativa frente a su tasa de acierto) y en `SE-539` (probabilidad declarada en una revisión de decisión frente a lo que ocurrió).

## Por qué importa

Cambia si un número se puede usar para decidir. Un percentil o una probabilidad solo valen si significan lo que dicen: si «85 %» se cumple el 60 % de las veces, quien planifica con él está asumiendo un riesgo mayor del que cree. La calibración es la prueba de que el lenguaje de la incertidumbre, ya sea fechas de entrega o probabilidades de un modelo, es fiable.

## Cómo funciona

Se comprueba contra la realidad, no con argumentos. `SE-191` propone una retrospectiva: simular muchos proyectos con un proceso conocido, pronosticar cada uno con su historia y contar cuántas veces se cumplió el pronóstico. Es, según la clase, la única manera de saber si «85 %» significa 85 %.

Dos fuentes de descalibración dominan en la planificación. La primera es la **historia corta**: con pocas semanas de datos se subestima la incertidumbre sobre la propia media, y el intervalo sale demasiado estrecho. La segunda son los **efectos que el modelo no incluye**, como el crecimiento del alcance: un pronóstico hecho solo con la historia de rendimiento supone que el trabajo pendiente no cambia. La corrección es ensanchar el intervalo o apoyarse en una clase de referencia cuando la historia es de menos de unas doce semanas.

En modelos (`SE-604`) la lógica es idéntica: se agrupan las predicciones por probabilidad declarada y se compara con la frecuencia observada en cada grupo.

## Ejemplo

En el taller de `SE-191` se simulan muchos proyectos con un proceso conocido. Para cada uno se pronostica la fecha con la historia disponible y se cuenta en cuántos el real quedó por debajo del percentil 85. Si el cumplimiento resulta inferior al 85 %, el pronóstico está sobreconfiado, y el taller muestra cuánto con el propio proceso. La clase observa que, cuanta más historia, mejor, pero con pocas semanas conviene ensanchar el intervalo.

## Errores y confusiones comunes

- **Confundir calibración con precisión.** Un pronóstico puede ser impreciso (intervalo ancho) y estar bien calibrado; uno estrecho puede estar descalibrado.
- **Creer que un percentil «vale» sin comprobarlo.** Sin retrospectiva, «85 %» es una etiqueta.
- **Ignorar el crecimiento del alcance.** El modelo con solo rendimiento histórico sobreestima su confianza.
- **Evaluar con una sola ocurrencia.** Un acierto o fallo aislado no dice nada: la calibración es una propiedad de muchas predicciones.

## Límites y cuándo no aplica

Requiere muchas predicciones comparables; con pocos casos la frecuencia observada es ruidosa y no permite concluir. Las clases lo practican con procesos simulados de proceso conocido, que no incluyen todas las perturbaciones de un proyecto real. Y no sustituye a la discriminación: un modelo bien calibrado puede ser inútil si da la misma probabilidad a todo. Es una condición necesaria para confiar en una probabilidad, no suficiente.
