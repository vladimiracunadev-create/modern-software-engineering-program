# Función de aptitud

[↑ Glosario](../../README.md) · [← Función](./funcion.md) · [Función de aptitud arquitectónica →](./funcion-de-aptitud-arquitectonica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Comprobación automática de una propiedad arquitectónica.

Definición de trabajo de [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md).

## Por qué importa

En [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md), el tema «Función de aptitud» importa porque protege contra la deriva silenciosa.

## Cómo funciona

Según [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md):

Cada estilo tiene restricciones que la deriva erosiona: en un monolito modular, que el dominio no importe la infraestructura y que no haya ciclos entre módulos; en un microkernel, que los complementos no importen el interior del núcleo. Una función de aptitud es una prueba automática que comprueba la restricción en cada integración. En el laboratorio se escribió una con el módulo `ast`: construye el grafo de importaciones de un paquete con tres capas (dominio, aplicación e infraestructura), comprueba que ninguna capa importe una superior y busca ciclos con un algoritmo de componentes fuertemente conexos.

Según [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md):

Un año después de la decisión, la persona nueva del equipo de *Avisos* propone separar el cálculo en un servicio. La líder abre el ADR y la conversación cambia: el disparador de p99 no se ha cumplido (el máximo del año es 171 ms), pero el número de equipos es ahora cinco, y el registro decía que con más de tres equipos la coordinación supera el umbral. La discusión deja de ser «monolito o servicios» y pasa a ser «la consecuencia negativa que aceptamos se materializó».

## Ejemplo

Ejemplo de [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md) (sección «Ejemplo profesional»):

Un año después de la decisión, la persona nueva del equipo de *Avisos* propone separar el cálculo en un servicio. La líder abre el ADR y la conversación cambia: el disparador de p99 no se ha cumplido (el máximo del año es 171 ms), pero el número de equipos es ahora cinco, y el registro decía que con más de tres equipos la coordinación supera el umbral. La discusión deja de ser «monolito o servicios» y pasa a ser «la consecuencia negativa que aceptamos se materializó».

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md)) son: El analizador, la función de aptitud y la serie son herramientas del autor sobre registros y un paquete de juguete; no se evaluó ningún ADR real ni se ejecutó ninguna herramienta de terceros. La conclusión de que un ADR con estas características mejora las decisiones no se midió.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Comprobación automática](../c/comprobacion-automatica.md), [Propiedad](../p/propiedad.md), [ADR](../a/adr.md), [Consecuencia negativa](../c/consecuencia-negativa.md), [Deriva arquitectónica](../d/deriva-arquitectonica.md), [Disparador de revisión](../d/disparador-de-revision.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-346](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Función](./funcion.md) · [Función de aptitud arquitectónica →](./funcion-de-aptitud-arquitectonica.md)
