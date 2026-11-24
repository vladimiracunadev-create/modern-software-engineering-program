# Fallo metaestable

## Definición

Un **fallo metaestable** es un estado degradado que persiste después de que desapareció el disparador que lo causó, porque un efecto de refuerzo lo sostiene. Es la definición de `SE-507`; `SE-438` lo presenta como un estado de sobrecarga que se sostiene por sí mismo cuando ya no está su causa inicial. El trabajo de Bronson et al. (HotOS 2021) lo formaliza como una clase de falla.

## Por qué importa

Rompe la intuición «arreglé la causa, el sistema se recuperará». En un fallo metaestable, retirar el disparador (un pico de carga, una dependencia lenta) no alcanza: el sistema sigue enfermo hasta que alguien interrumpe el ciclo. Cambia las prácticas de recuperación (hay que tener una acción para romper el ciclo, no solo para quitar la causa) y de diseño (evitar efectos de refuerzo).

## Cómo funciona

Hay tres elementos: un **disparador** temporal, un **estado degradado** y un **bucle de refuerzo** que alimenta el estado después del disparador. El refuerzo más común, según `SE-507`, son los reintentos. La falla termina, pero la cola que se formó sigue llena y las esperas siguen agotándose; entonces cada petición se reintenta y la carga efectiva sigue siendo triple de la capacidad. El trabajo útil por segundo cae mientras la carga ofrecida sube.

El sistema vuelve a ser sano solo si algo interrumpe el ciclo: un cortacircuitos que corta el flujo, un descarte de carga o un reinicio. `SE-507` cita el libro de SRE para el descarte de carga y las respuestas degradadas como formas de cortar el ciclo. La causa estructural es que el sistema tiene dos equilibrios estables, uno sano y otro degradado, y el disparador solo lo empuja del primero al segundo.

## Ejemplo

El experimento de `SE-507` (tiempo virtual, datos del autor): entre los 30 y los 60 s se retira la mitad de los hilos de la dependencia (la capacidad pasa de 200 a 100 peticiones por segundo, con 90 de demanda) y se mide cada 10 s la fracción de peticiones correctas.

- La configuración **A**, sin reintentos, no se entera: 90 caben en 100.
- La **C**, con reintentos y sin protección, cae a 10 % durante la falla y, cuando la dependencia recupera su capacidad a los 60 s, **sigue en 0 % durante los 60 s restantes**: cada petición agota otra vez la espera de 250 ms porque la cola de intentos viejos no se vacía, y cada fracaso se reintenta.
- La **E**, con cortacircuitos, baja a 44 % y sube a 100 % a los 75 s.

## Errores y confusiones comunes

- **Todo parece resiliente en el documento.** Se revisó la presencia de mecanismos, no su comportamiento; corrección de `SE-507`: inyectar la falla que cada mecanismo dice cubrir.
- **«El servicio no se recupera tras la falla».** Reintentos y cola mantienen la sobrecarga; hay que cortar el ciclo con cortacircuitos, descarte de carga o pausa con azar.
- **Buscar la causa raíz en el disparador.** El disparador explica el inicio; lo que mantiene el fallo es el refuerzo.
- **Confundirlo con una falla en cascada.** La cascada propaga a otros componentes; la metaestabilidad persiste sin disparador.

## Límites y cuándo no aplica

En `SE-507` no se inyectó ninguna falla en un sistema real: la dependencia de 8 hilos, el tráfico de 90 peticiones por segundo, las cinco configuraciones y las seis fallas son construcciones del autor, y los umbrales se eligieron para mostrar el fenómeno. El concepto aplica donde existe un bucle de refuerzo y capacidad limitada; un sistema sin reintentos ni colas persistentes se recupera al cesar la causa. La detección real suele llegar tarde, porque desde fuera el estado degradado parece una falla en curso.
