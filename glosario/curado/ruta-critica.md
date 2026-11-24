# Ruta crítica

## Definición

La **ruta crítica** es el camino más largo de pasos dependientes que determina el tiempo total. El programa la usa en cuatro contextos con el mismo núcleo: en `SE-496` (trazas distribuidas), el camino de *spans* que determina la latencia total de una petición; en `SE-235` (rendimiento web), la cadena más larga de recursos dependientes que decide el tiempo hasta la primera pintura; en `SE-370`, el camino de dependencias más largo en datos, que fija el tiempo de entrega; y en `SE-566`, la cadena de dependencias de mayor duración, que fija el mínimo de tiempo con cualquier número de trabajadores.

## Por qué importa

Solo importa lo que está en la cadena más larga; lo demás no cambia el total. Optimizar fuera de la ruta crítica no mejora la petición ni la entrega. Es la razón por la que medir antes de optimizar es una regla de trabajo, no un consejo.

## Cómo funciona

`SE-496`: en una traza con ramas paralelas, la latencia de la petición no es la suma de los spans sino el camino más largo desde la entrada hasta la salida. La identificación es mecánica:

- En un nodo con hijos **paralelos**, el hijo de mayor duración pertenece a la ruta.
- En un nodo con hijos **secuenciales**, todos pertenecen.

Consecuencias:

- Acelerar un span fuera de la ruta no cambia nada, porque la rama que domina tarda lo mismo. El ahorro es cero hasta que alcanza a la rama competidora.
- Acelerar uno dentro de la ruta ayuda, pero con un tope: cuando otra rama pasa a dominar, la ganancia termina.

En `SE-566`, la ruta crítica del plan de tareas fija el mínimo de tiempo con cualquier número de trabajadores: añadir personas no acorta lo que depende de una cadena secuencial.

## Ejemplo

Ilustración numérica propia: una petición llama en paralelo a A (120 ms) y B (80 ms), y luego a C (50 ms). La latencia es 120 + 50 = 170 ms; la ruta crítica es A → C. Reducir B de 80 a 40 ms no cambia nada. Reducir A a 90 ms baja el total a 140 ms; pero si A baja de 80 ms, B pasa a dominar y la mejora se detiene.

## Errores y confusiones comunes

- **Sumar los spans en paralelo** como si fueran secuenciales.
- **Optimizar el span más lento sin comprobar que esté en la ruta.**
- **Pensar que más trabajadores acortan siempre** un plan (`SE-566`).
- **Confundirla con el camino más frecuente:** la ruta crítica es la más larga, no la más usada.

## Límites y cuándo no aplica

La ruta crítica cambia entre ejecuciones (una rama que hoy es corta puede ser larga mañana); conviene mirar muchas trazas. Con ramas de duración similar, varias son casi críticas. Y ignora recursos compartidos que alargan ramas paralelas por competencia.
