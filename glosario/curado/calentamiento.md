# Calentamiento

## Definición

El **calentamiento** (*warm-up*) es el periodo en que una instancia nueva llena sus cachés y abre sus conexiones antes de rendir con normalidad. Es el sentido de `SE-250` (health, readiness y apagado ordenado). `SE-437` lo usa en mediciones: el conjunto de ejecuciones iniciales cuyo tiempo difiere del régimen estable por cachés frías o carga de módulos. En ambos, lo común es que las primeras operaciones son más lentas que las siguientes.

## Por qué importa

Una instancia recién arrancada con caché fría atiende peor que una caliente, y el criterio de disponibilidad lo reconoce o lo ignora. Si lo ignora, el balanceador manda tráfico completo a una instancia que no está lista y aparecen errores o lentitud. En mediciones (`SE-437`), si no se descarta el calentamiento el benchmark mide el arranque y no el comportamiento estable.

## Cómo funciona

Una instancia nueva tiene la caché vacía, conexiones sin abrir y código sin compilar. `SE-250` ofrece tres estrategias para decidir cuándo recibe tráfico completo:

1. **Recibir tráfico desde el arranque:** simple, con solicitudes lentas al principio.
2. **Esperar un tiempo fijo:** predecible, pero ignora la velocidad real de calentamiento.
3. **Declararse lista al alcanzar un umbral de aciertos de caché:** adaptable, pero exige instrumentar.

El calentamiento **traslada el costo**: mientras una instancia se calienta, las otras absorben más tráfico. Por eso conecta con la disponibilidad (readiness): una instancia puede estar viva y aun así no estar lista.

En `SE-437`, el mismo fenómeno obliga a diseñar la medición: ejecuciones de descarte iniciales y análisis solo del régimen estable.

## Ejemplo

El caso conductor de `SE-250` deja la plataforma de entregas con tres sondeos de propósito distinto, calentamiento declarado y apagado ordenado. Cambiar una sola decisión, el plazo de gracia de 30 a 10 segundos, obliga a revisar qué artefactos se tocan. Ilustración propia: si una instancia necesita 80 % de aciertos de caché para rendir, se marca lista al superarlo y no a los 30 segundos fijos.

## Errores y confusiones comunes

- **Instancia recién arrancada que responde con errores:** recibe tráfico sin estar lista; corrección, sondeo de disponibilidad y de arranque (`SE-250`).
- **Reinicio de todas las instancias cuando cae la base de datos:** el sondeo de vida consulta una dependencia externa; la vida debe ser local.
- **Confundirlo con arranque en frío:** aquel es crear el entorno; el calentamiento es lo que sigue.

## Límites y cuándo no aplica

La curva lineal de calentamiento de la clase es un supuesto: las cachés reales se calientan según la popularidad de las claves (`SE-250`). Con una aplicación sin caché relevante, la espera no aporta. Y el término de medición (`SE-437`) no es de operación: no se resuelve con sondeos.
