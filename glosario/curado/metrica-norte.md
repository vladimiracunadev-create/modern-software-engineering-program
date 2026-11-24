# Métrica norte

## Definición

La **métrica norte** (*north star metric*) es la medida única de resultado que resume el valor entregado y orienta las decisiones del equipo (SE-139). Es la cifra que mejor representa que el producto está haciendo lo que debe, y que el equipo puede mover.

## Por qué importa

Orienta decisiones de todo el equipo; si no representa valor, orienta mal a todos. Una métrica norte bien elegida alinea esfuerzos; una mal elegida los dirige hacia algo que no importa. Cambia cómo se priorizan funciones y experimentos: se evalúan por cuánto mueven la métrica norte.

## Cómo funciona

SE-139 pide tres propiedades. Debe ser un **resultado y no una actividad** (SE-135): cambio en lo que consiguen las personas, no movimiento dentro del producto. Debe ser **calculable**, con definición explícita (numerador, denominador, ventana y filtros). Y debe ser **sensible al cambio**: moverse cuando el equipo mejora algo, en un plazo útil para decidir.

En la plataforma de entregas, «entregas aceptadas a tiempo por estudiante activo de la semana» es un candidato: es resultado (la entrega fue aceptada y a tiempo), está definida con denominador explícito y responde a mejoras del flujo. «Sesiones» no lo es: es actividad, puede subir sin valor.

La clase insiste en la frase central: **una métrica norte orienta, no gobierna**; nunca debe usarse sin lo que la rodea. Eso son las **métricas contrarias** y las guardas: umbrales que no deben cruzarse mientras se optimiza. Sin ellas, el equipo puede mejorar la norte dañando otra cosa (la métrica norte sube y el producto empeora). El archivo de métricas conserva la definición, las guardas (métrica, umbral, ventana, responsable, acción) y los pares meta–contraria; la regla es que ninguna prueba arranca sin guardas y que cruzar una guarda detiene el despliegue hasta que el responsable decide.

Otro fallo que la clase señala: la métrica norte cambia de tendencia sin razón porque cambió su definición. Se corrige registrando los cambios de definición con fecha y recalculando la serie histórica.

## Ejemplo

Definición: numerador, entregas aceptadas antes del plazo en la semana; denominador, estudiantes con al menos una entrega aceptada o intento en la semana; ventana, semanal. Guardas: tasa de reclamos de nota por entrega no debe subir más de 10 %; tiempo de respuesta de la subida p95 no debe superar 3 s. Si un experimento sube la norte un 5 % pero los reclamos suben un 15 %, se detiene. (Definición ilustrativa en el estilo de SE-139.)

## Errores y confusiones comunes

- **La métrica norte sube y el producto empeora**: no hay guardas.
- **Cambiar la definición sin registrarlo.**
- **Elegir una actividad** (sesiones, clics) como norte.
- **Tener varias «norte»**: una sola es el punto.

## Límites y cuándo no aplica

Un producto con propósitos muy distintos (varios trabajos) difícilmente se resume en una sola cifra; ahí hacen falta varias métricas de resultado por segmento. Una norte mala es peor que ninguna, porque da orientación falsa. Y no sustituye el juicio cualitativo ni la investigación con personas.
