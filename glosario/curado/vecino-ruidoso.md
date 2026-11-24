# Vecino ruidoso

## Definición

Un **vecino ruidoso** (*noisy neighbor*) es un inquilino cuya carga degrada el servicio de otros que comparten los mismos recursos (`SE-342`, `SE-410`). `SE-398` lo generaliza a cualquier carga que, al consumir recursos compartidos, degrada el servicio que reciben las demás, por ejemplo en contenedores sobre un mismo nodo.

## Por qué importa

En un sistema compartido, el rendimiento de un cliente depende de lo que hagan los demás. Un solo cliente intensivo puede volver lento a todos, sin que haya fallo alguno. La decisión que cambia es cuánto aislamiento se da a cada inquilino, sabiendo que más aislamiento cuesta más.

## Cómo funciona

`SE-342` presenta el espectro de aislamiento en una plataforma de varios inquilinos:

1. **Todo compartido**: una sola base, un solo esquema y una columna que identifica al inquilino.
2. **Un esquema por inquilino** dentro de la misma base.
3. **Una base por inquilino**.
4. **Un despliegue completo** (cómputo y datos) por inquilino.

Cada paso hacia el aislamiento reduce el riesgo de **fuga de datos** y el de **vecino ruidoso**, y sube el costo por inquilino y el trabajo de operaciones. Un diseño real suele mezclar: los inquilinos pequeños comparten y los grandes o regulados tienen recursos dedicados. La decisión no es para siempre: debe poder moverse un inquilino de un nivel a otro, y eso es un requisito de diseño desde el inicio.

En `SE-398`, la causa técnica es la competencia por recursos compartidos (CPU, memoria, disco, red) en un mismo nodo. Los mecanismos del núcleo para repartir y limitar el consumo (grupos de control, o cgroups) son la herramienta que acota cuánto puede tomar cada carga. `SE-410` lo conecta con el producto SaaS: el cliente más grande suele ser el que más degrada a los demás y el que justifica recursos dedicados. En resiliencia, el patrón de mamparos (bulkhead) y las celdas aplican la misma idea de separar para que una carga no consuma lo de las otras.

## Ejemplo

Tras un incidente por un informe pesado, el equipo del caso de `SE-342` comprueba el aislamiento con una prueba de fuga entre inquilinos, y para el cliente con exigencia de residencia decide una base separada en su región. Para el cliente más grande, que degrada a los demás por volumen, se asignan recursos dedicados. Los pequeños siguen compartiendo.

## Errores y confusiones comunes

- **Creer que el aislamiento de datos resuelve el rendimiento**: una base con esquemas separados puede seguir compartiendo CPU y disco.
- **Aislar a todos por igual**: eleva el costo sin necesidad.
- **No poder mover a un inquilino de nivel**: la decisión se vuelve irreversible.
- **Medir solo promedios**: el vecino ruidoso se ve en la cola de latencia de los otros.

## Límites y cuándo no aplica

No aparece con un solo inquilino o con recursos holgados respecto a la carga. Aislar completamente cada inquilino elimina el problema pero pierde las economías de escala que justificaban compartir. `SE-342` presenta el espectro como decisiones de arquitectura con costos, no como una receta con umbrales universales.
