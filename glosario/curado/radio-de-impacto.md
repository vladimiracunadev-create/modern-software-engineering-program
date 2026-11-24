# Radio de impacto

## Definición

El **radio de impacto** es, en el sentido principal del programa (`SE-344`), la fracción de clientes afectada por un fallo. Otras clases lo usan con matices cercanos:

- En `SE-443` (resiliencia): la fracción del sistema o del tráfico que un experimento afecta.
- En `SE-410` (SaaS): el conjunto de clientes afectados por un fallo.
- En `SE-520` (modernización): el número de paquetes que deben cambiar como consecuencia de actualizar uno.

Se parece al radio de explosión; la diferencia que usa el programa es que el radio de impacto se expresa como fracción de clientes y se compara entre arquitecturas.

## Por qué importa

La disponibilidad habitual es un promedio sobre el tiempo y no dice cuántos clientes ven el problema cuando algo falla. Dos sistemas con la misma disponibilidad pueden diferir mucho: uno cae para todos un minuto, otro para el 1 % durante horas. La decisión que cambia es qué se optimiza: acotar cuántos se ven afectados por un único fallo, además de cuánto dura.

## Cómo funciona

`SE-344` define el radio como la fracción de clientes que quedan sin servicio por un único fallo. En una flota compartida, cualquier fallo que se propague por la flota alcanza al **100 %**. El objetivo de las **celdas** es poner un techo: con ocho celdas y reparto uniforme, un fallo contenido en una celda afecta a una octava parte, el 12,5 %. Ese techo es un escenario de calidad medible, que se puede comprobar inyectando el fallo («un fallo de cualquier inquilino afecta como máximo al 15 % de los inquilinos», en términos de `SE-337`).

La clase compara opciones tras un incidente: ocho celdas dan 12,5 %; fragmentación aleatoria sobre la flota existente da un 3,6 % caído del todo ante una petición venenosa. Pero el costo cuenta: el equipo descarta empezar con celdas completas porque el costo de capacidad del 20 % y la operación de ocho copias superan lo que puede asumir ese año, y elige un camino por etapas (tope de reintentos por inquilino y cortacircuitos, luego fragmentación aleatoria, y celdas solo para el cliente más grande).

En `SE-520`, el mismo concepto se aplica a dependencias: antes de actualizar un paquete se calcula el radio de impacto en el grafo, es decir, cuántos otros paquetes deben cambiar.

## Ejemplo

El equipo calcula el radio de impacto de los fallos más probables: una petición venenosa, un despliegue defectuoso, una base saturada, y expresa cada uno como una fracción de clientes. Eso les permite comparar la arquitectura actual con alternativas por una cifra común. Ejercicio de `SE-344`.

## Errores y confusiones comunes

- **Se actualiza una dependencia y se rompe otra**: no se miró el grafo; se calcula el radio de impacto antes de decidir (`SE-520`).
- **Confundirlo con disponibilidad**: no son la misma medida.
- **Calcularlo sin la distribución real de clientes**: un cliente dominante cambia las fracciones.
- **Suponer que el reparto uniforme se cumple**.

## Límites y cuándo no aplica

Las cifras de la clase (8 celdas, 12,5 %, 3,6 %, costo del 20 %) son del escenario construido; en otros sistemas cambian. Acotar el radio tiene un costo (capacidad, operación) que puede no justificarse para cargas pequeñas. Y el radio mide la fracción de clientes afectados, no la gravedad del daño a cada uno.
