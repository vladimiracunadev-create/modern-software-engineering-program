# Holgura

## Definición

La **holgura** tiene en el programa dos sentidos relacionados. En planificación (SE-186, SE-370) es el tiempo que un elemento o tarea puede retrasarse sin retrasar la entrega. En capacidad y resiliencia (SE-515) es la capacidad no usada que permite absorber un aumento de carga. Ambos comparten la idea de margen disponible antes de que algo se degrade.

## Por qué importa

La holgura dice dónde un retraso o un exceso de carga se absorbe y dónde no. En un plan, indica qué elementos pueden esperar sin consecuencias. En una infraestructura, indica si perder una región o recibir un pico traslada el problema a las demás.

## Cómo funciona

**En planificación.** Dada una red de dependencias con duraciones, el camino crítico es la cadena más larga; los elementos fuera de él tienen holgura. SE-186 da un ejemplo mínimo: el camino crítico es B → C → D (3 + 2 + 1 = 6 días) y A tiene 1 día de holgura; si A se alarga a 4 días, A pasa a ser parte del camino crítico y la duración sube. La holgura de un elemento es la diferencia entre el camino crítico y el camino más largo que lo atraviesa. En un flujo de datos (SE-370), las tareas que no están en el camino crítico pueden tardar más sin retrasar la entrega.

**En capacidad.** SE-515 la usa para el análisis de pérdida de regiones: cuando una región falla, su carga se traslada a las demás. Un experimento **difuso** reparte la falla sobre toda la capacidad (por ejemplo, 5 % de las peticiones recibe una lentitud extra) y el aumento de consumo lo absorbe la holgura normal; sirve para comprobar la lógica de una alternativa, no el comportamiento a escala. La evacuación completa de una región exige que las demás tengan holgura suficiente: con R regiones a utilización u, perder una eleva la utilización de las restantes a u·R/(R−1). Si el resultado supera la capacidad, la evacuación colapsa a las demás.

La causa del colapso es calcular la holgura con la capacidad **nominal** y no la real; la corrección es calcular `u·R/(R−1)` y probarlo con tráfico antes. SE-515 pide además escribir las precondiciones de un experimento concentrado y comprobar cuáles no se cumplirían hoy.

## Ejemplo

Tres regiones a una utilización del 60 %. Al perder una, las dos restantes asumen su carga: 0,6 × 3 / 2 = 0,9, es decir 90 % de utilización; queda poca holgura para picos. Con cuatro regiones al 60 %, el resultado es 0,6 × 4 / 3 = 80 %. (Cálculo con la fórmula de SE-515; los valores son de ejemplo.)

## Errores y confusiones comunes

- **La evacuación de una región colapsa a las demás**: holgura calculada con capacidad nominal; corrección: `u·R/(R−1)` y prueba con tráfico.
- **Confundir holgura con desperdicio**: es un margen que protege.
- **Asumir que un elemento con holgura puede alargarse sin límite.**
- **No recalcular tras cambios en la red.**

## Límites y cuándo no aplica

La holgura de planificación supone duraciones fijas; con duraciones inciertas, elementos con holgura pueden volverse críticos. La de capacidad depende de que la carga se redistribuya de forma pareja, lo que no siempre ocurre. Operar sin holgura abarata, pero reduce la tolerancia a fallos.
