# Variante defectuosa

## Definición

Una **variante defectuosa** es una copia del código (o de un programa, de un manifiesto o de un producto) con un cambio pequeño introducido a propósito, cuyo objetivo es comprobar si las pruebas lo detectan. Es el término que el programa usa para lo que la bibliografía llama **mutante** (*mutant*): `SE-422` la define como una copia con un cambio mecánico pequeño, «muerta» si alguna prueba falla y «superviviente» si todas pasan; `SE-541` usa «muere» y «sobrevive» respecto de los oráculos; `SE-426` la presenta junto con la mutación y el *fuzzing*. Quince clases la definen con variantes de redacción, siempre con el mismo núcleo: un defecto plantado para medir la capacidad de detección.

## Por qué importa

Una prueba que nunca ha fallado no demuestra que pueda fallar. La variante defectuosa responde a esa pregunta: si se rompe el código a propósito y todas las pruebas siguen pasando, la prueba no protege lo que parecía proteger. `SE-576` lo formula como comprobar que una prueba puede fallar. La alternativa habitual, la cobertura de líneas, responde otra pregunta: no «¿se ejecutó esta línea?», sino «si esta línea cambia, ¿falla algo?» (`SE-426`).

## Cómo funciona

El mecanismo, según `SE-426`, se apoya en un **operador de mutación**: una regla de cambio mecánico, como sustituir `<` por `<=`, `and` por `or`, sumar uno a una constante o negar una condición. Aplicado en cada lugar posible, produce una población de variantes, cada una un error plausible en pequeño. Se ejecuta la suite sobre cada una:

- Si alguna prueba falla, la variante **muere** (la suite la detectó).
- Si todas pasan, la variante **sobrevive**, y hay que clasificarla: caso faltante, aserción débil o variante **equivalente** (un cambio que no altera ninguna salida y que ninguna prueba puede matar), con la razón escrita (`SE-426`).

La **puntuación de mutación** es la fracción de variantes no equivalentes que alguna prueba mata. Se apoya en dos hipótesis con apoyo empírico parcial, no leyes: que los defectos reales son combinaciones de errores pequeños y que una batería que detecta los simples detecta la mayoría de los complejos.

## Ejemplo

En `SE-426`, un módulo de 21 líneas se muta con seis operadores y produce 18 variantes, ninguna equivalente. Se ejecutan cuatro baterías de pruebas. Pasar de la batería A a la B suma 22 puntos de cobertura y no mata ninguna variante más: los casos nuevos ejecutan líneas sin probar los límites. La batería D no tiene ninguna aserción, ejecuta dos tercios de las líneas y mata 6 variantes, todas porque el cambio provoca una excepción: es un detector de caídas, no de comportamientos erróneos. La C llega a 17 de 18 y su único superviviente cambia el redondeo de uno a dos decimales, porque ningún promedio probado tiene segundo decimal. Son datos de un módulo pequeño elegido por la clase.

## Errores y confusiones comunes

- **La cobertura sube y los mutantes muertos no.** Se añadieron casos que ejecutan líneas sin afirmar fronteras; corrección (`SE-426`): medir la puntuación de mutación al añadir casos.
- **Un superviviente que nadie explica.** No se clasifica; hay que decidir si falta un caso, la aserción es débil o es equivalente.
- **Usar la puntuación como probabilidad de detectar defectos reales.** No lo es: es una comparación entre baterías sobre el mismo conjunto de variantes (`SE-426`).

## Límites y cuándo no aplica

La puntuación solo compara baterías sobre el mismo conjunto de variantes: no mide la calidad del producto ni la probabilidad de detectar defectos reales (`SE-426`). Las variantes equivalentes no se pueden matar con ninguna prueba y por eso se excluyen de la puntuación, lo que obliga a clasificar cada superviviente con una razón escrita. Y como el programa usa nombres cercanos (mutante, mutación, variante defectuosa), conviene leerlos como el mismo mecanismo con énfasis distinto: el de la técnica, el del procedimiento y el del objeto.
