# Sonda

## Definición

En el programa, una **sonda** es un valor de entrada elegido por su capacidad de revelar defectos conocidos. Es la definición de trabajo de `SE-429`, en estrategia de pruebas. El término tiene otros dos sentidos, que conviene no mezclar: en `SE-522` es un programa que aplica una operación con el comportamiento antiguo y el nuevo sobre datos representativos y cuenta cuántos resultados difieren; en `SE-599` es una llamada ocasional al nivel superior para saber si ya se recuperó (como en un cortacircuitos semiabierto). Esta entrada desarrolla el de `SE-429` y relaciona los otros.

## Por qué importa

Los valores «típicos» casi nunca fallan. Los defectos viven en los bordes y en los rarezas: la cadena vacía, el espacio, la longitud límite. Elegir sondas con criterio cambia la eficiencia de una batería de pruebas: una lista dirigida encuentra defectos específicos casi siempre, y cadenas aleatorias casi nunca (`SE-429`).

## Cómo funciona

Una sonda se elige por lo que suele romper. `SE-429` da la lista:

- vacío y solo espacios;
- longitudes de borde (79, 80, 81 si el límite es 80);
- caracteres con tilde o combinantes;
- caracteres de control;
- texto bidireccional;
- emoji;
- cadenas que empiezan por un nombre reservado.

Una lista de sondas es una **lista de verificación de entradas**: no sustituye a la exploración, la prepara. La causa de su eficacia es que codifica experiencia sobre *clases* de fallo (los límites, las codificaciones), de modo que cada tipo de dato tiene su propia lista.

En el sentido de `SE-522`, la sonda es una herramienta de migración: aplica el comportamiento antiguo y el nuevo sobre datos representativos y cuenta cuántos resultados difieren, para encontrar cambios silenciosos. Y en `SE-599` es la llamada de prueba que decide si el sistema se recuperó.

## Ejemplo

Un validador de nombres de usuario acepta hasta 80 caracteres. La lista de sondas: `""`, `" "`, una cadena de 79, 80 y 81 caracteres, `"é"` en forma compuesta y descompuesta, `"‮"` (control bidireccional), un emoji, y `"con"` (nombre reservado en Windows). Un validador con el defecto `<= 80` escrito como `< 80` falla con la sonda de 80. Ninguna cadena aleatoria de 1 a 600 caracteres lo encontraría con probabilidad razonable. El código es ilustración del criterio de `SE-429`.

## Errores y confusiones comunes

- **Un validador acepta entradas que no debería.** Solo se probaron valores típicos (`SE-429`); corrección: lista de sondas por tipo de dato.
- **La suite pasa y los datos cambian.** Un cambio silencioso no fue ejercitado por las pruebas (`SE-522`); escribir sondas con datos reales y ampliar el maestro dorado.
- **Tomar la lista como completa.** Es un punto de partida; la exploración añade lo no previsto.
- **Confundir los tres sentidos.** Ver la definición.

## Límites y cuándo no aplica

Las sondas encuentran lo que ya se sabe que suele romper; un defecto de una clase nueva no aparece en la lista. Dependen del tipo de dato: sondas de texto no sirven para fechas ni archivos. La sonda de migración (`SE-522`) solo cubre los datos representativos que se le den. Y una sonda no es una especificación: dice que un valor revela algo, no cuál es el comportamiento correcto; eso lo decide el oráculo.
