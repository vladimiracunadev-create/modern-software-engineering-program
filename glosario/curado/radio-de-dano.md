# Radio de daño

## Definición

El **radio de daño** (*blast radius*) es el conjunto de recursos alcanzables con una credencial comprometida. Es el sentido de `SE-286` (confianza cero en la práctica). `SE-569` lo extiende a agentes: el conjunto de efectos que una acción errónea o maliciosa puede causar con la autoridad disponible. Es una medida de lo que se puede perder, no de la probabilidad de que ocurra.

## Por qué importa

Según `SE-286`, es la métrica que importa. No importa cuántos controles tiene un sistema, sino *cuántos servicios alcanza una credencial robada y durante cuánto tiempo*. Pasa la pregunta de «¿nos pueden entrar?» a «si entran, ¿hasta dónde llegan?».

## Cómo funciona

`SE-286` modela 200 servicios en 5 segmentos y una credencial robada de un servicio elegido al azar (5 000 repeticiones, semilla 48):

- **Red plana de confianza interna:** el atacante alcanza 200 servicios.
- **Segmentación de red en cinco partes:** 40.
- **Credenciales limitadas por destinatario** a las 3 dependencias autorizadas del servicio: 3.

Son valores del modelo, no medidas, pero la estructura es el punto: segmentar divide por el número de segmentos, y limitar por destinatario reduce el alcance al grado de dependencia del servicio comprometido. Ambas se combinan: la segmentación contiene lo que la política no previó. Para tu sistema, la cifra se calcula con el mapa real de dependencias.

En agentes (`SE-569`), el radio es lo que el agente *podría* hacer con las herramientas y permisos que tiene; se reduce con mínimo privilegio y confirmación humana para efectos graves.

## Ejemplo

Tras un incidente, el equipo de *Avisos* hace en `SE-286` tres cambios por orden de rendimiento. Primero, mapea los flujos entre servicios y descubre que el servicio de informes llamaba a doce servicios cuando solo necesitaba dos: reduce permisos por destinatario y el radio de daño de una credencial de ese servicio pasa de doce a dos.

## Errores y confusiones comunes

- **Medir cuántos controles hay** en vez de cuánto alcanza una credencial robada.
- **Credenciales amplias «por comodidad»,** compartidas entre servicios.
- **Confundirlo con la probabilidad de intrusión:** reduce el impacto, no la ocurrencia.
- **No acotar la duración:** una credencial que no caduca amplía el radio en el tiempo.

## Límites y cuándo no aplica

El número del modelo es de una simulación, no una medida de un sistema. El radio de daño solo contempla lo alcanzable con la credencial; no cubre daños por otros medios (ingeniería social, fallos de lógica). Reducirlo tiene costo operativo: más credenciales, más rotación y más reglas que mantener.
