# Indicador

## Definición

Un **indicador** es el resumen numérico de una medición con un estadístico, una ventana y un alcance declarados (`SE-433`). «p95 de latencia, ventana de 10 s, endpoint de entregas» es un indicador; «latencia» a secas no.

## Por qué importa

Un número sin estadístico, ventana y alcance no se puede interpretar ni comparar. Además, un indicador acaba siendo objetivo de decisiones: cuando se vuelve meta, se optimiza el número y no lo que representa (`SE-433`).

## Cómo funciona

Cada declaración elimina una ambigüedad: el **estadístico** (media, percentil, máximo), la **ventana** (sobre qué intervalo) y el **alcance** (qué eventos entran). `SE-495` añade un caso: un indicador leído a intervalos mayores que la duración de un pico nunca lo muestra; se registra un máximo por intervalo o un histograma. Los indicadores de servicio (SLI) son indicadores sobre eventos buenos y válidos, base de los objetivos (SLO).

## Ejemplo

Un panel muestra la latencia media por minuto; los usuarios se quejan de picos de 3 s. La media los diluye. Se sustituye por el p99 con un máximo por intervalo, y los picos aparecen.

## Errores y confusiones comunes

- **El objetivo se cumple y la experiencia no mejora.** El indicador se volvió meta; añadir uno complementario y revisar su validez (`SE-433`).
- **El indicador nunca muestra el pico.** Intervalo de lectura mayor que el pico (`SE-495`).

## Límites y cuándo no aplica

Ningún indicador agota lo que se quiere saber; es un resumen y descarta información. Se elige junto a la pregunta que debe responder.
