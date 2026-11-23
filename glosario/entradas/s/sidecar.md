# Sidecar

[↑ Glosario](../../README.md) · [← Shell](./shell.md) · [Signed-off-by →](./signed-off-by.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Proceso auxiliar desplegado junto a la aplicación.

Definición de trabajo de [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md): Proceso auxiliar desplegado junto a un servicio que intercepta su tráfico.

## Por qué importa

En [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), el tema «Sidecar y ambassador» importa porque sacan políticas de la aplicación a cambio de un salto

## Cómo funciona

Según [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md):

Un **sidecar** es un proceso auxiliar que se despliega junto a la aplicación y le presta servicios (registro, métricas, seguridad); un **ambassador** es un caso concreto: un proxy fuera de proceso que gestiona las conexiones salientes (reintentos, TLS, descubrimiento). La **fuerza** es sacar de la aplicación políticas que se repiten en muchos servicios y lenguajes. El **costo** es un salto de red adicional y una pieza operativa más. En una medición real con sockets locales (un servidor de eco, un proxy intermedio, 2000 repeticiones tras 100 de calentamiento) la mediana de una petición con su respuesta es de **unos 61 µs** directa y de **unos 122 µs** con el intermediario: aproximadamente **el doble**.

Según [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md):

Una malla coloca un proxy junto a cada servicio y desvía el tráfico por él. Cada salto añade latencia. Se construyó un proxy TCP de reenvío de bytes (sin TLS, sin reintentos, sin métricas) y se midieron 400 llamadas por camino en ocho rondas intercaladas, con conexiones reutilizadas: la mediana de medianas fue 0,365 ms directa, 0,483 ms con un proxy (+0,117 ms) y 0,586 ms con dos (+0,221 ms); el p99 fue 0,670, 0,849 y 1,059 ms. Cada salto añadió entre 0,11 y 0,12 ms a una llamada que cuesta 0,36 ms.

## Ejemplo

Caso medido en la sección «Sidecar y ambassador: políticas fuera de la aplicación» de [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md):

Un **sidecar** es un proceso auxiliar que se despliega junto a la aplicación y le presta servicios (registro, métricas, seguridad); un **ambassador** es un caso concreto: un proxy fuera de proceso que gestiona las conexiones salientes (reintentos, TLS, descubrimiento). La **fuerza** es sacar de la aplicación políticas que se repiten en muchos servicios y lenguajes. El **costo** es un salto de red adicional y una pieza operativa más.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La decisión entre una **biblioteca** y un **sidecar** tampoco es solo de latencia: la biblioteca es más barata en tiempo y obliga a mantener una versión por lenguaje; el sidecar centraliza la política y añade operación. ([SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Proceso](../p/proceso.md), [Servicio](./servicio.md), [Agregación](../a/agregacion.md), [Ambassador](../a/ambassador.md), [API gateway](../a/api-gateway.md), [BFF](../b/bff.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md), [SE-322](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Shell](./shell.md) · [Signed-off-by →](./signed-off-by.md)
