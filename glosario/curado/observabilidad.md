# Observabilidad

## Definición

La **observabilidad** es la propiedad de un sistema que permite explicar su comportamiento interno a partir de lo que emite, incluidas preguntas que nadie previó al diseñarlo. Las clases coinciden en el núcleo y varían el énfasis: `SE-033` la define como capacidad de inferir el estado interno a partir de las salidas disponibles, `SE-308` como capacidad de inferir el estado interno de un sistema a partir de lo que emite, `SE-493` añade «incluidas preguntas no previstas» y `SE-585` la aplica a agentes: explicar el comportamiento a partir de lo registrado. Hereda la idea de la teoría de control, donde un sistema es observable si su estado interno se deduce de sus salidas; la ingeniería de software la usa en sentido práctico.

## Por qué importa

Un sistema que falla de una forma nueva solo se diagnostica si ya emitía la información necesaria. La diferencia con monitorear es decisiva en un incidente: el monitoreo avisa de lo que se esperaba, la observabilidad permite investigar lo inesperado. `SE-493` propone un criterio empírico para saber si la tienes: puedes responder «¿qué tienen en común las peticiones lentas de las 14:03?» sin desplegar código nuevo para poder preguntarlo.

## Cómo funciona

Un sistema es más observable cuanto más preguntas permiten responder sus señales (`SE-033`). Las tres señales clásicas cumplen funciones distintas: los **logs** describen eventos, las **métricas** agregan medidas y las **trazas** relacionan los pasos de una operación a través de componentes. En un diagnóstico local también cuentan los códigos de salida, la configuración efectiva, la versión y el estado del sistema.

`SE-493` ordena el diseño con dos miradas complementarias:

- **Caja negra:** una sonda se comporta como una persona usuaria, llama al endpoint y mide lo que recibe; detecta síntomas con independencia de la causa y es la que suele despertar a alguien.
- **Caja blanca:** la instrumentación mira el interior (colas, caches, errores internos); explica lo que ocurrió y permite decidir qué hacer.

Se necesitan las dos. Y la causa de que ninguna señal aislada baste la da `SE-033`: un log registra lo que el programa alcanzó a emitir, y un cierre abrupto puede dejar eventos sin emitir. En sistemas con agentes, `SE-585` pide que la traza sea un contrato: por paso, la acción, el resultado, la observación resumida y el contexto visible, de modo que cada decisión de diagnóstico tenga un campo del que salir.

## Ejemplo

Una consulta tarda 4 segundos a las 14:03. Con solo un panel que muestra la latencia media, sabes que algo empeoró. Con trazas que llevan atributos (versión, tenant, región, tipo de consulta), puedes agrupar las peticiones lentas y ver qué comparten, sin añadir instrumentación nueva. Esa segunda capacidad es la que `SE-493` llama observabilidad; la primera es monitoreo. (Ilustración construida con el criterio de la clase; no es un caso medido.)

## Errores y confusiones comunes

- **Equiparar observabilidad con tener un panel.** Un panel responde preguntas previstas; la observabilidad se mide por las que no se previeron.
- **Confundirla con monitoreo.** El monitoreo comprueba condiciones conocidas («disco por encima del 90 %»); `SE-493` los distingue explícitamente.
- **Creer que las cuatro señales de oro la garantizan.** Latencia, tráfico, errores y saturación son un buen mínimo de monitoreo, no garantizan observabilidad (`SE-493`).
- **Confiar en una sola señal.** Un log no cuenta lo que el programa no alcanzó a emitir (`SE-033`).

## Límites y cuándo no aplica

Las clases advierten que las cuatro señales de oro no garantizan observabilidad (`SE-493`) y que ninguna señal aislada es verdad completa: un log solo registra lo que el programa alcanzó a emitir (`SE-033`). La observabilidad se define por la capacidad de explicar, no por tener herramientas; la clase la mide con una pregunta no prevista, no con el número de paneles.
