# Supresión

[↑ Glosario](../../README.md) · [← Supply chain mínima](./supply-chain-minima.md) · [Supuesto de vigilancia →](./supuesto-de-vigilancia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Borrado de los datos de una persona, incluidas sus copias derivadas.

Definición de trabajo de [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md).

## Por qué importa

En [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md), el tema «Supresión» importa porque el dato vive en copias derivadas.

## Cómo funciona

Según [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md):

La solicitud de supresión de un usuario exige encontrar todas sus copias. En el laboratorio, borrar al usuario 42 solo de la tabla de origen dejó datos en la tabla intermedia (1 fila), la tabla de eventos (3 filas), el almacén de variables (1 fila) y el archivo de exportación (1 línea). Propagar el borrado por el linaje de tablas (`SE-367`) limpió las cuatro tablas, y quedó solo la copia del archivo exportado, que no es una tabla y no aparece en el grafo.

Según [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md):

El equipo de *Avisos* hace el inventario de datos personales de su plataforma. Ejecuta el clasificador por contenido sobre las veinte tablas más usadas y encuentra seis columnas con correos o teléfonos que el nombre no delataba, dos de ellas en campos de texto libre. Marca cada una en el catálogo con dueño, plazo y base de tratamiento, y cambia la ingesta para seudonimizar con HMAC antes de la zona intermedia. Antes de entregar estadísticas a un investigador, calcula los grupos pequeños y generaliza el año de nacimiento a década. Para las solicitudes de supresión escribe un procedimiento que recorre el linaje de tablas, borra por seudónimo en cada una y lista las copias exportadas con su plazo de retirada.

## Ejemplo

Ejemplo de [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* hace el inventario de datos personales de su plataforma. Ejecuta el clasificador por contenido sobre las veinte tablas más usadas y encuentra seis columnas con correos o teléfonos que el nombre no delataba, dos de ellas en campos de texto libre. Marca cada una en el catálogo con dueño, plazo y base de tratamiento, y cambia la ingesta para seudonimizar con HMAC antes de la zona intermedia. Antes de entregar estadísticas a un investigador, calcula los grupos pequeños y generaliza el año de nacimiento a década.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Por eso el catálogo debe registrar las exportaciones como activos con dueño y plazo, y por eso el plazo de una supresión incluye las copias de seguridad, que esta prueba no modeló: suelen purgarse por el ciclo de rotación, no por borrado inmediato, y eso debe declararse. ([SE-369](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md), [SE-368](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md), [SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md), [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cuasi-identificador](../c/cuasi-identificador.md), [Dato personal](../d/dato-personal.md), [HMAC](../h/hmac.md), [K-anonimato](../k/k-anonimato.md), [Retención](../r/retencion.md), [Seudonimización](./seudonimizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-358](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md), [SE-100](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Supply chain mínima](./supply-chain-minima.md) · [Supuesto de vigilancia →](./supuesto-de-vigilancia.md)
