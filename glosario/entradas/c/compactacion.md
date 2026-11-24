# Compactación

[↑ Glosario](../../README.md) · [← Commit colgante](./commit-colgante.md) · [Comparabilidad y reporte →](./comparabilidad-y-reporte.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

La **compactación** es conservar solo el último mensaje de cada clave, de modo que el log reconstruya un estado y no una historia ([SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md)). El término tiene otros sentidos en el programa, y la entrada los distingue:

- En [SE-368](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md) (datos): reescribir muchos archivos pequeños en pocos grandes.
- En [SE-580](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md) y [SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md) (agentes): sustituir parte del contexto o del historial por un resumen más corto.

Esta entrada desarrolla el sentido de [SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md), el del log de mensajes; los otros comparten la idea de reducir volumen a cambio de detalle, pero son mecanismos distintos.

## Por qué importa

Un log no puede crecer sin límite. Elegir cómo recortarlo es decidir si el log es un **registro de hechos** o una **tabla de estado**, y esa decisión debe tomarse con el consumidor que lo necesitará. Una mala elección pierde información que alguien necesitaba o conserva de más datos, incluidos datos personales.

## Cómo funciona

[SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md) contrapone dos políticas. La **retención** descarta mensajes por antigüedad o tamaño: sirve para eventos que pierden valor, pero no para reconstruir un estado, porque una clave que no cambió dentro de la ventana desaparece. La **compactación** conserva el último valor de cada clave (más un marcador de borrado para las claves eliminadas): permite reconstruir el estado completo con mucho menos espacio, pero pierde la historia intermedia.

En el experimento de [SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md), la compactación guarda 1 999 entradas, cincuenta veces menos que el log completo, y reconstruye exactamente el mismo estado; renuncia a la historia: no se sabe qué valor tenía una clave hace un mes. La clase añade un criterio de retención: lo que permita los usos legítimos (reprocesar tras un defecto, incorporar un consumidor nuevo o auditar), recordando que cada día extra es almacenamiento y datos personales conservados. Si el consumidor necesita el último estado, la compactación es más barata y más segura que una retención larga.

## Ejemplo

Un tópico guarda cada cambio de la dirección de entrega de los estudiantes, con el identificador como clave. Con compactación, un servicio nuevo lee el log y obtiene la dirección vigente de cada estudiante, sin recorrer años de cambios. Un servicio de auditoría que necesita saber qué dirección tenía alguien el mes pasado no puede usar ese log compactado: necesita otro registro con retención de historia.

## Errores y confusiones comunes

- **Un servicio nuevo no ve datos anteriores**: tópico sin retención; se corrige con un log, o cargando la historia de otra fuente.
- **Usar retención por tiempo para reconstruir estado**: las claves sin cambios dentro de la ventana desaparecen.
- **Esperar historia de un log compactado**: solo conserva el último valor.
- **Olvidar los marcadores de borrado**: sin ellos, una clave eliminada no se distingue de una que nunca existió.
- **Confundir sentidos**: compactar archivos en un almacén no es lo mismo que compactar un log por clave.

## Límites y cuándo no aplica

No sirve cuando el valor está en la secuencia de hechos (auditoría, reproducción de un proceso) ni cuando las claves no identifican el estado que se quiere reconstruir. El experimento de [SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md) usa datos sintéticos; los factores de reducción dependen de cuántas veces cambia cada clave. En los sentidos de [SE-580](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md) y [SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md), el resumen pierde detalle que luego no se puede recuperar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](./contextos.md), [Estado](../e/estado.md), [Almacén](../a/almacen.md), [Codificación por diccionario](./codificacion-por-diccionario.md), [Cola de trabajo](./cola-de-trabajo.md), [Estadísticas por grupo](../e/estadisticas-por-grupo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-580 — Gestión de contexto, resets y handoffs](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.
- [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), [SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Apache Kafka: documentación](https://kafka.apache.org/documentation/) — particiones, desplazamientos, retención y compactación; autoridad: proyecto Apache Kafka.
- [EIP: Point-to-Point Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html) — canal con un único receptor por mensaje; autoridad: autores del libro.
- [EIP: Publish-Subscribe Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html) — canal que entrega una copia a cada suscriptor; autoridad: autores del libro.
- [EIP: Competing Consumers](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CompetingConsumers.html) — varios consumidores que reparten los mensajes de un canal; autoridad: autores del libro.
- [Amazon SQS: colas estándar](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html) — entrega al menos una vez y orden de mejor esfuerzo; autoridad: Amazon Web Services.

---

[↑ Glosario](../../README.md) · [← Commit colgante](./commit-colgante.md) · [Comparabilidad y reporte →](./comparabilidad-y-reporte.md)
