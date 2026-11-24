# Trabajador

## Definición

Un **trabajador** (*worker*) es un proceso o hilo que toma trabajos de una cola y los ejecuta. Es el sentido de `SE-223` (schedulers, workers y trabajos por lotes) y de `SE-247` (jobs, colas y procesamiento diferido). `SE-591` (orquestador-trabajadores y evaluador-optimizador) le da un sentido propio en sistemas de agentes: un componente con contexto y herramientas mínimas que resuelve una subtarea. En ambos, el trabajador hace la unidad de trabajo que otro le asigna.

## Por qué importa

Separa *recibir* una petición de *ejecutarla*: la petición responde rápido y el trabajo pesado ocurre aparte. Pero introduce una pregunta de fiabilidad: ¿qué pasa si el trabajador cae a mitad de un trabajo? `SE-247` responde con el tiempo de visibilidad.

## Cómo funciona

`SE-247`: una cola guarda trabajos pendientes. Cuando un trabajador toma uno, **no lo borra**: lo oculta durante un **tiempo de visibilidad** y lo borra al confirmar. Si el trabajador cae, el tiempo vence y el trabajo reaparece para otro. Así no se pierde trabajo ante caídas.

La condición crítica: el tiempo de visibilidad debe superar la duración máxima razonable de un trabajo. Si es menor, el trabajo reaparece mientras el primer trabajador aún lo ejecuta, y se duplica sin que nadie haya caído. Por eso el efecto debe ser idempotente.

En `SE-591`, un trabajador de agentes recibe del orquestador una subtarea con el contexto y las herramientas mínimas necesarias; esto limita su radio de acción y facilita evaluar su resultado.

## Ejemplo

La plataforma de `SE-247` encola un trabajo de calificación por entrega mediante outbox (`SE-241`). El trabajo tiene identificador, estados consultables en `/trabajos/{id}`, plazo máximo de 10 minutos, tres intentos con retroceso y jitter, y una cola de muertos con alerta cuando crece. El manejador registra la nota con restricción única por identificador de trabajo, de modo que una repetición no duplica. Se dimensiona con la tasa de llegada λ, la de servicio μ y un objetivo de utilización máxima de 0,7 en el cierre de plazo.

## Errores y confusiones comunes

- **Un tiempo de visibilidad menor que la duración del trabajo,** que causa duplicados sin caída.
- **Confirmar el trabajo antes de terminarlo:** se pierde si cae.
- **Efectos no idempotentes en el manejador.**
- **Confundirlo con un hilo del servidor web** o con un trabajador de agentes: el contexto cambia.

## Límites y cuándo no aplica

Para tareas rápidas que el usuario espera, una cola añade complejidad innecesaria. El tamaño del grupo de trabajadores sigue las leyes de colas (utilización alta dispara la espera). Un trabajador envenenado por un trabajo que siempre falla requiere una cola de muertos.
