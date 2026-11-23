# Inquilino

[↑ Glosario](../../README.md) · [← Inmutabilidad y evolución de valores](./inmutabilidad-y-evolucion-de-valores.md) · [Inquilino venenoso →](./inquilino-venenoso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Cliente cuyos datos y comportamiento deben aislarse de los de otros.

Definición de trabajo de [SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md): Cliente cuya cuenta, usuarios y datos el producto trata como una unidad de aislamiento y de facturación.

## Por qué importa

En [SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), el tema «Vecino ruidoso» importa porque un inquilino puede degradar a todos.

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

- El extremo compartido es una sola base, un solo esquema y una columna que identifica al inquilino. ([SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md))
- Después decide el nivel de aislamiento por inquilino (pool, silo o híbrido) con el costo medido de operar tu alternativa de aislamiento fuerte y el disparador que movería a un cliente de nivel. ([SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Aislamiento](../a/aislamiento.md), [Producto](../p/producto.md), [Aislamiento de datos](../a/aislamiento-de-datos.md), [Baja](../b/baja.md), [Barrera independiente](../b/barrera-independiente.md), [Barrera independiente de la consulta](../b/barrera-independiente-de-la-consulta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (22 clases más lo mencionan; las que más):

[SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md), [SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md), [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), [SE-411](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «tenant».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Inmutabilidad y evolución de valores](./inmutabilidad-y-evolucion-de-valores.md) · [Inquilino venenoso →](./inquilino-venenoso.md)
