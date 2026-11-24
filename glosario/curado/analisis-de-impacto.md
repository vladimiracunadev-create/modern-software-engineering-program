# Análisis de impacto

## Definición

**Análisis de impacto** es la determinación de los elementos que un cambio puede afectar, a partir de los enlaces entre artefactos. El sentido principal es el de `SE-151` y `SE-168`: dado un requisito o artefacto que cambia, su alcance es el conjunto de artefactos alcanzables siguiendo los enlaces hacia sus consecuencias. En `SE-449` (dispositivos médicos, IEC 62304) el mismo término se aplica a la evaluación del efecto de un cambio sobre riesgos, requisitos y pruebas, con el rigor que la norma exige.

## Por qué importa

Responde, antes de tocar nada, cuánto hay que revisar y a quién avisar. Cambia la decisión de aceptar o no un cambio y la de estimar su costo. Sin él, el riesgo es olvidar algo: modificar un requisito y no actualizar la prueba que lo verificaba, o el módulo que dependía de él.

## Cómo funciona

El mecanismo es un recorrido de grafo. Según `SE-151`, dado un cambio en un requisito se recorren los enlaces: las pruebas que lo verifican, los módulos que esas pruebas ejercitan y los requisitos que dependen de él. El tamaño del conjunto resultante estima el costo del cambio y el riesgo de olvido. `SE-168` precisa que es una **cota superior**: no todo lo alcanzable necesita cambiar, pero todo lo alcanzable merece mirarse.

La calidad del resultado depende de la densidad del grafo. Pocos enlaces por artefacto acotan el alcance; demasiados lo disparan. Dos síntomas diagnostican la matriz: si casi cualquier cambio alcanza casi todo el sistema, la matriz no ayuda a decidir (se enlazó todo con todo); si el alcance es siempre cero, probablemente faltan enlaces. Un alcance grande no es malo por sí mismo: señala que el cambio merece una revisión específica.

## Ejemplo

En la cadena del requisito conductor de `SE-151` cada artefacto lleva una etiqueta y un verificador comprueba los enlaces al integrar. Si cambia el tope de penalización por entrega tardía, se recorre el enlace hacia las pruebas que lo verifican y hacia el módulo de cálculo; el resultado es una lista concreta de artefactos a revisar y de personas a avisar, antes de modificar nada.

## Errores y confusiones comunes

- **Casi todo cambio «afecta» a casi todo.** Se enlazó todo con todo; corrección de `SE-151`: reducir los enlaces a los que responden preguntas concretas.
- **Matriz en un documento que nadie actualiza.** Una auditoría tarda un día en encontrar una prueba; corrección: etiquetar la prueba y verificar al integrar.
- **Leer la cota superior como lista de cambios obligatorios.** Es lo que hay que revisar, no lo que hay que modificar.
- **Confundir enlace con evidencia.** Que exista un enlace no prueba que la verificación sea buena.

## Límites y cuándo no aplica

El análisis solo ve lo que está enlazado: dependencias implícitas (comportamiento compartido, datos comunes, configuración) no aparecen si nadie las registró. Las clases lo practican sobre un módulo de juguete con datos sintéticos, no sobre un repositorio real, y las tasas de deterioro de los enlaces son hipótesis. En un contexto regulado (`SE-449`) el análisis es una obligación documentada; en uno informal puede bastar con una revisión de las pruebas y consumidores directos.
