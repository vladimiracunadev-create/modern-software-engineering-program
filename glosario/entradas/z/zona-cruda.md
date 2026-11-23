# Zona cruda

[↑ Glosario](../../README.md) · [← Zona](./zona.md) · [Zona gris →](./zona-gris.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Copia del dato tal como llegó, sin transformar.

Definición de trabajo de [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md).

## Por qué importa

En [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), el tema «Capas» importa porque la zona cruda permite corregir lo posterior.

## Cómo funciona

Según [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md):

La zona cruda guarda el dato como llegó, con su fecha de carga y su origen. La zona intermedia resuelve tipos, zonas horarias, duplicados y nombres. El modelo analítico reorganiza en hechos y dimensiones con la granularidad correcta. La razón de esta cadena no es el orden estético: es que cada transformación puede equivocarse y la corrección exige volver a empezar desde algo que no se haya tocado. Quien transforma al ingerir y descarta el original pierde esa posibilidad. El costo es almacenamiento y la disciplina de tratar la zona cruda como solo de lectura para todos salvo el proceso de ingesta.

Según [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md):

El equipo de *Avisos* recibe tres peticiones de datos en el mismo mes. En lugar de abrir tres informes a medida, dibuja la tabla de preguntas: cada una con las filas que toca, las columnas que usa, si necesita historia y con qué frecuencia se repite. Dos de las tres necesitan historia que la base ya perdió, y una se repite cada hora. Con esa tabla, el equipo propone un piloto acotado: conservar desde hoy los cambios de estado de avisos en una tabla de eventos, copiar cada noche a una zona cruda y construir un solo modelo analítico con granularidad de un aviso por día. No promete responder el pasado ya perdido; lo declara como pérdida irrecuperable y fija desde cuándo habrá respuesta.

## Ejemplo

Ejemplo de [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* recibe tres peticiones de datos en el mismo mes. En lugar de abrir tres informes a medida, dibuja la tabla de preguntas: cada una con las filas que toca, las columnas que usa, si necesita historia y con qué frecuencia se repite. Dos de las tres necesitan historia que la base ya perdió, y una se repite cada hora. Con esa tabla, el equipo propone un piloto acotado: conservar desde hoy los cambios de estado de avisos en una tabla de eventos, copiar cada noche a una zona cruda y construir un solo modelo analítico con granularidad de un aviso por día.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El costo es almacenamiento y la disciplina de tratar la zona cruda como solo de lectura para todos salvo el proceso de ingesta. ([SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa](../c/capa.md), [Carga analítica](../c/carga-analitica.md), [Carga operacional](../c/carga-operacional.md), [Estado actual](../e/estado-actual.md), [Extracción](../e/extraccion.md), [Interferencia](../i/interferencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md), [SE-368](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md), [SE-369](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Zona](./zona.md) · [Zona gris →](./zona-gris.md)
