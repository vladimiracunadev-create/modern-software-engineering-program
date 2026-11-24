# Latencia de cola

## Definición

La **latencia de cola** (*tail latency*) es la latencia de las peticiones más lentas, resumida con un percentil alto como el p99. `SE-436` (latencia, throughput, saturación y capacidad) la define así; `SE-281` la usa para los aceleradores: la latencia que no supera el p95 o el p99 de las peticiones. «Cola» alude a la cola derecha de la distribución de tiempos, no a una cola de espera.

## Por qué importa

El promedio oculta a quienes más sufren. Si el p99 es diez veces la mediana, una de cada cien peticiones es mucho más lenta, y en sistemas con muchas peticiones por persona esa fracción se alcanza pronto. Es lo que se compromete en un SLO de latencia, no el promedio.

## Cómo funciona

Una distribución de latencias suele tener una masa grande de peticiones rápidas y una cola larga de lentas (por esperas en cola, recolección de basura, reintentos, fallos de caché). Se resume con percentiles: p50 (mediana), p95, p99.

`SE-340` (microservicios y sus costos reales) añade la **amplificación**: si una petición del usuario espera a varias llamadas internas, basta que una caiga en la cola para que toda la petición sea lenta. Con *n* llamadas independientes, la probabilidad de que al menos una supere su p99 es 1 − 0,99ⁿ; con 100 llamadas, ronda el 63 %. Por eso la latencia de cola de la petición completa empeora con cada servicio añadido, junto con la disponibilidad multiplicada.

## Ejemplo

*Avisos*, en `SE-340`, evalúa separar el cálculo de avisos. La clase da el precio: más de mil veces una llamada en proceso, disponibilidad multiplicada, latencia de cola amplificada y un riesgo de acoplamiento por contrato. Ilustración numérica propia: una página que llama a 20 servicios con p99 de 200 ms cada uno tiene aproximadamente 18 % de probabilidad de que al menos una llamada pase de 200 ms.

## Errores y confusiones comunes

- **Reportar solo el promedio o la mediana.**
- **Promediar percentiles de varios servicios:** no se pueden combinar así.
- **Creer que los percentiles se suman:** el p99 de un flujo no es la suma de los p99 de sus pasos.
- **Confundirla con el tiempo en cola de espera:** la espera puede causarla, pero no es lo mismo.

## Límites y cuándo no aplica

El p99 solo describe bien con muchas observaciones; con pocas, es ruidoso. La cuenta de amplificación supone llamadas independientes y en paralelo; con dependencias correlacionadas (una causa común) el cálculo cambia. Para sistemas por lotes, donde importa el tiempo total y no cada petición, el percentil por petición es menos relevante.
