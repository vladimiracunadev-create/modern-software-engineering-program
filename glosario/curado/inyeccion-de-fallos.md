# Inyección de fallos

## Definición

La **inyección de fallos** es la introducción deliberada de un fallo en un sistema, o en su modelo, para observar si es detectado y cómo responde el sistema. `SE-275` la aplica a fallos físicos y digitales en simulación; `SE-443` la usa con latencia, error, caída o carga; `SE-227` la usa para provocar una condición de error en una automatización frágil. El núcleo es el mismo: provocar a propósito lo que «puede pasar» para verlo pasar.

## Por qué importa

Mide si una defensa funciona en lugar de suponerlo. `SE-227` lo dice con precisión: convierte «puede pasar» en «pasa y lo vemos». Y `SE-275` da el valor práctico: cambia «creemos que lo detecta» por «lo detecta en N de 100 casos», y el resultado informa qué defensa añadir.

## Cómo funciona

`SE-275` ejemplifica fallos físicos y digitales: congelar la lectura de un sensor, añadir una deriva, invertir un bit, cortar la energía a mitad de una escritura. Hsueh y colaboradores, citados por la clase, clasifican las técnicas según el nivel en que se inyecta: hardware, software o simulación. La clase elige simulación porque es reproducible y barato.

`SE-443` añade que **cada tipo de fallo ataca una defensa distinta**: la latencia añadida prueba los *timeouts* y los reintentos; los errores prueban el manejo de fallos y el circuit breaker; la caída de una dependencia prueba la degradación; la carga prueba los límites y la contención. El procedimiento general es:

1. Definir una hipótesis de comportamiento esperado.
2. Inyectar un fallo concreto, de alcance acotado.
3. Observar la respuesta con las métricas definidas.
4. Comparar con la hipótesis y corregir la defensa o el supuesto.

## Ejemplo

En `SE-275`, el nodo ambiental recibe un sensor de CO₂ congelado y se mide cuántas veces de 100 lo detecta el comparador de dos sensores. Ilustración propia: en una automatización que descarga archivos, se simula que la segunda descarga devuelve un error 500 para comprobar que la ejecución se detiene y deja un estado recuperable, no a medias.

## Errores y confusiones comunes

- **Inyectar sin hipótesis ni medición,** que no enseña nada.
- **Confundirla con una prueba de carga:** la carga es un tipo de fallo entre varios.
- **Inyectar en producción sin acotar el alcance** ni poder detenerla.
- **Considerar probada una defensa por un solo caso.**

## Límites y cuándo no aplica

Solo prueba los fallos que alguien imaginó inyectar. La simulación de `SE-275` no sustituye a la inyección en hardware real, que descubre fallos que el modelo no recoge. En sistemas sin un comportamiento esperado definido, no hay con qué comparar.
