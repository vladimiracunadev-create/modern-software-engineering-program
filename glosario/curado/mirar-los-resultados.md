# Mirar los resultados

## Definición

**Mirar los resultados** (en la literatura, *peeking*) es la decisión de cuándo analizar los datos de un experimento. Si se hace repetidamente y se detiene la prueba al primer resultado favorable, el error real supera al nominal (SE-127). El término alude al hábito, no a una técnica estadística.

## Por qué importa

Es una de las causas más comunes de «ganadores» que no se reproducen. Un equipo que revisa el tablero cada día y detiene la prueba cuando aparece «significativo» cree que tiene un 5 % de falsos positivos y en realidad tiene bastante más. Cambia el plan de experimento: cuándo se mira, cuántas veces y bajo qué regla se detiene.

## Cómo funciona

Un p-valor está calibrado para un **único análisis planificado**: su garantía (probabilidad de falso positivo del 5 %, por ejemplo) vale si se calcula una vez, con tamaño fijado de antemano. Si se calcula cada día y se detiene al primer «significativo», se da al azar muchas oportunidades de cruzar el umbral, y la probabilidad de que alguna de las miradas lo cruce sea mucho mayor que 5 %. Es el mismo problema de comparaciones múltiples, repartido en el tiempo.

SE-127 ofrece dos salidas: **fijar de antemano el tamaño y mirar una sola vez**, o usar **métodos secuenciales** diseñados para monitorear (con umbrales que se ajustan en cada mirada). Lo que no vale es mirar libremente y aplicar la prueba clásica. La disciplina se materializa en el plan del experimento: la hipótesis, la diferencia mínima relevante, el tamaño por rama y la potencia, el calendario de análisis (una mirada o un método secuencial declarado), la población, el criterio de asignación, el intervalo esperado y las decisiones asociadas a cada resultado posible. El plan se fecha antes de empezar y no se reescribe después de mirar los datos.

## Ejemplo

Un equipo prueba dos versiones de una pantalla de entrega y revisa el valor p cada mañana durante 20 días; el día 9 aparece 0,04 y detiene la prueba declarando ganadora a la variante B. Al repetirla, el efecto desaparece. Con 20 miradas sobre una diferencia que no existe, la probabilidad de ver al menos un valor p menor a 0,05 es mucho mayor que 5 %. La corrección: fijar el tamaño en el plan y analizar el día 20, o declarar un método secuencial. (Ilustración del mecanismo; las cifras son de ejemplo.)

## Errores y confusiones comunes

- **La prueba «ganadora» desaparece al repetirla**: se detuvo al primer resultado significativo tras mirar muchas veces.
- **El experimento dice «no hay diferencia» siempre**: la muestra no tenía potencia; corrección: calcular el tamaño por rama antes y cambiar de método si es inalcanzable.
- **Mirar «solo para vigilar»** y luego decidir con lo visto.
- **Reescribir el plan después de ver los datos.**

## Límites y cuándo no aplica

Vigilar métricas de seguridad o de daño durante el experimento es legítimo y recomendable (reglas de parada por daño); lo que se evita es decidir la victoria por mirada repetida con una prueba no secuencial. Los métodos secuenciales pagan con algo más de muestra o con umbrales más estrictos. Para decisiones baratas y reversibles, el rigor puede relajarse siempre que el equipo lo haga con conocimiento del riesgo.
