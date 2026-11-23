# BFF

[↑ Glosario](../../README.md) · [← Benchmark versionado](./benchmark-versionado.md) · [Bfs y distancia no ponderada →](./bfs-y-distancia-no-ponderada.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Backend propio de un tipo de cliente, que proyecta lo que su interfaz necesita.

Definición de trabajo de [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md).

## Por qué importa

En [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), el tema «BFF» importa porque ahorra bytes y desacopla a los clientes entre sí.

## Cómo funciona

Según [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md):

El gateway responde «¿quién puede entrar y por dónde?»: enrutamiento, autenticación, límites de tasa, terminación de TLS, a veces agregación simple. El BFF responde «¿qué necesita esta pantalla?»: una API pensada para un tipo de cliente, propiedad del equipo que construye ese cliente, que consume los servicios y devuelve exactamente lo que la interfaz usa. La malla responde «¿cómo se hablan los servicios entre sí?»: cifrado, reintentos, plazos, métricas, políticas de acceso entre servicios, aplicados por proxies sin cambiar el código de cada uno. Se confunden porque los tres son proxies en algún sentido; se distinguen por su dueño y por su dirección del tráfico (norte-sur frente a este-oeste).

Según [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md):

El equipo móvil de *Avisos* mide la pantalla de inicio en una red 3G simulada y observa que la mayor parte del tiempo se va en tres idas y vueltas y en descargar listas completas. Propone un BFF móvil. El equipo de plataforma, que mantiene el gateway, propone en cambio que el gateway agregue las llamadas. Discuten con los números del modelo: agregar ahorra una ronda; proyectar ahorra bytes y, además, independiza al equipo móvil. Deciden un BFF móvil propiedad del equipo móvil, que consume los servicios a través del gateway existente (para no duplicar autenticación) y que no contiene reglas de dominio: solo composición y formato.

## Ejemplo

Ejemplo de [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md) (sección «Ejemplo profesional»):

El equipo móvil de *Avisos* mide la pantalla de inicio en una red 3G simulada y observa que la mayor parte del tiempo se va en tres idas y vueltas y en descargar listas completas. Propone un BFF móvil. El equipo de plataforma, que mantiene el gateway, propone en cambio que el gateway agregue las llamadas. Discuten con los números del modelo: agregar ahorra una ronda; proyectar ahorra bytes y, además, independiza al equipo móvil. Deciden un BFF móvil propiedad del equipo móvil, que consume los servicios a través del gateway existente (para no duplicar autenticación) y que no contiene reglas de dominio: solo composición y formato.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un BFF por cliente permite que el equipo móvil evolucione su API sin negociar con el equipo web. ([SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Backend](./backend.md), [Interfaz](../i/interfaz.md), [Tipo](../t/tipo.md), [Agregación](../a/agregacion.md), [API gateway](../a/api-gateway.md), [Defensa en profundidad](../d/defensa-en-profundidad.md).
- **Se confunde con:** **Punto profesional.** La clase existe para que distingas tres componentes que se confunden en casi todas las conversaciones de arquitectura: el API gateway, el BFF (backend for frontend) y la malla de servicios.

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Benchmark versionado](./benchmark-versionado.md) · [Bfs y distancia no ponderada →](./bfs-y-distancia-no-ponderada.md)
