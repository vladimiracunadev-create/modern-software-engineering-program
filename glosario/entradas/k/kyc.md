# KYC

[↑ Glosario](../../README.md) · [← KS](./ks.md) · [Lago →](../l/lago.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Verificación de la identidad de quien recibe pagos.

Definición de trabajo de [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md).

## Por qué importa

La clase donde se define, [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md), existe con este propósito: la clase existe para que entiendas qué cambia cuando un producto deja de servir a un tipo de cliente y pasa a conectar a dos o más tipos que se necesitan entre sí: compradores y vendedores, huéspedes y anfitriones, quienes piden un viaje y quienes lo ofrecen.

## Cómo funciona

Según [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md):

Cuando la plataforma recibe el pago del comprador y lo entrega después al vendedor, mantiene dinero ajeno durante un tiempo. En muchas jurisdicciones eso es una actividad regulada (servicios de pago, custodia, transmisión de dinero) que exige licencias, verificación de identidad de los vendedores (conoce a tu cliente, KYC) y reportes fiscales. La solución habitual es delegar a un proveedor autorizado que ofrece cuentas conectadas, verificación y reparto, como Stripe Connect, y limitarse a modelar el flujo. Esto no elimina responsabilidades: sigue siendo la plataforma quien define el reparto, quien decide cuándo liberar y quien responde ante el cliente. Antes de lanzar, se consulta con asesoría legal local qué actividad se realiza y qué licencias aplican; el curso no sustituye esa asesoría.

Según [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md):

Para el dinero, el equipo delega en un proveedor de cuentas conectadas: la plataforma crea las cuentas de los autores con verificación de identidad, cobra al comprador, retiene los fondos siete días y libera descontando comisión y costo del procesador. Fija un mínimo de 5,00 por plantilla para que el costo fijo del procesador no deje al autor menos del 80 %, y muestra al autor el reparto exacto antes de publicar. Define la política de disputa (reembolso automático si la plantilla no abre; revisión humana si la causa es subjetiva), un canal para reportar copias y un registro de decisiones de moderación.

## Ejemplo

Ejemplo de [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md) (sección «Ejemplo profesional»):

Para el dinero, el equipo delega en un proveedor de cuentas conectadas: la plataforma crea las cuentas de los autores con verificación de identidad, cobra al comprador, retiene los fondos siete días y libera descontando comisión y costo del procesador. Fija un mínimo de 5,00 por plantilla para que el costo fijo del procesador no deje al autor menos del 80 %, y muestra al autor el reparto exacto antes de publicar. Define la política de disputa (reembolso automático si la plantilla no abre; revisión humana si la causa es subjetiva), un canal para reportar copias y un registro de decisiones de moderación.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md)) son: Se simuló la liquidez con semilla 34 y se calculó el reparto con porcentajes del autor; no se midió ningún mercado, no se modelaron efectos de red completos ni precios, y el flujo del dinero es un diseño sin dinero real. Las obligaciones regulatorias dependen de cada jurisdicción y no se resuelven aquí.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md), [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-415](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Verificación](../v/verificacion.md), [Arranque en frío](../a/arranque-en-frio.md), [Comisión](../c/comision.md), [Custodia](../c/custodia.md), [Desintermediación](../d/desintermediacion.md), [Efecto de red cruzado](../e/efecto-de-red-cruzado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← KS](./ks.md) · [Lago →](../l/lago.md)
