# Escalón de tráfico

## Definición

Un **escalón de tráfico** es un despliegue de un cambio a una fracción pequeña y limitada del tráfico (`SE-607`). El programa lo usa con matices: `SE-476` lo describe como el despliegue de una versión nueva a una fracción pequeña del tráfico para compararla con la anterior (el *canary*); `SE-346` como la fracción creciente del tráfico dirigida a un sistema nuevo durante una migración.

## Por qué importa

Desplegar a todo el tráfico de golpe convierte cualquier defecto en un incidente completo. Un escalón limita el radio del daño y, a la vez, genera evidencia: se compara la versión nueva con la vigente en condiciones reales. La decisión que cambia es que el avance se decide con datos del escalón, no con la confianza de quien lo desarrolló.

## Cómo funciona

La idea común es servir el cambio a una fracción y comparar una métrica con la de la versión vigente. En `SE-607` (ML en producción), un *canary* sirve el candidato a una fracción del tráfico y compara una métrica de error con la del modelo vigente. Con etiquetas que tardan siete días, solo se puede medir el error de las decisiones ya etiquetadas, y la potencia depende de cuántas decisiones del segmento afectado hay en la fracción.

El plan de la clase es por etapas. Etapa 1: **sombra** durante 24 horas (el candidato recibe tráfico pero no sirve decisiones), vigilando desacuerdo y tasa de marcados en cuatro segmentos definidos de antemano; regla: pausar si algún segmento se aparta más de 10 puntos. En el ejemplo, la primera noche pausa el plan: en el segmento móvil y nocturno el candidato marca al 4 % frente al 59 % del vigente; el equipo encuentra una anomalía de etiquetado, reentrena y repite. Etapa 2: canary del 5 % durante cinco días con guardas de latencia, errores y marcados por segmento. La sombra no sirve decisiones; el canary las sirve a una fracción.

## Ejemplo

El equipo de *Avisos-ML* pasa por sombra de 24 h y canary del 5 % durante cinco días, con la regla de pausar si un segmento se aparta más de 10 puntos. La sombra detecta una discrepancia en un segmento que el promedio global habría ocultado, y el despliegue se pausa antes de afectar a nadie. Caso de `SE-607`.

## Errores y confusiones comunes

- **Un canary demasiado pequeño**: `SE-607` advierte que un canary del 1 % por prudencia no tiene potencia para ver una regresión de un segmento minoritario en una semana; ofrece una sensación de seguridad.
- **Mirar solo la métrica global**: un segmento minoritario puede estar roto sin mover el promedio.
- **Confundir sombra con canary**: la sombra no sirve decisiones.
- **No definir antes el criterio de retroceso**.

## Límites y cuándo no aplica

El escalón solo detecta lo que su tamaño y duración le permiten ver: la potencia estadística depende de cuántas observaciones del caso relevante entran en la fracción. No aplica cuando el cambio no se puede servir de forma parcial (una migración de esquema irreversible) o cuando el tráfico es tan pequeño que la fracción no produce evidencia. Y no sustituye las pruebas previas al despliegue.
