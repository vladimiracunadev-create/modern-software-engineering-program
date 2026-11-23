# Tráfico norte-sur y este-oeste

[↑ Glosario](../../README.md) · [← Traducción con pérdida](./traduccion-con-perdida.md) · [Trama →](./trama.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

El que entra al sistema y el que circula entre servicios.

Definición de trabajo de [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md).

## Por qué importa

La clase donde se define, [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), existe con este propósito: la clase existe para que distingas tres componentes que se confunden en casi todas las conversaciones de arquitectura: el API gateway, el BFF (backend for frontend) y la malla de servicios.

## Cómo funciona

[SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md)) son: Los tamaños son de datos sintéticos, los tiempos de ronda son un modelo con supuestos del autor, el token es una demostración y el proxy es un reenviador mínimo. No se ejecutó ningún gateway, BFF ni malla real. El siguiente paso, `SE-342`, trata la identidad del inquilino: cómo se impide que los datos de un cliente aparezcan en la respuesta de otro y qué cuesta el aislamiento.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Servicio](../s/servicio.md), [Agregación](../a/agregacion.md), [API gateway](../a/api-gateway.md), [BFF](../b/bff.md), [Defensa en profundidad](../d/defensa-en-profundidad.md), [Gateway](../g/gateway.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Traducción con pérdida](./traduccion-con-perdida.md) · [Trama →](./trama.md)
