# Cola justa

[↑ Glosario](../../README.md) · [← Cola de trabajo](./cola-de-trabajo.md) · [Cola larga →](./cola-larga.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Una cola por inquilino con un planificador que atiende por turnos.

Definición de trabajo de [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md).

## Por qué importa

En [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md), el tema «Cola justa» importa porque protege a los demás sin rechazar, pero hace esperar más al que excede.

## Cómo funciona

Según [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md):

En lugar de rechazar, se mantiene una cola por cliente y el planificador atiende por turnos (un trabajo de cada cliente con trabajo pendiente). Los otros siete quedan igual: **p50 10 ms, p95 10 ms y p99 20 ms**. El vecino no pierde ninguna solicitud, pero espera lo que su propia cola le impone: **p50 de 34 870 ms y p99 de 74 280 ms**. La cola justa traslada el daño al causante en forma de espera y mantiene todo el trabajo, lo que conviene si el cliente necesita que su importación termine aunque tarde.

Según [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md):

El equipo de *Tablero* instrumenta primero: cada solicitud, trabajo y línea de log lleva el identificador del inquilino y el panel muestra el consumo por inquilino y por recurso. En una semana descubren que 11 de 4 000 clientes generan el 62 % de las consultas pesadas. Diseñan la política en tres capas: cuota de tasa por inquilino para las operaciones interactivas (con un cubo cuyo máximo cubre un pico legítimo y una respuesta 429 con el tiempo de reintento), cola justa con tope de longitud para las importaciones masivas (con prioridad baja) y una regla de traslado: el cliente que supera durante dos semanas el triple de su cuota recibe una oferta de plan con aislamiento dedicado.

## Ejemplo

Ejemplo de [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md) (sección «Ejemplo mínimo»):

El planificador por turnos atiende a `b` aunque `a` tenga más trabajo: mientras `b` tenga pendientes, ninguno atiende dos veces seguidas. Es la idea de la cola justa en cinco líneas; el experimento la ejecuta con ocho clientes y 15 000 ticks.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Su límite es la memoria que ocupan las colas largas: sin un tope, un cliente puede agotar la memoria con sus pendientes, así que se combinan ambas políticas (cola justa con una cola máxima por cliente y rechazo más allá de ella). ([SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Inquilino](../i/inquilino.md), [Inquilino](../i/inquilino.md).
- **Ver también:** [Planificador](../p/planificador.md), [Contexto del inquilino](./contexto-del-inquilino.md), [Cubo de fichas](./cubo-de-fichas.md), [Cuota](./cuota.md), [Radio de impacto](../r/radio-de-impacto.md), [Silo, puente, pool](../s/silo-puente-pool.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Cola de trabajo](./cola-de-trabajo.md) · [Cola larga →](./cola-larga.md)
