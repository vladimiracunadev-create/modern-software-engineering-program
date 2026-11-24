# Línea base

## Definición

En ingeniería de requisitos (SE-153), una **línea base** es una versión acordada del conjunto de requisitos que sirve de referencia y solo cambia por un proceso controlado. El programa usa la palabra con otros matices cercanos: en SE-527, los valores de las métricas de un sistema antes de un cambio, con su incertidumbre, contra los que se compara después; en SE-476, el comportamiento de la versión anterior, medido en paralelo, contra el que se compara el canario; en SE-601, una regla o modelo simple con el que se compara un modelo de ML. El hilo común es *lo contra lo que se compara*.

## Por qué importa

Hace posible responder preguntas que, sin referencia, no tienen respuesta: «¿esto está dentro del alcance?», «¿mejoró algo?», «¿cambió el comportamiento?». Sin línea base el alcance se mueve con cada edición, y una mejora se afirma sin saber de dónde se parte.

## Cómo funciona

En el sentido de SE-153, la línea base es una versión del conjunto de requisitos que el equipo acordó; lo que se construye, se prueba y se entrega se mide contra ella. No significa que no pueda cambiar: significa que cambia **de forma controlada**, mediante una solicitud de cambio con análisis de impacto y decisión, y que siempre se sabe contra cuál versión se trabaja. Para ello necesita identidad estable (etiqueta, commit o hash normalizado). La clase propone una prueba de regresión que verifica el hash normalizado de la línea base y falla si cambia sin una solicitud registrada.

En el sentido de medición (SE-527), la línea base son las métricas **antes** del cambio, con su incertidumbre. Un error típico: afirmar una mejora con 20 cambios porque la línea base se midió sin incertidumbre; la corrección es declarar el intervalo y ampliar la muestra. En el sentido del canario (SE-476), la versión anterior se mide en paralelo, no en un momento anterior, para que las condiciones sean comparables. En ML (SE-601), una línea base simple (por ejemplo, predecir la media) dice cuánto aporta realmente un modelo complejo.

## Ejemplo

SE-153 muestra una solicitud de cambio con su análisis y decisión sobre la línea base 1: el cambio propone modificar un tope de penalización; el análisis recorre las dependencias y lista requisitos y pruebas afectados; la decisión lo aprueba y se crea la línea base 2 con nuevo hash normalizado. Hasta entonces, el trabajo se mide contra la 1.

## Errores y confusiones comunes

- **Nadie sabe cuál era la versión acordada**: no hay línea base identificada; corrección: etiquetar cada versión acordada y registrar su hash normalizado.
- **Afirmar una mejora sin línea base con incertidumbre** (SE-527).
- **Confundirla con una congelación absoluta**: puede cambiar, pero de forma controlada.
- **Comparar con una línea base tomada en otras condiciones.**

## Límites y cuándo no aplica

Una línea base rígida frena la adaptación cuando el aprendizaje del proyecto es alto y el costo de cambiar es bajo: ahí conviene líneas base ligeras por iteración. Y una línea base mal elegida (una referencia demasiado débil en ML, por ejemplo) hace parecer buenos resultados mediocres.
