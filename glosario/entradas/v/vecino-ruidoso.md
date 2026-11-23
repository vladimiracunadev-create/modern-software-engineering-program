# Vecino ruidoso

[↑ Glosario](../../README.md) · [← Vary](./vary.md) · [Vendorización →](./vendorizacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Inquilino cuya carga degrada el servicio de otros.

Definición de trabajo de [SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md): Inquilino cuyo consumo degrada el servicio de otros.
- En [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md): Carga que, al consumir recursos compartidos, degrada el servicio que reciben las demás.

## Por qué importa

En [SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), el tema «Vecino ruidoso» importa porque un inquilino puede degradar a todos.

En [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md), el tema «Vecino ruidoso» importa porque un cliente puede degradar a todos sin tocar sus datos.

## Cómo funciona

Según [SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md):

El extremo compartido es una sola base, un solo esquema y una columna que identifica al inquilino. El siguiente punto da a cada inquilino su esquema dentro de la misma base. Después, una base por inquilino. En el extremo opuesto, un despliegue completo (cómputo y datos) por inquilino. Cada paso hacia el aislamiento reduce el riesgo de fuga y el de vecino ruidoso, y sube el costo por inquilino y el trabajo de operaciones. Un diseño real suele mezclar: los inquilinos pequeños comparten y los grandes o regulados tienen recursos dedicados. La decisión no es una vez para siempre: debe poder moverse un inquilino de un nivel a otro, y eso es un requisito de diseño desde el inicio.

Según [SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md):

Tras el incidente del informe del rector, el equipo de *Avisos* escribe una prueba de fuga: crea dos inquilinos con datos distintos y ejecuta cada endpoint, informe y trabajo por lotes como el inquilino A, comprobando que nada del B aparece. La prueba encuentra tres rutas más con el mismo defecto, todas de informes antiguos. Introducen una barrera en la capa de acceso a datos: cada solicitud establece el inquilino una vez, y el acceso a tablas pasa por vistas por inquilino. Para el cliente con exigencia de residencia deciden una base separada en la región correspondiente, con el mismo esquema y la misma migración orquestada; calculan que, con tres bases dedicadas, la migración es manejable y fijan un umbral (veinte bases) a partir del cual la orquestación debe automatizarse.

## Ejemplo

Ejemplo de [SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md) (sección «Ejemplo profesional»):

Tras el incidente del informe del rector, el equipo de *Avisos* escribe una prueba de fuga: crea dos inquilinos con datos distintos y ejecuta cada endpoint, informe y trabajo por lotes como el inquilino A, comprobando que nada del B aparece. La prueba encuentra tres rutas más con el mismo defecto, todas de informes antiguos. Introducen una barrera en la capa de acceso a datos: cada solicitud establece el inquilino una vez, y el acceso a tablas pasa por vistas por inquilino.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cada paso hacia el aislamiento reduce el riesgo de fuga y el de vecino ruidoso, y sube el costo por inquilino y el trabajo de operaciones. ([SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md))

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

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md).

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
