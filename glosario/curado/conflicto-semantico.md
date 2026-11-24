# Conflicto semántico

## Definición

Un **conflicto semántico** es una incompatibilidad entre dos cambios que se fusionan sin marcas de texto (SE-197). SE-584 lo dice como cambios compatibles para la fusión e incompatibles para el programa; SE-481 como la combinación de dos cambios que no choca en el texto y rompe una suposición compartida. Se opone al conflicto textual, que Git detecta y señala con marcas.

## Por qué importa

Un cambio puede combinarse sin avisos y romper el sistema. Git compara texto, no significado; si ambos cambios tocan zonas distintas, la fusión es limpia aunque el resultado sea incorrecto. Cambia dónde se pone la defensa: no basta que cada rama pase sus pruebas; hay que probar la combinación.

## Cómo funciona

SE-197 da el ejemplo clásico: uno cambia la firma de una función y otro añade una llamada con la firma vieja. Git no ve esto porque no entiende el programa. La clase lo reproduce con Git real: una rama invirtió el orden de los parámetros de `penalizar(nota, horas)` y actualizó `informe.py`; otra, partiendo de la versión anterior, añadió `panel.py` con la llamada de orden antiguo. La segunda fusión terminó con **código de salida 0** (sin conflicto de texto) y `panel.py` imprimió **42** en lugar de **60**.

La defensa es **probar el resultado de la combinación** antes de aceptar, no solo cada rama por separado: integración continua sobre el tronco y, con volumen alto, una **cola de fusión** que prueba cada cambio sobre el estado actual del tronco. Para estimar la frecuencia, la clase simula 500 PR con una proporción de solapamiento y una probabilidad de incompatibilidad, y presenta un mapa de calor: cuántas veces `main` queda roto crece con ambas proporciones. Ambas son supuestos del autor, pero el caso real prueba que el fenómeno existe.

La causa de fondo es que los cambios comparten **suposiciones implícitas** (una firma, un formato, un orden) que ningún archivo concreto declara. Cuanto más cambios simultáneos toquen lo mismo, más probable es el choque. Las ramas largas y las equipos grandes lo agravan.

## Ejemplo

Rama A: `penalizar(nota, horas)` pasa a `penalizar(horas, nota)` y se actualiza `informe.py`. Rama B, creada antes: añade `panel.py` que llama `penalizar(nota, horas)`. Ambas pasan sus pruebas por separado y la fusión no marca conflicto, pero el panel calcula con los argumentos invertidos. Solo las pruebas sobre la combinación (o una cola de fusión) lo detectan. (Caso de SE-197.)

## Errores y confusiones comunes

- **Main queda roto tras dos PR verdes**: no se probó la combinación; corrección: probar el resultado de la fusión o usar una cola.
- **Creer que «sin conflicto» significa «correcto».**
- **Confundirlo con un conflicto textual**: este sí lo detecta Git.
- **Ramas largas** que acumulan suposiciones divergentes.

## Límites y cuándo no aplica

Las pruebas solo detectan lo que cubren; un conflicto semántico en una zona sin pruebas pasa. En equipos pequeños con pocas ramas simultáneas ocurre menos. Las proporciones de la simulación son del autor y no describen equipos reales.
