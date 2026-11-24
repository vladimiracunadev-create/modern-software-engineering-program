# Degradación elegante

## Definición

La **degradación elegante** (*graceful degradation*) es una respuesta reducida pero útil que se ofrece cuando la respuesta completa no es posible. `SE-439` (circuit breakers, bulkheads y degradación) es su clase principal. `SE-249` la ve como reducción controlada de funciones para mantener lo esencial bajo sobrecarga, y `SE-321` como una respuesta parcial o antigua en lugar de un fallo total.

## Por qué importa

Una respuesta pobre pero útil vale más que un error. Convierte un fallo en servicio reducido. La decisión que cambia es qué se sacrifica primero y qué nunca: eso es una decisión de producto que debe tomarse *antes* del incidente, no durante.

## Cómo funciona

`SE-439` define una **respuesta degradada** como una respuesta más barata y menos completa que sigue siendo útil. Ejemplos de la clase: una miniatura genérica en lugar de la vista previa, la lista de entregas de la última caché con una marca de «actualizada hace 5 min», un resumen sin las estadísticas de la semana.

Tres condiciones:

1. **Mucho más barata que la completa.** Si cuesta casi lo mismo, no libera capacidad.
2. **Honesta:** la persona debe poder saber que está viendo algo degradado.
3. **Decidida de antemano con producto,** no improvisada.

Y un riesgo: servir datos viejos puede ser inaceptable para una calificación y aceptable para un historial; esa frontera es una decisión de negocio que hay que escribir. Se combina con el circuit breaker (que decide *cuándo* dejar de llamar a una dependencia) y los bulkheads (que limitan el daño a un compartimento).

## Ejemplo

En `SE-439`, cuando la dependencia que genera vistas previas se satura, el servicio responde con la miniatura genérica y sigue atendiendo entregas. Ilustración propia: si el servicio de recomendaciones cae, la página de inicio muestra los más recientes en vez de los personalizados, con el aviso correspondiente.

## Errores y confusiones comunes

- **Degradar sin avisar,** de modo que se confunde un dato viejo con uno actual.
- **Una versión degradada tan cara como la completa,** que no alivia la sobrecarga.
- **Improvisarla en el incidente,** sin acordar qué datos pueden estar atrasados.
- **Confundirla con tolerancia a fallos:** la degradación acepta ofrecer menos; la tolerancia busca ofrecer lo mismo.

## Límites y cuándo no aplica

No sirve cuando la respuesta parcial es peligrosa o incorrecta (un saldo atrasado en una operación de pago, una calificación definitiva). Exige mantener y probar un camino adicional de código que casi nunca se ejecuta, y por eso se degrada también. No reemplaza arreglar la causa de la sobrecarga.
