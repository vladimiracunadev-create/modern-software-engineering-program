# Plano de control

[↑ Glosario](../../README.md) · [← Planificador](./planificador.md) · [Plantilla de experimento →](./plantilla-de-experimento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Componentes que crean, configuran, miden y facturan a los inquilinos.

Definición de trabajo de [SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md): Parte del sistema que gestiona inquilinos, planes, medición y facturación; distinta de la que atiende el uso de cada cliente.

## Por qué importa

En [SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md), el tema «Plano de control y plano de datos» importa porque separar quién crea y gobierna a los inquilinos de quién les sirve evita acoplar el alta al camino de uso.

## Cómo funciona

[SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md):

*Escenario ilustrativo: las cifras y los resultados de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md)) son: Se ejecutó un alta de cinco pasos con sqlite3 en memoria y un fallo inyectado, y se midió la creación de 200 inquilinos como fila y como esquema de 12 tablas; no se probó una base de producción, un proveedor de identidad ni un procesador de pagos, y el cociente de tiempos varió entre ejecuciones.

## Relación con otros conceptos

- **Prerrequisito:** [Inquilino](../i/inquilino.md).
- **Ver también:** [Componente](../c/componente.md), [Medición](../m/medicion.md), [Aprovisionamiento](../a/aprovisionamiento.md), [Baja](../b/baja.md), [CAC (costo de adquisición de cliente)](../c/cac-costo-de-adquisicion-de-cliente.md), [Compensación](../c/compensacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md), [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), [SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md), [SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md), [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Cloudflare](../../../casos/exito/cloudflare.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Planificador](./planificador.md) · [Plantilla de experimento →](./plantilla-de-experimento.md)
