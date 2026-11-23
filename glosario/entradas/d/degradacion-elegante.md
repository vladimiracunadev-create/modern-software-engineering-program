# Degradación elegante

[↑ Glosario](../../README.md) · [← Degradación](./degradacion.md) · [Degradación explícita →](./degradacion-explicita.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Respuesta reducida pero útil que se ofrece cuando la respuesta completa no es posible.

Definición de trabajo de [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md): Reducción controlada de funciones para mantener lo esencial bajo sobrecarga.
- En [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md): Respuesta parcial o antigua en lugar de un fallo total.

## Por qué importa

En [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), el tema «Degradación elegante» importa porque una respuesta pobre pero útil vale más que un error.

## Cómo funciona

Según [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), en la sección «Degradación elegante»:

Una **respuesta degradada** es una respuesta más barata y menos completa que sigue siendo útil: una miniatura genérica en lugar de la vista previa, la lista de entregas de la última caché con una marca de «actualizada hace 5 min», un resumen sin las estadísticas de la semana. Convierte un error en un servicio reducido. Tiene condiciones: debe ser mucho más barata que la respuesta completa (si cuesta casi lo mismo, no libera capacidad), debe ser honesta (la persona debe poder saber que está viendo algo degradado) y debe haberse decidido de antemano con producto, no improvisado durante el incidente. Y tiene riesgos: servir datos viejos puede ser inaceptable para una calificación y aceptable para un historial, y esa frontera es una decisión de negocio que hay que escribir.

## Ejemplo

Caso medido en la sección «Degradación elegante» de [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md):

Una **respuesta degradada** es una respuesta más barata y menos completa que sigue siendo útil: una miniatura genérica en lugar de la vista previa, la lista de entregas de la última caché con una marca de «actualizada hace 5 min», un resumen sin las estadísticas de la semana. Convierte un error en un servicio reducido. Tiene condiciones: debe ser mucho más barata que la respuesta completa (si cuesta casi lo mismo, no libera capacidad), debe ser honesta (la persona debe poder saber que está viendo algo degradado) y debe haberse decidido de antemano con producto, no improvisado durante el incidente.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md)) son:

- **Una dependencia secundaria tumba la función principal** — causa: pool compartido. Corrección: mamparos por dependencia o por criticidad.
- **El interruptor se abre y cierra sin parar** — causa: umbral demasiado bajo para fallos aleatorios. Corrección: subir el umbral o usar una ventana con fracción de fallos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos.

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
