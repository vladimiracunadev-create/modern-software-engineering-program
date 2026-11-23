# Asiento

[↑ Glosario](../../README.md) · [← Aserción semántica](./asercion-semantica.md) · [Asiento de doble entrada →](./asiento-de-doble-entrada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Movimiento contable con apuntes cuyos débitos y créditos suman lo mismo.

Definición de trabajo de [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md).

## Por qué importa

En [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md), el tema «Libro inmutable» importa porque la corrección es un asiento nuevo, no una edición.

## Cómo funciona

Según [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md):

En un libro de partida doble cada movimiento (un *asiento*) afecta como mínimo a dos cuentas, con débitos y créditos que suman lo mismo. Un cobro de 49,00 con una comisión de 1,72 se registra así: débito a «procesador por cobrar» 47,28, débito a «comisiones» 1,72, crédito a «ingresos» 49,00. Los totales de ambos lados son iguales; si alguien intenta registrar uno que no (`100` contra `90`), la función de registro lo rechaza (en el experimento, «asiento desbalanceado»). La propiedad que se obtiene es que **la suma de todos los débitos es igual a la suma de todos los créditos, siempre**, y por tanto cualquier error que rompa esa igualdad se detecta de inmediato.

Según [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md):

El equipo de *Tablero* ordena su manejo del dinero en tres capas. Primero, la clave de idempotencia: cada operación de cobro usa `renovacion:{cliente}:{periodo}`, y el almacén de claves guarda la solicitud (con un resumen de los parámetros), el estado y la respuesta; un reintento con la misma clave y los mismos parámetros devuelve lo guardado y con parámetros distintos devuelve un error. Segundo, el libro: plan de siete cuentas (por cobrar del procesador, caja, ingresos de suscripción, ingresos de uso, comisiones, reembolsos, disputas), asientos con la referencia del procesador como clave única y una prueba que recorre todos los eventos del procesador de un mes de ensayo y comprueba que cada uno tiene su asiento.

## Ejemplo

Ejemplo de [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) (sección «Ejemplo mínimo»):

Registrar el mismo cobro dos veces no crea un segundo asiento; un asiento desbalanceado se rechaza antes de tocar la base; y el reembolso deja las tres cuentas en cero con dos asientos conservados en el historial. Todo ocurre en una transacción en una base real, para que un fallo no deje un asiento sin apuntes.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Los totales de ambos lados son iguales; si alguien intenta registrar uno que no (`100` contra `90`), la función de registro lo rechaza (en el experimento, «asiento desbalanceado»). ([SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Autorización, captura, liquidación](./autorizacion-captura-liquidacion.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Conciliación](../c/conciliacion.md), [Contracargo](../c/contracargo.md), [Liquidación](../l/liquidacion.md), [Partida doble](../p/partida-doble.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-418](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md), [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md), [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md), [SE-416](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md), [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Aserción semántica](./asercion-semantica.md) · [Asiento de doble entrada →](./asiento-de-doble-entrada.md)
