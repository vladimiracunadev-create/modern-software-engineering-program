# Grandfathering

[↑ Glosario](../../README.md) · [← Grafo de dependencias](./grafo-de-dependencias.md) · [Granularidad →](./granularidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Conservar para clientes existentes condiciones que ya no se ofrecen.

Definición de trabajo de [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md): Conservar condiciones anteriores a clientes existentes.

## Por qué importa

La clase donde se define, [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md), existe con este propósito: la clase existe para que separes tres cosas que casi todos los productos SaaS mezclan en la misma tabla o, peor, en el mismo `if`: el *plan* (un paquete comercial que se vende), el *derecho* (lo que una cuenta concreta puede hacer hoy, con límites y vencimientos) y la *bandera de funcionalidad* (un interruptor operativo que decide qué código se ejecuta).

## Cómo funciona

Según [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md):

Subir es sencillo: los derechos se amplían en cuanto el pago se confirma (`SE-412`). Bajar es difícil porque la cuenta puede exceder los límites del plan nuevo (18 usuarios en un plan de 3). Las políticas posibles son: impedir la bajada hasta que la cuenta cumpla, aplicarla al fin del ciclo y avisar con tiempo, o aplicarla y conservar lo existente en modo solo lectura y sin permitir crear más (*grandfathering* parcial). Cualquiera es válida si está escrita, se muestra antes de confirmar y se prueba. Lo que no es válido es no decidir: sin política, la cuenta conserva derechos que no paga o pierde datos sin aviso.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md):

*Escenario ilustrativo: las cifras y los resultados de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Las políticas posibles son: impedir la bajada hasta que la cuenta cumpla, aplicarla al fin del ciclo y avisar con tiempo, o aplicarla y conservar lo existente en modo solo lectura y sin permitir crear más (*grandfathering* parcial). ([SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md), [SE-475](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Bandera de funcionalidad](../b/bandera-de-funcionalidad.md), [Cambio de plan](../c/cambio-de-plan.md), [Cuota](../c/cuota.md), [Derecho](../d/derecho.md), [Disposición a pagar](../d/disposicion-a-pagar.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Grafo de dependencias](./grafo-de-dependencias.md) · [Granularidad →](./granularidad.md)
