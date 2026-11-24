# Decisión humana abierta

## Definición

Una **decisión humana abierta** es un punto que el contrato o el paquete no puede cerrar y que debe tomar una persona con autoridad; se registra con responsable, fecha y la evidencia que la modificaría. Es el sentido de `SE-264` y de `SE-228`. Es lo contrario de una duda informal: tiene nombre, plazo y criterio de cierre.

## Por qué importa

Cambia si un paquete de trabajo se declara cerrado con honestidad. Según `SE-264`, lo que ninguna herramienta decide queda con nombre y fecha; sin ellas, el paquete aparenta estar cerrado cuando solo está silenciado. El defecto que previene es la decisión tomada por omisión: el primero que implementa el caso resuelve sin saber que decidía.

## Cómo funciona

El paquete lista lo que sigue pendiente. En el cliente de sincronización de `SE-264`: qué pérdida de intención es aceptable en un conflicto, qué plazo de desconexión se tolera, qué capacidades se excluyen en una plataforma, qué telemetría se considera aceptable. Cada decisión abierta lleva tres campos: un **responsable** (persona con autoridad), una **fecha** y la **evidencia** que la cerraría o la cambiaría.

La razón de la tercera es que una decisión abierta no es una pregunta retórica: se cierra con un dato o una prueba concretos (por ejemplo, la frecuencia observada de conflictos). Así, la decisión se revisa cuando llega esa evidencia en lugar de repetirse por opinión. `SE-228` añade el criterio de qué entra aquí: lo que el paquete no puede resolver por sí mismo, no lo que el equipo no tuvo tiempo de resolver.

## Ejemplo

El equipo del cliente de entregas arma su paquete con una carpeta por artefacto y un índice con identificadores. Una prueba de extremo a extremo desconecta el cliente, hace cuarenta ediciones y reconecta con un canal que pierde y duplica. Aun con la prueba verde queda abierta «cuánto tiempo sin conexión se tolera antes de pedir resincronizar»: se registra con responsable, fecha y el dato (distribución de desconexiones reales) que la resolvería.

## Errores y confusiones comunes

- **Dejarla en un comentario o en la memoria de alguien.** Sin responsable ni fecha, se pierde.
- **Confundirla con un defecto.** Un defecto se corrige; una decisión abierta se decide.
- **Registrar lo que el equipo puede resolver.** Debe ser lo que el paquete no puede decidir.
- **Cerrarla sin evidencia.** Se vuelve opinión y se reabre.

## Límites y cuándo no aplica

Las clases la presentan dentro de proyectos con paquete de entrega; en trabajo pequeño puede bastar una nota en el ADR. Una lista larga de decisiones abiertas es señal de que el paquete no está listo para entregarse, no de que esté bien documentado. Los experimentos de `SE-264` usan datos sintéticos y no sustituyen la evidencia real que cada decisión debe nombrar.
