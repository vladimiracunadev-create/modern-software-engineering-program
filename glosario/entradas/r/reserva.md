# Reserva

[↑ Glosario](../../README.md) · [← Rerere](./rerere.md) · [Resiliencia declarada →](./resiliencia-declarada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Retención temporal de una unidad para un comprador, con vencimiento.

Definición de trabajo de [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md).

## Por qué importa

En [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md), el tema «Reserva con vencimiento» importa porque protege al que paga y puede bloquear a todos.

## Cómo funciona

Según [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md):

El **físico** es lo que hay en el almacén. El **reservado** es lo que está comprometido con pedidos en curso (reservas vivas más ventas pendientes de enviar). El **vendible** es lo que se puede ofrecer ahora: físico menos reservado menos un colchón de seguridad. Mezclarlos produce errores en ambos sentidos: mostrar «agotado» porque el físico está reservado por abandonos, o vender lo que está dañado o en tránsito. Cada operación (reservar, confirmar, enviar, recibir una devolución, ajustar por conteo) cambia números concretos y se registra como un movimiento con motivo, de modo que el inventario sea un libro y no solo un contador.

Según [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md):

El equipo de *Tablero* rediseña la tienda tras el lanzamiento fallido. Define los tres números de inventario y un movimiento por cada cambio (reserva, venta, envío, devolución, ajuste) con un motivo, y la operación de reserva como una actualización condicional con una restricción `CHECK` de respaldo. La reserva dura 3 minutos y se extiende 10 más mientras haya un pago en curso, con un trabajo que libera las vencidas cada 30 segundos. Antes de lanzar, una prueba de concurrencia lanza 300 compradores contra 50 unidades y comprueba tres cosas: pedidos aceptados igual a 50, ningún saldo negativo y ninguna unidad reservada más de 13 minutos.

## Ejemplo

Ejemplo de [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md) (sección «Ejemplo profesional»):

El equipo de *Tablero* rediseña la tienda tras el lanzamiento fallido. Define los tres números de inventario y un movimiento por cada cambio (reserva, venta, envío, devolución, ajuste) con un motivo, y la operación de reserva como una actualización condicional con una restricción `CHECK` de respaldo. La reserva dura 3 minutos y se extiende 10 más mientras haya un pago en curso, con un trabajo que libera las vencidas cada 30 segundos. Antes de lanzar, una prueba de concurrencia lanza 300 compradores contra 50 unidades y comprueba tres cosas: pedidos aceptados igual a 50, ningún saldo negativo y ninguna unidad reservada más de 13 minutos.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Pero una reserva que dura más que el pago bloquea el stock a quienes no pagarán. ([SE-418](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md), [SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Retención](./retencion.md), [Actualización condicional atómica](../a/actualizacion-condicional-atomica.md), [Captura](../c/captura.md), [Condición de carrera](../c/condicion-de-carrera.md), [Inventario físico / reservado / vendible](../i/inventario-fisico-reservado-vendible.md), [Reposición](./reposicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (96 clases más lo mencionan; las que más):

[SE-517](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md), [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md), [SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md), [SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Rerere](./rerere.md) · [Resiliencia declarada →](./resiliencia-declarada.md)
