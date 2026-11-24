# Lanzamiento por fases

## Definición

El **lanzamiento por fases** (*phased* o *staged release*) es la publicación de una versión a una fracción creciente de la base instalada para limitar el efecto de un error. Es el sentido de `SE-259` (actualizaciones, tiendas y distribución empresarial), donde las tiendas de aplicaciones lo ofrecen como lanzamiento escalonado. Es el mismo principio que el despliegue por etapas de flotas de dispositivos, aplicado al canal de una tienda.

## Por qué importa

Publicar a un porcentaje limita el daño de un error que se descubre tarde. En aplicaciones de cliente no se puede «volver atrás» una versión ya instalada con un botón, así que reducir cuántas personas la reciben antes de saber si funciona es la protección principal.

## Cómo funciona

Las tiendas permiten primero una fracción pequeña y luego más. Si la fracción pequeña revela un error grave, se detiene antes de llegar a todos. `SE-259` precisa su naturaleza: es una **red de seguridad, no una prueba**. Solo ve los fallos que aparecen en esa fracción y en el tiempo de espera.

Y necesita una forma de detectar fallos: errores y cierres inesperados por versión. Sin esa señal, la fase siguiente avanza a ciegas. Las condiciones de avance (porcentaje, tiempo de observación, métrica que debe mantenerse) se escriben antes de publicar.

## Ejemplo

El plan de lanzamiento del cliente en `SE-259`: publicar al 5 % en el canal automático y observar errores durante dos días; subir a 25, 50 y 100 % si no hay regresión; declarar una versión mínima soportada con un anuncio dentro de la aplicación; y retirar un campo del servidor solo cuando la telemetría muestre que menos del 1 % de las peticiones lo usa durante 14 días seguidos.

## Errores y confusiones comunes

- **Descubrir un error tras llegar al 100 % de la base:** el lanzamiento no tenía fases ni métricas de parada; la corrección es lanzar por fases con errores y cierres por versión (`SE-259`).
- **Creer que el 5 % equivale a probar:** solo ve lo que ocurre en esa fracción durante ese tiempo.
- **Avanzar por calendario** sin mirar las métricas.
- **Confundirlo con una bandera de funcionalidad:** el lanzamiento por fases controla quién *recibe la versión*; la bandera, quién *ve la función* ya instalada.

## Límites y cuándo no aplica

No ayuda con defectos que dependen de un subconjunto no representado en la fracción (un dispositivo o región) ni con errores que tardan en aparecer. Las personas que reciben la versión primero no son una muestra aleatoria si el canal es de adopción rápida. Una corrección urgente de seguridad puede obligar a acelerar las fases. La retirada de campos del servidor, como en el ejemplo, depende de que la versión mínima soportada esté definida.
