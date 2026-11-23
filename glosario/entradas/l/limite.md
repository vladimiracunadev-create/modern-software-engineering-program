# Límite

[↑ Glosario](../../README.md) · [← Lifecycle y caché](./lifecycle-y-cache.md) · [Límite de recursos →](./limite-de-recursos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Máximo de algo que existe a la vez (usuarios, proyectos).

Definición de trabajo de [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md).

## Por qué importa

En [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md), el tema «Tipos de derecho» importa porque un booleano, un límite y una cuota se verifican de forma distinta.

## Cómo funciona

Según [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md):

Una **funcionalidad** (exportar, inicio de sesión único, auditoría) es un derecho booleano: está o no incluida. Un **límite** (usuarios, proyectos) es un número máximo de algo que existe a la vez; se compara con el estado actual. Una **cuota por periodo** (llamadas de API por mes, correos enviados) es un número máximo de algo que ocurre en un periodo; se compara con el consumo medido (`SE-413`) y se renueva al comenzar el periodo. Distinguirlas importa porque se verifican en momentos distintos (el booleano al entrar a la función, el límite al crear, la cuota en cada llamada) y porque se comportan distinto ante un exceso: un límite puede dejar de crear y conservar lo existente; una cuota puede cobrar el exceso o bloquear.

Según [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md):

El equipo de *Tablero* sustituye sus 63 comprobaciones por una llamada al motor. Primero inventaría: cada `if plan ==` pasa a una clave de derecho con su tipo; cada constante de límite pasa a una fila del plan. Después separa las banderas: la `nueva_exportacion` se retira (la función está al 100 % hace ocho meses), y «exportar» pasa a ser un derecho del plan. Las excepciones se cargan como filas con vencimiento: nueve clientes tenían pactos escondidos en el código, tres ya habían vencido sin que nadie lo notara.

## Ejemplo

Ejemplo de [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) (sección «Ejemplo mínimo»):

Con una sola función, el cambio del precio de un plan o una excepción comercial es una fila nueva, no un despliegue. Una funcionalidad no incluida se modela como límite 0, lo que simplifica el motor a costa de una razón menos amable que la interfaz traduce a «no incluido en tu plan».

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **límite** (usuarios, proyectos) es un número máximo de algo que existe a la vez; se compara con el estado actual. ([SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md))
- Puede servir para una versión sencilla (funcionalidades activas por plan), pero los derechos tienen estado que cambia con la facturación, límites que dependen del consumo y excepciones con vencimiento y autoría: un modelo propio, ligado a tu base de clientes, suele ser más claro. ([SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md), [SE-475](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Bandera de funcionalidad](../b/bandera-de-funcionalidad.md), [Cambio de plan](../c/cambio-de-plan.md), [Cuota](../c/cuota.md), [Derecho](../d/derecho.md), [Excepción](../e/excepcion.md), [Grandfathering](../g/grandfathering.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (611 clases más lo mencionan; las que más):

[SE-415](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md), [SE-540](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md), [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md), [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), [SE-538](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-538-portafolio-entrevistas-y-defensa-profesional/README.md), [SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md), [SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md), [SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Lifecycle y caché](./lifecycle-y-cache.md) · [Límite de recursos →](./limite-de-recursos.md)
