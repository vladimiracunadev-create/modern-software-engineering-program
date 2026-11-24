# Pronóstico por simulación

## Definición

El **pronóstico por simulación** es la distribución del resultado obtenida repitiendo muchas veces un modelo del proceso con datos extraídos de la historia (SE-191). SE-533 lo formula como la estimación de la distribución de plazos remuestreando un historial de entrega. Es el enfoque de «Monte Carlo» aplicado a la pregunta «¿cuándo termina?».

## Por qué importa

Convierte la historia en una distribución de fechas sin suponer una fórmula. En lugar de una fecha única, se obtiene «el 85 % de las veces termina en 12 semanas o menos», que es una promesa con confianza. Cambia cómo se comunica un plazo: como rango con probabilidad, no como número exacto.

## Cómo funciona

SE-191 describe el procedimiento. Se toma la **historia de rendimiento semanal** (por ejemplo, ocho semanas con media 5,8 elementos terminados), se parte de un **desglose del trabajo pendiente** (62 elementos) y se **simula el futuro**: se eligen al azar semanas de esa historia, con reposición, hasta completar el trabajo pendiente, y se anota cuántas semanas tomó. Se repite miles de veces. El resultado es una **distribución de semanas hasta terminar**, de la que se leen **percentiles**.

Es la aplicación directa del **remuestreo** de Efron: no supone una forma para el rendimiento (normal, por ejemplo), solo que el futuro se parece a la historia observada. Su utilidad es que respeta la variabilidad real: semanas buenas y malas, sin necesidad de ajustar una distribución.

Dos fuentes de error, con su corrección. El percentil 85 que se cumple solo dos de cada tres veces ocurre porque el alcance se modeló fijo y la historia es corta; se corrige **incluyendo el crecimiento esperado del alcance** (en el ejemplo, entre 0 y 15 %, estimado con las últimas dos entregas) y **ensanchando el intervalo**. Y el margen de cada tarea que se consume mientras el plazo igual se pierde por expansión del trabajo; se corrige con un colchón compartido y vigilando su consumo. La calibración de la simulación se comprueba por retrospectiva: si el percentil 85 se cumple el 85 % de las veces. Con menos de unas doce semanas de historia conviene ensanchar el intervalo.

## Ejemplo

Historia: 4, 6, 5, 7, 6, 5, 8, 5 elementos por semana. Pendiente: 62 elementos. En cada simulación se sortean semanas de esa lista hasta sumar 62; tras 10.000 simulaciones, el percentil 50 de semanas es 11 y el percentil 85 es 13. Con crecimiento de alcance de 0 a 15 %, el percentil 85 sube a unas 15. Se comunica «entre 11 y 15 semanas, con 85 % de confianza». (Simulación ilustrativa con el método de SE-191; las cifras son de ejemplo.)

## Errores y confusiones comunes

- **El percentil 85 se cumple dos de cada tres veces**: alcance fijo y poca historia.
- **El margen de cada tarea se consume y el plazo se pierde**: expansión del trabajo.
- **Usar la media** como pronóstico único.
- **Remuestrear una historia no representativa** (con cambios de equipo).

## Límites y cuándo no aplica

Supone que el futuro se parece al pasado; si el equipo, el producto o el proceso cambian, la historia deja de valer. Con muy poca historia, la distribución es poco fiable. No sustituye la gestión del alcance ni las dependencias externas, que el modelo simple no incluye.
