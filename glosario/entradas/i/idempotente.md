# Idempotente

[↑ Glosario](../../README.md) · [← Idempotencia](./idempotencia.md) · [Identidad de carga de trabajo →](./identidad-de-carga-de-trabajo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Dicho de una operación cuyo efecto repetido es el mismo que el de una ejecución.

Definición de trabajo de [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md): Que repetir la operación con la misma entrada no cambia el resultado.

## Por qué importa

En [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), el tema «Idempotencia» importa porque una operación idempotente puede repetirse tras un fallo sin cambiar el resultado; si no lo es, hay que hacerla.

## Cómo funciona

Según [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md):

Una operación es idempotente si ejecutarla una vez o varias deja el sistema en el mismo estado. `PUT /entregas/42` con el cuerpo completo lo es; `POST /entregas` no lo es, porque cada llamada crea una entrega distinta; «sumar 1 a un contador» no lo es y «fijar el contador a 5» sí. Se puede convertir una operación no idempotente en idempotente asociándole una **clave**: la segunda llamada con la misma clave devuelve lo que devolvió la primera sin repetir el efecto.

Según [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md):

Lo es si la operación no es idempotente o si todos los clientes reintentan a la vez. Con clave y retroceso con jitter es una herramienta para convertir fallos transitorios en retardos.

## Ejemplo

Ejemplo de [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) (sección «Preguntas frecuentes»):

Lo es si la operación no es idempotente o si todos los clientes reintentan a la vez. Con clave y retroceso con jitter es una herramienta para convertir fallos transitorios en retardos.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md)) son:

- **Entregas duplicadas tras un error de red** — causa: POST sin clave de idempotencia. Corrección: clave por intención y restricción única.
- **El servicio vuelve a caer al recuperarse** — causa: reintentos sincronizados sin jitter. Corrección: retroceso exponencial con jitter y límite de intentos.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se puede convertir una operación no idempotente en idempotente asociándole una **clave**: la segunda llamada con la misma clave devuelve lo que devolvió la primera sin repetir el efecto. ([SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md))
- **reintentar una operación no idempotente y duplicar efectos**. ([SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Operación](../o/operacion.md), [Resultado](../r/resultado.md), [Aprovisionamiento](../a/aprovisionamiento.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Compensación](../c/compensacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (85 clases más lo mencionan; las que más):

[SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), [SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — métodos idempotentes y reintentos; autoridad: IETF.
- [Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — retroceso exponencial y jitter; autoridad: Amazon Builders' Library.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — restricciones únicas y transacciones; autoridad: Python Software Foundation.
- [Python: threading](https://docs.python.org/3/library/threading.html) — hilos de la prueba de carrera; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Idempotencia](./idempotencia.md) · [Identidad de carga de trabajo →](./identidad-de-carga-de-trabajo.md)
