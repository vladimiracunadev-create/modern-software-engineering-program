# Despliegue progresivo

## Definición

El **despliegue progresivo** es la exposición gradual de un cambio a fracciones crecientes de personas, con detección entre etapas (SE-142). Se llama también despliegue por etapas o canario cuando la primera etapa es una fracción pequeña. Se aplica sobre todo a decisiones costosas de revertir.

## Por qué importa

Limitar la exposición reduce el daño de un defecto y acorta el tiempo hasta verlo. Un defecto que llega a todos de golpe afecta a todos antes de que nadie lo note; el mismo defecto en una etapa pequeña afecta a pocos y se detecta con tiempo de reaccionar. Cambia la forma de liberar: el riesgo se reparte en el tiempo en lugar de concentrarse en un momento.

## Cómo funciona

Se despliega a una fracción (por ejemplo, 1 %), se observa y se amplía a fracciones mayores si las señales son buenas. SE-142 señala que la detección depende de dos cosas: **cuántas personas se ven afectadas** y **qué fracción lo reporta**. Un defecto frecuente se ve en la primera etapa; uno raro solo cuando la exposición es mayor. Por eso las etapas y el umbral de detección son una decisión que **se escribe antes de desplegar**: cuántas etapas, qué fracción en cada una, cuánto tiempo se observa y qué señal detiene el avance.

El mecanismo depende de que haya una **señal** (error, latencia, una métrica de resultado) con un umbral y de que se pueda **revertir** (volver a la versión anterior) o detener el avance. Esto conecta con la reversibilidad de las decisiones: el registro de la plataforma tiene por decisión su costo de equivocarse, su costo de reversión, su clasificación (de dos sentidos, costosa de revertir, de un sentido), la evidencia exigida y el mecanismo de salida. Ninguna migración se despliega sin comparación antes/después en un entorno de prueba, y las irreversibles requieren copia verificada y revisión de otra persona.

Una precisión importante: la reversión no siempre restituye el estado. El síntoma «tras revertir faltan datos» tiene causa conocida (la inversa recrea estructura, no contenido) y se corrige comparando antes y después y guardando copia verificada.

## Ejemplo

Un cambio en el cálculo de notas se despliega al 1 % de cursos durante un día, luego al 10 %, al 50 % y al 100 %. Entre etapas se vigila la tasa de reclamos y el tiempo de cálculo; si la tasa de reclamos supera el umbral escrito de antemano, se detiene el avance y se revierte. Un defecto que afecta a 1 de cada 1.000 entregas puede no aparecer en el 1 %, pero sí en el 50 %, de modo que el diseño de etapas debe considerar la frecuencia del defecto buscado. (Ilustración de SE-142.)

## Errores y confusiones comunes

- **Un defecto afecta a miles de personas el viernes**: despliegue a todos de golpe; corrección: desplegar por etapas con detección entre etapas.
- **Tras revertir faltan datos**: la inversa recrea estructura, no contenido.
- **Etapas sin umbral escrito**: se decide por intuición.
- **Creer que sustituye las pruebas.**

## Límites y cuándo no aplica

El despliegue progresivo reduce la exposición, no sustituye las pruebas (SE-142). No sirve para cambios que no admiten convivir (un cambio de esquema que exige que todos usen la misma versión) sin una estrategia de compatibilidad. Con muy poco tráfico, las etapas pequeñas no generan señal suficiente.
