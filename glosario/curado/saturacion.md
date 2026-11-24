# Saturación

## Definición

La **saturación** es el estado en que la utilización se acerca a 1 y la cola crece sin que aumente el trabajo útil (`SE-436`).

## Por qué importa

Explica por qué la latencia se dispara con una utilización que parece «razonable»: los sistemas con colas no degradan de forma lineal. Planificar con la media y no con el objetivo de percentil lleva a operar demasiado cerca del borde.

## Cómo funciona

Cuando la tasa de llegada se acerca a la capacidad, cualquier ráfaga forma cola, y la cola se vacía lentamente porque casi no hay capacidad sobrante. El tiempo de espera crece de forma no lineal al acercarse la utilización a 1. La fórmula de Pollaczek–Khinchine relaciona la espera con la variabilidad del servicio: un servicio más variable que el exponencial espera más de lo que predice la fórmula simple.

## Ejemplo

Un servicio con utilización del 70 % responde con holgura; a 95 % la cola ya es larga con ráfagas ordinarias. (Ilustración cualitativa; los experimentos de `SE-436` son sobre la API de entregas.)

## Errores y confusiones comunes

- **La latencia se dispara con una utilización «razonable».** Se planificó con la media; calcular la utilización máxima desde el objetivo de percentil.
- **La espera es mayor de lo que predice la fórmula.** El servicio es más variable que el exponencial; medir cv² y usar Pollaczek–Khinchine.

## Límites y cuándo no aplica

Los modelos de cola suponen llegadas y servicios con ciertas distribuciones; en la práctica se miden. Más allá de la saturación, reintentos y colas pueden sostener el problema (fallo metaestable).
