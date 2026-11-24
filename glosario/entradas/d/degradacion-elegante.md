# Degradación elegante

[↑ Glosario](../../README.md) · [← Degradación](./degradacion.md) · [Degradación explícita →](./degradacion-explicita.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

La **degradación elegante** (*graceful degradation*) es una respuesta reducida pero útil que se ofrece cuando la respuesta completa no es posible. [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) (circuit breakers, bulkheads y degradación) es su clase principal. [SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) la ve como reducción controlada de funciones para mantener lo esencial bajo sobrecarga, y [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md) como una respuesta parcial o antigua en lugar de un fallo total.

## Por qué importa

Una respuesta pobre pero útil vale más que un error. Convierte un fallo en servicio reducido. La decisión que cambia es qué se sacrifica primero y qué nunca: eso es una decisión de producto que debe tomarse *antes* del incidente, no durante.

## Cómo funciona

[SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) define una **respuesta degradada** como una respuesta más barata y menos completa que sigue siendo útil. Ejemplos de la clase: una miniatura genérica en lugar de la vista previa, la lista de entregas de la última caché con una marca de «actualizada hace 5 min», un resumen sin las estadísticas de la semana.

Tres condiciones:

1. **Mucho más barata que la completa.** Si cuesta casi lo mismo, no libera capacidad.
2. **Honesta:** la persona debe poder saber que está viendo algo degradado.
3. **Decidida de antemano con producto,** no improvisada.

Y un riesgo: servir datos viejos puede ser inaceptable para una calificación y aceptable para un historial; esa frontera es una decisión de negocio que hay que escribir. Se combina con el circuit breaker (que decide *cuándo* dejar de llamar a una dependencia) y los bulkheads (que limitan el daño a un compartimento).

## Ejemplo

En [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), cuando la dependencia que genera vistas previas se satura, el servicio responde con la miniatura genérica y sigue atendiendo entregas. Ilustración propia: si el servicio de recomendaciones cae, la página de inicio muestra los más recientes en vez de los personalizados, con el aviso correspondiente.

## Errores y confusiones comunes

- **Degradar sin avisar,** de modo que se confunde un dato viejo con uno actual.
- **Una versión degradada tan cara como la completa,** que no alivia la sobrecarga.
- **Improvisarla en el incidente,** sin acordar qué datos pueden estar atrasados.
- **Confundirla con tolerancia a fallos:** la degradación acepta ofrecer menos; la tolerancia busca ofrecer lo mismo.

## Límites y cuándo no aplica

No sirve cuando la respuesta parcial es peligrosa o incorrecta (un saldo atrasado en una operación de pago, una calificación definitiva). Exige mantener y probar un camino adicional de código que casi nunca se ejecuta, y por eso se degrada también. No reemplaza arreglar la causa de la sobrecarga.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Función](../f/funcion.md), [Reducción](../r/reduccion.md), [Sobrecarga](../s/sobrecarga.md), [429](../0-9/429.md), [Ambassador](../a/ambassador.md), [Bulkhead](../b/bulkhead.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-599](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md).

**Aparece en los casos de estudio:** [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «CircuitBreaker»](https://martinfowler.com/bliki/CircuitBreaker.html) — interruptor de circuito y sus estados; autoridad: autor del texto.
- [Microsoft Azure Architecture: patrón Bulkhead](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead) — aislamiento de recursos; autoridad: documentación de Microsoft.
- [AWS Builders' Library: Using load shedding to avoid overload](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/) — descarte de carga; autoridad: Amazon Web Services.
- [Google SRE: Handling Overload](https://sre.google/sre-book/handling-overload/) — sobrecarga, criticidad y degradación; autoridad: Google, libro de ingeniería de confiabilidad.
- [Microsoft Azure Architecture: patrón Circuit Breaker](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker) — estados y parámetros del interruptor; autoridad: documentación de Microsoft.

---

[↑ Glosario](../../README.md) · [← Degradación](./degradacion.md) · [Degradación explícita →](./degradacion-explicita.md)
