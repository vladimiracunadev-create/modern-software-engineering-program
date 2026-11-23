# Derecho

[↑ Glosario](../../README.md) · [← Deque y ventanas](./deque-y-ventanas.md) · [Deriva →](./deriva.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Lo que una cuenta puede hacer, resultado de plan, excepciones y estado.

Definición de trabajo de [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md).

## Por qué importa

En [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md), el tema «Plan, derecho y bandera» importa porque mezclarlos vuelve el precio un despliegue y la bandera un derecho.

## Cómo funciona

Según [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md):

El **plan** es un paquete comercial: un nombre, un precio, un ciclo y un conjunto de derechos. Lo define producto y negocio y cambia por decisión de precios. El **derecho** es lo que una cuenta puede hacer en un momento dado: resulta de combinar el plan, las excepciones pactadas y el estado de la cuenta. Lo gobierna el negocio y se evalúa en cada operación. La **bandera de funcionalidad** controla qué código se ejecuta y lo gobierna ingeniería con el objetivo de desplegar sin exponer y retirarse después. Una función puede estar tras una bandera de lanzamiento *y* restringida a un plan: son dos puertas distintas con dos llaves distintas, y quitar la primera no debe tocar la segunda.

Según [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md):

El equipo de *Tablero* sustituye sus 63 comprobaciones por una llamada al motor. Primero inventaría: cada `if plan ==` pasa a una clave de derecho con su tipo; cada constante de límite pasa a una fila del plan. Después separa las banderas: la `nueva_exportacion` se retira (la función está al 100 % hace ocho meses), y «exportar» pasa a ser un derecho del plan. Las excepciones se cargan como filas con vencimiento: nueve clientes tenían pactos escondidos en el código, tres ya habían vencido sin que nadie lo notara.

## Ejemplo

Ejemplo de [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) (sección «Ejemplo profesional»):

El equipo de *Tablero* sustituye sus 63 comprobaciones por una llamada al motor. Primero inventaría: cada `if plan ==` pasa a una clave de derecho con su tipo; cada constante de límite pasa a una fila del plan. Después separa las banderas: la `nueva_exportacion` se retira (la función está al 100 % hace ocho meses), y «exportar» pasa a ser un derecho del plan. Las excepciones se cargan como filas con vencimiento: nueve clientes tenían pactos escondidos en el código, tres ya habían vencido sin que nadie lo notara.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una **funcionalidad** (exportar, inicio de sesión único, auditoría) es un derecho booleano: está o no incluida. ([SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md))
- Puede servir para una versión sencilla (funcionalidades activas por plan), pero los derechos tienen estado que cambia con la facturación, límites que dependen del consumo y excepciones con vencimiento y autoría: un modelo propio, ligado a tu base de clientes, suele ser más claro. ([SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md), [SE-475](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Excepción](../e/excepcion.md), [Plan](../p/plan.md), [Resultado](../r/resultado.md), [Bandera de funcionalidad](../b/bandera-de-funcionalidad.md), [Cambio de plan](../c/cambio-de-plan.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (65 clases más lo mencionan; las que más):

[SE-536](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md), [SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md), [SE-411](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md), [SE-415](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md), [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md), [SE-004](../../../classes/part-00-ingenieria-de-software-como-profesion/se-004-etica-interes-publico-y-consecuencias-de-las-decisiones-tecnicas/README.md), [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md), [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Spotify](../../../casos/exito/spotify.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «entitlement».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Deque y ventanas](./deque-y-ventanas.md) · [Deriva →](./deriva.md)
