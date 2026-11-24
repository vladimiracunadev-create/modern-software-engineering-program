# Vecino ruidoso

[↑ Glosario](../../README.md) · [← Vary](./vary.md) · [Vendorización →](./vendorizacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Un **vecino ruidoso** (*noisy neighbor*) es un inquilino cuya carga degrada el servicio de otros que comparten los mismos recursos ([SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md)). [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) lo generaliza a cualquier carga que, al consumir recursos compartidos, degrada el servicio que reciben las demás, por ejemplo en contenedores sobre un mismo nodo.

## Por qué importa

En un sistema compartido, el rendimiento de un cliente depende de lo que hagan los demás. Un solo cliente intensivo puede volver lento a todos, sin que haya fallo alguno. La decisión que cambia es cuánto aislamiento se da a cada inquilino, sabiendo que más aislamiento cuesta más.

## Cómo funciona

[SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md) presenta el espectro de aislamiento en una plataforma de varios inquilinos:

1. **Todo compartido**: una sola base, un solo esquema y una columna que identifica al inquilino.
2. **Un esquema por inquilino** dentro de la misma base.
3. **Una base por inquilino**.
4. **Un despliegue completo** (cómputo y datos) por inquilino.

Cada paso hacia el aislamiento reduce el riesgo de **fuga de datos** y el de **vecino ruidoso**, y sube el costo por inquilino y el trabajo de operaciones. Un diseño real suele mezclar: los inquilinos pequeños comparten y los grandes o regulados tienen recursos dedicados. La decisión no es para siempre: debe poder moverse un inquilino de un nivel a otro, y eso es un requisito de diseño desde el inicio.

En [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), la causa técnica es la competencia por recursos compartidos (CPU, memoria, disco, red) en un mismo nodo. Los mecanismos del núcleo para repartir y limitar el consumo (grupos de control, o cgroups) son la herramienta que acota cuánto puede tomar cada carga. [SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md) lo conecta con el producto SaaS: el cliente más grande suele ser el que más degrada a los demás y el que justifica recursos dedicados. En resiliencia, el patrón de mamparos (bulkhead) y las celdas aplican la misma idea de separar para que una carga no consuma lo de las otras.

## Ejemplo

Tras un incidente por un informe pesado, el equipo del caso de [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md) comprueba el aislamiento con una prueba de fuga entre inquilinos, y para el cliente con exigencia de residencia decide una base separada en su región. Para el cliente más grande, que degrada a los demás por volumen, se asignan recursos dedicados. Los pequeños siguen compartiendo.

## Errores y confusiones comunes

- **Creer que el aislamiento de datos resuelve el rendimiento**: una base con esquemas separados puede seguir compartiendo CPU y disco.
- **Aislar a todos por igual**: eleva el costo sin necesidad.
- **No poder mover a un inquilino de nivel**: la decisión se vuelve irreversible.
- **Medir solo promedios**: el vecino ruidoso se ve en la cola de latencia de los otros.

## Límites y cuándo no aplica

No aparece con un solo inquilino o con recursos holgados respecto a la carga. Aislar completamente cada inquilino elimina el problema pero pierde las economías de escala que justificaban compartir. [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md) presenta el espectro como decisiones de arquitectura con costos, no como una receta con umbrales universales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Inquilino](../i/inquilino.md), [Recurso](../r/recurso.md), [Servicio](../s/servicio.md), [Aislamiento de datos](../a/aislamiento-de-datos.md), [Barrera independiente](../b/barrera-independiente.md), [Barrera independiente de la consulta](../b/barrera-independiente-de-la-consulta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Shopify](../../../casos/exito/shopify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [namespaces(7)](https://man7.org/linux/man-pages/man7/namespaces.7.html) — espacios de nombres como vista propia de recursos globales; autoridad: manual de Linux (proyecto man-pages).
- [Control Group v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) — grupos de control y distribución de recursos; autoridad: documentación del núcleo Linux.
- [OCI Runtime Specification](https://github.com/opencontainers/runtime-spec) — configuración y ciclo de vida de un contenedor; autoridad: Open Container Initiative.
- [Firecracker: Lightweight Virtualization for Serverless Applications](https://www.usenix.org/conference/nsdi20/presentation/agache) — microVMs como compromiso entre aislamiento y arranque; autoridad: artículo de USENIX NSDI 2020.
- [Python: subprocess](https://docs.python.org/3/library/subprocess.html) — API usada para medir procesos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Vary](./vary.md) · [Vendorización →](./vendorizacion.md)
