# Estrategia de caché

## Definición

Una **estrategia de caché** es la regla que decide, para cada petición, si se responde desde la caché, desde la red o desde ambas. Es el sentido de `SE-237` (PWA, caché, offline y sincronización), donde se aplica a un *service worker*. No hay una estrategia correcta: cada una intercambia obsolescencia por velocidad y disponibilidad.

## Por qué importa

La estrategia decide qué ve la persona cuando la red es lenta o está caída, y cuán viejo puede ser lo que ve. Elegir mal significa mostrar una calificación desactualizada o dejar una aplicación en blanco sin conexión.

## Cómo funciona

`SE-237` describe cuatro estrategias:

- **Solo red:** lo más fresco; no funciona sin conexión.
- **Caché primero:** responde al instante y puede servir contenido viejo indefinidamente.
- **Red primero con respaldo en caché:** frescura cuando hay red y degradación elegante cuando no; a costa de esperar el tiempo de espera cuando la red es mala.
- **Revalidar en segundo plano** (*stale-while-revalidate*): responde desde la caché y renueva para la próxima vez; rápido y casi fresco, con la limitación de mostrar una versión vieja una vez.

La elección es **por tipo de recurso**: el esqueleto de la aplicación (HTML, CSS, JavaScript, iconos) admite caché primero; los datos de una calificación, no.

## Ejemplo

La aplicación de entregas de `SE-237` precarga el esqueleto con una revisión por huella y lo sirve con caché primero; la lista de entregas usa revalidar en segundo plano; las calificaciones, red primero con tiempo de espera corto. El script del service worker se sirve con `no-cache`, la versión nueva avisa a la persona («hay una versión nueva») y se conserva una generación anterior.

## Errores y confusiones comunes

- **Aplicar una sola estrategia a todo.**
- **Caché primero para datos que cambian:** se sirve contenido viejo indefinidamente.
- **Cachear el propio script del service worker,** que impide actualizar.
- **Confundir estrategia con política de expiración:** la estrategia decide el orden de consulta; la expiración decide cuándo un dato deja de valer.

## Límites y cuándo no aplica

No resuelve la invalidación: saber cuándo un dato cacheado dejó de ser válido es un problema aparte. No aplica a recursos no cacheables (respuestas personalizadas sensibles). Y la estrategia vale en el navegador y el contexto de la clase; otras cachés (de servidor, de CDN) tienen sus propias reglas.
