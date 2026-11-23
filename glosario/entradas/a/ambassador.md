# Ambassador

[↑ Glosario](../../README.md) · [← Alto riesgo](./alto-riesgo.md) · [Ambigüedad →](./ambiguedad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Proxy fuera de proceso que gestiona las conexiones salientes.

Definición de trabajo de [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md).

## Por qué importa

En [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), el tema «Sidecar y ambassador» importa porque sacan políticas de la aplicación a cambio de un salto

## Cómo funciona

Según [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md):

Un **sidecar** es un proceso auxiliar que se despliega junto a la aplicación y le presta servicios (registro, métricas, seguridad); un **ambassador** es un caso concreto: un proxy fuera de proceso que gestiona las conexiones salientes (reintentos, TLS, descubrimiento). La **fuerza** es sacar de la aplicación políticas que se repiten en muchos servicios y lenguajes. El **costo** es un salto de red adicional y una pieza operativa más. En una medición real con sockets locales (un servidor de eco, un proxy intermedio, 2000 repeticiones tras 100 de calentamiento) la mediana de una petición con su respuesta es de **unos 61 µs** directa y de **unos 122 µs** con el intermediario: aproximadamente **el doble**.

## Ejemplo

Caso medido en la sección «Sidecar y ambassador: políticas fuera de la aplicación» de [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md):

Un **sidecar** es un proceso auxiliar que se despliega junto a la aplicación y le presta servicios (registro, métricas, seguridad); un **ambassador** es un caso concreto: un proxy fuera de proceso que gestiona las conexiones salientes (reintentos, TLS, descubrimiento). La **fuerza** es sacar de la aplicación políticas que se repiten en muchos servicios y lenguajes. El **costo** es un salto de red adicional y una pieza operativa más.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md)) son: La simulación usa tasas y latencias elegidas por el autor y un grupo fijo; la degradación se mide como disponibilidad de una respuesta, no como utilidad; el salto se mide con un protocolo trivial en un equipo. El siguiente paso, `SE-322`, mira el diseño desde el otro lado: cómo reconocer, con medidas, un sistema que ya se ha vuelto difícil de cambiar.

## Relación con otros conceptos

- **Prerrequisito:** [Proxy](../p/proxy.md).
- **Ver también:** [Proceso](../p/proceso.md), [Bulkhead](../b/bulkhead.md), [Degradación](../d/degradacion.md), [Degradación elegante](../d/degradacion-elegante.md), [Ley de Little](../l/ley-de-little.md), [Salto](../s/salto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md), [SE-322](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md), [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Alto riesgo](./alto-riesgo.md) · [Ambigüedad →](./ambiguedad.md)
