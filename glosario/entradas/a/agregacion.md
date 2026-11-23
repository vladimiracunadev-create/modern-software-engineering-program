# Agregación

[↑ Glosario](../../README.md) · [← Agilidad criptográfica](./agilidad-criptografica.md) · [Agregación y segmentos →](./agregacion-y-segmentos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Combinar en una respuesta datos de varios servicios.

Definición de trabajo de [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md).

## Por qué importa

En [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), el tema «Agregación» importa porque ahorra rondas al cliente.

## Cómo funciona

Según [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md):

El gateway responde «¿quién puede entrar y por dónde?»: enrutamiento, autenticación, límites de tasa, terminación de TLS, a veces agregación simple. El BFF responde «¿qué necesita esta pantalla?»: una API pensada para un tipo de cliente, propiedad del equipo que construye ese cliente, que consume los servicios y devuelve exactamente lo que la interfaz usa. La malla responde «¿cómo se hablan los servicios entre sí?»: cifrado, reintentos, plazos, métricas, políticas de acceso entre servicios, aplicados por proxies sin cambiar el código de cada uno. Se confunden porque los tres son proxies en algún sentido; se distinguen por su dueño y por su dirección del tráfico (norte-sur frente a este-oeste).

Según [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md):

Una agregación simple (juntar respuestas) es composición; una agregación que decide qué mostrar según reglas de negocio es lógica de dominio y debería vivir en un servicio o en el BFF de quien posee esa experiencia.

## Ejemplo

Ejemplo de [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md) (sección «Preguntas frecuentes»):

Una agregación simple (juntar respuestas) es composición; una agregación que decide qué mostrar según reglas de negocio es lógica de dominio y debería vivir en un servicio o en el BFF de quien posee esa experiencia.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El gateway responde «¿quién puede entrar y por dónde?»: enrutamiento, autenticación, límites de tasa, terminación de TLS, a veces agregación simple. ([SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Servicio](../s/servicio.md), [API gateway](./api-gateway.md), [BFF](../b/bff.md), [Defensa en profundidad](../d/defensa-en-profundidad.md), [Gateway](../g/gateway.md), [Malla de servicios](../m/malla-de-servicios.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-341 — BFF, API gateway y service mesh](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (20 clases más lo mencionan; las que más):

[SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md), [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-185](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md), [SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md), [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Agilidad criptográfica](./agilidad-criptografica.md) · [Agregación y segmentos →](./agregacion-y-segmentos.md)
