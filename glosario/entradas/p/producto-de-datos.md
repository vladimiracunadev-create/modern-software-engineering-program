# Producto de datos

[↑ Glosario](../../README.md) · [← Producto](./producto.md) · [Producto operable →](./producto-operable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Conjunto de datos con dueño, contrato, calidad y nivel de servicio.

Definición de trabajo de [SE-343 — Data mesh y propiedad de los datos](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md).

## Por qué importa

En [SE-343 — Data mesh y propiedad de los datos](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md), el tema «Producto de datos» importa porque un conjunto de datos con contrato y nivel de servicio.

## Cómo funciona

Según [SE-343 — Data mesh y propiedad de los datos](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md):

**Fallo.** Un dominio publica un nuevo producto de datos. Dos semanas después, el equipo de finanzas descubre que sus informes de avisos leídos están mal desde hace diez días. El producto pasó todas las comprobaciones.

## Ejemplo

Ejemplo de [SE-343 — Data mesh y propiedad de los datos](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md) (sección «Caso conductor»):

*Avisos* publica «avisos enviados» como un producto de datos con dueño y contrato, y mide si baja el tiempo de acceso. `SE-344` toma la propiedad y la convierte en frontera de fallo: qué ocurre cuando uno de esos dominios, o un inquilino, falla y cuánto del sistema se lleva con él.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-343 — Data mesh y propiedad de los datos](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md)) son: La cola, la penalización de contexto, las derivas y los umbrales son construcciones del autor; la fórmula de Erlang C se usó solo como control de la simulación. No se midió ningún equipo de datos, ninguna plataforma ni la calidad de ningún lago, y el resultado «no ahorra personas» es del modelo, no de la práctica.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-547](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Contrato](../c/contrato.md), [Servicio](../s/servicio.md), [Contrato de datos](../c/contrato-de-datos.md), [Data mesh](../d/data-mesh.md), [Deriva semántica](../d/deriva-semantica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-343 — Data mesh y propiedad de los datos](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), [SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Producto](./producto.md) · [Producto operable →](./producto-operable.md)
