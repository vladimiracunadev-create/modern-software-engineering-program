# Sección crítica

## Definición

Una **sección crítica** es un tramo de código que accede a un dato compartido y se protege para que ningún otro contexto lo interrumpa o acceda al mismo dato a la vez. `SE-269` (interrupciones, concurrencia y estado compartido) la presenta en microcontroladores, donde el otro contexto es una interrupción; `SE-386` y `SE-305` la presentan en hilos: el tramo debe ejecutarse sin que otro hilo acceda al mismo dato.

## Por qué importa

Es la herramienta básica para que el estado compartido no se corrompa: sin perder incrementos, sin leer valores partidos y sin desbordar búferes (`SE-269`). La decisión práctica es qué protege exactamente y por cuánto tiempo.

## Cómo funciona

El mecanismo depende del contexto:

- **Con una interrupción (microcontrolador):** se desactivan las interrupciones durante el tramo, o se usa una instrucción atómica. `SE-269` lo ofrece, junto a la lectura doble y al número de secuencia, como defensa contra la lectura partida.
- **Con hilos (`SE-386`):** se usa un cerrojo (*lock*) que un solo hilo puede tener a la vez; los demás esperan.

Principios de diseño:

1. **Mantenerla corta.** Cuanto más dura, más latencia de interrupción (en embebidos) o más contención (en hilos).
2. **Proteger el dato, no el código:** cada dato compartido debe tener un único cerrojo asociado.
3. **No bloquear dentro:** esperar entrada/salida con el cerrojo tomado bloquea a todos.
4. **Ordenar los cerrojos** si hay varios, para evitar interbloqueos.

`SE-269` añade que una prueba corta encuentra algunos defectos de concurrencia y solo una **enumeración de todos los intercalados** encuentra otros.

## Ejemplo

El equipo de la plataforma en `SE-269` escribe una regla de datos compartidos del nodo: qué datos comparte la interrupción con el bucle principal y cómo se protege cada uno. Ilustración propia del caso de lectura partida: el programa principal desactiva las interrupciones, copia el valor de 16 bits, las reactiva, y trabaja con la copia.

## Errores y confusiones comunes

- **Proteger solo algunos accesos** al dato; uno sin protección rompe todo.
- **Secciones críticas largas** que bloquean la interrupción o a otros hilos.
- **Confundirla con una operación atómica:** la atómica la hace el hardware en una instrucción; la sección crítica protege varios pasos.
- **Tomar dos cerrojos en distinto orden** en rutas diferentes.

## Límites y cuándo no aplica

No ayuda con datos que no se comparten. Desactivar interrupciones no protege de otros núcleos. En lugar de proteger, a veces conviene evitar el compartir (pasar mensajes, copiar). Una sección crítica correcta no garantiza el rendimiento: la contención se mide aparte.
