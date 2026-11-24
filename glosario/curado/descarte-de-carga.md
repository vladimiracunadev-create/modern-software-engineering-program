# Descarte de carga

## Definición

El **descarte de carga** (*load shedding*) es el rechazo deliberado de solicitudes cuando la demanda supera la capacidad. Es la definición de trabajo de `SE-439`. El principio es que, cuando la carga excede lo que el sistema puede atender, algo no se va a atender; la única pregunta es qué, y si se decide de antemano o se deja al azar.

## Por qué importa

Cambia el comportamiento ante el peor momento. Sin control, el sistema intenta atenderlo todo: las colas crecen, casi nada llega a tiempo y además trabaja para clientes que ya se fueron (`SE-439`). El resultado es peor que rechazar a algunos, porque degrada a *todos*. Descartar a propósito protege la latencia de lo que entra y deja elegir qué se sacrifica.

## Cómo funciona

`SE-439` describe dos niveles:

- **Cola acotada:** rechaza lo que excede un límite. Protege la latencia de lo aceptado, pero no distingue entre solicitudes.
- **Descarte por prioridad:** atiende primero lo crítico (entregar una tarea) y rechaza antes lo secundario (listar el historial).

Requiere dos decisiones previas: **quién clasifica** las solicitudes (el cliente o el servidor) y **cómo se hace visible el rechazo**. Una respuesta del tipo «reintenta en un momento», con una cabecera de espera, es mejor que un error genérico, porque le dice al cliente cuándo volver y evita reintentos inmediatos que amplifiquen el problema.

La causa de que funcione está en la ley de Little: con capacidad fija, una cola que crece sin límite hace crecer el tiempo de espera sin límite; acotarla acota el tiempo.

## Ejemplo

Ilustración sobre la API de entregas de `SE-439` (sus experimentos usan tiempo virtual y semillas fijas): si la demanda supera la capacidad y no hay descarte, la cola crece y la latencia de todo se dispara. Con cola acotada, lo aceptado conserva su latencia y el resto recibe un rechazo inmediato. Con descarte por prioridad, entregar una tarea sigue funcionando mientras se rechaza antes listar el historial. Un rechazo de la forma siguiente cuesta casi nada y ordena el reintento:

```text
HTTP/1.1 429 Too Many Requests
Retry-After: 5
```

## Errores y confusiones comunes

- **Una dependencia secundaria tumba la función principal.** Causa: pool compartido; corrección: mamparos por dependencia o por criticidad (`SE-439`).
- **El interruptor se abre y cierra sin parar.** Umbral demasiado bajo para fallos aleatorios: subirlo o usar una ventana con fracción de fallos.
- **Descartar sin avisar al cliente.** Un error genérico invita a reintentar de inmediato.
- **Confundirlo con el cortacircuitos.** El cortacircuitos deja de *llamar* a una dependencia enferma; el descarte rechaza solicitudes que *entran*.

## Límites y cuándo no aplica

`SE-439` es operativa para la API de entregas y sus experimentos usan tiempo virtual, con resultados idénticos en Windows y Ubuntu (WSL2), no tráfico real. Descartar exige poder clasificar bien: si la prioridad está mal asignada, se sacrifica lo crítico. No sustituye a aumentar capacidad cuando la demanda sostenida la supera; solo da tiempo y evita el colapso. Y requiere clientes que respeten la señal de espera: sin ello, el rechazo se convierte en tormenta de reintentos.
