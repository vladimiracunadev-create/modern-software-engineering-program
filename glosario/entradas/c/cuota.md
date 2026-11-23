# Cuota

[↑ Glosario](../../README.md) · [← Cuórum](./cuorum.md) · [Cursor →](./cursor.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Límite de uso por inquilino y periodo; en tasa, un número de solicitudes por unidad de tiempo.

Definición de trabajo de [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md): Máximo de algo que ocurre en un periodo (llamadas por mes).

## Por qué importa

En [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md), el tema «Cuota de tasa» importa porque protege la capacidad rechazando el exceso, que es un costo para quien lo envía.

## Cómo funciona

Según [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md):

Una cuota por cliente limita cuántas solicitudes puede enviar por unidad de tiempo; lo que excede se rechaza (en HTTP, con 429 y un tiempo de reintento). En la simulación, un cubo de fichas con recarga de 2,4 por tick y ráfaga máxima de 10 deja a los otros siete en **p50 10 ms, p95 10 ms y p99 20 ms** durante toda la prueba, y el vecino ve su p99 en 10 ms para lo que sí se atiende, pero **56 619 solicitudes rechazadas**. Un detalle importante: 914 solicitudes de los clientes normales también se rechazaron, porque su llegada aleatoria (Poisson de media 1,9) a veces supera la recarga de 2,4 en un instante.

Según [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md):

El equipo de *Tablero* instrumenta primero: cada solicitud, trabajo y línea de log lleva el identificador del inquilino y el panel muestra el consumo por inquilino y por recurso. En una semana descubren que 11 de 4 000 clientes generan el 62 % de las consultas pesadas. Diseñan la política en tres capas: cuota de tasa por inquilino para las operaciones interactivas (con un cubo cuyo máximo cubre un pico legítimo y una respuesta 429 con el tiempo de reintento), cola justa con tope de longitud para las importaciones masivas (con prioridad baja) y una regla de traslado: el cliente que supera durante dos semanas el triple de su cuota recibe una oferta de plan con aislamiento dedicado.

## Ejemplo

Ejemplo de [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md) (sección «Ejemplo profesional»):

El equipo de *Tablero* instrumenta primero: cada solicitud, trabajo y línea de log lleva el identificador del inquilino y el panel muestra el consumo por inquilino y por recurso. En una semana descubren que 11 de 4 000 clientes generan el 62 % de las consultas pesadas.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una cuota demasiado ajustada castiga a quien no hace ruido; por eso la recarga se fija con holgura sobre el consumo típico y la ráfaga permitida (el tamaño del cubo) se ajusta a lo que un cliente legítimo hace en un pico. ([SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Inquilino](../i/inquilino.md), [Inquilino](../i/inquilino.md).
- **Ver también:** [Límite](../l/limite.md), [Bandera de funcionalidad](../b/bandera-de-funcionalidad.md), [Cambio de plan](./cambio-de-plan.md), [Cola justa](./cola-justa.md), [Contexto del inquilino](./contexto-del-inquilino.md), [Cubo de fichas](./cubo-de-fichas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (34 clases más lo mencionan; las que más):

[SE-535](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md), [SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md), [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), [SE-298](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md), [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-537](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Cuórum](./cuorum.md) · [Cursor →](./cursor.md)
