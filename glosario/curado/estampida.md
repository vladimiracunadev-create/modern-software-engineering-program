# Estampida

## Definición

La **estampida** (*cache stampede*) es el pico de consultas a la base que ocurre cuando muchas entradas de la caché faltan o expiran a la vez (`SE-356`). Una caché existe para proteger a la base; la estampida es el momento en que esa protección desaparece de golpe y toda la carga cae sobre ella.

## Por qué importa

El sistema funciona bien con la caché caliente y se cae justo cuando más depende de ella: tras un despliegue, un reinicio o la expiración de una clave popular. La decisión que cambia es que la caché no se diseña solo para el caso normal: se diseña también para el instante en que está vacía, porque la base quizá no tenga capacidad para atender sola ese tráfico.

## Cómo funciona

`SE-356` describe el mecanismo en dos escalas. A escala de una clave: cuando una clave popular expira, muchas peticiones simultáneas encuentran la caché vacía y todas van a la base a calcular lo mismo; el trabajo se repite tantas veces como peticiones llegaron en esa ventana. A escala del sistema: si mil claves se crearon al mismo tiempo (un despliegue, un arranque en frío), expiran juntas y el pico es mil veces peor. Una caché fría tras un reinicio es el mismo problema a escala de todo el sistema.

La causa es la sincronización: todas las entradas comparten el mismo instante de creación y el mismo TTL, así que expiran juntas. Los remedios que da la clase se combinan:

1. **Variar el TTL** con un componente aleatorio, para repartir las expiraciones en el tiempo.
2. **Recarga única**: solo una petición recalcula; las demás esperan o sirven el valor viejo.
3. **Precalentar o renovar** antes de que expire, y de forma escalonada tras un despliegue.

La clase añade el cuidado con las versiones: un lector lento puede rellenar la caché con un valor viejo después de una invalidación; se corrige guardando con versión y sin pisar una mayor.

## Ejemplo

Tras un despliegue, la caché de calificaciones queda vacía y el tráfico de una hora pico va directo a la base, que se satura. Con TTL aleatorio, recarga única y precalentamiento escalonado, solo una petición por clave llega a la base y las expiraciones dejan de coincidir. Escenario de las simulaciones de `SE-356`.

## Errores y confusiones comunes

- **La base se satura tras un despliegue**: caché fría y expiraciones simultáneas; se corrige variando el TTL, precalentando escalonadamente y con recarga única.
- **Un valor sigue viejo tras una invalidación**: relleno tardío de un lector lento; se corrige guardando con versión.
- **TTL idéntico para todo**: sincroniza las expiraciones.
- **Creer que más caché lo resuelve**: el problema es el instante de vacío, no la capacidad.

## Límites y cuándo no aplica

`SE-356` aclara que no usó una caché real ni red de entrega: el reloj es discreto, la popularidad Zipf, el 5 % de escrituras, la recarga de 2 s y los TTL son supuestos del autor, y no se midió la espera de los clientes ni la latencia. La estampida solo importa donde la base no soporta el tráfico sin caché; si la base tiene holgura de sobra, el efecto es menor. La recarga única sirve valores viejos durante la recarga, lo que exige que el negocio acepte esa obsolescencia.
