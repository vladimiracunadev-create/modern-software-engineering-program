# Conciliación

[↑ Glosario](../../README.md) · [← Concentración de conocimiento](./concentracion-de-conocimiento.md) · [Concurrencia →](./concurrencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

La **conciliación** es la comparación de dos fuentes del mismo hecho y la explicación de sus diferencias ([SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md)). En [SE-371](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md) se usa en un sentido más acotado: comparar totales (número de filas, importes) entre dos capas o fuentes de datos, para saber si lo que llegó coincide con lo que salió.

## Por qué importa

Dos sistemas que registran el mismo hecho (un cobro en el libro propio y en el informe del procesador de pagos) terminan por discrepar: por fallos, duplicados, retrasos o errores de configuración. La conciliación convierte esas discrepancias en algo medible y asignado, en vez de descubrirlas en el cierre contable. La decisión que cambia es tratar la consistencia entre fuentes como una verificación periódica con responsable, no como una suposición.

## Cómo funciona

[SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) describe una conciliación diaria en tres pasos:

1. **Descargar** el informe de liquidación del procesador.
2. **Comparar** con el libro por referencia y **clasificar** las diferencias: faltantes en cada lado, montos distintos, duplicados.
3. **Informar** con la antigüedad de cada diferencia.

Dos reglas hacen que sea operable. Las diferencias de menos de un centavo por redondeo se aceptan con un límite de diez al día; todas las demás generan una tarea con responsable. Y lo que no se puede resolver sin el procesador (una disputa pendiente) queda registrado con fecha y estado.

Las decisiones de modelado que la hacen posible vienen de la misma clase: los importes se guardan en la unidad mínima de la moneda (centavos) como enteros, porque la coma flotante binaria no representa exactamente 0,10 y acumula diferencias que, a escala, aparecen en la conciliación; y los asientos son inmutables, de modo que un error se corrige con un asiento nuevo que lo revierte, conservando el historial para auditar. [SE-371](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md) aplica la misma idea de contrastar totales entre capas de un flujo de datos.

## Ejemplo

En el caso de [SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md), la primera semana la conciliación encuentra tres cobros de un entorno de ensayo configurado contra producción. El equipo corrige la configuración y añade una comprobación al despliegue. Al mes, el cierre pasa de dos días de investigación a unas horas, y la brecha media sin explicar baja a cero. Son resultados del escenario construido en la clase, no una medición general.

## Errores y confusiones comunes

- **Guardar importes como decimales binarios**: acumulan diferencias; se usan enteros en la unidad mínima.
- **Corregir editando el asiento**: se pierde la auditoría; se corrige con un asiento nuevo.
- **Aceptar cualquier diferencia pequeña sin límite**: debe haber un tope diario.
- **Confundir conciliar con igualar**: lo esencial es explicar, no forzar que coincidan.

## Límites y cuándo no aplica

Solo detecta diferencias entre las dos fuentes que se comparan: si ambas se equivocan igual, no lo ve. Exige una clave común (la referencia) y fuentes disponibles; donde falta una clave, un libro o una conciliación, no hay respuesta posible, como señala [SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md). Y lo que depende de un tercero (una disputa) no se resuelve comparando, solo se registra con estado.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), [SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md), [SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa](./capa.md), [Explicación](../e/explicacion.md), [Hecho](../h/hecho.md), [Acotar](../a/acotar.md), [Asiento](../a/asiento.md), [Autorización, captura, liquidación](../a/autorizacion-captura-liquidacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-371 — Taller: reparar un pipeline defectuoso](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (19 clases más lo mencionan; las que más):

[SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md), [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md), [SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md), [SE-363](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md), [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), [SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md), [SE-418](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md).

**Aparece en los casos de estudio:** [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Post Office Horizon](../../../casos/fallo/post-office-horizon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Concentración de conocimiento](./concentracion-de-conocimiento.md) · [Concurrencia →](./concurrencia.md)
