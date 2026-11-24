# Mutante equivalente

## Definición

Un **mutante equivalente** es una variante de un programa (o de una regla) producida por una mutación que no cambia ninguna salida observable sobre el dominio considerado, por lo que ninguna prueba puede distinguirla del original: no se puede «matar» (SE-541, SE-426, SE-464, SE-157, SE-265).

## Por qué importa

Corrige la lectura de una cifra de mutación. Si una suite deja sobrevivir algunos mutantes, no todos indican una prueba que falta: algunos son equivalentes y perseguirlos cuesta tiempo sin valor. SE-541 lo resume: cualquier cifra de mutantes muertos debe calcularse sobre los **no equivalentes**. Sin esa distinción, se castiga a una suite buena o se persigue un 100 % imposible.

## Cómo funciona

La prueba de mutación introduce defectos pequeños y deliberados (cambiar `>=` por `>`, quitar un rechazo) y cuenta cuántos detecta la suite. Un mutante sobrevive si ninguna prueba falla con él. Entonces hay dos posibilidades: la suite no tiene la prueba necesaria, o el mutante no cambia el comportamiento. En el segundo caso es equivalente. Decidir si un mutante es equivalente es, en general, un problema indecidible; en la práctica se revisa a mano.

SE-541 da el ejemplo de la clase: cambiar `offset != 1` por `offset > 1` no altera el comportamiento cuando los únicos umbrales posibles son 72, 24 y 1; ningún oráculo puede matarlo porque no hay diferencia observable. Los dos equivalentes del laboratorio (M19 y M20) sobreviven a los cinco oráculos, y eso es lo correcto.

SE-464 añade una fuente frecuente en seguridad: la **defensa en profundidad**. Cuando dos comprobaciones rechazan lo mismo, quitar una no cambia nada visible, y el mutante resultante es equivalente. La conclusión no es borrar la comprobación redundante (la redundancia es intencional), sino anotar por qué el mutante sobrevive. Y SE-157 y SE-265 usan la misma noción para reglas: una variante que no cambia ninguna salida sobre el dominio considerado.

## Ejemplo

Una regla de plazos solo acepta desplazamientos de 72, 24 o 1 hora. El código `if offset != 1` se muta a `if offset > 1`. Con esos tres valores, ambas condiciones dan el mismo resultado en todo el dominio; ninguna prueba puede distinguirlas. De 20 mutantes, 2 son equivalentes y la suite mata los otros 18: la puntuación correcta es 18/18 (100 %), no 18/20 (90 %). (Escenario construido con los datos de la clase.)

## Errores y confusiones comunes

- **Contar equivalentes como fallos de la suite.**
- **Escribir pruebas contorsionadas para «matar» un equivalente**, lo que fija detalles internos irrelevantes.
- **Declarar equivalente un mutante que no lo es** solo porque es difícil de matar: hay que comprobarlo sobre el dominio.
- **Confundir equivalente con superviviente**: todo equivalente sobrevive, pero no todo superviviente es equivalente.

## Límites y cuándo no aplica

La equivalencia depende del dominio considerado: un mutante equivalente hoy puede dejar de serlo si el dominio se amplía (por ejemplo, aparecen nuevos umbrales). Revisar equivalentes a mano no escala en bases de código grandes; las herramientas tienen heurísticas imperfectas. Si el dominio no está bien definido, no se puede afirmar equivalencia.
