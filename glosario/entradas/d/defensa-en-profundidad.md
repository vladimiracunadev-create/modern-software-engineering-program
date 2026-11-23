# Defensa en profundidad

[↑ Glosario](../../README.md) · [← Defecto sembrado](./defecto-sembrado.md) · [Defensa por profundidad →](./defensa-por-profundidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Validar en cada capa en lugar de confiar en una sola barrera.

Definición de trabajo de [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md).

## Por qué importa

La clase donde se define, [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), existe con este propósito: la clase existe para que distingas tres componentes que se confunden en casi todas las conversaciones de arquitectura: el API gateway, el BFF (backend for frontend) y la malla de servicios.

## Cómo funciona

Según [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md):

Se construyó un token de la forma `{estudiante, firma}` donde la firma es un HMAC-SHA256 del identificador con una clave (derivada de bytes fijos del laboratorio, no una clave real). Se modelaron cuatro servicios con dos políticas. En la primera, cada servicio confía en el gateway y no valida nada: ante una petición interna falsificada con una firma inventada, la aceptan 4 de 4. En la segunda, cada servicio valida la firma con comparación en tiempo constante: aceptan la falsificada 0 de 4 y la válida 4 de 4. El gateway sigue siendo útil (rechaza tráfico malformado, limita tasas y centraliza la identidad), pero no es la única barrera. Una petición falsificada puede llegar por otro servicio comprometido, por una herramienta de operaciones o por una configuración de red equivocada.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La defensa en profundidad cuesta una verificación de firma por llamada, y la gestión de claves, que el laboratorio no resuelve. ([SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa](../c/capa.md), [Agregación](../a/agregacion.md), [API gateway](../a/api-gateway.md), [BFF](../b/bff.md), [Gateway](../g/gateway.md), [Malla de servicios](../m/malla-de-servicios.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Defecto sembrado](./defecto-sembrado.md) · [Defensa por profundidad →](./defensa-por-profundidad.md)
