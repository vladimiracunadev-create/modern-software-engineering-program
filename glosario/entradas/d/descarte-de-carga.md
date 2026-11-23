# Descarte de carga

[↑ Glosario](../../README.md) · [← Desbordamiento](./desbordamiento.md) · [Descomponer la petición →](./descomponer-la-peticion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Rechazo deliberado de solicitudes cuando la demanda supera la capacidad.

Definición de trabajo de [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md).

## Por qué importa

En [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), el tema «Descarte de carga» importa porque bajo sobrecarga hay que elegir qué se atiende.

## Cómo funciona

Según [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), en la sección «Descarte de carga»:

Cuando la carga supera la capacidad, algo no se va a atender. La pregunta es qué. Sin control, el sistema atiende todo con colas crecientes y casi nada llega a tiempo, y además trabaja para clientes que ya se fueron. Una **cola acotada** rechaza lo que excede un límite y protege la latencia de lo que entra, pero no distingue entre solicitudes. Un **descarte por prioridad** atiende primero lo crítico (entregar una tarea) y rechaza antes lo secundario (listar el historial). El descarte requiere dos decisiones previas: quién clasifica las solicitudes (el cliente o el servidor) y qué hace el rechazo visible para la persona usuaria; una respuesta «reintenta en un momento» con una cabecera de espera es mejor que un error genérico.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md):

El equipo hace un mapa de las dependencias de la API de entregas. Para la base de datos (crítica), no hay interruptor con respaldo posible: se reserva un pool propio de trabajadores para entregar tareas y se acota la cola; si la base cae, la API responde con un error claro. Para el servicio de miniaturas (secundario) se pone un interruptor con apertura por cinco fallos seguidos y 10 s abierto, un compartimento de 5 trabajadores y una respuesta degradada (un icono genérico) marcada con una cabecera.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md)) son:

- **Una dependencia secundaria tumba la función principal** — causa: pool compartido. Corrección: mamparos por dependencia o por criticidad.
- **El interruptor se abre y cierra sin parar** — causa: umbral demasiado bajo para fallos aleatorios. Corrección: subir el umbral o usar una ventana con fracción de fallos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Bulkhead](../b/bulkhead.md), [Circuit breaker](../c/circuit-breaker.md), [Criticidad](../c/criticidad.md), [Degradación elegante](./degradacion-elegante.md), [Interruptor de circuito](../i/interruptor-de-circuito.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md).

**Aparece en los casos de estudio:** [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «load shedding».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [AWS Builders' Library: Using load shedding to avoid overload](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/) — descarte de carga; autoridad: Amazon Web Services.
- [Fowler, «CircuitBreaker»](https://martinfowler.com/bliki/CircuitBreaker.html) — interruptor de circuito y sus estados; autoridad: autor del texto.
- [Microsoft Azure Architecture: patrón Bulkhead](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead) — aislamiento de recursos; autoridad: documentación de Microsoft.
- [Google SRE: Handling Overload](https://sre.google/sre-book/handling-overload/) — sobrecarga, criticidad y degradación; autoridad: Google, libro de ingeniería de confiabilidad.
- [Microsoft Azure Architecture: patrón Circuit Breaker](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker) — estados y parámetros del interruptor; autoridad: documentación de Microsoft.

---

[↑ Glosario](../../README.md) · [← Desbordamiento](./desbordamiento.md) · [Descomponer la petición →](./descomponer-la-peticion.md)
