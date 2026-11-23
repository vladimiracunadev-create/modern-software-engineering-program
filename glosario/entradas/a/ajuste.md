# Ajuste

[↑ Glosario](../../README.md) · [← Aislamiento del sistema operativo](./aislamiento-del-sistema-operativo.md) · [Ajuste fino →](./ajuste-fino.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Línea en una factura posterior que corrige lo que llegó tras el cierre.

Definición de trabajo de [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md).

## Por qué importa

La clase donde se define, [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), existe con este propósito: la clase existe para que conviertas «lo que el cliente usó» en un importe que el cliente pueda verificar, que contabilidad pueda conciliar y que sobreviva a que los mensajes se repitan, lleguen tarde o se pierdan.

## Cómo funciona

Según [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md):

Un evento tardío puede llegar en cualquier momento, pero la factura debe emitirse en una fecha. La práctica es una *ventana de gracia*: el periodo se cierra N horas después de su fin (por ejemplo 24 horas) y la factura se emite desde ahí. Los eventos que llegan después del cierre no cambian la factura emitida (es inmutable): se registran como ajuste en la factura siguiente, con su concepto. El borrador previo al cierre se puede recalcular las veces que haga falta porque es una consulta determinista sobre los eventos crudos; la factura emitida no.

Según [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md):

El equipo de *Tablero* rehace su medición de llamadas de API. Define la métrica («llamada autenticada que devolvió una respuesta distinta de 5xx, contada en el servidor»), el evento con su identificador estable (el identificador de petición asignado por el balanceador) y un almacén con clave única. Los agregados por cliente y hora se recalculan desde los eventos crudos cada noche y se comparan con los de la tubería en línea: la diferencia debe ser cero y si no, alerta. El periodo se cierra 24 horas después de su fin, y los eventos posteriores generan un ajuste.

## Ejemplo

Ejemplo de [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md) (sección «Ejemplo profesional»):

El equipo de *Tablero* rehace su medición de llamadas de API. Define la métrica («llamada autenticada que devolvió una respuesta distinta de 5xx, contada en el servidor»), el evento con su identificador estable (el identificador de petición asignado por el balanceador) y un almacén con clave única. Los agregados por cliente y hora se recalculan desde los eventos crudos cada noche y se comparan con los de la tubería en línea: la diferencia debe ser cero y si no, alerta. El periodo se cierra 24 horas después de su fin, y los eventos posteriores generan un ajuste.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Los eventos que llegan después del cierre no cambian la factura emitida (es inmutable): se registran como ajuste en la factura siguiente, con su concepto. ([SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Factura](../f/factura.md).
- **Ver también:** [Ventana de gracia](../v/ventana-de-gracia.md), [Deduplicación](../d/deduplicacion.md), [Evento de uso](../e/evento-de-uso.md), [Métrica facturable](../m/metrica-facturable.md), [Tiempo de ocurrencia / de procesamiento](../t/tiempo-de-ocurrencia-de-procesamiento.md), [Tramos graduales / por volumen](../t/tramos-graduales-por-volumen.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (70 clases más lo mencionan; las que más):

[SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), [SE-605](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md), [SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md), [SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md), [SE-388](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md), [SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Aislamiento del sistema operativo](./aislamiento-del-sistema-operativo.md) · [Ajuste fino →](./ajuste-fino.md)
