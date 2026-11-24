# Inversión de prioridad

## Definición

La **inversión de prioridad** es la situación en que una tarea de alta prioridad espera por una de menor prioridad que, a su vez, es desplazada por otra de prioridad intermedia. Es el sentido de `SE-268` (sistemas de tiempo real y deadlines) y `SE-451` (RTOS y planificación). No es que la alta espere un poco: es que su espera depende de una tarea que no es la más urgente ni la que la bloquea.

## Por qué importa

Retrasa a la tarea más urgente sin que haya carga alta: el sistema puede parecer holgado y aun así incumplir un plazo. Una tarea media, que ni siquiera usa el recurso, puede hacer fallar a la alta.

## Cómo funciona

`SE-268` describe la secuencia:

1. La tarea de baja prioridad L toma un recurso (un mutex).
2. La de alta prioridad H se libera, necesita el recurso y queda bloqueada.
3. Una tarea de prioridad media M, que no necesita el recurso, se libera y **expulsa a L** (tiene más prioridad que L).
4. H espera además todo el cómputo de M. Esta es la inversión *sin acotar*.

Remedio: **herencia de prioridad.** Mientras L bloquea a H, L ejecuta con la prioridad de H, de modo que M no puede expulsarla y el bloqueo se acota a la sección crítica de L. Sha, Rajkumar y Lehoczky formalizaron estos protocolos, según cita la clase.

## Ejemplo

`SE-268` plantea tres tareas: H (alta; 2 ms de trabajo y necesita un mutex al empezar), M (media; 8 ms, no usa el mutex) y L (baja; toma el mutex en t = 0 y lo retiene 6 ms de cómputo, más 2 ms después). H se libera en t = 1 ms; M, en un instante variable entre 2 y 10 ms. Sin herencia, si M llega mientras L tiene el mutex, H espera además los 8 ms de M. Con herencia, L corre con la prioridad de H y M no la interrumpe, de modo que la espera de H queda acotada a lo que le quede a L en su sección crítica.

## Errores y confusiones comunes

- **Tratar la espera de H como «solo» el tiempo de L:** M puede añadirse.
- **Confundirla con el interbloqueo:** aquí el sistema avanza, pero tarde.
- **Creer que subir prioridades a todo evita el problema:** pierde el sentido de la prioridad.
- **No probarla con la tarea media en el peor instante.**

## Límites y cuándo no aplica

La herencia de prioridad acota la inversión, no la elimina: H sigue esperando la sección crítica de L. Con un solo núcleo y recursos sin compartir, el fenómeno no se da. Las duraciones del ejemplo son de la clase, no de un sistema real.
