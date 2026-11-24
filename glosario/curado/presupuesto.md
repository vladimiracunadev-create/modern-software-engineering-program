# Presupuesto

## Definición

«Presupuesto» es una palabra con varios sentidos técnicos en el programa, unidos por la idea de un **límite que se mide y tiene una acción al excederse**. El sentido principal de esta entrada es el de los agentes con modelos de lenguaje: el límite de costo (fichas, tiempo, dinero) del bucle, que `SE-598` amplía a un conjunto de topes de costo, tiempo y capacidades con una acción al excederlos. Los otros sentidos tienen entrada propia: el de rendimiento web (`SE-235`, ver *presupuesto de rendimiento*), el de recursos de un dispositivo (`SE-261`) y el de costos de plataformas de datos (`SE-370`).

## Por qué importa

Un agente que decide por sí mismo cuántos pasos dar puede no parar. `SE-581` (loops de agentes y criterios de parada) lo plantea así: el presupuesto acota el costo *real*, no el número de vueltas. Dos vueltas pueden costar cien veces más una que otra. En `SE-370`, los presupuestos hacen visible el desvío de costos de datos a tiempo; en `SE-235`, un número comprobable en cada cambio evita que el rendimiento se degrade sin que nadie lo decida.

## Cómo funciona

Un presupuesto de agente fija topes sobre magnitudes concretas:

- **Costo:** fichas (*tokens*) o dinero por tarea.
- **Tiempo:** duración total o por paso.
- **Capacidades:** cuántas herramientas o llamadas externas puede usar.

Y una **acción al excederlos**: parar, pedir confirmación humana o degradar a un modo más barato. El tope se calibra con datos: en `SE-575`, por ejemplo, el máximo de pasos se calibra con la cola de la distribución de las tareas buenas, no con la media.

Un presupuesto se combina con otros criterios de parada (repeticiones del mismo estado, pasos sin avance), porque un tope de costo solo detiene tarde.

## Ejemplo

Ilustración propia con el patrón de `SE-598`: un agente de envíos tiene presupuesto de 80 pasos, 200 000 fichas y 5 minutos por tarea. Al exceder cualquiera de los tres, para y deja un punto de control con el estado, en vez de seguir gastando. En `SE-235`, el equivalente web es un tope de 170 KB de JavaScript que hace fallar la integración.

## Errores y confusiones comunes

- **Limitar el número de vueltas** y no el costo.
- **Un presupuesto sin acción definida al excederse.**
- **Calibrarlo con la media** y cortar tareas legítimas largas.
- **Mezclar los sentidos:** el presupuesto de agente no es el de error de un SLO (`presupuesto de error`).

## Límites y cuándo no aplica

Un tope no sustituye vigilar *qué* hace el agente: puede causar daño con poco costo. Las cifras del ejemplo son ilustrativas. Un presupuesto demasiado ajustado interrumpe tareas válidas y uno demasiado holgado no protege.
