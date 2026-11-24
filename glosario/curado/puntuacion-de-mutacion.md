# Puntuación de mutación

## Definición

La **puntuación de mutación** es la fracción de mutantes no equivalentes que alguna prueba mata (`SE-426`). `SE-307` la usa en el mismo sentido: la fracción de mutantes no equivalentes que una batería detecta. Mide la capacidad de una batería de pruebas para notar cambios en el código.

## Por qué importa

La cobertura de líneas dice qué se ejecutó, no qué se comprobó. Una batería puede ejecutar todo y afirmar casi nada. La puntuación de mutación responde a otra pregunta: si esta línea cambia, ¿falla algo? La decisión que cambia es cómo se valora una batería de pruebas: por lo que detecta, no por lo que recorre.

## Cómo funciona

Un **mutante** es una copia del programa con un cambio pequeño y deliberado (invertir una comparación, cambiar un `<` por `<=`). Si alguna prueba falla con el mutante, está **muerto**; si todas pasan, sobrevive. Algunos mutantes son **equivalentes**: se comportan igual que el original y ninguna prueba puede distinguirlos; se excluyen del cálculo. La puntuación es:

mutantes muertos ÷ mutantes no equivalentes.

`SE-426` explica por qué difiere de la cobertura. Para una batería con aserciones débiles, la diferencia es grande: ejecutar todas las líneas y no comprobar casi ningún valor da cobertura alta y puntuación baja. Por eso añadir casos que ejecutan líneas sin afirmar fronteras sube la cobertura pero no la cantidad de mutantes muertos; la corrección es medir la puntuación al añadir casos.

La clase aclara su sentido: la puntuación no es una probabilidad de detectar defectos reales; es una **comparación entre baterías sobre el mismo conjunto de mutantes**. `SE-307` la usa como red de seguridad antes de refactorizar: si la puntuación es baja, la batería no detectaría un cambio de comportamiento.

## Ejemplo

El módulo sintético de `SE-426` tiene 21 líneas, 18 mutantes y cuatro defectos escritos por el autor. Una batería recorre todas las líneas (cobertura del 100 %) pero solo mata una parte de los mutantes, porque casi no comprueba valores de frontera. Al añadir casos que afirman los bordes, la puntuación sube. Un mutante que cambia `<` por `<=` sobrevive hasta que un caso lo prueba en el valor exacto.

## Errores y confusiones comunes

- **La cobertura sube y los mutantes muertos no**: se añadieron casos que ejecutan líneas sin afirmar fronteras; se corrige midiendo la puntuación de mutación.
- **Tratarla como probabilidad de hallar defectos reales**.
- **Contar los equivalentes** como supervivientes: falsean la puntuación a la baja.
- **Perseguir el 100 %**: el último tramo suele ser equivalentes o de poco valor.

## Límites y cuándo no aplica

`SE-426` precisa que usó un módulo sintético de 21 líneas, 18 mutantes y cuatro defectos del autor, sin herramienta de mutación ni fuzzer real; los generadores contienen valores que el autor sabía que importaban, y la equivalencia se decidió con una rejilla finita. Decidir si un mutante es equivalente puede ser indecidible en general. Generar y ejecutar mutantes cuesta tiempo, lo que obliga a acotar el alcance en bases de código grandes.
