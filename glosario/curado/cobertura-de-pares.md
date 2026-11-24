# Cobertura de pares

## Definición

La **cobertura de pares** (*pairwise*) es la propiedad de un conjunto de pruebas en el que cada combinación de valores de cada par de factores aparece al menos una vez (SE-176, SE-158, SE-240, SE-298). Es el caso t = 2 de la cobertura combinatoria. Es una métrica de una suite, no de código.

## Por qué importa

Reduce el número de casos sin renunciar a casi nada de lo que importa. El producto completo de factores crece de forma multiplicativa; una tabla de ejemplos con 243 filas nadie la lee ni la ejecuta. Con pares se mantiene una suite pequeña que encuentra la mayoría de los defectos que dependen de una o dos condiciones.

## Cómo funciona

Dados varios factores con sus valores, se construye un conjunto de filas tal que, para cualquier par de factores, todas las combinaciones de sus valores aparezcan en alguna fila. Un algoritmo voraz elige filas que cubran el mayor número de pares aún no cubiertos. SE-176 da un caso: cinco preferencias binarias de la interfaz (movimiento reducido, esquema oscuro, contraste más alto, colores forzados y zoom del 200 %) dan 32 combinaciones; los 40 pares (10 pares de factores × 4 valores) se cubren con solo 6 filas.

La clase mide qué pierde la reducción con una inyección de defectos: 60 defectos que se disparan con una, dos o tres preferencias a la vez (20, 28 y 12). Las 32 combinaciones encuentran los 60; las 6 filas de pares, 55; y 6 filas al azar, 50,4 de media en 200 sorteos. Los 5 defectos que los pares no encuentran son los que exigen tres factores a la vez. La conclusión: la cobertura de pares es un acuerdo económico que encuentra casi todo lo de uno o dos factores y deja lo de tres sin cubrir, y decide según el riesgo del proceso. Además, supera al azar con el mismo número de filas.

## Ejemplo

Con las cinco preferencias de SE-176, 6 filas bastan para cubrir todos los pares: en alguna fila aparece «esquema oscuro + zoom 200 %», en otra «contraste alto + colores forzados», etc. Si hay un defecto que solo aparece cuando están activas las tres a la vez (esquema oscuro, zoom y colores forzados), puede escapar; para esas combinaciones de riesgo se añaden casos a mano.

## Errores y confusiones comunes

- **Tabla de ejemplos de 243 filas que nadie lee**: producto completo de factores; corrección: reducir con cobertura de pares y añadir a mano las combinaciones de riesgo (SE-158).
- **La suite reducida pasa y una interacción real falla**: la interacción involucra tres factores o más.
- **Combinar valores inválidos** sin declarar restricciones.
- **Creer que pares garantiza todo.**

## Límites y cuándo no aplica

No cubre interacciones de tres o más factores, y los defectos de 3 factores del experimento (12 de 60) muestran que existen. 32 combinaciones se pueden probar enteras; 2¹⁰ no: la decisión depende del número de factores y del riesgo. Los defectos de la simulación son inyectados por el autor, de modo que las proporciones ilustran el mecanismo.
