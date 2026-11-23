# Liquidación

[↑ Glosario](../../README.md) · [← Linter](./linter.md) · [Liquidez →](./liquidez.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Informe y transferencia de fondos que el procesador entrega tras descontar comisiones.

Definición de trabajo de [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md).

## Por qué importa

La clase donde se define, [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md), existe con este propósito: la clase existe para que construyas la parte del sistema donde un error cuesta dinero de verdad y casi nunca se ve en el momento: cobrar sin duplicar, registrar cada movimiento de modo que siempre cuadre y comprobar periódicamente que lo que dice tu libro es lo que el procesador y el banco dicen.

## Cómo funciona

Según [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md):

Tu libro dice qué crees que ocurrió; el informe de liquidación del procesador, qué se movió; el extracto bancario, qué llegó. La conciliación los compara por una clave común (el identificador del cobro) y clasifica las diferencias: **en tu libro y no en la liquidación** (cobros pendientes, retenidos o fallidos), **en la liquidación y no en el libro** (cobros que tu sistema no conoce), **con importes distintos** (disputas, reembolsos parciales, comisiones) y **duplicados**. En el experimento, de 500 cobros: uno estaba en el libro sin liquidar (1 815 centavos), uno tenía un monto distinto (500), uno estaba en la liquidación y no en el libro (4 728), y un asiento estaba repetido (4 728).

Según [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md):

Tercero, la conciliación diaria: un trabajo descarga el informe de liquidación, lo compara con el libro por referencia, clasifica las diferencias (faltantes en cada lado, montos distintos, duplicados) y escribe un informe con la antigüedad de cada una. Las diferencias de menos de un centavo por redondeo se aceptan con un límite de diez al día; todas las demás generan una tarea con responsable. La primera semana encuentra tres cobros de un entorno de ensayo configurado contra producción; el equipo corrige la configuración y añade una comprobación al despliegue. Al mes, el cierre pasa de dos días de investigación a unas horas, y la brecha media sin explicar baja a cero. Lo que no pueden resolver sin el procesador (una disputa pendiente) queda registrado con fecha y estado.

## Ejemplo

Ejemplo de [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) (sección «Ejemplo profesional»):

Tercero, la conciliación diaria: un trabajo descarga el informe de liquidación, lo compara con el libro por referencia, clasifica las diferencias (faltantes en cada lado, montos distintos, duplicados) y escribe un informe con la antigüedad de cada una. Las diferencias de menos de un centavo por redondeo se aceptan con un límite de diez al día; todas las demás generan una tarea con responsable. La primera semana encuentra tres cobros de un entorno de ensayo configurado contra producción; el equipo corrige la configuración y añade una comprobación al despliegue.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **en tu libro y no en la liquidación** (cobros pendientes, retenidos o fallidos), **en la liquidación y no en el libro** (cobros que tu sistema no conoce), **con importes distintos** (disputas, reembolsos parciales, comisiones) y **duplicados**. ([SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md))
- **Fallo.** La conciliación diaria reporta 41 cobros «en la liquidación y no en el libro» cada lunes, siempre por importes parecidos. ([SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Comisión](../c/comision.md).
- **Ver también:** [Transferencia](../t/transferencia.md), [Asiento](../a/asiento.md), [Autorización, captura, liquidación](../a/autorizacion-captura-liquidacion.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Conciliación](../c/conciliacion.md), [Contracargo](../c/contracargo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-416](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md), [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Knight Capital](../../../casos/fallo/knight-capital.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Linter](./linter.md) · [Liquidez →](./liquidez.md)
