# Interbloqueo

## Definición

Un **interbloqueo** (*deadlock*) es la situación en que un grupo de tareas espera cada una un recurso que retiene otra del grupo, de modo que ninguna puede avanzar (`SE-386`). Detiene al grupo entero sin producir un error: el sistema simplemente deja de responder.

## Por qué importa

Es uno de los fallos de concurrencia más difíciles de diagnosticar, porque no hay excepción ni registro; solo silencio. Y suele aparecer solo bajo carga, cuando varias tareas coinciden en el orden desafortunado. La decisión que cambia es cómo se toman los cerrojos: con una regla global que impide el ciclo por construcción, no confiando en que no coincidan.

## Cómo funciona

`SE-386` recoge el resultado de Coffman y colaboradores: un interbloqueo requiere cuatro condiciones a la vez:

1. **Exclusión mutua**: el recurso no se comparte.
2. **Retención y espera**: se retiene un recurso mientras se pide otro.
3. **Ausencia de expropiación**: nadie puede quitar el recurso a quien lo tiene.
4. **Espera circular**: existe un ciclo de tareas, cada una esperando a la siguiente.

Basta eliminar **una** para que no ocurra. La más práctica de eliminar es la espera circular, imponiendo un **orden global de adquisición**: todos los cerrojos se toman siempre en el mismo orden (por ejemplo, por identificador creciente). Si la tarea A toma primero el recurso 1 y luego el 2, y la B hace lo mismo en el mismo orden, no puede formarse el ciclo en el que A espera al 2 reteniendo el 1 mientras B espera al 1 reteniendo el 2.

La clase aclara un error de método: un tiempo límite al adquirir **no previene** el interbloqueo; lo convierte en un error que hay que manejar, liberando lo tomado y reintentando con otro orden. Es una mitigación, no una prevención.

## Ejemplo

Dos transferencias entre cuentas A y B: una toma el cerrojo de A y pide el de B; la otra toma el de B y pide el de A. Quedan esperándose para siempre. Con un orden global (siempre primero la cuenta de menor identificador), ambas piden primero A y luego B, y una espera a la otra pero termina. Ejemplo ilustrativo del mecanismo de `SE-386`.

## Errores y confusiones comunes

- **El servicio se congela y no hay error**: espera circular entre cerrojos; se corrige con orden global de adquisición.
- **Contadores que a veces están un poco bajos**: leer-sumar-escribir sin sincronizar; se corrige con una operación atómica o una sección crítica. Es una carrera de datos, no un interbloqueo.
- **Creer que un tiempo límite lo previene**: solo lo vuelve visible.
- **Confundirlo con contención**: una tarea que espera mucho no está interbloqueada si el recurso eventualmente se libera.

## Límites y cuándo no aplica

El orden global exige que todos los puntos de adquisición lo respeten; un solo acceso fuera de orden reabre el riesgo, y en código que adquiere recursos dinámicos (de los que no se conoce el orden de antemano) puede ser difícil de aplicar. Con un solo recurso, o sin retención y espera, no hay interbloqueo posible. En sistemas distribuidos, el equivalente aparece entre servicios, y ahí se detecta con tiempos límite y observabilidad, no con orden de cerrojos.
