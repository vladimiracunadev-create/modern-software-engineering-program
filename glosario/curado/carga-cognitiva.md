# Carga cognitiva

## Definición

La **carga cognitiva** es el esfuerzo mental que un equipo dedica a recordar y decidir cosas ajenas a su trabajo principal (`SE-406`). `SE-489` la formula como la cantidad de cosas que un equipo debe conocer y mantener para hacer su trabajo, y `SE-530` como la cantidad de contexto que debe mantener para operar y cambiar lo que posee. El programa la toma de *Team Topologies*.

## Por qué importa

La capacidad de un equipo es finita. Cada herramienta de despliegue, política de seguridad o convención de infraestructura que debe recordar compite con el producto. La decisión profesional que cambia es qué se ofrece a los equipos: una plataforma interna se justifica si **reduce** esa carga, y no por lo mucho que ofrece. `SE-489` lo dice así: la plataforma existe para reducirla, no para sumar otra cosa que aprender.

## Cómo funciona

El trabajo de un equipo de producto tiene una carga cognitiva limitada; lo que excede ese límite se hace peor o se olvida. La respuesta que enseña el programa es mover capacidades repetidas (aprovisionamiento, canalizaciones, observabilidad, seguridad) a una plataforma ofrecida en autoservicio, con enfoque de producto: usuarios identificados, necesidades entendidas, interfaces fijadas, uso medido y retiro de lo que no sirve (documento de plataformas de la CNCF, que `SE-489` cita).

De ahí se deduce algo contraintuitivo: la plataforma compite con las alternativas que los equipos tienen a mano (construirlo ellos, usar un servicio externo, copiar la solución de otro equipo), y su éxito se mide por lo que los equipos **eligen**, no por lo que ofrece. Se vuelve costosa cuando ofrece mucho y se usa poco, e inútil cuando no ofrece lo necesario en el momento justo (`SE-406`).

`SE-530` aplica la idea al tamaño de lo que un equipo posee: si debe mantener demasiado contexto para operar y cambiar sus sistemas, la propiedad está mal dimensionada.

## Ejemplo

Un equipo debe crear un servicio nuevo y recordar límites de recursos, usuario sin privilegios, etiqueta de dueño y sondas de salud. Con un camino dorado, esas guardas vienen incorporadas y el equipo solo piensa en su lógica. La carga baja porque deja de recordar lo que la plataforma ya hace. Ilustración de `SE-406`.

## Errores y confusiones comunes

- **Los equipos no usan el camino**: es más difícil que lo manual o no cubre su caso; se corrige midiendo pasos y excepciones.
- **Plataforma saturada de solicitudes**: baja adopción y servicios hechos a mano; reducir pasos y atender primero las excepciones.
- **Medir la plataforma por funciones ofrecidas** en vez de por reducción real de esfuerzo.
- **Confundirla con carga de trabajo**: el número de tareas no es lo mismo que cuánto contexto hay que sostener a la vez.

## Límites y cuándo no aplica

El programa no da una unidad ni una medida estándar de carga cognitiva: es un criterio de diseño, no una métrica con umbral. Se estima con proxies (pasos, excepciones, tiempo de arranque) que hay que elegir y justificar. No sustituye la conversación con los equipos sobre qué les cuesta.
