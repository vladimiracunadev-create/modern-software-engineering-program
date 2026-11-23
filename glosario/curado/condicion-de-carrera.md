# Condición de carrera

## Definición

Una **condición de carrera** es una situación en que el resultado depende del orden en que se intercalan operaciones concurrentes cuyo orden no está controlado. Las clases lo formulan igual en contextos distintos: `SE-305` y `SE-430` en programas con varios hilos, `SE-418` en un carrito y un inventario con operaciones simultáneas y `SE-455` en un sistema crítico, donde el orden relativo de eventos que no se controla lleva a un estado inconsistente. El sentido que usa el programa es la dependencia del **orden relativo**, no la mera existencia de concurrencia.

## Por qué importa

Es un defecto que solo aparece a veces: el mismo código puede pasar cien pruebas y fallar en producción. `SE-430` extrae la consecuencia práctica: «lo corrí cien veces y pasó» no demuestra nada. En sistemas críticos el costo es mayor: `SE-455` analiza un caso en que una edición durante una ventana del proceso dejó parámetros inconsistentes en un equipo médico.

## Cómo funciona

Una carrera ocurre cuando dos o más actores leen y escriben un estado compartido sin una regla que ordene sus pasos. El ejemplo de `SE-430`: dos hilos incrementan un contador en dos pasos (leer, escribir). Hay seis intercalaciones posibles de los pasos, y solo dos terminan bien (33,3 %); con tres hilos, 6 de 90 (6,7 %). La causa de que sea tan difícil detectarla ejecutando es que el sistema real **no recorre todas las intercalaciones**: el intérprete cede el control en puntos concretos, y un código más corto o una versión distinta cambia la proporción de fallos de 0 % a 100 %.

De ahí dos consecuencias metodológicas. Primero, lo que demuestra la presencia o ausencia de la carrera es **enumerar** las intercalaciones o usar una herramienta que las fuerce, no repetir ejecuciones. Segundo, la defensa no es «tener más suerte» sino imponer orden o atomicidad: exclusión mutua, operaciones atómicas, restricciones únicas o transacciones, según dónde viva el estado.

## Ejemplo

`SE-455` modela una carrera real documentada: la edición del operador ocurre dentro de una ventana de 8 segundos del ajuste de imanes, después de que la rutina de espera comprobó por última vez si había cambios, y los parámetros quedan inconsistentes. En el modelo del laboratorio, con 100 000 tratamientos, una probabilidad de edición del 15 % (supuesto) y el instante de edición uniforme en los primeros 20 segundos, hay 5 705 inconsistencias en la variante original; con una ventana de 2 segundos son 1 129 y con 12 segundos, 8 611. El riesgo crece casi en proporción a la ventana durante la cual una edición no se vuelve a comprobar. Es un modelo con supuestos declarados, no una reconstrucción del suceso.

## Errores y confusiones comunes

- **Creer que pasar muchas pruebas descarta la carrera.** Las ejecuciones reales visitan pocas intercalaciones (`SE-430`).
- **Comprobar y luego actuar en el código de la aplicación.** Comprobar «¿existe?» y después insertar deja una ventana; la restricción única de la base de datos la cierra (`SE-246` lo desarrolla para idempotencia).

## Límites y cuándo no aplica

Las cifras de `SE-430` y `SE-455` salen de modelos y de supuestos declarados, de modo que fijan el método de razonamiento, no la frecuencia real de las carreras en un sistema concreto. Eliminar una carrera concreta no elimina la clase: `SE-455` insiste en que lo decisivo es cambiar el diseño para que no exista la ventana, no estrecharla.
