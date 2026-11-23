# Custodia

[↑ Glosario](../../README.md) · [← Cursor](./cursor.md) · [Custodio →](./custodio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Retención de fondos por un tercero hasta que se cumple una condición.

Definición de trabajo de [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md).

## Por qué importa

La clase donde se define, [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md), existe con este propósito: la clase existe para que entiendas qué cambia cuando un producto deja de servir a un tipo de cliente y pasa a conectar a dos o más tipos que se necesitan entre sí: compradores y vendedores, huéspedes y anfitriones, quienes piden un viaje y quienes lo ofrecen.

## Cómo funciona

Según [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md):

Comprar a un desconocido es arriesgado: puede no entregar, entregar algo distinto o no funcionar. Las plataformas construyen confianza con capas: verificación de identidad de quien vende, reseñas bidireccionales con reglas contra manipulación, pagos protegidos (el dinero se retiene hasta que se confirma), garantías o políticas de reembolso y un canal de disputa. Según los casos del curso, Mercado Pago nació como producto de custodia para dar confianza en pagos entre desconocidos, y Airbnb construyó pronto un sistema de pagos propio, reseñas y una garantía económica para anfitriones. En ambos casos el producto central del mercado es la reducción de la incertidumbre entre las partes, y la técnica (búsqueda, pagos, reseñas) se evalúa por cuánto la reduce.

Según [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md):

Habitualmente no es una buena idea y puede ser ilegal sin licencia: mantener fondos ajenos es una actividad regulada. La práctica común es delegar la custodia y el reparto a un proveedor autorizado. Consulta asesoría legal local antes de decidirlo.

## Ejemplo

Ejemplo de [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md) (sección «Caso conductor»):

*Tablero* lanzó «Plantillas» con 14 plantillas y comprobó que el buscador no era el problema. Esta clase da el modelo de liquidez, el reparto del dinero y el flujo de custodia, y conecta con los casos del curso: Airbnb (arranque lento y confianza), Mercado Libre (custodia como origen de un ecosistema de pagos) y Uber (más de dos lados y la diferencia entre ventas brutas e ingresos). `SE-417` toma el dinero que la plataforma retiene y reparte y lo registra con idempotencia y conciliación.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md)) son: Se simuló la liquidez con semilla 34 y se calculó el reparto con porcentajes del autor; no se midió ningún mercado, no se modelaron efectos de red completos ni precios, y el flujo del dinero es un diseño sin dinero real. Las obligaciones regulatorias dependen de cada jurisdicción y no se resuelven aquí.

## Relación con otros conceptos

- **Prerrequisito:** [Retención](../r/retencion.md).
- **Ver también:** [Condición](./condicion.md), [Arranque en frío](../a/arranque-en-frio.md), [Comisión](./comision.md), [Desintermediación](../d/desintermediacion.md), [Efecto de red cruzado](../e/efecto-de-red-cruzado.md), [KYC](../k/kyc.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (12 clases más lo mencionan; las que más):

[SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md), [SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-202](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md), [SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md), [SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md), [SE-358](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md), [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md).

**Aparece en los casos de estudio:** [Mercado Libre](../../../casos/exito/mercado-libre.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «escrow».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Cursor](./cursor.md) · [Custodio →](./custodio.md)
