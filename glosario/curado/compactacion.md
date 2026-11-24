# Compactación

## Definición

La **compactación** es conservar solo el último mensaje de cada clave, de modo que el log reconstruya un estado y no una historia (`SE-375`). El término tiene otros sentidos en el programa, y la entrada los distingue:

- En `SE-368` (datos): reescribir muchos archivos pequeños en pocos grandes.
- En `SE-580` y `SE-593` (agentes): sustituir parte del contexto o del historial por un resumen más corto.

Esta entrada desarrolla el sentido de `SE-375`, el del log de mensajes; los otros comparten la idea de reducir volumen a cambio de detalle, pero son mecanismos distintos.

## Por qué importa

Un log no puede crecer sin límite. Elegir cómo recortarlo es decidir si el log es un **registro de hechos** o una **tabla de estado**, y esa decisión debe tomarse con el consumidor que lo necesitará. Una mala elección pierde información que alguien necesitaba o conserva de más datos, incluidos datos personales.

## Cómo funciona

`SE-375` contrapone dos políticas. La **retención** descarta mensajes por antigüedad o tamaño: sirve para eventos que pierden valor, pero no para reconstruir un estado, porque una clave que no cambió dentro de la ventana desaparece. La **compactación** conserva el último valor de cada clave (más un marcador de borrado para las claves eliminadas): permite reconstruir el estado completo con mucho menos espacio, pero pierde la historia intermedia.

En el experimento de `SE-375`, la compactación guarda 1 999 entradas, cincuenta veces menos que el log completo, y reconstruye exactamente el mismo estado; renuncia a la historia: no se sabe qué valor tenía una clave hace un mes. La clase añade un criterio de retención: lo que permita los usos legítimos (reprocesar tras un defecto, incorporar un consumidor nuevo o auditar), recordando que cada día extra es almacenamiento y datos personales conservados. Si el consumidor necesita el último estado, la compactación es más barata y más segura que una retención larga.

## Ejemplo

Un tópico guarda cada cambio de la dirección de entrega de los estudiantes, con el identificador como clave. Con compactación, un servicio nuevo lee el log y obtiene la dirección vigente de cada estudiante, sin recorrer años de cambios. Un servicio de auditoría que necesita saber qué dirección tenía alguien el mes pasado no puede usar ese log compactado: necesita otro registro con retención de historia.

## Errores y confusiones comunes

- **Un servicio nuevo no ve datos anteriores**: tópico sin retención; se corrige con un log, o cargando la historia de otra fuente.
- **Usar retención por tiempo para reconstruir estado**: las claves sin cambios dentro de la ventana desaparecen.
- **Esperar historia de un log compactado**: solo conserva el último valor.
- **Olvidar los marcadores de borrado**: sin ellos, una clave eliminada no se distingue de una que nunca existió.
- **Confundir sentidos**: compactar archivos en un almacén no es lo mismo que compactar un log por clave.

## Límites y cuándo no aplica

No sirve cuando el valor está en la secuencia de hechos (auditoría, reproducción de un proceso) ni cuando las claves no identifican el estado que se quiere reconstruir. El experimento de `SE-375` usa datos sintéticos; los factores de reducción dependen de cuántas veces cambia cada clave. En los sentidos de `SE-580` y `SE-593`, el resumen pierde detalle que luego no se puede recuperar.
